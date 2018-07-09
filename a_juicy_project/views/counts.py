from flask import jsonify

from a_juicy_project import app, nutritionix_service


@app.route('/counts', methods=['GET'])
def get_counts():
    products = nutritionix_service.get_products()

    return jsonify({'total_products': products['total_hits']})
