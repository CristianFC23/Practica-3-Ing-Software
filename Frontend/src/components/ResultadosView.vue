<template>
  <div class="page-container">
    <div class="dashboard-cards">
      <div class="card resultadoes-card">
        <div class="card-header">
          <div class="card-icon resultadoes-icon">
            <span>📊</span>
          </div>
          <div class="card-title">
            <h3>Resultados Médicos</h3>
            <p>Buscar, editar o eliminar resultados médicos</p>
          </div>
        </div>

        <div class="card-body">
          <input
            type="text"
            v-model="searchQuery"
            placeholder="Ingrese código de ingreso del paciente"
            class="search-input"
          />
          <button @click="refrescarLista" class="refresh-btn" :disabled="loading">
            {{ loading ? 'Cargando...' : 'Refrescar' }}
          </button>

          <router-link to="/resultados/nuevo" class="btn btn-primary">
            <span class="btn-icon">+</span> Nuevo Resultado
          </router-link>
        </div>

        <div v-if="loading" class="loading-state">
          <p>Cargando resultadoss...</p>
        </div>

        <div v-if="error" class="error-state">
          <p>{{ error }}</p>
          <button @click="refrescarLista" class="retry-btn">Reintentar</button>
        </div>

        <div v-if="!loading && !error" class="card-body resultadoes-list">
          <div v-if="resultadosFiltrados.length === 0" class="no-results">
            <p>
              {{ searchQuery
                ? 'No se encontraron resultadoss que coincidan con la búsqueda'
                : 'No hay resultadoss registrados' }}
            </p>
          </div>

          <div v-else>
            <p class="results-count">
              {{ resultadosFiltrados.length }} resultados(s) encontrado(s)
            </p>
            <div
              v-for="resultados in resultadosFiltrados"
              :key="resultados.id"
              class="resultado-item"
            >
              <div class="resultado-info">
                <p class="resultado-nombre"><strong>Codigo ingreso:</strong> {{ resultados.cod_ing_r }}</p>
                <p class="resultado-detalle"><strong>Cedula:</strong> {{ resultados.cedula }} </p>
                <p class="resultado-detalle"><strong>Colesterol Total:</strong> {{ resultados.col_tot }}</p>
                <p class="resultado-detalle"><strong>Colesterol HDL:</strong> {{ resultados.col_hdl }}</p>
                <p class="resultado-detalle"><strong>Colesterol LDL:</strong> {{ resultados.col_ldl }}</p>
              </div>
              <div class="acciones">
                <button class="edit-btn" @click.stop="abrirModalEditar(resultados)">EDITAR</button>
                <button class="delete-btn" @click.stop="eliminarresultados(resultados.id)">ELIMINAR</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Modal de edición -->
    <div v-if="mostrarModal" class="modal-overlay">
      <div class="modal-content">
        <h3>Editar resultados Médico</h3>
        
        <label>Código</label>
        <input v-model="resultadosEditando.codigo" placeholder="Ej: EQ-001" />
        
        <label>Nombre del resultados</label>
        <input v-model="resultadosEditando.nombre" placeholder="Ej: Monitor de Signos Vitales" />
        
        <label>Marca</label>
        <input v-model="resultadosEditando.marca" placeholder="Ej: Philips" />
        
        <label>Modelo</label>
        <input v-model="resultadosEditando.modelo" placeholder="Ej: IntelliVue MX40" />
        
        <label>Serial</label>
        <input v-model="resultadosEditando.serial" placeholder="Ej: SN123456789" />
        
        <label>Ubicación</label>
        <select v-model="resultadosEditando.resultado" required>
          <option disabled value="">Seleccione una ubicación</option>
          <option 
            v-for="resultado in resultadoes" 
            :key="resultado.id" 
            :value="resultado.id"
          >
            {{ resultado.nombre }}
          </option>
        </select>
        
        <label>Responsable</label>
        <select v-model="resultadosEditando.responsable" required>
          <option disabled value="">Seleccione un responsable</option>
          <option 
            v-for="responsable in responsables" 
            :key="responsable.id" 
            :value="responsable.id"
          >
            {{ responsable.nombre }} {{ responsable.apellido }}
          </option>
        </select>

        <div class="modal-buttons">
          <button @click="guardarCambios" class="save-btn">Guardar Cambios</button>
          <button @click="cerrarModal" class="cancel-btn">Cancelar</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      resultados: [],
      searchQuery: '',
      loading: false,
      error: null,
      mostrarModal: false,
      resultadosEditando: null,
      resultadoes: [],
      responsables: []
    }
  },
  created() {
    this.consultarResultados()
    this.consultarresultadoes()
    this.consultarResponsables()
  },
  computed: {
    resultadosFiltrados() {
      if (!this.searchQuery) return this.resultados
      const q = this.searchQuery.toLowerCase()
      return this.resultados.filter(e =>
        e.cod_ing_r?.toLowerCase().includes(q) ||
        e.cedula?.toLowerCase().includes(q)
      )
    }
  },
  methods: {
    async consultarResultados() {
      this.loading = true
      this.error = null
      try {
        const res = await fetch('http://127.0.0.1:8000/api/resultados/')
        if (!res.ok) throw new Error('Error al obtener resultados')
        const datos = await res.json()
        this.resultados = Array.isArray(datos) ? datos : []
      } catch (err) {
        console.error(err)
        this.error = 'Error al cargar los resultados'
        this.resultados = []
      } finally {
        this.loading = false
      }
    },

    async consultarresultadoes() {
      try {
        const res = await fetch('http://127.0.0.1:8000/api/pacientes/')
        this.resultadoes = await res.json()
      } catch (err) {
        console.error('Error al cargar resultadoes:', err)
        this.resultadoes = []
      }
    },

    async consultarResponsables() {
      try {
        const res = await fetch('http://127.0.0.1:8000/api/laboratoristas/')
        this.responsables = await res.json()
      } catch (err) {
        console.error('Error al cargar responsables:', err)
        this.responsables = []
      }
    },

    refrescarLista() {
      this.consultarResultados()
    },

    async eliminarResultado(id) {
      if (!confirm('¿Seguro que quieres eliminar este resultado?')) return
      try {
        const res = await fetch(`http://127.0.0.1:8000/api/labresults/${id}/`, {
          method: 'DELETE'
        })
        if (res.ok) {
          alert('Resultado eliminado correctamente')
          this.consultarResultados()
        } else {
          alert('Error al eliminar el resultado')
        }
      } catch (err) {
        console.error('Error al eliminar:', err)
        alert('Error al eliminar el resultado')
      }
    },

    abrirModalEditar(resultados) {
      this.resultadosEditando = { ...resultados }
      this.mostrarModal = true
    },
    cerrarModal() {
      this.mostrarModal = false
      this.resultadosEditando = null
    },

    async guardarCambios() {
      if (!this.resultadosEditando) return
      try {
        const res = await fetch(`http://127.0.0.1:8000/api/labresults/${this.resultadosEditando.id}/`, {
          method: 'PUT',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(this.resultadosEditando)
        })
        if (res.ok) {
          alert('Resultado actualizado correctamente')
          this.cerrarModal()
          this.consultarResultados()
        } else {
          alert('Error al actualizar el resultado')
        }
      } catch (err) {
        console.error('Error al actualizar:', err)
      }
    }
  }
}
</script>

