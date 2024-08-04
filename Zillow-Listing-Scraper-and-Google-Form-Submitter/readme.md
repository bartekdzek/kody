**Zillow Listing Scraper and Google Form Submitter**

This project is a Python script designed to scrape rental listings from a cloned Zillow website and automatically submit the data to a Google Form. The data submitted to the Google Form is then collected in a linked Google Sheets spreadsheet for easy access and analysis.

**Features**

- Web Scraping: Extracts property listings including addresses, prices, and links from the Zillow clone website.
- Automated Form Submission: Uses Selenium to automatically fill and submit a Google Form for each property listing.
- Data Collection: Aggregates the scraped data in a Google Sheets spreadsheet, making it easy to manage and analyze the listings.
*Prerequisites*

- Python 3.12
- requests library
- BeautifulSoup library from bs4
- selenium library
- Google Chrome and ChromeDriver

**How It Works**

The script performs the following steps:

1. Scrape the Zillow Clone Website:

- Sends a GET request to the Zillow clone website to fetch the HTML content.
- Parses the HTML using BeautifulSoup to extract the links, addresses, and prices of the property listings.

2. Submit Data to Google Form:
- Configures Selenium WebDriver with Chrome options.
- Iterates through each listing and navigates to the Google Form URL.
- Fills in the form fields with the scraped data and submits the form.
- Each submission is collected in the linked Google Sheets spreadsheet.


**Usage**

- Run the Script: Execute the script to start the scraping and form submission process. The script will open Google Chrome, navigate to the Google Form, and submit the data for each property listing.

- Access Submitted Data: The data submitted via the Google Form can be accessed in the linked Google Sheets spreadsheet (https://docs.google.com/spreadsheets/d/1vqxLbWWiQZtYBc7X_bTLjAJgsRH1TazoXEx49XYi4yk/edit?usp=sharing).

This project automates the tedious process of manually collecting and entering property listing data, making it easier to manage and analyze rental listings from the Zillow clone website.
