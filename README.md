### Use Case
- Import data from an api filter it and save it in sqlite database.

###  Approach
- Using python requests following deliverables has been achieved:
  - extracted required data to the database from the API only for the existing and manually imported users already in the   database.
  - using sql query we  have filtered the response which we extracted from the apis and using a library **termtables**
    we are generating a report which displays the  count of albums for each user along with how many they have completed and not completed.

### Project Structure

```
|-- README.md
|-- database.py
|-- db
|-- get_summary.py
|-- load_data.py
|-- migrations.py
|-- report.py
|-- requirements.txt
|-- migrations
|   |-- 1_create_users.sql
|   |-- 2_populate_users.sql
|   |-- 3_create_albums.sql
|   `-- 4_create_tods.sql
|-- reports
|   `-- user_report.py
|-- tests
|   |-- __init__.py
|   |-- test_check_requests.py
|   |-- test_check_user_data_todos.py
|   |-- reports
|   |   |-- __init__.py
|   |   `-- test_user_report.py
`-- utils
    `-- utils.py

```

### How to run it locally
- Install all required libraries using following command.
```
pip install -r requirements.txt
```

- Run the following command to create the following tables in sqlite database and populate manually imported users .
  - users
  - todos
  - albums

```
python migration.py
```
 This will create the tables by reading from the *.sql file present under the db directory and insert the users to
 user table using 2_populate_users.sql script.

- Run the following command to extract the data from  given api.

```
python load_data.py
```
- Finally run the following command to generate report in the form of table on the console to know which user has least
  and most todos.

```
python report.py
```

### Tests
- There are two additional tests out of which one checks whether the api are accessible or not and second test validates
 if the response extracted has existing userIds or not.
- Run the following command to run the tests.

```
pytest
```
### Limitation
This code has been tested on following operating systems.
 * MacOS 12.1

This code has been tested on following Python Versions.
* Python 3.8.8

### Output

- The following report will be generated on console on running ```python report.py```. 

```
We have 4 users
We have following list of [1, 2, 4, 6] users
We have record for only following user in list  [1, 2, 4, 6] in todos table
We have record for only following user in list  [1, 2, 4, 6] in albums table
################################    GET SUMMARY FOR ALL USERS TODOS LIST     ################################
+--------+----------------------+------------------------+------------------------+----------------------------+
| userId | Name                 | Total Number of Albums | Albums_completed_Count | Albums_Not_completed_Count |
+========+======================+========================+========================+============================+
| 6      | Mrs. Dennis Schulist | 20                     | 6                      | 14                         |
+--------+----------------------+------------------------+------------------------+----------------------------+
| 4      | Patricia Lebsack     | 20                     | 6                      | 14                         |
+--------+----------------------+------------------------+------------------------+----------------------------+
| 2      | Ervin Howell         | 20                     | 8                      | 12                         |
+--------+----------------------+------------------------+------------------------+----------------------------+
| 1      | Leanne Graham        | 20                     | 11                     | 9                          |
+--------+----------------------+------------------------+------------------------+----------------------------+
Summary: All Users have same number of Albums
UserID 6 and 4 have most todos to complete
> Do people with the most albums have the least unfinished todos ?
With the data above this statement is false
```
