# AUDITORÍA TÉCNICA REAL — Landing Page Cour Arrière V1
**Fuente:** `00_INBOX_MANUS/LANDING_PAGES/2026-06-24_COUR_ARRIERE_V1_NOTES.md.txt` (263 KB HTML real)
**Fecha auditoría:** 2026-06-24
**Versión auditada:** V1 — prototipo Manus
**Auditor:** Claude Code — análisis de archivo local

---

## SCORE GLOBAL: 68 / 100

| Dimensión | Score | Peso |
|-----------|-------|------|
| Estructura comercial | 16/20 | 20% |
| Tablas de precios | 8/10 | 10% |
| Calculadora de estimación | 7/10 | 10% |
| Calculadora de financiamiento | 5/10 | 10% |
| Formularios | 6/15 | 15% |
| Integración Pipedrive/Zapier | 2/10 | 10% |
| UX móvil | 9/10 | 10% |
| Textos en francés | 9/10 | 10% |
| Errores técnicos | 3/5 | 5% |
| Conversión | 3/5 | 5% |

**Veredicto: NO lista para publicar.** Bloqueantes críticos en formulario (Loi 25 + Pipedrive) y datos no confirmados.

---

## 1. ESTRUCTURA COMERCIAL

**Score: 16/20**

### Secciones presentes
| Sección | Estado | Observación |
|---------|--------|-------------|
| Topbar con tel + email | ✅ | `514-266-2504` + `info@jardin-ideal.com` |
| NAV sticky | ✅ | `position:sticky;top:0` — correcto |
| Hero | ✅ | Imagen + headline + 2 CTAs + trust pills |
| Intro + precio range | ✅ | "$8,000 – $75,000+" con contexto |
| Tabla de precios | ✅ | 4 columnas, 9 filas + total |
| Sidebar sticky (desktop) | ✅ | CTA + stats block |
| Estimateur interactivo | ✅ | Checkboxes con imágenes — funcional |
| Mini-calc financement (inline) | ✅ | Integrado en estimateur |
| Secciones de servicios | ✅ | 4 servicios detallados + clés en main |
| Galerie réalisations | ✅ | 9 proyectos con hotspots interactivos |
| Pourquoi nous | ✅ | 4 tarjetas numeradas |
| Checklist entrepreneur | ✅ | 8 preguntas — diferenciador fuerte |
| Testimonials | ✅ | 3 avis Google reales con nombres/barrio |
| FAQ | ⚠️ | Solo 5 preguntas (mínimo recomendado: 10) |
| Financement section | ✅ | Con modal de pré-qualification 3 pasos |
| Calculateur financement (full) | ❌ | **AUSENTE** — el HTML no contiene el bloque `#calc-section` |
| Formulaire soumission | ⚠️ | Existe pero es stepper (sin campos clave) |
| Politique de confidentialité | ✅ | Sección `#confidentialite` presente y con contenido Loi 25 |
| Footer | ✅ | 4 columnas, redes sociales, QR code |
| Sticky mobile bar | ✅ | CTA doble: llamar + soumission |
| Chatbot Alex | ✅ | Burbuja + ventana chat funcional |
| Meta Pixel | ⚠️ | `fbq('init', 'TU_PIXEL_ID')` — placeholder SIN ID real |

### Orden observado vs recomendado
El orden es comercialmente sólido. Punto de mejora: la calculadora de financement completa (con slider + tasa + duración + resultado) está ausente como sección autónoma — solo existe integrada en el estimateur como mini-calc.

---

## 2. HERO

**Score: bien ejecutado** — Fortalezas y debilidades:

**✅ Fortalezas:**
- Headline impactante: *"Transformez votre arrière-cour en espace de vie"*
- 2 CTAs diferenciados: soumission + estimateur
- Trust pills: 1500+ projets, 15 ans, Garantie 5 ans, RBQ
- Animación `hzoom` sutil en imagen hero
- Eyebrow "Experts paysagistes depuis 2009"

