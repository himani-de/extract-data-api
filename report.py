import database
import reports.user_report
from get_summary import get_summary

connection = database.get_connection()
cur = connection.cursor()

# User count report
user_report = reports.user_report.UserReport(cur)
user_report_data = user_report.process()
user_distinct_data = user_report.check_distinct_users()
check_user_in_albums = user_report.check_distinct_users_albums()
check_user_in_todo = user_report.check_distinct_users_todos
print(f'We have {user_report_data} users')
print(f'We have following list of {user_distinct_data} users')
print(f'We have record for only following user in list  {user_distinct_data} in todos table')
print(f'We have record for only following user in list  {user_distinct_data} in albums table')

# Get Summary
get_summary(connection)
