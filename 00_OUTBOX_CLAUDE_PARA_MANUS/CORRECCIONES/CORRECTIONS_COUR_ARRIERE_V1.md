# LISTA DE CORRECCIONES — Cour Arrière V1 → V2
**Basado en:** Auditoría real del archivo HTML local
**Fecha:** 2026-06-24
**Destino:** Pegar en Manus para generar `2026-06-24_COUR_ARRIERE_V2_HTML.html`

---

## 🔴 CORRECCIONES CRÍTICAS (bloquean publicación)

### C1 — Checkbox de consentement Loi 25 en formulario soumission
**Problema:** El formulario tiene solo texto "vous acceptez notre politique de confidentialité" — NO hay checkbox que el usuario marque activamente. Esto viola la Loi 25 Quebec.

**Solución:** Agregar este bloque ANTES del botón de envío en `#coordsForm`:
```html
<div style="margin:16px 0;padding:14px 16px;background:rgba(0,142,63,.06);border-radius:8px;border:1px solid rgba(0,142,63,.2)">
  <label style="display:flex;align-items:flex-start;gap:12px;cursor:pointer;font-size:.85rem;color:var(--text)">
    <input type="checkbox" id="consentement" name="consentement" required
           style="margin-top:3px;accent-color:var(--green);width:18px;height:18px;cursor:pointer;flex-shrink:0">
    <span>J'accepte que Jardin Idéal collecte et utilise mes renseignements personnels pour traiter ma demande de soumission gratuite, conformément à sa <a href="#confidentialite" style="color:var(--green)">politique de confidentialité</a>. *</span>
  </label>
</div>
```
Y en la validación JS de `submitForm()`, verificar que esté marcado antes de enviar.

---

### C2 — Checkbox de consentement en modal de financement
**Problema:** El modal de pré-qualification etapa 3 tiene solo texto referenciando la política — sin checkbox activo.

**Solución:** Agregar en `#pqStep3`, ANTES del botón "Envoyer ma demande":
```html
<div style="margin:16px 0;padding:12px 14px;background:rgba(0,142,63,.06);border-radius:8px;border:1px solid rgba(0,142,63,.2)">
  <label style="display:flex;align-items:flex-start;gap:10px;cursor:pointer;font-size:.82rem;color:var(--text)">
    <input type="checkbox" id="consentementFin" required
           style="margin-top:2px;accent-color:var(--green);width:16px;height:16px;cursor:pointer;flex-shrink:0">
    <span>J'autorise Jardin Idéal à utiliser mes renseignements pour préparer mon dossier de financement et me contacter. <a href="#confidentialite" style="color:var(--green)">Politique de confidentialité</a>. *</span>
  </label>
</div>
```

---

### C3 — Reemplazar placeholder del Meta Pixel
**Problema:** Línea 878 del HTML: `fbq('init', 'TU_PIXEL_ID');` — no hay tracking real.

**Solución:** Reemplazar `TU_PIXEL_ID` con el ID real del Meta Pixel de Jardín Ideal.
> **NOTA para Daniel:** Buscar el ID real en Meta Business Suite → Events Manager → Pixels. El ID tiene formato numérico de 15-16 dígitos.

---

### C4 — Eliminar "Pré-approuvé" automático en confirmación financement
**Problema:** Al enviar el modal de financement, el mensaje dice "✅ Pré-approuvé" sin haber evaluado nada. Esto puede crear expectativas incorrectas y problemas legales.

**Solución:** Reemplazar el badge "Pré-approuvé" por:
```html
<div style="display:inline-block;background:#e8f5e9;border:2px solid var(--green);border-radius:100px;padding:6px 20px;margin-bottom:14px">
  <span style="font-family:var(--fh);font-weight:900;font-size:.85rem;color:#2e7d32;text-transform:uppercase;letter-spacing:.08em">✅ Demande reçue</span>
</div>
```
Y cambiar el texto de:
> *"Votre demande de financement est pré-approuvée"*
Por:
> *"Votre demande a bien été reçue. Un conseiller Jardin Idéal analysera votre dossier et vous contactera sous 24h avec les meilleures options disponibles."*

