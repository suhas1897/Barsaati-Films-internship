Selenium Barsaati Tech Internship - Assignment Submission Form

# Twitter Trends Scraper

This Flask application scrapes the latest trending topics from Twitter and stores them in a MongoDB database. The application uses Selenium for web scraping and a proxy for accessing Twitter.

## Prerequisites

Before running the application, make sure you have the following installed:

- Python 3.x
- pip (Python package installer)
- MongoDB
- GeckoDriver (for Firefox)
- Firefox browser

## Installation


GeckoDriver Setup:

Make sure geckodriver is installed and accessible from your system's PATH. You can download it from GeckoDriver releases and follow the installation instructions for your operating system.

Proxy Setup:

Replace the proxy settings in the code with your own proxy details if needed.


app.py:

The main Flask application which includes:

WebDriver setup with proxy.
MongoDB client setup.
Routes for the web interface (/ and /scrape).
Selenium logic for scraping Twitter trends.
requirements.txt:

Contains the list of Python packages required to run the application.

templates/index.html:

HTML template for the web interface.

Important Notes
Ensure your Twitter login credentials are valid and correctly entered in the app.py file.
The script is configured to use Firefox as the browser for Selenium. Make sure you have Firefox installed.
Adjust the WebDriverWait timeouts as needed based on your network speed and Twitter's response time.




1. Clone the repository:

```bash
git clone https://github.com/yourusername/twitter-trends-scraper.git
cd twitter-trends-scraper
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`

mongod

python app.py

twitter-trends-scraper/
│
├── app.py             # Main Flask application
├── requirements.txt   # List of required Python packages
├── templates/
│   └── index.html     # HTML template for the web interface
└── README.md          # This README file

```

## Images && Video

[selinium.1](https://github.com/suhas1897/Barsaati-Films-internship/issues/1#issue-2337521970)


![image1](https://github.com/suhas1897/Barsaati-Films-internship/assets/170518948/847a68e9-acd4-47de-8f51-2389c8b84dfb)

****
![app python](https://github.com/suhas1897/Barsaati-Films-internship/assets/170518948/558bd7c4-4d2a-40a0-96fa-4baae30b7198)

****

![html code](https://github.com/suhas1897/Barsaati-Films-internship/assets/170518948/259d99c4-c72e-4bd5-bb8f-34b77b9eae49)





