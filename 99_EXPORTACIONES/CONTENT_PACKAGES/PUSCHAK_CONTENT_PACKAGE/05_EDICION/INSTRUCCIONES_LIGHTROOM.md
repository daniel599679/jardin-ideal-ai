# INSTRUCCIONES LIGHTROOM — PROJET PUSCHAK
**Orden de retouche por prioridad de publicación**

---

## FOTO 1 — HERO (PRIORIDAD MÁXIMA)
**Archivo:** `01_HERO_apres_travaux.jpg`
**Tiempo estimado:** 45–60 minutos (incluye Photoshop)

### Lightroom — Ajustes globales
```
Exposición        : +0.30
Hautes lumières   : -40
Ombres            : +35
Blancs            : -15
Noirs             : +10
Contraste         : +12
Clarté            : +8
Texture           : +10
Vibrance          : +15
Saturation        : +5
Température       : 5600K
Teinte            : 0
```

### Lightroom — HSL (Couleur par couleur)
```
VERT   Teinte: 0  Saturation: +25  Luminance: +10
BLEU   Teinte: 0  Saturation: +20  Luminance: -10
ROUGE  Teinte: 0  Saturation: -20  Luminance: 0
ORANGE Teinte: 0  Saturation: -15  Luminance: +10
AQUA   Teinte: 0  Saturation: +10  Luminance: 0
```

### Lightroom — Courbe de tons
```
Ombres     : légèrement remonter (+10)
Tons moyens: légère S — milieu stable
Hautes lum.: légèrement baisser (-10)
Résultat   : contraste élégant sans crushing
```

### Photoshop — Retouches obligatoires
```
1. CÂBLES ÉLECTRIQUES (priorité absolue)
   Sélection: Lasso magnétique autour de chaque câble
   Action: Édition → Remplissage → Contenu pris en compte
   Vérifier: que le ciel reconstruit est naturel (nuages cohérents)
   Répéter pour chaque câble individuellement

2. CLIMATISEUR MURAL (gauche, mi-hauteur)
   Sélection: Lasso souple, sélectionner l'unité + légère marge
   Action: Tampon de duplication — cloner la texture du mur adjacent
   Conserver: l'ombre portée légère du mur (ne pas la retirer)

3. REMPLACEMENT DU CIEL (recommandé)
   Menu: Édition → Remplacement du ciel
   Style: Ciel bleu d'été avec cumulus légers
   Échelle: Ajuster pour que la ligne d'horizon soit naturelle
   Luminosité: Adapter pour que le ciel n'écrase pas le premier plan

4. VÉRIFICATION FINALE
   Zoom à 100% — vérifier qu'il n'y a pas d'artefacts de retouche
   Comparer avec l'original — la retouche doit être invisible
```

---

## FOTO 2 — DÉTAIL PAVÉ (20 minutes)
**Archivo:** `02_DETAIL_PAVE_apres_travaux-5.jpg`

### Lightroom
```
Exposición        : +0.20
Ombres            : +40
Hautes lumières   : -20
Clarté            : +15
Texture           : +20
VERT HSL          Saturation: +30  Luminance: +15
BLEU HSL          Saturation: +15
Courbe            : S légère (ombres +8, lumières -8)
```

### Photoshop (opcional — 5 minutos)
```
Dodge Tool (outil éclaircisseur) — plume 50%, exposition 10%
Passer sur les joints entre les dalles claires pour les faire ressortir
Ne pas toucher les dalles elles-mêmes — seulement les joints
```

---

## FOTO 3 — CLÔTURE PREMIUM (20 minutes)
**Archivo:** `03_CLOTURE_PREMIUM_apres_travaux-7.jpg`

### Lightroom
```
Exposición        : +0.15
Hautes lumières   : -30
Ombres            : +25
Clarté            : +20
Texture           : +25
VERT HSL          Saturation: +25  Luminance: +10
ORANGE HSL        Saturation: -20
BLEU HSL          Saturation: +15  Luminance: -10
Vignette          : -15  Point médian: 50
```

### Photoshop (10 minutos)
```
Dodge Tool — plume 30%, exposition 15%
Passer doucement sur les reflets chromés des poteaux métalliques
Résultat: les poteaux "brillent" légèrement — effet premium
```

---

## FOTO 4 — TERRASSE (40 minutes — retouche extensive)
**Archivo:** `04_TERRASSE_apres_travaux-4.jpg`

