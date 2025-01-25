from fastapi import FastAPI, HTTPException
from selenium import webdriver
from bs4 import BeautifulSoup
import requests

app = FastAPI()

@app.post("/scrape/")
async def scrape_data(url: str, scrape_type: str):
    if "instagram.com" in url:
        return scrape_instagram(url, scrape_type)
    elif "youtube.com" in url:
        return scrape_youtube(url, scrape_type)
    elif "tiktok.com" in url:
        return scrape_tiktok(url, scrape_type)
    elif "facebook.com" in url:
        return scrape_facebook(url, scrape_type)
    else:
        raise HTTPException(status_code=400, detail="Unsupported platform")

def scrape_instagram(url, scrape_type):
    driver = webdriver.Firefox()
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    if scrape_type == "followers":
        followers = soup.find_all('div', class_='follower-class')
        return {"followers": [f.text for f in followers]}
    else:
        return {"error": "Invalid scrape type for Instagram"}

def scrape_youtube(url, scrape_type):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    if scrape_type == "comments":
        comments = soup.find_all('yt-formatted-string', id='content-text')
        return {"comments": [c.text for c in comments]}
    return {"error": "Invalid scrape type for YouTube"}

def scrape_tiktok(url, scrape_type):
    return {"error": "TikTok scraping is restricted without API"}

def scrape_facebook(url, scrape_type):
    return {"error": "Facebook scraping is restricted without API"}