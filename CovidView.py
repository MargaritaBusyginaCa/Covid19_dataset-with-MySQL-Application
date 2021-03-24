import db_connector
#COMPLETED BY MARGARITA BUSYGINA
class CovidView():
    pass


def reloadDataFromFile_view():
    db_connector.read_data()


def createNewRecord_view():
    pruid = input("enter province id: ")
    date = input("enter date YY-MM-DD: ")
    numconf = input("enter number confirmed:")
    deaths = input("enter deaths: ")
    name = input("enter province province name: ")
    namefr = input("enter province province name(french): ")
    numtoday = input("enter province number today: ")
    total = input("enter province rate total: ")

    db_connector.add_record(pruid, date, numconf, deaths, name, namefr, numtoday, total)


def selectAndEdit_view():
    pruid = input("enter province id")
    nameNew = input("enter new province province name")
    db_connector.edit_record(pruid, nameNew)


def selectAndDelete_view():
    pruid = input("enter province id")
    date = input("enter date YY-MM-DD")
    db_connector.delete_record(pruid, date)


def deleteAll_view():
    db_connector.delete_all()


def display_menu():
    while True:
        menuChoice = ["1. RELOAD DATA FROM THE DATASET",
                      "2. CREATE A NEW RECORD",
                      "3. SELECT AND EDIT A RECORD",
                      "4. SELECT AND DELETE A RECORD",
                      "5. DELETE ALL RECORDS",
                      "6. EXIT MENU"]

        for item in menuChoice:
            print(item)
        answer = input()
        if answer == "1":
            reloadDataFromFile_view()
        if answer == "2":
            createNewRecord_view()
        if answer == "3":
            selectAndEdit_view()
        if answer == "4":
            selectAndDelete_view()
        if answer == "5":
            deleteAll_view()
        if answer == "6":
            print("COMPLETED BY MARGARITA BUSYGINA")
            quit()



display_menu()