### Lightroom
```
Exposición        : +0.30
Débrumage         : +40  ← PRIORITÉ — corrige le haze optique
Hautes lumières   : -35
Ombres            : +30
Clarté            : +15
Contraste         : +10
VERT HSL          Saturation: +20  Luminance: +10
ORANGE/ROUGE HSL  Saturation: -25
```

### Photoshop
```
Option A (rapide):
  Flou de champ (Filtre → Flou → Flou de champ)
  Sélectionner la zone de fond (clôture en bois + zone arrière)
  Appliquer un flou de 8–12px sur le fond uniquement
  Résultat: le fond recule visuellement

Option B (premium — 20 min supplémentaires):
  Sélectionner le fond via Sélection rapide
  Générative Fill (Adobe Firefly): "dense green garden privacy hedge summer bokeh"
  Valider le résultat le plus naturel
  Masquer les bords avec une brosse souple
```

---

## FOTO 5 — COULOIR (25 minutes)
**Archivo:** `05_COULOIR_apres_travaux-2.jpg`

### Lightroom
```
Exposición        : +0.40
Ombres            : +45
Hautes lumières   : -25
VERT HSL          Saturation: +30
Clarté            : +10
Crop              : Remonter le cadre en haut pour éliminer les câbles
                    (si possible sans perdre trop de composition)
```

### Photoshop
```
Si les câbles ne peuvent pas être éliminés par crop:
  Content-Aware Fill sur les câbles (identique à la Photo HERO)
Éliminer le parasol rouge visible au fond si accessible:
  Clone Stamp avec texture de clôture adjacente
```

---

## FOTO 6 — PROCESSUS EXCAVATRICE (15 minutes)
**Archivo:** `06_PROCESSUS_excavatrice.jpg`

### Lightroom — Retouche minimale
```
Exposición        : +0.20
Contraste         : +15
Clarté            : +20
VERT HSL          Saturation: +15
JAUNE HSL         Saturation: +10  (la machine jaune)
Courbe            : S légère — renforcer le dramatisme industriel
```

### Photoshop
```
Burn Tool (outil assombrisseur) légèrement sur le ciel surexposé
Pas d'autre retouche — l'image est déjà forte telle quelle
```

---

## FOTO 7 — AVANT NARRATIF (10 minutes)
**Archivo:** `07_AVANT_narratif.jpg`
**Tratamiento deliberadamente sobrio**

### Lightroom
```
Exposición        : -0.30  ← ASSOMBRIR DÉLIBÉRÉMENT
Saturation        : -15    ← DÉSATURER DÉLIBÉRÉMENT
Clarté            : +5
Contraste         : +8
Température       : -100K  ← Légèrement plus froid (ambiance "avant")
NOTE: L'avant doit paraître moins désirable que l'après.
      Ne pas embellir. Le contraste EST le message.
```

---

## ORDRE D'EXÉCUTION ET TEMPS TOTAL

```
AUJOURD'HUI  (2–3h de travail)
  1. HERO      → 60 min  → Livrer META_4x5 + META_1x1
  2. DÉTAIL    → 20 min  → Livrer META_4x5
  3. CLÔTURE   → 20 min  → Livrer META_4x5

DEMAIN MATIN  (1.5h de travail)
  4. PROCESSUS → 15 min
  5. AVANT     → 10 min
  6. Assembler carrusel 5 slides

DEMAIN APM    (1h de travail)
  7. TERRASSE  → 40 min
  8. COULOIR   → 25 min

TEMPS TOTAL : ~4.5–5 heures pour 7 photos premium livrées
```

---

## NOMENCLATURE DES FICHIERS LIVRÉS

```
PUSCHAK_01_HERO_META_4x5.jpg          → 1080 x 1350 px
PUSCHAK_01_HERO_META_1x1.jpg          → 1080 x 1080 px
PUSCHAK_01_HERO_STORY_9x16.jpg        → 1080 x 1920 px
PUSCHAK_02_DETAIL_META_4x5.jpg        → 1080 x 1350 px
PUSCHAK_03_CLOTURE_META_4x5.jpg       → 1080 x 1350 px
PUSCHAK_04_TERRASSE_META_4x5.jpg      → 1080 x 1350 px
PUSCHAK_05_COULOIR_META_4x5.jpg       → 1080 x 1350 px
PUSCHAK_06_PROCESSUS_META_4x5.jpg     → 1080 x 1350 px
PUSCHAK_07_AVANT_META_4x5.jpg         → 1080 x 1350 px
```
