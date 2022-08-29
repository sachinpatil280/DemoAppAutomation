import datetime
import sys

import pytest

sys.path.append(r"/Users/sachinpatil/Signant/Flasky")

from signantAutomation.utils.APIRequest import APIRequest
from signantAutomation.testdata.api_testdata import *
from signantAutomation.customLibraries.apiCall import apiCall

# URI
token_uri = "http://localhost:8080/api/auth/token"
all_users_uri = "http://localhost:8080/api/users"


@pytest.fixture
def api_setup(scope="session"):
    api_method = APIRequest()
    yield api_method


@pytest.fixture
def api_call_with_DB_access(scope="session"):
    api_method = APIRequest()
    yield api_method
    apiCall().reset_database()


def test_create_user_api(api_setup):
    '''
    Test Creation of user using the post call for "/api/users" route
    '''
    headers = {'Content-Type': 'application/json'}
    resp = api_setup.post(all_users_uri, headers=headers, json=create_user_data)
    assert resp.status_code == 201
    assert resp.as_dict['status'] == "SUCCESS"


def test_get_all_user_api(api_setup):
    '''
    Test api returns all users when GET call is made with "/api/users" route
    '''
    get_user = api_setup.get(all_users_uri)
    print(get_user)
    assert get_user.status_code == 200
    assert create_user_data['username'] in get_user.as_dict['payload']


def test_get_user_api(api_setup):
    '''
    Test api returns specific user details when GET call is made with "/api/users" route with valid token
    '''
    get_token = api_setup.get(token_uri, create_user_data['username'],
                              create_user_data['password'], "basic")
    token = get_token.as_dict['token']
    token_headers = {'Content-Type': 'application/json', 'Token': '{0}'.format(token)}
    get_user = api_setup.get("{0}/{1}".format(all_users_uri, create_user_data['username']), headers=token_headers)
    assert get_user.status_code == 200
    assert len(get_user.as_dict['payload']) != 0


def test_update_user_api(api_call_with_DB_access):
    '''
    Test api updates specific user details when PUT call is made with "/api/users" route with valid token
    '''
    get_token = api_call_with_DB_access.get(token_uri, create_user_data['username'],
                                 create_user_data['password'], "basic")
    assert get_token.status_code == 200
    token = get_token.as_dict['token']
    token_headers = {'Content-Type': 'application/json', 'Token': '{0}'.format(token)}
    api_call_with_DB_access.put("{0}/{1}".format(all_users_uri, create_user_data['username']),
                     headers=token_headers, json=updated_user_data)
    get_user = api_call_with_DB_access.get("{0}/{1}".format(all_users_uri, create_user_data['username']),
                                headers=token_headers)
    assert get_user.status_code == 200
    assert get_user.as_dict['payload']['firstname'] == updated_user_data['firstname']
    assert get_user.as_dict['payload']['lastname'] == updated_user_data['lastname']
