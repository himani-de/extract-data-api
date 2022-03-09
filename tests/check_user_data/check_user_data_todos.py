from utils.utils import get_api_response


def filter_userid_data():
    """
    filter api response only for existing, manually imported users
    """
    user_id_list = [1, 2, 4, 6]
    todos_page = "https://jsonplaceholder.typicode.com/todos"
    albums_page = "https://jsonplaceholder.typicode.com/albums"
    todos_page_response = get_api_response(todos_page)
    albums_page_response = get_api_response(albums_page)
    todos_response_body = todos_page_response.json()
    albums_response_body = albums_page_response.json()
    assert todos_response_body["userId"] in user_id_list
    assert albums_response_body["userId"] in user_id_list
