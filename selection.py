import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import Publisher, Book, Shop, Stock


DSN = "postgresql://postgres:1375@localhost:5432/bookstore"
engine = sqlalchemy.create_engine(DSN)
Session = sessionmaker(bind=engine)
session = Session()


def shop_search(publ):
    """
    Находит магазины где продают целевого издателя.
    """
    if publ.isdigit():
        for shop in session.query(Shop).join(Stock).join(Book).join(
                Publisher).filter(Publisher.id == publ).all():
            print(shop)
    else:
        for shop in session.query(Shop).join(Stock).join(Book).join(
                Publisher).filter(
                Publisher.name == publ).all():
            print(shop)
session.close()

if __name__ == '__main__':
    shop_search(input("Введите название/id издателя:"))
