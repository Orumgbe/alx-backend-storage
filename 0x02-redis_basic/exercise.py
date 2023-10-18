#!/usr/bin/env python3
"""Writing string to redis"""

import functools
import redis
from typing import Any, Callable, Optional, Union
import uuid


def count_calls(method: Callable) -> Callable:
    """Decorator to count number of calls"""
    @functools.wraps(method)    # Preserve metadata
    def wrapper(self, *args, **kwargs) -> Any:
        """Wrapper function to add incr functionality
           Save incr count to redis"""
        key = method.__qualname__
        self._redis.incr(key)
        result = method(self, *args, **kwargs)
        return result
    return wrapper


class Cache:
    """Cache class for Redis instance"""
    def __init__(self):
        """Initialise Redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data and generate random key"""
        rand_key = str(uuid.uuid4())
        self._redis.set(rand_key, data)
        return rand_key

    def get(self, key: str,
            fn: Optional[Callable[[str], Union[str, int]]] = None
            ) -> Union[bytes, str, int]:
        """Read and recover original type"""
        value = self._redis.get(key)
        if value is not None and fn is not None:
            return fn(value)
        return value

    def get_int(self, key: str) -> int:
        """Returns integer if original value type is int"""
        return self.get(key, fn=int)

    def get_str(self, key: str) -> str:
        """Returns string if original value type is str"""
        return self.get(key, fn=lambda d: d.decode("utf-8"))
