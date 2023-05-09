import pytest

@pytest.fixture(scope="session", autouse=True)
def auto_session_resource(request):
    """ Auto session resource fixture
    """
    print("auto_session_resource_setup")
    def auto_session_resource_teardown():
        print("auto_session_resource_teardown")
    request.addfinalizer(auto_session_resource_teardown)