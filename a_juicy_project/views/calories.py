from flask import jsonify

from a_juicy_project import app, nutritionix_service

from a_juicy_project.logic.calories import Calories


@app.route('/calories', methods=['GET'])
def get_avg_calories():
    """
    Note that there are many types of unit references from this api.
    Here are all of the unique serving size units:

    {'bottle', 'box', 'can', 'ea', 'fl oz', 'fl oz conc', 'mL', 'ml', 'oz', 'pop', 'pops', 'pouch'}

    For this endpoint, we will assume that 'fl oz', 'fl oz conc' and 'oz' are the same

    Some of the units cannot be converted to fl oz, so they will be filled with an 'error' message, example being pop

    'ml' can be converted to fl oz.
    1 fl oz == 29.5735 ml

    :return:
    """
    products = nutritionix_service.get_products()

    avg_calories = Calories.get_avg_calories(products)

    return jsonify(avg_calories)
