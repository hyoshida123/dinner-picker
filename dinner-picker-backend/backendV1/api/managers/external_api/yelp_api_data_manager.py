import requests
from api.config.yelp_api_config import headers, yelp_business_endpoint

class YelpAPIDataManager:
    """
    For communicating with Yelp API

    @see api.config_variables.yelp_api_config
    @author: Hideki Yoshida
    """
    def __init__(self):
        pass

    """
    Given a search word, return a list of dictionaries that contain a list of restaurants' information
    in the area.

    @param Required location: type string
    @param Optional kwargs:
        term=string (If term isn’t included it searches everything. The term keyword also accepts business names such as "Starbucks".)
        price=int (Integer between 1-4. The price filter can be a list of comma delimited pricing levels.
            For example, "1, 2, 3" will filter the results to show the ones that are $, $$, or $$$.)
        radius=int (Radius in meters. If the value is too large, a AREA_TOO_LARGE error may be returned.
            The max value is 40000 meters (25 miles).)
        sort_by=string (Sort the results by one of the these modes: best_match, rating, review_count or distance.)
        open_now=boolean (When set to true, only return the businesses open now. ***Notice that open_at and open_now cannot be used together.***)
        open_at=int (Integer represending the Unix time in the same timezone of the search location.
            If specified, it will return business open at the given time. ***Notice that open_at and open_now cannot be used together.***)
    """
    def get_restaurant_info(self, location, **kwargs):
        business_search_endpoint = get_endpoint_for('search')
        params = get_params_for(business_search_endpoint, location, kwargs)
        business_info = get_response_of(business_search_endpoint, headers, params=params).json()

        if 'error' in business_info:
            raise Exception(business_info['error'])

        business_info_list =  business_info['businesses']
        return business_info_list

    """
    Given a restaurant's ID, return a dictionary that contains a business hour information 
    of the restaurant.
     
    @param id: type string
    
    """
    def get_business_hours(self, id):
        business_hour_endpoint = get_endpoint_for(id)
        business_hour_json_data = get_response_of(business_hour_endpoint, headers=headers)
        business_hour_data_list = business_hour_json_data.json()['hours']
        business_hour_dict = business_hour_data_list[0]
        return business_hour_dict

    # TODO 
    # Don't have a VIP access to API yet.
    def get_more_business_details(self):
        return '***TODO***'

def get_response_of(endpoint, headers, **kwargs):
    if kwargs:
        headers = get_headers_for(endpoint)
        return requests.get(endpoint, params=kwargs['params'], headers=headers)
    else:
        headers = get_headers_for(endpoint)
        return requests.get(endpoint, headers=headers)


def get_params_for(endpoint, location, args):
    params = {'location': location}
    if args:
        for key, value in args.items():
            params[key] = value
    return params

def get_headers_for(endpoint):
    return headers

def get_endpoint_for(path):
    return yelp_business_endpoint + path
