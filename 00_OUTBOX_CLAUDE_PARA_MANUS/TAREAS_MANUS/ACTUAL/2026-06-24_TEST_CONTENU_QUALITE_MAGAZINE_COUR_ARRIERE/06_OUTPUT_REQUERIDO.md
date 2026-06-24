# OUTPUT REQUERIDO — Entregables de Manus
**Tarea:** TASK-002 · Carrusel Magazine Cour Arrière
**Destinatario de entrega:** Daniel → guardar en `00_INBOX_MANUS/CONTENIDO/`

---

## ENTREGABLES OBLIGATORIOS

### 1. Archivos de slide individuales

| Archivo | Especificaciones |
|---------|-----------------|
| `COUR_ARRIERE_SLIDE_01_HOOK.png` | 1080×1080 px · PNG · sRGB |
| `COUR_ARRIERE_SLIDE_02_PROBLEME.png` | 1080×1080 px · PNG · sRGB |
| `COUR_ARRIERE_SLIDE_03_EXPERTISE.png` | 1080×1080 px · PNG · sRGB |
| `COUR_ARRIERE_SLIDE_04_MATERIAU.png` | 1080×1080 px · PNG · sRGB |
| `COUR_ARRIERE_SLIDE_05_RESULTAT.png` | 1080×1080 px · PNG · sRGB |
| `COUR_ARRIERE_SLIDE_06_CTA.png` | 1080×1080 px · PNG · sRGB |

**Alternativa aceptada:** JPG alta calidad (≥90%) si PNG supera 2 MB por slide.

---

### 2. Texto exacto por slide (documento de verificación)

Entregar un archivo de texto o Markdown con el texto exacto que aparece en cada slide, tal como está en el diseño. Esto permite verificar ortografía sin abrir cada imagen.

**Formato mínimo:**
```
SLIDE 1: [texto headline] / [subtítulo si aplica]
SLIDE 2: [texto headline] / [subtítulo si aplica]
...etc.
```

---

### 3. Preview del carrusel completo

Una imagen combinada que muestre los 6 slides en secuencia (formato horizontal o grid 2×3), para revisar la coherencia visual del conjunto.

Formato sugerido:
- Grid 3×2: slides 1-2-3 en fila superior, 4-5-6 en fila inferior
- O banda horizontal: 6 slides en una sola fila

Nombre de archivo: `COUR_ARRIERE_CARRUSEL_PREVIEW.png`

---

### 4. Archivo editable (si es posible)

Si Manus puede exportar un archivo editable, entregarlo para facilitar ajustes futuros:

| Formato | Prioridad |
|---------|-----------|
| Archivo nativo Manus | ✅ Primera opción |
| Canva (link compartible) | ✅ Segunda opción |
| Figma (link compartible) | ✅ Segunda opción |
| PSD (Photoshop) | Aceptado |
| PDF editable | Mínimo aceptable |

**Si no es posible un archivo editable:** Indicar claramente en la nota de entrega.

---

### 5. Nota de entrega

Un texto breve que indique:
- Cuántas fotos fueron recibidas y cuántas se usaron
- Qué foto se eligió para cada slide y por qué
- Si alguna foto no pudo usarse (y la razón)
- Si se tomó alguna decisión de diseño no prevista en el brief
- Cualquier observación sobre la calidad o usabilidad de los assets proporcionados

---

## DÓNDE GUARDAR LOS ENTREGABLES

```
00_INBOX_MANUS/
└── CONTENIDO/
    └── 2026-06-24_CARRUSEL_COUR_ARRIERE_V1/
        ├── COUR_ARRIERE_SLIDE_01_HOOK.png
        ├── COUR_ARRIERE_SLIDE_02_PROBLEME.png
        ├── COUR_ARRIERE_SLIDE_03_EXPERTISE.png
        ├── COUR_ARRIERE_SLIDE_04_MATERIAU.png
        ├── COUR_ARRIERE_SLIDE_05_RESULTAT.png
        ├── COUR_ARRIERE_SLIDE_06_CTA.png
        ├── COUR_ARRIERE_CARRUSEL_PREVIEW.png
        ├── TEXTE_PAR_SLIDE.md
        └── NOTE_DE_LIVRAISON.md
```

---

## ESTADO ESPERADO POST-ENTREGA

Una vez que Daniel recibe los archivos y los guarda en `00_INBOX_MANUS/CONTENIDO/`:

1. Claude Code realiza la revisión con `07_CHECKLIST_REVISION_HUMAINE.md`
2. Se genera un reporte de revisión en `07_REPORTES/CONTENIDO/`
3. Si el resultado supera el umbral de calidad → Daniel aprueba o solicita revisión
4. Si no supera → se genera feedback específico para Manus en `00_OUTBOX_CLAUDE_PARA_MANUS/CORRECCIONES/`

---

## CRITERIO DE APROBACIÓN

El carrusel se considera aprobado para publicación cuando:

| Criterio | Umbral |
|----------|--------|
| Calidad visual magazine | ≥ 8/10 según juicio de Daniel |
| Ortografía francesa | 0 errores |
| Coherencia de marca | 100% (colores, tipografía, logo) |
| Ausencia de claims inventados | 100% |
| CTA claro en slide 6 | Sí |
| Aprobación humana explícita | Sí (requerida antes de publicar) |

---

## IMPORTANTE — NO PUBLICAR SIN APROBACIÓN

Este carrusel es un **test interno de calidad**. No debe publicarse en ninguna plataforma (Instagram, Facebook, Meta Ads) sin:

1. Revisión completa de `07_CHECKLIST_REVISION_HUMAINE.md`
2. Aprobación explícita de Daniel
3. Decisión sobre qué caption usar (03_COPY_CAPTIONS.md)
4. Si es para publicidad pagada: confirmación de budget y audiencia

---

*Output Requerido TASK-002 — Jardin Idéal · 2026-06-24*
