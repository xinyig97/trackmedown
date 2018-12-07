import sqlite3
import pandas as pd 

def output_watchlist():
    conn = sqlite3.connect('watchlist.db')
    c = conn.cursor()
    ip = list()
    username = list()
    geolocation = list()
    datetime = list()
    count = list()
    method = list()

    for row in c.execute('SELECT * FROM watchlist'):
        ip.append(row[0])
        username.append(row[1])
        geolocation.append(row[2])
        datetime.append(row[3])
        count.append(row[4])
        method.append(row[5])

    df = pd.DataFrame({'ip':ip,
                        'username':username,
                        'datetime':datetime,
                        'method':method,
                        'geolocation':geolocation,
                        'count':count})

    writer = pd.ExcelWriter('files.xlsx',
                            engine = 'xlsxwriter')

    df.to_excel(writer,sheet_name = 'Sheet1')
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    writer.save()
    conn.close()
