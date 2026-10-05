# 机场地面保障指挥平台

面向航空器停靠机位、廊桥对接、行李装卸、燃油加注、客梯车与污水勤务的航班地面保障调度后台。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 机位分配 | `stand_allocation` | 机位 | 机位编号、机位类型、可停机型 |
| 航班调配 | `flight_ground` | 进港航班 | 航班编号、航班号、航空公司 |
| 廊桥对接 | `bridge_dock` | 廊桥 | 廊桥编号、对应机位、对接机型 |
| 行李装卸 | `baggage_load` | 行李任务 | 任务编号、航班号、行李类型 |
| 货物装卸 | `cargo_handling` | 货运任务 | 任务编号、航班号、货物品类 |
| 燃油加注 | `fuel_service` | 加油任务 | 任务编号、航班号、燃油牌号 |
| 客舱清洁 | `cabin_clean` | 清洁任务 | 任务编号、航班号、清洁班组 |
| 上水服务 | `potable_water` | 上水任务 | 任务编号、航班号、上水车编号 |
| 污水勤务 | `lavatory` | 排污任务 | 任务编号、航班号、污物车编号 |
| 客梯车调度 | `air_stair` | 客梯车 | 车辆编号、车牌号、适用机型 |
| 传送带车 | `belt_loader` | 传送带车 | 车辆编号、车牌号、带速 |
| 地面电源 | `gpu` | 电源车 | 车辆编号、输出功率、电压等级 |
| 牵引车调度 | `pushback` | 牵引车 | 车辆编号、牵引力、适用机型 |
| 排班管理 | `crew_shift` | 保障班组 | 班组编号、保障类型、班组人数 |
| 异常事件 | `irregularity` | 异常事件 | 事件编号、航班号、异常类别 |
| 设备巡检 | `equip_inspect` | 巡检记录 | 记录编号、巡检设备、巡检区域 |
| 除冰作业 | `deicing` | 除冰任务 | 任务编号、航班号、除冰液类型 |
| 配餐服务 | `catering` | 配餐任务 | 任务编号、航班号、餐食品类 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。
