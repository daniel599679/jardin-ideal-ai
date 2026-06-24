# REGLAS DE FORMATO Y ESTILO VISUAL
**Tarea:** TASK-002 · Carrusel Magazine Cour Arrière
**Para:** Manus y revisión interna

---

## ESTÁNDAR VISUAL OBJETIVO

**Referente de calidad:** Magazine de diseño residencial de lujo.
Pensar en: *AD France, Côté Maison, Azure Magazine, Elle Décoration*.

Cada slide debe poder existir como portada de una revista de arquitectura exterior.

---

## FORMATO TÉCNICO

| Parámetro | Valor |
|-----------|-------|
| Dimensiones | 1080 × 1080 px |
| Resolución | 72 dpi (pantalla) — 300 dpi si se quiere imprimir |
| Formato de entrega | PNG (preferred) o JPG alta calidad (>90%) |
| Ratio | 1:1 (cuadrado) |
| Espacio de color | sRGB |
| Peso máximo por slide | 2 MB (para Meta) |

---

## PALETA DE COLORES — USAR SOLO ESTOS

```
Verde oscuro (fondo principal) : #052B16
Verde medio (hover, accents)   : #0A4523
Verde claro (badges, accents)  : #008E3F
Dorado (teléfono, highlights)  : #C8A45A
Crema (fondos suaves)          : #F5F2EB
Blanco cálido                  : #FAFAF8
Texto oscuro                   : #1C2118
Texto medio                    : #4A5546
```

**NUNCA usar:**
- Negro puro `#000000` (excepto sombras/shadows)
- Azules, rojos, naranjas, morados
- Colores de stock photos que no estén en esta paleta
- Blanco puro `#FFFFFF` como fondo de slide (demasiado frío)

---

## TIPOGRAFÍA

| Rol | Familia | Peso | Uso |
|-----|---------|------|-----|
| Headline principal | Montserrat | Bold 700 | Título de cada slide |
| Subtítulo | Montserrat | SemiBold 600 | Datos, bullets |
| Cuerpo / detalle | Open Sans | Regular 400 | Descripción larga |
| Datos / números | Montserrat | ExtraBold 800 | Cifras (1 500+, 15 ans) |

### Tamaños recomendados (para 1080×1080)

| Elemento | Tamaño px |
|----------|----------|
| Headline principal | 56–72 px |
| Subtítulo | 28–36 px |
| Bullets / details | 22–28 px |
| Footer / marca | 18–22 px |
| Micro-texto legal | 14–16 px |

**Regla de oro:** Si el texto parece pequeño cuando el slide se ve en teléfono a 30cm de distancia, es demasiado pequeño.

---

## FOTOGRAFÍA — REGLAS ABSOLUTAS

### Lo que se DEBE usar
- Fotos reales de proyectos de Jardín Ideal (las de `05_ASSETS/IMAGES/`)
- Fotos con cielo azul y nubes (preferido en 85%+ de proyectos)
- Pavé beige / gris clair — bien instalado, uniforme
- Césped verde brillante, bien mantenido
- Luz natural de tarde (dorada) o mediodía (limpia)
- Arquitectura residencial québécoise: briques rouges, revêtement de vinyle

### Lo que está PROHIBIDO
- Fotos de stock genéricas (Shutterstock, iStock, Unsplash)
- Jardines tropicales (palmeras, plantas exóticas, flores no-québécoises)
- Jardines europeos (casas muy diferentes a Quebec)
- Fotos de invierno / nieve (a menos que sea contenido específico)
- Fotos de drone / vista aérea
- Personas visibles en primer plano (evitar para no envejecer el contenido)
- Fotos oscuras, subexpuestas o mal enfocadas
- Fotos con marcas de agua de otros fotógrafos

---

## COMPOSICIÓN — GUÍAS POR SLIDE

### Slides de "show" (1, 4, 5)
```
[████████████████████]  ← foto pleno 85-90% del slide
[████████████████████]
[████████████████████]
[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓]  ← banda texto: verde oscuro semitransparente
[  HEADLINE AQUÍ     ]
[  subtítulo pequeño ]
```

