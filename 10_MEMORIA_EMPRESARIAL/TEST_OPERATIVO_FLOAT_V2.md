# TEST OPERATIVO — FLOAT V2 PREMIUM
**Versión:** 1.0 | **Fecha:** 2026-06-23
**Objetivo:** Producir y publicar una campaña real de Jardín Ideal esta semana.
**Resultado:** 5 piezas publicables desde 10 fotos + 3 videos + 1 audio.

---

## REGLA ÚNICA DE ESTE DOCUMENTO

Este archivo no es teoría. Es un guion de producción.
Se abre, se sigue paso a paso, se cierra cuando las 5 piezas están publicadas.

**Tiempo total estimado primera vez:** 5–6 horas
**Tiempo estimado a partir del segundo proyecto:** 3–4 horas

---

## PASO 0 — EVALUACIÓN DEL MATERIAL (hacer primero, siempre)

Antes de producir cualquier pieza, calificar el material disponible.
Si el material no alcanza el mínimo, no tiene sentido avanzar.

**Tiempo: 30–40 minutos**

```
INSTRUCCIÓN PARA CLAUDE CODE:
"Evalúa estas fotos con PREMIUM_VISUAL_SCORE.
Referencia: 05_MARKETING/FLOAT_V2_PREMIUM/03_PREMIUM_VISUAL_SCORE.md
Foto [nombre]: [descripción de lo que muestra]"
```

### Clasificación del material disponible

Completar esta tabla antes de producir nada:

```
INVENTARIO DE MATERIAL — PROYECTO: _______________________

FOTOS (evaluar las 10):
┌─────┬─────────────────────┬───────────────┬─────────┬────────────┐
│  #  │  Descripción        │  Hora tomada  │  Score  │  Decisión  │
├─────┼─────────────────────┼───────────────┼─────────┼────────────┤
│  1  │                     │               │  /100   │            │
│  2  │                     │               │  /100   │            │
│  3  │                     │               │  /100   │            │
│  4  │                     │               │  /100   │            │
│  5  │                     │               │  /100   │            │
│  6  │                     │               │  /100   │            │
│  7  │                     │               │  /100   │            │
│  8  │                     │               │  /100   │            │
│  9  │                     │               │  /100   │            │
│ 10  │                     │               │  /100   │            │
└─────┴─────────────────────┴───────────────┴─────────┴────────────┘

VIDEOS (evaluar los 3):
┌─────┬─────────────────────┬──────────┬─────────────┬────────────┐
│  #  │  Descripción        │  Durac.  │  Usable?    │  Para qué  │
├─────┼─────────────────────┼──────────┼─────────────┼────────────┤
│  1  │                     │          │  SÍ / NO    │            │
│  2  │                     │          │  SÍ / NO    │            │
│  3  │                     │          │  SÍ / NO    │            │
└─────┴─────────────────────┴──────────┴─────────────┴────────────┘

AUDIO:
  Duración: _____ | Idioma: _____ | Usable para voz en off: SÍ / NO

FOTO "ANTES" DISPONIBLE: SÍ / NO
  Si SÍ → descripción: _______________________________________
```

### Criterio go/no-go del material

```
CRITERIO                         MÍNIMO     ESTADO
─────────────────────────────────────────────────────
≥1 foto con score ≥90/100        OBLIGATORIO  __/10 fotos califican
≥1 foto "antes" identificable    OBLIGATORIO  SÍ / NO
≥3 fotos con score ≥80/100       OBLIGATORIO  __/10 fotos califican
≥1 video usable (estable, >5s)   OBLIGATORIO  __/3 videos califican
Material del mismo proyecto       OBLIGATORIO  SÍ / NO

Si no se cumplen todos los OBLIGATORIO → detener. Buscar otro proyecto.
```

---

## PIEZA A — HERO POST PREMIUM

**Objetivo:** Una sola foto que detiene el scroll. Feed permanente. Candidato a Meta Ad principal.

### Inputs necesarios

