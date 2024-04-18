import requests as req

def isbn_api_call(isbn):

#api request for isbn
	resp = req.get(f'https://brasilapi.com.br/api/isbn/v1/{isbn}').json()

#fields of intrest from json response
	fields = ['isbn','title','subtitle','authors','publisher','year','page_count']

	data = []

	
#create a list complete with the necessary fields
	for f in fields:
		#data.append(str(resp[f]).strip('[]'))
		data.append(resp[f])
	return data