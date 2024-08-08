import sqlite3


def check_userid_exists(userid):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT EXISTS(SELECT 1 FROM users WHERE userid = ?)", (userid,))
    result = c.fetchone()[0]
    conn.close()
    return bool(result)


def sign_up_user(name: str, phonenumber: str, userid: str):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (name, phonenumber, userid) VALUES (?, ?, ?)", (name, phonenumber, userid))
    conn.commit()
    conn.close()
    print("signed up successfully!")


def register_message_to_support(userid: str, messageText: str):
    # Connect to the database (or create it if it doesn't exist)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (userid, messageText) VALUES (?, ?)", (userid, messageText))
    conn.commit()
    conn.close()
    print("added to messages table successfully.")