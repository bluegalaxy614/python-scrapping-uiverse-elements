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
    ```

2. **Create a Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the Required Python Packages**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up ChromeDriver**

    Download the ChromeDriver that matches your version of Chrome from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads). Place it in a directory and note the path for the `.env` file.

5. **Set Up MongoDB**

    Ensure you have a MongoDB server running, either locally or on the cloud. Obtain your MongoDB connection string, which you'll use in the `.env` file.

## Usage

### Running the Scraper

1. **Set Environment Variables**

    Create a `.env` file in the root directory of the project and add the following variables:

    ```plaintext
    TARGET_URL=https://uiverse.io
    DB_URL=mongodb://localhost:27017
    DB_NAME=mydatabase
    DB_COLLECTION=mycollection
    CHROME_DRIVER_PATH=/path/to/chromedriver
    ```

    Replace `/path/to/chromedriver` with the actual path to your ChromeDriver executable.

2. **Run the Scraper**

    Run the scraper using the command:

    ```bash
    python scraper.py
    ```

    The script will begin scraping the specified URL, extract the required data, and store it in the MongoDB database you configured.

### Data Output

The data is stored in a MongoDB collection, with each document containing fields like:

- **category**: The category of the scraped element.
- **tag**: The specific tag associated with the element.
- **style**: The style type (e.g., tailwind, css).
- **link**: The link to the source of the data.
- **html**: Extracted HTML code.
- **css**: Extracted CSS code.
- **views**: The number of views the element has.
- **tags**: Associated tags.
- **report_date**: The date of the report or last update.

## Environment Variables

The project relies on the following environment variables set in the `.env` file:

- **TARGET_URL**: The base URL of the site you want to scrape.
- **DB_URL**: The MongoDB connection string.
- **DB_NAME**: The name of the MongoDB database where data will be stored.
- **DB_COLLECTION**: The name of the MongoDB collection.
- **CHROME_DRIVER_PATH**: The full path to the ChromeDriver executable.

## Project Structure

    ```plaintext
    selenium-web-scraper/
    │
    ├── .env                # Environment variables
    ├── scraper.py          # Main Python script
    ├── requirements.txt    # Python dependencies
    ├── README.md           # This README file
    └── venv/               # Virtual environment directory

## Contributing

    If you would like to contribute to this project, please feel free to fork the repository and submit a pull request. Alternatively, you can open an issue for any bug reports or feature requests.
