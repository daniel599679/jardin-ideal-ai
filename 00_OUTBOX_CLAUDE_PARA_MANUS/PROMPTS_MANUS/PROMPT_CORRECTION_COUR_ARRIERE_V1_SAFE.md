# PROMPT MANUS — Correcciones Cour Arrière V1 → V2 (VERSIÓN SAFE)
**Versión:** SAFE con datos confirmados al 2026-06-24
**Estado de datos:**
- ✅ Courriel: `info@jardin-ideal.com` CONFIRMADO
- ✅ Garantie pavé/pavé uni: **5 ans** CONFIRMADO
- ✅ Disclaimer financement CONFIRMADO
- ⏳ Meta Pixel ID: PENDIENTE (placeholder `TU_PIXEL_ID` hasta confirmación)
- ⏳ Zapier webhook: PENDIENTE (placeholder `TU_ZAPIER_WEBHOOK_URL` hasta confirmación)

---

## INSTRUCCIONES DE USO

1. Copiar TODO el contenido entre `===INICIO PROMPT===` y `===FIN PROMPT===`
2. Pegar en Manus al inicio de la sesión de trabajo
3. Proporcionar el archivo HTML V1 adjunto
4. Solicitar a Manus que genere `COUR_ARRIERE_V2.html`
5. Guardar el resultado en `00_INBOX_MANUS/LANDING_PAGES/`
6. Reemplazar `TU_PIXEL_ID` y `TU_ZAPIER_WEBHOOK_URL` cuando Daniel proporcione los datos reales

---

===INICIO PROMPT===

## CONTEXTE — Jardín Ideal

Tu es un développeur web senior spécialisé en landing pages de haute conversion pour le marché québécois. Tu vas apporter des corrections précises et uniquement celles listées à une landing page existante. **Règle absolue : ne pas modifier ce qui n'est pas dans la liste des corrections.**

### Informations de la compagnie — DONNÉES CONFIRMÉES
- **Nom:** Jardin Idéal / Groupe Ideal
- **Téléphone:** 514-266-2504
- **Courriel officiel:** info@jardin-ideal.com ✅ (confirmé — ne pas modifier)
- **Site:** jardin-ideal.com
- **RBQ:** #5773-1983-01
- **Assurance:** Responsabilité civile 2 M$
- **Expérience:** 15+ ans (depuis 2009)
- **Projets réalisés:** 1 500+
- **Marché:** Grand Montréal — Laval, Rive-Sud, Rive-Nord

---

## FICHIER DE RÉFÉRENCE

Travaille à partir du fichier HTML V1 fourni. Applique uniquement les corrections listées ci-dessous. Ne change rien d'autre.

