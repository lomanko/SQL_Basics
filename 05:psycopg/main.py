from psycopg2_db_class import ClientDB

clients_base = ClientDB('client_db', 'postgres', 'postgres')  # creates class instance
clients_base.drop_db_table('phones', 'clients')  # drop tables


# 1
clients_base.create_db_tables()  # creates tables

# 2
clients_base.add_new_client('Alexandr', 'Ivanov', 'alex_ivanov@ivanov.com')  # inserts clients to db
clients_base.add_new_client('Alexandr', 'Petrov', 'alex_petrov@petrov.com', '+79191231212')  # inserts clients to db
clients_base.add_new_client('Ivan', 'Sidorov', 'i_sidorov@sidorov.com')  # inserts clients to db
clients_base.add_new_client('Petr', 'Ivanov', 'i_ivanov@ivan.com', '+77777777','+78888888') # inserts clients to db
clients_base.add_new_client('Ivan', 'Fedorov', 'fedorov@sidorov.com', '+11111')

# 3
clients_base.add_phone(1, '+71112323')  # adds phone number to existing client_id
clients_base.add_phone(2, '+71132323','+99991122')  # adds several phone numbers to existing client_id
# clients_base.add_phone(5, '+71111111')  # instance for non-existent client_id

# 4
clients_base.change_client_information(2, 'Igor', 'Petrovskiy')  # changes client information

# 5
# clients_base.delete_phone_for_existing_client(1,'+71112323')  # delete clients phone
clients_base.delete_phone_for_existing_client(4,'+77777777','+78888888')  # delete clients phone

# 6
clients_base.delete_client(4) # delete client
# clients_base.delete_client(4,2) # delete several clients

# 7
clients_base.search_client('Ivan')
clients_base.search_client(client_name='Igor',client_surname='Petrovskiy',client_phone='+71132323')
clients_base.search_client('Sergey')


clients_base.conn.close()  # closes connection

