from __future__ import annotations

from typing import Generator, Type, TypeVar, Callable
from functools import wraps

from ..services import HealthService, ETFService
from ..db import get_db_session 

T = TypeVar('T')

def create_dependency(service_class: Type[T], needs_db: bool = False) -> Callable[[], Generator[T, None, None]]:
    """创建服务依赖的通用函数"""
    def dependency() -> Generator[T, None, None]:
        if needs_db:
            db = next(get_db_session())
            service = service_class(db)
        else:
            service = service_class()
        
        try:
            yield service
        finally:
            if hasattr(service, 'cleanup'):
                service.cleanup()
    
    return dependency

# 使用通用函数创建依赖
get_health_service = create_dependency(HealthService)
get_etf_service = create_dependency(ETFService)
# 示例：如果需要数据库的服务
# get_user_service = create_dependency(UserService, needs_db=True)

__all__ = ["get_health_service", "get_etf_service", "get_db_session", "create_dependency"]
