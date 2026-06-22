# TAREAS — Tareas Pendientes por Agente

## 1. Qué datos deben ir aquí

Todas las tareas abiertas organizadas por agente responsable y prioridad.
Este archivo captura lo que debe hacerse hoy que no está cubierto automáticamente por CRM, campañas u operaciones.

Incluye:
- Tareas de seguimiento CRM no automatizadas
- Tareas de marketing (ajustes de campaña, contenido pendiente)
- Tareas de operaciones (coordinación, permisos, proveedores)
- Tareas de automatización pendientes de implementar
- Tareas delegadas al equipo con plazo

## 2. Formato

**Archivo:** `tareas_pendientes.json`  
**Actualizar:** cada mañana — agregar tareas nuevas, marcar completadas del día anterior

```json
{
  "fecha": "2026-06-22",
  "tareas": [
    {
      "id": "T001",
      "agente": "CRM",
      "descripcion": "Llamar a Paul Gagné — propuesta enviada hace 8 días sin respuesta",
      "prioridad": "critica",
      "plazo": "10:00",
      "responsable": "Daniel",
      "estado": "pendiente",
      "lead_relacionado": "L003",
      "notas": "Usar plantilla seguimiento propuesta día 7 — ver 06_CRM/plantillas_mensajes.md"
    },
    {
      "id": "T002",
      "agente": "Marketing",
      "descripcion": "Rotar creatividades campaña Cour Avant/Arrière — frecuencia en 3.6",
      "prioridad": "alta",
      "plazo": "antes_del_mediodia",
      "responsable": "Daniel",
      "estado": "pendiente",
      "lead_relacionado": null,
      "notas": "Parar anuncio actual, subir 2 nuevas variantes de imagen"
    },
    {
      "id": "T003",
      "agente": "Operaciones",
      "descripcion": "Confirmar entrega granit con Pierre Naturelle para proyecto P2026-044",
      "prioridad": "alta",
      "plazo": "08:30",
      "responsable": "Daniel",
      "estado": "pendiente",
      "lead_relacionado": null,
      "notas": "Si no llega hoy — informar al cliente M. Gauthier en francés"
    },
    {
      "id": "T004",
      "agente": "Automatizacion",
      "descripcion": "Implementar Make.com Flujo A — Meta Lead Ads → CRM",
      "prioridad": "alta",
      "plazo": "esta_semana",
      "responsable": "Daniel",
      "estado": "pendiente",
      "lead_relacionado": null,
      "notas": "Ver 07_AUTOMATIZACIONES/automatizacion_leads.md — Flujo A"
    },
    {
      "id": "T005",
      "agente": "Marketing",
      "descripcion": "Publicar avant/après en Instagram y Facebook",
      "prioridad": "media",
      "plazo": "10:00",
      "responsable": "Daniel",
      "estado": "pendiente",
      "lead_relacionado": null,
      "notas": "Usar borrador del reporte de hoy — verificar autorización cliente primero"
    }
  ],
  "resumen": {
    "total_pendientes": 5,
    "criticas": 1,
    "altas": 3,
    "medias": 1,
    "por_agente": {
      "CRM": 1,
      "Marketing": 2,
      "Operaciones": 1,
      "Automatizacion": 1
    }
  }
}
```

## 3. Ejemplo de archivo válido

Un archivo válido tiene:
- ✅ `prioridad` uno de: `critica`, `alta`, `media`, `baja`
- ✅ `estado` uno de: `pendiente`, `en_progreso`, `completada`, `postergada`
- ✅ `agente` uno de: `CRM`, `Marketing`, `Operaciones`, `Automatizacion`, `General`
- ✅ `plazo` con hora (`"09:00"`) o descriptor (`"antes_del_mediodia"`, `"esta_semana"`)
- ✅ `resumen.total_pendientes` cuenta solo las que tienen `estado: "pendiente"`

## 4. Cómo será leído por el motor de reportes

El script lee `tareas_pendientes.json` directamente.

Lee:
- Tareas con `prioridad: "critica"` → sección "Prioridades antes de las 09:00 AM"
- Tareas con `prioridad: "alta"` y `plazo` con hora → sección de prioridades del día
- Tareas agrupadas por `agente` → sección de tareas por área
- `resumen.criticas > 0` → aparece en resumen ejecutivo como dato de atención

Si el archivo no existe:
```
ℹ️ TAREAS: archivo no encontrado — se asume sin tareas manuales pendientes
   Esto puede ser normal si todas las tareas vienen del CRM y campañas.
```

**Fuente recomendada:** Actualizar manualmente cada noche al cerrar el día (parte del checklist de cierre 17:00).
