import requests
import json
import time
from keep_alive import keep_alive
keep_alive()
tokens = [
    "1715922407329nKJqrcrcyFQfYecFbsrWvDMwbsjQwc9hEGNp1l7PpYYJeApVSoEUfyW9VWzwQOBh1606557047",
    "1716197037904BlFdYWbcPw0LzMzmt1TquejTwBfIlOa3H5ewZuJcyfrccxeKlrO9vQl46FUnyqJl7195822647",
    "1716200751287PGmYUJWiTyTFxuoJnDYFqRBuSr7QXa86XrO2nsKMz5mIR45d1wYEPK9WhYUdYtWd5611407285",
    "1716202378814omLJwOGEx6RkRq8ZKTOgfNt2efzd6PMzUFwPkI6kjHQUhpFBZmTh2K2DD6TOj1Zt7158065365",
    "1716203118744xBfQUMWNDLu5vrifyggl3xQ42PVa02gpNpPuP3HWSaZpck64AaabS6NLYgcVFIej6880544702",
    "1716204030954NeZwRYV0ytsuihtyDJePq4yjOLAcSUxuEzpNu1L1KXTqYFfconVGZyA7BwCpHy2Y7052127034"
]

general_headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 9; CPH2015 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36",
	  'Accept-Encoding': "gzip, deflate",
	  'origin': "https://hamsterkombat.io",
	  'x-requested-with': "org.telegram.messenger",
	  'sec-fetch-site': "same-site",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-dest': "empty",
	  'referer': "https://hamsterkombat.io/",
	  'accept-language': "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"
}

def sync(token):
	url = "https://api.hamsterkombat.io/clicker/sync"
	
	general_headers['authorization'] ='Bearer ' + token
	
	req = requests.post(url, headers=general_headers).json()
	
	availableTaps = req['clickerUser']['availableTaps']
	
	return availableTaps

def clicker_tap(tok):
	url = "https://api.hamsterkombat.io/clicker/tap"
	availableTaps = sync(tok)
	payload = {
  "count": 100,
  "availableTaps": availableTaps,
  "timestamp": int(time.time())
}

	general_headers['authorization'] ='Bearer ' + tok

	response = requests.post(url, json=payload, headers=general_headers).json()
	
	print(f" Your Balance: {response['clickerUser']['balanceCoins']}")
while True:
	time.sleep(2)
	for data in tokens:
		try:
			clicker_tap(data)
		except Exception as e:
			print('Error: '+ e)
	print('='*40)
			
