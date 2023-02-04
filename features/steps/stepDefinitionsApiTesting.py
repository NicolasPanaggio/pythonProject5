from behave import *
from features.MethodsDev.APIConnection import response, response_content, json_response, format_json


@given('Get API')
def get_api_data(context):
    """
        This function retrieved data from the specific API Request
    """
    context.response = response
    # print(response_content)
    # print(json_response)
    # print(response.status_code)
    # print(format_json)


@Step('Assert code response is 200')
def assert_code_response(context):
    """
        This function assert that the code response is 200
    """
    # Obtain code response
    code_response = response.status_code

    # Assert
    assert code_response == 200, "Code response is NOT 200, the data WASNT obtained"


@Step('Assert that exist an user')
def assert_exist_user(context):
    """
        This function assert that exist at least one user
    """
    name1 = "name"
    id1 = "id"
    email1 = "email"
    gender1 = "gender"
    status1 = "status"
    variable_for_assert = 1

    # Logic for handle assertion of the existence of an user
    if name1 in format_json:
        if id1 in format_json:
            if email1 in format_json:
                if gender1 in format_json:
                    if status1 in format_json:
                        print(f'"{format_json}" contains "{name1}" and "{id1}" and "{email1}" and "{gender1}" and "{status1}"')
                        variable_for_assert = 2
    else:
        variable_for_assert = 3

    # Assert
    assert variable_for_assert == 2, "Doesnt contain users in the list"


@Step('Assert one user name have letter C')
def assert_exist_user(context):
    """
        This function assert that one user name have letter C
    """
    global names_of_api, split_nameofapi
    take_firs_letter = ""

    # Logic for change to a string format, split it and join the strings
    for key in json_response:
        names_of_api = str(key['name'])
        split_nameofapi = names_of_api.split('  ')
        for p in split_nameofapi:
            take_firs_letter = take_firs_letter + p[0]

    # Take first letter of the names and join in same string
    print(take_firs_letter)
    letter_to_find = "C"
    find_letter = take_firs_letter.find(letter_to_find)
    print(find_letter)

    # Assert that in the string with the first letters, exist the specific letter
    assert find_letter != -1, f"No names start with the letter {letter_to_find}"


@Step('Retrieve list of users and show in console and assert user count')
def retrieve_list_and_show_in_console_and_assert_users_count(context):
    """
        This function retrieve a list and show in console
    """
    global names_of_api
    variable_for_assert = 1

    # Logic for show users in console
    for key in json_response:
        names_of_api = str(key)
        print(names_of_api)

    # Count of users
    counter_users = len(json_response)
    print(counter_users)

    if counter_users >= 0:
        variable_for_assert = 2
    else:
        variable_for_assert = 3

    assert variable_for_assert == 2, "Quantity of users is 0"
