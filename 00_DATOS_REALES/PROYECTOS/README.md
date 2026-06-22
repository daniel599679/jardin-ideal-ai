# PROYECTOS — Proyectos Activos en Obra

## 1. Qué datos deben ir aquí

Estado de todos los proyectos en curso: planificación, ejecución, pausa o finalización pendiente.
Este archivo es la fuente de verdad para operaciones — qué equipo está dónde y qué puede bloquearse.

Incluye:
- Nombre del cliente y dirección del proyecto
- Servicio que se está ejecutando
- Etapa actual y días transcurridos vs. estimados
- Equipo asignado
- Bloqueos activos (materiales, clima, cliente, permisos)
- Próxima acción y responsable

## 2. Formato

**Archivo:** `proyectos_activos.json`  
**Actualizar:** cada mañana o cuando hay cambio de estado  
**Nota:** No crear un archivo por día — este archivo es el estado actual, se sobreescribe

```json
{
  "fecha_actualizacion": "2026-06-22T07:00:00",
  "proyectos": [
    {
      "id": "P2026-047",
      "cliente": "Famille Bouchard",
      "direccion": "1234 Rue des Érables, Laval, QC H7W 2K1",
      "servicio": "pavé-uni",
      "descripcion": "Entrée + allée latérale, 85m²",
      "etapa": "en_curso",
      "equipo": ["Carlos", "Miguel"],
      "jefe_obra": "Carlos",
      "fecha_inicio": "2026-06-20",
      "dias_estimados": 4,
      "dias_transcurridos": 2,
      "fecha_estimada_entrega": "2026-06-23",
      "bloqueo_activo": false,
      "descripcion_bloqueo": null,
      "dias_pausado": 0,
      "fotos_requeridas": "progreso",
      "fotos_tomadas_hoy": false,
      "notas": "Cliente pidió conservar el arbusto del lado derecho"
    },
    {
      "id": "P2026-049",
      "cliente": "Famille Tremblay",
      "direccion": "567 Boul. des Laurentides, Laval, QC H7G 3R1",
      "servicio": "cour arrière",
      "descripcion": "Terrasse + bordures, 120m²",
      "etapa": "planificacion",
      "equipo": [],
      "jefe_obra": null,
      "fecha_inicio": "2026-06-24",
      "dias_estimados": 5,
      "dias_transcurridos": 0,
      "fecha_estimada_entrega": "2026-06-28",
      "bloqueo_activo": false,
      "descripcion_bloqueo": null,
      "dias_pausado": 0,
      "fotos_requeridas": "inicio",
      "fotos_tomadas_hoy": false,
      "notas": "Confirmar materiales antes del 23 junio"
    },
    {
      "id": "P2026-044",
      "cliente": "M. Gauthier",
      "direccion": "890 Ave. Papineau, Montréal, QC H2K 4J8",
      "servicio": "escaliers extérieurs",
      "descripcion": "Remplacement escalier 12 marches, granit gris",
      "etapa": "pausado",
      "equipo": ["Javier"],
      "jefe_obra": "Javier",
      "fecha_inicio": "2026-06-18",
      "dias_estimados": 3,
      "dias_transcurridos": 1,
      "fecha_estimada_entrega": null,
      "bloqueo_activo": true,
      "descripcion_bloqueo": "Granit pedido el 2026-06-18 aún no llega — proveedor Pierre Naturelle",
      "dias_pausado": 2,
      "fotos_requeridas": "progreso",
      "fotos_tomadas_hoy": false,
      "notas": "Cliente informado del retraso el 2026-06-20"
    }
  ],
  "resumen": {
    "total_activos": 3,
    "en_planificacion": 1,
    "en_curso": 1,
    "pausados": 1,
    "en_finalizacion": 0,
    "proyectos_con_bloqueo": 1,
    "proyectos_retrasados": 0,
    "entregas_esta_semana": 1
  }
}
```

## 3. Ejemplo de archivo válido

Un archivo válido tiene:
- ✅ Todos los proyectos activos (no los entregados — esos van a 08_REPORTES)
- ✅ `etapa` uno de: `planificacion`, `en_curso`, `pausado`, `finalizacion`
- ✅ `bloqueo_activo: true` siempre acompañado de `descripcion_bloqueo` con texto
- ✅ `resumen` con conteos correctos

Umbrales que generan alertas en el reporte:
- `bloqueo_activo: true` → siempre aparece en sección de alertas
- `dias_pausado >= 2` → alerta naranja
- `dias_transcurridos > dias_estimados` → proyecto retrasado, alerta naranja
- `fotos_requeridas != null` y `fotos_tomadas_hoy: false` → tarea pendiente

## 4. Cómo será leído por el motor de reportes

El script lee `proyectos_activos.json` directamente (sin fecha en el nombre).

Lee:
- `proyectos[]` → tabla "Proyectos Activos" en sección de Operaciones
- Proyectos con `bloqueo_activo: true` → sección de alertas críticas
- Proyectos con `dias_pausado >= 2` → alerta en prioridades 09:00 AM
- `fotos_tomadas_hoy: false` → tarea en sección de fotografías
- `resumen.entregas_esta_semana` → aparece en resumen ejecutivo

Si el archivo no existe:
```
⚠️ ALERTA — PROYECTOS: archivo no encontrado
   Estado de obra desconocido. Actualizar antes de la reunión de 09:00 AM.
```

**Fuente recomendada:** Actualizar manualmente cada mañana.  
**Futuro:** Integrar con tabla de proyectos en Google Sheets o Airtable.
