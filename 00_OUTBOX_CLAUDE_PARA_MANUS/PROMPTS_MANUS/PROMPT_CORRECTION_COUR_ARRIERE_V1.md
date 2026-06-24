# PROMPT PARA MANUS — Correcciones Cour Arrière V1 → V2
**Archivo de referencia:** `2026-06-24_COUR_ARRIERE_V1_HTML.html`
**Versión a generar:** `2026-06-24_COUR_ARRIERE_V2_HTML.html`
**Fecha:** 2026-06-24

---

## INSTRUCCIONES DE USO

1. Copiar TODO el contenido entre `===INICIO===` y `===FIN===`
2. Pegar en Manus
3. Proporcionar a Manus el archivo HTML de referencia (V1)
4. Exportar el resultado como `2026-06-24_COUR_ARRIERE_V2_HTML.html`
5. Guardar en `00_INBOX_MANUS/LANDING_PAGES/`

---

===INICIO===

## CONTEXTO — Jardín Ideal

Eres un développeur web senior spécialisé en pages d'atterrissage de conversion haut de gamme pour le marché québécois. Tu dois apporter des corrections précises à une landing page existante pour la compagnie **Jardin Idéal** (Groupe Ideal), spécialiste en aménagement paysager résidentiel à Montréal et banlieues.

**Informations de la compagnie :**
- Nom : Jardin Idéal / Groupe Ideal
- Téléphone : 514-266-2504
- Courriel de contact client : info@jardin-ideal.com
- Site : jardin-ideal.com
- RBQ : #5773-1983-01
- Spécialité : cour arrière, pavé-uni, pergola, terrasse, piscine, clôture, éclairage
- Clientèle : propriétaires résidentiels, Grand Montréal, budget $8 000–$75 000+

---

## FICHIER DE RÉFÉRENCE

Travaille à partir du fichier HTML de la version V1 de la landing page cour arrière. Tu dois appliquer les corrections décrites ci-dessous sans modifier ce qui fonctionne bien.

