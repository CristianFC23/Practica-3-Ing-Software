<template>
  <div class="page-container">
    <button @click="volverAtras" class="btn-home">🏠</button>

    <div class="detalles-container">
      <!-- Columna Izquierda: Foto y Botones -->
      <div class="columna-izquierda">
        <div class="foto-container">
          <div class="foto-placeholder">
            <p>📷</p>
            <span>{{ equipoDetalle.nombreEquipo }}</span>
          </div>
        </div>

        <button class="action-btn edit-btn">
          ✏️ Editar Info
        </button>

        <button class="action-btn baja-btn">
          ❌ Dar de baja
        </button>

        <button class="action-btn volver-btn" @click="volverAtras">
          ⬅️ Volver al menú
        </button>
      </div>

      <!-- Columna Derecha: Dashboard Scrolleable -->
      <div class="columna-derecha">
        <div class="dashboard-card">
          <h2 class="dashboard-title">{{ equipoDetalle.nombreEquipo }}</h2>
          <p class="codigo-principal">{{ equipoDetalle.codigoInventario }}</p>
          
          <div class="info-scrolleable">
            
            <!-- 1. INFORMACIÓN GENERAL -->
            <div class="info-section">
              <h3 class="section-title">📋 Información General</h3>
              <div class="info-grid">
                <div class="info-item">
                  <label>Proceso:</label>
                  <p>{{ equipoDetalle.proceso }}</p>
                </div>
                <div class="info-item">
                  <label>Nombre del equipo:</label>
                  <p>{{ equipoDetalle.nombreEquipo }}</p>
                </div>
                <div class="info-item">
                  <label>Código de inventario:</label>
                  <p class="destacado">{{ equipoDetalle.codigoInventario }}</p>
                </div>
                <div class="info-item">
                  <label>Código IPS:</label>
                  <p>{{ equipoDetalle.codigoIPS }}</p>
                </div>
                <div class="info-item">
                  <label>Código ECRI:</label>
                  <p>{{ equipoDetalle.codigoECRI }}</p>
                </div>
                <div class="info-item">
                  <label>Responsable:</label>
                  <p>{{ equipoDetalle.responsable }}</p>
                </div>
                <div class="info-item full-width">
                  <label>Ubicación física:</label>
                  <p>{{ equipoDetalle.ubicacionFisica }}</p>
                </div>
                <div class="info-item">
                  <label>Marca:</label>
                  <p>{{ equipoDetalle.marca }}</p>
                </div>
                <div class="info-item">
                  <label>Modelo:</label>
                  <p>{{ equipoDetalle.modelo }}</p>
                </div>
                <div class="info-item">
                  <label>Serie:</label>
                  <p>{{ equipoDetalle.serie }}</p>
                </div>
                <div class="info-item full-width">
                  <label>Clasificación eje misional:</label>
                  <p>{{ equipoDetalle.clasificacionMisional }}</p>
                </div>
                <div class="info-item">
                  <label>Clasificación IPS:</label>
                  <p>{{ equipoDetalle.clasificacionIPS }}</p>
                </div>
                <div class="info-item">
                  <label>Clasificación por riesgo:</label>
                  <p>{{ equipoDetalle.clasificacionRiesgo }}</p>
                </div>
                <div class="info-item full-width">
                  <label>Registro Invima:</label>
                  <p>{{ equipoDetalle.registroInvima }}</p>
                </div>
              </div>
            </div>

            <!-- 2. REGISTRO HISTÓRICO -->
            <div class="info-section">
              <h3 class="section-title">📅 Registro Histórico</h3>
              <div class="info-grid">
                <div class="info-item">
                  <label>Vida útil:</label>
                  <p>{{ equipoDetalle.vidaUtil }}</p>
                </div>
                <div class="info-item">
                  <label>Fecha de adquisición:</label>
                  <p>{{ equipoDetalle.fechaAdquisicion }}</p>
                </div>
                <div class="info-item">
                  <label>Propietario:</label>
                  <p>{{ equipoDetalle.propietario }}</p>
                </div>
                <div class="info-item">
                  <label>Fecha de fabricación:</label>
                  <p>{{ equipoDetalle.fechaFabricacion }}</p>
                </div>
                <div class="info-item">
                  <label>NIT:</label>
                  <p>{{ equipoDetalle.nit }}</p>
                </div>
                <div class="info-item full-width">
                  <label>Proveedor:</label>
                  <p>{{ equipoDetalle.proveedorEquipo }}</p>
                </div>
                <div class="info-item">
                  <label>¿En garantía?:</label>
                  <p :class="equipoDetalle.enGarantia === 'Sí' ? 'estado-activo' : 'estado-inactivo'">
                    {{ equipoDetalle.enGarantia }}
                  </p>
                </div>
                <div class="info-item">
                  <label>Fin de garantía:</label>
                  <p>{{ equipoDetalle.fechaFinGarantia }}</p>
                </div>
                <div class="info-item">
                  <label>Forma de adquisición:</label>
                  <p>{{ equipoDetalle.formaAdquisicion }}</p>
                </div>
                <div class="info-item">
                  <label>Tipo de documento:</label>
                  <p>{{ equipoDetalle.tipoDocumento }}</p>
                </div>
                <div class="info-item">
                  <label>Número de documento:</label>
                  <p>{{ equipoDetalle.numeroDocumento }}</p>
                </div>
              </div>
            </div>

            <!-- 3. INVENTARIO DE DOCUMENTOS -->
            <div class="info-section">
              <h3 class="section-title">📄 Inventario de Documentos</h3>
              <div class="info-grid">
                <div class="info-item">
                  <label>Hoja de vida:</label>
                  <p>{{ equipoDetalle.hojaVida }}</p>
                </div>
                <div class="info-item">
                  <label>Registro de importación:</label>
                  <p>{{ equipoDetalle.registroImportacion }}</p>
                </div>
                <div class="info-item">
                  <label>Manual de operación:</label>
                  <p>{{ equipoDetalle.manualOperacion }}</p>
                </div>
                <div class="info-item">
                  <label>Manual de servicio:</label>
                  <p>{{ equipoDetalle.manualServicio }}</p>
                </div>
                <div class="info-item">
                  <label>Guía rápida:</label>
                  <p>{{ equipoDetalle.guiaRapida }}</p>
                </div>
                <div class="info-item">
                  <label>Instructivo de manejo:</label>
                  <p>{{ equipoDetalle.instructivoManejo }}</p>
                </div>
                <div class="info-item">
                  <label>Protocolo Mto. Preventivo:</label>
                  <p>{{ equipoDetalle.protocoloMtoPrev }}</p>
                </div>
                <div class="info-item">
                  <label>Frecuencia metrológica:</label>
                  <p>{{ equipoDetalle.frecuenciaMetrologica }}</p>
                </div>
              </div>
            </div>

            <!-- 4. INFORMACIÓN METROLÓGICA ADMINISTRATIVA -->
            <div class="info-section">
              <h3 class="section-title">🔧 Información Metrológica Administrativa</h3>
              <div class="info-grid">
                <div class="info-item">
                  <label>Requiere mantenimiento:</label>
                  <p :class="equipoDetalle.requiereMantenimiento === 'Sí' ? 'estado-activo' : 'estado-inactivo'">
                    {{ equipoDetalle.requiereMantenimiento }}
                  </p>
                </div>
                <div class="info-item">
                  <label>Frecuencia mantenimiento:</label>
                  <p>{{ equipoDetalle.frecuenciaMantenimiento }}</p>
                </div>
                <div class="info-item">
                  <label>Requiere calibración:</label>
                  <p :class="equipoDetalle.requiereCalibracion === 'Sí' ? 'estado-activo' : 'estado-inactivo'">
                    {{ equipoDetalle.requiereCalibracion }}
                  </p>
                </div>
                <div class="info-item">
                  <label>Frecuencia calibración:</label>
                  <p>{{ equipoDetalle.frecuenciaCalibracion }}</p>
                </div>
              </div>
            </div>

            <!-- 5. INFORMACIÓN METROLÓGICA TÉCNICA -->
            <div class="info-section">
              <h3 class="section-title">📐 Información Metrológica Técnica</h3>
              <div class="info-grid">
                <div class="info-item full-width">
                  <label>Magnitud:</label>
                  <p>{{ equipoDetalle.magnitud }}</p>
                </div>
                <div class="info-item full-width">
                  <label>Rango del equipo:</label>
                  <p>{{ equipoDetalle.rangoEquipo }}</p>
                </div>
                <div class="info-item">
                  <label>Resolución:</label>
                  <p>{{ equipoDetalle.resolucion }}</p>
                </div>
                <div class="info-item">
                  <label>Rango de trabajo:</label>
                  <p>{{ equipoDetalle.rangoTrabajo }}</p>
                </div>
                <div class="info-item full-width">
                  <label>Error máximo permitido:</label>
                  <p>{{ equipoDetalle.errorMaximoPermitido }}</p>
                </div>
              </div>
            </div>

            <!-- 6. CONDICIONES DE FUNCIONAMIENTO -->
            <div class="info-section">
              <h3 class="section-title">⚡ Condiciones de Funcionamiento</h3>
              <div class="info-grid">
                <div class="info-item">
                  <label>Voltaje:</label>
                  <p>{{ equipoDetalle.voltaje }}</p>
                </div>
                <div class="info-item">
                  <label>Corriente:</label>
                  <p>{{ equipoDetalle.corriente }}</p>
                </div>
                <div class="info-item">
                  <label>Humedad relativa:</label>
                  <p>{{ equipoDetalle.humedadRelativa }}</p>
                </div>
                <div class="info-item">
                  <label>Temperatura:</label>
                  <p>{{ equipoDetalle.temperatura }}</p>
                </div>
                <div class="info-item">
                  <label>Dimensiones:</label>
                  <p>{{ equipoDetalle.dimensiones }}</p>
                </div>
                <div class="info-item">
                  <label>Peso:</label>
                  <p>{{ equipoDetalle.peso }}</p>
                </div>
                <div class="info-item full-width">
                  <label>Otros:</label>
                  <p>{{ equipoDetalle.otros }}</p>
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
    
    const equipoId = ref(route.params.id || null);

    // Datos del equipo - En producción, estos vendrían de una API
    const equipoDetalle = ref({
      // Información General
      proceso: 'Diagnóstico por Imágenes',
      nombreEquipo: 'Rayos X Digital',
      codigoInventario: 'RX-001-LIME-2023',
      codigoIPS: 'IPS-RX-2023-045',
      codigoECRI: '16-725',
      responsable: 'Dr. Carlos Martínez Pérez',
      ubicacionFisica: 'Sala de Radiología 1 - Piso 2',
      marca: 'Siemens',
      modelo: 'Luminos Agile Max',
      serie: 'SN-2023-RX-8947',
      clasificacionMisional: 'Docencia, Investigación, Extensión',
      clasificacionIPS: 'IND',
      clasificacionRiesgo: 'Clase IIB - Riesgo Alto',
      registroInvima: '2023DM-0012345',

      // Registro Histórico
      vidaUtil: '10 años',
      fechaAdquisicion: '15/03/2023',
      propietario: 'Universidad de Antioquia',
      fechaFabricacion: '01/2023',
      nit: '890980040-8',
      proveedorEquipo: 'Siemens Healthineers Colombia S.A.S.',
      enGarantia: 'Sí',
      fechaFinGarantia: '15/03/2026',
      formaAdquisicion: 'Compra directa',
      tipoDocumento: 'Factura',
      numeroDocumento: 'FV-2023-001234',

      // Inventario de Documentos
      hojaVida: 'Sí - Disponible',
      registroImportacion: 'Sí - RI-2023-0456',
      manualOperacion: 'Sí - Español',
      manualServicio: 'Sí - Español',
      guiaRapida: 'Sí - Disponible',
      instructivoManejo: 'Sí - Disponible',
      protocoloMtoPrev: 'Sí - Cada 6 meses',
      frecuenciaMetrologica: 'Anual',

      // Información Metrológica Administrativa
      requiereMantenimiento: 'Sí',
      frecuenciaMantenimiento: '2 veces al año',
      requiereCalibracion: 'Sí',
      frecuenciaCalibracion: '1 vez al año',

      // Información Metrológica Técnica
      magnitud: 'Radiación ionizante (kV, mAs)',
      rangoEquipo: '40-150 kV, 1-500 mAs',
      resolucion: '0.1 kV, 0.1 mAs',
      rangoTrabajo: '50-125 kV, 5-320 mAs',
      errorMaximoPermitido: '±5% en kV, ±10% en mAs',

      // Condiciones de Funcionamiento
      voltaje: '220V AC ± 10%',
      corriente: '50/60 Hz, 32A máx.',
      humedadRelativa: '30% - 75% sin condensación',
      temperatura: '15°C - 30°C',
      dimensiones: '210 cm (alto) x 180 cm (ancho) x 150 cm (profundo)',
      peso: '650 kg',
      otros: 'Requiere sistema de tierra dedicado, protección diferencial 30mA, conexión de red LAN para PACS'
    });

    const volverAtras = () => {
      // Volver a la vista de equipos con los parámetros de sede y categoría
      router.push({ 
        name: 'equipos',
        query: {
          sede: route.query.sede,
          categoria: route.query.categoria
        }
      });
    };

    return {
      equipoId,
      equipoDetalle,
      volverAtras
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
  padding: 0 10px;
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

.edit-btn:hover {
  background: #00bab3;
  color: white;
  border-color: #00bab3;
}

.baja-btn:hover {
  background: #e74c3c;
  color: white;
  border-color: #e74c3c;
}

.volver-btn:hover {
  background: #244652;
  color: white;
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

.codigo-principal {
  font-size: 14px;
  color: #00bab3;
  font-weight: 600;
  margin: 5px 0 20px 0;
  padding: 8px 12px;
  background: #f0fffe;
  border-radius: 8px;
  display: inline-block;
  border-left: 3px solid #00bab3;
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

.info-item p {
  font-size: 14px;
  color: #212a31;
  margin: 0;
  padding: 8px 12px;
  background: #f8f9fa;
  border-radius: 8px;
  border-left: 3px solid #e0e0e0;
}

.info-item p.destacado {
  background: #fff9e6;
  border-left-color: #ffc107;
  font-weight: 600;
  color: #856404;
}

.info-item p.estado-activo {
  background: #e8f5e9;
  border-left-color: #81d742;
  color: #2e7d32;
  font-weight: 600;
}

.info-item p.estado-inactivo {
  background: #ffebee;
  border-left-color: #e74c3c;
  color: #c62828;
  font-weight: 600;
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