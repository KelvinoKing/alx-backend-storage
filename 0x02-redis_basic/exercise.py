#!/usr/bin/env python3
"""
Create a Cache class. In the __init__ method, store an instance of the
Redis client as a private variable named _redis (using redis.Redis())
and flush the instance using flushdb.
Create a store method that takes a data argument and returns a string.
The method should generate a random key (e.g. using uuid), store the input
data in Redis using the random key and return the key.
"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_call(method: Callable) -> Callable:
    """
    Count call decorator
    """
    @wraps(method)
    def invoker(self, *args, **kwargs) -> any:
        """
        invoke method
        """
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return invoker


class Cache:
    """
    Cache class
    """
    def __init__(self):
        """
        Constructor
        """
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store method
        """
        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        return data_key

    def get(
            self,
            key: str,
            fn: Callable = None,
            ) -> Union[str, bytes, int, float]:
        """
        Get method
        """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
        Get string method
        """
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """
        Get int method
        """
        return self.get(key, int)
