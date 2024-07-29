# Open Flags

`open_flags` is a lightweight Python library for handling flag SVGs. It provides functions to fetch and display SVG flags based on country and region codes. This library is perfect for integrating into web applications or other Python projects.

## Installation

Install the package via pip:

```sh
pip install open_flags
```

## Usage

Retrieving an SVG

```py
from open_flags import get_flag_svg

svg_content = get_flag_svg('usa', 'colorado')
print(svg_content)
```

Getting All Flags

```py
from open_flags import get_all_flags

flags = get_all_flags()
print(flags)
Getting Flags by Country
python
Copy code
from open_flags import get_flags_by_country

us_flags = get_flags_by_country('usa')
print(us_flags)
```

## API

```
get_flag_svg(country: str, region: str) -> str
Returns the SVG content for the specified country and region.

get_all_flags() -> list
Returns a list of all available flags in the format country/region.

get_flags_by_country(country: str) -> list
Returns a list of flags for the specified country.
```

# Contributing

Contributions are welcome! Please open an issue or submit a pull request.
