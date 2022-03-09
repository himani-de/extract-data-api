from utils.utils import get_api_response


def check_page_status():
    """
    Check api status
    """
    todos_page = "https://jsonplaceholder.typicode.com/todos"
    albums_page = "https://jsonplaceholder.typicode.com/albums"
    todos_page_response = get_api_response(todos_page)
    albums_page_response = get_api_response(albums_page)
    assert todos_page_response.status_code == 200
    assert albums_page_response.status_code == 200

