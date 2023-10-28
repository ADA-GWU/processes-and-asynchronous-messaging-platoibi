import psycopg2
import random

def connectToDB(ip :str):
    conn = psycopg2.connect(
        database="hw1", user='dist_user', password='dist_pass_123', host=ip, port= '5432'
    )
    cur = conn.cursor()
    return cur

servers = open("databases.txt").readlines()
serverCursors = []
for server in servers:
    serverCursors.append(connectToDB(server))


print("Enter something to add to server: ", end = '')
while True:
    sql = """INSERT INTO async_messages(message)
            VALUES(%s);"""
    s = input()
    if s.lower() == 'exit':
        break 
    ind = random.randint(0, len(serverCursors)-1)
    serverCursors[ind].execute(sql, (s, ))
    print(serverCursors[ind].fetchone())
    print("Enter something to add to server: ", end = '')