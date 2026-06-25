# BRAND RULES — JARDÍN IDEAL / GROUPE IDEAL
**Versión:** 2.0 | **Fecha:** 2026-06-25 | **Decisión:** DS-020  
**Directorio oficial:** `05_MARKETING/BRANDING_OFFICIEL/`  
**Regla:** PERMANENTE — no modificar sin aprobación de Daniel

---

## REGLA CARDINAL — DS-020

> **Todo contenido producido para Jardín Ideal o Groupe Ideal usa exclusivamente los activos de `05_MARKETING/BRANDING_OFFICIEL/`.**
>
> Claude no solicita logos, colores, tipografías ni nombres de empresa al usuario.  
> Si un activo no existe → búsqueda automática → alerta de activo faltante.  
> Todo paquete Manus incluye branding automáticamente.

---

## LAS 7 REGLAS PERMANENTES DE LOGO (DS-020 — Reforzado)

### Regla 1 — Nunca crear logos nuevos
Está prohibido generar, dibujar, componer o inventar un logo. Solo se usan los archivos oficiales existentes en `05_MARKETING/BRANDING_OFFICIEL/logos/`.

### Regla 2 — Nunca usar tipografías para sustituir un logo
Escribir "Jardín Ideal" o "Groupe Ideal" en cualquier fuente, con cualquier estilo, NO es un logo. No se puede usar tipografía como reemplazo temporal o permanente del logo oficial.

### Regla 3 — Usar exclusivamente archivos oficiales
Los únicos archivos de logo válidos son los que se encuentran en:
```
05_MARKETING/BRANDING_OFFICIEL/logos/
```
Ningún otro archivo, URL, imagen externa o recreación es válida.

### Regla 4 — Logo Jardín Ideal → carpeta jardin_ideal/
```
05_MARKETING/BRANDING_OFFICIEL/logos/jardin_ideal/
├── LOGO_JARDIN_IDEAL_PRINCIPAL.png   ← USAR ESTE — fondo blanco, É con hoja
├── LOGO_JARDIN_IDEAL_ACCENT.png      ← Con acento É — versión alternativa
└── LOGO_JARDIN_IDEAL_SOCIAL.jpg      ← Versión cuadrada para redes sociales
```

### Regla 5 — Logo Groupe Ideal → carpeta groupe_ideal/
```
05_MARKETING/BRANDING_OFFICIEL/logos/groupe_ideal/
├── LOGO_GROUPE_IDEAL_PRINCIPAL.png   ← "CONSTRUCTION GROUPE IDÉAL" + monograma G (fondo oscuro)
├── LOGO_GROUPE_IDEAL_COMPACT.png     ← "GROUPE IDEAL" en rectángulo verde (fondo blanco)
└── LOGO_GROUPE_IDEAL_DARK.png        ← Monograma G solamente (fondo oscuro — ícono compacto)
```
⚠️ **ALERTA ACTIVA:** Todos los logos Groupe Ideal son capturas de pantalla — calidad limitada. Solicitar SVG/AI/EPS/PNG con fondo transparente a Daniel.

### Regla 6 — Todo paquete Manus incluye branding automáticamente
Cada ZIP enviado a Manus debe contener una carpeta `/branding/` con:
- `LOGO_JARDIN_IDEAL_PRINCIPAL.png`
- `PALETA_COLORES.txt`
- `FONT_GUIDE.txt`
- `BRAND_RULES.md`

Referencia completa: `05_MARKETING/BRANDING_OFFICIEL/MANUS_PACKAGE_TEMPLATE/BRANDING_CHECKLIST.md`

### ⛔ REGLA 7 — STOP INMEDIATO SI EL LOGO NO EXISTE O NO ES ACCESIBLE

> **Si el archivo de logo oficial no existe en `BRANDING_OFFICIEL/logos/` o no puede ser leído/copiado → DETENER LA TAREA INMEDIATAMENTE y notificar a Daniel.**

