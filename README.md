

---

# 📌 Credistx: Ethical Social Media Scraper

Credistx is a full-stack web application designed to **ethically scrape public data** from popular social media platforms such as **YouTube, Instagram, and Facebook**. With a **Flask-based backend** and a **React + Vite frontend**, this project provides developers and researchers with a modular framework for extracting and displaying data while emphasizing responsible usage.

---

## 📑 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Detailed File Descriptions](#detailed-file-descriptions)
  - [Backend](#backend)
  - [Frontend](#frontend)
- [Installation & Setup](#installation--setup)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [How It Works](#how-it-works)
  - [Backend API Endpoints](#backend-api-endpoints)
  - [Frontend User Flow](#frontend-user-flow)
- [Configuration & Environment Variables](#configuration--environment-variables)
- [Technologies Used](#technologies-used)
- [Ethical Considerations & Limitations](#ethical-considerations--limitations)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Overview

Credistx is intended for users who require a reliable tool to extract public information from social media channels for research, monitoring, or data aggregation purposes. The project demonstrates a layered approach: a Python backend handling data retrieval and processing (using both API integrations and web scraping techniques) paired with a modern React frontend to deliver results interactively.

---

## Features

- **Multi-Platform Scraping**:  
  - **YouTube**: Retrieve video details including title, description, views, likes, comments, and duration.
  - **Instagram**: Extract follower counts and other public metrics using Selenium.
  - **Facebook**: Limited scraping for basic public profile info (subject to platform restrictions).

- **Backend (Flask, Selenium, BeautifulSoup)**:  
  - API endpoints to handle scraping requests.
  - Utilizes **Selenium** for dynamic, JavaScript-heavy pages.
  - Integrates with the **YouTube API** for structured video data retrieval.

- **Frontend (React, Vite)**:  
  - Clean and interactive user interface.
  - Allows users to input URLs and select specific scrape types.
  - Displays fetched results dynamically with real-time feedback.

- **Extensibility**:  
  - Modular codebase with separate files for different platforms.
  - Easy integration of additional social media platforms or scraping functionalities.

---

## Project Structure

```plaintext
Credistx-main/
├── backend/
│   ├── app.py            # Main Flask API entry point.
│   ├── app_old.py        # Previous version with CORS and Selenium-based scraping.
│   ├── scraper.py        # Shared scraping functions for multiple platforms.
│   ├── yt.py             # Dedicated YouTube API integration and data formatting.
│   ├── yt.html           # Static HTML template for testing YouTube scraping.
├── frontend/
│   ├── public/
│   │   └── vite.svg      # Static asset for Vite.
│   ├── src/
│   │   ├── assets/
│   │   │   └── react.svg # React logo asset.
│   │   ├── App.jsx       # Main React component integrating the scraper UI.
│   │   ├── Scraper.jsx   # Core component to input URL, choose scrape type, and display data.
│   │   ├── main.jsx      # Application entry point (React rendering).
│   │   └── index.css     # Global CSS styles.
│   ├── package.json      # NPM configuration with dependencies and scripts.
│   └── vite.config.js    # Configuration file for Vite builds.
├── .gitignore            # Files and directories to ignore in Git.
└── scraper.py            # Standalone scraper script (alternative entry point).
```

---

## Detailed File Descriptions

### Backend

- **app.py**  
  - **Purpose**: Acts as the primary entry point for the Flask server.
  - **Functionality**:
    - Defines the root endpoint (`/`) for a welcome message.
    - Provides the `/scrape` endpoint to process POST requests.
    - Delegates requests to platform-specific functions:
      - For YouTube, it calls functions in `yt.py`.
      - For other platforms, it leverages scraping routines in `scraper.py`.
    - Loads API keys from environment variables.

- **app_old.py**  
  - **Purpose**: Contains an earlier iteration of the API with added CORS support and Selenium integration.
  - **Functionality**:
    - Implements additional scraping strategies using Selenium and BeautifulSoup.
    - Includes logic for handling Instagram, YouTube, TikTok, and Facebook scraping.
    - Retains legacy code for reference or potential fallback scenarios.

- **scraper.py**  
  - **Purpose**: Provides common scraping routines.
  - **Functionality**:
    - Processes POST requests on `/scrape`.
    - Uses Selenium for pages requiring JavaScript execution.
    - Uses BeautifulSoup to parse static HTML content.
    - Implements platform-specific functions for Instagram, YouTube comments, and handling unsupported platforms.

- **yt.py**  
  - **Purpose**: Dedicated module for YouTube video data retrieval using the YouTube API.
  - **Functionality**:
    - Extracts video IDs from URLs.
    - Fetches video details (title, description, views, likes, duration, etc.).
    - Converts ISO 8601 durations (e.g., "PT3M13S") into a human-readable format.
    - Maps YouTube category IDs to descriptive names.

- **yt.html**  
  - **Purpose**: A simple HTML template possibly used for testing or demonstration purposes related to YouTube scraping.

---

### Frontend

- **App.jsx**  
  - **Purpose**: Serves as the main React component.
  - **Functionality**:
    - Integrates the **Scraper** component.
    - Acts as the primary container for the application.

- **Scraper.jsx**  
  - **Purpose**: Core component for the scraping UI.
  - **Functionality**:
    - Provides an input field for users to enter a URL.
    - Offers a dropdown to select the type of scraping (e.g., comments, followers).
    - Uses Axios to send POST requests to the backend API at `http://localhost:5000/scrape/`.
    - Dynamically displays JSON-formatted results upon successful data retrieval.
    - Includes error handling to notify users of issues.

- **main.jsx**  
  - **Purpose**: Entry point for the React application.
  - **Functionality**:
    - Bootstraps the React app by rendering the **App** component.
    - Utilizes React's StrictMode for highlighting potential issues.

- **vite.config.js**  
  - **Purpose**: Configures Vite, a build tool that enhances the development experience with rapid builds and hot module replacement.

- **package.json**  
  - **Purpose**: Manages frontend dependencies and scripts.
  - **Functionality**:
    - Lists required libraries such as React, Axios, and CORS.
    - Defines development and production scripts for running and building the application.

- **Public Assets (vite.svg & react.svg)**  
  - **Purpose**: Static assets used within the frontend for branding and visual components.

---

## Installation & Setup

### Backend Setup (Flask & Python)

1. **Clone the repository** and navigate to the backend directory:
   ```bash
   cd Credistx-main/backend
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   > _Note: Ensure that your `requirements.txt` includes Flask, Selenium, BeautifulSoup4, and other necessary libraries._

3. **Set up environment variables**:
   - Create a `.env` file (or set environment variables in your system) with:
     ```env
     YOUTUBE_API_KEY=YOUR_YOUTUBE_API_KEY
     INSTAGRAM_API_KEY=YOUR_INSTAGRAM_API_KEY
     FACEBOOK_API_KEY=YOUR_FACEBOOK_API_KEY
     ```
4. **Run the Flask server**:
   ```bash
   python app.py
   ```
   This starts the API on **http://localhost:5000**.

---

### Frontend Setup (React + Vite)

1. **Navigate to the frontend directory**:
   ```bash
   cd Credistx-main/frontend
   ```
2. **Install dependencies**:
   ```bash
   npm install
   ```
3. **Start the development server**:
   ```bash
   npm run dev
   ```
   The frontend should now be accessible at **http://localhost:5173**.

---

## How It Works

### Backend API Endpoints

- **GET /**  
  - **Description**: Returns a simple welcome message indicating that the Ethical Scraper API is active.

- **POST /scrape**  
  - **Description**: Accepts JSON payloads containing:
    - `platform`: The social media platform (e.g., `"youtube"`, `"instagram"`, `"facebook"`).
    - `url`: The URL from which to scrape data.
    - `scrape_type`: The type of data requested (e.g., `"comments"`, `"followers"`).
  - **Processing**:
    - Depending on the `platform`, the endpoint calls the appropriate function:
      - For YouTube: Retrieves detailed video information using the YouTube API.
      - For Instagram and Facebook: Leverages Selenium and BeautifulSoup (with noted limitations).
  - **Response**: Returns JSON data with the scraped results or an error message if the platform is unsupported or if required parameters are missing.

### Frontend User Flow

1. **User Input**:  
   - The user enters a URL and selects a scrape type from the dropdown.
2. **API Request**:  
   - Upon clicking the “Scrape” button, Axios sends a POST request to the backend.
3. **Data Display**:  
   - The scraped results (or any errors) are displayed in real time on the interface.

---

## Configuration & Environment Variables

For the backend to function correctly, you need to set the following environment variables:

- **YOUTUBE_API_KEY**: Your API key for accessing the YouTube Data API.
- **INSTAGRAM_API_KEY**: (If applicable) API key for Instagram data.
- **FACEBOOK_API_KEY**: (If applicable) API key for Facebook data.

These keys are used within the application to authenticate and fetch data securely.

---

## Technologies Used

- **Backend**:
  - **Python** & **Flask**: For building RESTful APIs.
  - **Selenium**: To handle dynamic content rendering.
  - **BeautifulSoup**: For parsing HTML content.
  - **Requests**: For making HTTP calls (e.g., YouTube API requests).

- **Frontend**:
  - **React**: For building a dynamic user interface.
  - **Vite**: A fast development build tool.
  - **Axios**: For handling HTTP requests to the backend.
  - **ESLint**: For code quality and consistency.

- **Others**:
  - **CORS**: Middleware to enable cross-origin requests.
  - **Environment Management**: Using environment variables for secure API key management.

---

## Ethical Considerations & Limitations

- **API Key Limitations**:  
  - The YouTube scraping functionality requires a valid API key.  
  - Scraping Instagram and Facebook may require additional permissions and can be subject to the platform’s Terms of Service.
  
- **Usage Guidelines**:  
  - Use this tool responsibly, adhering to GDPR, CCPA, and other data privacy regulations.
  - Avoid excessive scraping that could overload target servers or breach service terms.
  
- **Legal Compliance**:  
  - Ensure that your usage of this tool complies with local laws and platform-specific policies.

---

## Contributing

Contributions are welcome! If you’d like to help improve Credistx:

1. **Fork the repository**.
2. **Create a new branch** for your feature or bug fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Commit your changes** with clear and descriptive messages.
4. **Push your branch** to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Open a pull request** detailing your changes and the problem they solve.

For major changes, please open an issue first to discuss what you would like to change.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Contact

For any questions, issues, or contributions, please open a GitHub Issue or contact the maintainers directly via the repository’s contact channels.

---
