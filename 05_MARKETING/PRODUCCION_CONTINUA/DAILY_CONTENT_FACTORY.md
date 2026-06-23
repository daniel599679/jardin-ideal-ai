# DAILY CONTENT FACTORY
**Sistema de Producción Continua — Jardín Ideal**
**Versión:** 1.0 | **Fecha:** 2026-06-23
**Integración:** FLOAT V2 Premium obligatoria
**Regla absoluta:** Todo material pasa por PREMIUM_VISUAL_SCORE antes de entrar al pipeline.

---

## QUÉ ES ESTE SISTEMA

La Fábrica de Contenido Diaria convierte cualquier entrada de material bruto (fotos, videos, audios, ideas) en piezas de contenido listas para publicar — clasificadas, priorizadas y en formato FLOAT V2 Premium.

**El sistema no descansa.** Cada día que hay un proyecto terminado, hay contenido producible.

---

## PARTE 1 — ENTRADA DE MATERIAL

### 1.1 Tipos de entrada aceptados

#### FOTOS
```
CARPETA DE DEPÓSITO: Drive / INBOX_MARKETING / [FECHA] / [PROYECTO]

FORMATOS ACEPTADOS:
  ✓ JPG / JPEG — resolución mínima 2400 × 3200 px (equivalente 12 MP)
  ✓ HEIC (iPhone) — convertir a JPG antes de procesar
  ✓ RAW (CR2, NEF, ARW) — preferido para proyectos hero

FORMATOS RECHAZADOS:
  ✗ Screenshots de WhatsApp o Instagram (calidad degradada, metadatos perdidos)
  ✗ Capturas de pantalla de videos — usar el frame exportado directamente
  ✗ Fotos recibidas por email comprimidas automáticamente por el cliente de email

METADATOS REQUERIDOS (añadir al nombre del archivo si no están en EXIF):
  Formato de nombre: YYYY-MM-DD_PROYECTO_ANGULO_SECUENCIA
  Ejemplo: 2026-06-23_PUSCHAK_PANORAMICO_01.jpg
```

#### VIDEOS / CLIPS
```
CARPETA: Drive / INBOX_MARKETING / [FECHA] / [PROYECTO] / VIDEO

FORMATOS ACEPTADOS:
  ✓ MP4 H.264 — estándar
  ✓ MOV (iPhone / GoPro) — convertir a MP4 antes del montaje
  ✓ Resolución mínima: 1080p @ 30fps
  ✓ Resolución preferida: 4K @ 30fps (más opciones de recorte en edición)

TIPOS DE CLIPS ÚTILES:
  • Time-lapse de instalación (3–6h comprimidas a 30s)
  • B-roll de proceso (colocación de pavé, nivelación, compactación)
  • Clip del resultado final caminando hacia la propiedad
  • Close-up de texturas y detalles (juntas, bordes, materiales)
  • Testimonio del cliente en el proyecto terminado (requiere consentimiento)
```

#### AUDIOS / IDEAS DE VOZ
```
CARPETA: Drive / INBOX_MARKETING / IDEAS_VOZ

FORMATO: Nota de voz WhatsApp, M4A, MP3 (cualquier calidad — es para transcripción)

QUÉ DEPOSITAR AQUÍ:
  • Descripción verbal del proyecto ("el cliente quería X, hicimos Y, quedó así...")
  • Idea de hook para reel dictada en el momento
  • Testimonio del cliente grabado con el teléfono en sitio
  • Observación técnica para contenido educativo ("hay que saber que en Quebec el pavé...")

PROCESO:
  1. Transcribir la nota con Claude o Whisper
  2. Convertir en copy o brief según el tipo de contenido
  3. Archivar el audio original en Drive
```

#### CAPTURAS DE PANTALLA
```
CARPETA: Drive / INBOX_MARKETING / CAPTURAS

TIPOS ACEPTADOS:
  • Reseña de Google 5 estrellas → TESTIMONIO
  • DM de cliente con felicitación → PRUEBA SOCIAL
  • Screenshot de métricas Meta Ads (CTR, CPL récord) → EDUCATIVO / AUTORIDAD
  • Conversación con lead que ilustra una objeción → EDUCATIVO

PROCESO DE LIMPIEZA ANTES DE USAR:
  1. Recortar: solo la parte relevante, sin interfaz de teléfono
  2. Anonimizar: cubrir apellido y foto del cliente si no hay consentimiento
  3. Verificar: que la información es verídica y no descontextualizada
```

---

### 1.2 Protocolo de depósito en campo (equipo de obra)

El jefe de obra deposita material siguiendo este protocolo al final de cada jornada:

```
AL TERMINAR UNA ETAPA DEL PROYECTO:
  1. Abrir la app de Drive en el teléfono
  2. Ir a: INBOX_MARKETING / [FECHA_HOY] / [NOMBRE_PROYECTO]
  3. Subir todas las fotos del día
  4. Añadir una nota de voz: "Proyecto [X], fecha [Y], etapa [Z]. [Descripción breve]."
  5. Si hay video: subir el clip
  6. Si el cliente dice algo positivo → grabar audio con permiso

AL TERMINAR EL PROYECTO COMPLETAMENTE:
  → Seguir el checklist_cierre_proyecto.md (Paso 2 y Paso 6)
  → Marcar la carpeta con la etiqueta "CIERRE" para priorización
```

