import requests
import pytest


@pytest.fixture
def auth_token():
    payload = {
        "username": "veritaris",
        "password": "veritaris"
    }
    r = requests.post("http://localhost:8000/api/v1/auth", data=payload)
    return r.json().get("token")


class TestAdminFunctionality:
    BASE_URL = "http://localhost:8000/api/v1"

    def test_admin_auth(self):
        url = self.BASE_URL + "/auth"
        payload = {
            "username": "veritaris",
            "password": "veritaris"
        }
        r = requests.post(url, data=payload)
        assert r.json().get("token") is not None

    def test_add_poll(self, auth_token):
        url = self.BASE_URL + "/polls/"
        payload = {
            "title": "Test poll",
            "description": "Some poll for testing",
            "id": "228"
        }
        r = requests.post(url, data=payload, headers={"Authorization": "Bearer " + auth_token}).json()
        expected_result = {
            "date_created": None,
            "description": "Some poll for testing",
            "id": None,
            "questions": [],
            "title": "Test poll"

        }
        r["date_created"] = None
        r["id"] = None
        assert r == expected_result

    def test_edit_poll(self, auth_token):
        url = self.BASE_URL + "/polls/4/"
        payload = {
            "title": "Edited title",
        }
        r = requests.patch(url, data=payload, headers={"Authorization": "Bearer " + auth_token}).json()
        expected_result = {
            "date_created": None,
            "description": "Some poll for testing",
            "id": None,
            "questions": [],
            "title": "Edited title"

        }
        r["date_created"] = None
        r["id"] = None
        assert r == expected_result

    def test_delete_poll(self, auth_token):
        url = self.BASE_URL + "/polls/6/"
        payload = {

        }
        r = requests.delete(url, data=payload, headers={"Authorization": "Bearer " + auth_token})
        assert r.status_code == 204

    def test_add_question(self, auth_token):
        url = self.BASE_URL + "/questions/"
        payload = {
            "poll_id": "6",
            "text": "Question text",
            "type": "TEXT"
        }
        r = requests.post(url, data=payload, headers={"Authorization": "Bearer " + auth_token}).json()
        expected_result = {
            "answers": [],
            "id": None,
            "poll_id": 6,
            "text": "Question text",
            "type": "TEXT"
        }
        r["id"] = None

        assert r == expected_result


class TestUserFunctionality:
    BASE_URL = "http://localhost:8000/api/v1"

    def test_get_polls(self):
        url = self.BASE_URL + "/polls/"
        r = requests.get(url)

        try:
            r.json()
        except Exception:
            raise

    def test_vote(self):
        url = self.BASE_URL + "/answers/"
        payload = {
            "question": "4",
            "text": "Some answer",
            "voter": "137"
        }
        r = requests.post(url, data=payload).json()
        expected_result = {
            "id": None,
            "question": 4,
            "text": "Some answer",
            "voter": 137
        }
        r["id"] = None
        assert r == expected_result

    def test_get_user_polls(self):
        url = self.BASE_URL + "/voters/1/"
        r = requests.get(url).json()
        
        assert r.get("id") is not None
