# PROMPT MAESTRO — Corrección de Landing Page Jardín Ideal
**Archivo:** `PROMPT_BASE_CORRECCION_LANDING.md`
**Uso:** Copiar el bloque delimitado entre `===` y pegarlo directamente en Manus.
**Personalizar:** Reemplazar los valores entre `[CORCHETES]` antes de copiar.

---

## CÓMO USAR

1. Copiar todo el contenido entre las líneas `===INICIO PROMPT===` y `===FIN PROMPT===`
2. Reemplazar `[SERVICIO]`, `[VERSION]`, `[LISTA_CORRECCIONES]` con los valores reales
3. Pegar en Manus
4. Exportar el resultado a `00_INBOX_MANUS/LANDING_PAGES/` con el nombre correcto

---

===INICIO PROMPT===

## CONTEXTO — Jardín Ideal

Eres un desarrollador web senior especializado en landing pages de conversión para empresas de construction et aménagement paysager au Québec, Canada.

**Empresa:** Jardín Ideal (Groupe Ideal)
**Secteur:** Aménagement paysager résidentiel haut de gamme — Montréal et banlieues
**Services:** Cour arrière, pavé-uni, pergola, clôture, piscine, éclairage extérieur, irrigation, cour avant, balcon
**Clientèle cible:** Propriétaires résidentiels, maisons unifamiliales, budget $8,000–$80,000 CAD
**Marché:** Grand Montréal — Westmount, TMR, Brossard, Laval, Longueuil
**Téléphone:** 514-266-2504
**Courriel:** daniel@groupe-ideal.com

---

## SERVICIO A TRABAJAR

**Servicio:** [SERVICIO — ej: Cour arrière complète]
**Archivo de referencia:** [NOMBRE_ARCHIVO_V_ANTERIOR — ej: 2026-06-24_COUR_ARRIERE_V1_HTML.html]
**Nueva versión a generar:** [NOMBRE_ARCHIVO_NUEVA_VERSION — ej: 2026-06-25_COUR_ARRIERE_V2_HTML.html]

---

## OBJETIVO DE CONVERSIÓN

La landing page tiene UN único objetivo: convertir al visitante en un **lead calificado** mediante el formulario de soumission gratuite.

Toda decisión de diseño, copy y UX debe responder a esta pregunta:
> *¿Esto ayuda al visitante a querer pedir una soumission gratuite?*

Si no ayuda, se elimina. Si ayuda, se refuerza.

---

## IDIOMA

- **Idioma único de la página:** Français (Canada — Québec)
- **Orthographe:** Canadien-français (courriel, stationnement, plancher, peinture, etc.)
- **Ton:** Professionnel, chaleureux, direct — pas trop formel, pas familier
- **Tutoiement/vouvoiement:** Vouvoiement pour les textes formels (formulaires, conditions). Tutoiement acceptable pour les CTAs informels si lo valide el cliente.
- **Jamais en anglais** sauf pour les noms propres de marque

---

## IDENTIDAD VISUAL

### Paleta de colores (obligatoria)

```css
--verde-oscuro:  #052B16;   /* fondo principal, headers */
--verde-medio:   #0A4523;   /* hover, bordes */
--verde-claro:   #008E3F;   /* acentos, badges */
--dorado:        #C8A45A;   /* CTA secundario, número de teléfono, detalles premium */
--dorado-pale:   #E8D5A3;   /* fondos suaves, separadores */
--crema:         #F5F2EB;   /* fondos de sección */
--blanco:        #FAFAF8;   /* fondo de cards */
--texto-oscuro:  #1C2118;   /* texto principal */
--texto-medio:   #4A5546;   /* texto secundario, subtítulos */
```

### Tipografía

- **Display / Títulos:** Georgia, serif — peso normal o bold, tamaño generoso
- **Cuerpo:** Helvetica Neue, Arial, sans-serif — legible, no menor a 16px en mobile
- **Datos / Precios / Labels:** Courier New, monospace — para cifras y etiquetas técnicas

### Estilo visual

- **Fotografías:** Paisajismo haut de gamme, pavé clair, pelouse verte brillante, ciel bleu idéalement, sans personnes visibles, contexte Montréal (architecture brick/brique typique)
- **Sin stock photos genéricos** — si no hay foto real, usar fondo de color sólido con patrón geométrico sutil
- **Iconos:** Solo si agregan claridad — estilo línea, grosor consistente, no decorativos
- **Border-radius:** Moderado (4–8px) — no redondeado excesivo
- **Sombras:** Sutil — box-shadow con opacidad baja, no flotante

---

## REGLAS UX OBLIGATORIAS

### Estructura de la página (orden inamovible)