<style scoped>
/* === CONTENEDOR GENERAL === */
.page-container {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  height: 100vh;
  overflow: hidden;
  padding: 0;
  background: none;
}

.dashboard-cards {
  display: grid;
  grid-template-columns: 1fr;
  max-width: 600px;
  width: 100%;
}

/* === TARJETAS === */
.card {
  background: rgba(255, 255, 255, 0.7);
  border-radius: 16px;
  padding: 25px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  border: 1px solid #C6A34F; /* cambiado a paleta base */
  transition: all 0.3s ease;
}

.card-header {
  display: flex;
  align-items: flex-start;
  margin-bottom: 20px;
}

.card-icon {
  width: 50px;
  height: 50px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 22px;
  margin-right: 15px;
}

/* icono con degradado paleta base */
.resultadoes-icon {
  background: linear-gradient(135deg, #C6A34F, #A3822F);
  color: #2c3e50;
}

.card-title h3 {
  font-size: 18px;
  font-weight: 600;
  margin: 0 0 5px 0;
  color: #2c3e50;
}

.card-title p {
  font-size: 14px;
  color: #7f8c8d;
  margin: 0;
  line-height: 1.4;
}

/* === INPUT DE BÚSQUEDA === */
.search-input {
  width: 100%;
  padding: 12px;
  border: 1px solid #e6d79a; /* suave acorde a paleta */
  border-radius: 8px;
  font-size: 14px;
  transition: all 0.2s ease;
  margin-bottom: 10px;
}

.search-input:focus {
  border-color: #A3822F;
  outline: none;
  box-shadow: 0 0 0 2px rgba(163, 130, 47, 0.18);
}

/* === BOTONES === */
.refresh-btn,
.retry-btn {
  padding: 8px 16px;
  border: 1px solid #A3822F;
  border-radius: 6px;
  background: white;
  color: #A3822F;
  cursor: pointer;
  font-size: 13px;
  font-weight: 500;
  transition: all 0.3s ease;
}
.refresh-btn:hover,
.retry-btn:hover {
  background: #C6A34F;
  color: #2c3e50;
}

/* === ESTADOS === */
.loading-state,
.error-state {
  text-align: center;
  padding: 20px;
  color: #8a6d2f;
}
.error-state {
  color: #c0392b;
}

/* === LISTA DE RESULTADOS === */
.resultadoes-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
  max-height: 400px;
  overflow-y: auto;
  padding-right: 8px;
  scrollbar-gutter: stable;
  scroll-behavior: smooth;
  box-shadow: inset 0 2px 6px rgba(0, 0, 0, 0.05);
}

