from sqlalchemy import Column, Integer, String, DateTime, Boolean, BigInteger, ForeignKey, Text
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, relationship

# Настройка асинхронного подключения к SQLite3
DB_URL = "sqlite+aiosqlite:///db/database.db"
engine = create_async_engine(DB_URL)  # Асинхронный движок SQLAlchemy
Session = async_sessionmaker(expire_on_commit=False, bind=engine)  # Фабрика сессий


class Base(DeclarativeBase, AsyncAttrs):
    """Базовый класс для декларативных моделей с поддержкой асинхронных атрибутов"""
    pass


class User(Base):
    """Модель для хранения запросов на подписку"""
    __tablename__ = "user"

    user_id = Column(BigInteger, primary_key=True)  # ID пользователя Telegram
    username = Column(String, nullable=True)  # @username пользователя
    first_name = Column(String, nullable=True)  # Имя пользователя
    last_name = Column(String, nullable=True)  # Фамилия пользователя
    user_is_block = Column(Boolean, default=False)  # Флаг блокировки пользователя


class Connection(Base):
    """Модель для хранения подключений"""
    __tablename__ = "connections"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String, nullable=False, unique=True)  # IP адрес (уникальный)
    start_time = Column(DateTime, nullable=False)  # Время начала подключения


async def create_tables():
    """Создает таблицы в базе данных"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
