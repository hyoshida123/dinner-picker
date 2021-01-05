"""

Config variables for Yelp API

@see api.manager.yelp_api_data_manager
"""
content_type = 'application/json'
api_key = 'EcG7QH-0Zvv-xft8StgjxgYrSWmOGfvMU07K2kqNAh2fNAoygJ7vCc3gyrzE_iP8V6jeeaPxa8PwA6uEaWw8Mj8oTjpfKKyA-LBOM-xOjTEPKOWsOEpEWPDO8FNAW3Yx'

headers = {
    'Content-Type': content_type,
	'Authorization': 'Bearer ' + api_key
}

yelp_business_endpoint = 'https://api.yelp.com/v3/businesses/'