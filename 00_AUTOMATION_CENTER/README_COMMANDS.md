# README — SISTEMA DE COMANDOS
**Automation Center — Jardín Ideal AI System**
**Versión:** 1.0 · **Fecha:** 2026-06-24

---

## ¿QUÉ ES UN COMANDO?

Un comando es un archivo Markdown en `COMMANDS_INBOX/` que describe una acción específica que Claude Code debe ejecutar sobre los archivos del proyecto. Los comandos son la forma estructurada de solicitar cambios sin necesidad de un chat manual.

---

## CONVENCIÓN DE NOMBRES

```
YYYY-MM-DD_TIPO_DESCRIPCION_BREVE.md
```

Ejemplos:
```
2026-06-24_UPDATE_GLOBAL_CONTACT_AND_PAVE_WARRANTY.md
2026-07-01_LEGAL_UPDATE_LOI25_CHECKBOX_ALL_FORMS.md
2026-07-15_VISUAL_HERO_COUR_ARRIERE_V2.md
2026-08-01_CAMPAIGN_ACTIVATE_PAVE_UNI_META.md
```

---

## TIPOS DE COMANDO

### 1. COMANDO GLOBAL
Afecta múltiples proyectos o la base de datos de marca completa.

**Cuándo usar:** Cambio de email, cambio de teléfono, actualización de logo, cambio de colores corporativos, nueva garantía confirmada.

**Estructura:**
```markdown
# COMANDO GLOBAL — [descripción]
TIPO: GLOBAL
PRIORIDAD: ALTA | MEDIA | BAJA
APROBACION_HUMANA: SI | NO

## Acción
[descripción exacta de qué debe cambiar]

## Archivos afectados (estimado)
- [lista de archivos o carpetas]

## Reglas
- [restricciones o precauciones]

## Criterio de éxito
[cómo saber que el comando se ejecutó correctamente]
```

---

### 2. COMANDO POR LANDING
Afecta una landing page específica (HTML/CSS/JS local).

**Cuándo usar:** Corrección de formulario, actualización de precios, cambio de CTA, corrección legal, nueva sección.

**Estructura:**
```markdown
# COMANDO LANDING — [nombre LP] — [descripción]
TIPO: LANDING
LANDING: [nombre exacto del archivo HTML]
VERSION_ACTUAL: V1 | V2 | V3...
VERSION_OBJETIVO: V2 | V3...
APROBACION_HUMANA: SI | NO

## Acción
[descripción exacta del cambio en el HTML/JS/CSS]

## Código a insertar / reemplazar
[bloque de código si aplica]

## Archivos afectados
- [ruta exacta del archivo HTML]

## Criterio de éxito
[comportamiento esperado después del cambio]
```

---

### 3. COMANDO POR CAMPAÑA
Afecta configuración de campañas publicitarias (Meta Ads, Google Ads).

**Cuándo usar:** Cambio de presupuesto, pausar/activar campaña, cambiar audiencia, nuevo copy de anuncio.

**⚠️ SIEMPRE requiere aprobación humana.**

**Estructura:**
```markdown
# COMANDO CAMPAÑA — [plataforma] — [descripción]
TIPO: CAMPANA
PLATAFORMA: META_ADS | GOOGLE_ADS | TIKTOK_ADS
CAMPANA_ID: [ID si se conoce]
APROBACION_HUMANA: SI (obligatorio)

## Acción solicitada
[descripción exacta: pausar, activar, cambiar budget, cambiar copy]

## Validaciones requeridas antes de ejecutar
- [ ] Zapier webhook activo
- [ ] Meta Pixel disparando correctamente
- [ ] Formulario LP funcionando y conectado
- [ ] Aprobación explícita de Daniel

## Notas
[contexto adicional]
```

---

### 4. COMANDO POR PIEZA DE CONTENIDO
Afecta una pieza específica: carrusel, reel, imagen, video.

**Cuándo usar:** Corrección de texto en imagen, actualización de precio en carrusel, nuevo copy en reel.

**Estructura:**
```markdown
# COMANDO CONTENIDO — [tipo] — [descripción]
TIPO: CONTENIDO
SUBTIPO: CARRUSEL | REEL | IMAGEN | VIDEO
ARCHIVO_FUENTE: [ruta del archivo]
APROBACION_HUMANA: SI (para publicar)

## Acción
[descripción del cambio]

## Plataforma destino
[Instagram / Facebook / TikTok / LinkedIn]

## Estado actual
[borrador | revisión | listo para publicar]
```

---

### 5. COMANDO LEGAL
Afecta textos legales: política de privacidad, disclaimers, consentimientos.

**⚠️ SIEMPRE requiere aprobación humana y revisión de Daniel.**

**Estructura:**
```markdown
# COMANDO LEGAL — [descripción]
TIPO: LEGAL
APROBACION_HUMANA: SI (obligatorio)
REQUIERE_REVISION_ABOGADO: SI | NO | RECOMENDADO

## Texto actual
[citar el texto que se quiere cambiar]

## Texto propuesto
[nuevo texto propuesto]

## Razón del cambio
[justificación: Loi 25, nueva regulación, error detectado]

## Archivos afectados
[lista de LPs y documentos que contienen este texto]
```

---

### 6. COMANDO TÉCNICO
Afecta configuración técnica: webhooks, Pixel, integraciones, formularios JS.

**Estructura:**
```markdown
# COMANDO TÉCNICO — [descripción]
TIPO: TECNICO
APROBACION_HUMANA: SI | NO

## Componente afectado
[Meta Pixel | Zapier | Pipedrive | Formulario | Calculadora]

## Acción
[descripción técnica exacta]

## Código actual (si aplica)
```[código actual]```

## Código nuevo (si aplica)
```[código nuevo]```

## Prueba de validación
[cómo confirmar que funciona]
```

---

### 7. COMANDO VISUAL
Solicita a Manus una generación o modificación visual (HTML, imagen, diseño).

**Estructura:**
```markdown
# COMANDO VISUAL — [descripción]
TIPO: VISUAL
EDITOR: MANUS
APROBACION_HUMANA: SI (para resultado final)

## Contexto
[briefing del cambio visual]

## Archivos de referencia para Manus
- [lista de archivos del PAQUETES_CONTEXT_MANUS a cargar]

## Prompt para Manus
[prompt completo listo para copiar en Manus]

## Resultado esperado
[nombre del archivo de salida y dónde guardarlo]
```

---

## CICLO DE VIDA DE UN COMANDO

```
COMMANDS_INBOX/          → Claude Code lee y ejecuta
      │
      ├── Éxito → COMMANDS_DONE/    (con reporte adjunto)
      │
      └── Error → COMMANDS_FAILED/  (con diagnóstico adjunto)
```

### Estado de un comando

| Campo | Valores |
|-------|---------|
| ESTADO | PENDIENTE · EN_PROCESO · COMPLETADO · FALLIDO · ESPERANDO_APROBACION |
| PRIORIDAD | CRITICA · ALTA · MEDIA · BAJA |
| APROBACION_HUMANA | SI · NO |

---

## EJEMPLO DE EJECUCIÓN MANUAL

Para ejecutar un comando manualmente, Daniel puede escribir:
> "Ejecuta el comando `2026-06-24_UPDATE_GLOBAL_CONTACT_AND_PAVE_WARRANTY.md`"

Claude Code leerá el archivo, ejecutará las acciones, generará reporte, hará commit y moverá el comando a `COMMANDS_DONE/`.

---

*README Commands — Jardín Ideal Automation Center · v1.0 · 2026-06-24*
