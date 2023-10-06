import redis

from typing import Optional

r = redis.Redis(host='redis', port=6379, decode_responses=True)

def redis_get(key: str):
    return r.get(key)

def redis_set(key: str, value, expire: Optional[int]):
    if expire:
        r.set(key, value, ex=expire)
    else:
        r.set(key, value)