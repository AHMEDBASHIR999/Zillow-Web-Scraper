import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def bypass_captcha(driver):
    while True:
        try:
            st.write("Attempting to bypass CAPTCHA...")
            body = driver.find_element(By.TAG_NAME, 'body')
            body.send_keys(Keys.TAB)
            time.sleep(1)  # Short delay
            
            action = ActionChains(driver)
            action.key_down(Keys.SPACE).perform()
            time.sleep(10)  # Hold for 10 seconds
            action.key_up(Keys.SPACE).perform()
            
            time.sleep(5)  # Wait for CAPTCHA to process

            if "px-captcha" not in driver.page_source:
                st.write("CAPTCHA bypassed successfully.")
                break
            else:
                st.write("CAPTCHA still present. Retrying...")
        except Exception as e:
            st.write(f"CAPTCHA bypass attempt failed: {e}")
            time.sleep(5)  # Wait before retrying

def press_key_multiple_times(driver, key, times):
    body = driver.find_element(By.TAG_NAME, 'body')
    for _ in range(times):
        body.send_keys(key)
        time.sleep(0.1)  # Short delay between key presses

def apply_newest_filter(driver):
    try:
        body = driver.find_element(By.TAG_NAME, 'body')
        for _ in range(19):
            body.send_keys(Keys.TAB)
            time.sleep(0.1)
        time.sleep(2)
        
        action = ActionChains(driver)
        action.key_down(Keys.SPACE).perform()
        time.sleep(0.5)
        action.key_up(Keys.SPACE).perform()
        time.sleep(2)
        
        for _ in range(4):
            body.send_keys(Keys.TAB)
            time.sleep(0.1)
        time.sleep(1)
        
        action.key_down(Keys.ENTER).perform()
        time.sleep(0.5)
        action.key_up(Keys.ENTER).perform()
    
        time.sleep(10)  # Wait for the filter to apply
    except Exception as e:
        st.write(f"Failed to apply 'Newest' filter: {e}")

def extract_data_from_page(driver, soup, data_list, stop_flag):
    property_cards = soup.find_all('article', {'data-test': 'property-card'})
    st.write(f"Found {len(property_cards)} properties on the page")
    
    for card in property_cards:
        if st.session_state.get(stop_flag):
            st.write("Scraping stopped by user.")
            return
        link = card.find('a', {'data-test': 'property-card-link'})
        if link:
            property_url = link['href']
            if not property_url.startswith('http'):
                property_url = 'https://www.zillow.com' + property_url
            st.write(f"Extracting data from: {property_url}")
            open_page_and_bypass_captcha(driver, property_url)
            property_data = extract_detailed_data(driver)
            if property_data:
                property_data['Link'] = property_url
                data_list.append(property_data)

