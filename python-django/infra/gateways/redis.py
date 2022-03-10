import redis


class RedisConfig:
    HOST: str = "mars-redis"
    PORT: int = 6379
    DB: int = 1


def get_instance() -> redis.Redis:
    return redis.Redis(host=RedisConfig.HOST, port=RedisConfig.PORT, db=RedisConfig.DB)
