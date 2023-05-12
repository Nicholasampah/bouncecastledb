inventory_table= """CREATE TABLE IF NOT EXISTS inventory (
                    id          INTEGER PRIMARY KEY AUTOINCREMENT,
                    name        TEXT NOT NULL,
                    quantity    INTEGER NOT NULL,
                    price       REAL NOT NULL,
                    colour      TEXT NOT NULL,
                    image       BLOB NOT NULL,
                    description TEXT NOT NULL,
                    Status      TEXT NOT NULL,
                    created_at  DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    updated_at  DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
)"""

vehicletype_table = """CREATE TABLE IF NOT EXISTS vehicletypes (
                id      INTEGER PRIMARY KEY AUTOINCREMENT,
                type    TEXT

)"""

logistics_table = """CREATE TABLE IF NOT EXISTS logistics (
            id                  INTEGER PRIMARY KEY AUTOINCREMENT,
            licence_number      TEXT,
            vehicle_type_id     INTEGER,
            vehicle_model       TEXT,
            vehicle_year        INTEGER,
            vehicle_make        TEXT,
            vehicle_colour       TEXT,
            max_weight          TEXT,
            FOREIGN KEY(vehicle_type_id) REFERENCES vehicletypes(id)
)"""

customer_table = """CREATE TABLE IF NOT EXISTS customers (
                    id          INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name  TEXT,
                    last_name   TEXT,
                    email       TEXT,
                    phone       INTEGER,
                    address     TEXT,
                    Postcode    TEXT
)"""


driver_table = """CREATE TABLE IF NOT EXISTS drivers (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name      TEXT NOT NULL,
                last_name       TEXT NOT NULL,
                license_number  TEXT NOT NULL,
                gender          TEXT NOT NULL,
                dob             TEXT NOT NULL,
                nationality     TEXT NOT NULL,
                email           TEXT NOT NULL,
                phone           INTEGER NOT NULL,
                address         TEXT NOT NULL
)"""

order_table = """CREATE TABLE IF NOT EXISTS orders (
                id             INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id        INTEGER NOT NULL,
                inventory_id     INTEGER NOT NULL,
                quantity       INTEGER NOT NULL,
                date_of_event   TEXT NOT NULL,
                number_of_days INTEGER NOT NULL,
                total          REAL,
                status         TEXT,
                created_at     DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at     DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(customer_id) REFERENCES customers(id),
                FOREIGN KEY(inventory_id) REFERENCES inventory(id)
               
)"""

delivery_table = """CREATE TABLE IF NOT EXISTS deliveries (
                    id            INTEGER PRIMARY KEY AUTOINCREMENT,
                    driver_id     INTEGER NOT NULL,
                    order_id      INTEGER NOT NULL,
                    status        TEXT NOT NULL,
                    created_at    DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    deliver_by    TEXT NOT NULL,
                    complete_by   TEXT NOT NULL,
                    collect_at    TEXT NOT NULL,
                    updated_at  DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                     FOREIGN KEY(driver_id) REFERENCES drivers(id),
                     FOREIGN KEY(order_id) REFERENCES orders(id)

)"""
