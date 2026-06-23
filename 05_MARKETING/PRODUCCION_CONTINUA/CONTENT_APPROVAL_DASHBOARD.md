# CONTENT APPROVAL DASHBOARD
**Panel de Aprobación de Contenido — Jardín Ideal**
**Versión:** 1.0 | **Fecha:** 2026-06-23
**Integración:** FLOAT V2 Premium + DAILY_CONTENT_QUEUE
**Propósito:** Estado centralizado de todo el contenido en producción — quién debe hacer qué y cuándo.

---

## LOS 6 ESTADOS DEL CONTENIDO

```
PENDIENTE        → Pieza en cola, material identificado, aún no se inicia la producción
EN PRODUCCIÓN    → Agente está produciendo activamente la pieza
REVISIÓN HUMANA  → Producción completa, esperando aprobación de Daniel
APROBADO         → Daniel aprobó la pieza, lista para programar
PROGRAMADO       → La pieza está en Meta Business Suite / Buffer con fecha y hora
PUBLICADO        → Pieza live en plataformas
```

---

## FLUJO DE ESTADOS

```
PENDIENTE
    ↓
    ¿Material tiene VISUAL_SCORE ≥ 90/100 (o ≥75 para stories)?
    SÍ → asignar al agente correspondiente
    NO → queda en PENDIENTE hasta nueva sesión fotográfica
    ↓
EN PRODUCCIÓN
    ↓
    ¿La pieza cumple todos los requisitos del GLOBAL_CONTENT_GUARDRAILS?
    SÍ → pasar a REVISIÓN HUMANA
    NO → corregir en la misma sesión → luego REVISIÓN HUMANA
    ↓
REVISIÓN HUMANA
    ↓
    Daniel revisa (tiempo máximo: 2 horas desde la notificación)
    APRUEBA → APROBADO
    PIDE CAMBIOS → volver a EN PRODUCCIÓN con instrucciones específicas
    RECHAZA → PENDIENTE con nota de qué falta
    ↓
APROBADO
    ↓
    Agente programa en Meta Business Suite / Buffer según hora óptima
    ↓
PROGRAMADO
    ↓
    [publicación automática a la hora programada]
    ↓
PUBLICADO → registrar en el historial semanal
```

---

## CRITERIOS DE REVISIÓN HUMANA

### Qué SIEMPRE requiere revisión de Daniel

```
REVISIÓN OBLIGATORIA (no delegar):
  ✓ Hero Posts (feed permanente — impacto en percepción de marca)
  ✓ Reels principales (mayor visibilidad)
  ✓ Cualquier pieza de Meta Ads que gaste presupuesto
  ✓ Testimonios de clientes (verificar que el cliente aprobó el uso)
  ✓ Cualquier mención de precios, descuentos u ofertas especiales
  ✓ Contenido con personas identificables (verificar consentimiento)
  ✓ Mensajes de urgencia o escasez (verificar que sean verídicos)
```

### Qué puede aprobarse sin Daniel (agente autónomo)

```
APROBACIÓN AUTÓNOMA (agente puede publicar directamente):
  ✓ Stories educativas sin imagen de proyecto (solo texto o encuesta)
  ✓ Respuestas a comentarios y DMs (dentro del protocolo de respuesta)
  ✓ Reutilización de contenido ya aprobado anteriormente (mismo asset, nuevo copy aprobado)
  ✓ Publicaciones de "behind the scenes" del equipo sin información sensible
```

---

## PLANTILLA DE REGISTRO DIARIO

Usar cada día para documentar el estado de las 5 piezas:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CONTENT APPROVAL DASHBOARD — [FECHA]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PIEZA 1 — HERO POST
  Estado:         [ ] PENDIENTE  [ ] EN PROD  [ ] REV. HUMANA  [ ] APROBADO  [ ] PROGRAMADO  [ ] PUBLICADO
  Asset:          ________________ | Score: ___ / 100
  Hook:           ________________
  Producido por:  ________________ | A las: ___:___
  Enviado a Daniel: ___:___ | Aprobado: ___:___
  Programado para: [fecha] [hora]
  Publicado: ___:___
  Notas: ________________

