import pytest
import requests
from IPython.lib.deepreload import found_now

AVITO_URL = "https://qa-internship.avito.com"

class BaseUrl:
    @pytest.fixture(scope="session")
    def api_base_url(self):
        return AVITO_URL

class TestCreateAdvertisement(BaseUrl):

    def test_create_advertisement_valid_data(self, api_base_url):
        payload = {
            "sellerID": 145799,
            "name": "Anton",
            "price": 120,
            "statistics": {
                "likes": 10,
                "viewCount": 12,
                "contacts": 13
            }
        }

        response = requests.post(f"{api_base_url}/api/1/item", json=payload)
        assert response.status_code == 200

    def test_create_advertisement_no_data(self, api_base_url):
        payload = None

        response = requests.post(f"{api_base_url}/api/1/item", json=payload)
        assert response.status_code == 400

class TestGetAllAdvertisiment(BaseUrl):

    def test_get_correct_status(self, api_base_url):
        id = "7146e41d-d71e-46e8-b2b5-b137d7ea4b0f"
        payload = {
            "sellerID": 145799,
            "name": "Anton",
            "price": 120,
            "statistics": {
                "likes": 10,
                "viewCount": 12,
                "contacts": 13
            }
        }

        response = requests.get(f"{api_base_url}/api/1/item/{id}")
        assert response.status_code == 200


    def test_get_correct_advertisement(self, api_base_url):
        id = "7146e41d-d71e-46e8-b2b5-b137d7ea4b0f"
        payload = {
            "sellerID": 145799,
            "name": "Anton",
            "price": 120,
            "statistics": {
                "likes": 10,
                "viewCount": 12,
                "contacts": 13
            }
        }

        response = requests.get(f"{api_base_url}/api/1/item/{id}")
        response = response.json()[0]
        _ = response.pop("id")
        _ = response.pop("createdAt")
        assert response == payload

    def test_unvalid_status_not_found(self, api_base_url):
        id = "7146e41d-d71e-46e8-b2b5-b137d7ea4b0d"

        response = requests.get(f"{api_base_url}/api/1/item/{id}")
        assert response.status_code == 404

    def test_unvalid_status_server_error(self, api_base_url):
        id = {200}

        response = requests.get(f"{api_base_url}/api/1/item/{id}/")
        assert response.status_code == 500

class TestGetAllAdvertisimentFromSeller(BaseUrl):

    def test_get_correct_status_advertisement_from_user(self, api_base_url):
        seller_id = 145799
        response = requests.get(f"{api_base_url}/api/1/{seller_id}/item")
        assert response.status_code == 200

    def test_get_correct_advertisement(self, api_base_url):
        seller_id = 145799
        payload = {
            "sellerID": 145799,
            "name": "Anton",
            "price": 120,
            "statistics": {
                "likes": 10,
                "viewCount": 12,
                "contacts": 13
            }
        }

        response = requests.get(f"{api_base_url}/api/1/{seller_id}/item")

        for advertisement in response.json():
            _ = advertisement.pop("id")
            _ = advertisement.pop("createdAt")
            assert advertisement == payload

    def test_unvalid_not_found(self, api_base_url):
        seller_id = "7146e41d-d71e-46e8-b2b5-b137d7ea4b0f"

        response = requests.get(f"{api_base_url}/api/1/{seller_id}/item")
        assert response.status_code == 400

    def test_unvalid_server_error(self, api_base_url):
        seller_id = ["7146e41d-d71e-46e8-b2b5-b137d7ea4b0f", "fdgfsdgsd"]

        response = requests.get(f"{api_base_url}/api/1/{seller_id}/item")
        assert response.status_code == 500

class TestGetStatistics(BaseUrl):

    def test_correct_status(self, api_base_url):
        id = "7146e41d-d71e-46e8-b2b5-b137d7ea4b0f"

        response = requests.get(f"{api_base_url}/api/1/statistic/{id}")
        assert response.status_code == 200

    def test_correct_data(self, api_base_url):
        id = "7146e41d-d71e-46e8-b2b5-b137d7ea4b0f"
        statistics = {
            "likes": 10,
            "viewCount": 12,
            "contacts": 13
        }
        response = requests.get(f"{api_base_url}/api/1/statistic/{id}")

        assert response.json()[0] == statistics

    def test_unvalid(self, api_base_url):
        id = 3124141234132

        response = requests.get(f"{api_base_url}/api/1/statistic/{id}")

        assert response.status_code == 400

    def test_error_not_found(self, api_base_url):
        id = "7146e41d-d71e-46e8-b2b5-b137d7ea4b1f"

        response = requests.get(f"{api_base_url}/api/1/statistic/{id}")
        assert response.status_code == 404

    def test_unvalid_server_error(self, api_base_url):
        id = "7146e41d-d71e-46e8-b2b5-b137d7ea4b1f"

        response = requests.get(f"{api_base_url}/api/1/statistic/{id}")
        assert response.status_code == 500