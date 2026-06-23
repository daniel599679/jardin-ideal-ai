# FLOAT V2 — ROADMAP DE LA FÁBRICA CONTINUA DE CONTENIDO
**FLOAT: Fábrica de Leads y Obras a través de Activos Transformados**
**Versión:** 2.0 | **Fecha:** 2026-06-23 | **Sistema:** Jardín Ideal AI System
**Estado base:** Puschak Content Package entregado · Pipeline activo $137K CAD

---

## DECLARACIÓN DE OBJETIVO

FLOAT V2 convierte cada obra terminada en una máquina de generación de leads.
Sin obra activa → no hay excusa para no publicar.
Sin foto aprobada → no hay excusa para no usar el banco de hooks.
Sin reel montado → no hay excusa para no lanzar un carrusel estático.

**La fábrica nunca se detiene. Solo cambia de input.**

---

## ESTADO ACTUAL (FLOAT V1 — baseline)

```
✅ EXISTE    : Proceso manual QC → Brief → Montaje (funciona con Claude, lento)
✅ EXISTE    : 1 Content Package completo (Puschak) listo para edición
✅ EXISTE    : Biblioteca visual organizada (3 proyectos COUR_AVANT + 2 COUR_ARRIÈRE)
✅ EXISTE    : 4 agentes de producción AV documentados
⬜ FALTA     : Captura sistematizada en obra (fotógrafo ≠ operario)
⬜ FALTA     : Clasificación automática de activos por calidad
⬜ FALTA     : Biblioteca de estilos de edición reutilizables
⬜ FALTA     : Banco de hooks testeados con datos de rendimiento
⬜ FALTA     : Score de producción medible semana a semana
⬜ FALTA     : KPIs de la fábrica (distinto de KPIs de campaña)
```

---

## MÓDULO 1 — HERO IMAGE FACTORY

### Objetivo
Producir 1 imagen hero premium lista para Meta Ads por cada proyecto terminado,
dentro de las 48 horas posteriores a la entrega al cliente.

### Inputs
```
· Fotos de cierre de obra (mínimo 5, recibidas por WhatsApp o Drive)
· Autorización verbal del cliente para uso en redes
· Nombre del proyecto y servicio (para nomenclatura)
· MAGAZINE_EDITING_BRIEF.md del proyecto (generado por Claude)
```

### Outputs
```
· 1 imagen hero retouchée — formato META_4x5 (1080×1350px)
· 1 versión STORY_9x16 (1080×1920px)
· 1 versión WEB_1x1 (1080×1080px)
· Archivo PSD maestro con capas (para variaciones futuras)
· Nomenclatura: [PROYECTO]_HERO_META_4x5_v1.jpg
```

### Pipeline de producción
```
DÍA 0 — ENTREGA AL CLIENTE
  └── Equipo en campo → 5 fotos mínimo + 1 video → WhatsApp al responsable

DÍA 1 — MAÑANA SIGUIENTE (antes de 12:00)
  └── Claude analiza fotos → genera MAGAZINE_EDITING_BRIEF en 20 min
  └── Responsable selecciona foto hero → abre Lightroom

DÍA 2 — ANTES DE 18:00
  └── Retouche hero completa → exportar 3 formatos
  └── Subir a 99_EXPORTACIONES/HEROES_APROBADOS/
  └── Notificar al agente de marketing → listo para campaña
```

### Automatizaciones necesarias
```
· Make.com: WhatsApp recibe foto → crea entrada en Google Sheets con estado "INBOX"
· Claude: genera MAGAZINE_EDITING_BRIEF automáticamente al recibir el brief de proyecto
· Notificación: cuando la foto llega a HEROES_APROBADOS → alerta WhatsApp al equipo
```

### Responsable
```
CAPTURA     : Equipo de campo (Carlos / Miguel / Luis)
BRIEF       : Claude (automático)
RETOUCHE    : Daniel o editor designado
VALIDACIÓN  : Daniel
```

### Prioridad: 🔴 1 — CRÍTICA
### Fecha de implementación: **2026-06-27** (esta semana — empezar con Bouchard)

---

