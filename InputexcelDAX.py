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
        str1 = ""
        for row1 in result:
            a = row1[0]
            if isinstance(a,float):
                a = format(a,'.2f')
            str1 = str1 + str(a)+"\n"
        b = col[2]
        str1 = str1.rstrip()
        if b == '':
            i = 'Error'
        else:
            if isinstance(b,float):
                b = format(float(col[2].replace(',', '')), '.2f')
            if str1 == str(b):
                i = 'PASS'
        temp = [col[0], col[1], b, str1.rstrip(), i]
        csv_f2.writerow(temp)

fp.close()
fp2.close()
cursor.close()
conn.close()