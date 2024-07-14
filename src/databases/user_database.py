from sqlalchemy import select

from src.models.user_model import User
from src.databases.connect import Session


def create_user(user: User) -> tuple[bool, None | dict[str, any]]:
    with Session() as session:
        session.begin()
        try:
            session.add(user)
        except:
            session.rollback()
            return False, None
        else:
            session.flush()
            user_dict = user._to_dict()
            print('From the database...')
            print(user_dict)
            session.commit()
            return True, user_dict

def get_user_by_id(id: str, do_serialize: bool = False) -> User | dict[str, any] | None:
    with Session() as session:
        statement = select(User).filter_by(id=id)
        user = session.scalars(statement).one_or_none()
        if user:
            if do_serialize:
                return user._to_dict()
            return user
        else:
            return None
        
def update_user_by_id(id: str, update: dict, do_serialize: bool = False) -> tuple[bool, User | dict[str, any] | None]:
    with Session() as session:
        session.begin()
        try:
            user = session.query(User).filter(User.id == id).update(update)
        except:
            session.rollback()
            return False, None
        else:
            if user == 0:
                session.rollback()
                return False, None
            session.commit()
            updated_user = get_user_by_id(id, do_serialize=do_serialize)
            return True, updated_user