## MÓDULO 2 — PROTOCOLO DE CAPTURA EN OBRA

### Objetivo
Garantizar que cada proyecto genere material fotográfico y video utilizable para
contenido premium, sin depender de que el operario "recuerde" sacar el teléfono.

### Problema actual
El equipo en campo captura fotos cuando puede, con el teléfono que tiene, desde el
ángulo más cómodo. El resultado: material desigual, ángulos repetidos, sin avants.
La Hero de Puschak casi fue descartada por los cables eléctricos — un problema
evitable si se tiene el protocolo.

### Inputs
```
· Orden de trabajo del día (proyectos activos)
· Protocolo de captura impreso o en teléfono del responsable de campo
· Teléfono con cámara ≥ 12MP (cualquier iPhone/Samsung moderno es suficiente)
```

### Outputs por proyecto
```
FASE AVANT (antes de comenzar — Día 1, primera hora)
  · 3 fotos del estado original desde ángulos definidos (ver checklist)
  · 1 video panorámico de 30 segundos mostrando el problema actual

FASE PROCESSUS (durante la obra — cada 2 días)
  · 2–3 fotos del proceso más fotogénico (máquinas, pavé en instalación, equipo)
  · 1 video corto de 15–30 segundos de la acción más impactante

FASE APRÈS (al terminar — último día, antes de retirar herramientas)
  · 5–8 fotos del resultado desde los mismos ángulos que el avant
  · 2–3 fotos de detalle (joints, esquinas, transiciones de material)
  · 1–2 videos de recorrido de 30–60 segundos
  · 1 foto vertical 9:16 optimizada para stories (el equipo la toma así)
```

### Checklist de captura — 3 ángulos obligatorios
```
ÁNGULO A — PERSPECTIVA LARGA
  Posición: desde el borde de la propiedad mirando hacia la casa
  Captura: el trabajo completo en un solo frame
  Momento: luz natural (antes de las 10:00 o después de las 15:00)

ÁNGULO B — DÉTAIL MATÉRIAU
  Posición: cámara al nivel del suelo (ras du sol), mirando a lo largo del pavé
  Captura: la textura, los joints, la diferencia de materiales
  Momento: cualquier momento

ÁNGULO C — VERTICAL STORY
  Posición: parado, mirando hacia abajo, capturar el pavé en 9:16 vertical
  Captura: el trabajo desde arriba
  Momento: antes de limpiar el sitio
```

### Reglas de campo
```
REGLA 1: NUNCA enviar fotos desde dentro del vehículo o con la obra sucia.
         Esperar a que el sitio esté limpio.
REGLA 2: La foto avant se toma SIEMPRE, incluso si el cliente no la ve bien.
         Es la mitad del antes/después.
REGLA 3: Sin personas en las fotos (a menos que sea para un testimonio).
         Sin vehículos de trabajo en primer plano.
REGLA 4: Luz natural solamente. Sin flash. Sin noche.
REGLA 5: Si llueve → esperan el próximo día soleado. No publicar fotos con cielo gris.
```

### Automatizaciones necesarias
```
· Recordatorio automático WhatsApp al responsable de campo:
  "📸 HOY: Fotos de cierre [Proyecto X] antes de las 16:00"
  Trigger: proyecto marcado como último día en operaciones_hoy.json
· Formulario simple en WhatsApp: foto → Make → Google Sheets con estado y metadata
```

### Responsable
```
EJECUTAR EN CAMPO : Carlos (responsable de equipo)
SUPERVISAR        : Daniel
RECORDATORIO AUTO : Make.com (cuando esté activo)
```

### Prioridad: 🔴 2
### Fecha de implementación: **2026-06-30** (implementar antes del próximo cierre de obra)

---

## MÓDULO 3 — CLASIFICADOR AUTOMÁTICO DE ACTIVOS

### Objetivo
Eliminar el tiempo de selección manual de fotos. Cada foto que llega a la biblioteca
recibe automáticamente una clasificación de calidad y un rol sugerido.

### Problema actual
Hoy, seleccionar las 7 fotos de Puschak tomó análisis manual foto por foto.
Con 10+ proyectos/mes, eso no es sostenible.

