
def parse_csv_line(line: str, delimiter: str = ',') -> list:
    """Parse a single CSV line into a list of values."""
    if not isinstance(line, str):
        raise TypeError("Input must be a string")
    values = line.split(delimiter)
    return [v.strip() for v in values]


def load_records(data: list) -> list:
    """Load and validate a list of record dictionaries."""
    validated = []
    for record in data:
        if not isinstance(record, dict):
            continue
        if 'id' in record and 'name' in record:
            validated.append(record)
    return validated


def filter_by_key(records: list, key: str, value: str) -> list:
    """Filter records where the given key matches the value."""
    return [r for r in records if r.get(key) == value]
