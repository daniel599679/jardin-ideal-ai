# FOTOS_VIDEOS — Documentación Visual de Proyectos

## 1. Qué datos deben ir aquí

Registro de fotografías y videos recibidos del equipo en campo, y estado de su procesamiento.
Las fotos de cierre son activo de marketing y documentación de garantía — este archivo garantiza que ninguna se pierda.

Incluye:
- Fotos/videos recibidos hoy (por proyecto y tipo)
- Estado: recibidas → subidas a Drive → aprobadas para marketing
- Proyectos que DEBEN tener fotos hoy y aún no las tienen

Tipos de registro:
- `inicio` — foto del espacio antes de comenzar
- `progreso` — 1-2 fotos por día en proyectos de +3 días
- `cierre` — mínimo 5 fotos finales, luz natural

## 2. Formato

**Archivo:** `fotos_videos_YYYY-MM-DD.json`  
**Actualizar:** cada tarde cuando el equipo envía las fotos del día

```json
{
  "fecha": "2026-06-22",
  "recibidos": [
    {
      "proyecto_id": "P2026-047",
      "cliente": "Famille Bouchard",
      "tipo": "progreso",
      "cantidad_fotos": 3,
      "cantidad_videos": 0,
      "canal_recepcion": "WhatsApp",
      "hora_recepcion": "16:45",
      "subidas_a_drive": false,
      "carpeta_drive": "Proyectos/P2026-047-Bouchard/",
      "aprobadas_marketing": false,
      "calidad": "buena",
      "notas": "Buena luz, ángulo calle bien cubierto"
    },
    {
      "proyecto_id": "P2026-044",
      "cliente": "M. Gauthier",
      "tipo": "progreso",
      "cantidad_fotos": 1,
      "cantidad_videos": 0,
      "canal_recepcion": "WhatsApp",
      "hora_recepcion": "12:30",
      "subidas_a_drive": true,
      "carpeta_drive": "Proyectos/P2026-044-Gauthier/",
      "aprobadas_marketing": false,
      "calidad": "regular",
      "notas": "Solo 1 foto — obra pausada por falta de material"
    }
  ],
  "pendientes": [
    {
      "proyecto_id": "P2026-047",
      "cliente": "Famille Bouchard",
      "tipo_requerido": "progreso",
      "razon": "Día 2 de 4 — progreso diario requerido",
      "urgencia": "normal"
    },
    {
      "proyecto_id": "P2026-049",
      "cliente": "Famille Tremblay",
      "tipo_requerido": "inicio",
      "razon": "Proyecto inicia el 24 — foto antes/inicio requerida",
      "urgencia": "baja"
    }
  ],
  "resumen": {
    "fotos_recibidas_hoy": 4,
    "videos_recibidos_hoy": 0,
    "proyectos_con_fotos_hoy": 2,
    "fotos_subidas_drive": 1,
    "fotos_pendientes_subir": 3,
    "proyectos_sin_fotos_requeridas": 2,
    "cierres_sin_documentar": 0
  }
}
```

## 3. Ejemplo de archivo válido

Un archivo válido tiene:
- ✅ `tipo` uno de: `inicio`, `progreso`, `cierre`, `otro`
- ✅ `calidad` uno de: `excelente`, `buena`, `regular`, `rechazada`
- ✅ `pendientes[]` lista proyectos que DEBEN tener fotos pero no las tienen aún
- ✅ `resumen.cierres_sin_documentar` siempre debe ser 0 — si >0 es alerta inmediata

Umbrales que generan alertas en el reporte:
- `resumen.cierres_sin_documentar > 0` → alerta naranja (activo de marketing perdido)
- `subidas_a_drive: false` al cierre del día → tarea pendiente de mañana
- Proyecto en `cierre` con menos de 5 fotos → alerta naranja

## 4. Cómo será leído por el motor de reportes

El script busca `fotos_videos_YYYY-MM-DD.json` con la fecha del día.

Lee:
- `pendientes[]` con `tipo_requerido: "cierre"` → alerta en prioridades
- `resumen.cierres_sin_documentar > 0` → alerta naranja en Operaciones
- `fotos_pendientes_subir > 0` → tarea en cierre del día
- `aprobadas_marketing: true` → notifica al Agente Marketing que hay contenido disponible

Si el archivo no existe:
```
ℹ️ FOTOS/VIDEOS: sin registro para hoy
   Verificar si el equipo envió fotos. Si hay proyectos en curso, solicitar.
```

**Fuente recomendada:** El equipo envía fotos por WhatsApp → Daniel o responsable registra aquí al recibirlas.  
**Futuro:** Google Drive API + Make.com puede detectar archivos nuevos en carpetas de proyecto y actualizar este archivo automáticamente.
