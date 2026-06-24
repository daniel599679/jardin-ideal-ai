# LISTA TÉCNICA DE CAMBIOS — LP COUR ARRIÈRE
**Fecha:** 2026-06-24
**Tipo:** Checklist de implementación técnica
**Referencia:** `PLAN_OPTIMISATION_LANDING.md` (mismo directorio)
**Para:** Desarrollador / Claude Code al momento de implementar

---

## ÍNDICE

1. [Estructura HTML por sección](#1-estructura-html)
2. [Formulario soumission — campos y validaciones](#2-formulario-soumission)
3. [Calculadora de estimación — código completo](#3-calculadora-estimacion)
4. [Calculadora de financiamiento — código completo](#4-calculadora-financiamiento)
5. [Formulario de financiamiento — campos](#5-formulario-financiamiento)
6. [Política de privacidad — plantilla](#6-politica-privacidad)
7. [Integración Zapier — mapping de campos](#7-integracion-zapier)
8. [Checklist de publicación](#8-checklist-publicacion)

---

## 1. ESTRUCTURA HTML

### Orden de secciones en la página (de arriba a abajo)

```
#hero               — Headline + CTA principal + foto hero
#barre-confiance    — Iconos de confianza (RBQ, avis, projets, garantie)
#proposition-valeur — 3–5 diferenciadores con iconos
#services           — Lista de componentes cour arrière con precios indicativos
#realisations       — Galería avant/après (6 proyectos mínimo)
#table-prix         — Los 4 niveles (Essentiel / Standard / Premium / Signature)
#temoignages        — 3–5 testimonios reales
#calculatrice-prix  — Calculadora de estimación (5 variables)
#financement        — Calculadora de financiamiento + formulario
#faq                — 10 preguntas colapsables (accordion)
#formulaire         — Formulario soumission completo
#footer             — Liens politique confidentialité + coordonnées
```

### Atributos de accesibilidad obligatorios

```html
<!-- Cada sección necesita: -->
<section id="[id]" aria-labelledby="[id]-title">
  <h2 id="[id]-title">...</h2>
</section>

<!-- Formularios -->
<label for="[field-id]">...</label>
<input id="[field-id]" name="[field-name]" required aria-required="true">

<!-- CTAs -->
<button type="submit" aria-describedby="form-disclaimer">...</button>
```

---

## 2. FORMULARIO SOUMISSION

### HTML completo del formulario

```html
<form id="form-soumission" action="/api/soumission" method="POST" novalidate>
  
  <!-- Section 1: Contact -->
  <fieldset>
    <legend>Vos coordonnées</legend>
    
    <div class="form-row">
      <div class="form-group">
        <label for="prenom">Prénom *</label>
        <input type="text" id="prenom" name="prenom" 
               placeholder="Marie" required autocomplete="given-name"
               data-pipedrive="first_name">
      </div>
      <div class="form-group">
        <label for="nom">Nom *</label>
        <input type="text" id="nom" name="nom" 
               placeholder="Tremblay" required autocomplete="family-name"
               data-pipedrive="last_name">
      </div>
    </div>
    
    <div class="form-row">
      <div class="form-group">
        <label for="telephone">Téléphone *</label>
        <input type="tel" id="telephone" name="telephone"
               placeholder="514-555-1234" required autocomplete="tel"
               pattern="[0-9]{3}[-\s]?[0-9]{3}[-\s]?[0-9]{4}"
               data-pipedrive="phone">
      </div>
      <div class="form-group">
        <label for="email">Courriel *</label>
        <input type="email" id="email" name="email"
               placeholder="marie@exemple.com" required autocomplete="email"
               data-pipedrive="email">
      </div>
    </div>
  </fieldset>

  <!-- Section 2: Projet -->
  <fieldset>
    <legend>Votre projet</legend>
    
    <div class="form-group">
      <label for="adresse">Adresse du projet *</label>
      <input type="text" id="adresse" name="adresse"
             placeholder="123 rue Saint-Denis" required
             data-pipedrive="custom_adresse_projet">
    </div>
    
    <div class="form-group">
      <label for="ville">Ville *</label>
      <select id="ville" name="ville" required data-pipedrive="custom_ville">
        <option value="">Sélectionnez votre ville</option>
        <option value="Montreal">Montréal</option>
        <option value="Laval">Laval</option>
        <option value="Westmount">Westmount</option>
        <option value="TMR">Town of Mount-Royal</option>
        <option value="Brossard">Brossard</option>
        <option value="Longueuil">Longueuil</option>
        <option value="Autre">Autre</option>
      </select>
    </div>
    
    <div class="form-group">
      <label>Type de projet * (cochez tout ce qui s'applique)</label>
      <div class="checkbox-grid">
        <label class="checkbox-item">
          <input type="checkbox" name="type_projet[]" value="pave_uni"
                 data-pipedrive="custom_type_projet">
          Pavé-uni (terrasse)
        </label>
        <label class="checkbox-item">
          <input type="checkbox" name="type_projet[]" value="pergola">
          Pergola / gazebo
        </label>
        <label class="checkbox-item">
          <input type="checkbox" name="type_projet[]" value="espace_vert">
          Espace vert / pelouse
        </label>
        <label class="checkbox-item">
          <input type="checkbox" name="type_projet[]" value="cloture">
          Clôture
        </label>
        <label class="checkbox-item">
          <input type="checkbox" name="type_projet[]" value="eclairage">
          Éclairage extérieur
        </label>
        <label class="checkbox-item">
          <input type="checkbox" name="type_projet[]" value="irrigation">
          Système d'irrigation
        </label>
        <label class="checkbox-item">
          <input type="checkbox" name="type_projet[]" value="mur">
          Mur de soutènement
        </label>
        <label class="checkbox-item">
          <input type="checkbox" name="type_projet[]" value="piscine">
          Piscine
        </label>
        <label class="checkbox-item">
          <input type="checkbox" name="type_projet[]" value="complet">
          Projet complet
        </label>
      </div>
    </div>
    
    <div class="form-row">
      <div class="form-group">
        <label for="superficie">Superficie approximative *</label>
        <select id="superficie" name="superficie" required
                data-pipedrive="custom_superficie">
          <option value="">Choisir une superficie</option>
          <option value="moins_200">Moins de 200 pi²</option>
          <option value="200_500">200 à 500 pi²</option>
          <option value="500_1000">500 à 1 000 pi²</option>
          <option value="plus_1000">Plus de 1 000 pi²</option>
        </select>
      </div>
      
      <div class="form-group">
        <label for="budget">Budget approximatif</label>
        <select id="budget" name="budget" data-pipedrive="custom_budget_client">
          <option value="">Choisir un budget estimé</option>
          <option value="8_15k">Entre $8 000 et $15 000</option>
          <option value="15_30k">Entre $15 000 et $30 000</option>
          <option value="30_50k">Entre $30 000 et $50 000</option>
          <option value="plus_50k">Plus de $50 000</option>
        </select>
      </div>
    </div>
    
    <div class="form-row">
      <div class="form-group">
        <label for="date_souhaitee">Date de début souhaitée</label>
        <input type="date" id="date_souhaitee" name="date_souhaitee"
               data-pipedrive="custom_date_souhaitee">
        <!-- Note JS: définir min = aujourd'hui + 14 jours au chargement -->
      </div>
      
      <div class="form-group">
        <label>Terrain en pente?</label>
        <div class="radio-group">
          <label><input type="radio" name="terrain_pente" value="non"> Non, terrain plat</label>
          <label><input type="radio" name="terrain_pente" value="legere"> Légère pente</label>
          <label><input type="radio" name="terrain_pente" value="forte"> Forte pente</label>
        </div>
      </div>
    </div>
  </fieldset>

  <!-- Section 3: Source et consentement -->
  <fieldset>
    <legend>Informations complémentaires</legend>
    
    <div class="form-group">
      <label for="source">Comment avez-vous entendu parler de nous?</label>
      <select id="source" name="source" data-pipedrive="custom_source_lead">
        <option value="">Sélectionner</option>
        <option value="facebook_instagram">Publicité Facebook / Instagram</option>
        <option value="google">Publicité Google</option>
        <option value="recommandation">Recommandation d'un ami ou voisin</option>
        <option value="enseigne">Enseigne dans mon quartier</option>
        <option value="autre">Autre</option>
      </select>
    </div>
    
    <div class="form-group">
      <label for="message">Message ou détails supplémentaires (optionnel)</label>
      <textarea id="message" name="message" rows="3"
                placeholder="Décrivez votre projet, vos préférences, vos questions..."
                data-pipedrive="note"></textarea>
    </div>
    
    <!-- Campo oculto para tracking -->
    <input type="hidden" name="source_page" value="lp-cour-arriere">
    <input type="hidden" name="utm_source" id="utm_source" value="">
    <input type="hidden" name="utm_medium" id="utm_medium" value="">
    <input type="hidden" name="utm_campaign" id="utm_campaign" value="">
    <input type="hidden" name="ics_score" id="ics_score" value="">
    <input type="hidden" name="ics_classification" id="ics_classification" value="">
    
    <div class="form-group consent-group">
      <label class="checkbox-item required-consent">
        <input type="checkbox" id="consentement" name="consentement" required
               aria-required="true">
        <span>
          J'accepte que Jardín Ideal collecte et utilise mes informations personnelles 
          pour traiter ma demande de soumission, conformément à sa 
          <a href="/politique-confidentialite" target="_blank" rel="noopener">
            politique de confidentialité
          </a>. *
        </span>
      </label>
    </div>
    
  </fieldset>
  
  <div id="form-disclaimer" class="form-disclaimer">
    Votre soumission est gratuite et sans engagement. 
    Nous vous contactons dans les 24 heures.
  </div>
  
  <button type="submit" class="btn-primary btn-large">
    Obtenir ma soumission gratuite →
  </button>
  
</form>
```

### JavaScript de validación + pre-score

```javascript
document.getElementById('form-soumission').addEventListener('submit', async function(e) {
  e.preventDefault();
  
  // 1. Calcular ICS score antes de enviar
  const formData = new FormData(this);
  const icsResult = calcularPreScoreICS({
    typeProjet: formData.getAll('type_projet[]'),
    budget: formData.get('budget'),
    superficie: formData.get('superficie'),
    ville: formData.get('ville'),
    dateSouhaitee: formData.get('date_souhaitee'),
    source: formData.get('source'),
    terrainPente: formData.get('terrain_pente')
  });
  
  // 2. Insertar score en campos ocultos
  document.getElementById('ics_score').value = icsResult.score;
  document.getElementById('ics_classification').value = icsResult.classification;
  
  // 3. Insertar UTM params
  const urlParams = new URLSearchParams(window.location.search);
  document.getElementById('utm_source').value = urlParams.get('utm_source') || '';
  document.getElementById('utm_medium').value = urlParams.get('utm_medium') || '';
  document.getElementById('utm_campaign').value = urlParams.get('utm_campaign') || '';
  
  // 4. Enviar
  try {
    const response = await fetch('/api/soumission', {
      method: 'POST',
      body: new FormData(this)
    });
    
    if (response.ok) {
      // Mostrar confirmación
      document.getElementById('form-soumission').innerHTML = `
        <div class="form-success">
          <h3>✅ Merci ${formData.get('prenom')} !</h3>
          <p>Votre demande a bien été reçue. Un membre de notre équipe vous 
          contactera dans les 24 heures.</p>
          <p>📞 Urgence : <strong>514-266-2504</strong></p>
        </div>
      `;
    }
  } catch (err) {
    console.error(err);
  }
});

// Definir fecha mínima para date picker
const dateInput = document.getElementById('date_souhaitee');
if (dateInput) {
  const minDate = new Date();
  minDate.setDate(minDate.getDate() + 14);
  dateInput.min = minDate.toISOString().split('T')[0];
}
```

---

## 3. CALCULADORA DE ESTIMACIÓN

```html
<section id="calculatrice-prix">
  <h2>Estimez le coût de votre projet</h2>
  <p class="subtitle">Obtenez une fourchette indicative en 30 secondes</p>

  <div class="calculatrice-wrapper">
    <div class="calc-inputs">
      
      <div class="calc-group">
        <label for="calc-type">Type de projet</label>
        <select id="calc-type">
          <option value="">Choisir le type de projet</option>
          <option value="pave_seul">Terrasse en pavé-uni seulement</option>
          <option value="pave_cloture">Pavé + clôture</option>
          <option value="pave_pergola">Pavé + pergola</option>
          <option value="complet">Cour complète (plusieurs éléments)</option>
        </select>
      </div>

      <div class="calc-group">
        <label for="calc-superficie">Superficie de la cour</label>
        <select id="calc-superficie">
          <option value="">Superficie approximative</option>
          <option value="moins_200">Moins de 200 pi² (petite cour)</option>
          <option value="200_500">200 à 500 pi² (cour moyenne)</option>
          <option value="500_1000">500 à 1 000 pi² (grande cour)</option>
          <option value="plus_1000">Plus de 1 000 pi² (très grande)</option>
        </select>
      </div>

      <div class="calc-group">
        <label for="calc-finition">Niveau de finition</label>
        <select id="calc-finition">
          <option value="">Niveau souhaité</option>
          <option value="economique">Économique — matériaux standards</option>
          <option value="standard">Standard — qualité résidentielle (recommandé)</option>
          <option value="premium">Premium — Techo-Bloc, pierre naturelle</option>
          <option value="luxe">Luxe — matériaux haut de gamme, design personnalisé</option>
        </select>
      </div>

      <div class="calc-group">
        <label for="calc-terrain">Votre terrain</label>
        <select id="calc-terrain">
          <option value="">Type de terrain</option>
          <option value="plat">Plat — travaux standards</option>
          <option value="legere_pente">Légère pente — nivellement requis</option>
          <option value="forte_pente">Forte pente — terrassement majeur</option>
          <option value="acces_difficile">Accès difficile — transport spécial</option>
        </select>
      </div>

      <div class="calc-group">
        <label>Éléments additionnels (optionnel)</label>
        <div class="checkbox-grid-small">
          <label><input type="checkbox" class="calc-addon" value="cloture"> Clôture (+~$6,500)</label>
          <label><input type="checkbox" class="calc-addon" value="eclairage"> Éclairage LED (+~$4,000)</label>
          <label><input type="checkbox" class="calc-addon" value="irrigation"> Irrigation (+~$4,500)</label>
          <label><input type="checkbox" class="calc-addon" value="plantation"> Plantation (+~$5,000)</label>
          <label><input type="checkbox" class="calc-addon" value="mur"> Mur soutènement (+~$9,000)</label>
          <label><input type="checkbox" class="calc-addon" value="piscine"> Piscine (+~$50,000)</label>
        </div>
      </div>

      <button type="button" id="btn-calculer" class="btn-secondary">
        Calculer mon estimation
      </button>
    </div>

    <div class="calc-result" id="calc-result" style="display:none">
      <div class="result-box">
        <div class="result-row">
          <span>Estimation minimale</span>
          <strong id="result-min"></strong>
        </div>
        <div class="result-row result-base">
          <span>Estimation de base</span>
          <strong id="result-base"></strong>
        </div>
        <div class="result-row">
          <span>Estimation maximale</span>
          <strong id="result-max"></strong>
        </div>
      </div>
      
      <p class="calc-disclaimer">
        📋 Ces estimations sont indicatives et basées sur des projets similaires réalisés 
        à Montréal. Le prix final sera établi lors de votre visite de soumission gratuite, 
        selon les spécificités réelles de votre terrain et les matériaux choisis.
      </p>
      
      <button type="button" class="btn-primary" 
              onclick="document.getElementById('formulaire').scrollIntoView({behavior:'smooth'})">
        Obtenir la soumission exacte →
      </button>
    </div>
  </div>
</section>
```

```javascript
// CALCULADORA — Lógica completa
const PRIX_BASE = {
  'pave_seul': 10000, 'pave_cloture': 16000,
  'pave_pergola': 22000, 'complet': 35000
};
const MULT_SUP = { 'moins_200': 0.75, '200_500': 1.0, '500_1000': 1.45, 'plus_1000': 1.9 };
const MULT_FIN = { 'economique': 0.75, 'standard': 1.0, 'premium': 1.35, 'luxe': 1.75 };
const MULT_TER = { 'plat': 1.0, 'legere_pente': 1.15, 'forte_pente': 1.3, 'acces_difficile': 1.2 };
const PRIX_ADD = { 'cloture': 6500, 'eclairage': 4000, 'irrigation': 4500,
                   'plantation': 5000, 'mur': 9000, 'piscine': 50000 };

function formatPrix(n) {
  return '$' + Math.round(n).toLocaleString('fr-CA');
}
function arrondir500(n) {
  return Math.round(n / 500) * 500;
}

document.getElementById('btn-calculer').addEventListener('click', function() {
  const type = document.getElementById('calc-type').value;
  const sup  = document.getElementById('calc-superficie').value;
  const fin  = document.getElementById('calc-finition').value;
  const ter  = document.getElementById('calc-terrain').value;
  
  if (!type || !sup || !fin || !ter) {
    alert('Veuillez remplir tous les champs pour obtenir une estimation.');
    return;
  }
  
  let estimation = PRIX_BASE[type] * MULT_SUP[sup] * MULT_FIN[fin] * MULT_TER[ter];
  
  document.querySelectorAll('.calc-addon:checked').forEach(cb => {
    estimation += (PRIX_ADD[cb.value] || 0);
  });
  
  const min  = arrondir500(estimation * 0.80);
  const base = arrondir500(estimation);
  const max  = arrondir500(estimation * 1.20);
  
  document.getElementById('result-min').textContent  = formatPrix(min);
  document.getElementById('result-base').textContent = formatPrix(base);
  document.getElementById('result-max').textContent  = formatPrix(max);
  document.getElementById('calc-result').style.display = 'block';
  document.getElementById('calc-result').scrollIntoView({ behavior: 'smooth' });
});
```

---

## 4. CALCULADORA DE FINANCIAMIENTO

```html
<section id="financement">
  <h2>Simulez votre financement</h2>
  <p class="subtitle">Estimez vos mensualités en quelques clics</p>

  <div class="financement-wrapper">
    <div class="fin-inputs">
      
      <div class="calc-group">
        <label for="fin-montant">Montant du projet ($CAD)</label>
        <div class="input-with-slider">
          <input type="range" id="fin-montant-slider" min="8000" max="80000" step="500" value="25000"
                 oninput="document.getElementById('fin-montant').value = this.value; calculerFin()">
          <input type="number" id="fin-montant" value="25000" min="8000" max="80000" step="500"
                 oninput="document.getElementById('fin-montant-slider').value = this.value; calculerFin()">
        </div>
      </div>

      <div class="calc-group">
        <label for="fin-mise">Mise de fonds (%)</label>
        <div class="input-with-slider">
          <input type="range" id="fin-mise-slider" min="10" max="50" step="5" value="20"
                 oninput="document.getElementById('fin-mise').value = this.value; calculerFin()">
          <input type="number" id="fin-mise" value="20" min="10" max="50" step="5"
                 oninput="document.getElementById('fin-mise-slider').value = this.value; calculerFin()">
          <span>%</span>
        </div>
      </div>

      <div class="calc-group">
        <label for="fin-taux">Taux d'intérêt estimé</label>
        <select id="fin-taux" onchange="calculerFin()">
          <option value="7.9">7,9% / an (excellent dossier)</option>
          <option value="9.9" selected>9,9% / an (bon dossier — estimé)</option>
          <option value="11.9">11,9% / an (dossier standard)</option>
          <option value="13.9">13,9% / an (dossier à consolider)</option>
        </select>
      </div>

      <div class="calc-group">
        <label for="fin-duree">Durée du financement</label>
        <select id="fin-duree" onchange="calculerFin()">
          <option value="12">12 mois (1 an)</option>
          <option value="24">24 mois (2 ans)</option>
          <option value="36">36 mois (3 ans)</option>
          <option value="48">48 mois (4 ans)</option>
          <option value="60" selected>60 mois (5 ans)</option>
        </select>
      </div>
    </div>

    <div class="fin-result" id="fin-result">
      <div class="fin-result-box">
        <div class="fin-row"><span>Montant du projet</span><strong id="fr-montant">$25 000</strong></div>
        <div class="fin-row"><span>Mise de fonds (20%)</span><strong id="fr-mise">$5 000</strong></div>
        <div class="fin-row"><span>Solde à financer</span><strong id="fr-solde">$20 000</strong></div>
        <div class="fin-row"><span>Taux estimé</span><strong id="fr-taux">9,9%/an</strong></div>
        <div class="fin-row"><span>Durée</span><strong id="fr-duree">60 mois</strong></div>
        <div class="fin-row fin-mensualite">
          <span>MENSUALITÉ ESTIMÉE</span>
          <strong id="fr-mensualite">$424/mois</strong>
        </div>
        <div class="fin-row fin-cout">
          <span>Coût total du crédit</span>
          <strong id="fr-cout-total">$25 440</strong>
        </div>
        <div class="fin-row fin-interets">
          <span>dont intérêts</span>
          <strong id="fr-interets">$5 440</strong>
        </div>
      </div>
      
      <!-- DISCLAIMER LEGAL OBLIGATORIO -->
      <div class="fin-disclaimer">
        <strong>⚠️ Simulation indicative uniquement</strong><br>
        Cette calculatrice est fournie à titre d'information générale seulement. 
        Les mensualités affichées sont des estimations basées sur des paramètres simplifiés. 
        Elles ne constituent <strong>pas une offre de financement</strong> ni une 
        <strong>approbation de crédit</strong>. Les taux et conditions réels dépendent 
        de votre dossier personnel et du partenaire financier choisi. 
        Jardín Ideal n'est pas un prêteur agréé.
      </div>
    </div>
  </div>

  <!-- Formulario de solicitud de financiamiento -->
  <div id="form-financement-wrapper">
    <h3>Demander une option de financement</h3>
    <form id="form-financement" action="/api/financement" method="POST">
      <div class="form-row">
        <div class="form-group">
          <label for="fin-prenom">Prénom *</label>
          <input type="text" id="fin-prenom" name="prenom" required>
        </div>
        <div class="form-group">
          <label for="fin-nom">Nom *</label>
          <input type="text" id="fin-nom" name="nom" required>
        </div>
      </div>
      <div class="form-row">
        <div class="form-group">
          <label for="fin-tel">Téléphone *</label>
          <input type="tel" id="fin-tel" name="telephone" required>
        </div>
        <div class="form-group">
          <label for="fin-email">Courriel *</label>
          <input type="email" id="fin-email" name="email" required>
        </div>
      </div>
      <div class="form-row">
        <div class="form-group">
          <label for="fin-montant-form">Montant estimé du projet *</label>
          <input type="number" id="fin-montant-form" name="montant_projet" 
                 min="8000" max="200000" required>
        </div>
        <div class="form-group">
          <label for="fin-revenu">Revenus annuels (approximatif)</label>
          <select id="fin-revenu" name="revenus">
            <option value="">Sélectionner</option>
            <option value="moins_40k">Moins de $40 000</option>
            <option value="40_70k">$40 000 – $70 000</option>
            <option value="70_100k">$70 000 – $100 000</option>
            <option value="plus_100k">Plus de $100 000</option>
          </select>
        </div>
      </div>
      <div class="form-group">
        <label>Statut d'occupation *</label>
        <div class="radio-group">
          <label><input type="radio" name="statut_occupation" value="proprietaire" required> Propriétaire</label>
          <label><input type="radio" name="statut_occupation" value="locataire"> Locataire</label>
        </div>
      </div>
      <input type="hidden" name="source_page" value="lp-cour-arriere-financement">
      <div class="form-group consent-group">
        <label class="checkbox-item">
          <input type="checkbox" name="consentement_fin" required>
          <span>J'autorise Jardín Ideal à utiliser mes informations pour m'informer 
          des options de financement disponibles. 
          <a href="/politique-confidentialite" target="_blank">Politique de confidentialité</a>. *</span>
        </label>
      </div>
      <button type="submit" class="btn-secondary">Demander une option de financement →</button>
    </form>
  </div>
</section>
```

```javascript
// CALCULADORA FINANCIAMIENTO — Lógica
function calculerFin() {
  const montant = parseFloat(document.getElementById('fin-montant').value) || 25000;
  const misePct = parseFloat(document.getElementById('fin-mise').value) || 20;
  const tauxAn  = parseFloat(document.getElementById('fin-taux').value) || 9.9;
  const duree   = parseInt(document.getElementById('fin-duree').value) || 60;

  const mise   = montant * (misePct / 100);
  const solde  = montant - mise;
  const tauxM  = tauxAn / 100 / 12;
  
  let mensualite;
  if (tauxM === 0) {
    mensualite = solde / duree;
  } else {
    const facteur = Math.pow(1 + tauxM, duree);
    mensualite = solde * (tauxM * facteur) / (facteur - 1);
  }

  const coutTotal   = mensualite * duree;
  const coutInterets = coutTotal - solde;

  const fmt = n => '$' + Math.round(n).toLocaleString('fr-CA');

  document.getElementById('fr-montant').textContent  = fmt(montant);
  document.getElementById('fr-mise').textContent     = fmt(mise);
  document.getElementById('fr-solde').textContent    = fmt(solde);
  document.getElementById('fr-taux').textContent     = tauxAn.toFixed(1) + '%/an';
  document.getElementById('fr-duree').textContent    = duree + ' mois';
  document.getElementById('fr-mensualite').textContent = fmt(mensualite) + '/mois';
  document.getElementById('fr-cout-total').textContent = fmt(coutTotal);
  document.getElementById('fr-interets').textContent  = fmt(coutInterets);
}

// Inicializar al cargar
document.addEventListener('DOMContentLoaded', calculerFin);
```

---

## 5. POLÍTICA DE PRIVACIDAD — PLANTILLA

```markdown
# Politique de confidentialité — Jardín Ideal
**Dernière mise à jour:** [DATE]

Jardín Ideal (ci-après « nous ») s'engage à protéger vos renseignements personnels 
conformément à la Loi 25 (Loi sur la protection des renseignements personnels dans 
le secteur privé, LPRPDE, et modifications au droit québécois depuis 2022).

## 1. Renseignements collectés
Nous collectons les informations que vous fournissez via nos formulaires:
prénom, nom, téléphone, courriel, adresse du projet, type et budget du projet.

## 2. Utilisation des renseignements
Ces informations sont utilisées exclusivement pour:
- Traiter votre demande de soumission gratuite
- Vous contacter au sujet de votre projet
- Améliorer nos services (données anonymisées)

## 3. Partage des informations
Vos données sont transmises aux systèmes suivants:
- Pipedrive (CRM) — gestion des contacts et projets
- Zapier — automatisation des communications
Ces plateformes sont liées par des accords de confidentialité.
Vos données ne sont jamais vendues à des tiers.

## 4. Conservation
Vos informations sont conservées pendant 3 ans après votre dernier contact avec nous.

## 5. Vos droits
Vous pouvez en tout temps:
- Demander l'accès à vos informations personnelles
- Demander la rectification de vos informations
- Demander la suppression de vos informations
Contact: daniel@groupe-ideal.com | 514-266-2504

## 6. Cookies et technologies de suivi
Ce site utilise [Meta Pixel / Google Analytics — ADAPTER] pour mesurer l'efficacité 
de nos publicités. Vous pouvez refuser via les paramètres de votre navigateur.

## 7. Contact pour questions de vie privée
Daniel Figueroa · daniel@groupe-ideal.com · 514-266-2504
```

---

## 6. INTEGRACIÓN ZAPIER — MAPPING DE CAMPOS

### Zap: Formulario LP → Pipedrive (Nuevo Deal)

| Trigger | Action | Campo Zapier → Pipedrive |
|---------|--------|--------------------------|
| Webhook POST /api/soumission | Create Person | prenom + nom → Name |
| | Create Person | email → Email |
| | Create Person | telephone → Phone |
| | Create Deal | "LP-CA · " + prenom + " " + nom → Title |
| | Create Deal | budget seleccionado → Value (medianom) |
| | Create Deal | "Leads qualifiés" → Pipeline |
| | Create Deal | "Nouveau lead" → Stage |
| | Create Deal | adresse + ville → custom_adresse_projet |
| | Create Deal | type_projet (joined) → custom_type_projet |
| | Create Deal | superficie → custom_superficie |
| | Create Deal | budget → custom_budget_client |
| | Create Deal | date_souhaitee → custom_date_souhaitee |
| | Create Deal | terrain_pente → custom_terrain |
| | Create Deal | source → custom_source_lead |
| | Create Deal | ics_score → custom_ics_score |
| | Create Deal | ics_classification → custom_ics_classification |
| | Create Note | Nota automática formateada (ver template) |
| | Create Activity | "Appeler dans " + delai_recommande → Task |

### Template de nota automática Pipedrive

```
[NOUVEAU LEAD — Landing Page Cour Arrière]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Date: {timestamp}
Source annonce: {utm_source} / {utm_campaign}
Source déclarée: {source}
ICS Pré-score: {ics_score}/100 → {ics_classification}
Délai de contact recommandé: {delai_appel}

DÉTAILS DU PROJET
Type: {type_projet}
Superficie: {superficie}
Budget déclaré: {budget}
Date souhaitée: {date_souhaitee}
Terrain en pente: {terrain_pente}
Adresse: {adresse}, {ville}

CONTACT
Téléphone: {telephone}
Email: {email}

MESSAGE DU CLIENT:
{message}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Généré automatiquement par lp-cour-arriere]
```

---

## 7. VARIABLES CSS DE MARCA

```css
:root {
  --verde-oscuro: #052B16;
  --verde-medio: #0A4523;
  --verde-claro: #008E3F;
  --dorado: #C8A45A;
  --dorado-pale: #E8D5A3;
  --crema: #F5F2EB;
  --crema-medio: #EAE5D8;
  --blanco: #FAFAF8;
  --texto-oscuro: #1C2118;
  --texto-medio: #4A5546;
  --rojo-alerta: #A03030;
  
  /* Tipografía */
  --font-display: Georgia, 'Times New Roman', serif;
  --font-body: 'Helvetica Neue', Helvetica, Arial, sans-serif;
  --font-mono: 'Courier New', Courier, monospace;
  
  /* Teléfono siempre en dorado */
  --color-telefono: var(--dorado);
}

/* CTA principal */
.btn-primary {
  background: var(--verde-oscuro);
  color: var(--crema);
  padding: 16px 32px;
  font-size: 16px;
  font-weight: 700;
  border: none;
  cursor: pointer;
  transition: background 0.15s;
}
.btn-primary:hover { background: var(--verde-medio); }

/* Teléfono */
.phone-number {
  color: var(--dorado);
  font-weight: 700;
  text-decoration: none;
}
```

---

## 8. CHECKLIST DE PUBLICACIÓN

```
PRE-LANZAMIENTO — LEGAL
[ ] Política de privacidad redactada y aprobada (Loi 25)
[ ] Checkbox consentimiento en formulario soumission
[ ] Checkbox consentimiento en formulario financiamiento
[ ] Disclaimer calculadora estimación visible
[ ] Disclaimer calculadora financiamiento visible (con "pas une approbation de crédit")
[ ] Enlace política de privacidad en footer
[ ] Banner cookies si se usa Meta Pixel o Google Analytics

PRE-LANZAMIENTO — TÉCNICO
[ ] Formulario soumission — todos los campos mapeados a Pipedrive
[ ] Formulario financement — todos los campos mapeados a Pipedrive
[ ] Zap configurado y probado (lead ficticio → Pipedrive)
[ ] ICS pre-score calculado correctamente
[ ] Nota automática generada en Pipedrive
[ ] Activity creada automáticamente en Pipedrive
[ ] UTM params capturados en campos ocultos
[ ] Fecha mínima en date picker (hoy + 14 días)
[ ] Teléfono en color dorado #C8A45A en toda la página
[ ] Página responsive (mobile first)
[ ] Velocidad de carga <2.5s (Lighthouse)
[ ] Meta tags (title, description, OG) configurados

PRE-LANZAMIENTO — CONTENIDO
[ ] Imagen hero: score ≥90/100 PREMIUM_VISUAL_SCORE
[ ] Mínimo 6 réalisations avant/après con datos reales
[ ] Mínimo 3 testimonios con barrio + presupuesto + fecha
[ ] FAQ: 10 preguntas completas
[ ] Tabla de 4 niveles con fotos representativas
[ ] Calculadora de estimación probada con 5+ combinaciones
[ ] Calculadora de financiamiento probada y disclaimer visible

POST-LANZAMIENTO — MÉTRICAS
[ ] Meta Pixel instalado y verificado (si aplica)
[ ] Google Analytics configurado (si aplica)
[ ] URL parámetros UTM para campañas Meta Ads
[ ] Tasa de conversión baseline establecida (día 1)
[ ] Monitoreo CPL integrado en reporte diario Cowork
```

---

*Lista técnica de cambios — Jardín Ideal AI System · 2026-06-24*
*Implementar en orden: Legal → Formularios → Calculadoras → Integración → Contenido*
