#!/usr/bin/env python3
"""Script that provides stats about Nginx logs in MongoDB"""

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx
    print("{} logs".format(logs_collection.estimated_document_count()))
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = logs_collection.count_documents({'method': method})
        print("\tmethod {}: {}".format(method, count))
    status_get = logs_collection.count_documents({'method': 'GET',
                                                 'path': "/status"})
    print("{} status check".format(status_get))
