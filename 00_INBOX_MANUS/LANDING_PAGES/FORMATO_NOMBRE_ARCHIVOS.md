# CONVENCIÓN DE NOMBRES — Archivos Landing Pages
**Carpeta:** `00_INBOX_MANUS/LANDING_PAGES/`

---

## Formato obligatorio

```
YYYY-MM-DD_SERVICIO_VERSION_TIPO.ext
```

---

## Segmentos del nombre

### `YYYY-MM-DD` — Fecha de exportación
La fecha en que el archivo fue exportado desde Manus, NO la fecha de creación del proyecto.

```
2026-06-24   ← correcto
24-06-2026   ← incorrecto
240624       ← incorrecto
```

### `SERVICIO` — Código del servicio
En mayúsculas, sin acentos, guiones bajos como separador.

| Servicio | Código |
|----------|--------|
| Cour arrière | `COUR_ARRIERE` |
| Cour avant | `COUR_AVANT` |
| Piscine | `PISCINE` |
| Cuisines extérieures | `CUISINE_EXT` |
| Balcon | `BALCON` |
| Stationnement | `STATIONNEMENT` |
| Clôture | `CLOTURE` |
| Éclairage | `ECLAIRAGE` |
| Irrigation | `IRRIGATION` |

### `VERSION` — Versión incremental
Empieza en V1. Sube por cada iteración de correcciones aplicadas por Manus.

```
V1   ← primer prototipo Manus
V2   ← después de aplicar correcciones de Claude Code
V3   ← segunda ronda de correcciones
```

No saltar versiones. Si una versión se descarta, documentarlo en `NOTES`.

### `TIPO` — Tipo de entregable

| Tipo | Descripción | Extensión |
|------|-------------|-----------|
| `HTML` | Código fuente de la landing page | `.html` |
| `SCREENSHOT` | Captura de pantalla completa | `.png` / `.jpg` |
| `EXPORT` | ZIP con HTML + assets | `.zip` |
| `NOTES` | Notas de sesión Manus | `.md` |
| `DIFF` | Comparación entre versiones | `.md` |

---

## Ejemplos completos

```
# Cour Arrière — ciclo completo de iteraciones
2026-06-24_COUR_ARRIERE_V1_HTML.html         ← prototipo inicial Manus
2026-06-24_COUR_ARRIERE_V1_SCREENSHOT.png    ← captura del prototipo
2026-06-24_COUR_ARRIERE_V1_NOTES.md          ← notas de la sesión Manus
2026-06-25_COUR_ARRIERE_V2_HTML.html         ← después de correcciones Claude Code
2026-06-25_COUR_ARRIERE_V2_SCREENSHOT.png    ← captura de la versión corregida
2026-06-25_COUR_ARRIERE_V2_DIFF.md           ← comparación V1 vs V2
2026-06-26_COUR_ARRIERE_V3_EXPORT.zip        ← versión final lista para publicar

# Piscine — inicio de nuevo servicio
2026-07-01_PISCINE_V1_HTML.html
2026-07-01_PISCINE_V1_SCREENSHOT.png
```

---

## Reglas adicionales

1. **Un HTML por versión** — no sobreescribir versiones anteriores, crear una nueva.
2. **Screenshot obligatorio** — siempre acompañar el HTML con una captura visual.
3. **NOTES opcional pero recomendado** — documenta qué pidió Manus, qué generó, errores encontrados.
4. **ZIP solo para versión final** — no comprimir cada iteración, solo la versión lista para publicar.
5. **Sin espacios en nombres** — usar guiones bajos únicamente.
6. **Sin caracteres especiales** — sans accents, sans apostrophes, sans é è à û.

---

## Tabla de versiones activas

| Servicio | V1 | V2 | V3 | Estado |
|----------|----|----|----|----|
| COUR_ARRIERE | ⏳ pendiente | — | — | Esperando exportación |

*Actualizar cuando se agregue cada archivo.*

---

*Jardín Ideal AI System · 2026-06-24*