**Comportamiento obligatorio:**
1. Intentar leer el logo desde la ruta oficial
2. Si falla (archivo no encontrado, error de acceso, archivo corrupto) → STOP
3. Enviar notificación: `⛔ REGLA 7 ACTIVADA — Logo [nombre] no accesible en [ruta]. Tarea detenida. Acción requerida: Daniel debe verificar/restaurar el archivo antes de continuar.`
4. NO continuar la tarea con ningún substituto
5. NO usar wordmarks temporales
6. NO crear un logo alternativo
7. NO ignorar el error y continuar

**Esto aplica a:** logos en paquetes Manus, piezas Meta Ads, carruseles, reels, landing pages, cualquier entregable visual.

---

## IDENTIDAD DE MARCA

### Nombres oficiales
| Marca | Nombre correcto | Evitar |
|-------|----------------|--------|
| Principal | **Jardín Ideal** | Jardin Ideal (sin acento), jardin ideal |
| Corporativa | **Groupe Ideal** | Grupo Ideal, Group Ideal |

### Taglines aprobados (francés — idioma de los clientes)
- "Votre entrée mérite mieux."
- "L'extérieur, réinventé."
- "Soumission gratuite · Sans engagement"
- "15+ ans d'expérience · Qualité garantie"

### Información de contacto oficial
| Dato | Valor | Color en piezas |
|------|-------|----------------|
| Teléfono | **514-266-2504** | `#C8A45A` dorado — SIEMPRE |
| Web | jardin-ideal.com | Blanco o crema |
| Zonas | Montréal · Laval · Rive-Nord | — |

---

## PALETA DE COLORES

| Nombre | HEX | Uso principal |
|--------|-----|---------------|
| Verde Oscuro | `#052B16` | Fondos, headers, overlays |
| Verde Claro | `#008E3F` | Color del logo, iconos, labels activos |
| Dorado | `#C8A45A` | Teléfono CTA, acentos premium |
| Crema | `#F5F2EB` | Fondos neutros, slides de texto |
| Blanco | `#FFFFFF` | Texto sobre oscuro |
| Rojo AVANT | `#CC3333` | Exclusivo para etiqueta "Avant" en B/A |

> ⚠️ El verde oscuro oficial es `#052B16`. La versión `#1E3A20` es INCORRECTA — no usar.

**Referencia completa:** `05_MARKETING/BRANDING_OFFICIEL/PALETA_COLORES.txt`

---

## TIPOGRAFÍA

| Rol | Fuente | Alternativa sistema |
|-----|--------|---------------------|
| Display / Títulos | Playfair Display / Georgia | Times New Roman |
| Cuerpo / UI | Montserrat | Arial, system-ui |
| Datos / Técnico | Courier New | Courier |

**Tamaños estándar:**
- Hero title: 52–72px
- Slide title: 36–48px
- Cuerpo: 14–16px
- CTA teléfono: 28–40px Bold

**Referencia completa:** `05_MARKETING/BRANDING_OFFICIEL/FONT_GUIDE.txt`

---

## REGLAS DE USO DEL LOGO EN PIEZAS

### Posicionamiento
| Formato | Posición | Aparición |
|---------|----------|-----------|
| Reels / Video | Inferior-izquierda | Fade in — últimos 5 segundos |
| Carrusel | Inferior-derecha o inferior-izquierda | TODOS los slides |
| Meta Ads estático | Inferior-derecha | Siempre visible |
| Landing page | Header o footer | Siempre |

### Prohibiciones absolutas de logo
- ❌ Distorsionar (cambiar proporciones)
- ❌ Agregar sombras, bordes, efectos no autorizados
- ❌ Cambiar colores del logo
- ❌ Colocar logo sobre fondos que impidan legibilidad
- ❌ Usar logos de menos de 80px de ancho
- ❌ Usar archivo que no sea de `BRANDING_OFFICIEL/logos/`

---

## PROTOCOLO DE BÚSQUEDA AUTOMÁTICA DE ACTIVOS (DS-020)

