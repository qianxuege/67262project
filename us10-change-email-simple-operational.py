from common import *

us='''
* Simple US: Change Email (US10)

   As a:  Traveler
 I want:  To change my contact email
So That:  I can be reached at my updated email address
'''

print(us)

def change_email(user_id, new_email):
    # Check if the user exists in Registered_Traveler
    check_query = '''
        SELECT user_id, name, email
          FROM Registered_Traveler
         WHERE user_id = %s
    '''
    cur.execute(check_query, (user_id,))
    result = cur.fetchone()

    if not result:
        print(f"Error: User ID {user_id} is not registered.")
        return

    print(f"Current email for {result[1]} (User ID {user_id}): {result[2]}")

    update_query = '''
        UPDATE Registered_Traveler
           SET email = %s
         WHERE user_id = %s
    '''
    cur.execute(update_query, (new_email, user_id))
    conn.commit()

    print(f"Email for User ID {user_id} has been updated to: {new_email}")

#example usage
change_email(4, "sophiazhu@cmu.edu")
