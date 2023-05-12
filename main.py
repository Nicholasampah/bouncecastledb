
import sqlite3 as db
import pandas as pd
from datetime import datetime
import tables


connection = db.connect("partycastleDB.db")
cursor = connection.cursor()


# Creating tables
cursor.execute(tables.customer_table)
cursor.execute(tables.delivery_table)
cursor.execute(tables.logistics_table)
cursor.execute(tables.order_table)
cursor.execute(tables.driver_table)
cursor.execute(tables.vehicletype_table)
cursor.execute(tables.inventory_table)
cursor.execute("PRAGMA foreign_keys = 1")






        
    


def customer_menu():
    customer_choice = ""
    while customer_choice != "5":
        print("""
        1. Make a booking
        2. View a booking
        3. Cancel booking
        4. View boucing Castles
        5. Previous Menu
        """)
        customer_choice = input("Please select an option: ")
        if customer_choice == '5':
            continue
        if customer_choice == "1":
            inventory_query = " SELECT * FROM inventory"
            print(pd.read_sql_query(inventory_query,connection))
        
            customer_id= input("Enter your customer id ")
            id= input("Enter the id for the product you want to hire ")
            quantity= input("Enter the quantity ")
            date_of_event= input("When is the event ")
            number_of_days=input("How many days do you want hire ")
        
            check_inventory= "SELECT * FROM inventory WHERE id=?" 
            cursor.execute(check_inventory, (id, )).fetchall()
            add_order= ("""INSERT INTO orders (customer_id, inventory_id, quantity, date_of_event, number_of_days, total, status) VALUES (?,?,?,?,?, 100, "AWAITING DISPATCH")""")
            cursor.execute(add_order, ( customer_id, id, quantity, date_of_event, number_of_days,))
            connection.commit()
            print("order made successfully.")
        
        elif customer_choice == "2":
            customer_id= input("Enter your customer number ")
            value_order=cursor.execute("SELECT * FROM orders WHERE customer_id=?",(customer_id, )).fetchall()
            print(value_order)
        
        elif customer_choice == "3":
            customer_id = input("Enter your customer number: ")
            order_id = input("Enter your order ID: ")
            
            query = "SELECT * FROM orders WHERE customer_id=? AND id=?"
            value_order = cursor.execute(query, (customer_id, order_id)).fetchall()
            print(value_order)
            
            print("Are you sure you want to delete this order? (y/n)")
            del_choice = input("Answer y/n: ")
            
            if del_choice == "y":
                delete_query = "DELETE FROM orders WHERE customer_id=? AND id=?"
                cursor.execute(delete_query, (customer_id, order_id))
                connection.commit()
                print("Order deleted successfully.")
            else:
                continue
        
        elif customer_choice == "4":
            inventory_query = " SELECT * FROM inventory"
            print(pd.read_sql_query(inventory_query,connection))
        
        else:
            print("Customer not found")
            continue

     


def choice():
    user_choice = ""
    while user_choice !="3":
        print("""
        1. New customer
        2. Current customer
        3. Quit
        """)
        user_choice = input("Please select an option: ")
        if user_choice == '3':
            continue
        if user_choice == "1":
            # Add new customer
            user_firstName = input("Enter your first name: ")
            user_lastName = input("Enter your last name: ")
            user_email = input("Enter your email address: ")
            user_phone = input("Enter your phone number: ")
            user_address = input("Enter your address: ")
            user_postcode = input("Enter your postcode: ")

            add_customer = f"INSERT INTO customers (first_name, last_name, email, phone, address, postcode) VALUES (?,?,?,?,?,?)"
            cursor.execute(add_customer, (user_firstName, user_lastName, user_email, user_phone, user_address, user_postcode))
            connection.commit()
            print("Customer added successfully.")
            
        elif user_choice == "2":
            id = input("Enter user ID: ")
        
            
            query = "SELECT * FROM customers WHERE id=?"
            values = cursor.execute(query, (id,)).fetchall()
            print(values)
            
            
            customer_menu()
        else:
            print("Customer not found")


choice()
   
        


connection.commit()
connection.close()
