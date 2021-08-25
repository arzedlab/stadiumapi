import os
from models.database import DATABASE_NAME, Session, create_db
from models.stadium import Stadium


if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        create_db()

    # session = Session()
    
    # title = input('Input the title: ')
    # price = input('Input the price: ')
    # size = input('Input the size: ')
    # location = input('Input the location: ')

    # stadium_info = Stadium(title,price,size,location)

    # session.add(stadium_info)

    # session.commit()
    # session.close()


    session = Session()

    it = session.query(Stadium).filter_by(id=8).first()
    print(f'Title: {it.title} Price: {it.price}')
