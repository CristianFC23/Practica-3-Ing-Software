<template>
  <div class="page-container">
    <button @click="volver" class="btn-home">🏠</button>

    <div class="detalles-container">
      <!-- IZQUIERDA -->
      <div class="columna-izquierda">
        <div class="foto-container">
          <div class="foto-placeholder">
            <p>📷</p>
            <span>Imagen actual o nueva</span>
            <input type="file" ref="fileInput" @change="handleImageUpload" style="display: none;" />
            <button class="upload-btn" @click="$refs.fileInput.click()">Cambiar imagen</button>
            <p v-if="imagenNombre" class="imagen-nombre">{{ imagenNombre }}</p>
          </div>
        </div>

        <button class="action-btn save-btn" @click="actualizarEquipo">💾 Guardar Cambios</button>
        <button class="action-btn cancel-btn" @click="volver">❌ Cancelar</button>
      </div>

      <!-- DERECHA -->
      <div class="columna-derecha">
        <div class="dashboard-card">
          <h2 class="dashboard-title">Editar Equipo</h2>
          <p class="subtitulo">Modifique los datos del equipo</p>

          <div class="info-scrolleable">

            <!-- GENERO SOLO UN EJEMPLO CORTO,
                 tú puedes pegar aquí todo el mismo contenido
                 de CrearEquipo.vue porque usan los mismos campos -->

            <div class="info-section">
              <h3 class="section-title">📋 Información General</h3>

              <div class="info-grid">
                <div class="info-item">
                  <label>Servicio:</label>
                  <input v-model="equipo.servicio" type="text" />
                </div>

                <div class="info-item">
                  <label>Sede:</label>
                  <select v-model="equipo.sede">
                    <option value="">Seleccionar</option>
                    <option value="Prado">Prado</option>
                    <option value="SIU">SIU</option>
                    <option value="San Vicente">San Vicente</option>
                  </select>
                </div>

                <div class="info-item">
                  <label>Nombre del equipo:</label>
                  <input v-model="equipo.nombre_equipo" type="text" />
                </div>

                <div class="info-item">
                  <label>Código inventario:</label>
                  <input v-model="equipo.codigo_inventario" type="text" />
                </div>

                <div class="info-item">
                  <label>Marca:</label>
                  <input v-model="equipo.marca" type="text" />
                </div>

                <div class="info-item">
                  <label>Modelo:</label>
                  <input v-model="equipo.modelo" type="text" />
                </div>

                <div class="info-item full-width">
                  <label>Ubicación física:</label>
                  <input v-model="equipo.ubicacion_fisica" type="text" />
                </div>
              </div>
            </div>

            <!-- Aquí pegarías todas las demás secciones 
                 igual que en CrearEquipo.vue 
                 (metrología, condiciones, documentos, etc.)-->

          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import { useRouter, useRoute } from "vue-router";
import axios from "axios";

export default {
  setup() {
    const router = useRouter();
    const route = useRoute();
    const fileInput = ref(null);

    const API_URL = "http://127.0.0.1:8000/api/equipos/";

    const equipo = ref({});
    const imagenNombre = ref("");

    const camposObligatorios = [
      "servicio",
      "sede",
      "nombre_equipo",
      "codigo_inventario",
      "marca",
      "modelo",
    ];

    // -------------------------------
    // Cargar equipo al abrir vista
    // -------------------------------
    const cargarEquipo = async () => {
      const id = route.params.id;
      try {
        const res = await axios.get(API_URL + id + "/");
        equipo.value = res.data;
      } catch (e) {
        console.error("Error cargando equipo:", e);
        alert("No se pudo cargar la información del equipo.");
      }
    };

    onMounted(() => {
      cargarEquipo();
    });

    // -------------------------------
    // Manejo imagen (solo nombre)
    // -------------------------------
    const handleImageUpload = (event) => {
      const f = event.target.files[0];
      if (f) {
        imagenNombre.value = f.name;
      }
    };

    // -------------------------------
    // Rellenar NI solo en los opcionales
    // -------------------------------
    const llenarNI = (data) => {
      const out = {};
      for (const key in data) {
        if (!data[key] || data[key].toString().trim() === "") {
          out[key] = "NI";
        } else {
          out[key] = data[key];
        }
      }
      return out;
    };

    // -------------------------------
    // PUT (actualizar)
    // -------------------------------
    const actualizarEquipo = async () => {
      for (const campo of camposObligatorios) {
        if (!equipo.value[campo] || equipo.value[campo].trim() === "") {
          alert(`El campo obligatorio "${campo}" está vacío.`);
          return;
        }
      }

      const payload = llenarNI(equipo.value);

      try {
        await axios.put(API_URL + route.params.id + "/", payload);
        alert("Equipo actualizado.");
        volver();
      } catch (e) {
        console.error("Error actualizando:", e);
        alert("Error al actualizar.");
      }
    };

    const volver = () => {
      router.push({ name: "equipos" });
    };

    return {
      equipo,
      imagenNombre,
      handleImageUpload,
      actualizarEquipo,
      volver,
      fileInput,
    };
  },
};
</script>


