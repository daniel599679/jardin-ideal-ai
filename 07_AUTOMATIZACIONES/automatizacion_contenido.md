# AUTOMATIZACIONES — CONTENIDO Y REDES SOCIALES
**Programación, publicación y distribución de contenido**

---

## Principio General
El contenido constante genera confianza. La automatización garantiza que el contenido llegue a tiempo aunque el equipo esté en obra. La regla: crear en bloques, programar con anticipación, nunca publicar en el último minuto.

---

## FLUJO 1 — Programación semanal de contenido (FLOAT V2 Premium integrado)

```
DISPARADOR
└── Bloque de contenido del calendario: Miércoles 10:00 AM

PROCESO (manual con herramientas de programación)
├── 0. GATE FLOAT V2 PREMIUM — ejecutar antes de todo:
│       ¿Hay fotos con VISUAL_SCORE ≥ 90/100 disponibles? (evaluar con 03_PREMIUM_VISUAL_SCORE.md)
│       Si NO → no programar hero/reel. Solo carrusel con score ≥75 si existe.
│       Si SÍ → continuar con el flujo.
├── 1. Seleccionar las fotos de la semana — solo de la carpeta DISPONIBLE (score ≥90 → hero, score 75-89 → secundario)
├── 2. Redactar los textos siguiendo el MAGAZINE_EDITORIAL_STANDARD (05_MARKETING/FLOAT_V2_PREMIUM/05)
│       Hook: máx. 8 palabras | Voz: declarativa | Sin "meilleur/qualité/professionnel" sin dato
├── 3. Programar en Meta Business Suite o Buffer:
│       Lunes: Antes/Después (hero ≥90pts)
│       Martes: Consejo técnico o proceso
│       Miércoles: Carrusel de detalle
│       Jueves: Testimonio o prueba social
│       Viernes: Inspiración / Reel
└── 4. Verificar que todas las publicaciones de la semana siguiente estén programadas

RESULTADO
└── Semana siguiente 100% cubierta de contenido sin intervención diaria
    y con estándar visual ≥90/100 en todas las publicaciones hero
```

**Herramienta primaria:** Meta Business Suite (gratuito, publica en Instagram y Facebook simultáneamente)
**Herramienta alternativa:** Buffer (~15 CAD/mes) o Later (~20 CAD/mes) — mejor interfaz visual

---

## FLUJO 2 — Publicación automática multi-plataforma

```
DISPARADOR
└── Se sube una publicación a Instagram (manualmente o programada)

ACCIÓN AUTOMÁTICA (si se usa Make/Zapier)
└── La misma publicación se replica automáticamente a Facebook
    con el mismo copy y hashtags

HERRAMIENTA NATIVA (sin Make)
└── Meta Business Suite permite programar en ambas plataformas
    en un solo paso — no requiere automatización externa
```

---

## FLUJO 3 — Alerta de foto de obra disponible para contenido (FLOAT V2 Premium integrado)

```
DISPARADOR
└── Equipo de obra sube fotos a la carpeta INBOX_MARKETING (Drive/Dropbox)

ACCIÓN — PASO 1: Evaluación Premium (antes de notificar a Marketing)
└── AGENTE_CONTROL_CALIDAD_MAGAZINE evalúa cada foto con PREMIUM_VISUAL_SCORE
    → Score ≥ 90/100: mover a carpeta DISPONIBLE/HERO
    → Score 75–89:    mover a carpeta DISPONIBLE/SECUNDARIO
    → Score < 75:     mover a carpeta RECHAZADO (no publicar)

ACCIÓN — PASO 2: Notificación a Marketing (solo si hay material aprobado)
└── Notificación automática al agente de Marketing:
    "📸 FOTOS EVALUADAS — FLOAT V2 PREMIUM
     Proyecto: [Nombre del proyecto]
     Hero (≥90pts): [N] fotos → candidatas para reel y Meta Ads hero
     Secundario (75-89pts): [N] fotos → candidatas para carrusel
     Rechazadas (<75pts): [N] fotos → no usar
     Carpeta: [Link directo a DISPONIBLE/HERO]
     → Activar pipeline FLOAT V2: QC → Director → Montaje → Marketing"
```

**Herramienta:** Google Drive + Make.com (Watch Files trigger) → WhatsApp notificación
**Alternativa manual:** Carpeta "INBOX_MARKETING" en Drive que el agente evalúa con PREMIUM_VISUAL_SCORE cada miércoles antes del bloque de contenido

---

## FLUJO 4 — Recordatorio de respuesta a comentarios

```
DISPARADOR
└── Lunes, Miércoles, Viernes a las 12:00 PM

ACCIÓN
└── Recordatorio al responsable de redes:
    "💬 REVISAR REDES AHORA
     → Comentarios sin responder en Instagram
     → Comentarios sin responder en Facebook
     → DMs pendientes
     Tiempo estimado: 15–20 minutos"
```

---

## FLUJO 5 — Boost automático de publicaciones con buen engagement

