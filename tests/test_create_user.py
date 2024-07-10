from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(username='aislan', email='aislan@mail.com', password='senha')
    session.add(user)
    session.commit()
    session.refresh(user)
    session.scalar(select(User).where(User.email == 'aislan@mail.com'))

    assert user.username == 'aislan'
