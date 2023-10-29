import psycopg2
import random
from queue import Queue 
import random
import time 
import threading

q = Queue(1)
q.put(0)
connected = 0

def sendMSG(ip :str):
    connection = psycopg2.connect(
        database="hw1", user='dist_user', password='dist_pass_123', host=ip, port= '5432'
    )
    cursor = connection.cursor()
    print('Connected to', ip)
    global connected
    connected += 1
    while True:
        if connected != len(servers):
            continue
        ind = q.get()
        if ind == -1:
            q.put(-1)
            return
        if ip == servers[ind]:
            print("Enter something to add to server: ", end = '')
            sql = """INSERT INTO async_messages(message, sender_name, sent_time)
                    VALUES(%s, %s, CURRENT_TIMESTAMP);"""
            s = input()
            if s.lower() == 'exit':
                q.put(-1)
                return
            cursor.execute(sql, (s, 'ibrahim'))
            connection.commit()
            print("sent to server", ind)
            q.put(random.randint(0, len(servers)-1))
            pass 
        else:
            q.put(ind)
        time.sleep(0.2)

servers = open("databases.txt").readlines()
for i in range(len(servers)):
    servers[i] = servers[i].strip()

threads = []
for server in servers:
    t = threading.Thread(target=sendMSG, args=(server, ))
    t.start()

for thread in threads:
    thread.join()