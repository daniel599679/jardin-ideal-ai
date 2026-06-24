# PLAN DE OPTIMIZACIÓN — LANDING PAGE COUR ARRIÈRE
**Fecha:** 2026-06-24
**Versión:** 1.0 — Plan pre-implementación
**Basado en:** Análisis estructural + MEMORIA_GLOBAL.md + sistema ICS
**Archivo técnico:** `CHANGEMENTS_TECHNIQUES.md` (mismo directorio)

> **Nota:** Este plan está listo para ejecutarse en cuanto la página sea accesible.
> Carpeta técnica del proyecto: `05_MARKETING/LANDING_PAGES/COUR_ARRIERE/`
> (El usuario indicó `03_MARKETING` — en este sistema la carpeta de marketing es `05_MARKETING`)

---

## OBJETIVO DEL PLAN

Convertir el prototipo en una **landing page de conversión real** que:
1. Genere soumissions calificadas directamente en Pipedrive
2. Pre-califique automáticamente el lead con ICS score
3. Cumpla con Loi 25 Quebec (política de privacidad + consentimientos)
4. Sea reproducible como plantilla para los 9 servicios del catálogo

**KPI de éxito:**
- Tasa de conversión visitante → lead: ≥3.5%
- CPL en Meta Ads usando esta LP: ≤$25 CAD (actual: $23.72 — mantener)
- Tasa de leads calificados PRE-A/B: ≥60%
- Tiempo de carga: <2.5s (Core Web Vitals)

---

## FASE 1 — CORRECCIONES CRÍTICAS (antes de publicar)

### 1.1 Política de privacidad + consentimientos legales

**Por qué primero:** Loi 25 Quebec obliga a toda empresa que recopile datos personales a tener política visible y consentimiento explícito. Sin esto, no se puede publicar.

**Acciones:**
- [ ] Redactar política de privacidad en francés (ver plantilla en `CHANGEMENTS_TECHNIQUES.md`)
- [ ] Agregar checkbox de consentimiento en formulario soumission
- [ ] Agregar checkbox de consentimiento en formulario financiamiento
- [ ] Enlace a política visible desde footer y bajo cada formulario
- [ ] Banner de cookies si se usa Meta Pixel o Google Analytics

**Responsable:** Daniel + legal (validar política)
**Plazo:** Antes de cualquier publicación

---

### 1.2 Formulario soumission — campos completos

**Objetivo:** Capturar suficientes datos para el pre-score ICS automático.

**Estructura del formulario optimizado:**

```
SECTION 1 — CONTACT
  Prénom*                    [text]
  Nom*                       [text]
  Téléphone*                 [tel]   → validar formato QC
  Email*                     [email]

SECTION 2 — PROJET
  Adresse du projet*         [text]
  Ville*                     [select] → Montréal / Laval / Westmount / TMR / Brossard / Longueuil / Autre
  Type de projet*            [checkboxes multi]
                             ☐ Pavé-uni (terrasse)
                             ☐ Pergola / gazebo
                             ☐ Espace vert / pelouse
                             ☐ Clôture
                             ☐ Éclairage extérieur
                             ☐ Système d'irrigation
                             ☐ Mur de soutènement
                             ☐ Piscine
                             ☐ Projet complet (plusieurs éléments)
  
  Superficie approximative*  [select]
                             ○ Moins de 200 pi²
                             ○ 200 à 500 pi²
                             ○ 500 à 1 000 pi²
                             ○ Plus de 1 000 pi²
  
  Budget approximatif*       [select]
                             ○ Entre $8 000 et $15 000
                             ○ Entre $15 000 et $30 000
                             ○ Entre $30 000 et $50 000
                             ○ Plus de $50 000
  
  Date souhaitée de début    [date]  → min = aujourd'hui + 14 jours
  
  Le terrain est-il en pente?  [radio] ○ Oui ○ Non ○ Légèrement

SECTION 3 — SOURCE ET CONSENTEMENT
  Comment avez-vous entendu parler de nous?   [select]
                             ○ Publicité Facebook / Instagram
                             ○ Publicité Google
                             ○ Recommandation d'un ami / voisin
                             ○ Enseigne dans mon quartier
                             ○ Autre

  Message ou détails supplémentaires         [textarea, optionnel]

  ☐ J'accepte que Jardín Ideal conserve mes informations pour traiter 
    ma demande de soumission. [OBLIGATOIRE — lien vers politique de confidentialité]

[BOUTON] Obtenir ma soumission gratuite →
```

