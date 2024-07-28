import uuid
import base62


def encode(u: uuid.UUID) -> str:
    return base62.encode(u.int)


def decode(s: str) -> str:
    return uuid.UUID(int=base62.decode(s))
