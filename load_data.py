import logging
import database
from utils.utils import get_api_response

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(message)s')


def get_users(connection):
    """
    Get the list of the users from the database
    """
    cur = connection.cursor()
    cur.execute("SELECT id FROM users")
    users = cur.fetchall()
    user_ids = [id[0] for id in users]
    cur.close()
    return user_ids


def get_filter_uid_data(user_id_list):
    """
    filter api response only for existing, manually imported users
    """
    todos_response = get_api_response('https://jsonplaceholder.typicode.com/todos')
    albums_response = get_api_response('https://jsonplaceholder.typicode.com/albums')
    filter_user_todos_response = [uid for uid in todos_response if (uid["userId"] in user_id_list)]
    filter_user_albums_response = [uid for uid in albums_response if (uid["userId"] in user_id_list)]
    return filter_user_todos_response, filter_user_albums_response


def get_tuple_response(filter_user_todos_response, filter_user_albums_response ):
    """
    Create tuple from the list
    """
    album_res = []
    todo_res = []
    for albums in filter_user_albums_response:
        extract_album_uid = albums["userId"]
        extract_album_title = albums["title"]
        album_res.append([extract_album_uid, extract_album_title])
        album_final_data = [tuple(list) for list in album_res]
    for todo in filter_user_todos_response:
        extract_todo_uid = todo["userId"]
        extract_todo_title = todo["title"]
        extract_todo_status = todo["completed"]
        todo_res.append([extract_todo_uid, extract_todo_title, extract_todo_status])
        todo_final_data = [tuple(list) for list in todo_res]
    return album_final_data, todo_final_data


def insert_data(connection, album_final_data, todo_final_data):
    """
    Insert Data in Database
    """
    cur = connection.cursor()
    cur.executemany('INSERT INTO albums VALUES(?,?);', album_final_data);
    print('We have inserted', cur.rowcount, 'records to album table.')
    cur.executemany('INSERT INTO todos VALUES(?,?,?);', todo_final_data);
    print('We have inserted', cur.rowcount, 'records to todos table.')
    connection.commit()
    connection.close()


if __name__ == '__main__':
    connection = database.get_connection()
    user_id_list = get_users(connection)
    filter_user_todos_response, filter_user_albums_response = get_filter_uid_data(user_id_list)
    album_final_data, todo_final_data = get_tuple_response(filter_user_todos_response, filter_user_albums_response)
    insert_data(connection, album_final_data, todo_final_data)