import os
from dotenv import load_dotenv
import logging
logging.getLogger().setLevel(logging.INFO)
import sys
sys.path.append(".")
from app.es_connector import ElasticsearchConnector



load_dotenv()

es = ElasticsearchConnector(indocker=False)

"""
To index, change es url in .env file!
"""

es.create_es_index_with_mapping(os.getenv("KAFKA_TOPIC_CHITCHAT"), os.getenv("ES_MAPPING_MOVIES_FILE"))
