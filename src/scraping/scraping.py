import requests


def scrape(url, extractor):
    headers = {
        'authority': 'www.amazon.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    # Download the page using requests
    print("Downloading %s" % url)
    r = requests.get(url, headers=headers)
    # Simple check to check if page was blocked (Usually 503)
    if r.status_code > 500:
        if "To discuss automated access to Amazon data please contact" in r.text:
            print("Page %s was blocked by Amazon. Please try using better proxies\n" % url)
        else:
            print("Page %s must have been blocked by Amazon as the status code was %d" % (url, r.status_code))
        return None
    # Pass the HTML of the page and create
    return extractor.extract(r.text)


def parse(response_data, writer, max_retries=100):
    try:
        for index, review in enumerate(response_data['reviews']):
            review["product"] = response_data["product_title"]
            if 'verified' in review:
                if 'Verified Purchase' in review['verified']:
                    review['verified'] = 'Yes'
                else:
                    review['verified'] = 'Yes'
            review['rating'] = review['rating'].split(' out of')[0]
            date_posted = review['date'].split('on ')[-1]
            if review['images']:
                review['images'] = "\n".join(review['images'])
            # r['date'] = dateparser.parse(date_posted).strftime('%d %b %Y')
            writer.writerow(review)
        # sleep(5)
    except (TypeError, AttributeError):
        print(f'WAR review ignored because does not contain valid content... ')
        pass

if __name__ == '__main__':
    print('1')