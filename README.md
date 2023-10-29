This program is a Python multithreaded PostgreSQL connector. It uses the ```psycopg2``` library to connect to PostgreSQL databases and the ```threading``` library to create and manage threads.

During the installation and running process, if you have multiple instances of python, then replace the keyword ```python``` with ```python3```, ```pip``` with ```pip3```, etc.

# Installation
To use the program, you will need to install the psycopg2 and threading libraries. You can do this with the following command:

```
pip install psycopg2 threading
```

# Usage
Fill the ```databases.txt``` file with ip's of databases.

Once the libraries are installed, you can run the sender program with this command:
```
python sender.py
```

and receiver program with this command:
```
python receiver.py
```


<br>
Once the programs are up and running, you will see prompts that the applications have connected to the databases

On the ```sender``` application enter any string to send to the database. It will send the message to a random database.

The ```receiver``` will grab the message and show it on the screen.