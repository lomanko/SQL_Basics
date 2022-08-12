import psycopg2
from pprint import pprint


class ClientDB:
    def __init__(self, database, user, password):
        self.database = database
        self.user = user
        self.password = password
        self.conn = psycopg2.connect(database=self.database, user=self.user, password=self.password)
        self.cur = self.conn.cursor()

    def create_db_tables(self):
        """
        Function creates 2 tables: clients and phones
        """
        self.cur.execute("""
                CREATE TABLE IF NOT EXISTS clients(
    	            id SERIAL PRIMARY KEY,
    	            client_name TEXT,
    	            client_surname TEXT,
    	            client_mail TEXT UNIQUE
    	        );
            """)
        self.cur.execute("""
                CREATE TABLE IF NOT EXISTS phones(
    	            id SERIAL PRIMARY KEY,
                    client_id INTEGER NOT NULL REFERENCES clients(id),
                    phone_number VARCHAR(80) UNIQUE
    	        );
            """)
        self.conn.commit()

    def drop_db_table(self, *table_names):
        """
        Function drop tables.
        """
        for table_name in table_names:
            query = f'DROP TABLE IF EXISTS {table_name};'
            self.cur.execute(query)
            self.conn.commit()

    def add_new_client(self, client_name, client_surname, client_mail, *phones):
        """
        Function adds new client to tables.
        Phones can be used or not (can be one o several phones)
        """
        self.cur.execute("""
            INSERT INTO clients(client_name, client_surname, client_mail)
                 VALUES (%s, %s, %s) RETURNING id;
        """, (client_name, client_surname, client_mail))
        self.conn.commit()
        client_id = self.cur.fetchone()
        if phones is not None:
            for phone in phones:
                self.cur.execute("""
                    INSERT INTO phones (client_id, phone_number)
                         VALUES (%s, %s);
                """, (client_id, phone))
        self.conn.commit()

    def check_client_id(self, client_id):
        """
        Function checks the existence of client in database
        """
        self.cur.execute("""
                    SELECT id, client_name, client_surname 
                      FROM clients WHERE id = %s;
                """, (client_id,))
        result = self.cur.fetchone()
        if result is None:
            return False
        else:
            return True

    def add_phone(self, client_id, *phones):
        """
        Function adds phone for existing client.
        Function can add several phone numbers.
        """
        if not self.check_client_id(client_id):
            print(f'Client with id {client_id} does not exist.')
            return
        else:
            for phone in phones:
                self.cur.execute("""
                    INSERT INTO phones(client_id, phone_number)
                         VALUES (%s, %s);
                """, (client_id, phone))
            self.conn.commit()

    def change_client_information(self, client_id, client_name=None, client_surname=None, client_mail=None):
        """
        Function changes client information (name, surname and mail).
        Function needs client_id
        """
        if not self.check_client_id(client_id):
            print(f'Client with id {client_id} does not exist.')
            return
        else:
            change_list = {'client_name': client_name, 'client_surname': client_surname, 'client_mail': client_mail}
            for change in change_list.items():
                if change[1] is not None:
                    query = f"UPDATE clients SET {change[0]}='{change[1]}' WHERE id='{client_id}';"
                    self.cur.execute(query)
                    self.conn.commit()

    def check_phone_existence(self, client_id, phone):
        """
        Function checks the existence of (client_id + phone) in table phones
        """
        self.cur.execute("""
                            SELECT id, client_id, phone_number 
                              FROM phones WHERE client_id = %s AND phone_number = %s;
                        """, (client_id, phone))
        result = self.cur.fetchone()
        if result is None:
            return False
        else:
            return True

    def delete_phone_for_existing_client(self, client_id, *phones):
        """
        Functions gets client_id and phones and delete phones from table phones.
        Function can delete several phones with one client_id
        """
        for phone in phones:
            if not self.check_phone_existence(client_id, phone):
                print(f'Client with id {client_id} and phone {phone} does not exist.')
            else:
                self.cur.execute("""
                    DELETE FROM phones WHERE client_id = %s AND phone_number = %s;
                """, (client_id, phone))
                self.conn.commit()

    def delete_client(self, *client_ids):
        """
        Function deletes clients.
        Function can delete several clients.
        """
        for client_id in client_ids:
            if not self.check_client_id(client_id):
                print(f'Client with id {client_id} does not exist.')
            else:
                self.cur.execute("""
                    DELETE FROM phones WHERE client_id = %s;
                """, (client_id, ))
                self.conn.commit()
                self.cur.execute("""
                    DELETE FROM clients WHERE id = %s;
                """, (client_id, ))
                self.conn.commit()

    def search_client(self, client_name='', client_surname='', client_mail='', client_phone=''):
        search_list = {'client_name': client_name,
                       'client_surname': client_surname,
                       'client_mail': client_mail,
                       'phone_number': client_phone}
        query = []
        for key, value in search_list.items():
            if value: query.append(f"{key} = '{value}'")
        query = 'WHERE ' + ' AND '.join(query)
        query = """
                SELECT c.id, c.client_name, c.client_surname, c.client_mail, p.phone_number
                  FROM clients c
                  LEFT JOIN phones p ON c.id = p.client_id
                """ + query
        self.cur.execute(query)
        res = self.cur.fetchall()
        if not res:
            print('Client not found')
        else:
            print('Client found:')
            pprint(res)
