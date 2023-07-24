# Import the required libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

# Initialize empty lists to store the extracted data
Product_name=[]
Product_url=[]
Prices =[]
Rating=[]
Num_review=[]

Pages_to_scrape=20

# Loop through the pages to scrape the data
for page in range(1,Pages_to_scrape+1):

    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    url = "https://www.flipkart.com/search?q=mobile&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=mobile%7CMobiles&requestId=a11a2e2c-9447-4d04-9992-282fd51dc33b&as-searchtext=mo&page=" + str(page)
    
    # Send a request to the URL to get the page's content.
    request= requests.get(url ,headers=headers)

    # Parse the HTML content using BeautifulSoup.
    soup = BeautifulSoup(request.text,"lxml")

    # Find the container that holds the individual products.
    container = soup.find("div", class_ = "_1YokD2 _3Mn1Gg")
    Products = container.find_all("div", class_ = "_13oc-S")
    
    # Extract information for each product in the container and store into the initialized empty list.
    for Product in Products :
        try :
            name = Product.find("div",class_ ="_4rR01T").text.strip()
        except:
            name = " "
        Product_name.append(name)

        try:
            p_url= "https://www.flipkart.com"+ Product.find("a", class_="_1fQZEK")['href']
        except:
            p_url=" "
        Product_url.append(p_url)

        try :
            price = Product.find("div", class_ = "_30jeq3 _1_WHN1").text.strip()
        except:
            price = " "
        Prices.append(price)

        try:
            rating = Product.find("div", class_ = "_3LWZlK").text.strip()
        except:
            rating = "Not Available"
        Rating.append(rating)

        try:
            n_review=Product.find("span",class_="_2_R_DZ").text.split()[3]
        except:
            n_review="0"
        Num_review.append(n_review)
    
    # Add a delay to avoid overloading the server with too many requests.
    time.sleep(2)


# Create a DataFrame from the extracted data and Save the DataFrame to a CSV file.      
df = pd.DataFrame({"Product Name":Product_name,"Product Url":Product_url,"Prices":Prices,"Rating":Rating,"Number of Review":Num_review})
df.to_csv("Products_1.csv", index=False)


