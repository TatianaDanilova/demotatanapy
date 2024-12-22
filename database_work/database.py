import psycopg2

import CheckPartnerData
from database_work import config
from CheckPartnerData import *

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

    def partner_add_func(self, partner_data: dict):
        if not self.connection:
            return False

        if not CheckPartnerData.main_func(partner_data):
            return False

        try:
            cursor = self.connection.cursor()

            query = '''
            insert into partners
            values (%s, %s, %s, %s, %s, %s, %s, %s)'''

            values = (
                partner_data['type'],
                partner_data['name'],
                partner_data['director'],
                partner_data['mail'],
                partner_data['phone'],
                partner_data['ur_addr'],
                partner_data['inn'],
                partner_data['rate'],
            )
            cursor.execute(query, values)

            self.connection.commit()
            cursor.close()
            print('Партнер добавлен')
            return True
        except Exception:
            return False

    def take_current_parent_info(self, partner_name):
        if not self.connection:
            return False

        try:
            cursor = self.connection.cursor()

            query = f'''
            select partner_name, partner_phone, partner_type, partner_mail,
            partner_ur_addr, partner_inn, partner_rate, partner_director
            from partners
            where partner_name = '{partner_name}'
           '''
            cursor.execute(query)
            partner_data = []
            for row in cursor.fetchall():
                partner_data.append({
                    "name": row[0],
                    "phone": row[1],
                    "type": row[2],
                    "mail": row[3],
                    "ur_addr": row[4],
                    "inn": row[5],
                    "rate": row[6],
                    "director": row[7],
                })

            print(partner_data)
            cursor.close()
            return partner_data
        except Exception:
            return []

    def update_partner_info(self, partner_name: str, partner_data: dict):
        if not self.connection:
            return False
        try:
            cursor = self.connection.cursor()

            query = f'''
            update partners
            set
            partner_type = '{partner_data["type"]}',
            partner_name = '{partner_data["name"]}',
            partner_phone = '{partner_data["phone"]}',
            partner_inn = '{partner_data["inn"]}',
            partner_rate = '{partner_data["rate"]}',
            partner_ur_addr = '{partner_data["ur_addr"]}',
            partner_director = '{partner_data["director"]}',
            partner_mail = '{partner_data["mail"]}'
            
            where partner_name = '{partner_name}'
           '''
            cursor.execute(query)
            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(e)
            return False