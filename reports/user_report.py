class UserReport:
  def __init__(self, database_cursor):
    self.cur = database_cursor
  
  def process(self):
    self.cur.execute("SELECT COUNT(1) FROM users")
    return self.cur.fetchone()[0]


  def check_distinct_users(self):
    self.cur.execute("SELECT DISTINCT(id) from users ORDER by id ASC;")
    users = self.cur.fetchall()
    user_ids = [id[0] for id in users]
    return user_ids

  def check_distinct_users_todos(self):
    self.cur.execute("SELECT DISTINCT(userId) from todos ORDER by userId ASC;")
    users = self.cur.fetchall()
    user_ids = [id[0] for id in users]
    return user_ids

  def check_distinct_users_albums(self):
    self.cur.execute("SELECT DISTINCT(userId) from albums ORDER by userId ASC;")
    users_albums = self.cur.fetchall()
    user_ids = [id[0] for id in users_albums]
    return user_ids
