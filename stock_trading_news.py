import requests  # Import the requests library to make HTTP requests

# Define the stock name and company name
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Define the endpoints for the stock and news APIs
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# Define the API keys for the stock and news APIs
STOCK_API_KEY = ""
NEWS_API_KEY = ""

# Define the parameters for the stock API request
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

# Make a GET request to the stock API and get the response
response = requests.get(STOCK_ENDPOINT, params=stock_params)
# Parse the JSON response to get the time series data
data = response.json()["Time Series (Daily)"]
# Convert the time series data into a list of dictionaries
data_list = [value for (key, value) in data.items()]
# Get the closing price for yesterday
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(f"Yesterday closing price = {yesterday_closing_price}")

# Get the closing price for the day before yesterday
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(f"Day before yesterday closing price = {day_before_yesterday_closing_price}")

# Calculate the difference between the two closing prices
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
# Determine the direction of the price change
up_down = "🔺" if difference > 0 else "🔻"

# Calculate the percentage difference
diff_percent = round((difference / float(yesterday_closing_price)) * 100)
print(f"Rounded percent difference = {diff_percent}")

# Check if the percentage difference is greater than 1%
if abs(diff_percent) > 1:
    # Define the parameters for the news API request
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    # Make a GET request to the news API and get the response
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    # Parse the JSON response to get the articles
    articles = news_response.json()["articles"]

    # Get the first three articles
    three_articles = articles[:3]

    # Format the articles into a list of strings
    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}"
        for article in three_articles
    ]

    # Join the formatted articles into a single string
    formatted_articles_string = "\n\n".join(formatted_articles)
    print(formatted_articles_string)


