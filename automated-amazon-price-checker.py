from bs4 import BeautifulSoup
import requests
import smtplib

URL = "https://appbrewery.github.io/instant_pot/"
BUY = None

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

price_span_class = soup.find_all("span", class_="a-offscreen")
price_span = price_span_class[0]
price = price_span.text
price_parts = price.split('$')
price_float = float(price_parts[1])


if price_float < 90:
    message = f"STEAL ALERT! The NEW  price is: {price}!!!"
    BUY = True
else:
    message = f"The price is: {price}. :<"
    BUY =False

print(message)


#sending message via gmail
if BUY:
    SMTP_ADDRESS="smtp.gmail.com"
    EMAIL_ADDRESS="*********@gmail.com" 
    EMAIL_PASSWORD="********"
    smtplib.SMTP("smtp.gmail.com", port=587)

    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_ADDRESS,
            to_addrs=EMAIL_ADDRESS,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )