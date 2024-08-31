
import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_dentist_data(page):
    url = f"https://www.yellowpages.com/search?search_terms=dentists&geo_location_terms=United+States&page={page}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    data = []
    listings = soup.find_all('div', class_='result')
    
    for listing in listings:
        name = listing.find('a', class_='business-name').text if listing.find('a', class_='business-name') else 'N/A'
        address = listing.find('div', class_='street-address').text if listing.find('div', class_='street-address') else 'N/A'
        locality = listing.find('div', class_='locality').text if listing.find('div', class_='locality') else 'N/A'
        phone = listing.find('div', class_='phones phone primary').text if listing.find('div', class_='phones phone primary') else 'N/A'
        website = listing.find('a', class_='track-visit-website')['href'] if listing.find('a', class_='track-visit-website') else 'N/A'
        email = 'N/A'  # Yellow Pages typically do not list emails directly

        data.append([name, address, locality, phone, website, email])
    
    return data

def main():
    all_data = []
    for page in range(1, 6):  # Adjust the range for the number of pages you want to scrape
        data = get_dentist_data(page)
        all_data.extend(data)
    
    df = pd.DataFrame(all_data, columns=['Name', 'Address', 'Locality', 'Phone', 'Website', 'Email'])
    df.to_csv('dentists.csv', index=False)
    print("Data has been written to dentists.csv")

if __name__ == '__main__':
    main()
