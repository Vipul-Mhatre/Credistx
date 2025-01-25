from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import re
import os

app = Flask(__name__)

CORS(app)

API_KEYS = {
    "youtube": os.getenv("YOUTUBE_API_KEY", "YOUR_YOUTUBE_API_KEY_HERE"),
}

@app.route('/')
def home():
    return "Welcome to the Ethical Scraper API!"

@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.json
    platform = data.get('platform')
    url = data.get('url')

    if not platform or not url:
        return jsonify({"error": "Platform and URL are required"}), 400

    if platform == "youtube":
        return fetch_youtube_data(url)
    else:
        return jsonify({"error": "Unsupported platform"}), 400

def fetch_youtube_data(url):
    try:
        video_id = extract_youtube_video_id(url)
        if not video_id:
            return jsonify({"error": "Invalid YouTube URL"}), 400

        youtube_api_url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics,contentDetails,liveStreamingDetails,topicDetails&id={video_id}&key={API_KEYS['youtube']}"
        response = requests.get(youtube_api_url)

        if response.status_code == 200:
            video_data = response.json()
            if "items" in video_data and video_data["items"]:
                video_details = video_data["items"][0]
                
                # Convert duration (e.g., PT3M13S) to hh:mm:ss format
                duration = video_details["contentDetails"]["duration"]
                formatted_duration = iso8601_duration_to_hms(duration)

                # Category ID mapping
                category_id = video_details["snippet"].get("categoryId", "N/A")
                category_name = category_id_to_name(category_id)

                video_info = {
                    "title": video_details["snippet"]["title"],
                    "description": video_details["snippet"]["description"],
                    "published_at": video_details["snippet"]["publishedAt"],
                    "view_count": video_details["statistics"]["viewCount"],
                    "like_count": video_details["statistics"]["likeCount"],
                    "dislike_count": video_details["statistics"].get("dislikeCount", "N/A"),
                    "comment_count": video_details["statistics"].get("commentCount", "N/A"),
                    "duration": formatted_duration,  # formatted duration
                    "category": f"{category_id} ({category_name})",  # category with ID and name
                    "tags": video_details["snippet"].get("tags", []),
                    "topics": video_details.get("topicDetails", {}).get("topicCategories", []),
                    "live_broadcast_content": video_details.get("liveStreamingDetails", {}).get("liveBroadcastContent", "N/A")
                }
                return jsonify(video_info)
            else:
                return jsonify({"error": "Video not found or no data available"}), 404
        else:
            return jsonify({"error": f"Failed to fetch YouTube data. Status code: {response.status_code}"}), response.status_code
    except Exception as e:
        print(f"Error fetching YouTube data: {e}")  # Log the error to the console
        return jsonify({"error": f"Server error: {str(e)}"}), 500

def iso8601_duration_to_hms(duration):
    """Convert ISO 8601 duration (e.g., PT3M13S) to hh:mm:ss format."""
    pattern = re.compile(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?")
    match = pattern.match(duration)
    
    if not match:
        return "00:00:00" 
    
    hours = match.group(1) or "0"
    minutes = match.group(2) or "0"
    seconds = match.group(3) or "0"
    
    return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

def category_id_to_name(category_id):
    """Convert YouTube category ID to category name."""
    categories = {
        "1": "Film & Animation",
        "2": "Autos & Vehicles",
        "10": "Music",
        "15": "Pets & Animals",
        "17": "Sports",
        "18": "Short Movies",
        "19": "Travel & Events",
        "20": "Gaming",
        "21": "Videoblogging",
        "22": "People & Blogs",
        "23": "Comedy",
        "24": "Entertainment",
        "25": "News & Politics",
        "26": "How-to & Style",
        "27": "Education",
        "28": "Science & Technology",
        "29": "Nonprofits & Activism",
        "30": "Movies",
        "31": "Anime/Animation",
        "32": "Action/Adventure",
        "33": "Classics",
        "34": "Comedy",
        "35": "Documentary",
        "36": "Drama",
        "37": "Family",
        "38": "Horror",
        "39": "Sci-Fi/Fantasy",
        "40": "Thriller"
    }
    return categories.get(category_id, "Unknown Category")

def extract_youtube_video_id(url):
    video_id = None
    youtube_url_pattern = r"(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S+?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]+)"
    match = re.match(youtube_url_pattern, url)
    if match:
        video_id = match.group(1)
    return video_id

if __name__ == "__main__":
    app.run(debug=True)
