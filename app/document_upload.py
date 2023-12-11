# based on 1) https://medium.com/@pritam7798sonawane/building-a-text-search-application-with-elasticsearch-and-fastapi-14ea78cf1890;
# and 2) https://dylancastillo.co/elasticsearch-python/
from es_connector import ElasticsearchConnector
import uuid
import os
from dotenv import load_dotenv
import pandas as pd
from elasticsearch.helpers import bulk
import logging
logging.getLogger().setLevel(logging.INFO)


load_dotenv()

es = ElasticsearchConnector(indocker=False)

"""
To index, change es url in .env file!
"""

es.create_es_index_with_mapping(os.getenv("ES_MOVIES_INDEX_NAME"), os.getenv("ES_MAPPING_CHAT_FILE"))

df = (
    pd.read_csv("data/wiki_movie_plots_deduped.csv")
    .dropna()
    .sample(5000, random_state=42)
    .reset_index()
)

# Upload documents to Elasticsearch with text embeddings
bulk_data = []
for i, row in df.iterrows():
    doc = {
        "title": row["Title"],
        "ethnicity": row["Origin/Ethnicity"],
        "director": row["Director"],
        "cast": row["Cast"],
        "genre": row["Genre"],
        "plot": row["Plot"],
        "year": row["Release Year"],
        "wiki_page": row["Wiki Page"]
    }

    bulk_data.append(
        {
            "_op_type": "index",
            "_index": os.getenv("ES_MOVIES_INDEX_NAME"),
            "_id": uuid.uuid4(),
            "_source": doc
        }
    )
    if i % 500 == 0:
        logging.info(f"Processing document {i}")
        # bulk upload to index
        bulk(client=es.es_client, actions=bulk_data)
        bulk_data = []
