from rest_framework.views import APIView
from rest_framework.response import Response
from ..converter.yelp_data_converter import YelpDataConverter
from api.managers.external_api.yelp_api_data_manager import YelpAPIDataManager
from api.util.decorators import deprecated_function

USERS = [
    {
        'name': 'Hideaki Yoshida',
        'user_preferences': {
            'food_categories_like': [
                'cajun',
                'russian',
                'american',
            ],
            'food_categories_dislike': [
                'pizza',
                'chicken_wings',
                'sandwiches',
            ],
            'food_spicy': 2,
            'food_vegan': -1,
            'food_vegetarian': -2,
            'place_loud': 2,
            'place_price': 3,
        },
    },
    {
        'name': 'Frank Yang',
        'user_preferences': {
            'food_categories_like': [
                'seafood',
                'french',
                'american'
            ],
            'food_categories_dislike': [
                'bakeries',
                'vegan',
            ],
            'food_spicy': -2,
            'food_vegan': -3,
            'food_vegetarian': -3,
            'place_loud': -1,
            'place_price': 2,
        },
    },
]

@deprecated_function
def score_food_categories(restaurant, user):
    max_score = len(user['user_preferences']['food_categories_like']) + len(user['user_preferences']['food_categories_dislike'])
    score = 0
    restaurant_food_categories = map(lambda category: category['alias'], restaurant['categories'])
    for food_category_like in user['user_preferences']['food_categories_like']:
        if food_category_like in restaurant_food_categories:
            score += 1
    for food_category_dislike in user['user_preferences']['food_categories_dislike']:
        if food_category_dislike in restaurant_food_categories:
            score -= 1
    return score / max_score

@deprecated_function
def score_place_price(restaurant, user):
    # Convert both restaurant price and user desired price into range between 0 and 1
    # Larger differences between the restaurant and user desired prices signify more of a mismatch
    # Difference is of range 0 to 1. difference = 0 equates to score = 1 (max positive score), while difference = 1 equates to score = -1
    difference = abs((restaurant['price'] / 4) - ((user['user_preferences']['place_price'] + 3) / 6))
    return ((-difference) + 1) * 2
  
class SuggestRestaurants(APIView):
    """
    Given a list of user preferences, group preferences and time, returns a list of restaurants ordered by relevance
    """
    @deprecated_function
    def get(self, request):
        yelp = YelpAPIDataManager()
        converter = YelpDataConverter(yelp.get_restaurant_info('Berkeley'))
        converter.convert_price_to_score()
        restaurants = converter.yelp_data
        # return Response(yelp.get_restaurant_info('Berkeley'), status=200)
        users = USERS
        max_score_per_user = 100 / len(users)
        # For each restaurant, assign a score from each user based on how their preferences compare/contrast to the restaurant details
        for restaurant in restaurants:
            for user in users:
                score = 0
                score += score_food_categories(restaurant, user)
                score += score_place_price(restaurant, user)
                if not score in restaurant:
                    restaurant['score'] = (score / 2) * max_score_per_user
                else:
                    restaurant['score'] += (score / 2) * max_score_per_user
        restaurant_names_and_scores = list(map(lambda restaurant: {'name': restaurant['name'], 'score': restaurant['score']}, restaurants))
        restaurant_names_and_scores.sort(key=lambda restaurant: restaurant['score'], reverse=True)
        return Response(restaurant_names_and_scores, status=200)