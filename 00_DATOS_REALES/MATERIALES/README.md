# MATERIALES — Pedidos Pendientes de Recibir

## 1. Qué datos deben ir aquí

Todos los materiales pedidos que aún no han llegado a obra, organizados por proyecto afectado.
Este archivo previene que un proyecto se detenga por falta de material.

Incluye:
- Materiales pedidos con proveedor y fecha prometida
- Proyecto al que están asignados
- Estado del pedido
- Urgencia (si el proyecto depende de que lleguen hoy)

Categorías frecuentes:
- Pavé-uni (blocs, bordures, sable polymère)
- Tierra vegetal / sustrato
- Piedra natural (granit, calcaire)
- Materiales para piscinas
- Herramientas y consumibles de obra

## 2. Formato

**Archivo:** `materiales_pendientes.json`  
**Actualizar:** cuando se hace un pedido nuevo o cuando llega un material

```json
{
  "fecha_actualizacion": "2026-06-22T07:00:00",
  "pedidos": [
    {
      "id": "M001",
      "material": "Granit gris — dalles 12x12",
      "descripcion": "60 piezas para escalier P2026-044",
      "cantidad": "60 dalles",
      "proveedor": "Pierre Naturelle Inc.",
      "telefono_proveedor": "450-555-0400",
      "proyecto_afectado": "P2026-044",
      "cliente_proyecto": "M. Gauthier",
      "fecha_pedido": "2026-06-18",
      "fecha_prometida": "2026-06-20",
      "dias_retraso": 2,
      "estado": "retrasado",
      "urgente": true,
      "bloquea_obra": true,
      "notas": "Llamar antes de las 08:30 para confirmar entrega hoy"
    },
    {
      "id": "M002",
      "material": "Sable polymère gris — sacos 20kg",
      "descripcion": "Para juntas de pavé-uni P2026-047",
      "cantidad": "40 sacos",
      "proveedor": "Paysagiste Pro Supply",
      "telefono_proveedor": "514-555-0500",
      "proyecto_afectado": "P2026-047",
      "cliente_proyecto": "Famille Bouchard",
      "fecha_pedido": "2026-06-19",
      "fecha_prometida": "2026-06-22",
      "dias_retraso": 0,
      "estado": "en_transito",
      "urgente": true,
      "bloquea_obra": false,
      "notas": "Se necesita para la etapa de relleno — estimado llegada 14:00"
    },
    {
      "id": "M003",
      "material": "Bordures de béton blanc — 6m",
      "descripcion": "Para delimitación cour arrière P2026-049",
      "cantidad": "24 piezas",
      "proveedor": "Matériaux Richelieu",
      "telefono_proveedor": "450-555-0600",
      "proyecto_afectado": "P2026-049",
      "cliente_proyecto": "Famille Tremblay",
      "fecha_pedido": "2026-06-21",
      "fecha_prometida": "2026-06-23",
      "dias_retraso": 0,
      "estado": "confirmado",
      "urgente": false,
      "bloquea_obra": false,
      "notas": "Proyecto empieza el 24 — no urgente"
    }
  ],
  "resumen": {
    "total_pedidos_activos": 3,
    "retrasados": 1,
    "en_transito": 1,
    "confirmados": 1,
    "bloquean_obra_activamente": 1,
    "urgentes_hoy": 2
  }
}
```

## 3. Ejemplo de archivo válido

Un archivo válido tiene:
- ✅ `estado` uno de: `pendiente`, `confirmado`, `en_transito`, `retrasado`, `recibido`
- ✅ `dias_retraso` calculado correctamente (0 si está en plazo)
- ✅ `bloquea_obra: true` solo si el proyecto está detenido por este material
- ✅ Materiales recibidos **no deben estar** en este archivo (eliminarlos al recibirlos)

Umbrales que generan alertas en el reporte:
- `dias_retraso >= 1` y `bloquea_obra: true` → alerta roja en prioridades
- `dias_retraso >= 1` y `urgente: true` → alerta naranja
- `dias_retraso >= 3` → alerta roja independientemente del impacto

## 4. Cómo será leído por el motor de reportes

El script lee `materiales_pendientes.json` directamente.

Lee:
- Pedidos con `bloquea_obra: true` → alerta crítica en prioridades 09:00 AM con acción inmediata
- Pedidos con `dias_retraso >= 1` → sección "Materiales con alerta" en Operaciones
- Pedidos con `estado: "en_transito"` y entrega hoy → confirmación en agenda del día
- `resumen.bloquean_obra_activamente` → si >0, aparece en resumen ejecutivo

Si el archivo no existe:
```
ℹ️ MATERIALES: archivo no encontrado — se asume sin pedidos pendientes
   Verificar si hay materiales esperados en obra.
```

**Fuente recomendada:** Actualizar manualmente al hacer cada pedido.  
**Futuro:** Integrar con tabla de pedidos en Google Sheets con notificación automática al vencer la fecha prometida.
