# Selenium Web Scraping Script for Report Automation

## Overview
This repository contains a Python script that automates the process of logging into a web-based reporting system, setting date ranges, running reports, and scraping the resulting data into a CSV file. This script is particularly useful for gathering data in intervals when a system limits the amount of data retrieved in a single request.

## How the Script Works
The script operates by performing the following steps:

1. **Initialize the WebDriver**: Set up Selenium WebDriver for Chrome to control browser actions.
2. **Login to the Reporting System**: Access the login page, fill in credentials, and submit the form to authenticate.
3. **Set Date Ranges for Reports**: Iterate over a series of date ranges, inputting the start and end dates for each report.
4. **Run Reports**: Trigger the generation of reports by simulating a button click.
5. **Scrape Data**: Extract the data from the generated reports using BeautifulSoup.
6. **Aggregate Data**: Combine data from each interval into a single DataFrame.
7. **Save Data**: Output the aggregated data to a CSV file for further analysis or storage.
8. **Close the Browser**: Terminate the WebDriver session and close the browser window.

## Features
- **Selenium WebDriver**: For automating web browser interaction.
- **BeautifulSoup**: For parsing HTML documents and extracting the data.
- **Pandas**: For data manipulation and analysis.
- **Datetime**: For handling dates and times.

## Requirements
- Python 3.x
- Selenium (`pip install selenium`)
- BeautifulSoup (`pip install beautifulsoup4`)
- Pandas (`pip install pandas`)
- ChromeDriver (Compatible with the version of the Chrome browser installed on your system)

## Installation
Ensure that Python and pip are already installed on your system. Then install the required Python packages:

```bash
pip install selenium beautifulsoup4 pandas

#this CSV file can be connected to the database like PostgreSQL and can be used for analysis
