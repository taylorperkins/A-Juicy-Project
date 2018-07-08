import json
import requests


class NutritionIxServiceError(Exception):
    pass


class NutritionIxService(object):
    def __init__(self, base_uri, api_key, app_id):
        self._base_uri = base_uri
        self._api_key = api_key
        self._app_id = app_id

    def _get_url_and_headers(self, brand_id='51db37d0176fe9790a899db2'):
        """Base method for getting consistent headers and url

        :param brand_id: defaults to Juicy Juice brand
        :return: (url --> str(), headers --> dict())
        """
        url = "{base_uri}/search/?brand_id={brand_id}&results=0%3A50&fields=*&appId={app_id}&appKey={api_key}".format(
            base_uri=self._base_uri,
            brand_id=brand_id,
            app_id=self._app_id,
            api_key=self._api_key
        )

        headers = {'Content-Type': 'application/xml'}

        return url, headers

    def get_products(self):
        url, headers = self._get_url_and_headers()

        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            raise NutritionIxServiceError("NutritionIx Network Error. Expected 200 status code, got {} instead".format(
                response.status_code
            ))

        return json.loads(response.content)
