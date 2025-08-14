from __future__ import annotations

from contextlib import contextmanager
import os
from pathlib import Path
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session

from ..core.config import get_settings


class Base(DeclarativeBase):
    pass


_engine = None
_SessionLocal: sessionmaker[Session] | None = None


def _ensure_sqlite_directory(database_url: str) -> None:
    if not database_url.startswith("sqlite"):
        return
    # Skip in-memory SQLite
    if database_url.endswith(":memory:") or database_url.endswith("?mode=memory&cache=shared"):
        return

    # Extract filesystem path from URL like sqlite:///./data/app.db
    raw_path = database_url.replace("sqlite:///", "", 1)
    # Handle absolute path case sqlite:////absolute/path.db
    if database_url.startswith("sqlite:////"):
        raw_path = database_url.replace("sqlite:////", "/", 1)

    db_path = Path(raw_path)
    directory = db_path.parent
    if directory and not directory.exists():
        os.makedirs(directory, exist_ok=True)


def _get_engine():
    global _engine
    if _engine is not None:
        return _engine

    settings = get_settings()
    _ensure_sqlite_directory(settings.database_url)
    connect_args = {"check_same_thread": False} if settings.database_url.startswith("sqlite") else {}
    _engine = create_engine(settings.database_url, echo=False, future=True, pool_pre_ping=True, connect_args=connect_args)
    return _engine


def get_sessionmaker() -> sessionmaker[Session]:
    global _SessionLocal
    if _SessionLocal is None:
        _SessionLocal = sessionmaker(bind=_get_engine(), autoflush=False, autocommit=False, expire_on_commit=False, class_=Session)
    return _SessionLocal


@contextmanager
def session_scope() -> Generator[Session, None, None]:
    session_local = get_sessionmaker()
    session = session_local()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


async def get_db_session() -> Generator[Session, None, None]:
    session_local = get_sessionmaker()
    session = session_local()
    try:
        yield session
    finally:
        session.close()


def init_db() -> None:
    # Place to import models to register metadata, then create tables
    # Example: from .models import *
    Base.metadata.create_all(bind=_get_engine())
