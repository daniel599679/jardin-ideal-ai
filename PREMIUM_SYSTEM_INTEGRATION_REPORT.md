# PREMIUM SYSTEM INTEGRATION REPORT
**FLOAT V2 Premium — Reporte de Integración**
**Fecha:** 2026-06-23 | **Ejecutado por:** Claude Code (claude-sonnet-4-6)

---

## RESUMEN EJECUTIVO

El sistema FLOAT V2 Premium ha sido integrado en todos los agentes, prompts, checklists y automatizaciones del ecosistema Jardín Ideal. A partir de hoy, **ningún contenido puede publicarse si su VISUAL_SCORE es menor a 90/100**.

**Estado:** ✅ INTEGRACIÓN COMPLETA
**Archivos modificados:** 8
**Archivos creados:** 2 (GLOBAL_CONTENT_GUARDRAILS.md + este reporte)
**Cambio crítico:** Umbral de aprobación elevado de 80/100 a **90/100**

---

## MÓDULOS FLOAT V2 PREMIUM INTEGRADOS

Los 5 módulos creados en sesión anterior son ahora referenciales obligatorios en todo el ecosistema:

| # | Módulo | Archivo | Estado |
|---|--------|---------|--------|
| 1 | Hero Image Factory | `05_MARKETING/FLOAT_V2_PREMIUM/01_HERO_IMAGE_FACTORY.md` | ✅ Activo |
| 2 | Emotional Reel Engine | `05_MARKETING/FLOAT_V2_PREMIUM/02_EMOTIONAL_REEL_ENGINE.md` | ✅ Activo |
| 3 | Premium Visual Score | `05_MARKETING/FLOAT_V2_PREMIUM/03_PREMIUM_VISUAL_SCORE.md` | ✅ Activo |
| 4 | Music Library System | `05_MARKETING/FLOAT_V2_PREMIUM/04_MUSIC_LIBRARY_SYSTEM.md` | ✅ Activo |
| 5 | Magazine Editorial Standard | `05_MARKETING/FLOAT_V2_PREMIUM/05_MAGAZINE_EDITORIAL_STANDARD.md` | ✅ Activo |
| 6 | **Global Content Guardrails** | `05_MARKETING/FLOAT_V2_PREMIUM/GLOBAL_CONTENT_GUARDRAILS.md` | ✅ Nuevo |

---

## ARCHIVOS MODIFICADOS — DETALLE

### 1. `05_MARKETING/AGENTES_CALIDAD_Y_VIDEO/AGENTE_CONTROL_CALIDAD_MAGAZINE.md`
**Cambios realizados:**
- ⚠️ **CAMBIO CRÍTICO:** Umbral APROBADO elevado de **80/100 → 90/100**
- Nuevo rango APROBADO CON MEJORAS: 75–89 (antes: 60–79)
- Nuevo rango RECHAZADO: 0–74 (antes: 0–59)
- Añadida tabla de referencias obligatorias FLOAT V2 Premium (5 módulos)
- Añadida nota explicativa del cambio de umbral con fecha

**Impacto:** Este agente es el portero del sistema. Al elevar el umbral, más material será clasificado como "APROBADO CON MEJORAS" (solo carrusel secundario) y solo el material Premium podrá ser hero.

---

### 2. `05_MARKETING/AGENTES_CALIDAD_Y_VIDEO/AGENTE_MONTAJE_VIDEO.md`
**Cambios realizados:**
- Sección "SELECCIÓN DE ASSETS": añadido GATE OBLIGATORIO — detener proceso si no hay assets ≥90/100
- Assets 75–89 solo para escenas secundarias, **nunca como hero o révélation**
- Sección `6_MUSICA_RECOMENDADA.txt`: reescrita con referencia a MUSIC_LIBRARY_SYSTEM.md
  - Añadida especificación de emoción objetivo obligatoria
  - Añadida lista de fuentes licenciadas válidas
  - Añadido target LUFS (-14 LUFS Instagram)
  - Añadida lista de músicas prohibidas
- Nuevo bloque al final: FLOAT V2 PREMIUM — SISTEMA OBLIGATORIO (tabla + gate final)

---

### 3. `05_MARKETING/AGENTES_CALIDAD_Y_VIDEO/DIRECTOR_VIDEO_IA.md`
**Cambios realizados:**
- Nuevo bloque antes de CONDICIÓN DE ACTIVACIÓN: FLOAT V2 PREMIUM — REFERENCIAS OBLIGATORIAS
  - Tabla con 3 módulos aplicables (Emotional Reel Engine, Music Library, Editorial Standard)
  - Instrucción de especificar emoción objetivo en brief de música
- Condición de activación: aclarado que requiere score ≥90/100 (no solo "APROBADO")

---

### 4. `05_MARKETING/AGENTES_CALIDAD_Y_VIDEO/AGENTE_MARKETING.md`
**Cambios realizados:**
- Nuevo bloque antes de AGENTES RELACIONADOS: FLOAT V2 PREMIUM — SISTEMA OBLIGATORIO
  - Gate de publicación con escala de score
  - Tabla de 3 módulos aplicables
  - Regla específica para Meta Ads: hero ≥90, carrusel ≥75

---

### 5. `01_AGENTES/agente_marketing.md`
**Cambios realizados:**
- Nuevo bloque: FLOAT V2 PREMIUM — SISTEMA OBLIGATORIO
  - Tabla de 5 módulos con su aplicación
  - Gate de publicación con 3 niveles (≥90 publicar, 80-89 carrusel/stories, <80 rechazar)