PIEZA 2 — REEL EMOCIONAL
  Estado:         [ ] PENDIENTE  [ ] EN PROD  [ ] REV. HUMANA  [ ] APROBADO  [ ] PROGRAMADO  [ ] PUBLICADO
  Tipo:           AVANT/APRÈS / PROCESO / PORTFOLIO
  Duración:       ___ seg | Score hero: ___ / 100
  Música:         ________________ (LUFS verificados: ☐)
  Producido por:  ________________ | A las: ___:___
  Enviado a Daniel: ___:___ | Aprobado: ___:___
  Programado para: [fecha] [hora]
  Publicado: ___:___
  Notas: ________________

PIEZA 3 — STORY
  Estado:         [ ] PENDIENTE  [ ] EN PROD  [ ] APROBADO  [ ] PROGRAMADO  [ ] PUBLICADO
  Tipo:           ________________
  Texto:          ________________
  Sticker:        ________________
  Producido por:  ________________ | A las: ___:___
  ¿Requiere Daniel? [ ] SÍ  [ ] NO
  Programado para: [fecha] [hora]
  Publicado: ___:___
  Notas: ________________

PIEZA 4 — POST EDUCATIVO
  Estado:         [ ] PENDIENTE  [ ] EN PROD  [ ] REV. HUMANA  [ ] APROBADO  [ ] PROGRAMADO  [ ] PUBLICADO
  Tema:           ________________
  Formato:        CARRUSEL ___ slides / IMAGEN ÚNICA
  Titular:        ________________
  Producido por:  ________________ | A las: ___:___
  ¿Requiere Daniel? [ ] SÍ  [ ] NO (si es carrusel con dato nuevo → SÍ)
  Programado para: [fecha] [hora]
  Publicado: ___:___
  Notas: ________________

PIEZA 5 — REMARKETING
  Estado:         [ ] PENDIENTE  [ ] EN PROD  [ ] REV. HUMANA  [ ] APROBADO  [ ] PROGRAMADO  [ ] PUBLICADO
  Tipo:           A / B / C / D
  Audiencia:      ________________
  Asset:          ________________ | Score: ___ / 100
  Presupuesto:    ___ CAD/día × ___ días
  Producido por:  ________________ | A las: ___:___
  Enviado a Daniel: ___:___ | Aprobado: ___:___
  Activo desde:   ___:___ | Activo hasta: ___
  Notas: ________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RESUMEN DEL DÍA:
  Piezas completadas y publicadas: ___ / 5
  Piezas en espera de Daniel:      ___
  Piezas bloqueadas (sin material): ___
  Alertas: ________________
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## REGISTRO SEMANAL CONSOLIDADO

Archivar cada domingo al cierre:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RESUMEN SEMANAL DE PRODUCCIÓN — Semana [N], [FECHA_INICIO] – [FECHA_FIN]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PRODUCCIÓN:
  Total piezas generadas:       ___
  Total piezas publicadas:      ___
  Total piezas pendientes:      ___
  Total piezas rechazadas:      ___ (y razón: _______________)

CALIDAD VISUAL:
  Score promedio de los heroes: ___ / 100
  Piezas con score <90 usadas como hero: ___ (debe ser 0)
  Material nuevo ingresado esta semana: ___ fotos / ___ videos

RENDIMIENTO (si hay datos):
  Reel con más alcance: ________________ (alcance: ___)
  Post con más engagement: ________________ (engagement: ___)
  Ad con mejor CPL: ________________ (CPL: ___ CAD)

APROBACIONES:
  Tiempo promedio Daniel responde desde notificación: ___ minutos
  Piezas que requirieron más de 1 revisión: ___