### Inputs
```
· Fotos y videos en carpeta INBOX (Drive o biblioteca local)
· AGENTE_CONTROL_CALIDAD_MAGAZINE (ya existe — el clasificador es su output)
· Metadata del proyecto (servicio, fase: avant/pendant/après)
```

### Outputs
```
· Score QC de 0–100 por cada foto
· Veredicto: ✅ APROBADO / 🟡 CON MEJORAS / 🔴 RECHAZADO
· Rol sugerido: hero / détail / carrusel / story / archivo
· Archivo ASSETS_CLASIFICADOS.json por proyecto con todos los scores
· Carpeta automática: fotos aprobadas → DISPONIBLE/, rechazadas → ARCHIVO/
```

### Pipeline
```
FOTO LLEGA A INBOX
      ↓
Claude (AGENTE_CONTROL_CALIDAD_MAGAZINE) evalúa en lote
      ↓
Genera ASSETS_CLASIFICADOS.json con scores
      ↓
Fotos con score ≥80 → copiar a DISPONIBLE/
Fotos con score 60–79 → copiar a DISPONIBLE/CON_MEJORAS/
Fotos con score <60 → mover a ARCHIVO/RECHAZADAS/
      ↓
Notificación al equipo: "X fotos aprobadas listas para producción"
```

### Estructura de ASSETS_CLASIFICADOS.json
```json
{
  "proyecto": "Puschak",
  "fecha_clasificacion": "2026-06-23",
  "total_evaluados": 10,
  "aprobados": 5,
  "con_mejoras": 2,
  "rechazados": 3,
  "assets": [
    {
      "archivo": "apres_travaux.jpg",
      "score": 87,
      "veredicto": "APROBADO",
      "rol_sugerido": "hero",
      "retouche_requerida": "extensiva",
      "notas": "Cables eléctricos a eliminar. Cielo reemplazar."
    }
  ]
}
```

### Automatizaciones necesarias
```
· Manus: al detectar nuevas fotos en INBOX → activa Claude QC automáticamente
· Script: mueve archivos físicamente según score (Python o PowerShell)
· Notificación WhatsApp: cuando clasificación está lista
```

### Responsable
```
CLASIFICACIÓN : Claude (AGENTE_CONTROL_CALIDAD_MAGAZINE)
AUTOMATIZACIÓN: Manus + Make.com
VALIDACIÓN    : Daniel (revisar la selección propuesta, no ejecutarla)
```

### Prioridad: 🟠 3
### Fecha de implementación: **2026-07-07** (semana 3)

---

## MÓDULO 4 — BIBLIOTECA DE ESTILOS

### Objetivo
Crear un repositorio de presets, plantillas y recetas visuales reutilizables que
garanticen consistencia editorial en todas las piezas sin reinventar el proceso
en cada proyecto.

### Problema actual
Cada proyecto comienza desde cero en términos de estilo visual.
Los parámetros de Lightroom de Puschak no están guardados como preset.
Las plantillas de Canva para el carrusel no existen todavía.
El estilo de texto del reel depende de que el editor "recuerde" los parámetros.

### Inputs
```
· MAGAZINE_STYLE_GUIDE.md (ya existe en el paquete Puschak)
· Parámetros de retouche de los primeros 3 proyectos retouchados
· Plantillas de Canva creadas para el primer carrusel
· Preset de CapCut del primer reel montado
```

### Outputs — Estructura de la biblioteca
```
05_MARKETING/99_BRANDING_GLOBAL/BIBLIOTECA_ESTILOS/
│
├── LIGHTROOM_PRESETS/
│   ├── JARDIN_IDEAL_HERO_v1.xmp          → Preset hero (luz de día, exterior)
│   ├── JARDIN_IDEAL_DETAIL_v1.xmp        → Preset détail (macro, textura)
│   ├── JARDIN_IDEAL_AVANT_v1.xmp         → Preset avant (deliberadamente sobrio)
│   └── README_PRESETS.md                 → Cuándo usar cada preset
│
├── CANVA_TEMPLATES/
│   ├── CARRUSEL_5SLIDES_4x5.canva        → Template carrusel (enlace Canva)
│   ├── STORY_PROMO_9x16.canva            → Template story con CTA
│   ├── META_AD_STATIC_1x1.canva          → Template anuncio cuadrado
│   └── README_CANVA.md                   → Instrucciones de uso
│
├── CAPCUT_PRESETS/
│   ├── REEL_TRANSFORMATION_35s.capcut    → Proyecto CapCut base (exportar como template)
│   └── README_CAPCUT.md                  → Cómo usar el preset base
│
└── TEXTOS_OVERLAY/
    ├── TIPOGRAFIAS_APROBADAS.md          → Fuentes exactas por rol
    ├── COLORES_APROBADOS.md              → Códigos HEX por elemento
    └── POSICIONES_ESTANDAR.md           → Dónde va cada elemento visual
```

