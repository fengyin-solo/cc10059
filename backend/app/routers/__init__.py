"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import stand_allocation as router_stand_allocation
from app.routers import flight_ground as router_flight_ground
from app.routers import bridge_dock as router_bridge_dock
from app.routers import baggage_load as router_baggage_load
from app.routers import cargo_handling as router_cargo_handling
from app.routers import fuel_service as router_fuel_service
from app.routers import cabin_clean as router_cabin_clean
from app.routers import potable_water as router_potable_water
from app.routers import lavatory as router_lavatory
from app.routers import air_stair as router_air_stair
from app.routers import belt_loader as router_belt_loader
from app.routers import gpu as router_gpu
from app.routers import pushback as router_pushback
from app.routers import crew_shift as router_crew_shift
from app.routers import irregularity as router_irregularity
from app.routers import equip_inspect as router_equip_inspect
from app.routers import deicing as router_deicing
from app.routers import catering as router_catering

ROUTERS = [router_stand_allocation, router_flight_ground, router_bridge_dock, router_baggage_load, router_cargo_handling, router_fuel_service, router_cabin_clean, router_potable_water, router_lavatory, router_air_stair, router_belt_loader, router_gpu, router_pushback, router_crew_shift, router_irregularity, router_equip_inspect, router_deicing, router_catering]
