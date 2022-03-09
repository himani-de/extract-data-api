import requests


def test_filter_userid_data():
    """
    filter api response only for existing, manually imported users
    """
    user_id_list = [1, 2, 4, 6]
    todos_page = "https://jsonplaceholder.typicode.com/todos"
    todos_page_response = requests.get(todos_page).json()
    todos_user_list = []
    user_id = set()
    for users in todos_page_response:
        user_id.add(users['userId'])
    todos_user_list.extend(user_id)
    check = all(user in todos_user_list for user in user_id_list)
    assert bool(check) == True