### Cómo se construye la biblioteca
```
PASO 1: Terminar la retouche del paquete Puschak → guardar el preset de Lightroom
        como JARDIN_IDEAL_HERO_v1.xmp
PASO 2: Crear el carrusel Puschak en Canva → duplicar como template vacío
PASO 3: Exportar el proyecto CapCut del reel Puschak como base reutilizable
PASO 4: Documentar en README de cada sección cuándo y cómo usar cada elemento
PASO 5: Con cada nuevo proyecto → comparar con el estándar, actualizar si es mejor
```

### Automatizaciones necesarias
```
· Ninguna en esta fase — la biblioteca se construye manualmente
  los primeros 3 proyectos y luego se estabiliza
· Futuro: Manus puede aplicar presets automáticamente al abrir Lightroom
```

### Responsable
```
CREAR PRESETS : Editor / Daniel (durante la retouche de Puschak)
MANTENER      : Daniel (actualizar con cada proyecto nuevo)
DOCUMENTAR    : Claude (genera README de cada sección)
```

### Prioridad: 🟠 4
### Fecha de implementación: **2026-07-04** — se construye durante la retouche de Puschak y Bériault

---

## MÓDULO 5 — BANCO DE HOOKS PREMIUM

### Objetivo
Crear, testear y clasificar hooks según su rendimiento real en Meta Ads,
para tener siempre disponible el hook de mayor conversión por tipo de contenido.

### Problema actual
Los 17 hooks del paquete Puschak fueron generados en base a criterios creativos,
no a datos de rendimiento. No sabemos cuál convierte mejor porque ninguno se ha
testeado aún.

### Inputs
```
· HOOKS.md inicial (ya existe en paquete Puschak — 17 hooks)
· Datos de CTR y CPL de cada variante de anuncio (Meta Ads Manager)
· Análisis de competidores (qué hooks usan Capia, Verts par Experts)
· Nuevos proyectos → nuevos hooks específicos por servicio
```

### Estructura del banco
```
04_COPIES/BANCO_HOOKS/
│
├── HOOKS_ACTIVOS.md          → Hooks en uso actual con su score
├── HOOKS_ARCHIVO.md          → Hooks pausados con razón
├── HOOKS_TESTING.md          → Hooks en A/B test activo
└── HOOKS_POR_SERVICIO.md     → Hooks específicos por: cour avant, cour arrière,
                                pavé-uni, clôture, terrasse, balcon
```

### Estructura de cada hook en el banco
```
ID        : H-CA-001
HOOK      : "Et si votre cour pouvait ressembler à ça ?"
SERVICIO  : Cour Avant / General
FORMATO   : Reel (texto pantalla) + Carrusel (slide 1)
LANZADO   : 2026-06-25
CTR       : [actualizar después de 5 días]
CPL       : [actualizar después de 5 días]
STATUS    : 🟡 TESTING → ✅ ACTIVO / 🔴 PAUSADO
NOTA      : Hook de pregunta-identificación. Funciona mejor con foto AVANT como imagen.
```

### Protocolo de testing
```
SEMANA 1 : Lanzar 2 hooks simultáneos (Variante A vs B) — mismo presupuesto
SEMANA 2 : Evaluar CTR a los 5 días. Si CTR > 3%: ACTIVO. Si < 1.5%: PAUSAR.
SEMANA 3 : Reemplazar el pausado con un hook nuevo. Repetir.
REGLA    : Nunca cambiar el hook y el visual al mismo tiempo — contamina el test.
CICLO    : Renovar el hook activo cada 3–4 semanas (fatiga de audiencia).
```

