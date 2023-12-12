#!/usr/bin/env python3
"""Module holds the list_all method"""

def list_all(mongo_collection):
    """list all documents in collection"""
    if mongo_collection:
        return list(mongo_collection.find())
    return []
