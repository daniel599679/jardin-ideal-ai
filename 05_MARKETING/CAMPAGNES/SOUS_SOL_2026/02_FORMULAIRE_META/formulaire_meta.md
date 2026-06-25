# 02 — FORMULAIRE META · SOUS-SOL 2026
**Type :** Facebook Lead Ads — Formulaire natif  
**Objectif :** Qualification rapide du lead sous-sol + collecte infos essentielles  
**Langue :** Français québécois  

---

## CONFIGURATION DU FORMULAIRE

**Type recommandé :** Intention élevée  
*(Les projets de sous-sol sont des engagements financiers importants — mieux vaut avoir des leads un peu plus qualifiés que beaucoup de leads froids.)*

---

## TEXTE D'INTRODUCTION

**Titre :**
> Transformez votre sous-sol — Obtenez une évaluation gratuite

**Description :**
> Vous avez un sous-sol non aménagé ou à rénover ? Jardín Ideal s'occupe de la transformation complète : plancher, plafond, pot-lights, escalier, chauffage et isolation. Remplissez ce formulaire pour planifier votre évaluation gratuite à domicile.

---

## QUESTIONS DU FORMULAIRE

### Champs pré-remplis automatiquement (Meta)
- Prénom
- Nom de famille
- Adresse courriel
- Numéro de téléphone

---

### Questions personnalisées

**Question 1 — Type de bâtiment**
> Quel type de bâtiment souhaitez-vous rénover ?
- 🔘 Duplex (2 logements)
- 🔘 Triplex (3 logements)
- 🔘 Quadruplex ou plus
- 🔘 Maison unifamiliale
- 🔘 Autre

**Question 2 — État actuel du sous-sol**
> Comment décririez-vous l'état actuel de votre sous-sol ?
- 🔘 Non aménagé (béton apparent, structures exposées)
- 🔘 Partiellement aménagé (quelques travaux déjà faits)
- 🔘 Aménagé mais à rénover (vieux, désuet)
- 🔘 Je ne suis pas certain

**Question 3 — Surface approximative**
> Quelle est la superficie approximative de votre sous-sol ?
- 🔘 Moins de 400 pi²
- 🔘 Entre 400 et 700 pi²
- 🔘 Entre 700 et 1 000 pi²
- 🔘 Plus de 1 000 pi²
- 🔘 Je ne sais pas

**Question 4 — Secteur géographique**
> Dans quel secteur est situé votre propriété ?
- 🔘 Montréal-Nord
- 🔘 Anjou
- 🔘 Saint-Léonard
- 🔘 Montréal-Est
- 🔘 Laval
- 🔘 Autre secteur de Montréal

**Question 5 — Stade du projet**
> Où en êtes-vous dans la planification de votre projet ?
- 🔘 J'explore les possibilités
- 🔘 J'ai un projet précis et je cherche une soumission
- 🔘 Je suis prêt à commencer dans les 30–60 prochains jours

**Question 6 — Budget approximatif**
> Avez-vous une idée du budget que vous souhaitez allouer ?
- 🔘 Moins de 15 000 $
- 🔘 Entre 15 000 $ et 30 000 $
- 🔘 Entre 30 000 $ et 60 000 $
- 🔘 Plus de 60 000 $
- 🔘 Je ne sais pas encore

---

## MESSAGE DE CONFIRMATION (carte de remerciement)

**Titre :**
> Merci — votre demande a bien été reçue !

**Texte :**
> Un membre de l'équipe Jardín Ideal vous contactera dans les 24 heures pour planifier votre évaluation gratuite à domicile.
>
> Nous sommes impatients de voir votre espace et de vous présenter les possibilités.
>
> Pour toute question urgente : [NUMERO_TELEPHONE]

**Bouton CTA :**
> Visitez notre site → [LIEN_SITE]

---

## MESSAGE AUTOMATIQUE POST-FORMULAIRE (WhatsApp / SMS)

> Bonjour [Prénom], merci pour votre intérêt envers Jardín Ideal !
>
> Nous avons bien reçu votre demande pour un projet de sous-sol. Notre équipe vous contactera bientôt pour planifier une visite gratuite à domicile et discuter des possibilités pour votre espace.
>
> On a hâte de voir ça !
> L'équipe Jardín Ideal

---

## CONNEXIONS TECHNIQUES REQUISES

| Système | Action | Responsable |
|---------|--------|-------------|
| Zapier | Connecter formulaire à Pipedrive | Daniel |
| Pipedrive | Pipeline : "Sous-Sol 2026" | Automatique via Zapier |
| Pipedrive | Étiquettes : source=meta, service=sous_sol, campagne=sous_sol_2026 | Automatique |
| Messagerie | Message automatique SMS/WhatsApp | Zapier |
| Pipedrive | Tâche vendeur "Appeler dans 1h" | Automatique via Zapier |

---

## LEAD SCORING — SOUS-SOL

| Critère | Points |
|---------|--------|
| Triplex ou plus | +25 |
| Sous-sol non aménagé (potentiel maximum) | +20 |
| Projet précis / prêt dans 30–60 jours | +20 |
| Surface > 700 pi² | +15 |
| Budget > 30 000 $ | +15 |
| Zone prioritaire (MTL-Nord, Anjou, St-Léonard) | +10 |
| Budget 15 000–30 000 $ | +5 |
| Budget inconnu | 0 |
| Budget < 15 000 $ | -20 |
| Surface < 400 pi² | -10 |
| Hors zone prioritaire | -5 |

**Score ≥ 60 → Lead très chaud → Appeler dans l'heure**  
**Score 35–59 → Lead qualifié → Appeler dans les 4h**  
**Score 20–34 → Lead tiède → Séquence courriel + appel J+1**  
**Score < 20 → Lead froid → Séquence courriel automatique uniquement**
