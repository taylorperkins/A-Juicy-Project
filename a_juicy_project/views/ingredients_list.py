from copy import deepcopy

from flask import render_template

from a_juicy_project import app, nutritionix_service

from a_juicy_project.logic.ingredient_list_hash import update_ingredients_list


@app.context_processor
def utility_processor():
    def convert_ingredients_to_class(ingredients):
        return ' '.join(['ingredient-' + str(ingredient[0]) for ingredient in ingredients])
    return dict(convert_ingredients_to_class=convert_ingredients_to_class)


@app.route('/', methods=['GET'])
def ingredient_list():
    products = nutritionix_service.get_products()

    total_products = products['total_hits']

    product_ingredient_map = list()

    product_results = deepcopy(products['hits'])
    ingredients_map = dict()

    for product in product_results:
        product_id = product['_id']

        nf_ingredient_statement = product['fields']['nf_ingredient_statement'] if product['fields']['nf_ingredient_statement'] else 'NA'

        product_ingredient_list = update_ingredients_list(nf_ingredient_statement, ingredients_map)

        product_ingredient_map.append({
            'product_ingredient_list': product_ingredient_list,
            'row': [product['fields']['item_name'], nf_ingredient_statement, product_id]
        })

    col_names = ['Item Name', 'Ingredients', 'ID']

    return render_template(
        'index.html',
        total_products=total_products,
        product_ingredient_map=product_ingredient_map,
        ingredients_map=ingredients_map,
        col_names=col_names
    )


