from elasticsearch import Elasticsearch
from elasticsearch.exceptions import RequestError
import re
import json
import urllib3
import logging

urllib3.disable_warnings()

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class E2hApiClient:
    def __init__(self, api_key: str):
        """
        Initialise le client Elasticsearch avec la clé API et l'hôte spécifiés.

        :param api_key: La clé API pour accéder à Elasticsearch.
        """
        self.host = "api.e2hbase.shop"
        self.api_key = api_key
        self.client = self._create_client()

    def _create_client(self):
        """
        Crée une instance du client Elasticsearch.

        :return: Instance du client Elasticsearch.
        :raises ValueError: Si la clé API n'est pas fournie.
        """
        if not self.api_key:
            raise ValueError("Please provide an API key!")
        return Elasticsearch(
            [f"https://{self.host}:9200"],
            api_key=self.api_key,
            verify_certs=False,
        )

    def search_documents(self, search_string) -> list:
        """
        Recherche des documents dans Elasticsearch en fonction de la chaîne de recherche fournie.
        :param search_string: La chaîne de recherche à utiliser dans la requête.
        :return: Liste des documents trouvés.
        :raises RequestError: Erreur liée à la requête Elasticsearch.
        :raises Exception: Erreur inattendue lors de la recherche.
        """
        search_query = {
            "match": {"content": search_string},
        }
        try:
            response = self.client.search(
                index="searcher", query=search_query, size=10000
            )
            return response["hits"]["hits"]
        except RequestError as e:
            logging.error(f"Request error: {e}")
            return []
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            return []

    @staticmethod
    def _extract_information(text):
        """
        Extrait les e-mails, numéros de téléphone, identifiants Steam et licences FiveM du texte fourni.

        :param text: Le texte à analyser.
        :return: Dictionnaire contenant les e-mails, numéros de téléphone, identifiants Steam et licences FiveM.
        """
        email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        phone_pattern = r"\+?\d{1,4}?[\d\s-]{8,}\d"
        steam_pattern = r"\bsteam:\w{17}\b"
        license_pattern = r"\blicense:\w{32}\b"

        emails = set(re.findall(email_pattern, text))
        phones = set(re.findall(phone_pattern, text))
        steam_ids = set(re.findall(steam_pattern, text))
        fivem_licenses = set(re.findall(license_pattern, text))

        return {
            "emails": emails,
            "phones": phones,
            "fivem_licenses": fivem_licenses,
            "steam_ids": steam_ids,
        }

    @staticmethod
    def _format_phone_number(number):
        """
        Formate un numéro de téléphone au format (XXX) XXX-XXXX.

        :param number: Le numéro de téléphone à formater.
        :return: Le numéro de téléphone formaté.
        """
        digits = re.sub(r"\D", "", number)
        if len(digits) < 10:
            return number
        formatted = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
        return formatted

    def process_search_results(self, documents) -> dict:
        """
        Traite les résultats de la recherche pour extraire les informations spécifiques.

        :param documents: Liste des documents trouvés.
        :return: Dictionnaire contenant les e-mails, numéros de téléphone, identifiants Steam et licences FiveM trouvés.
        """
        all_information = {
            "emails": set(),
            "phones": set(),
            "fivem_licenses": set(),
            "steam_ids": set(),
        }

        for doc in documents:
            source = doc.get("_source", {})
            content = source.get("content", "")

            info = self._extract_information(content)
            all_information["emails"].update(info["emails"])
            all_information["phones"].update(info["phones"])
            all_information["fivem_licenses"].update(info["fivem_licenses"])
            all_information["steam_ids"].update(info["steam_ids"])

            if isinstance(content, str):
                try:
                    data = json.loads(content)
                    if isinstance(data, dict):
                        identifiers = data.get("identifiers", [])
                        for identifier in identifiers:
                            if identifier.startswith("steam:"):
                                all_information["steam_ids"].add(identifier)
                            elif identifier.startswith("license:"):
                                all_information["fivem_licenses"].add(identifier)
                except json.JSONDecodeError:
                    logging.error(f"JSON decoding error for content: {content}")
                except TypeError:
                    logging.error(f"Type error while processing content: {content}")

        all_information["phones"] = [
            self._format_phone_number(phone) for phone in all_information["phones"]
        ]

        return {
            "emails": list(all_information["emails"]),
            "phones": all_information["phones"],
            "fivem_licenses": list(all_information["fivem_licenses"]),
            "steam_ids": list(all_information["steam_ids"]),
        }
