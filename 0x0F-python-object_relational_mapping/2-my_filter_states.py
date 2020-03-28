#!/usr/bin/python3
import sys
import MySQLdb

"""
    Script to conect to a sql db using MySQLdb client in python
"""

if len(sys.argv) != 5:
    print("arguments must be 4")
    sys.exit(1)
else:
    usrn = sys.argv[1]
    passw = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    hos_t = "localhost"

    db = MySQLdb.connect(host=hos_t, user=usrn,  passwd=passw, db=db_name)
    cur = db.cursor()

    try:
        data_query = "SELECT * FROM states WHERE name='{}'".format(state_name)
        cur.execute(data_query)
        rows = cur.fetchall()
    except MySQLdb.Error:
        st = "MySQL Error [{%d}]: {}"
        try:
            print(st.format(MySQLdb.Error.args[0], MySQLdb.Error.args[1]))
        except:
            print("MySQL Error %s".format(str(MySQLdb.Error)))

    for row in rows:
        print(row)

    cur.close()
    db.close()