**Nota de confirmación post-envío:**
```
Merci [Prénom] ! Votre demande a bien été reçue.
Un membre de notre équipe vous contactera dans les 24 heures.
📞 Si vous avez une urgence : 514-266-2504
```

---

### 1.3 Disclaimers en calculadoras

**Obligatorio bajo calculadora de estimación:**
```
📋 Les estimations affichées sont indicatives et basées sur des projets similaires.
Le prix final sera établi lors de la visite gratuite et dépend des spécificités 
de votre terrain, des matériaux choisis et de la complexité des travaux.
```

**Obligatorio bajo calculadora de financiamiento:**
```
⚠️ Cette simulation est fournie à titre indicatif uniquement.
Elle ne constitue pas une offre de financement ni une approbation de crédit.
Les taux et conditions réels dépendent de votre dossier et du partenaire financier.
Jardín Ideal n'est pas un prêteur agréé.
```

---

## FASE 2 — OPTIMIZACIÓN DE CONVERSIÓN

### 2.1 Hero section — versión optimizada

**Estructura recomendada:**

```
[IMAGEN HERO — patio_rotin_pub.png — score 100/100]

HEADLINE (H1, 72px):
"Votre cour arrière, transformée en 7 jours."

SUBHEADLINE (H2, 22px):
"+200 réalisations à Montréal · Soumission gratuite · Réponse en 24h"

URGENCE (badge rojo o dorado):
"🗓 Juillet se remplit rapidement. Quelques places disponibles."

CTA PRINCIPAL (bouton vert foncé):
[Obtenir ma soumission gratuite →]

CTA SECUNDARIO (texto, no botón):
Ou appelez maintenant: 514-266-2504

BARRA DE CONFIANZA (iconos):
✅ Licence RBQ  |  ⭐ 4.9/5 Google  |  🏆 +200 projets  |  🔒 Garantie incluse
```

**Reglas visual (Francisco Standard):**
- Imagen: cielo azul + pavé claro + muebles negros o verde césped
- Sin personas, sin drones, sin filtros HDR
- Score mínimo: 90/100

---

### 2.2 Tabla de precios — 4 niveles

**Estructura visual:**

```
NIVEAU ESSENTIEL             NIVEAU STANDARD              NIVEAU PREMIUM              NIVEAU SIGNATURE
💰 $8,000 – $18,000         💰 $18,000 – $32,000         💰 $32,000 – $48,000        💰 $48,000 – $80,000+
─────────────────────       ─────────────────────        ─────────────────────       ─────────────────────
✅ Excavation + drainage    ✅ Tout l'Essentiel           ✅ Tout le Standard          ✅ Tout le Premium
✅ Pavé-uni de base         ✅ Clôture résidentielle      ✅ Pergola / gazebo           ✅ Piscine ou spa
✅ Bordures finition        ✅ Espace vert pelouse        ✅ Éclairage LED              ✅ Système irrigation
                            ✅ Finition premium           ✅ Plantation premium         ✅ Mur de soutènement
                                                                                      ✅ Design personnalisé

⏱ 3–5 jours               ⏱ 5–7 jours                 ⏱ 7–10 jours               ⏱ 10–21 jours

[Obtenir une soumission]   [Obtenir une soumission]     [Obtenir une soumission]    [Obtenir une soumission]
```