### Automatizaciones necesarias
```
· Reporte semanal automático: AGENTE_REPORTES extrae CTR/CPL por variante
  desde los datos de Meta Ads y actualiza el banco
· Alerta: si CTR < 1.5% por 3 días → notificación para pausar
· Claude: genera 5 hooks nuevos cada lunes (input: proyectos de la semana pasada)
```

### Responsable
```
GENERAR HOOKS : Claude (lunes, batch semanal)
TESTEAR       : Daniel (configura en Meta Ads Manager)
ACTUALIZAR    : Claude + Daniel (datos post-campaña)
ARCHIVAR      : Claude (basado en datos de rendimiento)
```

### Prioridad: 🟠 4
### Fecha de implementación: **2026-06-30** — primer test al lanzar campaña Puschak

---

## MÓDULO 6 — SISTEMA DE SCORING FLOAT

### Objetivo
Tener un número único — el FLOAT SCORE — que mide en tiempo real el estado de
salud de la fábrica de contenido. Un número bajo dispara acciones específicas.

### El FLOAT SCORE — Definición
```
FLOAT SCORE = suma ponderada de 5 indicadores (máximo 100 puntos)

INDICADOR 1 — VELOCIDAD DE PRODUCCIÓN (25 pts)
  Fotos de cierre recibidas en <48h vs proyectos entregados esta semana
  25 pts = 100% | 15 pts = 75% | 5 pts = <50% | 0 pts = sin fotos

INDICADOR 2 — CALIDAD DEL ACTIVO HERO (25 pts)
  % de proyectos con hero image retouchée y lista para ads
  25 pts = 100% | 15 pts = 75% | 5 pts = <50% | 0 pts = ninguna

INDICADOR 3 — CADENCIA DE PUBLICACIÓN (20 pts)
  Piezas publicadas esta semana vs objetivo (7 piezas/semana)
  20 pts = 7+ | 15 pts = 5–6 | 8 pts = 3–4 | 0 pts = <3

INDICADOR 4 — RENDIMIENTO DEL HOOK ACTIVO (15 pts)
  CTR del anuncio activo vs objetivo (>3%)
  15 pts = CTR >3% | 10 pts = 2–3% | 5 pts = 1.5–2% | 0 pts = <1.5%

INDICADOR 5 — BANCO DE ACTIVOS DISPONIBLES (15 pts)
  Fotos aprobadas en carpeta DISPONIBLE listas para producción
  15 pts = >20 fotos | 10 pts = 10–20 | 5 pts = 5–9 | 0 pts = <5
```

### Escala de interpretación
```
FLOAT SCORE  80–100  : 🟢 FÁBRICA SANA — mantener ritmo
FLOAT SCORE  60–79   : 🟡 ATENCIÓN — identificar el indicador bajo y actuar
FLOAT SCORE  40–59   : 🟠 PROBLEMA — reunión de 15 min el lunes para diagnóstico
FLOAT SCORE  0–39    : 🔴 CRÍTICO — la fábrica está parada, escalar a Daniel hoy
```

### Cálculo y reporte
```
FRECUENCIA   : Cada lunes a las 08:00 AM (junto con el reporte semanal)
GENERADO POR : AGENTE_REPORTES (cuando tenga acceso a los datos)
FORMATO      : Línea en el reporte semanal + alerta WhatsApp si score < 60
ARCHIVO      : 08_REPORTES/FLOAT_SCORE_HISTORICO.md (registro semanal)
```

### Plantilla de reporte semanal FLOAT
```
═══════════════════════════════════════
FLOAT SCORE — SEMANA W[XX] · [FECHA]
═══════════════════════════════════════
Velocidad producción  : [X]/25 pts
Calidad hero          : [X]/25 pts
Cadencia publicación  : [X]/20 pts
Rendimiento hook      : [X]/15 pts
Banco de activos      : [X]/15 pts
─────────────────────────────────────
FLOAT SCORE TOTAL     : [XX]/100
ESTADO                : 🟢/🟡/🟠/🔴
─────────────────────────────────────
ACCIÓN REQUERIDA      : [si score < 80]
═══════════════════════════════════════
```

