# airporticao

# Airport ICAO Codes

This Python module provides information about airports from their ICAO code
including

* full name
* short name (removes redundant words like international and airport)
* description
* latitude and longitude
* timezone (UNIX style)
* elevation in feet and meters
* zip code

Information is provided by AirNav.com a fantastic resources for
pilots and aviation enthusiasts . Data is cached locally to reduce calls to AirNav.com

## Installation

% pip install airporticao


## Usage

Here's an example of how to use the module:

```python
from airporticao import AirNavAirports

ICAO = AirNavAirports()

data_jfk = ICAO.get_icao("KJFK")
print(f"name: {data_jfk['name']}")
```

## Documentation
You can find more detailed documentation for the airporticao module in the official documentation.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue on the GitHub repository.

## License
This project is licensed under the MIT License - see the LICENSE file for details.