**Nota bajo la tabla:**
```
📋 Ces prix sont indicatifs et basés sur des projets types à Montréal.
Votre soumission détaillée sera établie gratuitement lors de la visite.
```

---

## FASE 3 — CALCULADORAS CON LÓGICA CORRECTA

### 3.1 Calculadora de estimación de precio

**Variables de entrada:**

| Variable | Opciones | Factor |
|----------|----------|--------|
| Type de projet | Pavé seul / Pavé + clôture / Pavé + pergola / Complet | Base price |
| Superficie | <200 / 200-500 / 500-1000 / +1000 pi² | Size multiplier |
| Niveau de finition | Économique / Standard / Premium / Luxe | Finish multiplier |
| Terrain | Plat / Légère pente / Forte pente / Accès difficile | Terrain multiplier |
| Éléments additionnels | Éclairage / Irrigation / Plantation / Mur / Piscine | Add-on prices |

**Tabla de precios base por tipo de proyecto:**

| Type | Prix de base | Description |
|------|-------------|-------------|
| Pavé seul | $10,000 | Terrasse pavé-uni, excavation, drainage, bordures |
| Pavé + clôture | $16,000 | Pavé + clôture résidentielle standard |
| Pavé + pergola | $22,000 | Pavé + structure pergola bois ou aluminium |
| Cour complète | $35,000 | Pavé + pergola + espace vert + éléments décoratifs |

**Multiplicador por superficie:**

| Superficie | Multiplicateur |
|-----------|---------------|
| < 200 pi² | × 0.75 |
| 200 – 500 pi² | × 1.00 (référence) |
| 500 – 1 000 pi² | × 1.45 |
| > 1 000 pi² | × 1.90 |

**Multiplicador por nivel de acabado:**

| Niveau | Multiplicateur | Matériaux |
|--------|---------------|-----------|
| Économique | × 0.75 | Béton standard, clôture PVC de base |
| Standard | × 1.00 | Techo-Bloc / Permacon standard |
| Premium | × 1.35 | Techo-Bloc Graphix, pierre naturelle |
| Luxe | × 1.75 | Pierre importée, bois exotique, design personnalisé |

**Multiplicador por dificultad del terreno:**

| Terrain | Multiplicateur | Raison |
|---------|---------------|--------|
| Plat | × 1.00 | Travaux standards |
| Légère pente (<10%) | × 1.15 | Nivellement supplémentaire |
| Forte pente (>10%) | × 1.30 | Mur de soutènement ou terrassement majeur |
| Accès difficile | × 1.20 | Transport et installation à la main |

**Precios adicionales (suma lineal):**

| Élément | Min | Max | Moyen |
|---------|-----|-----|-------|
| Clôture | $3,500 | $12,000 | $6,500 |
| Éclairage LED | $2,500 | $6,000 | $4,000 |
| Système irrigation | $3,000 | $7,000 | $4,500 |
| Plantation / aménagement | $2,000 | $10,000 | $5,000 |
| Mur de soutènement | $5,000 | $15,000 | $9,000 |
| Piscine creusée | $30,000 | $80,000 | $50,000 |
| Pergola premium | $8,000 | $20,000 | $12,500 |

**FÓRMULA COMPLETA:**

