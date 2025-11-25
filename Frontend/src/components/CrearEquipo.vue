<template>
  <div class="page-container">
    <button @click="volverDashboard" class="btn-home">🏠</button>

    <div class="detalles-container">
      <!-- Columna Izquierda: Foto y Botones -->
      <div class="columna-izquierda">
        <div class="foto-container">
          <div class="foto-placeholder">
            <p>📷</p>
            <span>Subir foto del equipo</span>
            <input type="file" accept="image/*" @change="handleImageUpload" style="display: none;" ref="fileInput" />
            <button class="upload-btn" @click="$refs.fileInput.click()">
              Seleccionar imagen
            </button>
          </div>
        </div>

        <button class="action-btn save-btn" @click="guardarEquipo">
          💾 Guardar Equipo
        </button>

        <button class="action-btn cancel-btn" @click="cancelar">
          ❌ Cancelar
        </button>
      </div>

      <!-- Columna Derecha: Formulario Scrolleable -->
      <div class="columna-derecha">
        <div class="dashboard-card">
          <h2 class="dashboard-title">Agregar Nuevo Equipo Médico</h2>
          <p class="subtitulo">Complete la información del equipo</p>
          
          <div class="info-scrolleable">
            
            <!-- 1. INFORMACIÓN GENERAL -->
            <div class="info-section">
              <h3 class="section-title">📋 Información General</h3>
              <div class="info-grid">
                <div class="info-item">
                  <label>Proceso: <span class="required">*</span></label>
                  <input type="text" v-model="nuevoEquipo.proceso" placeholder="Ej: Diagnóstico por Imágenes" />
                </div>
                <div class="info-item">
                  <label>Nombre del equipo: <span class="required">*</span></label>
                  <input type="text" v-model="nuevoEquipo.nombreEquipo" placeholder="Ej: Rayos X Digital" />
                </div>
                <div class="info-item">
                  <label>Código de inventario: <span class="required">*</span></label>
                  <input type="text" v-model="nuevoEquipo.codigoInventario" placeholder="Ej: RX-001-LIME-2023" />
                </div>
                <div class="info-item">
                  <label>Código IPS:</label>
                  <input type="text" v-model="nuevoEquipo.codigoIPS" placeholder="Ej: IPS-RX-2023-045" />
                </div>
                <div class="info-item">
                  <label>Código ECRI:</label>
                  <input type="text" v-model="nuevoEquipo.codigoECRI" placeholder="Ej: 16-725" />
                </div>
                <div class="info-item">
                  <label>Responsable: <span class="required">*</span></label>
                  <input type="text" v-model="nuevoEquipo.responsable" placeholder="Ej: Dr. Carlos Martínez" />
                </div>
                <div class="info-item full-width">
                  <label>Ubicación física: <span class="required">*</span></label>
                  <input type="text" v-model="nuevoEquipo.ubicacionFisica" placeholder="Ej: Sala de Radiología 1 - Piso 2" />
                </div>
                <div class="info-item">
                  <label>Marca: <span class="required">*</span></label>
                  <input type="text" v-model="nuevoEquipo.marca" placeholder="Ej: Siemens" />
                </div>
                <div class="info-item">
                  <label>Modelo: <span class="required">*</span></label>
                  <input type="text" v-model="nuevoEquipo.modelo" placeholder="Ej: Luminos Agile Max" />
                </div>
                <div class="info-item">
                  <label>Serie:</label>
                  <input type="text" v-model="nuevoEquipo.serie" placeholder="Ej: SN-2023-RX-8947" />
                </div>
                <div class="info-item full-width">
                  <label>Clasificación eje misional:</label>
                  <input type="text" v-model="nuevoEquipo.clasificacionMisional" placeholder="Ej: Docencia, Investigación, Extensión" />
                </div>
                <div class="info-item">
                  <label>Clasificación IPS:</label>
                  <input type="text" v-model="nuevoEquipo.clasificacionIPS" placeholder="Ej: IND" />
                </div>
                <div class="info-item">
                  <label>Clasificación por riesgo:</label>
                  <input type="text" v-model="nuevoEquipo.clasificacionRiesgo" placeholder="Ej: Clase IIB - Riesgo Alto" />
                </div>
                <div class="info-item full-width">
                  <label>Registro Invima:</label>
                  <input type="text" v-model="nuevoEquipo.registroInvima" placeholder="Ej: 2023DM-0012345" />
                </div>
              </div>
            </div>

            <!-- 2. REGISTRO HISTÓRICO -->
            <div class="info-section">
              <h3 class="section-title">📅 Registro Histórico</h3>
              <div class="info-grid">
                <div class="info-item">
                  <label>Vida útil:</label>
                  <input type="text" v-model="nuevoEquipo.vidaUtil" placeholder="Ej: 10 años" />
                </div>
                <div class="info-item">
                  <label>Fecha de adquisición:</label>
                  <input type="date" v-model="nuevoEquipo.fechaAdquisicion" />
                </div>
                <div class="info-item">
                  <label>Propietario:</label>
                  <input type="text" v-model="nuevoEquipo.propietario" placeholder="Ej: Universidad de Antioquia" />
                </div>
                <div class="info-item">
                  <label>Fecha de fabricación:</label>
                  <input type="text" v-model="nuevoEquipo.fechaFabricacion" placeholder="Ej: 01/2023" />
                </div>
                <div class="info-item">
                  <label>NIT:</label>
                  <input type="text" v-model="nuevoEquipo.nit" placeholder="Ej: 890980040-8" />
                </div>
                <div class="info-item full-width">
                  <label>Proveedor:</label>
                  <input type="text" v-model="nuevoEquipo.proveedorEquipo" placeholder="Ej: Siemens Healthineers Colombia S.A.S." />
                </div>
                <div class="info-item">
                  <label>¿En garantía?:</label>
                  <select v-model="nuevoEquipo.enGarantia">
                    <option value="">Seleccionar</option>
                    <option value="Sí">Sí</option>
                    <option value="No">No</option>
                  </select>
                </div>
                <div class="info-item">
                  <label>Fin de garantía:</label>
                  <input type="date" v-model="nuevoEquipo.fechaFinGarantia" />
                </div>
                <div class="info-item">
                  <label>Forma de adquisición:</label>
                  <input type="text" v-model="nuevoEquipo.formaAdquisicion" placeholder="Ej: Compra directa" />
                </div>
                <div class="info-item">
                  <label>Tipo de documento:</label>
                  <input type="text" v-model="nuevoEquipo.tipoDocumento" placeholder="Ej: Factura" />
                </div>
                <div class="info-item">
                  <label>Número de documento:</label>
                  <input type="text" v-model="nuevoEquipo.numeroDocumento" placeholder="Ej: FV-2023-001234" />
                </div>
              </div>
            </div>

            <!-- 3. INVENTARIO DE DOCUMENTOS -->
            <div class="info-section">
              <h3 class="section-title">📄 Inventario de Documentos</h3>
              <div class="info-grid">
                <div class="info-item">
                  <label>Hoja de vida:</label>
                  <select v-model="nuevoEquipo.hojaVida">
                    <option value="">Seleccionar</option>
                    <option value="Sí - Disponible">Sí - Disponible</option>
                    <option value="No disponible">No disponible</option>
                  </select>
                </div>
                <div class="info-item">
                  <label>Registro de importación:</label>
                  <input type="text" v-model="nuevoEquipo.registroImportacion" placeholder="Ej: RI-2023-0456" />
                </div>
                <div class="info-item">
                  <label>Manual de operación:</label>
                  <select v-model="nuevoEquipo.manualOperacion">
                    <option value="">Seleccionar</option>
                    <option value="Sí - Español">Sí - Español</option>
                    <option value="Sí - Inglés">Sí - Inglés</option>
                    <option value="No disponible">No disponible</option>
                  </select>
                </div>
                <div class="info-item">
                  <label>Manual de servicio:</label>
                  <select v-model="nuevoEquipo.manualServicio">
                    <option value="">Seleccionar</option>
                    <option value="Sí - Español">Sí - Español</option>
                    <option value="Sí - Inglés">Sí - Inglés</option>
                    <option value="No disponible">No disponible</option>
                  </select>
                </div>
                <div class="info-item">
                  <label>Guía rápida:</label>
                  <select v-model="nuevoEquipo.guiaRapida">
                    <option value="">Seleccionar</option>
                    <option value="Sí - Disponible">Sí - Disponible</option>
                    <option value="No disponible">No disponible</option>
                  </select>
                </div>
                <div class="info-item">
                  <label>Instructivo de manejo:</label>
                  <select v-model="nuevoEquipo.instructivoManejo">
                    <option value="">Seleccionar</option>
                    <option value="Sí - Disponible">Sí - Disponible</option>
                    <option value="No disponible">No disponible</option>
                  </select>
                </div>
                <div class="info-item">
                  <label>Protocolo Mto. Preventivo:</label>
                  <input type="text" v-model="nuevoEquipo.protocoloMtoPrev" placeholder="Ej: Cada 6 meses" />
                </div>
                <div class="info-item">
                  <label>Frecuencia metrológica:</label>
                  <input type="text" v-model="nuevoEquipo.frecuenciaMetrologica" placeholder="Ej: Anual" />
                </div>
              </div>
            </div>

            <!-- 4. INFORMACIÓN METROLÓGICA ADMINISTRATIVA -->
            <div class="info-section">
              <h3 class="section-title">🔧 Información Metrológica Administrativa</h3>
              <div class="info-grid">
                <div class="info-item">
                  <label>Requiere mantenimiento:</label>
                  <select v-model="nuevoEquipo.requiereMantenimiento">
                    <option value="">Seleccionar</option>
                    <option value="Sí">Sí</option>
                    <option value="No">No</option>
                  </select>
                </div>
                <div class="info-item">
                  <label>Frecuencia mantenimiento:</label>
                  <input type="text" v-model="nuevoEquipo.frecuenciaMantenimiento" placeholder="Ej: 2 veces al año" />
                </div>
                <div class="info-item">
                  <label>Requiere calibración:</label>
                  <select v-model="nuevoEquipo.requiereCalibracion">
                    <option value="">Seleccionar</option>
                    <option value="Sí">Sí</option>
                    <option value="No">No</option>
                  </select>
                </div>
                <div class="info-item">
                  <label>Frecuencia calibración:</label>
                  <input type="text" v-model="nuevoEquipo.frecuenciaCalibracion" placeholder="Ej: 1 vez al año" />
                </div>
              </div>
            </div>

            <!-- 5. INFORMACIÓN METROLÓGICA TÉCNICA -->
            <div class="info-section">
              <h3 class="section-title">📐 Información Metrológica Técnica</h3>
              <div class="info-grid">
                <div class="info-item full-width">
                  <label>Magnitud:</label>
                  <input type="text" v-model="nuevoEquipo.magnitud" placeholder="Ej: Radiación ionizante (kV, mAs)" />
                </div>
                <div class="info-item full-width">
                  <label>Rango del equipo:</label>
                  <input type="text" v-model="nuevoEquipo.rangoEquipo" placeholder="Ej: 40-150 kV, 1-500 mAs" />
                </div>
                <div class="info-item">
                  <label>Resolución:</label>
                  <input type="text" v-model="nuevoEquipo.resolucion" placeholder="Ej: 0.1 kV, 0.1 mAs" />
                </div>
                <div class="info-item">
                  <label>Rango de trabajo:</label>
                  <input type="text" v-model="nuevoEquipo.rangoTrabajo" placeholder="Ej: 50-125 kV, 5-320 mAs" />
                </div>
                <div class="info-item full-width">
                  <label>Error máximo permitido:</label>
                  <input type="text" v-model="nuevoEquipo.errorMaximoPermitido" placeholder="Ej: ±5% en kV, ±10% en mAs" />
                </div>
              </div>
            </div>

            <!-- 6. CONDICIONES DE FUNCIONAMIENTO -->
            <div class="info-section">
              <h3 class="section-title">⚡ Condiciones de Funcionamiento</h3>
              <div class="info-grid">
                <div class="info-item">
                  <label>Voltaje:</label>
                  <input type="text" v-model="nuevoEquipo.voltaje" placeholder="Ej: 220V AC ± 10%" />
                </div>
                <div class="info-item">
                  <label>Corriente:</label>
                  <input type="text" v-model="nuevoEquipo.corriente" placeholder="Ej: 50/60 Hz, 32A máx." />
                </div>
                <div class="info-item">
                  <label>Humedad relativa:</label>
                  <input type="text" v-model="nuevoEquipo.humedadRelativa" placeholder="Ej: 30% - 75% sin condensación" />
                </div>
                <div class="info-item">
                  <label>Temperatura:</label>
                  <input type="text" v-model="nuevoEquipo.temperatura" placeholder="Ej: 15°C - 30°C" />
                </div>
                <div class="info-item">
                  <label>Dimensiones:</label>
                  <input type="text" v-model="nuevoEquipo.dimensiones" placeholder="Ej: 210 x 180 x 150 cm" />
                </div>
                <div class="info-item">
                  <label>Peso:</label>
                  <input type="text" v-model="nuevoEquipo.peso" placeholder="Ej: 650 kg" />
                </div>
                <div class="info-item full-width">
                  <label>Otros:</label>
                  <textarea v-model="nuevoEquipo.otros" placeholder="Información adicional sobre condiciones de funcionamiento" rows="3"></textarea>
                </div>
              </div>
            </div>

          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useRouter, useRoute } from 'vue-router';
