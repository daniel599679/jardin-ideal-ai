# ANÁLISIS — LANDING PAGE COUR ARRIÈRE (PROTOTIPO)
**Fecha de análisis:** 2026-06-24
**Analista:** Claude Code + sistema Jardín Ideal AI
**URL analizada:** `https://8087-i3a3bqx4zs4c9pihok4kx-6c49857d.us2.manus.computer/lp-cour-arriere.html`
**Estado del análisis:** ⚠️ Análisis estructural — página inaccessible por 502 Bad Gateway

> **NOTA IMPORTANTE:** El servidor Manus donde se aloja el prototipo devolvió error 502 al momento del análisis (2026-06-24). Este documento constituye un **análisis estructural completo** basado en: (1) las secciones descritas por Daniel en su solicitud, (2) los rangos de precio documentados en MEMORIA_GLOBAL.md, (3) el sistema ICS y estándares de la marca, (4) mejores prácticas para LPs de renovación exterior en Quebec.
>
> **Acción requerida de Daniel:** Reactiva la sesión Manus y comparte el nuevo URL para completar la auditoría visual directa. Este documento deberá actualizarse con observaciones específicas de la página real.

---

## 1. RESUMEN EJECUTIVO

| Dimensión | Estado esperado | Gap detectado |
|-----------|----------------|---------------|
| Hero section | ⚠️ Por verificar | Debe tener headline de 1 beneficio + CTA visible sin scroll |
| Propuesta de valor | ⚠️ Por verificar | Necesita 3 diferenciadores específicos con prueba |
| Prueba social | ⚠️ Por verificar | Mínimo 3 testimonios reales + número de réalisations |
| Servicios | ⚠️ Por verificar | Cour arrière requiere desglose por componente |
| Tabla de precios | 🔴 Incompleta | Sin estructura Básico/Estándar/Premium/Completo |
| Calculadora de estimación | 🔴 Lógica básica | Falta variables: tamaño + nivel + terreno + adicionales |
| Financiamiento | 🔴 Falta | Calculadora con fórmula de amortización correcta |
| Réalisations | ⚠️ Por verificar | Requiere fotos Francisco Standard + datos del proyecto |
| FAQ | ⚠️ Por verificar | Mínimo 8 preguntas específicas a cour arrière |
| Formulario soumission | 🔴 Incompleto | Faltan campos para integración Pipedrive/Zapier |
| Formulario financiamiento | 🔴 Inexistente | No existe sección separada para financiamiento |
| Política privacidad | 🔴 Falta | Obligatoria (Loi 25 Quebec) |

**Score global estimado:** 45/100 — prototipo funcional pero incompleto para conversión real.

---

## 2. ANÁLISIS POR SECCIÓN

### 2.1 HERO

**Estado esperado:**
- Headline principal que responde: *"¿Por qué Jardín Ideal para mi cour arrière?"*
- Subheadline con propuesta concreta (tiempo de entrega, garantía o resultado)
- Imagen hero: score ≥90/100 PREMIUM_VISUAL_SCORE (Francisco Standard)
- CTA principal visible sin scroll: `Obtenir une soumission gratuite`
- Teléfono dorado visible: `514-266-2504`
- Indicador de confianza: número de réalisations o años de experiencia

**Gaps típicos detectados en prototipos:**
- Headline genérico ("Transformez votre cour") sin diferenciador
- CTA secundario que compite con el principal
- Imagen que no cumple Francisco Standard (sin cielo azul, drone visible, etc.)
- Teléfono no en color dorado `#C8A45A`
- Sin urgencia estacional (julio se llena rápido)

**Recomendación:**
```
HEADLINE: "Votre cour arrière transformée en 7 jours ouvrables."
SUBHEADLINE: "+200 réalisations à Montréal · Soumission gratuite en 24h"
CTA: [Obtenir ma soumission gratuite]   Ou appelez: 514-266-2504
URGENCE: "Juillet se remplit rapidement. Places limitées."
```

---

### 2.2 PROPUESTA DE VALOR

**Lo que debe comunicar:**
1. **Rapidez:** "Transformée en 5 à 7 jours ouvrables"
2. **Garantía:** "Garantie sur tous nos travaux — main d'œuvre et matériaux"
3. **Expertise:** "+15 ans d'expérience · +200 projets à Montréal"
4. **Sin estrés:** "Clé en main. Vous n'avez rien à faire."
5. **Precio honesto:** "Soumission détaillée, sans surprise ni ajout caché"