---

### C5 — Conectar formulaires a endpoint real (Zapier webhook)
**Problema:** Las funciones `submitForm()` y `pqSubmit()` probablemente solo muestran una confirmación sin enviar datos.

**Solución:** En `submitForm()`, agregar:
```javascript
// Validar consentement antes de enviar
if (!document.getElementById('consentement').checked) {
  alert('Veuillez accepter notre politique de confidentialité pour continuer.');
  return;
}

// Recopilar todos los datos
const payload = {
  prenom: document.getElementById('fPrenom').value,
  nom: document.getElementById('fNom').value,
  telephone: document.getElementById('fTel').value,
  email: document.getElementById('fEmail').value,
  ville: document.getElementById('fVille').value,
  code_postal: document.getElementById('fPostal').value,
  notes: document.getElementById('fNotes').value,
  utm_source: document.getElementById('hUtmSource').value,
  utm_medium: document.getElementById('hUtmMedium').value,
  utm_campaign: document.getElementById('hUtmCampaign').value,
  source_page: 'lp-cour-arriere-v1',
  // Agregar respuestas del stepper
  type_projet: answers?.typeProjet || '',
  superficie: answers?.superficie || '',
  budget: answers?.budget || '',
  urgence: answers?.urgence || ''
};

// Enviar a Zapier webhook
await fetch('URL_DEL_WEBHOOK_ZAPIER', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify(payload)
});
```
> **NOTA:** `URL_DEL_WEBHOOK_ZAPIER` debe reemplazarse con la URL real del Zap de Pipedrive.

---

## 🟠 CORRECCIONES ALTAS (impactan calidad de leads)

### C6 — Agregar campo "Adresse du projet" en coordsForm
**Problema:** El formulario de contacto no tiene campo de dirección del proyecto — sin esto Pipedrive no puede asignar zona geográfica.

**Solución:** Agregar después del campo "Ville":
```html
<div class="form-row single">
  <div class="form-group">
    <label>Adresse du projet</label>
    <input type="text" id="fAdresse" name="adresse_projet" 
           autocomplete="street-address" placeholder="Ex: 123 rue Saint-Denis, Montréal">
  </div>
</div>
```

---

### C7 — Agregar campo "Comment nous avez-vous connu?" en coordsForm
**Problema:** Sin campo de fuente, Pipedrive no puede reportar atribución de lead más allá de UTM.

**Solución:** Agregar después del upload zone:
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

### C8 — Resolver inconsistencia de datos en hero
**Problema:** Hero dice "⭐ 4.9/5 sur Google · +200 projets réalisés" pero el trust pill dice "1 500+ projets réalisés".

**Solución:** Unificar a:
```
⭐ 4.9/5 sur Google · 1 500+ projets réalisés · 15 ans d'expérience
```
Eliminar la línea inconsistente y mantener solo los trust pills.

---

### C9 — Resolver inconsistencia garantie piscine
**Problema:** En la galería (hotspot piscine): "garantie 10 ans structure". En checklist y trust pills: "garantie 5 ans". Solo una puede ser verdad.

**Solución:** Confirmar con Daniel cuál es la garantía real. Mientras tanto, usar "5 ans" (dato más conservador, confirmado en checklist) y actualizar el hotspot:
```
garantie 5 ans structure
```

---

### C10 — Duración financement: permitir selección
**Problema:** Mini-calc fijado a 240 meses como único valor.

**Solución:** Reemplazar el display fijo por un select:
```html
<div class="mini-calc-row mini-calc-dur">
  <label>Durée</label>
  <select id="miniMonthsSel" onchange="document.getElementById('miniMonths').value=this.value; onCapitalSlide()">
    <option value="60">60 mois (5 ans)</option>
    <option value="120">120 mois (10 ans)</option>
    <option value="180">180 mois (15 ans)</option>
    <option value="240" selected>240 mois (20 ans — mensualité min)</option>
  </select>
</div>
```