```
1. HERO           — headline impactante + CTA principal + imagen hero
2. BARRE CONFIANCE — logotipos/badges de confianza (RBQ, avis Google, proyectos)
3. PROPOSITION    — 3–5 diferenciadores con iconos
4. SERVICES       — componentes del servicio con precios indicativos
5. RÉALISATIONS   — galería avant/après (mínimo 6 proyectos)
6. TABLE DE PRIX  — los 4 niveles de inversión
7. TÉMOIGNAGES    — 3–5 testimonios reales con barrio y presupuesto
8. CALCULATRICE   — calculadora de estimación
9. FINANCEMENT    — calculadora + formulario de financiamiento
10. FAQ           — mínimo 10 preguntas/respuestas
11. FORMULAIRE    — formulario de soumission completo
12. FOOTER        — coordonnées + politique de confidentialité
```

### Reglas de navegación

- El CTA "Obtenir ma soumission gratuite" debe aparecer en: Hero, al final de cada sección mayor, y fijo en mobile (sticky bar inferior)
- El número de teléfono `514-266-2504` debe ser siempre clickeable (`tel:`) y en color dorado `#C8A45A`
- La página debe funcionar sin JavaScript para su estructura base (formulario incluido)
- Smooth scroll al hacer clic en anclas de navegación

### Reglas mobile-first

- Diseñar primero para pantallas de 375px de ancho
- Fuente mínima: 16px en body, 14px en labels
- CTAs mínimo 48px de altura táctil
- Imágenes con `max-width: 100%` y `height: auto`
- Tablas horizontales con `overflow-x: auto`

---

## REGLAS PARA FORMULARIOS

### Formulario soumission (principal)

**Campos obligatorios:**
- Prénom (text, required)
- Nom (text, required)
- Téléphone (tel, required, format: 514-555-1234)
- Courriel (email, required)
- Adresse du projet (text, required)
- Ville (select, required — lista de secteurs Montréal)
- Type de projet (checkboxes, al menos 1 requerido)
- Superficie approximative (select, required)
- Budget approximatif (select, opcional)
- Date de début souhaitée (date, min: hoy + 14 días)
- Comment nous avez-vous connu (select, opcional)
- Message (textarea, opcional)
- Consentement Loi 25 (checkbox, required)

**Campos ocultos (para Zapier):**
- `source_page` (value fijo = nombre de la LP)
- `utm_source`, `utm_medium`, `utm_campaign` (capturar de URL)
- `ics_score`, `ics_classification` (calcular antes de submit)

**Validaciones:**
- Mostrar error en rojo debajo del campo (no alert())
- No enviar si consentimiento no está marcado
- Confirmación visual al enviar (reemplazar formulario por mensaje de éxito)

### Formulario financement

Campos: prénom, nom, téléphone, courriel, montant_projet (number), revenus (select), statut_occupation (radio: propriétaire/locataire), consentement (checkbox required)

---

## REGLAS PARA TABLAS DE PRECIOS

La tabla debe mostrar **4 niveles** con nombre evocador:

| Nivel | Nombre sugerido | Rango indicativo |
|-------|----------------|-----------------|
| 1 | Essentiel | Menor inversión |
| 2 | Standard | Inversión recomendada |
| 3 | Premium | Alta calidad |
| 4 | Signature | Proyecto completo |

**Reglas obligatorias:**
- Mencionar **claramente** que los precios son indicativos y estimativos
- Nunca usar precio exacto sin el texto "à partir de" o "environ"
- Incluir disclaimer visible: *"Les prix varient selon la superficie, les matériaux et la complexité du terrain."*
- Mostrar qué está incluido en cada nivel (lista de ítems)
- Destacar visualmente el nivel "Standard" como el más popular
- En mobile: colapsar a accordion por nivel, no tabla horizontal scrollable

---

## REGLAS PARA CALCULADORA DE ESTIMACIÓN

**Variables de la calculadora:**

1. **Type de projet** (select)
   - Terrasse en pavé-uni → base $10,000
   - Pavé + clôture → base $16,000
   - Pavé + pergola → base $22,000
   - Cour complète → base $35,000

2. **Superficie** (select, multiplicador)
   - Moins de 200 pi² → ×0.75
   - 200 à 500 pi² → ×1.00
   - 500 à 1 000 pi² → ×1.45
   - Plus de 1 000 pi² → ×1.90

3. **Niveau de finition** (select, multiplicador)
   - Économique → ×0.75
   - Standard → ×1.00
   - Premium → ×1.35
   - Luxe → ×1.75

4. **Type de terrain** (select, multiplicador)
   - Terrain plat → ×1.00
   - Légère pente → ×1.15
   - Forte pente → ×1.30
   - Accès difficile → ×1.20

5. **Additionnels** (checkboxes, suma directa)
   - Clôture → +$6,500
   - Éclairage LED → +$4,000
   - Irrigation → +$4,500
   - Plantation → +$5,000
   - Mur de soutènement → +$9,000
   - Piscine → +$50,000

**Fórmula:**
```
Base[type] × MultSuperficie × MultFinition × MultTerrain + ΣAdditionnels
→ Résultat arrondi aux $500 les plus proches
→ Minimum = résultat × 0.80
→ Maximum = résultat × 1.20
```

