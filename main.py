
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


# Create the "created_at" trigger
cursor.execute("""
    CREATE TRIGGER IF NOT EXISTS inventory_created_at_trigger
    AFTER INSERT ON inventory
    BEGIN
        UPDATE inventory SET created_at = datetime('now') WHERE id = NEW.id;
    END;
""")

# Create the "updated_at" trigger
cursor.execute("""
    CREATE TRIGGER IF NOT EXISTS inventory_updated_at_trigger
    AFTER UPDATE ON inventory
    BEGIN
        UPDATE inventory SET updated_at = datetime('now') WHERE id = NEW.id;
    END;
""")

def customer_menu():
    customer_choice = ""
    while customer_choice != "4":
        print("""
        1. Make a booking
        2. View a booking
        3. View boucing Castles
        4. Previous Menu
        """)
        customer_choice = input("Please select an option: ")
        if customer_choice == '4':
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
        add_order= f"INSERT INTO orders (customer_id, inventory_id, quantity, date_of_event, number_of_days) VALUES (?,?,?,?,?)" 
        cursor.execute(add_order, ( customer_id, id, quantity, date_of_event, number_of_days))
        connection.commit()
        print("order made successfully.")

     


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
   
        
#menu_choice()
# Call the function to create the trigger
#create_delivery_trigger()


##################INVENTORY TABLE#####################
# # Insert data into INVENTORY TABLE
# cursor.execute("""INSERT INTO inventory (id, name, quantity, price, colour, image, description, Status)  VALUES (101,"Princess Bouncy Castle with Slide", 6, 70, "Pink", "image1.jpg", "Contents: Bouncer, air blower, 8 stakes, carry bag, repair kit and manual
# Electric air blower for continuous inflation and airflow
# Set up in minutes for hours of fun
# Mesh sides for adult supervision
# Stakes anchor the bouncer firmly in place
# Total weight limit: 113kg (max. 5 children at a time)
# Dimensions: 295L x 233W x 175Hcm", "Avialable")""")
# #View data into CUSTOMERS TABLE
# inventory_query = " SELECT * FROM inventory"
# print(pd.read_sql_query(inventory_query,connection))
# # # Update data into INVENTORY TABLE
# # # Delete data into INVENTORY TABLE

# ##################VEHICLETYPE TABLE#####################
# #insert data into VEHICLETYPE TABLE
# cursor.execute("""INSERT INTO vehicletypes (id, type) VALUES(201, "Mini-Truck")""")
# cursor.execute("""INSERT INTO vehicletypes (id, type) VALUES(202, "Truck")""")
# cursor.execute("""INSERT INTO vehicletypes (id, type) VALUES(203, "Mini-Van")""")
# cursor.execute("""INSERT INTO vehicletypes (id, type) VALUES(204, "Van")""")
# #view data in VEHICLETYPE TABLE
# vehicletype_query = " SELECT * FROM vehicletypes"
# print(pd.read_sql_query(vehicletype_query,connection))
# #Update data in vehicletypes
# #Delete data in vehicle types
# cursor.execute("""DELETE FROM vehicletypes WHERE""")



# # ##################LOGISTICS TABLE#####################
# # #Insert data into LOGISTIC TABLE
# cursor.execute("""INSERT INTO logistics (licence_number, vehicle_type_id, vehicle_model, vehicle_year, vehicle_make, vehicle_colour, max_weight) VALUES("PC1 HRE", 201, "Sprinter", 2017, "Mercedes-Benz", "White", "1248kg")""")
# # View data in LOgistics TABLE
# logistics_query = " SELECT * FROM logistics"
# print(pd.read_sql_query(logistics_query,connection))


# # ##################DRIVERS TABLE#####################
# # #Insert data into DRIVERS TABLE
# cursor.execute("""INSERT INTO drivers (first_name, last_name, license_number, gender, dob, nationality, email, phone, address) VALUES ("Michael", "Kane", "KANEM874682A45T", "Male", "23-NOV-1969", "English", "kanem@gmail.com", 0759712507, "789 Market Street, Manchester" )""")
# #view data in DRIVERS TABLE
# driver_query = " SELECT * FROM drivers"
# print(pd.read_sql_query(driver_query,connection))

# # ##################CUSTOMERS TABLE#####################
# #Insert data into CUSTOMERS TABLE
# cursor.execute("""INSERT INTO customers (first_name, last_name, email, phone, address, postcode) VALUES("Nicholas", "Ampah", "nicholas.ampah@yahoo.com", 07860987621, "20 Oak Road, Manchester", "M99 0YU")""")
# # View data into CUSTOMERS TABLE
# customer_query = " SELECT * FROM customers"
# print(pd.read_sql_query(customer_query,connection))
# # # Update data into CUSTOMERS TABLE
# cursor.execute("""UPDATE customers SET first_name="Judith", last_name="Brookes" , email="brookesme@aol.com", phone=07296397101, address="23 Travis Court, Manchester", postcode="M11 4TC" WHERE id=503""")
# # # Delete data into CUSTOMERS TABLE
# cursor.execute("""DELETE FROM customers WHERE id=505""")

# # ##################ORDERS TABLE#####################
# # #Insert data into ORDERS TABLE
# cursor.execute("""INSERT INTO orders (customer_id, inventory_id, quantity, date_of_event, number_of_days, total, status) VALUES (501, 101, 2, "20-MAY-2023", 1, 100, "Awaiting Delivery")""")
# #view data in ORDERS TABLE
# orders_query = "SELECT * FROM orders"
# print(pd.read_sql_query(orders_query,connection))

# # ##################DELIVERY TABLE#####################
# # #Insert data into DELIVERY TABLE
# cursor.execute("""INSERT INTO deliveries (driver_id, order_id, status, deliver_by, complete_by, collect_at) VALUES (401, 601, "NOT DISPACHED", "19-MAY-2023", "20-MAY-2023", "20-MAY-2023")""")
# #view data in DELIVERY TABLE
# delivery_query = "SELECT * FROM deliveries"
# print(pd.read_sql_query(delivery_query,connection))

# cursor.execute("SELECT * FROM orders WHERE customer_id = 501 ")

connection.commit()
connection.close()
