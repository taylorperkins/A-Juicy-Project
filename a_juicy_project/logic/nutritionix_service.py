import json

import requests

from a_juicy_project.base_api_exception import BaseAPIException


class NutritionIxServiceError(BaseAPIException):
    pass


class NutritionIxService(object):
    def __init__(self, base_uri, api_key, app_id):
        self._base_uri = base_uri
        self._api_key = api_key
        self._app_id = app_id

    def _get_url_and_headers(self, brand_id='51db37d0176fe9790a899db2', fields=None, page=1, limit=50):
        """Base method for getting consistent headers and url

        :param brand_id: defaults to Juicy Juice brand
        :param fields: str() Fields you want returned. Pass in '*' for all fields.
        :return: (url --> str(), headers --> dict())
        """
        end = page * limit
        start = end - limit

        if fields is None:
            fields = 'item_name,item_description,nf_ingredient_statement,nf_calories,nf_servings_per_container,nf_serving_size_qty,nf_serving_size_unit'

        url = "{base_uri}/search/?brand_id={brand_id}&results={start}%3A{end}&fields={fields}&appId={app_id}&appKey={api_key}".format(
            base_uri=self._base_uri,
            brand_id=brand_id,
            start=start,
            end=end,
            fields=fields,
            app_id=self._app_id,
            api_key=self._api_key
        )

        headers = {'Content-Type': 'application/xml'}

        return url, headers

    def get_products(self):
        products = {
            'total_hits': 0,
            'hits': []
        }

        start = 1
        for i in range(4):
            url, headers = self._get_url_and_headers(page=start)

            response = requests.get(url, headers=headers)

            if response.status_code != 200:
                raise NutritionIxServiceError("NutritionIx Network Error. Expected 200 status code, got {} instead".format(
                    response.status_code
                ))

            content = json.loads(response.content)
            products['total_hits'] = content['total_hits']
            products['hits'].extend(content['hits'])

            # we got em all. Maybe worry about async stuff another time. Or caching.
            if len(products['hits']) == products['total_hits']:
                break

            start += 1

        return products
