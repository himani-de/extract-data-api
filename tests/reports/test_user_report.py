import pytest
import database
import migrations
import reports.user_report


# Fixture for a test databse connection
@pytest.fixture(autouse=False)
def connection():
    db_name = 'test'
    connection = database.get_connection(db_name)
    migrations.migrate(connection)
    yield connection
    database.delete_db(db_name)


def test_user_report(connection):
    # Run the report
    ur = reports.user_report.UserReport(connection.cursor())
    data = ur.process()
    # We should have 4 users from the initial population
    assert data == 4