### Automatizaciones necesarias
```
· AGENTE_REPORTES: calcular score automáticamente con datos disponibles
· Make.com: si score < 60 → notificación WhatsApp urgente a Daniel
· Google Sheets: registro histórico del FLOAT SCORE semana a semana
  para identificar tendencias
```

### Responsable
```
CALCULAR  : Claude (AGENTE_REPORTES) — semi-manual hasta que Make.com esté activo
INTERPRETAR: Daniel
ACTUAR    : Daniel + equipo según el indicador bajo
```

### Prioridad: 🟡 5
### Fecha de implementación: **2026-07-14** — cuando haya 3 semanas de datos para calibrar

---

## MÓDULO 7 — KPI DE PRODUCCIÓN

### Objetivo
Separar los KPIs de la fábrica (producción) de los KPIs de campaña (marketing).
Medir la salud de la cadena de producción, no solo el resultado en Meta Ads.

### Por qué son distintos
```
KPI DE CAMPAÑA   : CPL, CTR, ROAS, leads generados → mide el resultado comercial
KPI DE PRODUCCIÓN: Mide si la fábrica tiene la materia prima para llegar a ese resultado

Un CPL alto puede significar mal hook, mala foto O mal targeting.
Sin KPIs de producción, no puedes saber cuál de los tres es el problema.
```

### Los 8 KPIs de producción FLOAT

| # | KPI | Objetivo | Alerta | Frecuencia |
|---|-----|----------|--------|------------|
| P1 | Fotos recibidas por proyecto | ≥5 fotos avant/après | <3 fotos | Por proyecto |
| P2 | Tiempo foto→hero retouchée | <48h desde entrega | >72h | Por proyecto |
| P3 | Tasa de aprobación QC | >60% de fotos aprobadas | <40% | Semanal |
| P4 | Piezas producidas por semana | ≥7 piezas | <4 piezas | Semanal |
| P5 | Proyectos sin hero image | 0 proyectos sin hero | >1 sin hero | Semanal |
| P6 | Banco de fotos disponibles | >20 fotos DISPONIBLE | <10 fotos | Semanal |
| P7 | Reels montados vs proyectos | 1 reel por proyecto | Ratio <0.5 | Mensual |
| P8 | Tiempo reel→publicado | <5 días desde montaje | >7 días | Por reel |

### Dashboard de producción semanal
```
FLOAT DASHBOARD — SEMANA W[XX]
════════════════════════════════════════════════════════════
P1 — Fotos recibidas esta semana         : [N] fotos / [N] proyectos
P2 — Tiempo promedio foto→hero           : [N] horas
P3 — Tasa aprobación QC                  : [N]% ([N] aprobadas / [N] evaluadas)
P4 — Piezas producidas                   : [N] / 7 objetivo
P5 — Proyectos sin hero                  : [N] proyectos
P6 — Banco disponible                    : [N] fotos en DISPONIBLE/
P7 — Ratio reel/proyecto                 : [N] reels / [N] proyectos
P8 — Tiempo montaje→publicación          : [N] días promedio
════════════════════════════════════════════════════════════
FLOAT SCORE                              : [XX]/100
```

### Fuentes de datos por KPI
```
P1 → fotos_videos_[fecha].json (00_DATOS_REALES/FOTOS_VIDEOS/)
P2 → Registro manual en FLOAT_SCORE_HISTORICO.md hasta Make.com activo
P3 → ASSETS_CLASIFICADOS.json (output del Módulo 3)
P4 → Conteo de publicaciones en Meta Business Suite
P5 → 99_EXPORTACIONES/HEROES_APROBADOS/ — contar archivos
P6 → 00_BIBLIOTECA_VISUAL/[SERVICIO]/DISPONIBLE/ — contar archivos
P7 → 99_EXPORTACIONES/CONTENT_PACKAGES/ — contar reels exportados
P8 → Registro manual de fechas
```

