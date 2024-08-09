# Selenium Web Scraper with MongoDB Storage

This project is a Python-based web scraper that uses Selenium to extract data from websites and stores it in a MongoDB database. The script scrapes specific elements from web pages, such as CSS and HTML code snippets, view counts, tags, and report dates, and organizes this data by category, tag, and style.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- Python 3.9+
- [MongoDB](https://www.mongodb.com/)
- [Google Chrome](https://www.google.com/chrome/)
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/selenium-web-scraper.git
   cd selenium-web-scraper

2. **Create a Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install the Required Python Packages**

    ```bash
    pip install -r requirements.txt

4. **Set Up ChromeDriver**

    Download the ChromeDriver that matches your version of Chrome.

5. **Set Up MongoDB**

    Ensure you have a MongoDB server running, either locally or on the cloud.
    Get your MongoDB connection string, which you'll use in the .env file.

## Usage

### Running the Scraper

1. **Set Environment Variables**

    Create a .env file in the root directory and add the following variables:

    TARGET_URL=https://uiverse.io/
    DB_URL=mongodb://localhost:27017/
    DB_NAME=mydatabase
    DB_COLLECTION=mycollection
    CHROME_DRIVER_PATH=/path/to/chromedriver

    Replace /path/to/chromedriver with the actual path to your ChromeDriver executable.

2. **Run the Scraper**

  ```bash
    python scraper.py

    The script will begin scraping the specified URL, extract the required data, and store it in the MongoDB database you configured.

## Data Output

    The data is stored in a MongoDB collection, with each document containing fields like:

    category: The category of the scraped element.
    tag: The specific tag associated with the element.
    style: The style type (e.g., tailwind, css).
    link: The link to the source of the data.
    html: Extracted HTML code.
    css: Extracted CSS code.
    views: The number of views the element has.
    tags: Associated tags.
    report_date: The date of the report or last update.

## Environment Variables

    The project relies on the following environment variables:

    TARGET_URL: The base URL of the site you want to scrape.
    DB_URL: The MongoDB connection string.
    DB_NAME: The name of the MongoDB database where data will be stored.
    DB_COLLECTION: The name of the MongoDB collection.
    CHROME_DRIVER_PATH: The full path to the ChromeDriver executable.

## Contributing

    If you would like to contribute, feel free to create a pull request or open an issue.

## License

### How to Use:
    - Replace `"https://example.com"` in `TARGET_URL` with the actual target website URL.
    - Update the MongoDB connection string, database name, collection name, and ChromeDriver path in the `.env` file.

### Key Sections:
- **Installation**: Step-by-step instructions to set up your environment.
- **Usage**: How to configure and run the scraper.
- **Environment Variables**: Details on necessary configuration settings.

This `README.md` file is a complete guide for anyone who wants to understand, set up, and run your Selenium-based web scraper project.