/* === SCROLLBAR PERSONALIZADO === */
.resultadoes-list::-webkit-scrollbar {
  width: 8px;
}
.resultadoes-list::-webkit-scrollbar-thumb {
  background: rgba(198, 163, 79, 0.4); /* acorde a paleta */
  border-radius: 10px;
}
.resultadoes-list::-webkit-scrollbar-thumb:hover {
  background: rgba(163, 130, 47, 0.8);
}

/* === RESULTADOS === */
.results-count {
  font-size: 12px;
  color: #A3822F; /* acento paleta */
  margin-bottom: 15px;
  font-weight: 500;
}

.no-results {
  text-align: center;
  padding: 30px;
  color: #7f8c8d;
}

/* === ITEMS === */
.resultado-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #fffdf6;
  border-radius: 10px;
  padding: 15px;
  transition: all 0.3s ease;
  border-left: 4px solid #C6A34F;
}
.resultado-item:hover {
  background: #fff8e6;
  transform: translateX(5px);
}

.resultado-info {
  flex: 1;
}

.resultado-nombre {
  font-weight: 600;
  color: #2c3e50;
  margin: 0 0 8px 0;
  font-size: 16px;
}

.resultado-detalle {
  font-size: 13px;
  color: #7f8c8d;
  margin: 0 0 5px 0;
}
.resultado-detalle strong {
  color: #A3822F;
}

.acciones {
  display: flex;
  gap: 6px;
}

/* === BOTONES DE ACCIÓN === */
.edit-btn {
  background: linear-gradient(135deg, #C6A34F, #A3822F);
  color: #2c3e50;
  border: none;
  padding: 6px 12px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 12px;
  font-weight: 600;
}
.edit-btn:hover {
  background: linear-gradient(135deg, rgba(198,163,79,0.95), #a8883a);
}

.delete-btn {
  background: #e74c3c;
  color: white;
  border: none;
  padding: 6px 12px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 12px;
  font-weight: 600;
}
.delete-btn:hover {
  background: #c0392b;
}

/* === MODAL === */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
}

.modal-content {
  background: #fffef5;
  padding: 20px;
  border-radius: 12px;
  width: 400px;
  max-width: 90%;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  max-height: 90vh;
  overflow-y: auto;
}
.modal-content h3 {
  margin-top: 0;
  color: #2c3e50;
}
.modal-content label {
  font-size: 13px;
  color: #7f8c8d;
  margin-top: 10px;
  display: block;
  font-weight: 500;
}
.modal-content input,
.modal-content select {
  width: 100%;
  padding: 8px;
  margin-top: 4px;
  border: 1px solid #C6A34F;
  border-radius: 6px;
  font-size: 14px;
  box-sizing: border-box;
}
.modal-content input:focus,
.modal-content select:focus {
  border-color: #A3822F;
  outline: none;
  box-shadow: 0 0 0 2px rgba(163, 130, 47, 0.2);
}

.modal-buttons {
  margin-top: 15px;
  display: flex;
  justify-content: flex-end;
  gap: 8px;
}
.cancel-btn {
  background: #d5d5d5;
  color: #2c3e50;
  border: none;
  padding: 8px 16px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 13px;
}
.cancel-btn:hover {
  background: #bbb;
}
.save-btn {
  background: linear-gradient(135deg, #C6A34F, #A3822F);
  color: #2c3e50;
  border: none;
  padding: 8px 16px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 13px;
  font-weight: 600;
}
.save-btn:hover {
  background: linear-gradient(135deg, rgba(198,163,79,0.95), #a8883a);
}

/* === BOTÓN PRINCIPAL (+ NUEVO) === */
.btn {
  flex: 1;
  padding: 10px 14px;
  margin: 10px 50px;
  border: none;
  border-radius: 10px;
  font-weight: 600;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  text-decoration: none;
}
.btn-primary {
  background: linear-gradient(135deg, #C6A34F, #A3822F);
  color: white;
}
.btn-primary:hover {
  background: linear-gradient(135deg, rgba(198,163,79,0.95), #a8883a);
}
</style>