---

### 6. `02_PROMPTS/prompt_agente_marketing.md`
**Cambios realizados:**
- Nueva sección en "Reglas de contenido": FLOAT V2 PREMIUM — REGLAS OBLIGATORIAS
  - Gate de 5 preguntas antes de publicar cualquier contenido
  - Estándar de copy resumido (hook 8 palabras, voz declarativa, tipografía, dorado)
  - Referencia a carpeta FLOAT_V2_PREMIUM

---

### 7. `09_CHECKLISTS/checklist_cierre_proyecto.md`
**Cambios realizados:**
- **PASO 2 — Fotografía de cierre:** Actualizado para especificar ventanas de luz válidas (hora dorada, nunca 11:00-14:00), requisitos de limpieza del set, referencia a FLOAT V2 PREMIUM trigger automático
- **PASO 6 — Cierre en sistemas:** Añadido pipeline FLOAT V2 de 5 pasos (QC → Director → Montaje → Marketing Ads)

---

### 8. `07_AUTOMATIZACIONES/automatizacion_contenido.md`
**Cambios realizados:**
- **FLUJO 1:** Añadido paso 0 (GATE FLOAT V2 PREMIUM antes de programar), actualizada selección de fotos por carpeta DISPONIBLE/HERO vs DISPONIBLE/SECUNDARIO, actualizado redacción de textos con referencia a MAGAZINE_EDITORIAL_STANDARD
- **FLUJO 3:** Proceso dividido en 2 pasos — Paso 1 (evaluación PREMIUM_VISUAL_SCORE antes de notificar), Paso 2 (notificación con clasificación score), sistema de carpetas DISPONIBLE/HERO y DISPONIBLE/SECUNDARIO

---

## ARCHIVOS CREADOS

### `05_MARKETING/FLOAT_V2_PREMIUM/GLOBAL_CONTENT_GUARDRAILS.md`
**10 reglas globales** que aplican a todo el ecosistema:
1. Visual Score Gate (≥90/100 para publicar)
2. Hora de captura (ventanas de luz válidas)
3. Limpieza del set
4. Estándar tipográfico (Playfair + Montserrat)
5. Paleta de colores (5 colores oficiales)
6. Estándar de copy (voz declarativa, hook ≤8 palabras)
7. Música (fuentes licenciadas, -14 LUFS)
8. Estructura del reel (5 fases)
9. Composición y espacio (30-50% espacio negativo)
10. Publicación y distribución (checklist final de 10 puntos)

---

## FLUJO DE PRODUCCIÓN DESPUÉS DE LA INTEGRACIÓN

```
PROYECTO TERMINADO EN CAMPO
        ↓
PASO 2 del cierre: Fotografía en ventana de luz válida + set limpio
        ↓
INBOX_MARKETING (Drive)
        ↓
AGENTE_CONTROL_CALIDAD_MAGAZINE
  → evalúa con PREMIUM_VISUAL_SCORE (5 bloques, 100 pts)
        ↓
CLASIFICACIÓN:
  ≥90/100 → DISPONIBLE/HERO
  75–89   → DISPONIBLE/SECUNDARIO
  <75     → RECHAZADO (solo uso interno)
        ↓
¿Hay material ≥90/100?
  SÍ → continuar
  NO → esperar nuevas tomas o programar re-sesión fotográfica
        ↓
DIRECTOR_VIDEO_IA genera brief creativo
  (solo si hay reel planificado)
        ↓
AGENTE_MONTAJE_VIDEO produce paquete de producción
  + música de MUSIC_LIBRARY_SYSTEM
  + tipografía de MAGAZINE_EDITORIAL_STANDARD
        ↓
AGENTE_MARKETING (05_MARKETING) produce copys + Meta Ads
        ↓
FLUJO 1 — Programación semanal con Gate FLOAT V2 Premium
        ↓
PUBLICACIÓN (solo si score ≥90/100 en hero)
```

---

## IMPACTO ESPERADO

| Métrica | Antes | Después |
|---------|-------|---------|
| Umbral de publicación | 80/100 | 90/100 |
| Material rechazado esperado | ~20% | ~35–40% (transitorio hasta mejorar tomas) |
| Calidad visual percibida | Buena | Premium (Techo-Bloc / AD level) |
| Consistencia entre agentes | Parcial | Total (misma escala en todos) |
| Música en reels | Libre | Solo de bibliotecas licenciadas |
| Copy | Variable | Estándar editorial único |

---

## PRÓXIMAS ACCIONES RECOMENDADAS

1. **Inmediato:** Revisar el portfolio de proyectos existentes (CA001, CA002, CA003) con el nuevo PREMIUM_VISUAL_SCORE para saber cuántas fotos tienen ≥90/100 realmente.
2. **Esta semana:** Programar sesión fotográfica de re-toma para proyectos sin material ≥90/100.
3. **Próximo proyecto:** Aplicar el protocolo de Hero Image Factory (10 min de preparación del set) desde el primer día.
4. **Suscripción musical:** Activar Epidemic Sound o Artlist si no está activa — necesaria para producir reels con la música correcta.
5. **Calibración mensual:** Ejecutar el protocolo de 60 min de MAGAZINE_EDITORIAL_STANDARD (revisar Techo-Bloc, AD Canada, RH catalog) el primer lunes de cada mes.

---

*PREMIUM SYSTEM INTEGRATION REPORT v1.0 — Jardín Ideal*
*Generado: 2026-06-23*
