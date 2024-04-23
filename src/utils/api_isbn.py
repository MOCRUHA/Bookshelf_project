import requests as req

def isbn_api_call(isbn):

#api request for isbn
	resp = req.get(f'https://brasilapi.com.br/api/isbn/v1/{isbn}').json()
	print('-----API CALL RESULT JSON:\n')
	print(resp, '\n')
#fields of intrest from json response
	#fields = ['isbn','title','subtitle','authors','publisher','year','page_count']

	#data = []

	
#create a list complete with the necessary fields

	return resp