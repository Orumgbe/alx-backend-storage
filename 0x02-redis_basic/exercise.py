#!/usr/bin/env python3
"""Writing string to redis"""

import redis
from typing import Union
import uuid


class Cache:
    """Cache class for Redis instance"""
    def __init__(self):
        """Initialise Redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data and generate random key"""
        rand_key = str(uuid.uuid4())
        self._redis.set(rand_key, data)
        return rand_key