---

### C11 — Corregir courriel de contacto
**Problema:** Topbar y footer muestran `info@jardin-ideal.com` — el courriel operacional es `daniel@groupe-ideal.com`.

**Solución:** 
- Si `info@jardin-ideal.com` existe y está redirigido: OK, mantener para el público
- Si no existe o no funciona: reemplazar por el correcto
> **Confirmar con Daniel** cuál courriel recibe los leads de la landing

---

### C12 — Expandir FAQ de 5 a 10 preguntas
**Problema:** Solo 5 preguntas — insuficiente para SEO y para resolver objeciones.

**Agregar estas 5 preguntas:**
```html
<details style="background:var(--cream);border:1px solid var(--border);border-radius:var(--r);padding:16px 24px;cursor:pointer">
  <summary style="font-family:var(--fh);font-weight:700;color:var(--dark);font-size:1.05rem;list-style:none;display:flex;justify-content:space-between;align-items:center">
    Quelle est la meilleure période pour faire des travaux d'aménagement au Québec ?
    <span style="color:var(--green);font-size:1.4rem;font-weight:300;flex-shrink:0;margin-left:12px">+</span>
  </summary>
  <p style="margin-top:12px;color:var(--text2);font-size:0.95rem;line-height:1.7">La saison principale va de mai à octobre. Pour les projets de pavé uni, on peut travailler jusqu'en novembre si les températures restent au-dessus de 0°C. Nous planifions selon la météo pour garantir la qualité.</p>
</details>

<details style="background:var(--cream);border:1px solid var(--border);border-radius:var(--r);padding:16px 24px;cursor:pointer">
  <summary style="font-family:var(--fh);font-weight:700;color:var(--dark);font-size:1.05rem;list-style:none;display:flex;justify-content:space-between;align-items:center">
    Combien de temps à l'avance dois-je planifier mon projet ?
    <span style="color:var(--green);font-size:1.4rem;font-weight:300;flex-shrink:0;margin-left:12px">+</span>
  </summary>
  <p style="margin-top:12px;color:var(--text2);font-size:0.95rem;line-height:1.7">En haute saison (juin–août), notre calendrier se remplit rapidement. Idéalement, contactez-nous 6 à 8 semaines à l'avance pour sécuriser une date. Contactez-nous maintenant pour vérifier la disponibilité.</p>
</details>

<details style="background:var(--cream);border:1px solid var(--border);border-radius:var(--r);padding:16px 24px;cursor:pointer">
  <summary style="font-family:var(--fh);font-weight:700;color:var(--dark);font-size:1.05rem;list-style:none;display:flex;justify-content:space-between;align-items:center">
    Le prix de la soumission peut-il changer après avoir commencé les travaux ?
    <span style="color:var(--green);font-size:1.4rem;font-weight:300;flex-shrink:0;margin-left:12px">+</span>
  </summary>
  <p style="margin-top:12px;color:var(--text2);font-size:0.95rem;line-height:1.7">Non, si vous ne demandez pas de modifications. Notre soumission est ferme et détaillée. Des changements en cours de travaux peuvent générer des coûts supplémentaires, mais toujours approuvés par écrit avec vous au préalable.</p>
</details>

<details style="background:var(--cream);border:1px solid var(--border);border-radius:var(--r);padding:16px 24px;cursor:pointer">
  <summary style="font-family:var(--fh);font-weight:700;color:var(--dark);font-size:1.05rem;list-style:none;display:flex;justify-content:space-between;align-items:center">
    Comment entretenir mon pavé uni l'hiver ?
    <span style="color:var(--green);font-size:1.4rem;font-weight:300;flex-shrink:0;margin-left:12px">+</span>
  </summary>
  <p style="margin-top:12px;color:var(--text2);font-size:0.95rem;line-height:1.7">Évitez les fondants corrosifs comme le sel de table — préférez un abrasif ou du sel de mer. Un scellant appliqué à l'automne protège votre investissement. Nous proposons des services d'entretien annuel.</p>
</details>

<details style="background:var(--cream);border:1px solid var(--border);border-radius:var(--r);padding:16px 24px;cursor:pointer">
  <summary style="font-family:var(--fh);font-weight:700;color:var(--dark);font-size:1.05rem;list-style:none;display:flex;justify-content:space-between;align-items:center">
    Est-ce que la soumission engage à quelque chose ?
    <span style="color:var(--green);font-size:1.4rem;font-weight:300;flex-shrink:0;margin-left:12px">+</span>
  </summary>
  <p style="margin-top:12px;color:var(--text2);font-size:0.95rem;line-height:1.7">Non, absolument pas. La soumission est 100% gratuite et sans engagement. Vous n'êtes lié par rien tant que vous n'avez pas signé un contrat formel.</p>
</details>
```

