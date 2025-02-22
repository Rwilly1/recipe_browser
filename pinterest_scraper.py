#This is a work in progress 


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from recipe_scrapers import scrape_me
import requests
from bs4 import BeautifulSoup
import json

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def get_pinterest_links(board_url):
    driver = setup_driver()
    try:
        driver.get(board_url)
        time.sleep(5)
        
        for _ in range(3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
        
        pins = driver.find_elements(By.CSS_SELECTOR, "a[href*='/pin/']")
        pin_links = [pin.get_attribute('href') for pin in pins]
        
        return pin_links
    finally:
        driver.quit()

def get_original_recipe_url(pin_url):
    try:
        response = requests.get(pin_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        meta_tag = soup.find('meta', {'property': 'og:see_also'})
        if meta_tag:
            return meta_tag.get('content')
    except Exception as e:
        print(f"Error getting original URL from pin {pin_url}: {str(e)}")
    return None

def scrape_recipe(url):
    try:
        scraper = scrape_me(url)
        recipe = {
            'name': scraper.title(),
            'ingredients': scraper.ingredients(),
            'instructions': scraper.instructions().split('\n'),  # Split into steps
            'meal_type': ['dinner'],  # Default to dinner
            'allergies': [],  # Default to no allergies
            'source': url
        }
        return recipe
    except Exception as e:
        print(f"Error scraping recipe from {url}: {str(e)}")
        return None

def get_recipes_from_pinterest(board_url):
    pin_links = get_pinterest_links(board_url)
    recipes_dict = {}
    seen_urls = set()
    
    for pin_link in pin_links:
        original_url = get_original_recipe_url(pin_link)
        if original_url and original_url not in seen_urls:
            recipe = scrape_recipe(original_url)
            if recipe:
                # Use recipe name as key, replacing spaces with underscores
                key = recipe['name'].lower().replace(' ', '_')
                recipes_dict[key] = recipe
                seen_urls.add(original_url)
    
    return recipes_dict

def save_recipes_to_json(recipes, filename='recipes.json'):
    with open(filename, 'w') as f:
        json.dump(recipes, f, indent=2)
