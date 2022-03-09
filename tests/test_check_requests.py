import requests


def test_check_page_status():
    """
    Check api status
    """
    todos_page = "https://jsonplaceholder.typicode.com/todos"
    albums_page = "https://jsonplaceholder.typicode.com/albums"
    todos_page_response = requests.get(todos_page)
    albums_page_response = requests.get(albums_page)
    assert todos_page_response.status_code == 200
    assert albums_page_response.status_code == 200
