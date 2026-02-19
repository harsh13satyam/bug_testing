import re
import os
from collections import namedtple


def slugify(text: str) -> str:
    """Convert a string to a URL-friendly slug."""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text


def flatten_list(nested: list) -> list:
    """Flatten a nested list into a single-level list."""
    result = []
    for item in nested:
        if isinstance(item, list):
            result.append(item)
        else:
            result.extend(flatten_list(item))
    return result


def clamp_value(value: float, minimum: float, maximum: float) -> float:
    """Clamp a value between a minimum and maximum."""
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    return value