def extract_detailed_data(driver):
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    try:
        address_tag = soup.find('div', class_='styles__AddressWrapper-fshdp-8-100-2__sc-13x5vko-0 jrtioM')
        address = address_tag.find('h1').text.strip() if address_tag else 'N/A'
        
        price_tag = soup.find('span', {'data-testid': 'price'})
        price = price_tag.find('span').text.strip() if price_tag else 'N/A'
        
        beds = 'N/A'
        baths = 'N/A'
        sqft = 'N/A'
        bed_bath_sqft = soup.find_all('div', {'data-testid': 'bed-bath-sqft-fact-container'})
        for fact in bed_bath_sqft:
            fact_text = fact.text.strip().lower() if fact else ''
            if 'beds' in fact_text:
                beds = fact.find('span', class_='Text-c11n-8-100-2__sc-aiai24-0').text.strip() if fact else 'N/A'
            elif 'baths' in fact_text:
                baths = fact.find('span', class_='Text-c11n-8-100-2__sc-aiai24-0').text.strip() if fact else 'N/A'
            elif 'sqft' in fact_text:
                sqft = fact.find('span', class_='Text-c11n-8-100-2__sc-aiai24-0').text.strip() if fact else 'N/A'

        year_built_tag = soup.find('span', class_='Text-c11n-8-100-2__sc-aiai24-0', text=lambda x: x and 'Built in' in x)
        year_built = year_built_tag.text.strip() if year_built_tag else 'N/A'

        sqft_lot_tag = soup.find('span', string=lambda text: 'sqft lot' in text if text else False)
        sqft_lot = sqft_lot_tag.text.strip() if sqft_lot_tag else 'N/A'
        
        price_per_sqft_tag = soup.find('span', string=lambda text: '/sqft' in text if text else False)
        price_per_sqft = price_per_sqft_tag.text.strip() if price_per_sqft_tag else 'N/A'
        
        hoa_tag = soup.find('span', string=lambda text: 'HOA' in text if text else False)
        hoa = hoa_tag.text.strip() if hoa_tag else 'N/A'
        
        zestimate_parent_tags = soup.find_all('div', class_='styles__StyledContainer-fshdp-8-100-2__sc-6k0go5-0 kPhJKv')
        if len(zestimate_parent_tags) >= 4:
            zestimate_tag = zestimate_parent_tags[3].find('span', class_='Text-c11n-8-100-2__sc-aiai24-0')
            zestimate = zestimate_tag.text.strip().split(' ')[0] if zestimate_tag else 'N/A'
        else:
            zestimate = 'N/A'
        
        property_data = {
            'Address': address,
            'Price': price,
            'Beds': beds,
            'Baths': baths,
            'Sqft': sqft,
            'Year Built': year_built,
            'Zestimate': zestimate,
            'Lot Size': sqft_lot,
            'Price per Sqft': price_per_sqft,
            'HOA': hoa
        }
        
        st.write(f"Extracted data: {property_data}")
        return property_data
    except Exception as e:
        st.write(f"Error extracting data: {e}")
        return None

def open_page_and_bypass_captcha(driver, url):
    driver.get(url)
    time.sleep(5)  # Wait for the page to load
    
    if "px-captcha" in driver.page_source:
        bypass_captcha(driver)

def get_total_pages(soup):
    pagination = soup.find('ul', class_='PaginationList-c11n-8-100-8__sc-1b5xve1-0 bTjRSb')
    if pagination:
        last_page_link = pagination.find_all('li')[-3].find('a')
        if last_page_link:
            return int(last_page_link.text)
    return 1  # Default to 1 if pagination is not found

def scrape_zillow(search_url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        driver.get(search_url)
        time.sleep(5)  # Wait for the page to load
        
        if "px-captcha" in driver.page_source:
            bypass_captcha(driver)
        
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        total_pages = get_total_pages(soup)
        
        st.write(f"Total pages to scrape: {total_pages}")
        
        data_list = []
        for page in range(1, total_pages + 1):
            if st.session_state.get("stop_scraping"):
                st.write("Scraping stopped by user.")
                break
            
            current_url = f"{search_url}&page={page}"
            driver.get(current_url)
            time.sleep(5)  # Wait for the page to load
            
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            extract_data_from_page(driver, soup, data_list, "stop_scraping")
        
        st.write("Scraping completed.")
        return pd.DataFrame(data_list)
    except Exception as e:
        st.write(f"An error occurred during scraping: {e}")
        return None
    finally:
        driver.quit()

load_view():
    st.title("Zillow Property Scraper")
    search_url = st.text_input("Enter Zillow Search URL")
    
    if st.button("Start Scraping"):
        st.session_state.stop_scraping = False
        if search_url:
            df = scrape_zillow(search_url)
            if df is not None:
                st.write("Scraping Results:")
                st.dataframe(df)
                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button(label="Download CSV", data=csv, file_name='zillow_properties.csv', mime='text/csv')
        else:
            st.write("Please enter a valid URL.")
    
    if st.button("Stop Scraping"):
        st.session_state.stop_scraping = True
        st.write("Stopping scraping...")
