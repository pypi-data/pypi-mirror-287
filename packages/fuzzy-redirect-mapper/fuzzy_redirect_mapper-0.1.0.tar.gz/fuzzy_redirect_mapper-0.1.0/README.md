# Fuzzy Redirect Mapper

The Fuzzy Multi-format Redirect Builder Python script is a time-saving tool to help speed up redirect mapping. Every SEO knows that redirect mapping can be a tedious and very time-consuming task.

This python script helps you to speed up the redirect mapping process, saving yourself, your team, and your clients time and money.

## Installation

```sh
pip install fuzzy_redirect_mapper
```

## Usage

```python
from fuzzy_redirect_mapper import compare_urls_in_csv

file_name = "urls-input.csv"
column1 = "source"
column2 = "destination"
result_df = compare_urls_in_csv(file_name, column1, column2)
```

## License

MIT License. See the LICENSE file for details.