**⚠️ Débil:**
- Rating "⭐ 4.9/5 sur Google · +200 projets réalisés" contradice el trust pill "1 500+ projets réalisés" — inconsistencia interna
- La imagen hero `patio_arriere_pub.webp` es una ruta relativa — si el HTML se abre localmente sin el archivo, aparece roto

**❌ Ausente:**
- No hay prueba social inmediata debajo del hero (barre de confiance con logos/badges)
- El número de teléfono no es visible en el hero (solo en topbar y nav)

---

## 3. TABLA DE PRECIOS

**Score: 8/10**

**✅ Bien ejecutado:**
- 4 columnas: Entrée de gamme / Milieu de gamme / Haut de gamme / Prestige
- Milieu de gamme destacado visualmente (`highlight`)
- 9 servicios con rangos coherentes
- Row total "Forfait Cour Arrière Complète" con todos los niveles
- Disclaimer claro: `* Les prix sont établis à partir de données internes...`
- Overflow horizontal en mobile: `overflow-x:auto`

**⚠️ Mejoras:**
- El nombre de columnas es diferente al protocolo (Essentiel/Standard/Premium/Signature) — no es bloqueante pero crea inconsistencia si se replica como plantilla
- El total de "Forfait Cour Arrière Complète" arranca en $50,000 (entry) — puede desincentivar leads de proyectos medianos que ven el total primero
- Falta badge "Le plus populaire" en la columna Milieu de gamme (solo en tabla, sí existe en sección de servicios)

---

## 4. CALCULADORA DE ESTIMACIÓN

**Score: 7/10**

### Estructura real detectada
```
Variables activas:
1. Type de propriété (select: Unifamiliale ×1 / Maison de ville ×1.2 / Condo ×0.8 / Grande ×1.5)
2. Taille de la cour (tarjetas S/M/L/XL con multiplicadores: 0.55 / 1.0 / 1.6 / 2.4)
3. Services à inclure (8 checkboxes con imágenes reales)

Precios base por servicio:
- Patio pavé uni: à partir de 6,500$ (varía con taille)
- Terrasse composite: à partir de 7,500$
- Pergola/Gazebo: à partir de 4,000$
- Piscine creusée: à partir de 35,000$
- Cuisine extérieure: à partir de 8,000$
- Clôture & murets: à partir de 3,500$
- Éclairage extérieur: à partir de 1,500$
- Aménagement paysager: à partir de 2,500$
```

**✅ Bien ejecutado:**
- Tarjetas visuales S/M/L/XL con referencias comprensibles (~X stationnements)
- Checkboxes con foto del servicio — UX superior a selects
- Disclaimer de estimations indicatives visible
- CTA posterior al resultado
- Lógica de precio al pi² coherente con el mercado

**⚠️ Problemas:**
- NO hay variable de niveau de finition (économique/standard/premium/luxe) — la calculadora solo varía por tipo de propiedad + tamaño + servicios
- NO hay variable de tipo de terrain (plat/pente/accès difficile)
- El resultado muestra "à partir de X$" pero no un rango min/base/max — el cliente no ve el spread de incertidumbre
- Mini-calc de financement integrado usa **240 mois como único valor fijo** — esto es engañoso (ver sección 5)

---

## 5. CALCULADORA DE FINANCIAMIENTO

**Score: 5/10**

### Problema crítico: duración fija en 240 meses

El mini-calc integrado en el estimateur tiene la duración **hardcodeada en 240 mois** (20 años):
```html
<input type="hidden" id="miniMonths" value="240">
```
Y en el modal de pré-qualification también:
```html
<span style="font-family:var(--fh);font-weight:800;font-size:1rem;color:var(--dark)">240 mois</span>
<input type="hidden" id="pqDuree" value="240">
```