### CE QUI EST CORRECT ET NE DOIT PAS ÊTRE MODIFIÉ
- Structure générale de la page (ordre des sections)
- Charte graphique : couleurs `--dark:#052B16`, `--green:#008E3F`, doré `#C8A45A`, polices Montserrat + Open Sans
- Témoignages Google (Madeleine, Bétina Eustache, Monique Létourneau) — textes réels intacts
- Checklist entrepreneur (8 questions/réponses)
- Galerie avec 9 projets et hotspots interactifs
- Chatbot Alex
- Sticky bar mobile
- Section politique de confidentialité (#confidentialite) — texte légal existant est correct
- Calculatrice d'estimation visuelle (cartes S/M/L/XL + checkboxes visuels)
- Tableau des prix (entrée / milieu / haut / prestige)

---

## CORRECTIONS À APPLIQUER

### CORRECTION 1 — OBLIGATOIRE (Loi 25 Québec)
**Ajouter checkbox consentement dans le formulaire principal `#coordsForm`**

Localise la div du formulaire `#coordsForm`. Juste avant le bouton de soumission principal (celui qui appelle `submitForm()`), insère :

```html
<div style="margin:16px 0;padding:14px 16px;background:rgba(0,142,63,.06);border-radius:8px;border:1px solid rgba(0,142,63,.2)">
  <label style="display:flex;align-items:flex-start;gap:12px;cursor:pointer;font-size:.85rem;color:var(--text)">
    <input type="checkbox" id="consentement" name="consentement" required
           style="margin-top:3px;accent-color:var(--green);width:18px;height:18px;cursor:pointer;flex-shrink:0">
    <span>J'accepte que Jardin Idéal collecte et utilise mes renseignements personnels pour traiter ma demande de soumission gratuite, conformément à sa <a href="#confidentialite" style="color:var(--green)">politique de confidentialité</a>. *</span>
  </label>
</div>
```

Dans la fonction JS `submitForm()`, ajouter en PREMIÈRE LIGNE (avant toute autre logique) :
```javascript
if (!document.getElementById('consentement').checked) {
  alert('Veuillez accepter la politique de confidentialité pour continuer.');
  return;
}
```

---

### CORRECTION 2 — OBLIGATOIRE (Loi 25 Québec)
**Ajouter checkbox consentement dans le modal financement `#prequalModal`**

Dans l'étape 3 du modal (`#pqStep3`), juste avant le bouton "Envoyer ma demande", ajouter :

```html
<div style="margin:16px 0;padding:12px 14px;background:rgba(0,142,63,.06);border-radius:8px;border:1px solid rgba(0,142,63,.2)">
  <label style="display:flex;align-items:flex-start;gap:10px;cursor:pointer;font-size:.82rem;color:var(--text)">
    <input type="checkbox" id="consentementFin" name="consentementFin" required
           style="margin-top:2px;accent-color:var(--green);width:16px;height:16px;cursor:pointer;flex-shrink:0">
    <span>J'autorise Jardin Idéal à utiliser mes renseignements pour préparer mon dossier de financement et me contacter. <a href="#confidentialite" style="color:var(--green)">Politique de confidentialité</a>. *</span>
  </label>
</div>
```

Dans la fonction `pqSubmit()`, ajouter en première ligne :
```javascript
if (!document.getElementById('consentementFin').checked) {
  alert('Veuillez accepter la politique de confidentialité pour continuer.');
  return;
}
```

---

### CORRECTION 3 — OBLIGATOIRE (éthique / légal)
**Remplacer "Pré-approuvé" dans `#pqConfirm`**

Dans la section de confirmation du modal financement, chercher et remplacer :

AVANT :
```
✅ Pré-approuvé
```
APRÈS :
```
✅ Demande reçue
```

Chercher aussi tout texte contenant "pré-approuvée" ou "pre-approuvée" et remplacer par :
> "Votre demande a bien été reçue. Un conseiller Jardin Idéal analysera votre dossier et vous contactera sous 24h avec les meilleures options disponibles."

---

### CORRECTION 4 — OBLIGATOIRE (leads perdus)
**Connecter `submitForm()` à Zapier webhook**

Remplacer la fonction `submitForm()` existante (ou la compléter si incomplète) pour qu'elle envoie les données :

```javascript
async function submitForm() {
  // Validation Loi 25
  if (!document.getElementById('consentement').checked) {
    alert('Veuillez accepter la politique de confidentialité pour continuer.');
    return;
  }

  // Récupérer les valeurs
  const payload = {
    prenom:          getValue('fPrenom'),
    nom:             getValue('fNom'),
    telephone:       getValue('fTel'),
    email:           getValue('fEmail'),
    code_postal:     getValue('fCodePostal'),
    ville:           getValue('fVille'),
    type_projet:     getValue('fTypeProjet'),
    superficie:      getValue('fSuperficie'),
    budget:          getValue('fBudget'),
    description:     getValue('fDescription'),
    adresse_projet:  getValue('fAdresse') || '',
    source:          getValue('fSource') || '',
    landing_page:    'cour-arriere-v2',
    date_soumission: new Date().toISOString()
  };

  // Validation champs obligatoires
  const required = ['prenom','nom','telephone','email','code_postal','type_projet'];
  for (const f of required) {
    if (!payload[f] || payload[f].trim() === '') {
      alert('Veuillez remplir tous les champs obligatoires.');
      return;
    }
  }

  // Afficher état de chargement
  const btn = document.querySelector('#coordsForm button[type="submit"], #coordsForm .btn-submit');
  if (btn) { btn.disabled = true; btn.textContent = 'Envoi en cours...'; }

  try {
    await fetch('TU_ZAPIER_WEBHOOK_URL', {
      method: 'POST',
      mode: 'no-cors',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });

    // Meta Pixel Lead event
    if (typeof fbq === 'function') fbq('track', 'Lead');

    // Afficher confirmation
    showConfirmation();

  } catch(e) {
    console.error('Erreur envoi:', e);
    alert('Une erreur est survenue. Veuillez réessayer ou nous appeler au 514-266-2504.');
    if (btn) { btn.disabled = false; btn.textContent = 'Envoyer ma demande de soumission gratuite'; }
  }
}

function getValue(id) {
  const el = document.getElementById(id);
  return el ? el.value.trim() : '';
}
```

Note: `mode: 'no-cors'` est requis pour les requêtes vers Zapier depuis une page HTML statique.

---

### CORRECTION 5 — IMPORTANTE (durée financement sélectionnable)
**Remplacer la durée fixe 240 mois dans le mini-calculateur**

Dans `#miniCalc`, trouver l'`<input type="hidden" id="miniMonths" value="240">` et son label fixe.

Remplacer par :
```html
<div class="mini-calc-row">
  <label style="font-size:.8rem;color:var(--text-muted);font-family:var(--fm)">Durée du financement</label>
  <select id="miniMonthsSel"
          onchange="document.getElementById('miniMonths').value=this.value; if(typeof onCapitalSlide==='function') onCapitalSlide();"
          style="width:100%;padding:8px 12px;border:1.5px solid var(--border);border-radius:6px;font-family:var(--fb);font-size:.88rem;color:var(--text);background:#fff;cursor:pointer;margin-top:4px">
    <option value="60">60 mois — 5 ans</option>
    <option value="120">120 mois — 10 ans</option>
    <option value="180">180 mois — 15 ans</option>
    <option value="240" selected>240 mois — 20 ans (mensualité la plus basse)</option>
  </select>
</div>
<input type="hidden" id="miniMonths" value="240">
```

Appliquer le même changement dans l'étape 2 du modal `#prequalModal`.

---

### CORRECTION 6 — IMPORTANTE (données cohérentes)
**Supprimer la ligne contradictoire dans le hero**

Chercher et supprimer (ou commenter) la ligne :
```
⭐ 4.9/5 sur Google · +200 projets réalisés
```

Cette information contredit les trust pills qui indiquent "1 500+ projets réalisés". Garder uniquement les trust pills.

---

### CORRECTION 7 — IMPORTANTE (garantie cohérente)
**Uniformiser la garantie dans la galerie**

Dans la section galerie, chercher les textes des hotspots. Si un hotspot de piscine indique "garantie 10 ans structure", remplacer par :
```
Garantie selon le type de projet et les conditions du contrat
```

**Règle garantie confirmée :**
- Pavé / Pavé uni uniquement : "Garantie de 5 ans sur les travaux de pavé"
- Tous les autres services : "Garantie selon le type de projet, les matériaux sélectionnés et les conditions du contrat"

---

### CORRECTION 8 — IMPORTANTE (attribution marketing)
**Ajouter le champ "Source" dans le formulaire**

Dans `#coordsForm`, après les champs de description et upload (si présent), AVANT le bloc consentement, ajouter :

```html
<div style="margin-bottom:16px">
  <label style="display:block;font-weight:600;margin-bottom:6px;font-size:.9rem;font-family:var(--fm)">Comment avez-vous entendu parler de nous ? <span style="font-weight:400;color:var(--text-muted)">(optionnel)</span></label>
  <select id="fSource" name="source"
          style="width:100%;padding:12px 14px;border:1.5px solid var(--border);border-radius:8px;font-family:var(--fb);font-size:.9rem;color:var(--text);background:#fff;cursor:pointer">
    <option value="">Sélectionnez</option>
    <option value="facebook_instagram">Publicité Facebook / Instagram</option>
    <option value="google_ads">Publicité Google</option>
    <option value="google_organic">Recherche Google (résultats naturels)</option>
    <option value="recommandation">Recommandation d'un ami ou voisin</option>
    <option value="enseigne">Enseigne dans mon quartier</option>
    <option value="deja_client">Déjà client Jardin Idéal</option>
    <option value="autre">Autre</option>
  </select>
</div>
```

---

### CORRECTION 9 — IMPORTANTE (FAQ étendue)
**Ajouter 5 questions à la FAQ (de 5 à 10)**

Après la 5e question existante de la FAQ, ajouter en format `<details>` identique aux existants :

```html
<details>
  <summary>Quelle est la meilleure période pour faire des travaux d'aménagement au Québec ?</summary>
  <p>La saison principale va de mai à octobre. Pour les projets de pavé uni, nous pouvons travailler jusqu'en novembre si les températures restent au-dessus de 0°C. Nous planifions toujours selon la météo pour garantir la qualité de nos travaux.</p>
</details>

<details>
  <summary>Combien de temps à l'avance dois-je planifier mon projet ?</summary>
  <p>En haute saison (juin–août), notre calendrier se remplit rapidement. Idéalement, contactez-nous 6 à 8 semaines à l'avance pour sécuriser votre date. <a href="#formulaire" style="color:var(--green)">Contactez-nous maintenant</a> pour vérifier les disponibilités pour votre projet.</p>
</details>

<details>
  <summary>Le prix de la soumission peut-il changer après avoir commencé les travaux ?</summary>
  <p>Non, si vous ne demandez pas de modifications. Notre soumission est ferme et détaillée. Des changements en cours de travaux peuvent générer des coûts supplémentaires, mais ils sont toujours approuvés par écrit avec vous avant d'être réalisés.</p>
</details>

<details>
  <summary>Comment entretenir mon pavé uni l'hiver ?</summary>
  <p>Évitez les fondants corrosifs comme le sel de table ordinaire — préférez un abrasif écologique ou du sel de mer. Un scellant appliqué à l'automne protège votre investissement et facilite l'entretien. Nous proposons également des services d'entretien annuel.</p>
</details>

<details>
  <summary>Est-ce que la soumission m'engage à quelque chose ?</summary>
  <p>Non, absolument pas. La soumission est 100% gratuite et sans engagement de votre part. Vous n'êtes lié par rien tant que vous n'avez pas signé un contrat formel avec nous.</p>
</details>
```

---

### CORRECTION 10 — MINEURE (textes et dates)
**Corrections d'orthographe et de mise à jour**

1. Chercher `"Comment ca fonctionne"` → remplacer par `"Comment ça fonctionne"`
2. Chercher `© 2025 Jardin Idéal` → remplacer par `© 2026 Jardin Idéal`
3. Chercher tout lien ou texte visible vers `admin-cour-arriere.html` → retirer ou commenter le lien
4. Vérifier que le courriel affiché publiquement est bien `info@jardin-ideal.com` — si c'est déjà le cas, ne rien changer

---

## ÉLÉMENTS À NE PAS MODIFIER

- Politique de confidentialité (#confidentialite) — texte légal correct
- Témoignages Google (Madeleine, Bétina Eustache, Monique Létourneau)
- Checklist entrepreneur (8 questions/réponses)
- Galerie 9 projets avec hotspots
- Tableau des prix (4 colonnes : entrée / milieu / haut / prestige)
- Calculatrice d'estimation visuelle (cartes S/M/L/XL)
- Chatbot Alex et son script
- Sticky bar mobile
- Tokens CSS (couleurs, polices, border-radius)
- Téléphone : 514-266-2504 (déjà correct en doré)
- Trust pills : "1 500+ projets", "15 ans", "Garantie 5 ans", "RBQ #5773-1983-01"

---

## RÈGLE ABSOLUE — NE PAS INVENTER

Ne pas ajouter :
- Des prix exacts non confirmés
- Des garanties pour des services autres que pavé/pavé uni
- Des certifications ou licences fictives
- Des statistiques sans source confirmée dans ce prompt
- Du texte en anglais dans la page principale

---

## ÉLÉMENTS AVEC PLACEHOLDER (à remplacer manuellement)

Ces éléments doivent rester comme placeholder dans la V2 — ils seront remplacés par Daniel quand disponibles :

| Placeholder | À remplacer par | Qui / Quand |
|------------|----------------|------------|
| `TU_PIXEL_ID` dans `fbq('init', 'TU_PIXEL_ID')` | ID réel Meta Pixel | Daniel → Meta Business Suite |
| `TU_ZAPIER_WEBHOOK_URL` dans `submitForm()` | URL webhook Zapier | Daniel → configurer Zap |

Ne pas inventer ces valeurs. Garder les placeholders exactement tels quels pour faciliter la recherche + remplacement.

---

## LIVRAISON ATTENDUE

Un fichier HTML unique, auto-contenu (CSS et JS inline), qui :
1. Fonctionne localement sans serveur web
2. Intègre les 10 corrections listées ci-dessus
3. Ne brise aucune section existante
4. Est nommé exactement : `COUR_ARRIERE_V2.html`

À la fin, confirme quelles corrections ont été appliquées avec succès et note si une correction n'a pas pu être appliquée et pourquoi.

===FIN PROMPT===

---

## NOTES POUR DANIEL (checklist avant d'envoyer à Manus)

- [ ] Avoir le fichier HTML V1 prêt pour joindre à Manus
- [ ] Ce prompt est safe : pas de données inventées, placeholders clairs
- [ ] Après V2 générée : récupérer et tester localement
- [ ] Remplacer `TU_PIXEL_ID` avec l'ID réel de Meta Business Suite
- [ ] Remplacer `TU_ZAPIER_WEBHOOK_URL` avec l'URL du Zap configuré
- [ ] Tester le formulaire complet avant de publier
- [ ] Sauvegarder V2 dans `00_INBOX_MANUS/LANDING_PAGES/`

---

*Prompt SAFE v1.0 — Jardín Ideal AI System · 2026-06-24*
*Données confirmées par Daniel le 2026-06-24 | Audit V1: 68/100*