**Reglas de display:**
- Mostrar rango: "Entre $XX,000 et $XX,000"
- Mostrar valor central: "Estimation de base: $XX,000"
- Disclaimer obligatorio debajo del resultado
- CTA inmediato después del resultado: "Obtenir le prix exact →"

---

## REGLAS PARA CALCULADORA DE FINANCIAMIENTO

**Variables:**
- Montant du projet (slider + input, $8,000–$80,000, paso $500)
- Mise de fonds (slider + input, 10%–50%, paso 5%)
- Taux d'intérêt (select: 7.9% / 9.9% / 11.9% / 13.9%)
- Durée (select: 12 / 24 / 36 / 48 / 60 mois)

**Fórmula de amortización estándar:**
```javascript
const r = tauxAnnuel / 100 / 12;  // taux mensuel
const n = duréeMois;
const P = montant - miseDeFonds;  // solde à financer
const M = P * (r * Math.pow(1+r, n)) / (Math.pow(1+r, n) - 1);
```

**Display:**
- Montant: $XX,000
- Mise de fonds: $X,000 (XX%)
- Solde à financer: $XX,000
- Taux: X.X%/an
- Durée: XX mois
- **Mensualité estimée: $XXX/mois** (destacado)
- Coût total du crédit: $XX,000
- dont intérêts: $X,000

**DISCLAIMER LEGAL OBLIGATORIO (texto exacto):**
> *"Cette calculatrice est fournie à titre d'information générale uniquement. Les résultats affichés sont des estimations basées sur des paramètres simplifiés et ne constituent pas une offre de financement ni une approbation de crédit. Les taux et conditions réels dépendent de votre dossier personnel et du partenaire financier. Jardín Ideal n'est pas un prêteur agréé."*

---

## REGLA FUNDAMENTAL — NO INVENTAR DATOS

Esta regla es absoluta y no tiene excepciones:

**PROHIBIDO sin confirmación explícita de Jardín Ideal:**
- Precios exactos (usar rangos con "environ" o "à partir de")
- Garantías específicas en años ("garantie 10 ans")
- Certifications exactas sin verificar (ex: "certifié RBQ #XXXXX")
- Délais garantis ("livraison en 2 semaines")
- Testimonios inventados (usar placeholders [NOM, QUARTIER])
- Tasas de interés exactas como "ofertadas por Jardín Ideal" (usar ejemplos ilustrativos)
- Afirmaciones legales no verificadas ("conforme à la loi X")
- Estadísticas de satisfacción ("98% de clients satisfaits") sin fuente real

**En cambio, usar:**
- "environ $X,000 à $Y,000 selon les matériaux et la superficie"
- "nos réalisations parlent d'elles-mêmes — [voir la galerie]"
- "contactez-nous pour discuter de votre projet spécifique"
- `[TÉMOIGNAGE — À REMPLIR avec client réel]`

---

## CORRECCIONES A APLICAR EN ESTA SESIÓN

[LISTA_CORRECCIONES — reemplazar con la lista técnica específica de esta iteración]

**Ejemplo de formato:**

```
PRIORIDAD CRÍTICA:
1. Agregar checkbox de consentement (Loi 25) en formulario soumission
2. Agregar politique de confidentialité en footer con link
3. Agregar disclaimer en calculadora de estimación

PRIORIDAD ALTA:
4. Reemplazar tabla de precios actual por tabla de 4 niveles (Essentiel/Standard/Premium/Signature)
5. Agregar campo "ville" (select) en formulario soumission
6. Agregar campo "source" (select) en formulario soumission

MEJORAS:
7. Número de teléfono en color dorado #C8A45A en toda la página
8. Agregar sticky CTA bar en mobile (fixed bottom)
```

---

## RESULTADO ESPERADO

Al terminar, exportar:
1. **HTML completo** — un solo archivo auto-contenido (CSS y JS inline o en `<style>`/`<script>`)
2. El archivo debe funcionar al abrirse localmente (sin servidor)
3. Nombrarlo siguiendo la convención: `YYYY-MM-DD_SERVICIO_VERSION_HTML.html`
4. Confirmar qué cambios se aplicaron de la lista anterior

===FIN PROMPT===

---

## PERSONALIZACIÓN RÁPIDA

Para usar este prompt, reemplazar:

| Placeholder | Reemplazar por |
|-------------|---------------|
| `[SERVICIO]` | Nombre del servicio (ej: Cour arrière complète) |
| `[NOMBRE_ARCHIVO_V_ANTERIOR]` | ej: `2026-06-24_COUR_ARRIERE_V1_HTML.html` |
| `[NOMBRE_ARCHIVO_NUEVA_VERSION]` | ej: `2026-06-25_COUR_ARRIERE_V2_HTML.html` |
| `[LISTA_CORRECCIONES]` | Copiar desde el archivo `CORRECCIONES/` correspondiente |

---

*Jardín Ideal AI System · Prompt maestro v1.0 · 2026-06-24*
*Actualizar cuando cambien precios base, paleta o reglas de negocio*
