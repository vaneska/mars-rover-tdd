from email.policy import default

from pydantic import BaseSettings, Field, RedisDsn

import redis


class RedisConfig(BaseSettings):
    REDIS_DSN: RedisDsn = Field(default="redis://mars-redis:6379/1", env="REDIS_DSN")


def get_instance() -> redis.Redis:
    return redis.from_url(RedisConfig().REDIS_DSN)