### Slides de "info" (2, 3)
```
[████████████████████]  ← foto 60-70% del slide
[████████████████████]
[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓]  ← área de texto más grande
[  HEADLINE          ]
[  • bullet 1        ]
[  • bullet 2        ]
[  • bullet 3        ]
```

### Slide CTA (6)
```
[████████████████████]  ← foto overlay muy oscuro (70% opacidad)
[     LOGO           ]
[  HEADLINE GRANDE   ]
[  514-266-2504      ]  ← en dorado #C8A45A
[  → BOUTON CTA      ]
[  info@j-i.com      ]
[  RBQ #5773...      ]
```

---

## REGLAS DE TEXTO EN SLIDES

| Regla | Detalle |
|-------|---------|
| **Máximo palabras** | 6–8 palabras en el headline principal |
| **No saturar** | Si hay duda entre más o menos texto → menos texto |
| **Contraste** | Texto siempre legible: blanco sobre oscuro, oscuro sobre claro |
| **Sombra** | Usar text-shadow suave si el texto está sobre foto |
| **Alineación** | Preferir izquierda o centrado — no justificado |
| **Tracking** | Ligeramente expandido en titulares (letter-spacing: 0.05em) |
| **No ALL CAPS agresivo** | Aceptable en subtítulos cortos, evitar en párrafos |

---

## ESTILO VISUAL POR SLIDE

| Slide | Mood | Temperatura | Contraste |
|-------|------|-------------|-----------|
| 1 | Aspiracional, limpio | Fría-neutra | Alto |
| 2 | Honesto, cálido | Cálida | Medio |
| 3 | Profesional, técnico | Neutra | Medio-alto |
| 4 | Sensorial, lujoso | Cálida-natural | Alto (textura) |
| 5 | Emocional, satisfecho | Cálida-dorada | Alto |
| 6 | Directo, acción | Oscura-verde | Máximo legibilidad |

---

## ELEMENTOS DE MARCA

### Logo
- Slide 6 (CTA): Logo en posición prominente
- Slides 1–5: Logo pequeño y discreto en esquina (no protagonista)
- Si no hay logo disponible: usar solo el nombre "Jardin Idéal" en Montserrat Bold

### Número de slide
- Pequeño en esquina inferior derecha (ej: "1/6", "2/6"...)
- O usar puntos de progresión visual (dots)
- Color: blanco al 60% de opacidad

### RBQ
- Siempre en slide 6 (CTA) — visibilidad completa
- Opcional en slide 3 (expertise) — tamaño pequeño

---

## ERRORES FRECUENTES A EVITAR

| Error | Solución |
|-------|----------|
| Texto muy pequeño en mobile | Mínimo 56px para headline en 1080px |
| Foto de fondo muy brillante → texto ilegible | Overlay oscuro o banda de color |
| Demasiados elementos en un slide | Eliminar lo menos importante |
| Colores fuera de paleta | Usar exactamente los hex confirmados |
| Garantía para servicio no confirmado | Garantía 5 ans solo para pavé/pavé uni |
| Precio inventado | No poner ningún precio sin confirmación |
| Marca de agua de stock | Solo fotos reales de 05_ASSETS/IMAGES/ |
| Logo demasiado grande | Logo es firma, no protagonista (excepción: slide 6) |

---

## CALIDAD MAGAZINE — CHECKLIST DE DISEÑADOR

Antes de entregar, cada slide debe pasar esta prueba mental:

- [ ] ¿Esta imagen podría aparecer en AD Magazine o Côté Maison?
- [ ] ¿El texto se lee en 2 segundos desde el feed?
- [ ] ¿La foto es la protagonista, no el texto?
- [ ] ¿Los colores son consistentes con los de los otros 5 slides?
- [ ] ¿Hay un elemento visual que te hace querer ver el siguiente slide?

---

*Reglas de Formato TASK-002 — Carrusel Magazine Cour Arrière · 2026-06-24*
