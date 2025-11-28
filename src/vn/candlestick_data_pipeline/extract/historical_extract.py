import cloudscraper

url = "https://tvc4.investing.com/4379fbb3b2cf9327a768dbfde5d69d1d/1761556750/52/52/110/history?symbol=ACB&resolution=1&from=1609459200&to=1672531199"

scraper = cloudscraper.create_scraper(
    browser={"browser": "chrome", "platform": "windows", "mobile": False}
)

headers = {
    "User-Agent": scraper.headers["User-Agent"],
    "Accept": "application/json, text/plain, */*",
    "Referer": "https://www.investing.com/",
    "Connection": "keep-alive",
}

response = scraper.get(url, headers=headers)
print(response.text)