| Input | Descripción | Dónde está |
|-------|-------------|-----------|
| Foto hero | La de mayor score del inventario (≥90/100) | Del Paso 0 |
| Retoque Lightroom | Parámetros del Módulo 01 (Hero Image Factory) | `FLOAT_V2_PREMIUM/01_HERO_IMAGE_FACTORY.md` |
| Copy: hook | 1 frase, ≤8 palabras, declarativa, en francés | Claude Code genera |
| Copy: subtexto | 1 línea de contexto o social proof | Claude Code genera |
| CTA | Siempre: "Soumission gratuite · 514-266-2504" | Fijo |

### Instrucción de copy a Claude Code

```
"Genera el copy para un Hero Post de Jardín Ideal.
Proyecto: [tipo de proyecto — cour arrière, piscine, pavé-uni, etc.]
Zona: [barrio / ciudad]
Resultado visual: [describir lo que muestra la foto]

Reglas:
- Hook: ≤8 palabras, declarativo (no pregunta), en francés
- Subtexto: 1 línea, en francés, social proof o dato concreto
- CTA: 'Soumission gratuite · 514-266-2504'
- Sin signos de exclamación
- Sin 'meilleur' o 'meilleure' sin dato que lo respalde

Referencia: 05_MARKETING/FLOAT_V2_PREMIUM/05_MAGAZINE_EDITORIAL_STANDARD.md"
```

### Tiempo estimado

| Actividad | Tiempo |
|-----------|--------|
| Selección de la foto hero (del inventario) | 5 min |
| Retoque en Lightroom (parámetros del Módulo 01) | 20–30 min |
| Exportar en 4 formatos (4:5 / 1:1 / 16:9 / 9:16) | 5 min |
| Generar copy con Claude Code | 10 min |
| Componer el overlay de texto (Canva / Photoshop) | 10 min |
| Revisión final con PREMIUM_VISUAL_SCORE | 5 min |
| **TOTAL** | **55–65 min** |

### Score mínimo requerido

**90/100** en PREMIUM_VISUAL_SCORE (los 5 bloques)

### Método de evaluación

```
EVALUACIÓN HERO POST — usar la hoja de 03_PREMIUM_VISUAL_SCORE.md

Bloque 1 Composición:    ___ / 25
Bloque 2 Luz:            ___ / 25
Bloque 3 Color:          ___ / 20
Bloque 4 Limpieza:       ___ / 15
Bloque 5 Impacto:        ___ / 15
─────────────────────────────────
TOTAL:                   ___ / 100

¿Descalificación automática? SÍ / NO → Si SÍ: ¿cuál? ___________
```

### Criterios de rechazo

| Condición | Acción |
|-----------|--------|
| Score <90/100 | No publicar como hero. Usar como slide 2 del carrusel. |
| Descalificación automática activa | Descartar. Usar la foto de score más alto que no tenga descalificación. |
| Copy con signo de exclamación | Reescribir. |
| Copy con "meilleur/meilleure" sin dato | Reescribir. |
| CTA sin número de teléfono | Agregar. No publicar sin CTA. |
| Logo no visible | Agregar logo en esquina inferior derecha. |

### Responsable de aprobación

**Daniel** — aprobación final antes de publicar. Tiempo de revisión: 3 minutos.

### Publicación

```
Formato principal: 4:5 (1080×1350px) — Instagram Feed
Horario: lunes–viernes 17:30–18:30 (horario óptimo Quebec)
Caption (Claude Code genera): hook + 3 líneas de contexto + CTA + 5 hashtags relevantes
Crosspost: Facebook Page simultáneo
```

---

## PIEZA B — REEL EMOCIONAL (20–25 segundos)

**Objetivo:** El video que genera leads directos. Arquitectura de 5 fases. Diseñado para detener el scroll en ≤3 segundos.

### Inputs necesarios

