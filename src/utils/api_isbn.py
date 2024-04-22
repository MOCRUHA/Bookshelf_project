import requests as req

def isbn_api_call(isbn):

#api request for isbn
	resp = req.get(f'https://brasilapi.com.br/api/isbn/v1/{isbn}').json()
	print(resp)
#fields of intrest from json response
	fields = ['isbn','title','subtitle','authors','publisher','year','page_count']

	data = []

	
#create a list complete with the necessary fields
	for f in fields:
		if resp[f] == None:
			data.append(None)
		if f == 'authors':
			na = len(resp[f])
			for author in resp[f]:
				data.append(resp[f])
			for n in (4 - na):
				data.append(None)

		else:
			data.append(resp[f])
	print(data)
	return data