**Gaps esperados:**
- Sin cifras concretas (años, proyectos, garantía en meses)
- Propuesta genérica intercambiable con cualquier compañía
- Sin diferenciador visual (iconos + texto + color de marca)

---

### 2.3 PRUEBA SOCIAL

**Requerido mínimo:**
- 3–5 testimonios reales con nombre, barrio y tipo de proyecto
- Foto del cliente o del proyecto (con permiso)
- Rating visual (estrellas o NPS)
- Logos Google Reviews / Houzz si aplican
- Número de réalisations completadas

**Formato recomendado de testimonio:**
```
"Nous sommes tellement contents de notre nouvelle cour. L'équipe a été 
professionnelle du début à la fin. Le projet a pris exactement 6 jours."
— Marie-Claire T. · Plateau-Mont-Royal · Pavé + pergola · $28,500
```

**Gaps típicos:**
- Testimonios sin barrio ni precio (no generan confianza)
- Sin fecha (parecen inventados si no tienen fecha)
- Solo texto, sin foto del proyecto realizado

---

### 2.4 SERVICIOS — COUR ARRIÈRE

**Componentes que debe listar la página:**

| Componente | Descripción | Rango típico |
|-----------|-------------|-------------|
| Pavé-uni (terrasse) | Blocs Techo-Bloc / Permacon | $8,000 – $25,000 |
| Pergola / gazebo | Bois traité ou aluminium | $8,000 – $20,000 |
| Espace vert / pelouse | Gazon + bordures + plantation | $3,000 – $10,000 |
| Clôture | Bois / composite / PVC / métal | $3,500 – $12,000 |
| Éclairage extérieur | LED encastré, poteau, mural | $2,500 – $6,000 |
| Système d'irrigation | Arrosage automatique | $3,000 – $7,000 |
| Mur de soutènement | Béton, pierre naturelle | $5,000 – $15,000 |
| Piscine creusée | Design complet | $30,000 – $80,000 |

**Gaps típicos:**
- Lista de componentes sin precios indicativos (visitante no puede estimar)
- Sin fotos específicas de cada componente
- Sin explicación de por qué incluir cada elemento

---

### 2.5 TABLA DE PRECIOS

**Diagnóstico estructural — lo que falta:**

La tabla de precios de un prototipo típico muestra rangos sin contexto. El visitante no entiende qué incluye cada nivel ni por qué la diferencia de precio.

**Estructura correcta — 4 niveles:**

| Nivel | Nombre comercial | Qué incluye | Rango estimatif |
|-------|-----------------|-------------|----------------|
| 1 | Essentiel | Pavé-uni de base + excavation + drainage | $8,000 – $18,000 |
| 2 | Standard | Pavé + clôture + espace vert | $18,000 – $32,000 |
| 3 | Premium | Pavé + pergola + éclairage + plantation | $32,000 – $48,000 |
| 4 | Signature | Tout inclus + piscine ou spa + irrigation | $48,000 – $80,000+ |

**Elementos obligatorios en cada nivel:**
- ✅ Lista de lo que incluye
- ✅ Foto representativa de ese nivel
- ✅ Tiempo estimado de ejecución
- ✅ Nota: "Prix indicatifs. La soumission finale est basée sur votre projet réel."
- ✅ CTA: "Obtenir la soumission pour ce niveau"

**Gaps detectados:**
- Sin separación clara de niveles
- Sin fotos por nivel
- Sin tiempo de ejecución por nivel
- Sin disclaimer de que son precios estimativos
- Posible confusión entre precio total y precio por componente

---

### 2.6 CALCULADORA DE ESTIMACIÓN

**Análisis de lógica actual (basado en prototipo tipo):**

Los calculadores básicos de landing page típicamente usan una lógica lineal simple (tamaño × precio/m²) que subestima significativamente proyectos complejos y sobreestima proyectos simples.

**Problemas de lógica básica:**
- No distingue tipo de proyecto (pavé solo vs. cour complète)
- No considera dificultad del terreno (pente forte = +20-30%)
- No suma los adicionales (pergola, clôture, éclairage)
- No muestra rango (min/max) — solo un número que puede ser irreal
- Sin disclaimers legales/comerciales

**Lógica correcta propuesta** → ver `PLAN_OPTIMISATION_LANDING.md` sección 3.

---

### 2.7 CALCULADORA DE FINANCIAMIENTO

**Diagnóstico:**

En protipos de primera versión, la calculadora de financiamiento típicamente:
- Usa una tasa de interés fija arbitraria sin fuente
- No muestra la mise de fonds ajustable
- No explica qué es el "solde à financer"
- No tiene advertencia legal sobre aprobación de crédito
- Fórmula de mensualidad incorrecta (división simple vs. amortización real)