```javascript
// Calcul de l'estimation
function calculerEstimation(typeProjet, superficie, finition, terrain, additionnels) {
  const PRIX_BASE = {
    'pave_seul': 10000,
    'pave_cloture': 16000,
    'pave_pergola': 22000,
    'complet': 35000
  };

  const MULT_SUPERFICIE = {
    'moins_200': 0.75,
    '200_500': 1.00,
    '500_1000': 1.45,
    'plus_1000': 1.90
  };

  const MULT_FINITION = {
    'economique': 0.75,
    'standard': 1.00,
    'premium': 1.35,
    'luxe': 1.75
  };

  const MULT_TERRAIN = {
    'plat': 1.00,
    'legere_pente': 1.15,
    'forte_pente': 1.30,
    'acces_difficile': 1.20
  };

  const PRIX_ADDITIONNELS = {
    'cloture': 6500,
    'eclairage': 4000,
    'irrigation': 4500,
    'plantation': 5000,
    'mur': 9000,
    'piscine': 50000,
    'pergola_premium': 12500
  };

  // Calcul central
  let base = PRIX_BASE[typeProjet];
  let estimation = base * MULT_SUPERFICIE[superficie] * MULT_FINITION[finition] * MULT_TERRAIN[terrain];
  
  // Ajouter les éléments additionnels sélectionnés
  additionnels.forEach(el => {
    estimation += PRIX_ADDITIONNELS[el];
  });

  // Générer la fourchette (±20%)
  const min = Math.round(estimation * 0.80 / 500) * 500;  // Arrondir à 500 près
  const max = Math.round(estimation * 1.20 / 500) * 500;
  const moyen = Math.round(estimation / 500) * 500;

  return { min, moyen, max };
}

// Affichage
// "Votre estimation: entre $XX,XXX et $XX,XXX (base: ~$XX,XXX)"
// + disclaimer obligatoire
```

**Display en la página:**
```
Votre estimation pour ce projet:
╔══════════════════════════════════════╗
║  Minimum estimé:    $ XX,000 CAD    ║
║  Estimation base:   $ XX,000 CAD ◄  ║
║  Maximum estimé:    $ XX,000 CAD    ║
╚══════════════════════════════════════╝

📋 Cette estimation est indicative. La soumission exacte sera établie lors de la visite gratuite.

[Obtenir ma soumission gratuite →]
```

---

### 3.2 Calculadora de financiamiento

**Variables de entrada:**

| Variable | Tipo | Default | Rango |
|----------|------|---------|-------|
| Montant du projet | Number (slider + input) | $25,000 | $8,000 – $80,000 |
| Mise de fonds | Number / % slider | 20% | 10% – 50% |
| Taux d'intérêt estimé | Select | 9.9% | 7.9% / 9.9% / 11.9% / 13.9% |
| Durée du prêt | Select (mois) | 60 | 12 / 24 / 36 / 48 / 60 |

**FÓRMULA COMPLETA:**

```javascript
function calculerFinancement(montantTotal, miseDeFonds, tauxAnnuel, dureeEnMois) {
  // Calculs de base
  const mise = (typeof miseDeFonds === 'string' && miseDeFonds.endsWith('%'))
    ? montantTotal * (parseFloat(miseDeFonds) / 100)
    : parseFloat(miseDeFonds);

  const soldeAFinancer = montantTotal - mise;
  
  // Taux mensuel
  const tauxMensuel = tauxAnnuel / 100 / 12;
  
  // Formule d'amortissement standard (mensualité constante)
  // M = P × [r(1+r)^n] / [(1+r)^n - 1]
  let mensualite;
  if (tauxMensuel === 0) {
    mensualite = soldeAFinancer / dureeEnMois;
  } else {
    const facteur = Math.pow(1 + tauxMensuel, dureeEnMois);
    mensualite = soldeAFinancer * (tauxMensuel * facteur) / (facteur - 1);
  }
  
  const coutTotal = mensualite * dureeEnMois;
  const coutInterets = coutTotal - soldeAFinancer;

  return {
    montantTotal: montantTotal,
    miseDeFonds: Math.round(mise),
    soldeAFinancer: Math.round(soldeAFinancer),
    tauxAnnuel: tauxAnnuel,
    dureeEnMois: dureeEnMois,
    mensualite: Math.round(mensualite),
    coutTotal: Math.round(coutTotal),
    coutInterets: Math.round(coutInterets)
  };
}
```

