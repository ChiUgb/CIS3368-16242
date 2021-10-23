import sys
import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

conn = create_connection('cis3368.cg8u13ghvwys.us-east-2.rds.amazonaws.com','admin','Vbouusx7.','CIS3368Fall2021')
cursor = conn.cursor(dictionary=True)
sql = 'SELECT * FROM shoppinglist'
cursor.execute(sql)
rows = cursor.fetchall

for items in rows:
    print(items)








def shoppingmenu():
    print('       **MENU**')
    print('c - Current Shopping List')
    print('a - Add item')
    print('d - remove item')
    print('u - update item details')
    print('r1 - output all items in alphabetical order')
    print('r2 - output all items sorted by quantity (asending)')
    print('q - Quit \n')

shoppingmenu()
option_choose = (input('Enter your option: '))

while option_choose != 0:
    if option_choose == 'c':
        #add item
        pass
    elif option_choose == 'a':
        #remove item
        pass
    elif option_choose == 'd':
        #remove item
        pass
    elif option_choose == 'u':
        #remove item
        pass
    elif option_choose == 'r1':
        #remove item
        pass
    elif option_choose == 'r2':
        #remove item
        pass
    elif option_choose == 'q':
        #remove item
        sys.exit()
    else:
        print('Invalid Option Chosen')

print()
shoppingmenu()
option_choose = ('Enter your option: ')


