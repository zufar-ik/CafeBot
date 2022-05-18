import sqlite3


class Database:
    def __init__(self, path_to_db="db.sqlite3"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_cart(self):
        sql = """
        CREATE TABLE Cart (
            tg_id int NOT NULL,
            Name varchar(255),
            quantity int
            );
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, id: int, tg_id: int, username: str, lname: str):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO main_users(id, tg_id, username, lname) VALUES(?, ?, ?, ?)
        """
        self.execute(sql, parameters=(id, tg_id, username, lname), commit=True)

    def add_cat(self, id: int, clas_id: int, name: str, anons: str, image: str, price: str, slug: str):
        sql = """
        INSERT INTO main_category(id,clas_id,anons,name,image,price,slug) VALUES (?,?,?,?,?,?,?)
        """
        self.execute(sql, parameters=(id, clas_id, name, anons, image, price, slug), commit=True)

    def add_product(self, tg_id: int, name: str, quantity: int,price:str):
        sql = """
        INSERT INTO main_cart(tg_id, name, quantity,price) VALUES(?, ?, ?,?)
        """
        self.execute(sql, parameters=(tg_id, name, quantity,price), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM main_users
        """
        return self.execute(sql, fetchall=True)

    def View_cat(self):

        sql = """
        SELECT * FROM main_product
        """

        return self.execute(sql, fetchall=True)
    def where_cat(self, **kwargs):
        sql = 'SELECT * FROM main_product WHERE '
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchall=True)
    def View_prod(self):
        sql = """
                SELECT * FROM main_category
                """
        return self.execute(sql, fetchall=True)

    def where_prod(self, **kwargs):
        sql = 'SELECT * FROM main_category WHERE '
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchall=True)

    def get_products(self, **kwargs):
        sql = "SELECT * FROM main_cart WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchall=True)

    def check_product(self, **kwargs):
        sql = "SELECT * FROM main_cart WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchone=True)

    def update_product(self, tg_id: int, name: str, quantity: int,price:str):
        sql = "UPDATE main_cart SET quantity=? WHERE tg_id=? AND name=? AND price=?"
        return self.execute(sql, (quantity, tg_id, name,price), commit=True)

    def delete_product(self, tg_id: int, name: str,price:str):
        sql = "DELETE FROM main_cart WHERE tg_id=? AND name=? AND price=?"
        return self.execute(sql, (tg_id, name,price), commit=True)

    def clear_cart(self, **kwargs):
        sql = "DELETE FROM main_cart WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, commit=True)

    def select_user(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM main_users;", fetchone=True)

    def update_user_email(self, email, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE Users SET email=? WHERE id=?
        """
        return self.execute(sql, parameters=(email, id), commit=True)

    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)

    def delete_cart(self):
        self.execute("DELETE FROM main_cart WHERE TRUE", commit=True)


def logger(statement):
    print(f"""
_____________________________________________________
Executing:
{statement}
_____________________________________________________
""")
