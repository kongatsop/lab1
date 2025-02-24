import requests  # εισαγωγή της βιβλιοθήκης
import datetime

def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break
'''
url = 'http://python.org/'  # προσδιορισμός του url

with requests.get(url) as response:  # το αντικείμενο response
    html = response.text
    more(html)'''


url=input("give url:\t")


if not url.startswith('https://'):
    url='https://'+url

print(url)

with requests.get(url) as response:
    for key in response.headers:
        print(f"{key}:[]{response.headers[key]}")
    
    print(f"Server:{response.headers.get('Server')}")


    if "set-cookie" in response.headers.keys():
        cookies = response.cookies
        for cookie in cookies:
            print(f"\n Uses cookies.\nName: {cookie.name}\nValue: {cookie.value}\nExpiration Date: {datetime.datetime.fromtimestamp(float(cookie.expires)) if cookie.expires is not None else 'Does Not Expire'}")        
    else:
        print('\n Does not use cookies')