<style scoped>
.page-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  padding: 40px;
  background: #244652;
  box-sizing: border-box;
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
  border: none;
  font-size: 26px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 16px rgba(129, 215, 66, 0.3);
  transition: 0.3s ease;
  z-index: 1000;
  padding-bottom: 7px;
}

/* CONTENEDOR PRINCIPAL */
.detalles-container {
  display: grid;
  grid-template-columns: 320px 1fr;
  gap: 25px;
  max-width: 1400px;
  width: 100%;
  height: 85vh;
}

/* COLUMNA IZQUIERDA */
.columna-izquierda {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.foto-container {
  background: rgba(255, 255, 255, 0.95);
  border-radius: 24px;
  padding: 20px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
}

.foto-placeholder {
  width: 100%;
  aspect-ratio: 1;
  background: linear-gradient(135deg, #f0f0f0 0%, #e0e0e0 100%);
  border-radius: 16px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border: 2px dashed #244652;
  gap: 10px;
  padding: 20px;
}

.imagen-nombre {
  font-size: 12px;
  color: #5a6c7d;
  margin-top: 6px;
}

.upload-btn {
  background: #00bab3;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 8px;
  cursor: pointer;
  font-size: 13px;
  font-weight: 600;
  transition: all 0.3s ease;
  margin-top: 10px;
}

/* BOTONES DE ACCIÓN */
.action-btn {
  background: white;
  color: #244652;
  border: 2px solid #244652;
  padding: 14px 20px;
  border-radius: 16px;
  cursor: pointer;
  font-size: 15px;
  font-weight: 600;
  transition: all 0.3s ease;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.save-btn {
  background: #6fc232;
  color: white;
  border-color: #6fc232;
}

.cancel-btn:hover {
  background: #e74c3c;
  color: white;
  border-color: #e74c3c;
}

/* COLUMNA DERECHA */
.columna-derecha {
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.dashboard-card {
  background: rgba(255, 255, 255, 0.95);
  border-radius: 24px;
  padding: 30px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  height: 100%;
  overflow: hidden;
}

.dashboard-title {
  margin: 0;
  font-size: 26px;
  font-weight: 700;
  color: #244652;
}

.subtitulo {
  font-size: 14px;
  color: #5a6c7d;
  margin: 5px 0 20px 0;
}

/* ÁREA SCROLLEABLE */
.info-scrolleable {
  flex: 1;
  overflow-y: auto;
  padding-right: 15px;
}

.info-section {
  margin-bottom: 30px;
  padding-bottom: 20px;
  border-bottom: 2px solid #f0f0f0;
}

.section-title {
  font-size: 18px;
  font-weight: 700;
  color: #212a31;
  margin: 0 0 15px 0;
  padding-bottom: 10px;
  border-bottom: 2px solid #00bab3;
  display: flex;
  align-items: center;
  gap: 8px;
}

.info-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 15px;
}

.info-item {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.info-item.full-width {
  grid-column: 1 / -1;
}

.info-item label {
  font-size: 12px;
  font-weight: 600;
  color: #5a6c7d;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.required {
  color: #e74c3c;
  font-weight: 700;
}

.info-item input,
.info-item select,
.info-item textarea {
  font-size: 14px;
  color: #212a31;
  padding: 10px 12px;
  background: #f8f9fa;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  transition: all 0.3s ease;
  font-family: inherit;
}

.info-item input:focus,
.info-item select:focus,
.info-item textarea:focus {
  outline: none;
  border-color: #00bab3;
  background: white;
  box-shadow: 0 0 0 3px rgba(0, 186, 179, 0.1);
}

/* RESPONSIVE */
@media (max-width: 1024px) {
  .detalles-container {
    grid-template-columns: 1fr;
    height: auto;
  }
  .columna-izquierda {
    flex-direction: row;
    flex-wrap: wrap;
  }
  .foto-container {
    flex: 1;
    min-width: 200px;
  }
  .action-btn {
    flex: 1;
    min-width: 150px;
  }
}

@media (max-width: 768px) {
  .page-container {
    padding: 20px;
  }
  .info-grid {
    grid-template-columns: 1fr;
  }
  .columna-izquierda {
    flex-direction: column;
  }
  .dashboard-title {
    font-size: 22px;
  }
  .section-title {
    font-size: 16px;
  }
}
</style>
