# e2hapi/client.py

from elasticsearch import Elasticsearch
from elasticsearch.exceptions import RequestError
import re
import json
import urllib3
import logging

urllib3.disable_warnings()

# Configurer le logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class E2hApiClient:
    def __init__(self, api_key: str, host="api.e2hbase.shop"):
        """
        Initialise le client Elasticsearch avec la clé API et l'hôte spécifiés.

        :param api_key: La clé API pour accéder à Elasticsearch.
        :param host: L'hôte Elasticsearch (par défaut : "api.e2hbase.shop").
        """
        self.host = host
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

    def search_documents(self, search_string):
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
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")

    @staticmethod
    def extract_information(text):
        """
        Extrait les e-mails, numéros de téléphone, identifiants Steam et licences FiveM du texte fourni.

        :param text: Le texte à analyser.
        :return: Dictionnaire contenant les e-mails, numéros de téléphone, identifiants Steam et licences FiveM.
        """
        email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        phone_pattern = r"\+?\d[\d -]{8,}\d"
        steam_pattern = r"steam:\w{17}"
        license_pattern = r"license:\w{32}"

        emails = re.findall(email_pattern, text)
        phones = re.findall(phone_pattern, text)
        steam_ids = re.findall(steam_pattern, text)
        fivem_licenses = re.findall(license_pattern, text)

        return {
            "emails": emails,
            "phones": phones,
            "fivem_licenses": fivem_licenses,
            "steam_ids": steam_ids,
        }

    @staticmethod
    def format_phone_number(number):
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

    def process_search_results(self, documents):
        """
        Traite les résultats de la recherche pour extraire les informations spécifiques.

        :param search_string: La chaîne de recherche utilisée pour trouver les documents.
        :return: Dictionnaire contenant les e-mails, numéros de téléphone, identifiants Steam et licences FiveM trouvés.
        """
        all_information = {
            "emails": [],
            "phones": [],
            "fivem_licenses": [],
            "steam_ids": [],
        }

        if documents:
            for doc in documents:
                source = doc["_source"]
                content = source.get("content", "")

                info = self.extract_information(content)

                all_information["emails"].extend(info["emails"])
                all_information["phones"].extend(info["phones"])
                all_information["fivem_licenses"].extend(info["fivem_licenses"])
                all_information["steam_ids"].extend(info["steam_ids"])

                if isinstance(content, str):
                    try:
                        data = json.loads(content)
                        if isinstance(data, dict):
                            identifiers = data.get("identifiers", [])
                            for identifier in identifiers:
                                if identifier.startswith("steam:"):
                                    all_information["steam_ids"].append(identifier)
                                elif identifier.startswith("license:"):
                                    all_information["fivem_licenses"].append(identifier)
                    except json.JSONDecodeError:
                        logging.error(f"JSON decoding error for content: {content}")
                    except TypeError:
                        logging.error(f"Type error while processing content: {content}")

        all_information["phones"] = [
            self.format_phone_number(phone) for phone in all_information["phones"]
        ]

        return all_information
