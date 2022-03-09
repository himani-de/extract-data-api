import database
import termtables as tt


def get_summary(connection):
    """
    Get the list of the users from the database
    """
    cur = connection.cursor()
    print(
        "################################    GET SUMMARY FOR ALL USERS TODOS LIST     ################################")
    cur.execute('''
                select  userId ID , name Name ,count(title)  Albums_Count, 
                sum(case when completed = 1 then 1 else 0 end) as album_completed,
                sum(case when completed = 0 then 1 else 0 end) as album_not_completed 
                from todos a , users b where a.userId=b.id
                group by userId ORDER by album_not_completed DESC;
                ''')
    result = cur.fetchall()
    table = tt.to_string([result], header=["userId", "Name", "Total Number of Albums",
                                           "Albums_completed_Count", "Albums_Not_completed_Count"],
                         style=tt.styles.ascii_thin_double)
    print(table)
    print(f"Summary: All Users have same number of Albums \nUserID 6 and 4 have most todos to complete")
    print(f"> Do people with the most albums have the least unfinished todos ? \nWith the data above "
          "this statement is false")

