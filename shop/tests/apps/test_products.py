import pytest
from django.test.client import Client
from django.contrib.auth.models import User

@pytest.mark.django_db
class TestIndex:
    def setup_method(self):
        self.client = Client()

    def test_my_function(self):
        response = self.client.get("/register/")
        assert response.status_code == 200

        response = self.client.post("/register/", data={
            "email": "kingtiger27062004@gmail.com",
            "password": "chemberlen",
            "first_name": "Test",
            "last_name": "Test",
        }, follow=True)
        assert response.status_code == 200
        assert User.objects.exists()

        response = self.client.post("/login_view/", data={
            "email": "kingtiger27062004@gmail.com",
            "password": "chemberlen",
        }, follow=True)
        assert response.status_code == 200