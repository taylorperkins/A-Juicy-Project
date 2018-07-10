from flask import jsonify, redirect

from a_juicy_project import app

from a_juicy_project.logic.nutritionix_service import NutritionIxServiceError


@app.errorhandler(NutritionIxServiceError)
def handle_nutritionix_service_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.errorhandler(404)
def page_not_found(e):
    return redirect('/'), 404