| Input | Descripción | Dónde está |
|-------|-------------|-----------|
| Video principal | El más estable y de mejor luz de los 3 disponibles | Del Paso 0 |
| Videos secundarios | Hasta 2 videos adicionales para planos de detalle | Del Paso 0 |
| Foto "antes" | Para la Fase 2 del reel (el problema) | Del Paso 0 |
| Hero photo | Para el frame final del CTA | Pieza A ya retocada |
| Audio/música | Track de la biblioteca REVELACIÓN o ASPIRACIÓN | `04_MUSIC_LIBRARY_SYSTEM.md` |

### Estructura de edición exacta

```
TIMELINE DEL REEL (20 segundos, música a ~90–110 BPM)

00:00–00:03 → GANCHO (elegir uno):
  OPCIÓN 1: Drone alejándose del resultado → revela escala
  OPCIÓN 2: Foto "antes" estática → texto "Avant" esquina sup izq → corte abrupto al después
  OPCIÓN 3: Extreme close-up textura → se aleja → revela proyecto completo
  Regla: sin logo, sin nombre de empresa en estos 3 segundos

00:03–00:06 → EL PROBLEMA:
  Foto "antes" — desaturada, flat, Ken Burns effect (zoom lento)
  Texto: "Avant" — Montserrat, pequeño, esquina sup izq
  Si no hay foto "antes" → mostrar el espacio vacío o el trabajo en proceso (BTS)

00:06–00:14 → LA REVELACIÓN (8 segundos, 5 planos):
  Plano 1 (1.5 seg): close-up de textura o acabado — junta perfecta, borde nítido
  Plano 2 (2 seg): ángulo editorial del Módulo 01 (diagonal, nivel agua, ground raking)
  Plano 3 (2 seg): plano general — escala completa del proyecto
  Plano 4 (1.5 seg): detalle emocional — agua moviéndose, luz en escalones, sombra en pavé
  Plano 5 (1 seg): wider shot — todo el proyecto en un frame
  Regla: cada corte cae en el beat fuerte de la música

00:14–00:18 → PRUEBA SOCIAL (elegir uno):
  Dato: "+[X] projets réalisés à Montréal"
  Zona: "Westmount • TMR • Laval • Montréal"
  Split screen antes/después instantáneo (si el material lo permite)

00:18–00:20 → CTA:
  Hero photo como fondo
  Playfair Display Bold Italic: frase de cierre (elegir de Módulo 02)
  Montserrat: "514-266-2504" en #C8A45A (dorado)
  Logo Jardín Ideal: esquina inferior derecha, pequeño
```

### Instrucción de copy a Claude Code

```
"Genera el copy de texto para el reel de Jardín Ideal.
Proyecto: [tipo]
Emoción objetivo: [REVELACIÓN / ASPIRACIÓN — elegir uno]
Número de proyectos realizados: [X] (si no se sabe, omitir)

Necesito:
1. Texto para el gancho (≤6 palabras, aparece en pantalla)
2. Frase de cierre para el CTA (≤8 palabras, Playfair Display)
3. Opción de copy para la prueba social

Referencia: 05_MARKETING/FLOAT_V2_PREMIUM/02_EMOTIONAL_REEL_ENGINE.md"
```

### Tiempo estimado

| Actividad | Tiempo |
|-----------|--------|
| Seleccionar y cortar clips de video | 20 min |
| Seleccionar y sincronizar música (del catálogo licenciado) | 15 min |
| Editar el reel (Adobe Premiere, CapCut, DaVinci Resolve) | 45–60 min |
| Sincronizar cortes con beats | 10 min |
| Agregar texto overlays y CTA | 10 min |
| Medir audio a -14 LUFS y exportar | 10 min |
| Evaluación con checklist | 5 min |
| **TOTAL** | **115–130 min** |

### Score mínimo requerido

**90/100** en PREMIUM_VISUAL_SCORE **+** checklist de reel:

