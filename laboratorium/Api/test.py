import sqlite3
import random
from datetime import date, datetime, timedelta

current_date = datetime.strptime('2020-10-9', '%Y-%m-%d')
end_date = datetime.strptime('2018-10-10', '%Y-%m-%d')



conn = sqlite3.connect('Cortland.db')
c = conn.cursor()


c.execute('''Select * FROM Iphone_11''')
print(c.fetchall())

conn.commit()
conn.close()