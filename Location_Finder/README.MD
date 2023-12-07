# Geolocation Finder with Python 🌍

## Overview 🌐
This repository contains two Python scripts leveraging the `geopy` library to extract location information based on geographic coordinates. One script fetches full addresses, while the other retrieves only the pin codes.

## Scripts Description 📜

### 1. Full Address Finder (`full_address_finder.py`)
This script uses a list of geographic coordinates (latitude and longitude) to find the full address of each location. It's useful for obtaining detailed location information, including street name, city, country, etc.

#### How It Works:
- **Coordinates List**: The script starts with a predefined list of latitude and longitude pairs.
- **Geolocation Service**: Utilizes `Nominatim` from `geopy.geocoders` with a user-defined agent name (`"location_finder"`).
- **Address Retrieval**: For each coordinate pair, the script queries the geolocation service to find the corresponding full address.

### 2. Pin Code Finder (`pin_code_finder.py`)
This script is specifically designed to extract pin codes from a list of geographical coordinates. It's ideal for cases where only the postal code of a location is required.

#### How It Works:
- **Coordinates List**: Begins with a set of latitude and longitude pairs.
- **Geolocation Service**: Employs `Nominatim` from `geopy.geocoders` with the user agent `"location_finder"`.
- **Pin Code Extraction**: For each coordinate, it fetches the location data and extracts the `postcode` from the response. If a pin code is not available, it outputs "Pin code not found for location."

## Requirements 📋
- Python 3.x
- geopy library (`pip install geopy`)

## How to Use 🛠
1. **Clone the Repository:**
2. **Install geopy:**
3. **Run the Script:**
- For full addresses:
  ```
  python full_address_finder.py
  ```
- For pin codes:
  ```
  python pin_code_finder.py
  ```

## Contribution Guidelines 🤝
[Standard contribution guidelines]

## Acknowledgements 🙏
- Thanks to the geopy library for providing easy access to geolocation services.


