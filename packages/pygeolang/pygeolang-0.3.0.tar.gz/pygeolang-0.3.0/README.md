# PyGeoLang: Python Library for Geo-Linguistic Data

[![PyPI Version](https://img.shields.io/pypi/v/pygeolang.svg)](https://pypi.org/project/pygeolang/)
[![Documentation Status](https://readthedocs.org/projects/pygeolang/badge/?version=latest)](https://pygeolang.readthedocs.io/en/latest/?badge=latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

PyGeoLang is a Python library that provides easy access to comprehensive geographic and linguistic data about countries and continents. It builds upon and extends the functionality of popular libraries like `pycountry` and `langcodes` to offer a unified interface for various geo-linguistic queries.


## Features

- **Country Data:**
  - Get country codes (alpha-2, alpha-3, numeric) by name.
  - Get country names by code.
  - Get official country names.
  - Get the continent a country belongs to.
  - Get languages spoken in a country.
- **Continent Data:**
  - Get a list of countries in a continent.
- **Language Data:**
  - Get countries where a specific language is spoken.
- **Data Source:**
  - Data is sourced from reliable sources (`pycountry`, custom dataset) and efficiently stored in a binary format for fast loading.
- **Simple API:**
  - Easy-to-use functions for common geo-linguistic queries.
- **Extensible:**
  - Designed to be easily extended with additional data sources or custom functions.


## Installation

```bash
pip install pygeolang
```

## Usage

```python
import pygeolang

# Get country code
code = pygeolang.get_country_code("Germany", "alpha_3")
print(code)  # Output: DEU

# Get country by code
country = pygeolang.get_country_by_code("276")
print(country.name)  # Output: Germany
print(country.official_name)  # Output: Federal Republic of Germany
print(country.languages)    # Output: ['German']
print(country.continent)    # Output: Europe

# Get countries by continent
countries = pygeolang.get_countries_by_continent("Asia")
print(countries) # ['Afghanistan', 'Armenia', ... ]

# Get languages by country
languages = pygeolang.get_languages_by_country("India")
print(languages) # ['Hindi', 'English', ...]
```

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests. 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.