```
CHECKLIST DE REEL — verificar ANTES de exportar:
☐ Hook detiene scroll en ≤3 segundos (probar con alguien ajeno al proyecto)
☐ Cada corte cae en el beat fuerte de la música
☐ Ningún plano dura más de 2.5 segundos (excepto hero final)
☐ Audio a -14 LUFS (medir con medidor LUFS)
☐ Sin clipping de audio (ningún pico en rojo)
☐ Número de teléfono visible en el frame final — en dorado #C8A45A
☐ Logo visible en el frame final
☐ Sin zoom digital (solo óptico o edición)
☐ Sin handheld sin estabilización
☐ Sin glitch transitions / wipe / dissolve
☐ Exportado en 9:16 (1080×1920px) como formato principal
```

### Criterios de rechazo

| Condición | Acción |
|-----------|--------|
| Hook >3 segundos para generar interés | Reeditar. El reel no puede publicarse. |
| Cortes no sincronizados al beat | Reordenar cortes. |
| Audio no a -14 LUFS | Ajustar en herramienta de edición. No exportar sin esto. |
| Zoom digital visible | Reemplazar plano. |
| Número de teléfono no visible en frame final | Agregar antes de exportar. |
| Música sin licencia (de Spotify/Apple Music sin suscripción Epidemic/Artlist) | Reemplazar. Riesgo legal y de silencio en Instagram. |

### Responsable de aprobación

**Daniel** — ver el reel completo 2 veces antes de aprobar. Tiempo: 5 minutos.

### Publicación

```
Formato: 9:16 (1080×1920px) como Reel de Instagram
Horario: martes o miércoles 17:00–19:00 (máximo alcance orgánico de reels en Quebec)
Caption: misma estructura que el Hero Post + "Lien en bio" si aplica
Crosspost: Facebook Reels simultáneo
```

---

## PIEZA C — 3 STORIES

**Objetivo:** Cobertura de 24h que dirige tráfico al perfil y al formulario. Las 3 stories son una secuencia, no piezas sueltas.

### Story 1 — La imagen (hook de perfil)

| Campo | Detalle |
|-------|---------|
| **Input** | Hero photo ya retocada (de Pieza A) |
| **Formato** | 9:16 (1080×1920px) |
| **Texto overlay** | Playfair Display Bold: 1 línea del hook del Hero Post |
| **Elemento interactivo** | Encuesta (pregunta de 2 respuestas) O sondaje "¿Tu patio podría lucir así?" |
| **Tiempo de producción** | 10 minutos |
| **Score mínimo** | 70/100 (stories son efímeras — criterio más flexible) |

### Story 2 — El proceso (BTS / confianza)

| Campo | Detalle |
|-------|---------|
| **Input** | 1 clip de video del trabajo en proceso (antes, durante, o detalle artesanal) O foto de detalle (material, herramienta premium, proceso) |
| **Formato** | 9:16 — clip de 10–15 segundos o foto estática |
| **Texto overlay** | "Chaque détail compte." O "Voilà comment on travaille." — Montserrat, blanco |
| **Elemento interactivo** | Sticker de link al perfil O "DM pour plus d'info" |
| **Tiempo de producción** | 10 minutos |
| **Score mínimo** | N/A — es contenido de proceso, no evaluado con PREMIUM_VISUAL_SCORE |

### Story 3 — El CTA (conversión directa)

