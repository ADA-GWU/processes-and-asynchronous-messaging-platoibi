def connectToDB(ip :str):
    pass

servers = open("databases.txt").readlines()
for server in servers:
    connectToDB(server)