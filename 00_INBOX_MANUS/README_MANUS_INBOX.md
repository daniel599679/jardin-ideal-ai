# INBOX MANUS — Archivos Exportados desde Manus
**Carpeta:** `00_INBOX_MANUS/`
**Propósito:** Recibir y almacenar todos los archivos exportados desde Manus para análisis local por Claude Code.

---

## Por qué existe esta carpeta

Manus ejecuta sus sesiones en servidores temporales (URLs tipo `us2.manus.computer`). Esas URLs expiran cuando la sesión está inactiva y retornan `502 Bad Gateway`. Para que Claude Code pueda analizar archivos reales — en lugar de intentar acceder a URLs caídas — todos los entregables de Manus deben exportarse y guardarse aquí antes de pedir un análisis.

**Regla fundamental:** Si el archivo no está en esta carpeta, Claude Code no puede analizarlo.

---

## Estructura de subcarpetas

```
00_INBOX_MANUS/
├── LANDING_PAGES/      ← Archivos HTML de landing pages
├── CAPTURES/           ← Screenshots y capturas de pantalla
├── BRIEFS/             ← Documentos de brief recibidos de Manus
└── EXPORTS_ZIP/        ← Exports comprimidos completos (HTML + assets)
```

---

## Convención de nombres obligatoria

Todos los archivos deben seguir el formato:

```
YYYY-MM-DD_SERVICIO_VERSION_TIPO.ext
```

| Segmento | Descripción | Ejemplos |
|----------|-------------|---------|
| `YYYY-MM-DD` | Fecha de exportación | `2026-06-24` |
| `SERVICIO` | Nombre del servicio en mayúsculas | `COUR_ARRIERE`, `PISCINE`, `COUR_AVANT` |
| `VERSION` | Versión incremental | `V1`, `V2`, `V3` |
| `TIPO` | Tipo de archivo | `HTML`, `SCREENSHOT`, `EXPORT`, `NOTES` |

**Ejemplos reales:**
```
2026-06-24_COUR_ARRIERE_V1_HTML.html
2026-06-24_COUR_ARRIERE_V1_SCREENSHOT.png
2026-06-24_COUR_ARRIERE_V1_EXPORT.zip
2026-06-24_COUR_ARRIERE_V1_NOTES.md
2026-06-25_COUR_ARRIERE_V2_HTML.html     ← segunda versión después de correcciones
```

---

## Cómo exportar desde Manus

### Opción A — Copiar HTML
1. En Manus, abrir la landing page generada
2. Hacer clic derecho → Ver código fuente (o Ctrl+U)
3. Seleccionar todo (Ctrl+A), copiar
4. Crear un archivo `.html` con el nombre correcto en `LANDING_PAGES/`
5. Pegar el contenido y guardar

### Opción B — Descargar ZIP
1. En Manus, usar la función de export/descarga si está disponible
2. Renombrar el ZIP con la convención de nombres
3. Guardar en `EXPORTS_ZIP/`

### Opción C — Screenshot
1. Captura de pantalla completa de la landing (usa extensión de navegador para páginas largas)
2. Guardar en `CAPTURES/` con el nombre correcto

---

## Tipos de archivos aceptados

| Subcarpeta | Extensiones | Notas |
|------------|-------------|-------|
| `LANDING_PAGES/` | `.html`, `.htm` | Un solo archivo auto-contenido preferido |
| `CAPTURES/` | `.png`, `.jpg`, `.webp` | Full-page screenshot recomendado |
| `BRIEFS/` | `.md`, `.txt`, `.pdf` | Documentos de contexto de Manus |
| `EXPORTS_ZIP/` | `.zip` | Incluir HTML + imágenes + CSS externo si aplica |

---

## Qué hace Claude Code con estos archivos

Una vez el archivo está en esta carpeta:

1. **Lee el HTML local** — no necesita URL, lee el archivo directamente
2. **Analiza la estructura** — secciones, formularios, calculadoras, precios
3. **Genera diagnóstico** → guardado en `07_REPORTES/LANDING_PAGES/`
4. **Genera correcciones** → guardadas en `00_OUTBOX_CLAUDE_PARA_MANUS/CORRECCIONES/`
5. **Genera prompt para Manus** → guardado en `00_OUTBOX_CLAUDE_PARA_MANUS/PROMPTS_MANUS/`
6. **Compara versiones** si existe V_anterior

---

## Estado actual de archivos

| Servicio | Versión | Fecha | Estado |
|----------|---------|-------|--------|
| Cour Arrière | V1 | — | ⏳ PENDIENTE EXPORTAR desde Manus |

*Actualizar esta tabla cada vez que se agrega un archivo.*

---

*Jardín Ideal AI System · 2026-06-24*
