import requests
import datetime as dt

from twilio.rest import Client
account_sid = '' #add yours
auth_token = "" #add yours
client = Client(account_sid, auth_token)


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

NEWS_APIKEY = "28a6822d9c1b46da80c1a96e368f8ca4"
STOCK_APIKEY = "180S93C53G7YR5LV"
TWILIO_API = "VB39UQ4G33HX12YXTECNRM6Y"

today = dt.date.today()
yesterday = today - dt.timedelta(days=1)
DByesterday = today - dt.timedelta(days=2)

print(yesterday)
print(DByesterday)

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price.

stock_param = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":STOCK_APIKEY
}
response = requests.get(url=STOCK_ENDPOINT,params=stock_param)
data = response.json()
stock_yesterday = data["Time Series (Daily)"][str(yesterday)]["4. close"]
stock_DByesterday = data["Time Series (Daily)"][str(DByesterday)]["4. close"]

if abs(float(stock_yesterday)-float(stock_DByesterday))>=2:
    
    ## STEP 2: Use https://newsapi.org/docs/endpoints/everything
    # Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
    #HINT 1: Think about using the Python Slice Operator

    news = requests.get(url=f"https://newsapi.org/v2/everything?q={STOCK}&from={DByesterday}&to={yesterday}&pageSize=3&sortBy=popularity&apiKey={NEWS_APIKEY}") #intentionally hard coded to explore all possibilities
    newsdata = news.json()
    
    
    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    # Send a separate message with each article's title and description to your phone number. 
    #HINT 1: Consider using a List Comprehension.
    
    message = client.messages.create(
    messaging_service_sid='MG46bfa036904c66fef26b68245736747f',
    body=f"""tesla Price fluctuating !! \n 
    {newsdata["articles"][0]["description"]} \n {newsdata["articles"][1]["description"]}
    """,
    to='+919663064308'
    
)
    


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

