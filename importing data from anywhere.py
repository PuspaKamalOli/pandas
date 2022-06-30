# note that csv excel and sql file are present in ur desktop
import pandas as pd
import pymysql

dt_frame = pd.DataFrame([[1, 2, 4], [5, 6, 7]], ["A", "B"], ['C', "D", 'E'])
print(dt_frame)

# reads csv file
print(pd.read_csv('computer.csv'))
# reads excel file
print(pd.read_excel('expenditure.xlsx', 0))

# converts to csv
print(dt_frame.to_csv("a.csv"))
# converts to excel
print(dt_frame.to_excel('v.xlsx'))
# work on mysql database
db_connection = pymysql.connect(db='admin', user='oli', passwd='**', host='localhost', port=3306)
exp = pd.read_sql('SELECT * FROM COST', con=db_connection)
db_connection.close()
# making permanent change on database
cursor = db_connection.cursor()
cursor.execute('some command of mysql')
db_connection.commit()