**Ce qui est bien et ne doit PAS être changé :**
- La structure générale de la page (ordre des sections)
- La charte graphique (couleurs, polices, tokens CSS)
- Les témoignages Google (Madeleine, Bétina Eustache, Monique Létourneau) — textes réels, ne pas modifier
- La section checklist entrepreneur (8 questions + réponses Jardin Idéal)
- La galerie avec hotspots interactifs (9 projets)
- Le chatbot Alex
- La sticky bar mobile
- La politique de confidentialité (section #confidentialite) — texte légal existant est correct
- La calculatrice d'estimation visuelle (cartes S/M/L/XL + checkboxes visuels)

---

## CORRECTIONS À APPLIQUER — V1 → V2

### CORRECTION 1 — OBLIGATOIRE (Loi 25 Québec)
**Ajouter un checkbox de consentement dans le formulaire de soumission**

Dans la section `#coordsForm`, AVANT le bouton "Envoyer ma demande de soumission gratuite", ajouter :

```html
<div style="margin:16px 0;padding:14px 16px;background:rgba(0,142,63,.06);border-radius:8px;border:1px solid rgba(0,142,63,.2)">
  <label style="display:flex;align-items:flex-start;gap:12px;cursor:pointer;font-size:.85rem;color:var(--text)">
    <input type="checkbox" id="consentement" name="consentement" required
           style="margin-top:3px;accent-color:var(--green);width:18px;height:18px;cursor:pointer;flex-shrink:0">
    <span>J'accepte que Jardin Idéal collecte et utilise mes renseignements personnels pour traiter ma demande de soumission gratuite, conformément à sa <a href="#confidentialite" style="color:var(--green)">politique de confidentialité</a>. *</span>
  </label>
</div>
```

Dans la fonction JS `submitForm()`, ajouter en première ligne :
```javascript
if (!document.getElementById('consentement').checked) {
  alert('Veuillez accepter la politique de confidentialité pour continuer.');
  return;
}
```

---

### CORRECTION 2 — OBLIGATOIRE (Loi 25 Québec)
**Ajouter un checkbox de consentement dans le modal de financement**

Dans `#pqStep3`, AVANT le bouton "Envoyer ma demande", ajouter :

```html
<div style="margin:16px 0;padding:12px 14px;background:rgba(0,142,63,.06);border-radius:8px;border:1px solid rgba(0,142,63,.2)">
  <label style="display:flex;align-items:flex-start;gap:10px;cursor:pointer;font-size:.82rem;color:var(--text)">
    <input type="checkbox" id="consentementFin" required
           style="margin-top:2px;accent-color:var(--green);width:16px;height:16px;cursor:pointer;flex-shrink:0">
    <span>J'autorise Jardin Idéal à utiliser mes renseignements pour préparer mon dossier de financement et me contacter. <a href="#confidentialite" style="color:var(--green)">Politique de confidentialité</a>. *</span>
  </label>
</div>
```

Dans la fonction `pqSubmit()`, vérifier que `consentementFin` est coché avant de continuer.

---

### CORRECTION 3 — OBLIGATOIRE (légal/éthique)
**Remplacer "Pré-approuvé" par "Demande reçue" dans la confirmation du modal financement**

Dans `#pqConfirm`, remplacer :
```html
<span>✅ Pré-approuvé</span>
```
Par :
```html
<span>✅ Demande reçue</span>
```

Remplacer le texte :
> "Votre demande de financement est pré-approuvée."

Par :
> "Votre demande a bien été reçue. Un conseiller Jardin Idéal analysera votre dossier et vous contactera sous 24h avec les meilleures options disponibles."

---

### CORRECTION 4 — IMPORTANTE (qualité des leads)
**Ajouter le champ "Adresse du projet" dans le formulaire de contact**

Dans `#coordsForm`, après les champs Ville/Code postal, ajouter :

```html
<div class="form-row single">
  <div class="form-group">
    <label>Adresse du projet (optionnel)</label>
    <input type="text" id="fAdresse" name="adresse_projet" 
           autocomplete="street-address" 
           placeholder="Ex: 123 rue Saint-Denis, Montréal">
  </div>
</div>
```

Ajouter aussi `fAdresse` dans le payload de `submitForm()`.

---

### CORRECTION 5 — IMPORTANTE (attribution marketing)
**Ajouter le champ "Comment avez-vous entendu parler de nous?"**

Dans `#coordsForm`, après la zone d'upload, AVANT le bloc de consentement, ajouter :

```html
<div class="form-row single">
  <div class="form-group">
    <label>Comment avez-vous entendu parler de nous? (optionnel)</label>
    <select id="fSource" name="source">
      <option value="">Sélectionnez</option>
      <option value="facebook_instagram">Publicité Facebook / Instagram</option>
      <option value="google">Publicité Google</option>
      <option value="recommandation">Recommandation d'un ami ou voisin</option>
      <option value="enseigne">Enseigne dans mon quartier</option>
      <option value="autre">Autre</option>
    </select>
  </div>
</div>
```

---

### CORRECTION 6 — IMPORTANTE (cohérence des données)
**Unifier les chiffres mentionnés dans le hero**

Chercher et supprimer la ligne suivante dans le hero :
```
⭐ 4.9/5 sur Google · +200 projets réalisés
```

Garder uniquement les trust pills qui disent "1 500+ projets réalisés". Les deux chiffres sont contradictoires.

---

### CORRECTION 7 — IMPORTANTE (cohérence garantie)
**Uniformiser la garantie piscine à 5 ans**

Dans la galerie (hotspot de la piscine creusée), remplacer :
```
garantie 10 ans structure
```
Par :
```
garantie 5 ans structure
```

Cette mise à jour aligne le message avec la checklist entrepreneur et les trust pills (qui disent tous "Garantie 5 ans").

---

### CORRECTION 8 — IMPORTANTE (UX financement)
**Permettre la sélection de la durée dans le mini-calculateur**

Dans `#miniCalc`, remplacer le bloc durée fixe :
```html
<div style="display:flex;align-items:center;gap:8px;padding:8px 14px;...">
  <span>240 mois</span>
  <span>— Mensualité la plus basse</span>
</div>
<input type="hidden" id="miniMonths" value="240">
```

Par un select :
```html
<div class="mini-calc-row mini-calc-dur">
  <label>Durée du financement</label>
  <select id="miniMonthsSel" 
          onchange="document.getElementById('miniMonths').value=this.value; onCapitalSlide()"
          style="width:100%;padding:8px 12px;border:1.5px solid var(--border);border-radius:6px;font-family:var(--fb);font-size:.88rem;color:var(--text);background:#fff;cursor:pointer">
    <option value="60">60 mois (5 ans)</option>
    <option value="120">120 mois (10 ans)</option>
    <option value="180">180 mois (15 ans)</option>
    <option value="240" selected>240 mois (20 ans — mensualité min)</option>
  </select>
</div>
<input type="hidden" id="miniMonths" value="240">
```

Faire de même dans le modal `#prequalModal` (étape 2), en remplaçant le bloc durée fixe par le même select.

---

### CORRECTION 9 — IMPORTANTE (FAQ)
**Étendre la FAQ de 5 à 10 questions**

Après la 5e question existante ("Est-ce que vous offrez une garantie?"), ajouter ces 5 nouvelles questions dans le même format `<details>` :

**Question 6 :** Quelle est la meilleure période pour faire des travaux d'aménagement au Québec ?
> La saison principale va de mai à octobre. Pour les projets de pavé uni, on peut travailler jusqu'en novembre si les températures restent au-dessus de 0°C. Nous planifions selon la météo pour garantir la qualité.

**Question 7 :** Combien de temps à l'avance dois-je planifier mon projet ?
> En haute saison (juin–août), notre calendrier se remplit rapidement. Idéalement, contactez-nous 6 à 8 semaines à l'avance pour sécuriser une date. Contactez-nous maintenant pour vérifier la disponibilité.

**Question 8 :** Le prix de la soumission peut-il changer après avoir commencé les travaux ?
> Non, si vous ne demandez pas de modifications. Notre soumission est ferme et détaillée. Des changements en cours de travaux peuvent générer des coûts supplémentaires, mais toujours approuvés par écrit avec vous au préalable.

**Question 9 :** Comment entretenir mon pavé uni l'hiver ?
> Évitez les fondants corrosifs comme le sel de table — préférez un abrasif ou du sel de mer. Un scellant appliqué à l'automne protège votre investissement. Nous proposons des services d'entretien annuel.

**Question 10 :** Est-ce que la soumission engage à quelque chose ?
> Non, absolument pas. La soumission est 100% gratuite et sans engagement. Vous n'êtes lié par rien tant que vous n'avez pas signé un contrat formel.

---

### CORRECTION 10 — MINEURE (textes)
**Corriger les erreurs de texte**

1. Remplacer `"Comment ca fonctionne ?"` par `"Comment ça fonctionne ?"`
2. Remplacer `© 2025 Jardin Idéal` par `© 2026 Jardin Idéal`
3. Retirer ou masquer le lien `admin-cour-arriere.html` visible dans le topbar et le footer

---

## CE QU'IL NE FAUT PAS CHANGER

- La politique de confidentialité (section #confidentialite) — le texte légal existant est correct
- Les témoignages Google (Madeleine, Bétina Eustache, Monique Létourneau)
- La checklist entrepreneur (8 questions/réponses)
- La galerie 9 projets avec hotspots
- Les prix dans le tableau (entrée / milieu / haut / prestige)
- La calculatrice d'estimation visuelle (cartes S/M/L/XL)
- Le chatbot Alex
- La sticky bar mobile
- La police, les couleurs, les tokens CSS

---

## RÈGLE ABSOLUE — NE PAS INVENTER

Ne pas ajouter ou modifier :
- Des prix exacts non confirmés
- Des garanties non mentionnées dans le fichier V1
- Des certifications ou licences fictives
- Des statistiques sans source confirmée
- Du texte en anglais dans la page principale

---

## LIVRAISON ATTENDUE

Fichier HTML complet, auto-contenu (CSS et JS inline), qui :
1. Fonctionne localement (sans serveur web)
2. Intègre toutes les corrections listées ci-dessus
3. Ne brise aucune section existante
4. Est nommé : `2026-06-24_COUR_ARRIERE_V2_HTML.html`

Confirmer à la fin quelles corrections ont été appliquées et lesquelles n'ont pas pu l'être.

===FIN===

---

## NOTES POUR DANIEL (avant de passer à Manus)

**Éléments à confirmer avant d'envoyer ce prompt :**
1. **Meta Pixel ID** — récupérer l'ID réel dans Meta Business Suite → Events Manager
2. **Courriel de contact** — confirmer si `info@jardin-ideal.com` reçoit les leads ou si c'est `daniel@groupe-ideal.com`
3. **Garantie piscine** — 5 ans ou 10 ans ? (actuellement incohérent dans la page)
4. **URL Zapier webhook** — avoir l'URL du webhook avant de passer en production

**Éléments que Manus ne peut PAS faire et qui doivent être configurés manuellement :**
- Connexion Zapier (demande accès aux comptes Pipedrive + Zapier)
- ID du Meta Pixel (demande accès à Meta Business Suite)
- URL des réseaux sociaux réels

---

*Prompt prêt à copier — Jardín Ideal AI System · 2026-06-24*
*Référence audit : `07_REPORTES/LANDING_PAGES/ANALISIS_REAL_COUR_ARRIERE_V1.md`*
