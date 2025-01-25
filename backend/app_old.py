from flask import Flask, request, jsonify
from flask_cors import CORS 
from selenium import webdriver
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

CORS(app, supports_credentials=True, origins="http://localhost:5173") 

@app.route("/scrape", methods=["POST", "OPTIONS"])
def scrape_data():
    if request.method == "OPTIONS":
        return "", 200  

    data = request.get_json()
    url = data.get("url")
    scrape_type = data.get("scrape_type")

    if "instagram.com" in url:
        return jsonify(scrape_instagram(url, scrape_type))
    elif "youtube.com" in url:
        return jsonify(scrape_youtube(url, scrape_type))
    elif "tiktok.com" in url:
        return jsonify(scrape_tiktok(url, scrape_type))
    elif "facebook.com" in url:
        return jsonify(scrape_facebook(url, scrape_type))
    else:
        return jsonify({"error": "Unsupported platform"}), 400

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

if __name__ == "__main__":
    app.run(debug=True)