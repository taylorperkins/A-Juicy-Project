

class Calories(object):
    @classmethod
    def get_avg_calories(cls, products):
        avg_calories = list()

        for product in products['hits']:
            unit = product['fields']['nf_serving_size_unit'].lower()

            if unit in ['fl oz', 'fl oz conc']:
                total_fl_oz = cls._calculate_fl_oz_from_fl_oz(product)
                avg_calories.append(cls._write_fl_oz(total_fl_oz, product))

            elif unit == 'ml':
                total_fl_oz = cls._calculate_fl_oz_from_ml(product)
                avg_calories.append(cls._write_fl_oz(total_fl_oz, product))

            else:
                avg_calories.append(cls._write_error(product, unit))

        return avg_calories

    @staticmethod
    def _calculate_fl_oz_from_ml(product):
        nf_serving_size_qty = product['fields']['nf_serving_size_qty']
        nf_servings_per_container = product['fields']['nf_servings_per_container']

        return (nf_serving_size_qty * nf_servings_per_container) * 0.033814

    @staticmethod
    def _calculate_fl_oz_from_fl_oz(product):
        nf_serving_size_qty = product['fields']['nf_serving_size_qty']
        nf_servings_per_container = product['fields']['nf_servings_per_container']

        return nf_serving_size_qty * nf_servings_per_container

    @staticmethod
    def _write_fl_oz(total_fl_oz, product):
        nf_calories = product['fields']['nf_calories']

        return {
            product['_id']: dict(
                avg_calories_per_fl_oz=(1.0 / float(total_fl_oz)) * nf_calories,
                **product['fields']
            )
        }

    @staticmethod
    def _write_error(product, unit):
        return {
            product['_id']: {
                'name': product['fields']['item_name'],
                'avg_calories_per_fl_oz': 'NA',
                'error': 'Cannot convert {unit} to fl oz'.format(unit=unit)
            }
        }
