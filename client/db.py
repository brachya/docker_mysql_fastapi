import mysql.connector
from log_model import Log


class MyDb:
    def __init__(
        self,
        host: str = "database",
        port: int = 3306,
        user: str = "brachya",
        password: str = "1234",
        database: str = "logs_db",
        table: str = "logs",
    ) -> None:
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.table = table
        self.mydb = mysql.connector.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database,
        )
        self.mycursor = self.mydb.cursor()

    def query(self, search: str = "") -> tuple[bool, str]:
        self.mycursor.execute(f"SHOW COLUMNS FROM {self.table};")
        headers = self.mycursor.fetchall()
        self.mycursor.execute(
            f'SELECT * FROM {self.table} where log_msg like "%{search}%" LIMIT 10'
        )
        data = self.mycursor.fetchall()
        html = "<table\n"
        html += "<tr>\n"
        for head in headers:
            html += f"<th>{head[0]}</th>\n"  # type:ignore
        html += "</tr>\n"
        for row in data:
            html += "<tr>\n"
            for val in row:
                html += f"<td>{val}</td>\n"
            html += "</tr>\n"
        html += "</table>\n"
        return (True if data else False, html)

    def create_log(self, msg: Log) -> bool:
        try:
            insert_statement = (
                f"INSERT INTO {self.table} (log_msg) VALUES('{msg.log_msg}');"
            )
            print(insert_statement)
            self.mycursor.execute(insert_statement)
            return True
        except:
            return False

    def create_logs(self, logs: list[Log]) -> bool:
        try:
            for one_log in logs:
                insert_statement = (
                    f"INSERT INTO {self.table} (log_msg) VALUES('{one_log.log_msg}');"
                )
                print(insert_statement)
                self.mycursor.execute(insert_statement)
            return True
        except:
            return False

    def close(self) -> None:
        self.mycursor.close()
        self.mydb.close()
