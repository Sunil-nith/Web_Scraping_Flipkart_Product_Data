# Import the required libraries.
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse, parse_qs

# Define the CSV file containing the product data.
csv_file = "Products_1.csv" 

# Read the data from the CSV file into a DataFrame.
df = pd.read_csv(csv_file)

# Initialize new columns to store additional information.
df['Description'] = ""
df['FSN']=""
df['Product_Description']=""
df['Manufacturer']=""

# Loop through each row in the DataFrame to extract data from the product URLs.
for index, row in df.iterrows():

    # Limit the number of URLs processed (optional, here set to 200).
    if index >= 5:
        break

    # Get the URL for the current product.
    url = row['Product Url']
    print(index)

    # Configure options for the headless Chrome browser.
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")

    # Create a new instance of the Chrome driver.
    driver = webdriver.Chrome(options=options)

    # Use requests and BeautifulSoup to scrape some data from the initial URL.
    request = requests.get(url)
    soup = BeautifulSoup(request.text,"lxml")
        
    try:
        # Use Selenium to navigate to the product URL and interact with the page.
        driver.get(url)

        # Wait for the "Read More" button to be clickable and click it to reveal hidden content.
        read_more_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Read More')]"))
            )
        read_more_button.click()

        # Click on the "Manufacturing, Packaging and Import Info" section to reveal details.
        manufacture_info_section = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Manufacturing, Packaging and Import Info')]"))
            )
        manufacture_info_section.click()
        
        # Wait for the updated content to load and then parse it with BeautifulSoup.
        WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='_3-9BsV']"))
            )
        updated_html = driver.page_source
        updated_soup = BeautifulSoup(updated_html, 'html.parser')
        manufacture = updated_soup.find('li', class_='_3_27HS').text.strip()
    
    except Exception as e:
        print(f"Error: {e}")
        manufacture = ""
    
    finally:
        # Close the browser after processing each URL.
         driver.quit()

    # Update the DataFrame with the extracted information.
    df.at[index, 'Manufacturer'] = manufacture
    
    # Extract the product description from the initial URL using BeautifulSoup and Update the DataFrame with the extracted information.
    try :
        desc= soup.find("div",class_="_1mXcCf RmoJUa").text.strip()
    except:
        desc= " "
    df.at[index, 'Description'] = desc

    # Extract the product description in details from the initial URL using BeautifulSoup and Update the DataFrame with the extracted information.
    try :
        prod_descs= soup.find_all("div",class_="_3zQntF")
        prod_desc = "\n\n".join(div.text.strip() for div in prod_descs)
    except:
        prod_desc= " "
    df.at[index, 'Product_Description'] = prod_desc

    # Parse the FSN from the product URL using urlparse and parse_qs.
    try:
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)

        pid_value = query_params.get('pid', [''])[0]
    except:
        pid_value="0"
    df.at[index, 'FSN'] = pid_value

# Save the updated DataFrame to a new CSV file.
output_csv_file = "Products_2.csv"
df.to_csv(output_csv_file, index=False)