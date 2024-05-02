from PySide6 import QtWidgets, QtSql


class Data:
    def __init__(self):
        super(Data, self).__init__()
        self.create_connection()

    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('expense_db.db')

        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Cannot open database",
                                           "Click Cancel to exit.", QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS expenses (ID integer primary key AUTOINCREMENT, Date VARCHAR(20), "
                   "Category VARCHAR(20), Description VARCHAR(20), Balance REAL)")
        return True

    def execute_query_with_params(self, sql_query, query_values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)

        query.exec()

        return query

    def add_new_transaction_query(self, date, category, description, balance):
        sql_query = "INSERT INTO expenses (Date, Category, Description, Balance) VALUES (?, ?, ?, ?)"
        self.execute_query_with_params(sql_query, [date, category, description, balance])
        
    def delete_transaction_query(self, id):
        sql_query = "DELETE FROM expenses WHERE ID=?"
        self.execute_query_with_params(sql_query, [id])

    def get_total(self, column, filter=None, value=None):
        sql_query = f"SELECT SUM({column}) FROM expenses"

        if filter is not None and value is not None:
            sql_query += f" WHERE {filter} = ?"

        query_values = []

        if value is not None:
            query_values.append(value)

        query = self.execute_query_with_params(sql_query, query_values)

        if query.next():
            if str(query.value(0)) == '':
                return '0₽'
            else:
                return str(query.value(0)) + '₽'
        return '0'

    def total_balance(self):
        return self.get_total(column="Balance")
