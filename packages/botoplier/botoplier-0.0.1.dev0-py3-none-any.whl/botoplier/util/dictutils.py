import asyncio
from collections import defaultdict
from collections.abc import Awaitable, Iterable
from functools import reduce
from typing import Callable, TypeVar


def get_in(_dict, keys: list, default=None):
    """Get a value from arbitrarily nested dicts."""
    if not keys:
        return _dict
    if len(keys) == 1:
        return _dict.get(keys[0], default)
    return get_in(_dict.get(keys[0], {}), keys[1:], default)


def get_path_in(_dict, dot_separated_keys: str, default=None):
    """Get a value from arbitrarily nested dicts using a dot-separated path."""
    return get_in(_dict, dot_separated_keys.split("."), default)


K = TypeVar("K")
V = TypeVar("V")


# From https://gist.github.com/privatwolke/11711cc26a843784afd1aeeb16308a30 (Public domain)
async def gather_dict(tasks: dict[K, Awaitable[V]]) -> dict[K, V]:
    """Return a dict of (key, returned_values) from a dict of (key, future)."""

    async def mark(key: K, coro: Awaitable[V]) -> tuple[K, V]:
        return key, await coro

    return dict(await asyncio.gather(*(mark(key, coro) for key, coro in tasks.items())))


def densest_key(things: list[dict]):
    """Find the densest key in a series of dict.

    The densest key of a key is the key for which the value contains the most
    information. This is based purely on __len__ for dict and list only.
    """
    assert isinstance(things, list)
    assert reduce(lambda r, e: r and isinstance(e, dict), things, initial=True)

    density_scores = defaultdict(lambda: 0)
    for thing in things:
        longest_key = None
        longest_key_length = -1
        for k, v in thing.items():
            if (isinstance(v, (list, dict))) and len(v) > longest_key_length:
                longest_key = k
                longest_key_length = len(v)
        density_scores[longest_key] += 1
    densest_score = max(density_scores.values())
    return next(k for k, v in density_scores.items() if v == densest_score)


T = TypeVar("T")


def groupby(iterable: Iterable[T], key: Callable[[T], K]) -> dict[K, list[T]]:
    """Groups by elements from an iterable into a dict. Takes arguments very similar
    to itertools.groupby.

    Unlike itertools.groupby, does not require prior sorting.
    Unlike itertools.groupby, this operates greedily and not lazily.
    """
    result = {}
    for e in iterable:
        k = key(e)
        if k not in result:
            result[k] = []
        result[k].append(e)
    return result


def keys(d: dict[K, V]) -> list[K]:
    """Greedy, memory allocating, variant of dict.keys."""
    return list(d.keys())


def values(d: dict[K, V]) -> list[V]:
    """Greedy, memory allocating, variant of dict.values."""
    return list(d.values())


def nested_keys(d: dict, prefix="") -> list:
    return [nested_keys(v, f"{prefix}{k}.") if isinstance(v, dict) else f"{prefix}{k}" for k, v in d.items()]


def max_by_key(objects: list[dict], k, default="") -> dict:
    return max(objects, key=lambda e: get_path_in(e, k, default))
