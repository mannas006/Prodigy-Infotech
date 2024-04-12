import csv
import requests
from bs4 import BeautifulSoup

def scrape_products(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        products = []

        # Modify this part to extract product information based on the Symphony Limited website's HTML structure
        for product in soup.find_all('div', class_='product-item'):
            name = product.find('h3', class_='product-title').text.strip()
            price = product.find('span', class_='money').text.strip()
            rating = product.find('div', class_='shopify-product-reviews-badge').text.strip()
            
            products.append({'Name': name, 'Price': price, 'Rating': rating})

        return products
    else:
        print(f"Failed to retrieve data from {url}")
        return None

def save_to_csv(products, filename):
    if products:
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['Name', 'Price', 'Rating']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(products)
        print(f"Data saved to {filename}")
    else:
        print("No data to save.")

if __name__ == "__main__":
    url = 'https://www.amazon.in/All-Product/s?k=All+Product'
    products = scrape_products(url)
    if products:
        save_to_csv(products, 'amazon_products.csv')