### Automatizaciones necesarias
```
· AGENTE_REPORTES: consolidar KPIs de las fuentes disponibles cada lunes
· Make.com (futuro): automatizar la recolección de P4 desde Meta Business Suite API
· Google Sheets: dashboard vivo con los 8 KPIs y gráficos de tendencia
· Alerta: si P5 > 1 (proyectos sin hero) → alerta WhatsApp automática
```

### Responsable
```
CALCULAR  : Claude (AGENTE_REPORTES) — lunes AM junto al reporte semanal
REVISAR   : Daniel — lunes en reunión 09:00 AM
ACTUAR    : Carlos/equipo (P1) · Editor (P2, P3, P8) · Daniel (P4, P5, P6, P7)
```

### Prioridad: 🟡 5
### Fecha de implementación: **2026-07-07** — semana 3, cuando haya datos de los primeros 2 proyectos

---

## CALENDARIO DE IMPLEMENTACIÓN

```
SEMANA 1 — 2026-06-23 al 2026-06-27
  · Ejecutar: Retouche Puschak HERO (Módulo 1 — primer ciclo)
  · Implementar: Protocolo de captura — reunión con Carlos y equipo
  · Crear: Presets Lightroom de Puschak → base Módulo 4
  · Lanzar: Primer A/B test de hooks (Módulo 5 — primer ciclo)

SEMANA 2 — 2026-06-30 al 2026-07-04
  · Activar: Protocolo de captura en obra (Módulo 2 — para próximo proyecto)
  · Construir: Plantillas Canva carrusel → Módulo 4 avanza
  · Testear: Resultados hook semana 1 → actualizar banco
  · Producir: Paquete Bériault (segundo proyecto completo)

SEMANA 3 — 2026-07-07 al 2026-07-11
  · Implementar: Clasificador automático con Claude en lote (Módulo 3 — manual)
  · Activar: KPIs de producción — primera medición (Módulo 7)
  · Producir: Paquete Annis Issa (tercer proyecto — COUR ARRIÈRE)
  · Evaluar: Resultados de las 2 primeras campañas con material Puschak

SEMANA 4 — 2026-07-14 al 2026-07-18
  · Activar: FLOAT SCORE — primera semana con datos suficientes (Módulo 6)
  · Revisar: Biblioteca de estilos — ajustar presets con 3 proyectos de datos
  · Planificar: Automatización Make.com para Módulos 1 y 3

MES 2 — AGOSTO 2026
  · Make.com activo: notificaciones de fotos recibidas
  · Clasificador semi-automático (Claude + trigger Make)
  · FLOAT SCORE calculado automáticamente cada lunes
  · Objetivo: 7 piezas/semana sin fallar 2 semanas seguidas
```

---

## RESUMEN EJECUTIVO

| Módulo | Qué logra | Cuándo | Quién |
|--------|-----------|--------|-------|
| 1 · Hero Image Factory | 1 hero premium por proyecto en <48h | Esta semana | Daniel + Editor |
| 2 · Protocolo Captura | Fotos de calidad garantizada desde campo | 2026-06-30 | Carlos + equipo |
| 3 · Clasificador Activos | Selección automática de las mejores fotos | 2026-07-07 | Claude + Make |
| 4 · Biblioteca Estilos | Cero tiempo reinventando el estilo visual | 2026-07-04 | Daniel (build) |
| 5 · Banco Hooks | Hooks testeados con datos reales de CPL | 2026-06-30 | Claude + Daniel |
| 6 · FLOAT Score | 1 número que dice si la fábrica está sana | 2026-07-14 | Claude + Daniel |
| 7 · KPI Producción | Diagnóstico preciso cuando algo falla | 2026-07-07 | Claude |

**La fábrica es funcional desde hoy con Módulos 1 y 5.**
**Los Módulos 2, 3, 4 la hacen consistente.**
**Los Módulos 6 y 7 la hacen medible y mejoran con el tiempo.**

---

*FLOAT V2 ROADMAP generado el 2026-06-23 — Jardín Ideal AI System*
*Próxima revisión: 2026-07-14 (cuando el FLOAT SCORE tenga 3 semanas de datos)*
