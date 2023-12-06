
from elasticsearch import Elasticsearch
from dotenv import load_dotenv
import os
import logging
import json

load_dotenv()

class ElasticsearchConnector:
    def __init__(self) -> None:
        self.es_client = None
        self.connect()


    def connect(self):
        try: 
            es = Elasticsearch(os.getenv("ES_URL"))
            logging.info(es.info().body)
            self.es_client = es
        except Exception as e:
            logging.error(f"Error while connecting to ES: {e}")


    def create_es_index_with_mapping(self, index_name: str, mapping_file: dict)-> None:
        try:
            if not self.es_client.indices.exists(index=index_name):
                with open(mapping_file) as f:
                    mapping = json.loads(f.read())
                    self.es_client.indices.create(index=index_name, mappings=mapping)
        except Exception as e:
            logging.error(f"Failed to create index {index_name}: {e}")


    def insert_document(self, index_name: str, _id: str, doc: dict)-> None:
        try:
            self.es_client.index(index=index_name, id=_id, document=doc)
        except Exception as e:
            logging.error(f"Failed to log document to index {index_name} with id {_id} and content {doc}: {e}")

    def update_document(self, index_name: str, _id: str, _doc: str)-> None:
        try:
            self.es_client.update(index=index_name, id=_id, doc=_doc)
        except Exception as e:
            logging.error(f"Failed to update document to index {index_name} with id {_id} and content {_doc}: {e}")
    

    def search_documents(self, index_name: str, _query: str):
        try:
            response = self.es_client.search(index=index_name, query=_query)
            return response
        except Exception as e:
            logging.error(f"Failed to search documents in index {index_name} with query {_query}: {e}")


    def delete_document(self, index_name: str, _id: str)-> None:
        try:
            self.es_client.delete(index=index_name, id=_id)
        except Exception as e:
            logging.error(f"Failed to delete document from index {index_name} with id {_id}: {e}")


