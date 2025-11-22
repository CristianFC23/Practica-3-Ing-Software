<template>
  <div class="page-container">
    <button @click="volverDashboard" class="btn-home">🏠</button>

    <div class="dashboard-cards">
      <div class="card ubicaciones-card">
        <div class="card-header">
          <div class="card-icon ubicaciones-icon">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon">
              <path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path>
            </svg>
          </div>

          <div class="card-title">
            <h3>Equipos Médicos - {{ categoriaActual }}</h3>
            <p>Sede: {{ sedeActual }}</p>
          </div>
        </div>

        <div class="card-body">
          <input
            type="text"
            v-model="searchQuery"
            placeholder="Buscar por nombre, código o marca"
            class="search-input"
          />
          <button @click="refrescarLista" class="refresh-btn" :disabled="loading">
            {{ loading ? 'Cargando...' : 'Refrescar' }}
          </button>
        </div>

        <div v-if="loading" class="loading-state">
          <p>Cargando equipos...</p>
        </div>

        <div v-if="error" class="error-state">
          <p>{{ error }}</p>
          <button @click="refrescarLista" class="retry-btn">Reintentar</button>
        </div>

        <div v-if="!loading && !error" class="card-body ubicaciones-list">
          <div v-if="equiposFiltrados.length === 0" class="no-results">
            <p>
              {{ searchQuery
                ? 'No se encontraron equipos que coincidan con la búsqueda'
                : 'No hay equipos registrados en esta categoría' }}
            </p>
          </div>

          <div v-else>
            <p class="results-count">
              {{ equiposFiltrados.length }} equipo(s) encontrado(s)
            </p>
            
            <div v-for="equipo in equiposFiltrados" :key="equipo.id" class="ubicacion-item">
              <div class="ubicacion-info">
                <p class="ubicacion-nombre">{{ equipo.nombre }}</p>
                <p class="ubicacion-detalle">
                  Código: {{ equipo.codigo }} – Marca: {{ equipo.marca }}
                </p>
                <p class="ubicacion-telefono">
                  📍 {{ equipo.ubicacion }} | Estado: {{ equipo.estado }}
                </p>
              </div>

              <div class="acciones">
                <button class="edit-btn" @click.stop="editarEquipo(equipo)">MÁS INFORMACIÓN</button>
                <button class="delete-btn" @click.stop="eliminarEquipo(equipo.id)">ELIMINAR</button>
              </div>
            </div>

          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
import { useRoute, useRouter } from 'vue-router';
import { ref, computed } from 'vue';

export default {
  setup() {
    const route = useRoute();
    const router = useRouter();
    
    const sedeActual = ref(route.query.sede || 'Sede desconocida');
    const categoriaActual = ref(route.query.categoria || 'todos');
    const searchQuery = ref('');
    const loading = ref(false);
    const error = ref(null);

    const equipos = ref([
      { id: 1, nombre: 'Rayos X Digital', codigo: 'RX-001', marca: 'Siemens', ubicacion: 'Sala 1', estado: 'activo' },
      { id: 2, nombre: 'Ecógrafo', codigo: 'ECO-002', marca: 'GE Healthcare', ubicacion: 'Sala 2', estado: 'activo' },
      { id: 3, nombre: 'Tomógrafo', codigo: 'TC-003', marca: 'Philips', ubicacion: 'Sala 3', estado: 'inactivo' },
    ]);

    const equiposFiltrados = computed(() => {
      let resultado = equipos.value;

      if (categoriaActual.value !== 'todos') {
        resultado = resultado.filter(e => e.estado === categoriaActual.value);
      }

      if (searchQuery.value) {
        const q = searchQuery.value.toLowerCase();
        resultado = resultado.filter(e =>
          e.nombre.toLowerCase().includes(q) ||
          e.codigo.toLowerCase().includes(q) ||
          e.marca.toLowerCase().includes(q)
        );
      }

      return resultado;
    });

    const refrescarLista = () => {
      loading.value = true;
      setTimeout(() => loading.value = false, 500);
    };

    const editarEquipo = (equipo) => {
      router.push({
        name: 'detalles',
        params: { id: equipo.id },
        query: {
          sede: sedeActual.value,
          categoria: categoriaActual.value
        }
      });
    };

    const eliminarEquipo = (id) => {
      if (confirm('¿Seguro que quieres eliminar este equipo?')) {
        equipos.value = equipos.value.filter(e => e.id !== id);
        alert('Equipo eliminado correctamente');
      }
    };

    const volverDashboard = () => {
      router.push({ name: 'home' });
    };

    return {
      sedeActual,
      categoriaActual,
      searchQuery,
      loading,
      error,
      equipos,
      equiposFiltrados,
      refrescarLista,
      editarEquipo,
      eliminarEquipo,
      volverDashboard
    };
  }
};
</script>

