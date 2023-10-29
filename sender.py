import psycopg2
import random

def connectToDB(ip :str):
    conn = psycopg2.connect(
        database="hw1", user='dist_user', password='dist_pass_123', host=ip, port= '5432'
    )
    cur = conn.cursor()
    return (cur, conn)

servers = open("databases.txt").readlines()
serverCursors = []
serverConnections = []
for server in servers:
    cur, conn = connectToDB(server.strip())
    serverCursors.append(cur)
    serverConnections.append(conn)


print("Enter something to add to server: ", end = '')
while True:
    sql = """INSERT INTO async_messages(message, sender_name)
            VALUES(%s, %s);"""
    s = input()
    if s.lower() == 'exit':
        break 
    ind = random.randint(0, len(serverCursors)-1)
    serverCursors[ind].execute(sql, (s, 'ibrahim'))
    serverConnections[ind].commit()
    print("sent to server", ind)
    print("Enter something to add to server: ", end = '')