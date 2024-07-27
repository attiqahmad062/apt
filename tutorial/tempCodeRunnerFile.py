from elasticsearch import Elasticsearch

es = Elasticsearch(["http://localhost:9200"])

try:
    es.ping()
    print("Connected to Elasticsearch")
except Exception as e:
    print(f"Could not connect to Elasticsearch: {e}")