**Esto es engañoso**: mostrar solo la mensualidad más baja posible (240 meses) sin que el usuario pueda modificar la duración distorsiona la percepción de costo real. Un proyecto de $15,000 a 240 meses puede costar $30,000+ en intereses totales.

### Calculadora de financement completa
**AUSENTE**: No existe la sección `#calc-section` con slider de monto, selector de tasa y selector de duración como sección independiente. Solo existe el mini-calc embebido en el estimateur.

### Disclaimer presente
El mini-calc sí incluye el disclaimer legal:
> *"Le taux d'intérêt applicable est déterminé par notre partenaire financier... Les montants présentés sont indicatifs seulement. Taux final communiqué lors de l'approbation. Sous réserve d'approbation du crédit. Jardin Idéal agit à titre d'intermédiaire et ne prend aucune décision de crédit."*

**Correcto** — este texto debe mantenerse.

### Formulario de pré-qualification (modal)
**✅ Bien estructurado:** 3 pasos (identité + projet + profil financier)
**⚠️ Problema:** El botón final `pqSubmit()` probablemente no está conectado a ningún backend real (verificar JS)

---

## 6. FORMULARIOS

**Score: 6/15** — El más problemático

### Formulario principal: Questionnaire stepper (5 pasos)

El formulario es un **stepper interactivo de 5 preguntas** con opciones visuales (tarjetas con imágenes), seguido de un formulario de coordonnées. **No es un formulario HTML tradicional**.

**Campos de contacto detectados (coordsForm):**
- Prénom ✅
- Nom ✅
- Téléphone ✅
- Courriel ✅
- Ville ✅
- Code postal ✅
- Notes/questions (textarea) ✅
- Upload de fotos ✅

**Campos ocultos presentes:**
- `hUtmSource`, `hUtmMedium`, `hUtmCampaign`, `hUtmContent` ✅
- `hServicePage` = "cour-arriere" ✅
- `hLandingUrl`, `hFormName`, `hDateSubmitted` ✅

**PROBLEMAS CRÍTICOS:**

| Problema | Gravedad | Detalle |
|---------|---------|---------|
| **Sin checkbox de consentement Loi 25** | 🔴 CRÍTICO | Solo hay texto "vous acceptez notre politique de confidentialité" — NO es un checkbox marcado activamente por el usuario |
| **Sin campo "adresse du projet"** | 🟠 ALTO | Solo hay "Ville" y "Code postal" — no hay adresse completa |
| **Sin campo "superficie"** | 🟠 ALTO | El stepper pregunta tipo de projet pero no superficie exacta |
| **Sin campo "budget"** | 🟠 ALTO | No hay campo de presupuesto declarado por el cliente |
| **Sin campo "source"** | 🟠 ALTO | No hay campo de fuente (Facebook/Google/recommandation) |
| **Sin campo "date souhaitée"** | 🟡 MEDIO | No hay campo de fecha de inicio deseada |
| **Sin campo "terrain_pente"** | 🟡 MEDIO | No hay pregunta sobre tipo de terreno |
| **Sin ICS pre-score** | 🟠 ALTO | No hay cálculo automático de calificación del lead |
| **Sin campos data-pipedrive** | 🔴 CRÍTICO | Los campos no tienen atributos de mapping para Pipedrive/Zapier |
| **submitForm() no conectado** | 🔴 CRÍTICO | La función JS de envío probablemente no está conectada a un endpoint real |

### Formulario de pré-qualification financement
**Campos detectados:** prénom, nom, téléphone, courriel, ville, service, montant, miseFonds, emploi, revenu, crédit, délai
**✅ Más completo que el formulario principal**
**❌ Sin checkbox de consentement explícito** (solo texto referenciando política)
**❌ Sin endpoint de envío configurado**

---

## 7. CAMPOS PARA PIPEDRIVE / INTEGRACIÓN ZAPIER

**Score: 2/10**

