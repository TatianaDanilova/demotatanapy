import psycopg2
from database_work import config

class Database():
    def __init__(self):
        self.connection = self.connect_db()


    def connect_db(self):
        # установка подключения к БД
        try:
            connection = psycopg2.connect(
                host=config.host,
                user=config.user,
                password=config.password,
                database=config.db_name
            )
            print("Установлено соединение с бд")
            return connection
        except Exception as e:
            print(f"Ошибка подключения к бд: {e}")
            return None

    def take_partner_information(self):
        if not self.connection:
            return []
        try:
            cursor = self.connection.cursor()

            query = '''
            select partner_name, partner_phone, partner_type, partner_mail,
            partner_ur_addr, partner_inn, partner_rate, partner_director
            
            from partners'''

            cursor.execute(query)
            partner = [
                {
                    "name": row[0],
                    "phone": row[1],
                    "type": row[2],
                    "mail": row[3],
                    "ur_addr": row[4],
                    "inn": row[5],
                    "rate": row[6],
                    "director": row[7],

                }
                for row in cursor.fetchall()
            ]

            cursor.close()
            return partner

        except Exception:
            return []

    def sale_sum(self, partner_name: str):
        if not self.connection:
            return []
        try:
            cursor = self.connection.cursor()

            query = f'''
            select sum(history_products_count) as result_pr
            from history 
            where partner_name_fk = '{partner_name}'
            '''

            cursor.execute(query, {partner_name},)
            sales_data = [
                {
                    "procent": row[0],
                }
                for row in cursor.fetchall()
            ]

            cursor.close()
            return sales_data

        except Exception:
            return []
