import mysql.connector
#COMPLETED BY MARGARITA BUSYGINA

try:
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="040965074", database="covid19")
    mycursor = mydb.cursor(buffered=True)
except:
    print("ERROR CONNECTING DATABASE")

#READ function
#prints all the records from the dataset
def read_data():
    mycursor.execute("SELECT * FROM covid_data")
    result_set = mycursor.fetchall()
    print("Success\n")
    for row in result_set:
        print(row)
        print(" ")

#CREATE function
def add_record(pruid, date, numconf, numdeaths, prname, prnameFR, numtoday, ratetotal):
  try:
    sqlFormula = "INSERT INTO covid_data(PRUID, DATE, NUMCONF, NUMDEATHS, PRNAME, PRNAME_FR, NUMTODAY, RATETOTAL) " \
                 "VALUES(%s, %s, %s, %s, %s, %s, %s, %s) "
    newRecord = (pruid, date, numconf, numdeaths, prname, prnameFR, numtoday, ratetotal)
    mycursor.execute(sqlFormula, newRecord)
    mydb.commit()
    print("Success")
  except ValueError:
        print("Invalid value")

#UPDATE function
def edit_record(id, new_prov):
   try:
    sqlFormula = ("UPDATE covid_data SET PRNAME = %s, PRNAME_FR =%s WHERE pruid=%s ")
    mycursor.execute(sqlFormula, (new_prov, new_prov, id))
    mydb.commit()
    print("Success")
   except ValueError:
       print("Invalid value")

#DELETE function
def delete_record(pruid, date):
 try:
    sqlFormulaDelete = "DELETE FROM covid_data WHERE date = %s AND pruid = %s"
    recordDelete = (date, pruid)
    mycursor.execute(sqlFormulaDelete, recordDelete)
    mydb.commit()
    print("Success")
 except ValueError:
  print("Invalid value")


def delete_all():
    sqlFormulaDelete = " DELETE FROM covid_data"
    mycursor.execute(sqlFormulaDelete)
    mydb.commit()
    print("Success")

