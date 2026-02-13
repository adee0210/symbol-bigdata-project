from datetime import datetime, timezone
import time
import json
import cloudscraper

from ckvn.stock.candlestick.configs.config import SYMBOL_API


def logic():
    day = 180
    end_time = int(datetime.now(tz=timezone.utc).timestamp())
    stack = day * 24 * 60 * 60
    start_time = end_time - stack
    i = 0

    while True:
        scraper = cloudscraper.create_scraper()

        url = (
            str(SYMBOL_API["investing_api"])
            .replace("=symbol", "VCB")
            .replace("=from", f"={start_time}")
            .replace("=to", f"={end_time}")
        )
        response = scraper.get(url=url)
        data = response.json()
        if data.get("s") != "no_data" and data.get("s") is not None:
            with open(f"/home/duc/symbol-bigdata-project/data/data_{i}.json", "w") as f:
                json.dump(data, f)
            end_time = start_time - 60
            start_time = end_time - stack
            print(f"crawl data {i}")
            i += 1
            time.sleep(10)
        else:
            print("Done")
            break


logic()
