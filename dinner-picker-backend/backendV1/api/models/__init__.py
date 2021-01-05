"""
SANG:
Add models in this __init__.py file. Create a model in a seperate file and import them here. Then migration will be
handled automatically.
"""

from api.models.snippet.models import Snippet
from api.models.user_account.user_account_model import User
from api.models.preference.preference_model import Preferences
from api.models.preference.food_category_model import FoodCategoryLiked
from api.models.preference.food_category_model import FoodCategoryDisliked
from api.models.group.group_model import Group