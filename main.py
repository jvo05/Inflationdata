import sqlite3 as sq
import chart

con = sq.connect("data.sqlite")
cur = con.cursor()

data = cur.execute("select * from main").fetchall()

kategorien = []
for k in data:
    pointer = k[0]
    pointer = str(pointer)
    pointer = pointer[2:4]
    kategorien.append(pointer)

values = []
for d in data:
    d = d[1]
    d = float(d.replace(",","."))
    values.append(d)

chart.main(kategorien, values)