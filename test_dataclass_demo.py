from dataclasses import dataclass
from datetime import datetime

# 使用 @dataclass
@dataclass
class HealthService:
    def get_status(self) -> dict[str, str]:
        return {"status": "ok", "time": datetime.utcnow().isoformat() + "Z"}

# 不使用 @dataclass
class HealthServiceTraditional:
    def __init__(self):
        pass
    
    def __repr__(self):
        return f"HealthServiceTraditional()"
    
    def __eq__(self, other):
        if not isinstance(other, HealthServiceTraditional):
            return False
        return True
    
    def get_status(self) -> dict[str, str]:
        return {"status": "ok", "time": datetime.utcnow().isoformat() + "Z"}

# 测试效果
if __name__ == "__main__":
    # 创建实例
    service1 = HealthService()
    service2 = HealthService()
    service_traditional = HealthServiceTraditional()
    
    print("=== @dataclass 效果演示 ===")
    print(f"1. 字符串表示: {service1}")
    print(f"2. 相等比较: {service1 == service2}")
    print(f"3. 类型检查: {type(service1)}")
    print(f"4. 方法调用: {service1.get_status()}")
    
    print("\n=== 传统方式对比 ===")
    print(f"1. 字符串表示: {service_traditional}")
    print(f"2. 相等比较: {service_traditional == HealthServiceTraditional()}")
    print(f"3. 类型检查: {type(service_traditional)}")
    print(f"4. 方法调用: {service_traditional.get_status()}")
