# CHANGELOG — Jardín Ideal AI System

---

## [2026-06-24] — Datos confirmados + Paquete Manus Context Pack

### Datos confirmados por Daniel

| Dato | Valor confirmado |
|------|-----------------|
| Courriel oficial (todas las LPs) | `info@jardin-ideal.com` ✅ |
| Garantie pavé / pavé uni | 5 ans ✅ |
| Garantie otros servicios | "Garantie selon le type de projet, les matériaux sélectionnés et les conditions du contrat" ✅ |
| Texto financement disclaimer | "Estimation indicative. Sujet à l'analyse et à l'approbation du partenaire financier." ✅ |
| Meta Pixel ID | ⏳ PENDIENTE — recuperar de Meta Business Suite |
| Zapier webhook URL | ⏳ PENDIENTE — configurar Zap |

### Archivos creados / actualizados

**Actualizados:**
- `00_OUTBOX_CLAUDE_PARA_MANUS/CORRECCIONES/CORRECTIONS_COUR_ARRIERE_V1.md`
  - Tabla de datos confirmados añadida al inicio
  - C9 (garantía): actualizado con reglas por tipo de servicio
  - C11 (email): confirmado, no requiere cambio

**Creados — Prompts:**
- `00_OUTBOX_CLAUDE_PARA_MANUS/PROMPTS_MANUS/PROMPT_CORRECTION_COUR_ARRIERE_V1_SAFE.md`
  - Prompt completo safe para generar V2, con datos confirmados, sin datos inventados
  - Placeholders claros para Pixel ID y Zapier

**Creados — Paquete Context Manus:**
- `00_OUTBOX_CLAUDE_PARA_MANUS/PAQUETES_CONTEXT_MANUS/ACTUAL/01_INDICE_CONTEXT_PACK.md`
- `00_OUTBOX_CLAUDE_PARA_MANUS/PAQUETES_CONTEXT_MANUS/ACTUAL/02_REGLAS_DE_MARCA_Y_ESTILO.md`
- `00_OUTBOX_CLAUDE_PARA_MANUS/PAQUETES_CONTEXT_MANUS/ACTUAL/03_REGLAS_LANDING_PAGES.md`
- `00_OUTBOX_CLAUDE_PARA_MANUS/PAQUETES_CONTEXT_MANUS/ACTUAL/04_CONTEXTO_CAMPANA_ACTUAL.md`

### Pendientes operacionales (Daniel)

- [ ] Recuperar Meta Pixel ID → Meta Business Suite → Events Manager → Pixels
- [ ] Configurar Zapier Zap → obtener webhook URL
- [ ] Aplicar `PROMPT_CORRECTION_COUR_ARRIERE_V1_SAFE.md` en Manus → generar V2
- [ ] Confirmar garantías para servicios distintos a pavé (piscine, terrasse, clôture...)
- [ ] Pausar campañas Meta: cour avant + banos
- [ ] Subir budget Meta cour arrière a $55/día
- [ ] Corregir Zapier: reemplazar `daniel@grupoideal.com` → `daniel@groupe-ideal.com`
- [ ] Llamar leads en espera (Emilie Fournelle 12d, JF Gilbert 9d, Archambault 8d, otros)

---

## [2026-06-24] — Auditoría técnica real LP Cour Arrière V1

### Análisis completado

- HTML V1 auditado en 10 dimensiones técnicas
- Score: **68/100** — NO lista para publicación
- 5 blockers críticos identificados

### Archivos creados

- `07_REPORTES/LANDING_PAGES/ANALISIS_REAL_COUR_ARRIERE_V1.md` — diagnóstico completo
- `00_OUTBOX_CLAUDE_PARA_MANUS/CORRECCIONES/CORRECTIONS_COUR_ARRIERE_V1.md` — 20 correcciones con código
- `00_OUTBOX_CLAUDE_PARA_MANUS/PROMPTS_MANUS/PROMPT_CORRECTION_COUR_ARRIERE_V1.md` — prompt para Manus
- `07_REPORTES/LANDING_PAGES/PROTOCOLO_MANUS_CLAUDE_CODE.md` — protocolo de trabajo

---

## [2026-06-24] — Sistema de comunicación Manus ↔ Claude Code

### Infraestructura creada

Estructura completa de carpetas para intercambio de archivos entre Manus y Claude Code:
- `00_INBOX_MANUS/` (3 subcarpetas) — archivos entrantes de Manus
- `00_OUTBOX_CLAUDE_PARA_MANUS/` (4 subcarpetas) — archivos salientes para Manus
- Protocolo 13 pasos + checklist 25 puntos
- README de protocolo + naming conventions

---

## [2026-06-23] — Sesión diaria + Plan marketing + Hero Post

### Tareas completadas

- Sync diario del sistema operativo
- Resumen ejecutivo CEO (estado leads, campañas, operaciones)
- Plan marketing semana del 2026-06-23
- Hero Post LinkedIn (contenido semana)
- Presentación ecosistema IA 2026 (15 slides HTML)

---

*CHANGELOG generado por Claude Code — Jardín Ideal AI System*