<style scoped>
.page-container {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  height: 100vh;
  overflow: hidden;
  padding: 50px;
  background: #244652;
}

.dashboard-cards {
  display: grid;
  grid-template-columns: 1fr;
  max-width: 600px;
  width: 100%;
}

.card {
  background: rgba(255, 255, 255, 0.95);
  border-radius: 24px;
  padding: 25px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
}

.card-header {
  display: flex;
  align-items: flex-start;
  margin-bottom: 20px;
}

.card-icon {
  width: 55px;
  height: 55px;
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 15px;
  background: #244652;
}

.icon {
  width: 28px;
  height: 28px;
  color: white;
}

.card-title h3 {
  font-size: 20px;
  font-weight: 700;
  margin: 0 0 5px 0;
  color: #212a31;
}

.card-title p {
  font-size: 14px;
  color: #5a6c7d;
  margin: 0;
}

/* INPUT BUSCADOR */
.search-input {
  width: 95%;
  padding: 12px;
  border: 1px solid #244652;
  border-radius: 10px;
  font-size: 14px;
  transition: 0.2s ease;
  margin-bottom: 10px;
  background: rgba(255, 255, 255, 0.9);
}

.search-input:focus {
  border-color: #212a31;
  outline: none;
  box-shadow: 0 0 0 2px rgba(36, 70, 82, 0.2);
}

/* BOTONES */
.refresh-btn,
.retry-btn {
  padding: 8px 16px;
  border: 1px solid #244652;
  border-radius: 8px;
  background: white;
  color: #244652;
  cursor: pointer;
  font-size: 13px;
  transition: 0.2s ease;
  font-weight: 600;
}

.refresh-btn:hover,
.retry-btn:hover {
  background: #244652;
  color: white;
}

.refresh-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

/* ESTADOS */
.loading-state,
.error-state,
.no-results {
  text-align: center;
  padding: 30px;
  color: #5a6c7d;
}

.error-state {
  color: #e74c3c;
}

.results-count {
  font-size: 12px;
  color: #244652;
  margin-bottom: 15px;
  font-weight: 600;
}

/* LISTA */
.ubicaciones-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
  max-height: 60vh;
  overflow-y: auto;
  padding-right: 8px;
}

.ubicaciones-list::-webkit-scrollbar {
  width: 8px;
}

.ubicaciones-list::-webkit-scrollbar-track {
  background: #f0f0f0;
  border-radius: 6px;
}

.ubicaciones-list::-webkit-scrollbar-thumb {
  background: #244652;
  border-radius: 6px;
}

.ubicaciones-list::-webkit-scrollbar-thumb:hover {
  background: #212a31;
}

/* ITEMS */
.ubicacion-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #ffffff;
  border-radius: 14px;
  padding: 16px;
  border-left: 4px solid #244652;
  transition: 0.3s ease;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.ubicacion-item:hover {
  background: #f8f9fa;
  transform: translateX(6px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.12);
}

.ubicacion-info {
  flex: 1;
}

.ubicacion-nombre {
  font-weight: 700;
  color: #212a31;
  margin: 0 0 5px 0;
  font-size: 16px;
}

.ubicacion-detalle {
  font-size: 13px;
  color: #5a6c7d;
  margin: 0 0 5px 0;
}

.ubicacion-telefono {
  font-size: 12px;
  color: #244652;
  font-weight: 600;
  margin: 0;
}

.acciones {
  display: flex;
  gap: 6px;
}

/* EDITAR */
.edit-btn {
  background: #00bab3;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 8px;
  cursor: pointer;
  font-size: 12px;
  font-weight: 600;
  transition: all 0.3s ease;
}

.edit-btn:hover {
  background: #6fc232;
  transform: translateY(-2px);
}

/* ELIMINAR */
.delete-btn {
  background: #e74c3c;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 8px;
  cursor: pointer;
  font-size: 12px;
  font-weight: 600;
  transition: all 0.3s ease;
}

.delete-btn:hover {
  background: #c0392b;
  transform: translateY(-2px);
}

/* BOTÓN HOME */
.btn-home {
  position: fixed;
  top: 20px;
  left: 20px;
  width: 55px;
  height: 55px;
  border-radius: 50%;
  background: white;
  color: white;
  border: none;
  font-size: 26px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 16px rgba(129, 215, 66, 0.3);
  transition: 0.3s ease;
  z-index: 1000;
}

.btn-home:hover {
  transform: scale(1.1);
  background: #00bab3;
  box-shadow: 0 6px 20px rgba(129, 215, 66, 0.4);
}

.btn-home:active {
  transform: scale(0.95);
}
</style>