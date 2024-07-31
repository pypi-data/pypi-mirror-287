from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from entities.base import Base
from data_access.repositories.category_repository import CategoryRepository
from data_access.repositories.channel_repository import ChannelRepository
from data_access.repositories.message_repository import MessageRepository


class UnitOfWork:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def __enter__(self):
        self.session = self.Session()
        self.categories = CategoryRepository(self.session)
        self.channels = ChannelRepository(self.session)
        self.messages = MessageRepository(self.session)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            self.session.rollback()
        else:
            self.session.commit()
        self.session.close()
