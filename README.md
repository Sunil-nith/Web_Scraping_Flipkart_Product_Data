# Web Scraping Flipkart Products Data.

* This project is a web scraping tool to extract product data from Flipkart's search results for a specific search query. 
* It retrieves product information, such as product URLs, names, prices, ratings, and the number of reviews from multiple pages of search results. 
* It uses Python with libraries like requests and BeautifulSoup for web scraping.
* Also incorporates Selenium for handling dynamic content, such as "Read More" buttons and other hidden details.



### Built With

* Python
* BeautifulSoup
* requests
* Selenium
* pandas

## Features
* Scrape product data from Flipkart search results.
* Extract product URLs, names, prices, ratings,review counts,description,FSN,Product Description and Manufacturer details.
* Supports scraping multiple pages of product listings.
* Utilizes Selenium for handling dynamic content and hidden details.
* Provides a basic framework for further data extraction from product detail pages.
* Exports the basic product data to a CSV file.
* Extract additional product details (e.g., description, FSN, manufacturer) from    each product URL.
* Updates the CSV file with the additional product details.


## Prerequisites
Before running the application, make sure you have the following prerequisites installed on your system:

* Python (version 3.x recommended)
* Required Python libraries: requests, beautifulsoup4, selenium, pandas
```sh
   pip install requests beautifulsoup4 selenium pandas
   ```


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Sunil-nith/Web_Scraping_Flipkart_Product_Data.git
   ```
2. Navigate to the project directory.
3. Install Required Python libraries.
4. Run First web_scraping_1.py then Run web_scraping_2.py
   

## Usage

1. Open the web_scraping_1.py file.
2. In the url variable, update the search query (e.g., bags) to the desired product category you want to scrape.
3. In the Pages_to_scrape variable, update the number of pages you want to scrape (e.g., 20).
4. Run the web_scraping_1.py script using Python.
5. This script will scrape product data from the specified number of pages and save the basic product data (name, price, URL) to a CSV file named Products_1.csv.
6. Now Open the web_scraping_2.py file.
7. Run the web_scraping_2.py script using Python.
8. The script will read the basic product data from the  Products_1.csv file, visit each product URL, fetch additional product details (e.g., description, FSN, manufacturer), and update the CSV file with the additional information to a CSV file named Product_2.csv


## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, please create an issue or submit a pull request

## Contact

If you have any questions or need further assistance, please feel free to contact me at skjnv2009@gmail.com.