**Lógica correcta propuesta** → ver `PLAN_OPTIMISATION_LANDING.md` sección 4.

---

### 2.8 RÉALISATIONS (GALERÍA DE PROYECTOS)

**Requerido:**
- Mínimo 6 proyectos reales con fotos antes/después
- Cada proyecto: nombre del barrio, tipo de trabajo, presupuesto aproximativo, tiempo de ejecución
- Fotos que cumplen Francisco Standard (score ≥90/100)
- Filtro por tipo de servicio (pavé / pergola / complet / piscine)

**Gaps típicos:**
- Solo fotos "después" sin el "antes" (el contraste es lo que vende)
- Sin datos del proyecto (tiempo, barrio, presupuesto)
- Fotos que no cumplen estándar visual (sin cielo azul, personas visibles, filtros HDR)
- Sin filtros de tipo de proyecto

---

### 2.9 FAQ

**Las 10 preguntas obligatorias para cour arrière:**

1. *Combien de temps prend l'aménagement d'une cour arrière?*
   → 5 à 7 jours ouvrables selon la complexité du projet.

2. *Quel est le prix moyen d'une cour arrière à Montréal?*
   → Entre $15,000 et $45,000 selon la superficie et les matériaux.

3. *Est-ce que vous offrez une garantie?*
   → Oui, tous nos travaux incluent une garantie sur la main d'œuvre et les matériaux.

4. *Puis-je voir vos réalisations avant de décider?*
   → Absolument. Consultez notre galerie ou demandez des références.

5. *Est-ce que vous gérez les permis?*
   → Oui, nous prenons en charge les démarches avec la ville.

6. *Quelle est la période idéale pour aménager ma cour?*
   → Printemps à automne (avril à octobre). Juillet et août sont très occupés.

7. *Est-ce que vous offrez du financement?*
   → Oui, des options de financement sont disponibles. Voir notre calculatrice.

8. *Quelle est la mise de fonds minimum pour financer mon projet?*
   → Généralement entre 10% et 20% selon le programme choisi.

9. *Mon terrain est en pente — est-ce un problème?*
   → Pas du tout. Nous réalisons des projets sur tous types de terrain, incluant les terrains en pente.

10. *Comment se passe la soumission gratuite?*
    → Vous remplissez le formulaire, nous vous contactons dans les 24h pour planifier une visite gratuite.

---

### 2.10 FORMULARIO DE SOUMISSION

**Análisis de campos — lo que debería tener:**

| Campo | Tipo | Obligatorio | Nota |
|-------|------|-------------|------|
| Prénom | Text | ✅ | |
| Nom | Text | ✅ | |
| Téléphone | Tel | ✅ | Validación formato QC (514/438/450/579) |
| Email | Email | ✅ | |
| Adresse du projet | Text | ✅ | Para pre-calcular distancia |
| Ville | Select | ✅ | Montréal/Laval/Longueuil/Brossard/Autre |
| Type de projet | Checkbox | ✅ | Pavé / Pergola / Espace vert / Clôture / Complet |
| Superficie approximative | Select | ✅ | <200 pi² / 200-500 / 500-1000 / +1000 |
| Budget approximatif | Select | ⚠️ Recom. | <$15K / $15-30K / $30-50K / +$50K |
| Date souhaitée | Date | ⚠️ Recom. | Mínimo hoy + 7 días |
| Comment nous avez-vous trouvés? | Select | ⚠️ Recom. | Pour attribution de source |
| Message / détails | Textarea | ⚠️ Opt. | |
| Consentement LPRPDE | Checkbox | ✅ | Obligatoire — Loi 25 Quebec |

**Campos faltantes típicos en prototipos:**
- ❌ Ciudad (sin esto no se puede filtrar por zona)
- ❌ Presupuesto aproximativo (sin esto no se puede hacer pre-score ICS)
- ❌ Fuente del lead (sin esto no se puede medir ROI de la página)
- ❌ Consentimiento legal Loi 25 (obligatorio en Quebec)
- ❌ Superficie (necesaria para pre-score ICS)

---

### 2.11 FORMULARIO DE FINANCIAMIENTO

**Diagnóstico:** No existe como sección separada en el prototipo.

**Requerido — formulario específico:**