### Estado actual
Los campos del formulario NO tienen atributos `name` normalizados para Pipedrive ni ningún mapping explícito. La integración está completamente ausente.

### Campos mínimos requeridos para Pipedrive

**Deal:**
| Campo LP | → Campo Pipedrive | Tipo |
|----------|------------------|------|
| prenom + nom | Person Name | Text |
| telephone | Phone | Tel |
| email | Email | Email |
| ville + code_postal | custom_adresse_projet | Text |
| type_projet (del stepper) | custom_type_projet | Text |
| superficie (del stepper) | custom_superficie | Text |
| budget declarado | custom_budget_client | Text |
| source | custom_source_lead | Text |
| utm_source | custom_utm_source | Text |
| utm_campaign | custom_utm_campaign | Text |
| ics_score (calculado) | custom_ics_score | Number |
| ics_classification (A/B/C) | custom_ics_classification | Text |

**Auto-nota Pipedrive requerida:**
```
[LEAD LP Cour Arrière V1]
Source: {utm_source} / {utm_campaign}
ICS: {ics_score}/100 → {ics_classification}
Délai contact recommandé: {delai_appel}
Projet: {type_projet} · {superficie}
Budget déclaré: {budget}
Ville: {ville}
Message: {notes}
```

**Zap requerido:**
- Trigger: Webhook POST al enviar formulario
- Action 1: Crear/buscar Person en Pipedrive
- Action 2: Crear Deal en pipeline "Leads qualifiés"
- Action 3: Agregar Note con template auto
- Action 4: Crear Activity "Appeler dans Xh"

### Campo `source_page` detectado
El campo `hServicePage` value="cour-arriere" ya existe — puede usarse como base para el Zap.

---

## 8. UX MÓVIL

**Score: 9/10**

### Elementos mobile correctamente implementados
- `font-size:16px` en todos los inputs (previene zoom iOS) ✅
- Sticky bar inferior (double CTA: llamar + soumission) ✅
- `@media(max-width:768px)` completo con ajustes de todas las secciones ✅
- Hero `min-height:90vh` en mobile ✅
- Grillas colapsan a 1 columna ✅
- Tabla de precios con `overflow-x:auto` ✅
- Chat window ajustada: `width:calc(100vw - 32px)` ✅
- Imagen hero con `object-fit:cover` ✅
- `@media(max-width:480px)` con ajustes adicionales ✅
- `prefers-reduced-motion` — NO detectado (oportunidad de mejora)

**Único problema:**
- El article layout desktop (2 columnas: content + sidebar) usa `position:sticky` para el sidebar — en tablet 1024px se colapsa correctamente, pero en 768–1024px podría dar overflow horizontal en algunos dispositivos

---

## 9. TEXTOS EN FRANCÉS

**Score: 9/10**

**✅ Correcto:**
- Todo el contenido visible está en francés canadiense
- Vocabulario local: "cour arrière", "pavé uni", "soumission", "mise de fonds"
- Ortografía local: "courriel" (no "email" en formularios)
- Ton profesional y accesible — no demasiado formal
- Vouvoiement consistente

**⚠️ Pequeños errores detectados:**
- Topbar: `info@jardin-ideal.com` pero el protocolo interno usa `daniel@groupe-ideal.com` — courriel de contacto incorrecto para leads
- Footer: `© 2025 Jardin Idéal` — debería ser `© 2026`
- Mini-calc explainer: *"Comment ca fonctionne ?"* — falta acento: "Comment ça fonctionne ?"
- El link "Conditions d'utilisation" en el footer no tiene página destino (`href="#"`)

---

## 10. ERRORES TÉCNICOS

**Score: 3/5**

