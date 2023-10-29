import psycopg2
import random
import time
from queue import Queue
import threading

def receiveData(ip: str):
    connection = psycopg2.connect(
        database="hw1", user='dist_user', password='dist_pass_123', host=ip, port= '5432'
    )
    cursor = connection.cursor()
    for i in range(20):
        selectSQL = """SELECT * FROM async_messages WHERE received_time is null limit 1 for update"""
        cursor.execute(selectSQL)
        f = cursor.fetchone()
        x = q.get()
        if f is not None and x is True:
            print(f)
            updateSQL = """UPDATE async_messages
                        SET received_time = CURRENT_TIMESTAMP
                        WHERE record_id = %s"""
            if f is not None:
                cursor.execute(updateSQL, (f[0],))
            connection.commit()
        q.put(False)
        time.sleep(3)
        q.get()
        q.put(True)



q = Queue(1)
q.put(True)

threadlist = []
servers = open("databases.txt").readlines()
for server in servers:
    t = threading.Thread(target=receiveData, args=(server.strip(), ))
    t.start()
    threadlist.append(t)

time.sleep(20)
for thread in threadlist:
    thread.join()

