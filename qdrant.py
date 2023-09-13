#!/usr/bin/env python
# -*- coding: utf-8 -*-

from qdrant_client import QdrantClient

client = QdrantClient(":memory:") # Create in-memory Qdrant instance, for testing, CI/CD
# client = QdrantClient(path="path/to/db")  # Persists changes to disk, fast prototyping


# Prepare your documents, metadata, and IDs
docs = ["Qdrant has Langchain integrations", "Qdrant also has Llama Index integrations"]
metadata = [
    {"source": "Langchain-docs"},
    {"source": "Linkedin-docs"},
]
ids = [42, 2]

# Use the new add method
client.add(
    collection_name="demo_collection",
    documents=docs,
    metadata=metadata,
    ids=ids
)

search_result = client.query(
    collection_name="demo_collection",
    query_text="This is a query document"
)
print(f'--- {search_result=}')


