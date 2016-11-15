%logstart -ot sqlalchemy.log.5
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
fake_user = MyUser(name='fakeuser', fullname='Invalid', password='12345')
session.add(fake_user)

session.query(MyUser).filter(MyUser.name.in_(['Edwardo', 'fakeuser'])).all()

session.rollback()
ed_user.name
fake_user in session

session.query(MyUser).filter(MyUser.name.in_(['ed', 'fakeuser'])).all()

for instance in session.query(MyUser).order_by(MyUser.id):
     print(instance.name, instance.fullname)
for name, fullname in session.query(MyUser.name, MyUser.fullname):
     print(name, fullname)
for row in session.query(MyUser, MyUser.name).all():
     print(row.MyUser, row.name)
for row in session.query(MyUser.name.label('name_label')).all():
     print(row.name_label)

from sqlalchemy.orm import aliased
user_alias = aliased(MyUser, name='user_alias')

for row in session.query(user_alias, user_alias.name).all():
     print(row.user_alias)
for u in session.query(MyUser).order_by(MyUser.id)[1:3]:
     print(u)
for name, in session.query(MyUser.name).filter_by(fullname='Ed Jones'):
     print(name)
for name, in session.query(MyUser.name).filter(MyUser.fullname=='Ed Jones'):
     print(name)
for user in session.query(MyUser).filter(MyUser.name=='ed').filter(MyUser.fullname=='Ed Jones'):
     print(user)

query = session.query(MyUser).filter(MyUser.name.like('%ed')).order_by(MyUser.id)
query.all()
query.first()
user = query.one()
user = query.filter(MyUser.id == 99).one()
query = session.query(MyUser.id).filter(MyUser.name == 'ed').order_by(MyUser.id)

from sqlalchemy import text
for user in session.query(MyUser).filter(text("id<224")).order_by(text("id")).all():
     print(user.name)
session.query(MyUser).filter(text("id<:value and name=:name")).params(value=224, name='fred').order_by(MyUser.id).one()
session.query(MyUser).from_statement(text("SELECT * FROM myusers where name=:name")).params(name='ed').all()
stmt = text("SELECT name, id, fullname, password ""FROM myusers where name=:name")
stmt = stmt.columns(MyUser.name, MyUser.id, MyUser.fullname, MyUser.password)
session.query(MyUser).from_statement(stmt).params(name='ed').all()
stmt = text("SELECT name, id FROM myusers where name=:name")
stmt = stmt.columns(MyUser.name, MyUser.id)
session.query(MyUser).filter(MyUser.name.like('%ed')).count()
from sqlalchemy import func
session.query(func.count(MyUser.name), MyUser.name).group_by(MyUser.name).all()
session.query(func.count('*')).select_from(MyUser).scalar()
session.query(func.count(MyUser.id)).scalar()

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
class Address(Base):
     __tablename__ = 'addresses'
     id = Column(Integer, primary_key=True)
     email_address = Column(String, nullable=False)
     user_id = Column(Integer, ForeignKey('myusers.id'))
     user = relationship("MyUser", back_populates="addresses")
     def __repr__(self):
         return "<Address(email_address='%s')>" % self.email_address