PRÓXIMA SEMANA:
  Material disponible para producir: ___ fotos / ___ videos
  Proyectos con cierre esta semana (candidatos para contenido): ________________
  Temas prioritarios: ________________
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## PROTOCOLO DE NOTIFICACIÓN A DANIEL

### Cuándo notificar

```
NOTIFICACIÓN INMEDIATA (WhatsApp):
  → Pieza HERO o REEL lista para revisión
  → Pieza de REMARKETING lista para lanzar
  → Problema bloqueante (no hay material ≥90/100 para publicar hoy)
  → Pieza con información sensible (precios, descuentos, personas)

NOTIFICACIÓN DIARIA BATCH (resumen 11:00 AM):
  → Piezas de STORY y EDUCATIVO listas para revisión/aprobación
  → Estado general de la cola del día

NOTIFICACIÓN SEMANAL (domingo 17:00):
  → Resumen de producción semanal
  → Alertas de material faltante para la semana siguiente
```

### Formato de notificación

```
FORMATO WHATSAPP — PIEZA LISTA PARA REVISIÓN:
  "📸 [TIPO DE PIEZA] lista para revisión
   Proyecto: [nombre]
   Score visual: [X/100]
   Descripción: [1 línea]
   → Aprobar para publicar [fecha] a las [hora]
   Archivo: [ubicación o link a Drive]"

RESPUESTA DE DANIEL:
  "✅" o "APROBADO" → publicar según lo programado
  "Cambiar [X]" → hacer ajuste y reenviar
  "❌" o "RECHAZADO" → documentar razón y buscar alternativa
```

---

## ALERTAS DEL SISTEMA

```
🔴 ALERTA CRÍTICA — publicar inmediatamente a Daniel:
  • 3 días consecutivos sin Hero Post publicado
  • VISUAL_SCORE de un ad activo bajó a <75/100 (material desactualizado)
  • Comentario negativo en publicación con >1,000 impresiones
  • Error factual en una pieza ya publicada

🟠 ALERTA ALTA — notificar en el batch diario:
  • No hay material ≥90/100 en INBOX para la semana próxima
  • CTR del reel publicado <1% en 48 horas
  • Pieza esperando aprobación de Daniel por >4 horas

🟡 ALERTA MEDIA — mencionar en el resumen semanal:
  • 2 piezas de la semana necesitaron >1 revisión
  • Score promedio de heroes bajó a <92/100
  • Tema educativo repetido sin notarlo
```

---

## INTEGRACIÓN CON FLOAT V2 PREMIUM

Antes de marcar cualquier pieza como "lista para REVISIÓN HUMANA", el agente verifica:

```
CHECKLIST FLOAT V2 PREMIUM — pre-revisión:
  ☐ VISUAL_SCORE documentado (≥90 para hero, ≥75 para secundarias)
  ☐ Hero image producida según HERO_IMAGE_FACTORY
  ☐ Reel (si aplica): arquitectura 5 fases verificada con EMOTIONAL_REEL_ENGINE
  ☐ Música (si aplica): de biblioteca validada, -14 LUFS medidos
  ☐ Copy: hook ≤8 palabras, voz declarativa, sin palabras prohibidas
  ☐ Tipografía: Playfair Display + Montserrat únicamente
  ☐ Colores: solo paleta oficial (#052B16 / #008E3F / #C8A45A / #F5F2EB / #FFFFFF)
  ☐ Dorado #C8A45A: solo en número de teléfono y CTA directo
  ☐ Logo: esquina inferior derecha, tamaño correcto

SI ALGÚN PUNTO FALLA → No enviar a REVISIÓN HUMANA. Corregir primero.
```

---

## HISTORIAL DE CAMBIOS

| Versión | Fecha | Cambio |
|---------|-------|--------|
| 1.0 | 2026-06-23 | Creación del sistema de aprobación con 6 estados |

---

*CONTENT APPROVAL DASHBOARD v1.0 — Sistema de Producción Continua — Jardín Ideal*
*05_MARKETING/PRODUCCION_CONTINUA/CONTENT_APPROVAL_DASHBOARD.md*