**Display en la página:**
```
Simulation de financement:
┌─────────────────────────────────────────────┐
│  Montant du projet:      $ 25,000 CAD       │
│  Mise de fonds (20%):    $  5,000 CAD       │
│  Solde à financer:       $ 20,000 CAD       │
│  Taux estimé:            9.9 % / an         │
│  Durée:                  60 mois            │
├─────────────────────────────────────────────┤
│  MENSUALITÉ ESTIMÉE:     $   424 / mois  ◄  │
│  Coût total du crédit:   $ 25,440 CAD       │
│  Coût des intérêts:      $  5,440 CAD       │
└─────────────────────────────────────────────┘

⚠️ Simulation indicative uniquement — pas une approbation de crédit.
[Demander un financement →]   [Parler à un conseiller: 514-266-2504]
```

---

## FASE 4 — INTEGRACIÓN PIPEDRIVE + ZAPIER

### 4.1 Estructura del deal en Pipedrive al recibir soumission

**Campos del deal (mapeado desde el formulario):**

| Campo Pipedrive | Campo formulario | Notas |
|----------------|-----------------|-------|
| Titre du deal | "LP-CA · {Prénom} {Nom}" | LP = Landing Page, CA = Cour Arrière |
| Contact name | Prénom + Nom | |
| Email | Email | |
| Téléphone | Téléphone | |
| Organisation | — | Vide si particulier |
| Pipeline | Leads qualifiés | |
| Étape | Nouveau lead | |
| Valeur estimée | Basée sur budget select | $8K/15K/30K/50K+ → valeur médiane |
| Propriétaire | Daniel Figueroa | Pour leads PRE-A |
| Source (custom) | Comment nous avez-vous trouvés | |
| Adresse projet (custom) | Adresse + Ville | |
| Type projet (custom) | Type de projet (checkboxes) | Liste séparée par virgules |
| Superficie (custom) | Superficie approximative | |
| Budget client (custom) | Budget approximatif | |
| Date souhaitée (custom) | Date souhaitée de début | |
| Terrain en pente (custom) | Oui/Non/Légèrement | |
| ICS pre-score (custom) | Calculé auto | Voir formule ci-dessous |
| Source page (custom) | lp-cour-arriere | Fijo para esta página |

**Nota automática en Pipedrive (generada por Zapier):**

```
[NOUVEAU LEAD — Landing Page Cour Arrière]
Date: {{timestamp}}
Source: lp-cour-arriere · {{source_publicité}}
ICS Pré-score: {{ics_score}}/100 → {{classification}}

PROJET
Type: {{type_projet}}
Superficie: {{superficie}}
Budget déclaré: {{budget}}
Date souhaitée: {{date_souhaitee}}
Terrain en pente: {{terrain_pente}}
Adresse: {{adresse}}, {{ville}}

CONTACT
Téléphone: {{telephone}}
Email: {{email}}

MESSAGE: {{message}}

[Action recommandée: Appel dans {{delai_recommande}}]
```

### 4.2 Fórmula de pre-score ICS automático

El pre-score se calcula automáticamente en Zapier antes de crear el deal:

