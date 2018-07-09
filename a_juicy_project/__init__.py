from flask import Flask

from a_juicy_project.config import NUTRITIONIX_API_KEY, NUTRITIONIX_APP_ID

from a_juicy_project.logic.nutritionix_service import NutritionIxService


app = Flask(__name__)

nutritionix_service = NutritionIxService(
    base_uri='https://api.nutritionix.com/v1_1/',
    api_key=NUTRITIONIX_API_KEY,
    app_id=NUTRITIONIX_APP_ID
)


import a_juicy_project.views
