# REGLAS LANDING PAGES — Jardín Ideal
**Paquete:** MANUS_CONTEXT_PACK · Documento 03/04
**Versión:** 1.0 · **Última actualización:** 2026-06-24
**Uso:** Cargar en Manus antes de crear o modificar cualquier landing page

---

## ESTRUCTURA OBLIGATORIA — ORDEN DE SECCIONES

Toda landing page de Jardín Ideal debe seguir este orden:

```
1. NAV / TOPBAR
2. HERO (CTA principal + calculadora o estimado visual)
3. TRUST PILLS / SOCIAL PROOF RÁPIDO
4. FORMULARIO O PASO 1 DEL FLUJO
5. GALERÍA DE PROYECTOS (con hotspots interactivos)
6. PROCESO EN PASOS (Cómo funciona)
7. FINANCEMENT / CALCULADORA FINANCEMENT
8. CHECKLIST ENTREPRENEUR vs Jardin Idéal
9. TESTIMONIOS GOOGLE (reales — ver base de datos)
10. FAQ (mínimo 8, máximo 15 preguntas)
11. CTA FINAL
12. FOOTER
13. POLITIQUE DE CONFIDENTIALITÉ (sección inline oculta)
```

---

## FORMULARIOS — CAMPOS Y REGLAS

### Formulario principal de soumission

Campos obligatorios (en este orden):
1. Prénom (`fPrenom`) — obligatorio
2. Nom (`fNom`) — obligatorio
3. Téléphone (`fTel`) — obligatorio, format 514-266-2504
4. Courriel (`fEmail`) — obligatorio, validación email
5. Code postal (`fCodePostal`) — obligatorio, format H1A 1A1
6. Ville (`fVille`) — obligatorio
7. Type de projet (`fTypeProjet`) — select obligatorio
8. Superficie approximative (`fSuperficie`) — select, avec ranges
9. Budget approximatif (`fBudget`) — select, avec ranges
10. Description / détails (`fDescription`) — textarea, opcional
11. Adresse du projet (`fAdresse`) — opcional
12. Comment vous nous avez trouvés (`fSource`) — select, opcional
13. Upload photos (`fPhotos`) — file, opcional, accept="image/*"

**Checkbox Loi 25 — OBLIGATORIO en TODO formulario:**
```html
<input type="checkbox" id="consentement" name="consentement" required>
<label>J'accepte que Jardin Idéal collecte et utilise mes renseignements personnels 
pour traiter ma demande de soumission gratuite, conformément à sa 
<a href="#confidentialite">politique de confidentialité</a>. *</label>
```

**El botón enviar NO funciona sin que este checkbox esté activo.**

### Formulaire de financement

Campos en el modal/wizard de financement (3 étapes):
- Étape 1: Capital (slider $5K–$100K), taux (% editable), durée (select 60/120/180/240 mois)
- Étape 2: Prénom, Nom, Téléphone, Courriel, Ville, Code postal, revenu annuel estimé
- Étape 3: Résumé + checkbox consentement financement + bouton enviar

**Checkbox Loi 25 — OBLIGATORIO también en financement:**
```html
<input type="checkbox" id="consentementFin" required>
<label>J'autorise Jardin Idéal à utiliser mes renseignements pour préparer 
mon dossier de financement et me contacter. 
<a href="#confidentialite">Politique de confidentialité</a>. *</label>
```

---

## TEXTOS PROHIBIDOS — NUNCA USAR

| Texto PROHIBIDO | Razón | Texto correcto |
|-----------------|-------|---------------|
| "Pré-approuvé" | Engañoso, no existe evaluación real | "Demande reçue" |
| "Approuvé par Desjardins" | No confirmado por Desjardins | Omitir referencia directa |
| "Garantie 5 ans" para servicios no pavé | No confirmado | "Garantie selon le type de projet..." |
| "+200 projets réalisés" | Contradictorio con "1 500+" | "1 500+ projets réalisés" |
| Precios exactos inventados | Pueden crear disputas legales | Ranges o "à partir de $X" |
| "admin-xxx.html" en links visibles | Expone sistema backend | Remover o ocultar completamente |
| Copyright año anterior | Desactualizado | © 2026 Jardin Idéal |
| "ca" sin cedilla | Ortografía FR | "ça" |

