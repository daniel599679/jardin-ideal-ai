# 00_DATOS_REALES — Fuente de Datos del Motor de Reportes

Esta carpeta es la **única fuente de verdad** del sistema de reportes de Jardín Ideal.
El motor de reportes (`scripts/generar_reporte.py`) lee exclusivamente de aquí.
Sin datos aquí → el reporte muestra alertas, no datos inventados.

---

## Estructura

```
00_DATOS_REALES/
├── CRM/                    → Pipeline de ventas (leads por etapa, alertas)
├── LEADS/                  → Leads nuevos del día (últimas 24h)
├── META_ADS/               → Métricas de campañas Meta (Facebook/Instagram)
├── GOOGLE_ADS/             → Métricas de campañas Google Ads
├── PROYECTOS/              → Proyectos activos en obra
├── TAREAS/                 → Tareas pendientes por agente
├── MATERIALES/             → Pedidos de materiales pendientes de recibir
├── FOTOS_VIDEOS/           → Registro de fotos/videos recibidos del equipo
└── OPERACIONES/            → Visitas, equipos, agenda reunión 09:00 AM
```

---

## Cómo actualizar cada mañana (07:00 AM)

| Carpeta | Frecuencia | Tiempo estimado | Fuente |
|---------|-----------|----------------|--------|
| CRM/ | Diario | 5 min | Pipedrive → exportar pipeline |
| LEADS/ | Diario | 3 min | Meta Business Suite + Google Ads |
| META_ADS/ | Diario | 3 min | Meta Ads Manager → datos de ayer |
| GOOGLE_ADS/ | Diario | 3 min | Google Ads → datos de ayer |
| PROYECTOS/ | Cuando hay cambio | 5 min | Manual |
| TAREAS/ | Diario | 3 min | Manual (agregar nuevas, marcar completadas) |
| MATERIALES/ | Cuando hay cambio | 2 min | Manual al hacer/recibir pedidos |
| FOTOS_VIDEOS/ | Diario tarde | 3 min | Manual al recibir fotos del equipo |
| OPERACIONES/ | Noche anterior | 5 min | Manual + calendario |

**Total estimado:** 20–30 minutos manuales por día hasta que estén activas las automatizaciones de Make.com.

---

## Reglas de este directorio

1. **No eliminar archivos** — el motor detecta archivos del día por fecha en el nombre
2. **Nunca editar las plantillas README.md** — son la documentación del esquema
3. **Formato de fecha siempre ISO:** `YYYY-MM-DD` en nombres de archivos y dentro de los JSON
4. **Campos vacíos permitidos:** usar `""` para strings y `null` para valores nulos — nunca omitir campos del esquema
5. **Un archivo por día** para CRM, LEADS, META_ADS, GOOGLE_ADS, FOTOS_VIDEOS
6. **Archivo único** (sin fecha) para PROYECTOS, TAREAS, MATERIALES, OPERACIONES — se sobreescribe

---

## Qué pasa si un archivo falta

El motor de reportes no falla — genera el reporte con alertas visibles:

```
⚠️ DATOS FALTANTES — 2026-06-22

  🔴 CRM/leads_pipeline_2026-06-22.json       — NO ENCONTRADO
  🔴 LEADS/leads_nuevos_2026-06-22.json        — NO ENCONTRADO
  ✅ META_ADS/meta_ads_2026-06-21.json         — OK
  ✅ GOOGLE_ADS/google_ads_2026-06-21.json     — OK
  ✅ PROYECTOS/proyectos_activos.json          — OK
  🟡 TAREAS/tareas_pendientes.json             — NO ENCONTRADO (no crítico)
  ✅ MATERIALES/materiales_pendientes.json     — OK
  🟡 FOTOS_VIDEOS/fotos_videos_2026-06-22.json — NO ENCONTRADO (no crítico)
  ✅ OPERACIONES/operaciones_hoy.json          — OK
```

Las secciones del reporte con datos faltantes se marcan con `[SIN DATOS]`
en lugar de mostrar información inventada.

---

## Futuro — Automatización con Make.com

Cuando estén implementados los flujos de Make.com, estos archivos se generarán automáticamente:

| Carpeta | Flujo Make.com | Estado |
|---------|---------------|--------|
| LEADS/ | Flujo A — Meta Lead Ads → CRM + archivo JSON | ⬜ Pendiente |
| META_ADS/ | Meta Marketing API → JSON diario | ⬜ Pendiente |
| GOOGLE_ADS/ | Google Ads API → JSON diario | ⬜ Pendiente |
| CRM/ | Pipedrive API → exportación automática | ⬜ Pendiente |

Ver `07_AUTOMATIZACIONES/automatizacion_leads.md` para el diseño de cada flujo.
