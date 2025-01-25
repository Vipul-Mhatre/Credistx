import React, { useState } from "react";
import axios from "axios";

const Scraper = () => {
    const [url, setUrl] = useState("");
    const [scrapeType, setScrapeType] = useState("");
    const [data, setData] = useState(null);

    const handleScrape = async () => {
        try {
            const response = await axios.post("http://localhost:5000/scrape/", {
                url,
                scrape_type: scrapeType,
            }, {
                headers: {
                    "Content-Type": "application/json",
                }
            });
            setData(response.data);
        } catch (error) {
            console.error("Error scraping data:", error);
        }
    };    

    return (
        <div>
            <h1>Scraper Tool</h1>
            <input
                type="text"
                placeholder="Enter URL"
                value={url}
                onChange={(e) => setUrl(e.target.value)}
            />
            <select
                value={scrapeType}
                onChange={(e) => setScrapeType(e.target.value)}
            >
                <option value="">Select Scrape Type</option>
                <option value="followers">Followers</option>
                <option value="following">Following</option>
                <option value="comments">Comments</option>
            </select>
            <button onClick={handleScrape}>Scrape</button>
            <pre>{data && JSON.stringify(data, null, 2)}</pre>
        </div>
    );
};

export default Scraper;