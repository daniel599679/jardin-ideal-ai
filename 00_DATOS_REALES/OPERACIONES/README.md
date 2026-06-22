# OPERACIONES — Visitas, Equipo y Agenda del Día

## 1. Qué datos deben ir aquí

Coordinación operativa del día: visitas técnicas programadas, ubicación de equipos en campo y estado de la reunión de 09:00 AM.
Este archivo es lo que el Agente Operaciones necesita para preparar la agenda antes de la reunión.

Incluye:
- Visitas técnicas programadas (hora, cliente, propósito)
- Confirmación del cliente para cada visita
- Ubicación de cada equipo durante el día
- Estado de la reunión de 09:00 AM
- Pendientes del día anterior no resueltos

## 2. Formato

**Archivo:** `operaciones_hoy.json`  
**Actualizar:** la noche anterior o a las 07:00 AM como primera tarea

```json
{
  "fecha": "2026-06-22",
  "visitas_tecnicas": [
    {
      "id": "V001",
      "hora": "10:00",
      "cliente": "Famille Martin",
      "telefono": "514-555-0700",
      "direccion": "234 Rue Jarry E, Montréal-Nord, QC H2R 1W5",
      "proposito": "visita_tecnica",
      "servicio_interes": "cour arrière + terrasse",
      "responsable": "Daniel",
      "confirmado_cliente": true,
      "hora_confirmacion": "2026-06-21T17:30:00",
      "tiempo_desplazamiento_min": 25,
      "materiales_necesarios": ["muestras pavé-uni", "tabla de precios"],
      "notas": "Cliente vio nuestro Instagram — pedir autorización para fotos si acepta"
    },
    {
      "id": "V002",
      "hora": "14:30",
      "cliente": "M. Leblanc",
      "telefono": "450-555-0800",
      "direccion": "890 Rue des Pins, Laval, QC H7L 3A2",
      "proposito": "entrega_proyecto",
      "servicio_interes": null,
      "responsable": "Carlos",
      "confirmado_cliente": false,
      "hora_confirmacion": null,
      "tiempo_desplazamiento_min": 20,
      "materiales_necesarios": ["factura", "garantía firmada"],
      "notas": "⚠️ Sin confirmar — llamar antes de las 12:00"
    }
  ],
  "equipos_en_campo": [
    {
      "nombre": "Equipo 1",
      "integrantes": ["Carlos", "Miguel"],
      "proyecto_asignado": "P2026-047",
      "cliente": "Famille Bouchard",
      "direccion": "1234 Rue des Érables, Laval",
      "hora_salida_estimada": "07:00",
      "hora_regreso_estimada": "17:00",
      "tareas_del_dia": "Día 3 de 4 — instalar segunda sección de pavé, avanzar bordures"
    }
  ],
  "reunion_0900": {
    "confirmada": true,
    "modalidad": "presencial",
    "agenda_lista": false,
    "puntos_urgentes": [
      "Material granit P2026-044 — ¿llegó?",
      "Lead Paul Gagné — propuesta 8 días sin respuesta"
    ]
  },
  "pendientes_dia_anterior": [
    {
      "descripcion": "Subir fotos proyecto Bouchard a Google Drive",
      "responsable": "Daniel",
      "completado": false
    }
  ]
}
```

## 3. Ejemplo de archivo válido

Un archivo válido tiene:
- ✅ `proposito` uno de: `visita_tecnica`, `entrega_proyecto`, `seguimiento_obra`, `reunion_cliente`
- ✅ `confirmado_cliente: false` con nota de acción en `notas`
- ✅ `reunion_0900.agenda_lista: false` es válido — el motor lo incluye como tarea
- ✅ `pendientes_dia_anterior[]` puede estar vacío `[]` — es normal

Umbrales que generan alertas en el reporte:
- `confirmado_cliente: false` → tarea urgente en prioridades: "Confirmar visita antes de las X"
- `reunion_0900.agenda_lista: false` → tarea en prioridades 08:30
- `pendientes_dia_anterior[]` no vacío → aparece en agenda reunión como "Pendientes de ayer"

## 4. Cómo será leído por el motor de reportes

El script lee `operaciones_hoy.json` directamente.

Lee:
- `visitas_tecnicas[]` → tabla "Visitas del Día" con columna de confirmación
- Visitas con `confirmado_cliente: false` → alerta en prioridades
- `equipos_en_campo[]` → sección "Coordinación de Equipos"
- `reunion_0900.puntos_urgentes[]` → se incluyen en la agenda generada
- `pendientes_dia_anterior[]` → bloque "Pendientes de Ayer" en agenda 09:00

Si el archivo no existe:
```
ℹ️ OPERACIONES: archivo no encontrado
   No hay visitas ni coordinación de equipos registrada para hoy.
   Crear antes de la reunión de 09:00 AM.
```

**Fuente recomendada:** Actualizar la noche anterior como parte del checklist de cierre (17:55).  
Revisar el calendario y confirmar con el equipo por WhatsApp.
