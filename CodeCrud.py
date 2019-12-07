import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', password='', db='mibase', port=3306)
with conn:
    cursors = conn.cursor()
    cursors.execute("SELECT VERSION()")
    version = cursors.fetchone()
    print("Database version: {}".format(version[0]))
    print("Connection successfully done.")

def insertarRegistro():
    print(" --- Insert registers ---")
    #Retrieving data
    id = input("Input worker's ID::")
    name1 = input("Input worker's name::")
    salary1 = input("Input worker's salary:")
    sql = "INSERT INTO trabajadores(ID, name, salary) VALUES (" + str(id) + "'"+name1+"'" + ", "+str(salary1) +");"
    # cursor executes the sentence
    cursors.execute(sql)
    # Commit for saving changes
    conn.commit()
    print(cursors.rowcount, "Worker inserted ..")

def cambiarRegistro():
    print(" --- Edit registers ---")
    #Retrieving data
    clavicordio = input("Input worker's ID:")
    loo = 1
    while loo==1:
        opc = input("1.- Modify name\n 2.-Modify salary")
        if opc==1:
            nom =  input("Input the new name:")
            sql = "UPDATE Trabajadores Set Name= " + nom + "WHERE ID = "+ clavicordio+";"
        if opc==2:
            sal = input("Input the new name:")
            sql = "UPDATE Trabajadores Set Name= " + sal + "WHERE ID = "+ clavicordio+";"
    # sql sentence again
    cursors.execute(sql)
    conn.commit()
    print("Done update!")

def buscarRegistro():
    print(" --- Search registers ---")
    clavicordio = input("Input worker's ID:")
    sql = "SELECT * FROM trabajadores(code, nombre, sueldo) WHERE ID = "+ clavicordio+";"
    # sql sentence
    cursors.execute(sql)
    # .fetchall brings all tuples
    fetched = cursors.fetchall()
    # loop to show all
    for i in fetched:
        print(i)
    conn.commit()

def borrarRegistro():
    print(" --- Delete registers ---")
    clavicordio = input("Input worker's ID:")
    sql = "DELETE * FROM trabajadores WHERE ID = "+ clavicordio+";"
    cursors.execute(sql)
    conn.commit()

def listarRegistros():
    print(" --- All tha slaves ---")
    sql = "SELECT * FROM trabajadores"
    cursors.execute(sql)
    fetched = cursors.fetchall()
    for i in fetched:
        print(i)
    conn.commit()
#Main function
def main():
    print(" --- CRUD with MYSQL ---")
    print("1. Insert worker\n2. Search worker by ID\n3.- Modify")
    print("4. Delete \n5. List of whole workers \n6. Exit\n")
    opt = input("Select an option between 1 and 6: ")
    if opt == 1:
        insertarRegistro()
    elif opt == 2:
         buscarRegistro()
    elif opt == 3:
         cambiarRegistro()
    elif opt == 4:
         borrarRegistro()
    elif opt == 5:
         listarRegistros()
    elif opt == 6:
         exit()
if __name__ == "__main__":
    main()