#!/usr/bin/env python3
"""This module contains the 'schools_by_topic method"""

def schools_by_topic(mongo_collection, topic):
    """Returns list of schools having a specific topic"""
    return [topic for topic in mongo_collection.find({"topics": topic})]
