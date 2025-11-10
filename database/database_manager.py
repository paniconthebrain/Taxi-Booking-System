import pyodbc

class DatabaseManager:
    def __init__(self, server='.', database='TBS', username='sa', password='ura@tech12345'):
        self._server = server
        self._database = database
        self._username = username
        self._password = password
        self._conn = None
        self._cursor = None

    def connect(self):
        """Establish SQL Server connection"""
        try:
            conn_str = (
                f'DRIVER={{ODBC Driver 17 for SQL Server}};'
                f'SERVER={self._server};'
                f'DATABASE={self._database};'
                f'UID={self._username};'
                f'PWD={self._password}'
            )
            self._conn = pyodbc.connect(conn_str)
            self._cursor = self._conn.cursor()
            print("✅ Database connection successful.")
        except Exception as e:
            print("❌ Database connection failed:", e)
            self._conn = None
            self._cursor = None

    def insert_user(self, name, username, password, contact, role):
        """Insert new user into 'users' table"""
        try:
            self._cursor.execute('''
                INSERT INTO users (name, username, password, contact, role)
                VALUES (?, ?, ?, ?, ?)
            ''', (name, username, password, contact, role))
            self._conn.commit()

            # Retrieve inserted record
            self._cursor.execute('SELECT * FROM users WHERE username=?', (username,))
            row = self._cursor.fetchone()
            if row:
                columns = [col[0] for col in self._cursor.description]
                return dict(zip(columns, row))
            return None

        except pyodbc.IntegrityError:
            print("⚠️ Username already exists.")
            return None
        except Exception as e:
            print("❌ Error while inserting user:", e)
            return None

    def fetch_user(self, username, password):
        """Fetch user by credentials"""
        try:
            self._cursor.execute('''
                SELECT * FROM users WHERE username=? AND password=?
            ''', (username, password))
            row = self._cursor.fetchone()
            if row:
                columns = [col[0] for col in self._cursor.description]
                return dict(zip(columns, row))
            return None
        except Exception as e:
            print("❌ Error while fetching user:", e)
            return None

    def close(self):
        """Close connection"""
        if self._conn:
            self._conn.close()
            print("🔒 Database connection closed.")
