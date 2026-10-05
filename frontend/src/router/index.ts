import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
const StandAllocation = () => import('@/views/stand_allocation/index.vue')
const FlightGround = () => import('@/views/flight_ground/index.vue')
const BridgeDock = () => import('@/views/bridge_dock/index.vue')
const BaggageLoad = () => import('@/views/baggage_load/index.vue')
const CargoHandling = () => import('@/views/cargo_handling/index.vue')
const FuelService = () => import('@/views/fuel_service/index.vue')
const CabinClean = () => import('@/views/cabin_clean/index.vue')
const PotableWater = () => import('@/views/potable_water/index.vue')
const Lavatory = () => import('@/views/lavatory/index.vue')
const AirStair = () => import('@/views/air_stair/index.vue')
const BeltLoader = () => import('@/views/belt_loader/index.vue')
const Gpu = () => import('@/views/gpu/index.vue')
const Pushback = () => import('@/views/pushback/index.vue')
const CrewShift = () => import('@/views/crew_shift/index.vue')
const Irregularity = () => import('@/views/irregularity/index.vue')
const EquipInspect = () => import('@/views/equip_inspect/index.vue')
const Deicing = () => import('@/views/deicing/index.vue')
const Catering = () => import('@/views/catering/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: Dashboard },
    { path: '/stand_allocation', name: 'stand_allocation', component: StandAllocation },
    { path: '/flight_ground', name: 'flight_ground', component: FlightGround },
    { path: '/bridge_dock', name: 'bridge_dock', component: BridgeDock },
    { path: '/baggage_load', name: 'baggage_load', component: BaggageLoad },
    { path: '/cargo_handling', name: 'cargo_handling', component: CargoHandling },
    { path: '/fuel_service', name: 'fuel_service', component: FuelService },
    { path: '/cabin_clean', name: 'cabin_clean', component: CabinClean },
    { path: '/potable_water', name: 'potable_water', component: PotableWater },
    { path: '/lavatory', name: 'lavatory', component: Lavatory },
    { path: '/air_stair', name: 'air_stair', component: AirStair },
    { path: '/belt_loader', name: 'belt_loader', component: BeltLoader },
    { path: '/gpu', name: 'gpu', component: Gpu },
    { path: '/pushback', name: 'pushback', component: Pushback },
    { path: '/crew_shift', name: 'crew_shift', component: CrewShift },
    { path: '/irregularity', name: 'irregularity', component: Irregularity },
    { path: '/equip_inspect', name: 'equip_inspect', component: EquipInspect },
    { path: '/deicing', name: 'deicing', component: Deicing },
    { path: '/catering', name: 'catering', component: Catering },
  ],
})

export default router
