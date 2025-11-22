import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/components/HomeView.vue'
// import PacientesView from '@/components/PacientesView.vue'
// import LaboratoristasView from '@/components/LaboratoristasView.vue'
// import ResultadosView from '@/components/ResultadosView.vue'
// import NuevoResultado from '@/components/NuevoResultado.vue'
// import NuevoPaciente from '@/components/NuevoPaciente.vue'
// import NuevoLaboratorista from '@/components/NuevoLaboratorista.vue'
import EquiposView from'@/components/EquiposView.vue'
import DetallesView from '@/components/DetallesView.vue'
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  { 
    path: '/equipos',
    name: 'equipos',
    component: EquiposView
  },
  { 
    path: '/detalles',
    name: 'detalles',
    component: DetallesView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router