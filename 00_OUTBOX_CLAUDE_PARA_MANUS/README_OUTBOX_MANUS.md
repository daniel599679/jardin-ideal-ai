# OUTBOX CLAUDE → MANUS — Instrucciones Listas para Copiar
**Carpeta:** `00_OUTBOX_CLAUDE_PARA_MANUS/`
**Propósito:** Claude Code deposita aquí todo lo que debes copiar y pegar directamente en Manus.

---

## Concepto

Claude Code no puede hablarle a Manus directamente. Esta carpeta es el puente: Claude Code escribe instrucciones precisas aquí, tú las copias y las pegas en la sesión de Manus. El ciclo completo:

```
Claude Code analiza
    ↓
Escribe instrucciones en esta carpeta
    ↓
Tú copias y pegas en Manus
    ↓
Manus ejecuta
    ↓
Tú exportas resultado a 00_INBOX_MANUS/
    ↓
Claude Code analiza la nueva versión
```

---

## Estructura de subcarpetas

```
00_OUTBOX_CLAUDE_PARA_MANUS/
├── INSTRUCCIONES/     ← Instrucciones generales de sesión para Manus
├── CORRECCIONES/      ← Lista de cambios específicos por landing page y versión
├── BRIEFS_VISUALES/   ← Descripciones visuales para que Manus genere diseños
└── PROMPTS_MANUS/     ← Prompts maestros reutilizables por tipo de tarea
```

---

## Tipos de documentos

### `INSTRUCCIONES/`
Instrucciones de sesión completas. Se usan cuando se inicia una nueva sesión de Manus desde cero.

**Nombre:** `YYYY-MM-DD_INSTRUCCION_[DESCRIPCION].md`
**Ejemplo:** `2026-06-25_INSTRUCCION_INICIO_SESION_LP_COUR_ARRIERE.md`

Contenido típico:
- Contexto del proyecto
- Qué debe hacer Manus en esta sesión
- Archivos de referencia
- Resultado esperado y formato de entrega

### `CORRECCIONES/`
Lista técnica de cambios a aplicar sobre una versión existente de landing page.

**Nombre:** `YYYY-MM-DD_[SERVICIO]_[VERSION]_CORRECCIONES.md`
**Ejemplo:** `2026-06-25_COUR_ARRIERE_V1_CORRECCIONES.md`

Contenido típico:
- Cambios ordenados por prioridad (Crítico → Alto → Mejora)
- Cada cambio con: sección afectada, problema, solución exacta
- Fragmentos de código HTML/CSS/JS cuando aplica

### `BRIEFS_VISUALES/`
Descripciones de diseño para que Manus genere o modifique elementos visuales.

**Nombre:** `YYYY-MM-DD_[SERVICIO]_BRIEF_VISUAL.md`
**Ejemplo:** `2026-06-25_COUR_ARRIERE_BRIEF_VISUAL.md`

Contenido típico:
- Colores exactos (hex)
- Tipografía
- Mood / estilo visual
- Referencias de imágenes (criterios, no URLs externas)
- Elementos a incluir / excluir

### `PROMPTS_MANUS/`
Prompts maestros reutilizables. No son específicos de una versión sino de un tipo de tarea.

**Nombre:** `PROMPT_[TIPO_TAREA].md`
**Ejemplo:** `PROMPT_BASE_CORRECCION_LANDING.md`

---

## Cómo usar estos documentos

1. **Abre el documento** correspondiente en tu editor de texto
2. **Selecciona todo** el contenido (Ctrl+A)
3. **Copia** (Ctrl+C)
4. **Abre tu sesión de Manus** (reiniciar si hace falta para evitar 502)
5. **Pega** el contenido en el chat de Manus
6. **Revisa** el output de Manus antes de exportar
7. **Exporta** el resultado a `00_INBOX_MANUS/LANDING_PAGES/` con el nombre correcto

---

## Reglas para Claude Code al escribir en esta carpeta

- Cada documento debe ser **completo y auto-contenido** — Manus no tiene memoria de sesiones anteriores
- Siempre incluir **contexto de Jardín Ideal** al inicio (empresa, servicio, objetivo)
- Las instrucciones técnicas deben ser **copiables literalmente** — sin texto explicativo mezclado
- Separar claramente **qué hacer** vs **cómo verificar** que se hizo bien
- Nunca incluir precios exactos, garantías legales o datos no confirmados

---

*Jardín Ideal AI System · 2026-06-24*
