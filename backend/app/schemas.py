"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class StandAllocationEntry(BaseModel):
    """机位明细结构。"""

    field_0: str | None = None  # 机位编号
    field_1: str | None = None  # 机位类型
    field_2: str | None = None  # 可停机型
    field_3: str | None = None  # 廊桥位标识
    field_4: str | None = None  # 夜间限制
    field_5: str | None = None  # 开启时间
    field_6: str | None = None  # 关闭时间
    field_7: str | None = None  # 机位状态

class FlightGroundEntry(BaseModel):
    """进港航班明细结构。"""

    field_0: str | None = None  # 航班编号
    field_1: str | None = None  # 航班号
    field_2: str | None = None  # 航空公司
    field_3: str | None = None  # 机型
    field_4: str | None = None  # 计划到达
    field_5: str | None = None  # 实际到达
    field_6: str | None = None  # 分配机位
    field_7: str | None = None  # 航班状态

class BridgeDockEntry(BaseModel):
    """廊桥明细结构。"""

    field_0: str | None = None  # 廊桥编号
    field_1: str | None = None  # 对应机位
    field_2: str | None = None  # 对接机型
    field_3: str | None = None  # 操作员
    field_4: str | None = None  # 对接时间
    field_5: str | None = None  # 撤离时间
    field_6: str | None = None  # 保养周期
    field_7: str | None = None  # 廊桥状态

class BaggageLoadEntry(BaseModel):
    """行李任务明细结构。"""

    field_0: str | None = None  # 任务编号
    field_1: str | None = None  # 航班号
    field_2: str | None = None  # 行李类型
    field_3: str | None = None  # 件数
    field_4: str | None = None  # 卸机口
    field_5: str | None = None  # 装车号
    field_6: str | None = None  # 目的地
    field_7: str | None = None  # 任务状态

class CargoHandlingEntry(BaseModel):
    """货运任务明细结构。"""

    field_0: str | None = None  # 任务编号
    field_1: str | None = None  # 航班号
    field_2: str | None = None  # 货物品类
    field_3: str | None = None  # 重量吨
    field_4: str | None = None  # ULD板号
    field_5: str | None = None  # 装卸班组
    field_6: str | None = None  # 集装器号码
    field_7: str | None = None  # 任务状态

class FuelServiceEntry(BaseModel):
    """加油任务明细结构。"""

    field_0: str | None = None  # 任务编号
    field_1: str | None = None  # 航班号
    field_2: str | None = None  # 燃油牌号
    field_3: str | None = None  # 申请量
    field_4: str | None = None  # 实际加注量
    field_5: str | None = None  # 油车编号
    field_6: str | None = None  # 加油员
    field_7: str | None = None  # 任务状态

class CabinCleanEntry(BaseModel):
    """清洁任务明细结构。"""

    field_0: str | None = None  # 任务编号
    field_1: str | None = None  # 航班号
    field_2: str | None = None  # 清洁班组
    field_3: str | None = None  # 清洁等级
    field_4: str | None = None  # 预计时长
    field_5: str | None = None  # 开始时间
    field_6: str | None = None  # 完成时间
    field_7: str | None = None  # 任务状态

class PotableWaterEntry(BaseModel):
    """上水任务明细结构。"""

    field_0: str | None = None  # 任务编号
    field_1: str | None = None  # 航班号
    field_2: str | None = None  # 上水车编号
    field_3: str | None = None  # 水量升
    field_4: str | None = None  # 加水口位置
    field_5: str | None = None  # 操作员
    field_6: str | None = None  # 水质检测结果
    field_7: str | None = None  # 任务状态

class LavatoryEntry(BaseModel):
    """排污任务明细结构。"""

    field_0: str | None = None  # 任务编号
    field_1: str | None = None  # 航班号
    field_2: str | None = None  # 污物车编号
    field_3: str | None = None  # 排污口位置
    field_4: str | None = None  # 液位检测
    field_5: str | None = None  # 操作员
    field_6: str | None = None  # 消毒记录
    field_7: str | None = None  # 任务状态

