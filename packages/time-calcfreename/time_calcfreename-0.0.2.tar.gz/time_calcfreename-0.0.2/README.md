# time_calc

## Description

This package provides a simple utility function to calculate the exact time after adding a specified number of seconds.

## Installation

You can install this package using pip:

```bash
pip install time_calc
```

## Usage

```python
from time_calc import add_seconds

# Example usage
result = add_seconds(60)
print(f"Updated time: {result}")
```

## Documentation

### `add_seconds(secs: float) -> datetime`

Calculates the exact time after adding the specified number of seconds.

- `secs` : Number of seconds to add.
- Returns: The updated `datetime` object.

