#!/usr/bin/python3
import sys
import MySQLdb

"""
    Script to conect to a sql db using MySQLdb client in python
"""

if len(sys.argv) != 4:
    print("arguments must be 3")
    sys.exit(1)
else:
    usrn = sys.argv[1]
    passw = sys.argv[2]
    db_name = sys.argv[3]
    hos_t = "localhost"

    db = MySQLdb.connect(host=hos_t, user=usrn,  passwd=passw, db=db_name)
    cur = db.cursor()

    try:
        cur.execute("SELECT id, name FROM states ORDER BY id ASC")
        rows = cur.fetchall()
    except MySQLdb.Error:
        str = "MySQL Error [%d]: %s"
        try:
            print(str % (MySQLdb.Error.args[0], MySQLdb.Error.args[1]))
        except:
            print(str % str(e))

    for row in rows:
        print(row)

    cur.close()
    db.close()
