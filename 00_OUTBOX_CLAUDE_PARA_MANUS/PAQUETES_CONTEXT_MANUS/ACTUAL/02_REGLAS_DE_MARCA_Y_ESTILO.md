# REGLAS DE MARCA Y ESTILO — Jardín Ideal
**Paquete:** MANUS_CONTEXT_PACK · Documento 02/04
**Versión:** 1.0 · **Última actualización:** 2026-06-24
**Uso:** Cargar en Manus al inicio de cada sesión de diseño / desarrollo

---

## IDENTIDAD DE MARCA

| Dato | Valor |
|------|-------|
| Nombre empresa | Jardín Ideal / Groupe Ideal / Jardin Idéal |
| Nom commercial (FR) | Jardin Idéal |
| Teléfono | 514-266-2504 |
| Courriel oficial | info@jardin-ideal.com |
| Sitio web | jardin-ideal.com |
| Licencia RBQ | #5773-1983-01 |
| Assurance | Responsabilité civile 2 M$ |
| Fundación | 2009 (15+ ans d'expérience en 2024) |
| Proyectos realizados | 1 500+ |
| Mercado | Grand Montréal — Laval, Rive-Sud, Rive-Nord |
| Idioma landing pages | Français (Canada — Québec) |

---

## PALETA DE COLORES — OBLIGATORIA

```css
:root {
  /* Verdes */
  --verde-oscuro: #052B16;    /* fondo principal, headers, nav */
  --verde-medio:  #0A4523;    /* hover states, bordes activos */
  --verde-claro:  #008E3F;    /* acentos, tags, badges, checkboxes */
  --verde-sage:   #e8f0e8;    /* fondos suaves, alternativas */

  /* Dorado — NUNCA reemplazar */
  --dorado:       #C8A45A;    /* teléfono, detalles premium, highlights */
  --dorado-pale:  #E8D5A3;    /* versión suave para fondos */

  /* Neutros */
  --crema:        #F5F2EB;    /* fondos de sección alternativa */
  --crema-medio:  #F5F4F0;    /* variante existente en HTML */
  --blanco:       #FAFAF8;    /* fondo de cards */
  --blanco-puro:  #FFFFFF;    /* fondo formularios */
  --border:       #dde8dd;    /* bordes sutiles */

  /* Texto */
  --texto-oscuro: #1C2118;    /* cuerpo principal */
  --texto-medio:  #4A5546;    /* subtítulos, descripciones */
  --texto-suave:  #4a4a4a;    /* texto secundario */
}
```

**Regla absoluta:** El número de teléfono `514-266-2504` debe mostrarse siempre en `--dorado` (#C8A45A) cuando aparece sobre fondo oscuro.

---

## TIPOGRAFÍA

| Rol | Familia | Uso |
|-----|---------|-----|
| Display / Títulos | Montserrat (Google Fonts) | H1, H2, H3, tags, botones, labels |
| Cuerpo | Open Sans (Google Fonts) | Párrafos, inputs, textos largos |
| Datos / Precios | Courier New (sistema) | Cifras de precio, datos técnicos |

**Tamaño mínimo:** 16px en body para mobile (evitar zoom iOS en inputs).

---

## BOTONES Y CTAS

```css
/* CTA principal — SIEMPRE verde oscuro */
.btn-primaire {
  background: var(--verde-claro);   /* #008E3F */
  color: #fff;
  padding: 14px 28px;
  font-family: Montserrat, sans-serif;
  font-weight: 700;
  border-radius: 6px;
}
.btn-primaire:hover { background: #006b2f; }

/* CTA secundario */
.btn-secondaire {
  background: transparent;
  color: #fff;
  border: 2px solid rgba(255,255,255,.6);
}
```

**Texto CTA principal obligatorio:** `Obtenir ma soumission gratuite` (o variante directa del mismo concepto).

---

## FOTOGRAFÍAS — ESTÁNDAR VISUAL

**Criterios de selección (Francisco Visual Standard):**
- Cielo azul + nubes preferido (85%+ de fotos del portfolio)
- Sin personas visibles en el primer plano
- Sin drone / vista aérea
- Pavé clair (beige/gris clair) — no oscuro ni manchado
- Césped verde brillante — no amarillo ni seco
- Contexto Montreal: arquitectura brick typique, cours résidentielles
- Accents negros (meubles, luminaires) en proyectos premium

**PROHIBIDO usar:**
- Fotos de stock genéricas de América Latina o Europa
- Jardines tropicales (palmeras, plantas tropicales)
- Nieve o condiciones de invierno extremas (a menos que sea contenido específico)

---

## GARANTÍAS — REGLAS CONFIRMADAS

| Servicio | Garantía | Estado |
|----------|---------|--------|
| Pavé / Pavé uni | **5 ans** | ✅ CONFIRMADO por Daniel — 2026-06-24 |
| Piscine | — | ⏳ Pendiente confirmación |
| Terrasse (bois / composite) | — | ⏳ Pendiente confirmación |
| Clôture | — | ⏳ Pendiente confirmación |
| Pergola / Gazebo | — | ⏳ Pendiente confirmación |
| Gazon / Aménagement | — | ⏳ Pendiente confirmación |
| Cuisine extérieure | — | ⏳ Pendiente confirmación |
| Éclairage | — | ⏳ Pendiente confirmación |
| Irrigation | — | ⏳ Pendiente confirmación |

**Fórmula prudente para servicios sin confirmación:**
> *"Garantie selon le type de projet, les matériaux sélectionnés et les conditions du contrat."*

**NUNCA inventar una garantía específica en años para servicios no confirmados.**

---

## COURRIEL — REGLA DEFINITIVA

`info@jardin-ideal.com` es el courriel oficial para:
- Contacto visible en landing pages
- Correo de referencia en politique de confidentialité
- Réponse automática en formularios (cuando aplique)
- Coordonnées en footer

`daniel@groupe-ideal.com` es el courriel INTERNO operacional — no publicar en landing pages.

---

## TEXTOS LEGALES OBLIGATORIOS

### Financement — disclaimer

> *"Cette calculatrice est fournie à titre d'information générale uniquement. Les résultats affichés sont des estimations indicatives. Ils ne constituent pas une offre de financement ni une approbation de crédit. Estimation indicative. Sujet à l'analyse et à l'approbation du partenaire financier. Jardin Idéal agit à titre d'intermédiaire et ne prend aucune décision de crédit."*

**Texto prohibido:** "Pré-approuvé" sin evaluación real.

### Consentement Loi 25 (obligatoire dans tout formulaire)

> *"J'accepte que Jardin Idéal collecte et utilise mes renseignements personnels pour traiter ma demande, conformément à sa politique de confidentialité."*

Siempre con checkbox activo — nunca solo texto.

### Données confirmées à utiliser

- Projets réalisés: **1 500+**
- Années d'expérience: **15+ ans** (depuis 2009)
- Note Google: **4.9/5** (si verificado y actualizado)
- RBQ: **#5773-1983-01**
- Assurance: **2 M$** (responsabilité civile)

---

*Reglas de marca Jardín Ideal — v1.0 · 2026-06-24*
*Actualizar cuando Daniel confirme nuevos datos de garantía u otros parámetros*
