<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">机场地面保障指挥平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">面向航空器停靠机位、廊桥对接、行李装卸、燃油加注、客梯车与污水勤务的航班地面保障调度后台。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "机位分配", path: "/stand_allocation" }, { label: "航班调配", path: "/flight_ground" }, { label: "廊桥对接", path: "/bridge_dock" }, { label: "行李装卸", path: "/baggage_load" }, { label: "货物装卸", path: "/cargo_handling" }, { label: "燃油加注", path: "/fuel_service" }, { label: "客舱清洁", path: "/cabin_clean" }, { label: "上水服务", path: "/potable_water" }, { label: "污水勤务", path: "/lavatory" }, { label: "客梯车调度", path: "/air_stair" }, { label: "传送带车", path: "/belt_loader" }, { label: "地面电源", path: "/gpu" }, { label: "牵引车调度", path: "/pushback" }, { label: "排班管理", path: "/crew_shift" }, { label: "异常事件", path: "/irregularity" }, { label: "设备巡检", path: "/equip_inspect" }, { label: "除冰作业", path: "/deicing" }, { label: "配餐服务", path: "/catering" }]
</script>