```javascript
function calcularPreScoreICS(formData) {
  let score = 0;

  // TIPO DE PROYECTO (max 20 pts)
  const tiposScore = {
    'piscine': 20,
    'complet': 18,
    'pave_pergola': 16,
    'pave_cloture': 12,
    'pave_seul': 10
  };
  // Toma el score del tipo de mayor valor seleccionado
  score += Math.max(...formData.typeProjet.map(t => tiposScore[t] || 8));

  // BUDGET DECLARADO (max 20 pts)
  const budgetScore = {
    'plus_50k': 20,
    '30_50k': 16,
    '15_30k': 12,
    '8_15k': 6
  };
  score += budgetScore[formData.budget] || 0;

  // SUPERFICIE (max 15 pts)
  const superficieScore = {
    'plus_1000': 15,
    '500_1000': 12,
    '200_500': 8,
    'moins_200': 4
  };
  score += superficieScore[formData.superficie] || 0;

  // ZONA GEOGRÁFICA (max 15 pts)
  const villeScore = {
    'Westmount': 15, 'TMR': 15,
    'Montréal': 13, 'Laval': 12,
    'Brossard': 11, 'Longueuil': 10,
    'Autre': 7
  };
  score += villeScore[formData.ville] || 7;

  // FECHA DESEADA — URGENCIA (max 12 pts)
  const hoy = new Date();
  const fechaDeseada = new Date(formData.dateSouhaitee);
  const diasHastaProyecto = Math.ceil((fechaDeseada - hoy) / (1000 * 60 * 60 * 24));
  if (diasHastaProyecto <= 30) score += 12;
  else if (diasHastaProyecto <= 60) score += 8;
  else if (diasHastaProyecto <= 90) score += 5;
  else score += 2;

  // FUENTE (max 8 pts)
  const fuenteScore = {
    'recommandation': 8,
    'enseigne': 7,
    'google': 6,
    'facebook_instagram': 5,
    'autre': 3
  };
  score += fuenteScore[formData.source] || 3;

  // TERRAIN (max 5 pts — penalización si es difícil)
  if (formData.terrainPente === 'non') score += 5;
  else if (formData.terrainPente === 'legere') score += 3;
  else score += 1;

  // Clasificación
  let classification;
  let delaiAppel;
  if (score >= 75) { classification = 'PRE-A'; delaiAppel = '< 2 heures'; }
  else if (score >= 55) { classification = 'PRE-B'; delaiAppel = '< 4 heures'; }
  else { classification = 'PRE-C'; delaiAppel = 'Séquence email'; }

  return { score: Math.min(score, 100), classification, delaiAppel };
}
```

---

## FASE 5 — RÉALISATIONS Y PRUEBA SOCIAL

### 5.1 Estructura de cada réalisation

**Template de tarjeta de proyecto:**
```
[FOTO AVANT]  →  [FOTO APRÈS]

📍 Plateau-Mont-Royal · Montréal
🏗 Cour arrière complète · Pavé + Pergola + Éclairage
💰 Investissement: $34,500 CAD
⏱ Réalisé en: 8 jours ouvrables
⭐ "Nous avons adoré travailler avec l'équipe. Résultat parfait." — M.T.
```

### 5.2 Template de testimonio

```
"[Cita directa del cliente — específica, con detalle del proyecto o equipo]"

[Foto del cliente o foto del proyecto]
— [Prénom + Initiale du nom] · [Quartier/Ville] · [Type de projet] · [Montant approximatif]
⭐⭐⭐⭐⭐ · [Mois AAAA]
```

---

## RESUMEN DE IMPLEMENTACIÓN

| Fase | Tarea | Prioridad | Tiempo estimado |
|------|-------|-----------|----------------|
| 1 | Política privacidad + consentimientos | 🔴 Crítico | 2h |
| 1 | Formulario soumission completo | 🔴 Crítico | 3h |
| 1 | Disclaimers en calculadoras | 🔴 Crítico | 30min |
| 2 | Hero optimizado | 🟡 Alto | 2h |
| 2 | Tabla 4 niveles con fotos | 🟡 Alto | 3h |
| 3 | Calculadora estimación (nueva lógica) | 🟡 Alto | 4h |
| 3 | Calculadora financiamiento | 🟡 Alto | 3h |
| 4 | Integración Zapier → Pipedrive | 🟡 Alto | 4h |
| 4 | ICS pre-score automático | 🟡 Alto | 2h |
| 5 | Galería avant/après con datos | 🔵 Mejora | 4h |
| 5 | FAQ completa 10 preguntas | 🔵 Mejora | 1h |

**Tiempo total estimado de implementación:** ~28 horas de desarrollo

---

*Plan de optimización — Jardín Ideal AI System · 2026-06-24*
*Siguiente paso: Lista técnica completa → `CHANGEMENTS_TECHNIQUES.md`*