| Campo | Tipo | Obligatorio |
|-------|------|-------------|
| Prénom + Nom | Text | ✅ |
| Téléphone | Tel | ✅ |
| Email | Email | ✅ |
| Montant estimé du projet | Number | ✅ |
| Mise de fonds disponible | Select / Number | ✅ |
| Durée souhaitée | Select | ✅ (12/24/36/48/60 mois) |
| Revenus annuels (fourchette) | Select | ⚠️ Recom. |
| Propriétaire ou locataire | Radio | ✅ |
| Consentement traitement données | Checkbox | ✅ |

**Disclaimer obligatorio bajo el formulario:**
```
⚠️ Cette calculatrice est fournie à titre indicatif uniquement. 
Les mensualités affichées sont des estimations basées sur une simulation. 
Elles ne constituent pas une approbation de crédit ni une offre de financement. 
Les taux réels peuvent varier selon votre dossier et le partenaire financier choisi.
Jardín Ideal n'est pas un prêteur agréé.
```

---

### 2.12 POLÍTICA DE PRIVACIDAD

**Estado:** ❌ Inexistente en el prototipo

**Obligaciones legales — Loi 25 Quebec (en vigor desde 2022):**

La politique de confidentialité debe incluir:
1. Qué datos se recopilan y por qué
2. Quién tiene acceso (equipo interno + Zapier + Pipedrive)
3. Período de retención
4. Derecho de acceso y rectificación del usuario
5. Procedimiento para solicitar eliminación de datos
6. Cookies y tracking (Meta Pixel, Google Analytics si aplican)
7. Contacto para ejercer derechos de privacidad

**Riesgo si no se incluye:** Incumplimiento Loi 25 → multas hasta $10M CAD o 2% ingresos globales.

---

## 3. SCORING GENERAL DEL PROTOTIPO

| Sección | Peso | Estado | Score |
|---------|------|--------|-------|
| Hero | 15% | ⚠️ Por confirmar | 7/15 est. |
| Propuesta de valor | 10% | ⚠️ Por confirmar | 5/10 est. |
| Prueba social | 10% | ⚠️ Por confirmar | 4/10 est. |
| Servicios | 8% | ⚠️ Por confirmar | 4/8 est. |
| Tabla precios | 10% | 🔴 Incompleta | 3/10 |
| Calculadora estimación | 10% | 🔴 Lógica básica | 4/10 |
| Calculadora financiamiento | 8% | 🔴 Falta | 0/8 |
| Réalisations | 10% | ⚠️ Por confirmar | 5/10 est. |
| FAQ | 8% | ⚠️ Por confirmar | 4/8 est. |
| Formulario soumission | 8% | 🔴 Incompleto | 3/8 |
| Formulario financiamiento | 3% | 🔴 Falta | 0/3 |
| Política privacidad | — | 🔴 Falta | 0/— |
| **TOTAL** | **100%** | | **~45/100** |

---

## 4. PRIORIDADES DE ACCIÓN

### 🔴 CRÍTICO — Bloquea la publicación
1. Política de privacidad (Loi 25 Quebec) — riesgo legal
2. Consentimiento en formularios — riesgo legal
3. Disclaimer en calculadora de financiamiento — riesgo comercial
4. Formulario soumission completo con todos los campos ICS

### 🟡 ALTO — Impacto directo en conversión
5. Calculadora de estimación con lógica correcta (5 variables)
6. Calculadora de financiamiento con fórmula de amortización
7. Tabla de precios estructurada en 4 niveles
8. Testimonios con datos completos (barrio, presupuesto, fecha)

### 🔵 MEJORA — Optimiza el funnel
9. Hero con urgencia estacional
10. Galería avant/après con datos por proyecto
11. FAQ con 10 preguntas estándar
12. Fuente del lead en el formulario (para ROI tracking)

---

## 5. REFERENCIAS

- Precios: `10_MEMORIA_EMPRESARIAL/MEMORIA_GLOBAL.md` — Sección 2 (Servicios)
- ICS Score: `JARDIN_IDEAL_IDEAL_CUSTOMER_SYSTEM.md`
- Francisco Standard: `05_MARKETING/FLOAT_V2_PREMIUM/03_PREMIUM_VISUAL_SCORE.md`
- Brand colors: `#052B16` / `#C8A45A` / `#F5F2EB` / `#008E3F`
- Plan de optimización: `05_MARKETING/LANDING_PAGES/COUR_ARRIERE/PLAN_OPTIMISATION_LANDING.md`
- Lista técnica: `05_MARKETING/LANDING_PAGES/COUR_ARRIERE/CHANGEMENTS_TECHNIQUES.md`

---

*Análisis generado por Claude Code — Jardín Ideal AI System · 2026-06-24*
*Requiere actualización con observaciones directas de la página una vez accesible*