class AirStairEntry(BaseModel):
    """客梯车明细结构。"""

    field_0: str | None = None  # 车辆编号
    field_1: str | None = None  # 车牌号
    field_2: str | None = None  # 适用机型
    field_3: str | None = None  # 可调高度
    field_4: str | None = None  # 当前位置
    field_5: str | None = None  # 驾驶员
    field_6: str | None = None  # 保养日期
    field_7: str | None = None  # 车辆状态

class BeltLoaderEntry(BaseModel):
    """传送带车明细结构。"""

    field_0: str | None = None  # 车辆编号
    field_1: str | None = None  # 车牌号
    field_2: str | None = None  # 带速
    field_3: str | None = None  # 可调高度
    field_4: str | None = None  # 最大载重
    field_5: str | None = None  # 当前位置
    field_6: str | None = None  # 驾驶员
    field_7: str | None = None  # 车辆状态

class GpuEntry(BaseModel):
    """电源车明细结构。"""

    field_0: str | None = None  # 车辆编号
    field_1: str | None = None  # 输出功率
    field_2: str | None = None  # 电压等级
    field_3: str | None = None  # 适用机型
    field_4: str | None = None  # 当前位置
    field_5: str | None = None  # 操作员
    field_6: str | None = None  # 供电时长
    field_7: str | None = None  # 车辆状态

class PushbackEntry(BaseModel):
    """牵引车明细结构。"""

    field_0: str | None = None  # 车辆编号
    field_1: str | None = None  # 牵引力
    field_2: str | None = None  # 适用机型
    field_3: str | None = None  # 当前位置
    field_4: str | None = None  # 驾驶员
    field_5: str | None = None  # 保养日期
    field_6: str | None = None  # 牵引记录
    field_7: str | None = None  # 车辆状态

class CrewShiftEntry(BaseModel):
    """保障班组明细结构。"""

    field_0: str | None = None  # 班组编号
    field_1: str | None = None  # 保障类型
    field_2: str | None = None  # 班组人数
    field_3: str | None = None  # 当班长
    field_4: str | None = None  # 值班时段
    field_5: str | None = None  # 在岗人数
    field_6: str | None = None  # 调休记录
    field_7: str | None = None  # 班组状态

class IrregularityEntry(BaseModel):
    """异常事件明细结构。"""

    field_0: str | None = None  # 事件编号
    field_1: str | None = None  # 航班号
    field_2: str | None = None  # 异常类别
    field_3: str | None = None  # 发现时间
    field_4: str | None = None  # 影响环节
    field_5: str | None = None  # 处置人
    field_6: str | None = None  # 恢复时间
    field_7: str | None = None  # 事件状态

class EquipInspectEntry(BaseModel):
    """巡检记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 巡检设备
    field_2: str | None = None  # 巡检区域
    field_3: str | None = None  # 巡检日期
    field_4: str | None = None  # 巡检人员
    field_5: str | None = None  # 发现隐患数
    field_6: str | None = None  # 整改期限
    field_7: str | None = None  # 巡检状态

class DeicingEntry(BaseModel):
    """除冰任务明细结构。"""

    field_0: str | None = None  # 任务编号
    field_1: str | None = None  # 航班号
    field_2: str | None = None  # 除冰液类型
    field_3: str | None = None  # 用量升
    field_4: str | None = None  # 除冰车编号
    field_5: str | None = None  # 操作员
    field_6: str | None = None  # 开始时间
    field_7: str | None = None  # 任务状态

class CateringEntry(BaseModel):
    """配餐任务明细结构。"""

    field_0: str | None = None  # 任务编号
    field_1: str | None = None  # 航班号
    field_2: str | None = None  # 餐食品类
    field_3: str | None = None  # 配备份数
    field_4: str | None = None  # 特殊餐食
    field_5: str | None = None  # 配餐车编号
    field_6: str | None = None  # 配送人员
    field_7: str | None = None  # 任务状态
