%logstart -ot sqlalchemy.log.3
import sqlalchemy

from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String
class MyUser(Base):
    __tablename__ = 'myusers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
       return "<MyUser(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)

Base.metadata.create_all(engine)

ed_user = MyUser(name='ed', fullname='Ed Jones', password='edspassword')

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

ed_user = MyUser(name='ed', fullname='Ed Jones', password='edspassword')
session.add(ed_user)

our_user = session.query(MyUser).filter_by(name='ed').first()

session.add_all([
    MyUser(name='wendy', fullname='Wendy Williams', password='foobar'),
    MyUser(name='mary', fullname='Mary Contrary', password='xxg527'),
    MyUser(name='fred', fullname='Fred Flinstone', password='blah')])

ed_user.password = 'f8s7ccs'
session.dirty
session.new
session.commit()

ed_user.id

ed_user.name = 'Edwardo'
fake_user = User(name='fakeuser', fullname='Invalid', password='12345')
session.add(fake_user)

session.query(User).filter(User.name.in_(['Edwardo', 'fakeuser'])).all()

session.rollback()
ed_user.name
fake_user in session

session.query(User).filter(User.name.in_(['ed', 'fakeuser'])).all()
