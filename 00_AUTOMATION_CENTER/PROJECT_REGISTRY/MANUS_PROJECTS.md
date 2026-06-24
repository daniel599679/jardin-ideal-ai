# REGISTRO DE PROYECTOS MANUS — Jardín Ideal
**Automation Center — Project Registry**
**Versión:** 1.0 · **Última actualización:** 2026-06-24

---

## INSTRUCCIONES

Este archivo registra todos los proyectos activos generados con o para Manus. Es la fuente de verdad sobre el estado de cada pieza. Actualizar después de cada sesión de trabajo.

**Campos obligatorios al registrar un proyecto:**
- Nombre único del proyecto
- Tipo y servicio
- Rutas locales fuente/inbox/outbox
- Versión actual y próxima
- Estado y automatización permitida

---

## PROYECTOS ACTIVOS

---

### PROYECTO 001 — Landing Cour Arrière

| Campo | Valor |
|-------|-------|
| **ID** | LP-001 |
| **Nombre** | Landing Cour Arrière |
| **Tipo** | Landing Page |
| **Servicio** | Cour Arrière (aménagement complet) |
| **Idioma** | Français (Québec) |
| **Generado en** | Manus |

#### Rutas de archivos

| Rol | Ruta |
|-----|------|
| **Carpeta local fuente** | `05_MARKETING/LANDING_PAGES/COUR_ARRIERE/` |
| **HTML V1 (referencia)** | `00_INBOX_MANUS/LANDING_PAGES/2026-06-24_COUR_ARRIERE_V1_NOTES.md.txt` |
| **Correcciones V1→V2** | `00_OUTBOX_CLAUDE_PARA_MANUS/CORRECCIONES/CORRECTIONS_COUR_ARRIERE_V1.md` |
| **Prompt V2 para Manus** | `00_OUTBOX_CLAUDE_PARA_MANUS/PROMPTS_MANUS/PROMPT_CORRECTION_COUR_ARRIERE_V1_SAFE.md` |
| **Análisis técnico** | `07_REPORTES/LANDING_PAGES/ANALISIS_REAL_COUR_ARRIERE_V1.md` |
| **Carpeta inbox Manus** | `00_INBOX_MANUS/LANDING_PAGES/` |
| **Carpeta outbox Manus** | `00_OUTBOX_CLAUDE_PARA_MANUS/PROMPTS_MANUS/` |

#### Estado de versiones

| Campo | Valor |
|-------|-------|
| **Versión actual** | V1 (generada por Manus) |
| **Score auditoría V1** | 68/100 |
| **Próxima versión** | V2 |
| **Estado V2** | ⏳ Pendiente — generar en Manus con PROMPT_SAFE |

#### Automatización

| Campo | Valor |
|-------|-------|
| **Automatización permitida** | Correcciones técnicas locales (HTML/JS/CSS) |
| **Aprobación humana requerida** | Publicación, activación de campaña, cambio de textos legales |
| **Blockers actuales** | Meta Pixel ID ⏳ · Zapier webhook URL ⏳ |

#### Blockers antes de publicar

- [ ] Meta Pixel ID real (actualmente `TU_PIXEL_ID`)
- [ ] Zapier webhook URL configurado
- [ ] Loi 25 checkboxes añadidos al formulario principal
- [ ] Loi 25 checkboxes añadidos al modal financement
- [ ] "Pré-approuvé" reemplazado por "Demande reçue"
- [ ] `submitForm()` conectada a Zapier
- [ ] Test completo del formulario (campo por campo)
- [ ] Test de la calculadora de estimation
- [ ] Test del mini-calculateur financement
- [ ] Revisión en mobile (iPhone + Android)

#### Checklist de publicación

- [ ] Score mínimo 85/100 en auditoría Claude Code
- [ ] Formulario enviando datos reales a Pipedrive
- [ ] Meta Pixel disparando eventos `PageView` y `Lead`
- [ ] Approbation explicite de Daniel
- [ ] Backup del HTML antes de publicar
- [ ] URL de producción documentada aquí

#### Notas

- V1 generada en Manus, auditada el 2026-06-24
- Email `info@jardin-ideal.com` ya correcto en V1 — no requiere cambio
- Garantie "5 ans" en trust pills y checklist → correcto solo para pavé
- "+200 projets" contradice "1 500+" → eliminar en V2
- Copyright "2025" → actualizar a "2026" en V2
- `admin-cour-arriere.html` visible en topbar → ocultar en V2

---

### PROYECTO 002 — Landing Pavé Uni

| Campo | Valor |
|-------|-------|
| **ID** | LP-002 |
| **Nombre** | Landing Pavé Uni |
| **Tipo** | Landing Page |
| **Servicio** | Pavé uni (projet spécialisé) |
| **Idioma** | Français (Québec) |
| **Generado en** | Por generar |

| Campo | Valor |
|-------|-------|
| **Carpeta local fuente** | `05_MARKETING/LANDING_PAGES/PAVE_UNI/` *(pendiente crear)* |
| **Versión actual** | — (no generada) |
| **Estado** | ⏳ Por generar — prioridad después de LP-001 V2 |
| **Automatización permitida** | N/A hasta tener V1 |
| **Aprobación humana requerida** | Todo |

---

### PROYECTO 003 — Landing Piscine + Aménagement

| Campo | Valor |
|-------|-------|
| **ID** | LP-003 |
| **Nombre** | Landing Piscine + Aménagement |
| **Tipo** | Landing Page |
| **Servicio** | Piscine creusée + aménagement paysager |
| **Idioma** | Français (Québec) |
| **Generado en** | Por generar |

| Campo | Valor |
|-------|-------|
| **Versión actual** | — (no generada) |
| **Estado** | ⏳ Prioridad alta — alta temporada julio 2026 |
| **Automatización permitida** | N/A hasta tener V1 |

---

## PROYECTOS EN PIPELINE (no iniciados)

| ID | Nombre | Tipo | Prioridad | Estado |
|----|--------|------|-----------|--------|
| LP-004 | Landing Terrasse | Landing Page | Media | Por iniciar |
| LP-005 | Landing Cour Avant | Landing Page | Baja | Por iniciar |
| LP-006 | Landing Pergola/Gazebo | Landing Page | Media | Por iniciar |
| LP-007 | Landing Cuisine Extérieure | Landing Page | Baja | Por iniciar |
| CC-001 | Carrusel Cour Arrière — Meta | Carrusel | Alta | Por iniciar |
| CC-002 | Carrusel Pavé Uni — Meta | Carrusel | Media | Por iniciar |
| RL-001 | Reel Timelapse Proyecto | Reel | Media | Por iniciar |

---

## TIPOS DE PROYECTO — REFERENCIA

| Tipo | Descripción | Editor principal |
|------|-------------|-----------------|
| `landing` | Página HTML de captura de leads | Manus + Claude Code |
| `carrusel` | Serie de imágenes para Meta/Instagram | Manus / Canva |
| `reel` | Video corto para Meta/TikTok | Manus / CapCut |
| `video` | Video largo o de campaña | Manus / Premiere |
| `imagen` | Imagen única para anuncio | Manus / Canva |
| `campana` | Configuración completa de campaña | Meta Ads / Google Ads |

---

## HISTORIAL DE CAMBIOS AL REGISTRO

| Fecha | Cambio |
|-------|--------|
| 2026-06-24 | Creación del registro. LP-001 registrada con auditoría V1. |

---

*Project Registry — Jardín Ideal Automation Center · v1.0 · 2026-06-24*
*Actualizar después de cada sesión de trabajo con Manus o Claude Code*