---

## CALCULADORA DE ESTIMATION — FÓRMULAS

```javascript
// Precio base por tipo de proyecto
const PRIX_BASE = {
  'amenagement_complet':    35000,
  'pave_pergola':           22000,
  'pave_cloture':           16000,
  'pave_seul':              10000,
  'piscine_amenagement':    45000,
  'terrasse_seule':          8000,
  'cour_avant':              7500
};

// Multiplicadores de superficie
const MULT_SUP = {
  'moins_200':  0.75,   // < 200 pi²
  '200_500':    1.00,   // 200–500 pi²
  '500_1000':   1.45,   // 500–1000 pi²
  'plus_1000':  1.90    // > 1000 pi²
};

// Multiplicadores de finición
const MULT_FIN = {
  'economique': 0.75,
  'standard':   1.00,
  'premium':    1.35,
  'luxe':       1.75
};

// Multiplicadores de terrain
const MULT_TER = {
  'plat':           1.00,
  'legere_pente':   1.15,
  'forte_pente':    1.30,
  'acces_difficile':1.20
};

// Fórmula
const estimation = PRIX_BASE[type] * MULT_SUP[sup] * MULT_FIN[fin] * MULT_TER[ter];
// Margen: +/- 20%, redondear al $500 más cercano
const min = Math.round(estimation * 0.85 / 500) * 500;
const max = Math.round(estimation * 1.15 / 500) * 500;
```

**Siempre mostrar como rango:** `Entre $XX,XXX et $XX,XXX` (nunca precio único exacto)

---

## CALCULADORA FINANCEMENT — FÓRMULA

```javascript
// M = P × [r(1+r)^n] / [(1+r)^n - 1]
function calcMensualite(capital, tauxAn, mois) {
  if (tauxAn === 0) return capital / mois;
  const r = tauxAn / 100 / 12;
  const facteur = Math.pow(1 + r, mois);
  return capital * (r * facteur) / (facteur - 1);
}
```

**Disclaimer obligatorio bajo la calculadora:**
> "Cette calculatrice est fournie à titre d'information générale uniquement. Les résultats affichés sont des estimations indicatives. Ils ne constituent pas une offre de financement ni une approbation de crédit. Estimation indicative. Sujet à l'analyse et à l'approbation du partenaire financier. Jardin Idéal agit à titre d'intermédiaire et ne prend aucune décision de crédit."

---

## DURACIÓN DE FINANCEMENT — SELECTOR OBLIGATORIO

```html
<select id="miniMonthsSel">
  <option value="60">60 mois (5 ans)</option>
  <option value="120">120 mois (10 ans)</option>
  <option value="180">180 mois (15 ans)</option>
  <option value="240" selected>240 mois (20 ans — mensualité min)</option>
</select>
<input type="hidden" id="miniMonths" value="240">
```

**NUNCA hardcodear la duración a 240 meses únicamente.**

---

## META PIXEL — INTEGRACIÓN

```html
<!-- Meta Pixel Code -->
<script>
  !function(f,b,e,v,n,t,s)
  {if(f.fbq)return;n=f.fbq=function(){n.callMethod?
  n.callMethod.apply(n,arguments):n.queue.push(arguments)};
  if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
  n.queue=[];t=b.createElement(e);t.async=!0;
  t.src=v;s=b.getElementsByTagName(e)[0];
  s.parentNode.insertBefore(t,s)}(window, document,'script',
  'https://connect.facebook.net/en_US/fbevents.js');
  fbq('init', 'TU_PIXEL_ID');  // ⚠️ REEMPLAZAR con ID real
  fbq('track', 'PageView');
</script>
<!-- Tracking en submit -->
<!-- fbq('track', 'Lead'); — activar en función submitForm() -->
```

**⚠️ Meta Pixel ID:** PENDIENTE — recuperar de Meta Business Suite → Events Manager → Pixels

---

## ZAPIER WEBHOOK — INTEGRACIÓN