```
CUANDO CLAUDE NECESITA UN ACTIVO DE MARCA:

PASO 1 → Buscar en 05_MARKETING/BRANDING_OFFICIEL/
  ✅ Encontrado → usar directamente
  ❌ No encontrado → PASO 2

PASO 2 → Buscar en 05_MARKETING/99_BRANDING_GLOBAL/ y 10_MEMORIA_EMPRESARIAL/
  ✅ Encontrado → copiar a BRANDING_OFFICIEL/ y usar
  ❌ No encontrado → PASO 3

PASO 3 → Generar alerta ALERT_ACTIVO_FALTANTE
  → Notificar a Daniel con ruta exacta que se buscó
  → NUNCA preguntar al usuario "¿tienes el logo?"
  → NUNCA continuar con substituto no oficial
  → Si es un logo: activar REGLA 7 y detener la tarea
```

---

## CHECKLIST PARA AGENTES — ANTES DE CUALQUIER ENTREGABLE VISUAL

```
□ 1. ¿El logo oficial existe en BRANDING_OFFICIEL/logos/?       [REGLA 7: STOP si no]
□ 2. ¿El verde oscuro en la pieza es #052B16?                   [no #1E3A20]
□ 3. ¿El teléfono 514-266-2504 está en dorado #C8A45A?          [siempre]
□ 4. ¿El logo está en posición correcta y tamaño mínimo 80px?   [ver tabla arriba]
□ 5. ¿El paquete ZIP incluye carpeta /branding/ con 4 archivos? [obligatorio]
□ 6. ¿Todo el texto para cliente está en francés?               [DS-009]
□ 7. ¿Las fuentes son Georgia/Playfair + Montserrat/Arial?      [tipografía oficial]
□ 8. ¿El tagline final es "Soumission gratuite · Sans engagement"? [CTA estándar]
```

---

## JERARQUÍA DE PIEZAS VISUALES

### Reel / Video
- Escena CTA: overlay negro 40–50% + texto blanco + teléfono dorado
- Logo: inferior-izquierda, fade in en los últimos 5 segundos
- Etiqueta "Avant": rojo `#CC3333` (temporal — solo en escena avant)
- Etiqueta "Après": verde oscuro `#052B16` + texto dorado `#C8A45A`

### Carrusel
- Portada (slide 1): imagen hero + overlay + título Georgia blanco
- Slides texto: fondo crema `#F5F2EB` + texto verde oscuro `#052B16`
- Slide final CTA: fondo verde oscuro `#052B16` + teléfono dorado `#C8A45A`
- Logo en todos los slides: inferior-derecha o inferior-izquierda

### Meta Ads estático
- Headline: máximo 40 caracteres, impacto directo
- Descripción: incluir "Soumission gratuite · Sans engagement"
- CTA button: "Obtenir un devis" o "Appeler maintenant"
- Imagen: siempre la de mayor score FLOAT del paquete

---

## TONO DE COMUNICACIÓN (cliente = francés)

**Estilo:** Aspiracional y cálido. Habla del resultado, no del proceso.  
**Urgencia:** Sin presión ("Dernières disponibilités" — no "¡LLAME AHORA!")  
**Propuesta sin riesgo:** Siempre incluir "Soumission gratuite · Sans engagement"

### Prohibido en comunicaciones
- ❌ Hablar de precios sin antes hablar de valor
- ❌ Comparaciones negativas con competidores
- ❌ Promesas no verificables ("Le meilleur de Montréal")
- ❌ Puntuación excesiva (!!!, ???)
- ❌ Errores ortográficos en francés — siempre verificar

---

## ALERTAS ACTIVAS

| # | Alerta | Acción requerida |
|---|--------|-----------------|
| ⚠️ 1 | Logos Groupe Ideal son capturas de pantalla (baja resolución) | Daniel: proveer archivos SVG/AI/PNG con fondo transparente |
| ⚠️ 2 | No existe logo Groupe Ideal con fondo transparente | Solicitar a agencia o recrear vectorialmente |
| ✅ 3 | Logos Jardín Ideal disponibles en buena resolución | Listo para uso |
| ✅ 4 | Logos Groupe Ideal tienen nombres canónicos (v2.0) | `PRINCIPAL / COMPACT / DARK` — confirmado |

---

*BRAND_RULES.md — Jardín Ideal AI System · DS-020 v2.0 · 2026-06-25*  
*Regla permanente — requiere aprobación de Daniel para modificar*
