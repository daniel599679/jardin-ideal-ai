# 08_REPORTES / RESUMENES_DIARIOS
**Responsable:** Daniel
**Frecuencia:** Un archivo por día hábil + un archivo por semana + un archivo por mes

---

## QUÉ SE ALMACENA AQUÍ

Los resúmenes ejecutivos que integran todas las fuentes (CRM + Meta Ads + Google Ads + Operaciones) en una vista consolidada. Es la carpeta que el START_DAY_ENGINE lee cada mañana.

### Archivos presentes

| Archivo | Tipo | Estado |
|---------|------|--------|
| `reporte_diario.md` | Plantilla diaria | ✅ Plantilla oficial |
| `reporte_semanal.md` | Plantilla semanal | ✅ Plantilla oficial |
| `reporte_diario_2026-06-22.md` | Reporte real | ✅ Completado |
| `reporte_2026-06-22.md` | Reporte real | ✅ Completado |
| `reporte_diario_2026-06-22_093532.md` | Reporte real (timestamp) | ✅ Completado |
| `reporte_semana_2026-W25.md` | Reporte real semana 25 | ✅ Completado |
| `reporte_semana_2026-W26.md` | Reporte real semana 26 | ✅ Completado |

### Convención de nombres

```
DIARIO:   reporte_YYYY-MM-DD.md        (ej: reporte_2026-06-24.md)
SEMANAL:  reporte_semana_YYYY-WNN.md   (ej: reporte_semana_2026-W26.md)
```

---

## ESTRUCTURA DEL REPORTE DIARIO (resumen)

Cada archivo diario integra datos de todas las fuentes:

```
1. LEADS DEL DÍA          → fuente: CRM/ + Meta Ads/
2. CAMPAÑAS ACTIVAS        → fuente: META_ADS/ + GOOGLE_ADS/
3. PROYECTOS EN CAMPO      → fuente: OPERACIONES/
4. ACCIONES PRIORITARIAS   → decisión de Daniel
5. ALERTAS ACTIVAS         → cualquier sistema que requiera atención
6. CIERRE DEL DÍA          → confirmación de tareas completadas
```

---

## FRECUENCIA DE ACTUALIZACIÓN

| Acción | Cuándo | Tiempo estimado |
|--------|--------|----------------|
| Crear reporte diario | 17:00h todos los días hábiles | 10-15 min |
| Revisar reporte del día anterior | 07:00h (START_DAY_ENGINE) | 5 min |
| Crear reporte semanal | Lunes AM antes de reunión 09:00h | 30 min |
| Archivar reportes viejos | Mensualmente | 5 min |

---

## RESPONSABLE

- **Creación:** Daniel — al cierre del día (17:00h)
- **Lectura:** START_DAY_ENGINE — al inicio del día (07:00h)
- **Distribución:** WhatsApp equipo antes de 18:00h (si aplica)

---

## CÓMO USAR LAS PLANTILLAS

```
Para reporte diario:
  1. Copiar reporte_diario.md
  2. Renombrar: reporte_YYYY-MM-DD.md
  3. Llenar todas las secciones
  4. Si un dato no está disponible: escribir "N/D — razón"
  5. Guardar aquí y hacer commit

Para reporte semanal:
  1. Copiar reporte_semanal.md
  2. Renombrar: reporte_semana_YYYY-WNN.md
  3. Consolidar datos de los 5 reportes diarios
  4. Comparar con semana anterior
  5. Guardar aquí y hacer commit
```

---

## CONEXIÓN CON OTROS SISTEMAS

- **Lee desde:** `CRM/`, `META_ADS/`, `GOOGLE_ADS/`, `OPERACIONES/`
- **Alimenta:** `DASHBOARDS/` — los reportes diarios son el input del CEO Dashboard
- **Lee:** START_DAY_ENGINE (`10_MEMORIA_EMPRESARIAL/OPERACIONES_DIARIAS/START_DAY_ENGINE.md`)
- **Distribución:** WhatsApp equipo (manual hasta automatización activa)