```javascript
async function submitForm() {
  // ... validar campos ...
  const payload = {
    // CRM
    prenom: document.getElementById('fPrenom').value,
    nom: document.getElementById('fNom').value,
    telephone: document.getElementById('fTel').value,
    email: document.getElementById('fEmail').value,
    code_postal: document.getElementById('fCodePostal').value,
    ville: document.getElementById('fVille').value,
    // Proyecto
    type_projet: document.getElementById('fTypeProjet').value,
    superficie: document.getElementById('fSuperficie').value,
    budget: document.getElementById('fBudget').value,
    description: document.getElementById('fDescription').value,
    adresse_projet: document.getElementById('fAdresse')?.value || '',
    source: document.getElementById('fSource')?.value || '',
    // Meta
    landing_page: 'cour-arriere-v2',
    date_soumission: new Date().toISOString()
  };

  const response = await fetch('TU_ZAPIER_WEBHOOK_URL', {  // ⚠️ REEMPLAZAR
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });
  // fbq('track', 'Lead');  // Meta Pixel Lead event
}
```

**Zapier → Pipedrive mapping:**
| Campo JS | Campo Pipedrive |
|----------|----------------|
| `prenom + nom` | Person Name |
| `telephone` | Phone |
| `email` | Email |
| `ville + code_postal` | City / ZIP |
| `type_projet` | Deal Title prefix |
| `budget` | Deal Value (range midpoint) |
| `source` | Lead Source |
| `landing_page` | Canal / UTM Source |

---

## ICS PRE-SCORE (para notas automáticas Pipedrive)

| Factor | Puntaje máx |
|--------|------------|
| Tipo de proyecto | 20 pts |
| Budget seleccionado | 20 pts |
| Superficie | 15 pts |
| Zona geográfica (CP) | 15 pts |
| Urgencia / timeline | 12 pts |
| Fuente (source) | 8 pts |
| Terreno | 5 pts |
| **Total** | **100 pts** |

**Clasificación:**
- PRE-A: ≥ 75 pts → Rappel immédiat
- PRE-B: 55–74 pts → Rappel sous 24h
- PRE-C: < 55 pts → Séquence email automatique

---

## FAQ — PREGUNTAS MÍNIMAS A INCLUIR

Todo LP debe tener al menos estas 8 preguntas:
1. Quel est le délai pour obtenir une soumission ?
2. Quelle est la superficie minimale pour un projet ?
3. Offrez-vous un financement ?
4. Intervenez-vous dans toutes les régions du Grand Montréal ?
5. Est-ce que vous offrez une garantie ? (pavé: 5 ans; autres: selon contrat)
6. Quelle est la meilleure période pour faire des travaux d'aménagement ?
7. Combien de temps à l'avance dois-je planifier mon projet ?
8. Est-ce que la soumission engage à quelque chose ?

---

## GALERÍA — PROYECTOS REALES CONFIRMADOS (cour arrière)

| Tipo | Descripción | Zona |
|------|-------------|------|
| Pavé uni | Gris clair 1 200 pi², cour arrière + latérale | Laval |
| Pavé + clôture | Beige châteauguay + aluminium noir | Brossard |
| Pavé + pergola | Standard + aluminium anthracite | Longueuil |
| Piscine + aménagement | Creusée ovale + margelles pierre naturelle | Repentigny |
| Terrasse composite | 400 pi² gris naturel + garde-corps verre | Laval |
| Éclairage décoratif | Spots encastrés + lanterneaux solaires | Montréal-Nord |
| Gazon naturel + haie | Réaménagement complet | Terrebonne |
| Pavé + cuisine ext | BBQ intégré + îlot en granite | Brossard |
| Cour avant + arrière | Pavé gris + accès carrossable | Saint-Léonard |

**Tamaño texto en hotspots:** máximo 3 líneas. Formato: `Titre · Superficie · Prix indicatif (optionnel)`

---

*Reglas Landing Pages Jardín Ideal — v1.0 · 2026-06-24*
*Actualizar cuando se confirmen: Meta Pixel ID, Zapier URL, garantías adicionales*
