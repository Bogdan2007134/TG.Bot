import psycopg2
from user_id import host, user, db_name, password
# просто тесты, нечего более
try:
    connection = psycopg2.connect(
        host=host,
        password=password,
        user=user,
        database=db_name
    )
    connection.autocommit = True
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )

        print(f"Server version; {cursor.fetchone()}")
    with connection.cursor() as cursor:
        cursor.execute(
            """
            )"""
        )

except Exception as _ex:
    print(_ex)

#print(f'from: {message.chat.id}; to: {interlocutors[message.chat.id]}, message: {message.text}')
#""f'SELECT second_id FROM users_id WHERE first_id = {message.chat.id}::TEXT;'""
