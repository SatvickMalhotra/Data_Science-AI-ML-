# Interactive Clinic Location Mapper & Analyzer 🌍🏥

## Overview 🌐
This Python script is designed to visualize and analyze clinic locations across India. It uses geographic coordinates to create an interactive map, allowing for the evaluation of clinic distribution, proximity, and potential areas for expansion, merging, or closure.

## Features 🌟
- **Interactive Map Creation**: Utilizes `folium` to plot clinic locations on an interactive map.
- **Distance Calculation**: Implements functions to calculate the distance between any two points, aiding in the assessment of clinic proximity.
- **Dropdown Menus for Selection**: Integrates `ipywidgets` for easy selection of locations and distance calculation.
- **Geodesic Distance Measurement**: Uses `geodesic` from `geopy.distance` to measure real-world distances between clinics.

## How It Works 🔍
- **Plotting Clinics**: The script plots each clinic's location on the map with markers, tooltips, and popups for easy identification.
- **Interactive Selection**: Users can interactively select two points on the map to calculate the distance between them.
- **Dropdown Menus**: Allows users to select locations from dropdown menus to calculate distances.
- **Distance Analysis**: The calculated distances help in determining which clinics could be merged, closed, or where new ones could be opened based on proximity and distribution.

## Requirements 📋
- Python 3.x
- folium (`pip install folium`)
- ipywidgets (`pip install ipywidgets`)
- geopy (`pip install geopy`)
- IPython (`pip install ipython`)

## How to Use 🛠
1. **Clone the Repository:**
2. **Install Required Libraries:**
3. **Run the Script:**
- Execute the script in a Jupyter Notebook environment for full interactivity.
- Select locations using the dropdown menus or directly on the map to analyze distances.

## Contribution Guidelines 🤝
[Standard contribution guidelines]

## Acknowledgements 🙏
- Special thanks to the developers of `folium`, `geopy`, and `ipywidgets` for their invaluable tools.