import { ref } from 'vue';

export default {
  setup() {
    const router = useRouter();
    const route = useRoute();
    
    const fileInput = ref(null);

    // Objeto para el nuevo equipo
    const nuevoEquipo = ref({
      // Información General
      proceso: '',
      nombreEquipo: '',
      codigoInventario: '',
      codigoIPS: '',
      codigoECRI: '',
      responsable: '',
      ubicacionFisica: '',
      marca: '',
      modelo: '',
      serie: '',
      clasificacionMisional: '',
      clasificacionIPS: '',
      clasificacionRiesgo: '',
      registroInvima: '',

      // Registro Histórico
      vidaUtil: '',
      fechaAdquisicion: '',
      propietario: '',
      fechaFabricacion: '',
      nit: '',
      proveedorEquipo: '',
      enGarantia: '',
      fechaFinGarantia: '',
      formaAdquisicion: '',
      tipoDocumento: '',
      numeroDocumento: '',

      // Inventario de Documentos
      hojaVida: '',
      registroImportacion: '',
      manualOperacion: '',
      manualServicio: '',
      guiaRapida: '',
      instructivoManejo: '',
      protocoloMtoPrev: '',
      frecuenciaMetrologica: '',

      // Información Metrológica Administrativa
      requiereMantenimiento: '',
      frecuenciaMantenimiento: '',
      requiereCalibracion: '',
      frecuenciaCalibracion: '',

      // Información Metrológica Técnica
      magnitud: '',
      rangoEquipo: '',
      resolucion: '',
      rangoTrabajo: '',
      errorMaximoPermitido: '',

      // Condiciones de Funcionamiento
      voltaje: '',
      corriente: '',
      humedadRelativa: '',
      temperatura: '',
      dimensiones: '',
      peso: '',
      otros: ''
    });

    const handleImageUpload = (event) => {
      const file = event.target.files[0];
      if (file) {
        // Aquí puedes manejar la imagen
        console.log('Imagen seleccionada:', file.name);
        // En producción, subirías la imagen a un servidor
      }
    };

    const guardarEquipo = () => {
      // Validar campos obligatorios
      if (!nuevoEquipo.value.nombreEquipo || !nuevoEquipo.value.codigoInventario || 
          !nuevoEquipo.value.marca || !nuevoEquipo.value.responsable) {
        alert('Por favor, complete los campos obligatorios (*)');
        return;
      }

      // Aquí iría la lógica para guardar en la base de datos
      console.log('Guardando equipo:', nuevoEquipo.value);
      
      // Simulación de guardado exitoso
      alert('¡Equipo guardado exitosamente!');
      
      // Redirigir a la lista de equipos
      router.push({ 
        name: 'equipos',
        query: {
          sede: route.query.sede,
          categoria: route.query.categoria
        }
      });
    };

    const cancelar = () => {
      if (confirm('¿Está seguro de cancelar? Se perderán los datos no guardados.')) {
        router.push({ 
          name: 'equipos',
          query: {
            sede: route.query.sede,
            categoria: route.query.categoria
          }
        });
      }
    };

    const volverDashboard = () => {
      if (confirm('¿Está seguro de cancelar? Se perderán los datos no guardados.')) {
        router.push({ name: 'home' });
      }
    };

    return {
      nuevoEquipo,
      fileInput,
      handleImageUpload,
      guardarEquipo,
      cancelar,
      volverDashboard
    };
  }
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

.btn-home:hover {
  transform: scale(1.1);
  background: #e74c3c;
  box-shadow: 0 6px 20px rgba(231, 76, 60, 0.4);
}

.btn-home:active {
  transform: scale(0.95);
}

/* CONTENEDOR PRINCIPAL */
.detalles-container {
  display: grid;
  grid-template-columns: 280px 1fr;
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

.foto-placeholder p {
  color: #244652;
  font-size: 48px;
  margin: 0;
}

.foto-placeholder span {
  color: #5a6c7d;
  font-size: 14px;
  font-weight: 600;
  text-align: center;
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

.upload-btn:hover {
  background: #009991;
  transform: translateY(-2px);
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

.action-btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
}

.action-btn:active {
  transform: translateY(-1px);
}

.save-btn {
  background: #6fc232;
  color: white;
  border-color: #6fc232;
}

.save-btn:hover {
  background: #5da829;
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

.info-scrolleable::-webkit-scrollbar {
  width: 8px;
}

.info-scrolleable::-webkit-scrollbar-track {
  background: #f0f0f0;
  border-radius: 6px;
}

.info-scrolleable::-webkit-scrollbar-thumb {
  background: #244652;
  border-radius: 6px;
}

.info-scrolleable::-webkit-scrollbar-thumb:hover {
  background: #212a31;
}

/* SECCIONES DE INFORMACIÓN */
.info-section {
  margin-bottom: 30px;
  padding-bottom: 20px;
  border-bottom: 2px solid #f0f0f0;
}

.info-section:last-child {
  border-bottom: none;
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

.info-item textarea {
  resize: vertical;
  min-height: 60px;
}

.info-item select {
  cursor: pointer;
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