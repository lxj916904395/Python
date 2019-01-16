#!/usr/bin/env python 
# -*- coding:utf-8 -*-


from sqlalchemy import Column, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


# ORM就是把数据库表的行与相应的对象建立关联，互相转换

# 创建对象的基类:
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))

    # 一对多:
    # 查询一个User对象时，该对象的books属性将返回一个包含若干个Book对象的list。
    books = relationship('Book')

    def __str__(self):
        return 'id:' + self.id + ' name:' + self.name


# 一个User拥有多个Book，就可以定义一对多关系
class Book(Base):
    __tablename__ = 'book'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # “多”的一方的book表是通过外键关联到user表的:
    user_id = Column(String(20), ForeignKey('user.id'))

    def __str__(self):
        return 'id:' + self.id + ' name:' + self.name + ' 拥有者:' + self.user_id


# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:lxj4522241991@localhost:3306/mytest')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

"""插入数据表"""


def insert():
    session = DBSession()
    new_user = User(id='1111', name='bob')
    # 添加新数据
    session.add(new_user)

    # 提交即保存到数据库:
    session.commit()
    session.close()


def insert_book():
    session = DBSession()
    # session.execute('create table book (id varchar(20) primary key ,name varchar(20), user_id varchar (20))')

    book = Book(id='1', name='iOS开发', user_id='1')
    session.add(book)

    session.commit()
    session.close()


"""查询"""


def query():
    session = DBSession()

    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    user = session.query(User).filter(User.id).all()

    if isinstance(user, list):
        for u in user:
            for book in u.books:
                print(book)
            print(u)
    else:
        print(user)

    session.close()


"""删除"""


def delete():
    session = DBSession()

    session.execute('delete from user where id=\'1111\'')
    session.commit()
    session.close()




if __name__ == '__main__':
    # insert()
    # insert_book()
    # query()
    delete()
