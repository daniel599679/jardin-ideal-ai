# 02 — FORMULAIRE META · COUR ANGLAISE 2026
**Type :** Facebook Lead Ads — Formulaire natif  
**Objectif :** Qualification rapide du lead + collecte des infos essentielles  
**Langue :** Français québécois  

---

## CONFIGURATION DU FORMULAIRE

### Type de formulaire recommandé
- **Type :** Volume élevé (plus court = plus de leads)  
- **Alternative :** Intention élevée (plus de questions = leads plus qualifiés)  
- **Recommandation Jardín Ideal :** Commencer avec Volume élevé, tester Intention élevée après 50 leads.

---

## TEXTE D'INTRODUCTION DU FORMULAIRE

**Titre :**
> Demandez votre soumission — Cour Anglaise

**Description :**
> Vous avez un projet de cour anglaise à Montréal ? Remplissez ce court formulaire et un membre de l'équipe Jardín Ideal vous contactera dans les 24 heures pour discuter de votre projet.

---

## QUESTIONS DU FORMULAIRE

### Champs pré-remplis automatiquement (Meta)
- Prénom
- Nom de famille
- Adresse courriel
- Numéro de téléphone

---

### Questions personnalisées

**Question 1 — Qualification du projet**
> Quel type de bâtiment souhaitez-vous aménager ?
- 🔘 Duplex (2 logements)
- 🔘 Triplex (3 logements)
- 🔘 Maison unifamiliale
- 🔘 Quadruplex ou plus
- 🔘 Autre

**Question 2 — Secteur géographique**
> Dans quel secteur est situé votre propriété ?
- 🔘 Montréal-Nord
- 🔘 Anjou
- 🔘 Saint-Léonard
- 🔘 Montréal-Est
- 🔘 Laval
- 🔘 Autre secteur de Montréal

**Question 3 — Stade du projet**
> Où en êtes-vous dans votre projet ?
- 🔘 J'explore les options — pas encore décidé
- 🔘 J'ai un projet précis — je cherche une soumission
- 🔘 Je suis prêt à commencer rapidement

**Question 4 — Budget approximatif (optionnel)**
> Avez-vous une idée du budget que vous souhaitez allouer à ce projet ?
- 🔘 Moins de 5 000 $
- 🔘 Entre 5 000 $ et 15 000 $
- 🔘 Entre 15 000 $ et 30 000 $
- 🔘 Plus de 30 000 $
- 🔘 Je ne sais pas encore

**Question 5 — Canal de contact préféré**
> Comment préférez-vous être contacté ?
- 🔘 Par téléphone
- 🔘 Par texto (SMS)
- 🔘 Par courriel

---

## MESSAGE DE CONFIRMATION (après soumission)

**Titre de la carte de remerciement :**
> Merci pour votre demande !

**Texte de la carte :**
> Nous avons bien reçu vos informations. Un membre de l'équipe Jardín Ideal vous contactera dans les 24 heures pour discuter de votre projet de cour anglaise.
>
> Vous pouvez aussi nous joindre directement au : [NUMERO_TELEPHONE]

**Bouton CTA de la carte :**
> Visitez notre site web → [LIEN_SITE]

---

## MESSAGE AUTOMATIQUE POST-FORMULAIRE (WhatsApp / SMS)

> Bonjour [Prénom], merci pour votre intérêt envers Jardín Ideal !
>
> Nous avons bien reçu votre demande pour un projet de cour anglaise. Notre équipe vous contactera bientôt pour planifier une évaluation gratuite sur place.
>
> À très bientôt,
> L'équipe Jardín Ideal

---

## CONNEXIONS TECHNIQUES REQUISES

| Système | Action | Responsable |
|---------|--------|-------------|
| Zapier | Connecter le formulaire à Pipedrive | Daniel |
| Pipedrive | Créer deal dans pipeline "Cour Anglaise 2026" | Automatique via Zapier |
| Pipedrive | Ajouter étiquette source=meta, service=cour_anglaise | Automatique via Zapier |
| WhatsApp/SMS | Envoyer message automatique au lead | Zapier → outil de messagerie |
| Vendeur | Créer tâche "Appeler dans 1h" dans Pipedrive | Automatique via Zapier |

---

## LEAD SCORING — COUR ANGLAISE

| Critère | Points |
|---------|--------|
| Triplex ou plus | +20 |
| Projet précis avec budget | +20 |
| Montréal-Nord / Anjou / Saint-Léonard | +15 |
| Budget > 15 000 $ | +15 |
| Veut être contacté par téléphone | +10 |
| Duplex | +10 |
| Budget inconnu | 0 |
| Hors zone prioritaire | -10 |
| Budget < 5 000 $ | -15 |

**Score ≥ 50 → Lead chaud → Appeler dans l'heure**  
**Score 30–49 → Lead tiède → Appeler dans les 24h**  
**Score < 30 → Lead froid → Séquence courriel automatique**
