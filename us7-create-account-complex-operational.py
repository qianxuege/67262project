from common import *

us='''
* Complex US: Create Account (US7)

   As a:  Traveler
 I want:  To create an account to become a registered user
So That:  I can have my information be saved when I revisit the site
'''

print(us)

def is_user_registered(user_id):
    """
    Check if the user_id exists in the Registered_Traveler table.
    """
    query = '''
        SELECT user_id
          FROM Registered_Traveler
         WHERE user_id = %s
    '''
    cur.execute(query, (user_id,))
    result = cur.fetchone()
    return result is not None

def is_guest_user(user_id):
    """
    Check if the user_id exists in the Guest_Traveler table.
    """
    query = '''
        SELECT user_id
          FROM Guest_Traveler
         WHERE user_id = %s
    '''
    cur.execute(query, (user_id,))
    result = cur.fetchone()
    return result is not None

def create_account_and_update(user_id, name, email):
    """
    Check if the user_id is already registered. If not, check if the user_id
    exists in Guest_Traveler. If it does, create the account and delete the guest record.
    Finally, show the new Registered_Traveler record.
    """
    # Check if user_id is already in Registered_Traveler
    if is_user_registered(user_id):
        print(f"Error: User ID {user_id} is already registered.")
        return

    # Check if user_id exists in Guest_Traveler
    if not is_guest_user(user_id):
        print(f"Error: User ID {user_id} does not exist in Guest_Traveler.")
        return

    # Create the account in Registered_Traveler
    print(f"Creating account for {name}...")
    register_query = '''
        INSERT INTO Registered_Traveler (user_id, name, email)
        VALUES (%s, %s, %s)
    '''
    cur.execute(register_query, (user_id, name, email))
    conn.commit()

    # Delete the user record from Guest_Traveler
    delete_query = '''
        DELETE FROM Guest_Traveler
         WHERE user_id = %s
    '''
    cur.execute(delete_query, (user_id,))
    conn.commit()

    # Show the new account in Registered_Traveler
    print("New Registered Traveler account:")
    show_new_account(user_id)

def show_new_account(user_id):
    """
    Display the details of the newly registered account.
    """
    query = '''
        SELECT user_id, name, email
          FROM Registered_Traveler
         WHERE user_id = %s
    '''
    cur.execute(query, (user_id,))
    rows = cur.fetchall()
    show_table(rows, cols='user_id name email')

#example usage
create_account_and_update(7, "Test User", "testuser@andrew.cmu.edu")

