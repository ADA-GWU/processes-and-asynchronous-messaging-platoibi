import psycopg2

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