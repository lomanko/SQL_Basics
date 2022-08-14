import sqlalchemy
from sqlalchemy.orm import sessionmaker
import json

from model import create_tables, Publisher, Shop, Book, Stock, Sale

DSN = 'postgresql://postgres:postgres@localhost:5432/books'
engine = sqlalchemy.create_engine(DSN)

# Task 1
create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Task 3
with open('fixtures/tests_data.json') as f:
    json_data = json.load(f)

for row in json_data:
    model = {'publisher': Publisher,
             'shop': Shop,
             'book': Book,
             'stock': Stock,
             'sale': Sale}[row.get('model')]
    session.add(model(id=row.get('pk'), **row.get('fields')))

    session.commit()


# Task 2 (find publisher)
def find_publisher():
    """
    Function finds information from table publisher.
    Function asks ID (digit) or Name (part of name).
    """
    input_inf = input('Input publisher ID (digit) or publisher name: ')
    if input_inf.isdigit():
        query = session.query(Publisher).filter(Publisher.id == int(input_inf))
        if query.first() is None:
            print(f'Publisher with id \033[1m{input_inf}\033[0m does not exist.')
        else:
            for p in query.all():
                print(p)
    else:
        query = session.query(Publisher).filter(Publisher.name.ilike(f'%{input_inf}%'))
        if query.first() is None:
            print(f'Publisher with name contains \033[1m{input_inf}\033[0m does not exist.')
        else:
            for p in query.all():
                print(p)


# Task 2 (find publisher books on stocks
def find_publisher_shops():
    """
    Function finds all books from inputted publisher in stocks.
    """
    input_inf = input('Input publisher ID (digit) or publisher name to find shop with his books on stock: ')
    if input_inf.isdigit():
        query = session.query(
            Shop, Stock, Book, Publisher,
        ).filter(Shop.id == Stock.id_shop,
                 ).filter(Stock.id_book == Book.id,
                          ).filter(Book.id_publisher == Publisher.id,
                                   ).filter(Publisher.id == int(input_inf))
    else:
        query = session.query(
            Shop, Stock, Book, Publisher,
        ).filter(Shop.id == Stock.id_shop,
                 ).filter(Stock.id_book == Book.id,
                          ).filter(Book.id_publisher == Publisher.id,
                                   ).filter(Publisher.name.ilike(f'%{input_inf}%'))

    if query.first() is None:
        print(f'There is no book stocks for this publisher.')
    else:
        for stock in query:
            if stock.Stock.count > 0:
                print(f'Publisher \033[1m{stock.Publisher.name}\033[0m '
                      f'has book \033[1m"{stock.Book.title}"\033[0m '
                      f'in shop \033[1m{stock.Shop.name}\033[0m with '
                      f'a stock of \033[1m{stock.Stock.count}\033[0m book(s)')


find_publisher()
find_publisher_shops()

session.close()