| Campo | Detalle |
|-------|---------|
| **Input** | Fondo de color sólido (#052B16 verde oscuro) O hero photo con overlay oscuro |
| **Texto principal** | Playfair Display: "Votre soumission gratuite." |
| **Subtexto** | Montserrat SemiBold: "Appelez-nous aujourd'hui" |
| **CTA** | Número en dorado #C8A45A — grande, centrado: "514-266-2504" |
| **Elemento interactivo** | Sticker de link a la landing page O "Répondez à ce message" |
| **Tiempo de producción** | 5 minutos |
| **Score mínimo** | N/A — texto puro, sin evaluación visual |

### Tiempo total Pieza C

**25 minutos** (las 3 stories en secuencia)

### Criterios de rechazo

| Condición | Acción |
|-----------|--------|
| Story 1 sin elemento interactivo | Agregar encuesta o sondaje antes de publicar |
| Story 3 sin número de teléfono visible | Es el único propósito de esta story — agregar |
| Texto ilegible (contraste insuficiente) | Agregar sombra detrás del texto o cambiar color |

### Responsable de aprobación

**Daniel** — revisión rápida de 2 minutos (las 3 juntas).

### Publicación

```
Publicar las 3 stories en secuencia, en orden: Story 1 → Story 2 → Story 3
Horario: cualquier día 11:00–14:00 (stories tienen menos dependencia de horario que feed)
Programar: el mismo día de publicación del Hero Post o un día después
```

---

## PIEZA D — CARRUSEL ANTES / DESPUÉS

**Objetivo:** El contenido con mayor tasa de guardado (save) en Instagram. Educa + convierte. Feed permanente.

### Estructura exacta del carrusel (6 slides)

```
SLIDE 1 — LA PORTADA (el hook del carrusel)
  Contenido: Hero photo en formato 4:5
  Texto: Hook del proyecto (mismo que Hero Post)
  Elemento visual: flechas sutiles indicando "deslizar →"
  Score mínimo: 90/100 (es la imagen que determina si la gente desliza)

SLIDE 2 — EL ANTES
  Contenido: Foto del estado original del espacio
  Color grade: desaturado, flat, sin corrección de Lightroom — contraste intencional
  Texto: "Avant" — Montserrat, pequeño, esquina superior izquierda
  Score mínimo: N/A (el "antes" no se evalúa estéticamente — es el problema)

SLIDE 3 — DESPUÉS: VISIÓN GENERAL
  Contenido: Foto de score más alto del inventario (puede ser la misma que Slide 1)
  Texto: "Après" — Montserrat, pequeño
  Score mínimo: 80/100

SLIDE 4 — DESPUÉS: DETALLE PREMIUM
  Contenido: Close-up de textura, acabado o material (el detalle artesanal)
  Texto: Dato técnico en 1 línea: "Pavé-uni Bergerac — Techo-Bloc" O "Béton estampé personnalisé"
  Score mínimo: 80/100

SLIDE 5 — DESPUÉS: ÁNGULO ALTERNATIVO
  Contenido: Segunda perspectiva del proyecto (drone, punto de entrada, nivel bajo)
  Texto: Zona geográfica: "Réalisé à [Barrio/Ciudad]" — Montserrat, pequeño
  Score mínimo: 80/100

SLIDE 6 — EL CTA
  Contenido: Fondo verde oscuro (#052B16) puro
  Texto principal (Playfair Display Bold Italic): "Votre projet mérite le même traitement."
  Subtexto (Montserrat SemiBold): "Demandez votre soumission gratuite"
  CTA (Montserrat Bold, dorado #C8A45A, grande): "514-266-2504"
  Logo: centrado en la parte inferior
  Score mínimo: N/A — tipográfico puro
```

### Instrucción de copy a Claude Code

```
"Genera el copy para el carrusel antes/después de Jardín Ideal.
Proyecto: [tipo]
Zona: [barrio / ciudad]
Material usado: [si se sabe]
Tiempo de instalación: [si se sabe]

Necesito:
1. Hook para Slide 1 (≤8 palabras, francés, declarativo)
2. Dato técnico para Slide 4 (1 línea, francés)
3. Frase de cierre para Slide 6 (≤10 palabras, aspiracional)
4. Caption del post (2–3 oraciones + CTA + 5 hashtags)

No usar signos de exclamación. No usar 'meilleur' sin dato concreto."
```

### Tiempo estimado

| Actividad | Tiempo |
|-----------|--------|
| Seleccionar fotos (del inventario, las ya evaluadas) | 5 min |
| Retocar foto "antes" (desaturar intencionalmente) | 5 min |
| Diseñar 6 slides en Canva | 25–35 min |
| Generar copy con Claude Code | 10 min |
| Revisión de consistencia visual entre slides | 5 min |
| **TOTAL** | **50–60 min** |

### Score mínimo requerido

- Slide 1: **90/100** (determina el CTR del carrusel)
- Slides 3–5: **80/100** cada una
- Slide 2 y 6: No evaluados con PREMIUM_VISUAL_SCORE

### Criterios de rechazo

| Condición | Acción |
|-----------|--------|
| Slide 1 <90/100 | Reemplazar con otra foto del inventario que sí alcance 90 |
| Foto "antes" con color grade premium | Desaturar — el "antes" NUNCA puede verse bien editado |
| Menos de 6 slides | Agregar slides faltantes antes de publicar |
| Slide 6 sin número de teléfono | Agregar. Es el único propósito de ese slide. |
| Inconsistencia de color grade entre slides 3–5 | Re-editar en Lightroom con el mismo preset |

### Responsable de aprobación

**Daniel** — revisar el carrusel completo en el teléfono (no en desktop). Si se ve bien en teléfono, se publica.

### Publicación

```
Formato: 4:5 (1080×1350px) por slide
Máximo slides: 10 (Instagram) — usar 6 como mínimo, hasta 8 si el material lo justifica
Horario: jueves o viernes 17:30–19:00 (carruseles tienen alto engagement estos días)
Caption: hook + descripción del proyecto + CTA + hashtags (Claude Code genera)
```

---

## PIEZA E — REMARKETING

**Objetivo:** Recuperar a quien ya vio el Hero Post o visitó el perfil pero no convirtió. Copy diferente a las piezas orgánicas. Tono más directo.

### Inputs necesarios

| Input | Descripción | Dónde está |
|-------|-------------|-----------|
| Hero photo | La misma imagen ya aprobada de Pieza A (no producir nueva) | Ya existe |
| Copy nuevo | Diferente ángulo — el visitor ya conoce el trabajo, falta el impulso | Claude Code |
| Presupuesto de ads | $20–40 CAD/día × 5–7 días = $100–280 CAD de test | Meta Ads Manager |

### Diferencias clave vs. Hero Post

```
HERO POST (orgánico)         →  REMARKETING (paid)
Objetivo: awareness           →  Objetivo: conversión directa
Tono: aspiracional            →  Tono: urgencia elegante
Hook: "Voici ce qu'on fait"   →  Hook: "Vous avez vu notre travail..."
CTA: suave (soumission libre) →  CTA: directo ("Appelez maintenant")
Audiencia: cold               →  Audiencia: warm (visitaron el perfil / vieron el ad anterior)
```

### Instrucción de copy a Claude Code

```
"Genera el copy para un ad de remarketing de Jardín Ideal.
La audiencia ya vio nuestro contenido anterior pero no contactó.
Proyecto que vieron: [tipo]

Reglas:
- Hook: acknowledge que ya nos conocen (≤8 palabras, francés)
- Cuerpo: 1 razón concreta para actuar esta semana (temporada, disponibilidad, garantía)
- CTA: más directo que las piezas orgánicas — "Appelez" no "Découvrez"
- Emoción: URGENCIA ELEGANTE (ver Módulo 04 — no ansiedad, no presión barata)

El copy debe sonar como si un amigo que conoce la empresa hablara contigo, no como un ad."
```

### Tiempo estimado

| Actividad | Tiempo |
|-----------|--------|
| Adaptar el hero post (nuevo copy overlay) | 10 min |
| Generar copy de remarketing con Claude Code | 10 min |
| Crear ad en Meta Ads Manager | 10 min |
| Configurar audiencia: retargeting (IG visitors, video viewers) | 10 min |
| **TOTAL** | **40 min** |

### Score mínimo requerido

**90/100** — misma imagen que el Hero Post, ya evaluada. Lo que se valida aquí es el copy:

```
CHECKLIST DE COPY REMARKETING:
☐ Hook diferente al Hero Post (no copiar)
☐ Tono más directo pero no agresivo
☐ CTA es "Appelez" o acción inmediata — no "Découvrez"
☐ Menciona disponibilidad, temporada o garantía concreta
☐ Sin signos de exclamación
☐ Sin "meilleur/meilleure" sin dato
☐ Número de teléfono en dorado #C8A45A visible
```

### Criterios de rechazo

| Condición | Acción |
|-----------|--------|
| Copy idéntico al Hero Post | Reescribir. El remarketing tiene otra función. |
| Tono agresivo / "¡Llama ahora ya!" | Reescribir. La urgencia en Jardín Ideal es siempre elegante. |
| Audiencia incorrecta (cold en vez de warm) | Verificar configuración de audiencia en Meta Ads. |
| Presupuesto >$50 CAD/día en primer test | Empezar con $20–30 CAD/día. Escalar si CPL <$80. |

### Responsable de aprobación

**Daniel** — aprobación del ad y del presupuesto antes de activar.

### Configuración del ad

```
Tipo de campaña: Conversión o Alcance (según la etapa)
Audiencia:
  - Personas que visitaron el perfil de Instagram en los últimos 30 días
  - Personas que vieron el video/reel al 50% o más
  - Excluyendo: ya contactaron (si se puede crear esta exclusión)
Presupuesto: $20–30 CAD/día × 7 días primer test
Duración: 7 días → revisar CPL → si <$80: continuar. Si >$100: pausar y cambiar copy.
KPI: CPL <$80 CAD (objetivo). CPL <$50: excepcional.
```

---

## CHECKLIST OPERATIVO COMPLETO — REUTILIZABLE

Usar este checklist para cada campaña nueva. Cada ítem es binario: hecho o no hecho.

```
════════════════════════════════════════════════════════════════
CHECKLIST DE PRODUCCIÓN — CAMPAÑA FLOAT V2
Proyecto: _________________________  Fecha: _________________
════════════════════════════════════════════════════════════════

PASO 0 — MATERIAL
☐ 10 fotos evaluadas con PREMIUM_VISUAL_SCORE
☐ ≥1 foto con score ≥90/100 identificada como hero
☐ ≥3 fotos con score ≥80/100 disponibles para carrusel
☐ Foto "antes" identificada (o equivalente)
☐ ≥1 video usable (estable, ≥5 segundos, buena luz)
☐ Música licenciada seleccionada (Epidemic Sound / Artlist)

PIEZA A — HERO POST PREMIUM
☐ Hero photo retocada con parámetros del Módulo 01
☐ Score final: ___ /100 (mínimo 90)
☐ Exportada en 4 formatos (4:5 / 1:1 / 16:9 / 9:16)
☐ Copy generado: hook + subtexto + CTA
☐ Sin signos de exclamación en el copy
☐ Número de teléfono visible: 514-266-2504
☐ Logo Jardín Ideal visible (esquina inferior derecha)
☐ Aprobada por Daniel: SÍ / NO

PIEZA B — REEL EMOCIONAL
☐ 5 planos de revelación seleccionados y cortados
☐ Foto "antes" integrada en posición 00:03–00:06
☐ Música sincronizada — cortes en beats fuertes
☐ Hook testado con persona ajena: detiene scroll en ≤3 seg SÍ / NO
☐ Audio medido: ___ LUFS (objetivo: -14)
☐ Sin clipping de audio (cero picos en rojo)
☐ Número de teléfono en dorado en el frame final
☐ Score reel: ___ /100 (mínimo 90)
☐ Checklist de reel completo: SÍ
☐ Aprobado por Daniel: SÍ / NO

PIEZA C — 3 STORIES
☐ Story 1: hero photo + hook + elemento interactivo (encuesta/sondaje)
☐ Story 2: clip de proceso o detalle + texto de contexto
☐ Story 3: CTA directo — número en dorado visible
☐ Las 3 en secuencia preparadas
☐ Aprobadas por Daniel: SÍ / NO

PIEZA D — CARRUSEL ANTES/DESPUÉS
☐ Slide 1: hero (score ≥90) + hook + flechas de deslizamiento
☐ Slide 2: foto "antes" desaturada + texto "Avant"
☐ Slides 3–5: fotos de calidad (score ≥80) con copy mínimo
☐ Slide 6: CTA en verde oscuro + número en dorado + logo
☐ Consistencia de color grade entre slides 3–5
☐ Revisado en teléfono (no en desktop): SÍ
☐ Aprobado por Daniel: SÍ / NO

PIEZA E — REMARKETING
☐ Misma imagen del Hero Post (no producir nueva)
☐ Copy DIFERENTE al del Hero Post
☐ Tono: urgencia elegante (no agresivo)
☐ Audiencia: warm (visitors + video viewers)
☐ Presupuesto: $20–30 CAD/día para primer test
☐ Duración del test: 7 días
☐ KPI de éxito: CPL <$80 CAD
☐ Aprobado por Daniel: SÍ / NO

PUBLICACIÓN
☐ Hero Post: publicado a las ___:___ en [fecha]
☐ Reel: publicado a las ___:___ en [fecha]
☐ Stories: publicadas a las ___:___ en [fecha]
☐ Carrusel: publicado a las ___:___ en [fecha]
☐ Ad Remarketing: activado en [fecha], presupuesto $___/día

MÉTRICAS A REVISAR (48h después de publicar)
☐ Hero Post: alcance ___ / engagement ___ / CTA clicks ___
☐ Reel: vistas ___ / completes ___ / shares ___
☐ Carrusel: saves ___ / slides promedio vistas ___
☐ Ad Remarketing: impresiones ___ / CPL ___ CAD

DECISIÓN FINAL:
☐ Si CPL Remarketing <$80 → escalar presupuesto a $40–60 CAD/día
☐ Si CPL Remarketing >$100 → pausar → cambiar copy → reintentar
☐ Registrar en CEO_DASHBOARD_TEMPLATE del día correspondiente
════════════════════════════════════════════════════════════════
```

---

## ORDEN DE PRODUCCIÓN RECOMENDADO (por eficiencia)

```
DÍA 1 — MAÑANA (90 min):
  07:00 → Paso 0: evaluar las 10 fotos con Claude Code (30 min)
  08:00 → Identificar hero + material para cada pieza
  08:30 → Retocar hero photo en Lightroom (30 min)
  09:00 → REUNIÓN FIJA — no tocar la producción

DÍA 1 — TARDE (90 min):
  14:00 → Pieza A: composición + copy (30 min) → ¿score ≥90? → si SÍ → aprobar
  14:30 → Pieza C: 3 Stories desde Pieza A ya hecha (25 min)
  15:00 → Pieza E: remarkt copy + configuración de ad (40 min)

DÍA 2 — MAÑANA (130 min):
  09:00 → Pieza B: cortar clips + sincronizar música (90 min)
  10:30 → Testeo del hook con 1–2 personas
  11:00 → Exportar + checklist de reel

DÍA 2 — TARDE (60 min):
  14:00 → Pieza D: carrusel 6 slides (60 min)
  15:00 → Revisión final de todas las piezas con checklist
  17:30 → Publicar Hero Post
  17:35 → Publicar Stories

DÍA 3:
  17:00 → Publicar Reel
  18:00 → Publicar Carrusel (opcional — puede esperar al jueves)
  Activar ad de Remarketing

REVISIÓN (DÍA 5 — 48h después del Reel):
  Revisar métricas. Registrar en CEO_DASHBOARD_TEMPLATE.
```

---

## REGISTRO DE CAMPAÑAS PRODUCIDAS

*(Completar después de cada campaña — este archivo se reutiliza)*

| # | Fecha | Proyecto | Hero Score | CPL Final | Leads generados | Nota |
|---|-------|---------|-----------|----------|----------------|------|
| 1 | | | /100 | CAD | | |
| 2 | | | /100 | CAD | | |
| 3 | | | /100 | CAD | | |

---

**Referencia FLOAT V2:** `05_MARKETING/FLOAT_V2_PREMIUM/`
**Score de evaluación:** `03_PREMIUM_VISUAL_SCORE.md`
**Música:** `04_MUSIC_LIBRARY_SYSTEM.md`
**Estándar editorial:** `05_MAGAZINE_EDITORIAL_STANDARD.md`
