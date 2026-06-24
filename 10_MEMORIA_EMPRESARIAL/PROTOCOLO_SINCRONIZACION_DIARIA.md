# PROTOCOLO DE SINCRONIZACIÓN DIARIA
**Versión:** 1.0 | **Fecha:** 2026-06-24
**Clasificación:** PROTOCOLO OBLIGATORIO — ejecutar antes de cualquier tarea diaria

---

## PROPÓSITO

Este protocolo conecta el sistema de IA (Jardín Ideal AI System) con los datos reales del negocio. Los datos provienen del **Agente Director** que monitorea Meta Ads Manager, Pipedrive y Outlook en tiempo real y genera un briefing diario.

**Regla fundamental:**
> El dato real del JSON siempre prevalece sobre cualquier documentación previa del sistema.

---

## PASO 1 — LEER ARCHIVOS DE DATOS

**Ruta:** `Claude/Projects/Agente Director/data/`
*(Ruta absoluta: `C:/Users/Daniel/Desktop/Jardin-ideal-AI/Claude/Projects/Agente Director/data/`)*

**Archivos a identificar y leer:**

```
BRIEFING-CLAUDE-CODE-YYYY-MM-DD.md   ← briefing narrativo con contexto
reporte-diario-YYYY-MM-DD.json        ← datos estructurados con todos los números
```

Leer **ambos archivos completos** antes de cualquier acción. Si el archivo del día no existe, usar el más reciente disponible e indicar la fecha.

---

## PASO 2 — ACTUALIZAR ARCHIVOS DEL SISTEMA

Con los datos verificados del JSON, actualizar únicamente con información real:

| Archivo | Qué actualizar |
|---------|---------------|
| `10_MEMORIA_EMPRESARIAL/MEMORIA_GLOBAL.md` | Estado campañas, pipeline, problemas técnicos activos |
| `10_MEMORIA_EMPRESARIAL/KPIS_EMPRESA.md` | KPIs Meta Ads, leads, CPL, gasto |
| `10_MEMORIA_EMPRESARIAL/ESTADO_ACTUAL_ECOSISTEMA.md` | Estado de integraciones, Zapier, bugs activos |
| `10_MEMORIA_EMPRESARIAL/PROXIMO_SPRINT.md` | Reprioritizar según urgencias reales del día |
| `08_REPORTES/META_ADS/` | Snapshot de campañas del día |
| `08_REPORTES/CRM/` | Estado del pipeline, leads vencidos |

**Regla:** Si los datos reales contradicen la documentación previa → corregir la documentación. Nunca al revés.

---

## PASO 3 — PRIORIDADES OPERATIVAS

Toda decisión del día debe seguir este orden:

```
1. Generación de ingresos        → leads calientes, propuestas, cierres
2. Seguimiento de leads          → leads vencidos, sin contacto, en riesgo
3. Optimización de campañas      → pausar lo que no funciona, escalar lo que funciona
4. Cierres de ventas             → propuestas enviadas, visitas agendadas
5. Eliminación de cuellos        → bugs técnicos, Zapier roto, integraciones fallidas
```

---

## PASO 4 — GENERAR START_DAY_ENGINE

Crear archivo: `08_REPORTES/RESUMENES_DIARIOS/START_DAY_ENGINE_YYYY-MM-DD.md`

**Estructura obligatoria:**

```markdown
# START DAY ENGINE — YYYY-MM-DD

## ⚠️ RIESGOS CRÍTICOS
[Problemas que cuestan dinero o leads hoy]

## 🔴 LEADS URGENTES
[Tabla: nombre | servicio | días vencido | propietario | acción]

## 📊 CAMPAÑAS A OPTIMIZAR
[Tabla: campaña | acción | razón | impacto]

## 💰 OPORTUNIDADES DE CIERRE
[Leads en etapas avanzadas — RDV, propuestas, visitas]

## 📋 ACTIVIDADES VENCIDAS EN PIPEDRIVE
[Resumen de cuántas, quién las debe, cuántos días]

## ✅ TAREAS DEL DÍA
[Lista por responsable: Daniel / Lyes / Jonathan / equipo]

## 📈 KPIs PRINCIPALES
[Tabla resumen: campañas, pipeline, presupuesto]

## 🔧 PROBLEMAS TÉCNICOS ABIERTOS
[Bugs Zapier, HubSpot, integraciones]
```

---

## PASO 5 — COMMIT Y PUSH

```bash
git add 08_REPORTES/ 10_MEMORIA_EMPRESARIAL/
git commit -m "sync: START_DAY_ENGINE YYYY-MM-DD — datos reales Meta Ads + Pipedrive"
git push origin master
```

---

## REGLAS DE CONDUCTA

```
✅ Usar solo datos del JSON — no inventar métricas
✅ Marcar "por confirmar" si un dato falta en el JSON
✅ Idioma interno: español
✅ Idioma para clientes: francés (Quebec)
❌ No modificar Pipedrive directamente — solo documentar
❌ No modificar Zapier directamente — solo documentar acciones para Daniel
❌ No asumir emails o datos de contacto — si no está en el JSON, es desconocido
```

---

## FUENTES DE DATOS — ARQUITECTURA

```
Meta Ads Manager ─────────────────────┐
Pipedrive (pipeline "Leads qualifiés") ├──► Agente Director (Cowork)
Outlook (emails 7 días) ──────────────┘         │
                                                  │
                              ┌───────────────────┤
                              │                   │
                              ▼                   ▼
              BRIEFING-CLAUDE-CODE-YYYY.md   reporte-diario-YYYY.json
              (narrativo, contexto)          (datos estructurados)
                              │
                              ▼
                    Claude Code ejecuta
                    PROTOCOLO_SINCRONIZACION_DIARIA
                              │
                              ▼
              START_DAY_ENGINE_YYYY-MM-DD.md
              (brief operativo del día)
```

---

## HISTORIAL DE EJECUCIONES

| Fecha | Archivo JSON | Problemas encontrados | Acciones tomadas |
|-------|-------------|----------------------|-----------------|
| 2026-06-24 | reporte-diario-2026-06-24.json | Zap email incorrecto, 9 leads vencidos, 2 campañas a pausar | START_DAY_ENGINE generado, KPIS actualizados, acciones documentadas |

---

*PROTOCOLO_SINCRONIZACION_DIARIA v1.0 — Jardín Ideal AI System — 2026-06-24*
