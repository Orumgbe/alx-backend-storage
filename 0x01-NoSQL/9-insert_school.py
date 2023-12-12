#!/usr/bin/env python3
"""This module holds the 'insert_school' method"""

def insert_school(mongo_collection, **kwargs):
    """Inserts document into a collection"""
    if mongo_collection:
        if len(kwargs) == 0:
            return None
        return mongo_collection.insert(kwargs)