| Error | Gravedad | Detalle |
|-------|---------|---------|
| Meta Pixel ID placeholder | 🔴 CRÍTICO | `fbq('init', 'TU_PIXEL_ID')` — no hay tracking real de conversiones |
| Inconsistencia datos hero | 🟠 ALTO | "+200 projets réalisés" vs "1 500+" en trust pills |
| Duración financement hardcoded 240M | 🟠 ALTO | Ver sección 5 |
| "ça" sin acento | 🟡 BAJO | "Comment ca fonctionne" |
| Copyright 2025 | 🟡 BAJO | Debería ser 2026 |
| Links sociales genéricos | 🟡 BAJO | `facebook.com/jardinideal` — verificar que sea la URL real |
| `admin-cour-arriere.html` visible | 🟡 BAJO | Link admin en topbar y footer — debería ocultarse en producción |
| `prefers-reduced-motion` ausente | 🟡 BAJO | Accesibilidad — animaciones hzoom/pulse sin respeto de preferencias OS |
| Garantie piscine inconsistente | 🟠 ALTO | Hotspot piscine dice "garantie 10 ans structure" pero trust pill y checklist dicen "5 ans" |

---

## 11. ELEMENTOS QUE AFECTAN CONVERSIÓN

### Positivos (mantener)
1. **Checklist entrepreneur** — diferenciador real, responde objeciones preventivamente
2. **Galería con hotspots** — UX innovadora, mantiene engagement
3. **3 testimonios Google reales** con nombre completo y barrio — alta credibilidad
4. **RBQ number visible** en múltiples lugares — confianza legal
5. **Sticky bar mobile** — CTA siempre presente en mobile
6. **Estimateur visual** con fotos de servicios — mucho mejor que selects

### Negativos (corregir)
1. **Formulario stepper** sin checkbox de consentement — **bloquea legalmente la publicación**
2. **Meta Pixel sin ID real** — gasto publicitario sin datos de conversión
3. **Mini-calc fijado a 240 meses** — puede generar conversaciones incómodas cuando el cliente recibe el taux real
4. **5 FAQ insuficientes** — Google puede penalizar y usuarios tienen más preguntas
5. **Sin barre de confiance** inmediata post-hero — se pierde momento de credibilidad
6. **"Pré-approuvé"** en confirmación del modal de financement — afirmación prematura sin verificar dossier (riesgo legal)

---

## RESUMEN DE PRIORIDADES

### 🔴 CRÍTICO — Bloquea publicación (hacer antes de conectar a Meta Ads)
1. Agregar checkbox de consentement (Loi 25) en formulario soumission
2. Agregar checkbox de consentement en modal de financement
3. Reemplazar `TU_PIXEL_ID` con el ID real del Meta Pixel
4. Conectar `submitForm()` a endpoint real (Zapier webhook)
5. Eliminar "Pré-approuvé" automático en confirmación financement

### 🟠 ALTO — Impacta conversión y calidad de leads
6. Agregar campo `adresse du projet` en formulaire
7. Agregar campo `source` (comment avez-vous connu?) en formulaire
8. Agregar campo `budget` en formulaire
9. Resolver inconsistencia "+200 projets" vs "1 500+"
10. Resolver inconsistencia garantie piscine (10 ans vs 5 ans)
11. Corregir courriel de contacto: `info@jardin-ideal.com` → `daniel@groupe-ideal.com`
12. Agregar calculadora de financement completa (con selector de tasa y duración)
13. Permitir seleccionar duración en mini-calc (no solo 240 meses)

### 🟡 MEJORAS — Optimización de conversión y calidad
14. Expandir FAQ: 5 → 10 preguntas mínimo
15. Agregar barre de confiance post-hero
16. Corregir copyright 2025 → 2026
17. Corregir "ca" → "ça"
18. Ocultar links `admin-cour-arriere.html` en producción
19. Verificar URLs redes sociales
20. Agregar `prefers-reduced-motion`

---

*Auditoría basada en análisis real del archivo HTML local · Jardín Ideal AI System · 2026-06-24*
*Siguiente paso: aplicar correcciones críticas en Manus → exportar V2 → comparar*
