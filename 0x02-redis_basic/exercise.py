#!/usr/bin/env python3
"""Writing string to redis"""

import redis
import uuid


class Cache:
    """Cache class for Redis instance"""
    def __init__(self):
        """Initialise Redis client"""
        self._redis = redis.Redis()

    def store(self, data: any) -> str:
        """Store data and generate random key"""
        rand_key = str(uuid.uuid4())
        self._redis.set(rand_key, data)
        return rand_key
