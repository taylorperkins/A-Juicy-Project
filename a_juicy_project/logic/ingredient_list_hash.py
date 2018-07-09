import re


def update_ingredients_list(ing_list, ingredients, product_id):
    # we want to remove periods
    if ingredients[-1] == '.':
        ingredients = ingredients[:-1]

    ingredients = re.sub(r', and', ',', ingredients)
    ingredients = re.sub(r', \(', ' (', ingredients)

    # Now we want to iterate through all the characters, checking for both commas and parenthesis
    # Comma denotes new ingredient, where parenthesis denotes the small print stuff
    index = 0
    small_print = ''

    while True:
        ing_len = len(ingredients)

        if index == ing_len or ingredients[index] == ',':
            ingredient = ingredients[:index].strip().lower()
            ing_list[ingredient][product_id] = small_print

            # break out of the loop here
            if index == ing_len:
                return

            small_print = ''

            # Skipping the comma
            ingredients = ingredients[index + 1:].lstrip()

            index = 0

        # find the closing piece and delete it, while keeping track of the small print
        elif ingredients[index] == '(':
            small_print_match = re.search(r'\((.*?)\)', ingredients)
            if small_print_match:
                # Keep track, then move to the end of the match.
                small_print = small_print_match.group(1)
                ingredients = ingredients[:small_print_match.start()] + ingredients[small_print_match.end():]

        else:
            index += 1
