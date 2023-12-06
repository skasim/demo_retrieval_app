import os, sys
sys.path.append(os.path.abspath("."))
from app.es_connector import ElasticsearchConnector
import os
from dotenv import load_dotenv
import uuid
import json
from elasticsearch.helpers import bulk
import logging
logging.getLogger().setLevel(logging.INFO)

load_dotenv()

# create index
es = ElasticsearchConnector()
print(es.es_client.info().body)
es.create_es_index_with_mapping("chitchat", os.getenv("ES_MAPPING_CHAT_FILE"))


# read data file
# with open("data/dummy_chat_data.json") as f:
#     data = json.load(f)

# bulk_data = []
# for item in data:
#     doc = {
#         "comment": item["sentence"],
#         "timestamp": item["timestamp"]
#     }

#     bulk_data.append(
#         {
#             "_op_type": "index",
#             "_index": os.getenv("ES_MOVIES_INDEX_NAME"),
#             "_id": uuid.uuid4(),
#             "_source": doc
#         }
#     )

# # bulk upload to index
# bulk(client=es.es_client, actions=bulk_data)