---

## PARTE 2 — CLASIFICACIÓN AUTOMÁTICA

### 2.1 Tipos de contenido y criterios de clasificación

#### 🥇 HERO
```
¿Qué es? La mejor foto o video del proyecto. El contenido que define la percepción de marca.
¿Cuándo clasificar como HERO?
  ✓ La imagen tiene VISUAL_SCORE ≥ 90/100 (PREMIUM_VISUAL_SCORE)
  ✓ Muestra el resultado final en su máxima expresión
  ✓ Genera "wow" inmediato al verla
  ✓ Podría aparecer en la página de Techo-Bloc sin sentirse inferior

¿Qué se produce a partir de HERO?
  → Hero Image para Meta Ads (awareness)
  → Primer slide de carrusel
  → Thumbnail del reel
  → Post de feed permanente
```

#### 📚 EDUCATIVO
```
¿Qué es? Contenido que enseña algo útil sobre paisajismo, materiales o mantenimiento.
¿Cuándo clasificar como EDUCATIVO?
  ✓ Hay una observación técnica documentada (audio o texto)
  ✓ Hay una pregunta frecuente del cliente que merece respuesta pública
  ✓ Hay un error común que Jardín Ideal evita y puede mostrar cómo
  ✓ Hay datos de rendimiento o durabilidad de un material

¿Qué se produce?
  → Post educativo tipo "Voici pourquoi..." / "Ce que vous devez savoir sur..."
  → Carrusel de pasos o consejos
  → Reel tipo tutorial corto (proceso de trabajo)
  → Story con pregunta y respuesta (formato encuesta)
```

#### 🌟 PRUEBA SOCIAL
```
¿Qué es? Evidencia de que otros clientes confían en Jardín Ideal y están satisfechos.
¿Cuándo clasificar como PRUEBA SOCIAL?
  ✓ Reseña de Google ≥4 estrellas con texto
  ✓ DM de felicitación o foto compartida por el cliente
  ✓ Número de proyectos terminados este mes / temporada / año
  ✓ Cliente que refirió a otro cliente
  ✓ Zona premium nueva donde Jardín Ideal acaba de instalar

¿Qué se produce?
  → Post "Merci [Prénom] pour votre confiance"
  → Story con cita textual del cliente (con permiso)
  → Dato de impacto ("127 projets réalisés à Laval")
  → Reel de testimonios editados
```

#### 🎁 OFERTA
```
¿Qué es? Contenido con CTA directo a conversión — llamada, formulario, soumission.
¿Cuándo clasificar como OFERTA?
  ✓ Hay slots disponibles en el calendario de instalación
  ✓ Es inicio o fin de temporada (urgencia natural)
  ✓ Hay un proyecto con fecha de inicio próxima que puede mostrarse
  ✓ Hay un descuento o condición especial aprobada por Daniel

¿Qué se produce?
  → Meta Ad directo con CTA "Obtenez votre soumission"
  → Story con countdown o fechas disponibles
  → Post de urgencia elegante ("L'agenda de juillet se remplit.")
```

#### 💬 TESTIMONIO
```
¿Qué es? La voz directa del cliente — más persuasiva que cualquier copy.
¿Cuándo clasificar como TESTIMONIO?
  ✓ Audio o video grabado en sitio con el cliente
  ✓ Texto transcrito de una reseña o DM con identificación confirmada
  ✓ Foto del cliente en el proyecto terminado (con consentimiento firmado)

¿Qué se produce?
  → Video testimonio editado (si hay clip)
  → Post con cita textual sobre foto del proyecto
  → Story "Ce que nos clients disent"
  → Ad de retargeting (testimonios convierten más en remarketing)
```

#### 🔄 ANTES/DESPUÉS
```
¿Qué es? El formato con mayor conversión de Jardín Ideal. Muestra la transformación.
¿Cuándo clasificar como ANTES/DESPUÉS?
  ✓ Hay foto del estado previo Y foto del resultado final del mismo ángulo
  ✓ El contraste es evidente en menos de 2 segundos
  ✓ Ambas fotos tienen calidad aceptable (antes puede ser score 60+)

¿Qué se produce?
  → Reel de transformación (formato más popular de la cuenta)
  → Carrusel antes/après (slide 1: antes, slides 2-4: après y detalles)
  → Meta Ad con split image o video de reveal
  → Story swipe-up "Avant → Après"
```

---

### 2.2 Árbol de decisión para clasificar

