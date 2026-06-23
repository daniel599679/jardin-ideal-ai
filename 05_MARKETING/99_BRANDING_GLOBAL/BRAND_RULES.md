# BRAND RULES — JARDÍN IDEAL / GROUPE IDEAL
**Versión:** 1.0 | **Fecha:** 2026-06-23
**Directorio oficial:** `05_MARKETING/99_BRANDING_GLOBAL/`

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

### Información de contacto
- Teléfono: **514-266-2504** — siempre en color dorado #C8A45A en piezas visuales
- Web: jardin-ideal.com
- Zonas de servicio: Montréal · Laval · Rive-Nord

---

## LOGOTIPOS

### Logos disponibles — Jardín Ideal
```
99_BRANDING_GLOBAL/logos_renombrados/
├── LOGO_JARDIN_IDEAL_PRINCIPAL.png   ← PNG, fondo blanco, con hoja en É
└── LOGO_JARDIN_IDEAL_SOCIAL.jpg      ← JPEG, versión social media
```

### Logos disponibles — Groupe Ideal
```
99_BRANDING_GLOBAL/logos/groupe ideal/   ← pendiente de recibir archivos
```

### Cada paquete de producción incluye copia local
```
PAQUETE_PUBLICACION_FINAL/7_BRANDING/
├── LOGO_JARDIN_IDEAL_PRINCIPAL.png
├── LOGO_JARDIN_IDEAL_SOCIAL.jpg
└── BRANDING_INFO.txt
```

### Reglas de uso del logo
1. **Siempre usar el archivo oficial** — nunca redibujar ni reescribir el nombre a mano
2. El logo se coloca en la esquina **inferior-izquierda** en reels y slides
3. Tamaño mínimo: 80px de ancho en pantalla
4. No distorsionar (nunca cambiar proporciones)
5. Sobre fondos oscuros: usar el logo con fondo blanco o con versión en blanco si disponible
6. No agregar sombras, bordes o efectos no autorizados

---

## PALETA DE COLORES

| Nombre | HEX | Uso principal |
|--------|-----|---------------|
| Verde Oscuro | `#052B16` | Fondos, headers, overlays |
| Verde Claro | `#008E3F` | Color del logo, iconos, labels activos |
| Dorado | `#C8A45A` | Teléfono CTA, acentos premium |
| Crema | `#F5F2EB` | Fondos neutros, slides de texto |
| Blanco | `#FFFFFF` | Texto sobre oscuro |

**Referencia completa:** `99_BRANDING_GLOBAL/PALETA_COLORES.txt`

> ⚠️ El verde oscuro oficial es `#052B16`. Versiones anteriores del sistema usaban `#1E3A20` — ese valor es incorrecto y no debe usarse.

---

## TIPOGRAFÍA

| Rol | Fuente | Alternativa sistema |
|-----|--------|---------------------|
| Display / Títulos | Playfair Display / Georgia | Times New Roman |
| Cuerpo / UI | Montserrat | Arial, system-ui |
| Datos / Técnico | Courier New | Courier |

**Referencia completa:** `99_BRANDING_GLOBAL/FONT_GUIDE.txt`

---

## REGLAS PARA AGENTES DE IA

### Comportamiento obligatorio al inicio de cada sesión
```
1. Verificar existencia de 99_BRANDING_GLOBAL/
2. Leer PALETA_COLORES.txt y FONT_GUIDE.txt
3. Aplicar los colores oficiales en TODO contenido generado
4. Si se crea un paquete de producción → incluir 7_BRANDING/ con logos copiados
```

### Checklist de branding para cualquier entregable visual
- [ ] ¿El verde oscuro es #052B16? (no #1E3A20)
- [ ] ¿El verde claro es #008E3F?
- [ ] ¿El teléfono 514-266-2504 está en dorado #C8A45A?
- [ ] ¿El logo está en la posición correcta (inferior-izquierda)?
- [ ] ¿La carpeta 7_BRANDING/ existe y tiene los logos?
- [ ] ¿Todo el texto para cliente está en francés?
- [ ] ¿Las fuentes son Georgia/Playfair + Montserrat/Arial?

---

## JERARQUÍA DE PIEZAS VISUALES

### Reel / Video (CapCut / Manus)
- Escena CTA: overlay negro 40-50% + texto blanco + teléfono dorado
- Logo: inferior-izquierda, fade in en los últimos 5 segundos
- Etiqueta "Avant": rojo #CC3333 (temporal — solo en escena avant)
- Etiqueta "Après": verde oscuro #052B16 + texto dorado #C8A45A

### Carrusel (Canva)
- Portada (slide 1): imagen hero + overlay + título Georgia blanco
- Slides texto: fondo crema #F5F2EB + texto verde oscuro #052B16
- Slide final CTA: fondo verde oscuro #052B16 + teléfono dorado #C8A45A
- Logo en todos los slides: inferior-derecha o inferior-izquierda

### Meta Ads
- Headline: máximo 40 caracteres, impacto directo
- Descripción: incluir "Soumission gratuite · Sans engagement"
- CTA button: "Obtenir un devis" o "Appeler maintenant"
- Imagen: siempre la de mayor QC score del paquete

### Documentos internos (reportes, agentes, análisis)
- Pueden usar español (trabajo interno)
- Misma paleta de colores si se generan en HTML
- Logo no requerido pero recomendado en portada

---

## TONO DE COMUNICACIÓN

### Para clientes (francés)
- Aspiracional y cálido — habla del resultado, no del proceso
- Evitar jerga técnica innecesaria
- Crear urgencia sin presión ("Dernières disponibilités")
- Siempre incluir la propuesta sin riesgo ("Soumission gratuite · Sans engagement")

### Prohibido en comunicaciones
- ❌ Hablar de precios sin antes hablar de valor
- ❌ Comparaciones negativas con competidores
- ❌ Promesas no verificables ("Le meilleur de Montréal")
- ❌ Errores ortográficos en francés — revisar siempre

---

## CONFIGURACIÓN POR DEFECTO PARA NUEVOS AGENTES

Todo nuevo agente creado para Jardín Ideal debe incluir esta sección en su header:

```
## BRANDING — REFERENCIA OBLIGATORIA
Paleta  : 99_BRANDING_GLOBAL/PALETA_COLORES.txt
Tipog.  : 99_BRANDING_GLOBAL/FONT_GUIDE.txt
Logos   : 99_BRANDING_GLOBAL/logos_renombrados/
Reglas  : 99_BRANDING_GLOBAL/BRAND_RULES.md

Colores rápidos:
  #052B16 Verde oscuro  | #008E3F Verde claro
  #C8A45A Dorado        | #F5F2EB Crema   | #FFFFFF Blanco
Teléfono CTA: 514-266-2504 siempre en #C8A45A
```
