#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pip install txtai

from txtai.embeddings import Embeddings

embeddings = Embeddings(path="sentence-transformers/nli-mpnet-base-v2")
embeddings.index(["Correct", "Not what we hoped"])
embeddings.search("positive", 1)