---

## 🟡 MEJORAS (optimización)

### M1 — Agregar barre de confiance post-hero
```html
<div style="background:#fff;border-bottom:1px solid var(--border);padding:16px 0">
  <div class="container">
    <div style="display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:32px">
      <div style="display:flex;align-items:center;gap:10px;font-family:var(--fh);font-size:.82rem;font-weight:700;color:var(--dark)">
        <span style="font-size:1.4rem">⭐</span> 4.9/5 Google
      </div>
      <div style="display:flex;align-items:center;gap:10px;font-family:var(--fh);font-size:.82rem;font-weight:700;color:var(--dark)">
        <span style="font-size:1.4rem">🏗️</span> RBQ #5773-1983-01
      </div>
      <div style="display:flex;align-items:center;gap:10px;font-family:var(--fh);font-size:.82rem;font-weight:700;color:var(--dark)">
        <span style="font-size:1.4rem">🛡️</span> Assurance 2M$
      </div>
      <div style="display:flex;align-items:center;gap:10px;font-family:var(--fh);font-size:.82rem;font-weight:700;color:var(--dark)">
        <span style="font-size:1.4rem">✅</span> Garantie 5 ans
      </div>
      <div style="display:flex;align-items:center;gap:10px;font-family:var(--fh);font-size:.82rem;font-weight:700;color:var(--dark)">
        <span style="font-size:1.4rem">🏆</span> 1 500+ projets
      </div>
    </div>
  </div>
</div>
```

### M2 — Corregir texto
- Línea del mini-calc: `"Comment ca fonctionne ?"` → `"Comment ça fonctionne ?"`
- Footer copyright: `© 2025` → `© 2026`
- Verificar que los links de redes sociales apunten a las páginas reales

### M3 — Ocultar link admin en producción
Agregar `style="display:none"` o `<!-- -->` a:
```html
<a href="admin-cour-arriere.html" style="opacity:.5;font-size:.7rem">Admin</a>
```

---

## CHECKLIST DE IMPLEMENTACIÓN PARA MANUS

```
CRÍTICO (antes de publicar):
[ ] C1 — Checkbox consentement en formulario soumission
[ ] C2 — Checkbox consentement en modal financement
[ ] C3 — ID real del Meta Pixel (pedir a Daniel)
[ ] C4 — "Demande reçue" en lugar de "Pré-approuvé"
[ ] C5 — submitForm() conectado a Zapier webhook

ALTO (misma iteración si es posible):
[ ] C6 — Campo adresse du projet
[ ] C7 — Campo source/comment nous avez-vous connu
[ ] C8 — Unificar datos hero ("+200" vs "1 500+")
[ ] C9 — Garantie piscine: confirmar 5 ans o 10 ans
[ ] C10 — Selector de duración en mini-calc
[ ] C11 — Courriel correcto (confirmar con Daniel)
[ ] C12 — 10 preguntas en FAQ (agregar 5 nuevas)

MEJORAS (V3 si no cabe en V2):
[ ] M1 — Barre de confiance post-hero
[ ] M2 — Corregir textos (ça, copyright 2026)
[ ] M3 — Ocultar link admin
```

---

*Correcciones para V2 — Jardín Ideal AI System · 2026-06-24*
