
from elasticsearch import Elasticsearch
from dotenv import load_dotenv
import os
import elasticsearch
import logging
#import yaml

load_dotenv()

class ElasticsearchConnector:
    def __init__(self) -> None:
        self.es_client = None
        self.connect()

    def connect(self):
        es = es = Elasticsearch("http://localhost:9200")
        print(es.info().body)
        self.es_client = es

    def create_index(self, index_name, mapping=None):
        try:
            if mapping:
                pass
                # with open('config.yml', 'r') as file:
                #     mappings = yaml.safe_load(file)
                return self.es_client.indices.create(index=index_name, mappings=mappings)
            else:
                return self.es_client.indices.create(index=index_name)
        except Exception as e:
            logging.error(e)

        
    def insert_document(self, index_name, document_id, document):
        try:
            return self.es_client.index(index=index_name, id=document_id, body=document)
        except Exception as e:
            logging.error(e)

    def get_data(self, index_name, search_query, size=os.getenv("ES_RETRIEVAL_SIZE")): 
        try:
            result = self.es_client.search(index=index_name, body=search_query, allow_partial_search_results=True,
                                           size=size, request_timeout=120)
            return result
        except Exception as e:
            logging.error(e)