```
DISPARADOR
└── Publicación orgánica supera umbral de engagement en 24h:
    - >50 likes O
    - >10 comentarios O
    - >20 compartidos

ACCIÓN
└── Notificación a Daniel:
    "🚀 PUBLICACIÓN CON ALTO ENGAGEMENT — BOOST RECOMENDADO
     Publicación: [Título o descripción]
     Likes: ___ | Comentarios: ___ | Alcance: ___
     → Boostar con 20–50 CAD durante 3 días para amplificar
     Audiencia sugerida: misma del anuncio mejor rendimiento"
```

**Esta automatización convierte el mejor contenido orgánico en publicidad pagada de forma eficiente.** El contenido que ya demostró engagement convierte mejor que el creado directamente para ads.

---

## FLUJO 6 — Reutilización de contenido top (cada 3 meses)

```
DISPARADOR
└── Primer lunes de cada trimestre

ACCIÓN
└── Reporte automático con top 5 publicaciones del trimestre anterior:
    "♻️ CONTENIDO TOP PARA REUTILIZAR
     (Las publicaciones con mayor alcance de los últimos 3 meses)
     
     1. [Descripción] — Alcance: ___ | Engagement: ___%
     2. [Descripción] — Alcance: ___ | Engagement: ___%
     ...
     
     → Republica con foto nueva o actualiza el texto para refrescar"
```

**Regla:** El contenido top puede reutilizarse con variaciones cada 3–6 meses sin que la audiencia lo perciba como repetido, especialmente en cuentas de menos de 10,000 seguidores.

---

## FLUJO 7 — Calendario de contenido estacional (programado anual)

Contenido específico a programar con anticipación según la época:

```
ENERO–FEBRERO — "Réservez pour le printemps"
├── Publicaciones: proyectos del año anterior (los mejores)
├── Mensajes: urgencia de reserva anticipada
└── Ads: campaña de reservas con CTA "Réservez maintenant"

MARZO — "La saison recommence"
├── Publicaciones: "Notre équipe est prête pour la saison 2026"
├── Mensajes: disponibilidades limitadas
└── Ads: máxima inversión, temporada arranca

ABRIL–MAYO — "Transformez votre extérieur"
├── Publicaciones: proyectos en proceso (stories de obra diarias)
├── Mensajes: "Voyez la transformation en temps réel"
└── Ads: antes/después de proyectos recientes

JUIN–JUILLET — "Profitez de l'été"
├── Publicaciones: proyectos terminados (cursos, terrazas, piscinas)
├── Mensajes: resultados y calidad de vida
└── Ads: piscinas y cursos arrière

AOÛT — "Dernières disponibilités"
├── Publicaciones: urgencia + testimonios de la temporada
├── Mensajes: "Il reste [N] créneaux en septembre"
└── Ads: escasez real de agenda

SEPTIEMBRE–OCTOBRE — "Préparez le printemps prochain"
├── Publicaciones: consejos de entretien otoñal
├── Mensajes: proyectos de otoño + reservas 2027
└── Ads: reducir presupuesto progresivamente
```

---

## Stack de Herramientas para Contenido

| Herramienta | Para qué | Costo |
|---|---|---|
| Meta Business Suite | Programar Instagram + Facebook en 1 paso | Gratuito |
| Canva Pro | Crear diseños con templates de marca | ~17 CAD/mes |
| Later o Buffer | Calendario visual + analytics | 15–20 CAD/mes |
| Make.com | Notificaciones de fotos disponibles | incluido en plan |
| Google Drive | Carpeta compartida de fotos de obra | Gratuito |
| CapCut | Edición rápida de Reels y videos | Gratuito |

**Costo total estimado:** ~35–50 CAD/mes para el stack completo de contenido.

---

## Protocolo de Carpetas en Drive

```
📁 Jardín Ideal — Contenido
├── 📁 INBOX_MARKETING (fotos nuevas sin procesar)
│   └── El equipo de obra sube aquí — sin organizar
├── 📁 PUBLICADO
│   └── Fotos ya usadas en redes — organizadas por mes
├── 📁 DISPONIBLE
│   └── Fotos aprobadas, listas para usar
└── 📁 ARCHIVO
    └── Proyectos pasados — fuente de contenido evergreen
```

**Regla:** Mover las fotos de INBOX a DISPONIBLE o PUBLICADO dentro de las 48h. Un INBOX que crece sin revisarse pierde valor — las fotos de obra se vuelven viejas rápido.

---

## Registro de Automatizaciones Implementadas

```
FLUJO 1 — Programación semanal de contenido
Estado: ⬜ / ⚙️ / ✅  |  Herramienta: ___  |  Desde: ___

FLUJO 2 — Publicación multi-plataforma
Estado: ⬜ / ⚙️ / ✅  |  Herramienta: ___  |  Desde: ___

FLUJO 3 — Alerta de fotos disponibles
Estado: ⬜ / ⚙️ / ✅  |  Herramienta: ___  |  Desde: ___

FLUJO 4 — Recordatorio respuesta comentarios
Estado: ⬜ / ⚙️ / ✅  |  Herramienta: ___  |  Desde: ___

FLUJO 5 — Boost de publicaciones con engagement alto
Estado: ⬜ / ⚙️ / ✅  |  Herramienta: ___  |  Desde: ___

FLUJO 6 — Reutilización de contenido top trimestral
Estado: ⬜ / ⚙️ / ✅  |  Herramienta: ___  |  Desde: ___
```
