import csv
import logging
import pyodbc as pdb

conn = pdb.connect("dsn=TESTDSN;uid=rp;pwd=Sasyak@143Tej")
cursor = conn.cursor()

fp = open(r'Testcases.csv')
csv_f = csv.reader(fp)

fp2 = open(r'TestResultssheet.csv', 'w', newline='')
csv_f2 = csv.writer(fp2, quoting=csv.QUOTE_NONNUMERIC, quotechar='"', doublequote=True, delimiter=',', lineterminator='\n')

Headers = ["DAX function", "Generated SQL", "Expected", "Actual","Results"]
csv_f2.writerow(Headers)

for row in csv_f:
    for col in csv_f:
        combined = [col[0],col[1],col[2]]
        sql = col[1]
        cursor.execute(sql)
        result = cursor.fetchall()
        i = 'FALSE'
        for row1 in result:
            combined.extend(row1)
            a = format(combined[3],'.2f')
            b = col[2]
            if b == '':
                i = 'Error'
            else:
                b = format(float(col[2].replace(',','')),'.2f')
                if a == b:
                 i = 'PASS'
            combined.append(i)
            temp = [col[0],col[1],b,a,i]
            csv_f2.writerow(temp)
fp.close()
fp2.close()
cursor.close()
conn.close()

