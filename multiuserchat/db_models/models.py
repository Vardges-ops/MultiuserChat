from sqlalchemy import (
    Column, Integer, String, ForeignKey,
    Boolean, DateTime, Table, create_engine
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func


engine = create_engine("sqlite:///events.db", echo=True) # TODO fill with params
Base = declarative_base()

room_member_association = Table(
    'roommembers',
    Base.metadata,
    Column('room_id', Integer, ForeignKey('rooms.Id')),
    Column('member_id', Integer, ForeignKey('users.Id'))
)


class Rooms(Base):
    __tablename__ = "rooms"
    Id = Column(Integer, primary_key=True)
    type_name = Column(String, nullable=False)
    name = Column(String, nullable=False)
    pinned_message_id = Column(Integer, ForeignKey('messages.Id'))


class Conversations(Base):
    __tablename__ = "conversations"
    Id = Column(Integer, primary_key=True)
    start_timestamp = Column(DateTime, nullable=False)
    end_timestamp = Column(DateTime, nullable=False)

    room_id = Column(Integer, ForeignKey('rooms.Id'))
    room = relationship('Rooms')
    messages = relationship('Messages')


class Reactions(Base):
    __tablename__ = "reactions"
    Id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)


class User(Base):
    __tablename__ = "users"
    Id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    profile_pic = Column(String, nullable=False)
    last_seen = Column(DateTime)
    status = Column(String, nullable=False)

    rooms = relationship('Rooms', secondary=room_member_association)


class Messages(Base):
    __tablename__ = "messages"
    Id = Column(Integer, primary_key=True)
    text_content = Column(String)
    is_sent = Column(Boolean)
    timestamp = Column(DateTime, default=func.now())

    author_id = Column(Integer, ForeignKey('users.Id'))
    conversation_id = Column(Integer, ForeignKey('conversations.Id'))


class ForwardedMessages(Base):
    __tablename__ = "forwardedmessages"
    Id = Column(Integer, primary_key=True)

    conversation_id = Column(Integer, ForeignKey('conversations.Id'))
    origin_id = Column(Integer, ForeignKey('messages.Id'))
    forward_id = Column(Integer, ForeignKey('messages.Id'))


class MessageReaction(Base):
    __tablename__ = 'messagereactions'
    Id = Column(Integer, primary_key=True)
    message_id = Column(Integer, ForeignKey('messages.Id'))
    user_id = Column(Integer, ForeignKey('users.Id'))
    reaction_id = Column(Integer, ForeignKey('reactions.Id'))


def create_db():
    Base.metadata.create_all(engine)
