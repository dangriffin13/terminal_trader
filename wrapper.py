import requests

class Markit:
	def __init__(self):
        # ?input=
		self.lookup_url = "http://dev.markitondemand.com/Api/v2/Lookup/json"
        # ?symbol=
		self.quote_url = "http://dev.markitondemand.com/Api/v2/Quote/json"

	def company_search(self,string):
		response = requests.get(self.lookup_url + "?input=" + string)
		
		if not response.json():
			return 0
		else:
			return response.json()


		# print("json:", response.json())
		# symbol = response.json()[0]['Symbol']
		# exchange = response.json()[0]['Exchange']
		# name = response.json()[0]['Name']

		# print("Symbol:", symbol)
		# print("Exchange:", exchange)
		# print("Name:", name)

		# r.raise_for_status()

	def get_quote(self,string):
		response = requests.get(self.quote_url + "?symbol=" + string)
		
		if response.json().get("Symbol") is None:
			return 0
		else:
			return response.json()

		# print(response.json())
		# print("status code:", response.status_code)
		# print("status:", response.raise_for_status())
		# print("json:", response.json())
		# symbol = response.json()['Symbol']
		# quote = response.json()['LastPrice']
		# time = response.json()['Timestamp']

		# print("Symbol:", symbol)
		# print("Last Price:", quote)
		# print("Time:", time)