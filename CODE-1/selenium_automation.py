# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timedelta
import time

# Function to add days to a date
def add_days_to_date(date_str, days):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    return (date_obj + timedelta(days=days)).strftime('%Y-%m-%d')

# Set up the Chrome WebDriver
chrome_driver_path = r'C:\Users\chromedriver.exe'  # Path to your ChromeDriver

driver = webdriver.Chrome(service=Service(chrome_driver_path))

# Navigate to the login page
val = 'Link' # Replace with your inventory link
driver.get(val)

# Log in to the page
input_username = driver.find_element(By.ID, 'username')
input_password = driver.find_element(By.ID, 'password')
login_btn = driver.find_element(By.ID, 'login_button')

input_username.send_keys('') # Replace with your actual username
input_password.send_keys('') # Replace with your actual password
login_btn.click()

# Wait for the report page to load after login
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'u1')))

# Set the initial start date and the number of days to add each time
initial_start_date = '2023-04-01'
days_to_add = 5
total_intervals = 12

all_data = [] # List to hold all scraped data

for interval in range(total_intervals):
    start_date = add_days_to_date(initial_start_date, interval * days_to_add)
    end_date = add_days_to_date(start_date, days_to_add - 1)

# Input the start date
    start_date_input = driver.find_element(By.ID, 'u1')
    start_date_input.clear()
    start_date_input.send_keys(start_date)

# Input the end date
    end_date_input = driver.find_element(By.ID, 'u2')
    end_date_input.clear()
    end_date_input.send_keys(end_date)

# Select 'Clinic Only' option, '1' for Yes or '0' for No
    clinic_only_option = driver.find_element(By.XPATH, '//input[@name="u3" and @value="0"]')
    clinic_only_option.click()

# Click the 'Run report' button
    run_report_button = driver.find_element(By.CLASS_NAME, 'runreport')
    run_report_button.click()

# Wait for the report to be generated and ensure that the table is loaded
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'dbr_rt1')))

# Scrape the data using BeautifulSoup
    table_element = driver.find_element(By.ID, 'dbr_rt1')
    table_html = table_element.get_attribute('outerHTML')
    soup = BeautifulSoup(table_html, 'html.parser')
    df = pd.read_html(str(soup))[0]
    all_data.append(df)

# Go back to the main report page to start the next interval
    driver.back()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'u1')))
    time.sleep(2) # Adjust the sleep time as needed for your page's load time

# Concatenate all data into one DataFrame
all_clinics_df = pd.concat(all_data, ignore_index=True)

# Save the concatenated DataFrame to a CSV file
all_clinics_df.to_csv(r'C:\Users\extracted_data_test.csv', index=False)

driver.quit()
