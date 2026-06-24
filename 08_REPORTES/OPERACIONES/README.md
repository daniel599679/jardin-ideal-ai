# 08_REPORTES / OPERACIONES
**Responsable:** Daniel (decisiones) + equipo de campo
**Frecuencia:** Actualización diaria — registro de proyectos en curso

---

## QUÉ SE ALMACENA AQUÍ

Todo lo relacionado con la ejecución de proyectos en campo: proyectos activos, agenda de trabajos, seguimiento de equipos, materiales, y calidad de entrega.

### Archivos esperados

| Tipo | Nombre de archivo | Frecuencia |
|------|------------------|-----------|
| Estado de proyectos activos | `operaciones_proyectos_YYYY-MM-DD.md` | Diario (días con proyectos) |
| Agenda semanal de trabajos | `operaciones_agenda_YYYY-WNN.md` | Semanal (viernes para semana siguiente) |
| Reporte de proyecto completado | `proyecto_[CLIENTE]_[FECHA].md` | Al cerrar cada proyecto |
| Incidencias en campo | `incidencia_[FECHA]_[TIPO].md` | Cuando ocurra |

### Campos mínimos — Estado proyectos activos

```
OPERACIONES — YYYY-MM-DD

PROYECTOS EN EJECUCIÓN HOY: ___
  [Cliente] — [Servicio] — Día ___ de ___ — Estado: En curso / Pausa / Completado
  [Cliente] — [Servicio] — Día ___ de ___ — Estado: ___

PROYECTOS QUE INICIAN ESTA SEMANA:
  [Fecha inicio] — [Cliente] — [Dirección] — [Servicio]

PROYECTOS QUE TERMINAN ESTA SEMANA:
  [Fecha fin] — [Cliente] — Pendiente: [fotos / soumission final / cobro]

DISPONIBILIDAD EQUIPO:
  Equipo A: ___________________________________
  Equipo B: ___________________________________ (si aplica)

MATERIALES PENDIENTES:
  [ ] _______________
  [ ] _______________
```

---

## FRECUENCIA DE ACTUALIZACIÓN

| Acción | Cuándo |
|--------|--------|
| Estado de proyectos | Cada mañana (input del START_DAY_ENGINE) |
| Agenda semanal | Viernes 16:00h — planificar semana siguiente |
| Proyecto completado | Al día de terminación — incluir fotos tomadas |
| Incidencia | Inmediato — registrar para análisis de calidad |

---

## RESPONSABLE

- **Coordinación:** Daniel — agenda y decisiones
- **Ejecución:** Equipo de campo — reportar novedades por WhatsApp
- **Control de calidad:** Francisco (selección de fotos) → `05_MARKETING/00_BIBLIOTECA_VISUAL/`
- **Conexión ventas:** Proyecto completado → solicitar reseña Google/Facebook al cliente

---

## PROCESO AL COMPLETAR UN PROYECTO

```
1. Equipo de campo notifica "terminado" por WhatsApp
2. Daniel actualiza etapa en Pipedrive → "Ganado / Completado"
3. Fotografías tomadas en campo → enviadas a Francisco para selección
4. Francisco aprueba fotos → van a 05_MARKETING/00_BIBLIOTECA_VISUAL/
5. Daniel solicita reseña al cliente (template en 06_CRM/)
6. Crear archivo proyecto_[CLIENTE]_[FECHA].md aquí con resumen
7. Registrar ingreso en CEO Dashboard semanal
```

---

## CONEXIÓN CON OTROS SISTEMAS

- **Fuente:** WhatsApp equipo + visitas de supervisión de Daniel
- **Alimenta:** `CRM/` — actualizar etapa del deal en Pipedrive
- **Alimenta:** `RESUMENES_DIARIOS/` — sección proyectos del reporte diario
- **Alimenta:** `05_MARKETING/` — fotos del proyecto completado → nueva campaña
- **Alimenta:** `DASHBOARDS/` — proyectos completados = ingresos realizados