```
¿Hay foto del resultado final?
  SÍ → ¿VISUAL_SCORE ≥ 90/100?
    SÍ → HERO (candidato a todo)
    NO (75-89) → ¿Hay foto del "antes"?
      SÍ → ANTES/DESPUÉS (usar como segundo frame)
      NO → EDUCATIVO o PRUEBA SOCIAL si el contenido lo permite
  NO → ¿Hay audio/texto del cliente?
    SÍ → TESTIMONIO o PRUEBA SOCIAL
    NO → ¿Hay observación técnica?
      SÍ → EDUCATIVO
      NO → ¿Hay urgencia de agenda?
        SÍ → OFERTA
        NO → Material insuficiente — solicitar más material
```

---

## PARTE 3 — PRIORIDAD DE PRODUCCIÓN DIARIA

### 3.1 Jerarquía de producción

```
PRIORIDAD 1 — ANTES/DESPUÉS con HERO (score ≥90 en el après)
  Por qué: máxima conversión, mayor alcance orgánico, mejor CPL en Meta Ads
  Tiempo de producción: 45–90 minutos
  Produce: Reel + Carrusel + Meta Ad + Story

PRIORIDAD 2 — HERO solo (sin "antes")
  Por qué: construye aspiración de marca, alimenta las campañas de awareness
  Tiempo de producción: 20–40 minutos
  Produce: Post feed + Meta Ad + Story + thumbnail reel

PRIORIDAD 3 — TESTIMONIO
  Por qué: prueba social directa — la voz del cliente vende mejor que el copy
  Tiempo de producción: 15–30 minutos
  Produce: Post + Story + Ad retargeting

PRIORIDAD 4 — EDUCATIVO
  Por qué: construye autoridad, posiciona a Jardín Ideal como expertos
  Tiempo de producción: 20–30 minutos
  Produce: Carrusel + Post educativo

PRIORIDAD 5 — OFERTA
  Por qué: conversión directa cuando hay capacidad de agenda disponible
  Tiempo de producción: 10–20 minutos
  Produce: Meta Ad + Story + Post orgánico

PRIORIDAD 6 — PRUEBA SOCIAL
  Por qué: solidifica la confianza en cuentas que ya siguen a Jardín Ideal
  Tiempo de producción: 10–20 minutos
  Produce: Post + Story
```

### 3.2 Regla de la semana balanceada

```
Distribución semanal objetivo:
  2 × ANTES/DESPUÉS o HERO → Lunes y Miércoles (días de mayor alcance)
  1 × TESTIMONIO o PRUEBA SOCIAL → Jueves
  1 × EDUCATIVO → Martes
  1 × OFERTA → Viernes
  1 × BEHIND THE SCENES → Sábado
  1 × INSPIRACIÓN → Domingo
```

---

## PARTE 4 — EVALUACIÓN PREMIUM_VISUAL_SCORE (gate de entrada)

Antes de clasificar cualquier pieza en el pipeline, evaluar con los 5 bloques:

```
EVALUACIÓN RÁPIDA (3 minutos por foto):
  Composición (25pts): ¿Sujeto dominante? ¿Profundidad? ¿Sin distractores?
  Luz (25pts): ¿Hora dorada? ¿Sin sombras duras? ¿Cielo con detalle?
  Color (20pts): ¿Paleta alineada? ¿Sin sobreretoque?
  Limpieza (15pts): ¿Sin personas/herramientas? ¿Set limpio?
  Impacto (15pts): ¿Genera "wow"? ¿Memorable?

DECISIÓN:
  ≥ 90 → HERO → pipeline completo
  75–89 → SECUNDARIO → carrusel, stories, antes del "après"
  60–74 → INTERNO → referencia de proyecto, no publicar
  < 60 → DESCARTAR
```

**Referencia completa:** `05_MARKETING/FLOAT_V2_PREMIUM/03_PREMIUM_VISUAL_SCORE.md`

---

## PARTE 5 — INTEGRACIÓN FLOAT V2 PREMIUM

| Módulo | Cuándo se activa en este flujo |
|--------|-------------------------------|
| `01_HERO_IMAGE_FACTORY.md` | Al seleccionar el hero image del proyecto |
| `02_EMOTIONAL_REEL_ENGINE.md` | Al producir cualquier reel (arquitectura 5 fases) |
| `03_PREMIUM_VISUAL_SCORE.md` | Gate de entrada — SIEMPRE, antes de clasificar |
| `04_MUSIC_LIBRARY_SYSTEM.md` | Al producir reels (selección de emoción → biblioteca) |
| `05_MAGAZINE_EDITORIAL_STANDARD.md` | Al escribir cualquier copy (hook, overlay, caption) |
| `GLOBAL_CONTENT_GUARDRAILS.md` | Reglas base que aplican a TODO el contenido |

---

## RESUMEN — LA FÁBRICA EN UNA FRASE

> Material entra → se evalúa con el score → se clasifica → se prioriza → se produce en formato FLOAT V2 Premium → pasa al DAILY_CONTENT_QUEUE para programación.

---

*DAILY CONTENT FACTORY v1.0 — Sistema de Producción Continua — Jardín Ideal*
*05_MARKETING/PRODUCCION_CONTINUA/DAILY_CONTENT_FACTORY.md*
