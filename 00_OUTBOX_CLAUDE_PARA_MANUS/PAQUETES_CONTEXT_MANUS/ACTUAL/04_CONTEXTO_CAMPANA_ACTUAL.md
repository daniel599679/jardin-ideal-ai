# CONTEXTO CAMPAÑA ACTUAL — Jardín Ideal
**Paquete:** MANUS_CONTEXT_PACK · Documento 04/04
**Versión:** 1.0 · **Última actualización:** 2026-06-24
**Uso:** Contexto de negocio para que Manus entienda prioridades actuales

---

## ESTADO GENERAL DE CAMPAÑAS (2026-06-24)

| Canal | Campaña | Estado | Acción requerida |
|-------|---------|--------|-----------------|
| Meta Ads | Cour arrière | ✅ ACTIVA | Subir budget a $55/día |
| Meta Ads | Cour avant | ⚠️ PAUSAR | Prioridad baja — recursos a cour arrière |
| Meta Ads | Baños (banos) | ⚠️ PAUSAR | Prioridad baja |
| Google Ads | General | Estado desconocido | Verificar con Daniel |
| Landing page | Cour arrière V1 | 🔴 NO publicada | En corrección → V2 |

---

## LANDING PAGE EN DESARROLLO

### Cour Arrière V2
- **Origen:** V1 generada en Manus (cour-arrière.html)
- **Auditoría:** Realizada 2026-06-24 — Score: 68/100
- **Problema crítico:** 5 blockers legales/técnicos
- **Estado actual:** En proceso de corrección → V2
- **Archivo de correcciones:** `00_OUTBOX_CLAUDE_PARA_MANUS/CORRECCIONES/CORRECTIONS_COUR_ARRIERE_V1.md`
- **Prompt para V2:** `00_OUTBOX_CLAUDE_PARA_MANUS/PROMPTS_MANUS/PROMPT_CORRECTION_COUR_ARRIERE_V1_SAFE.md`

**Críticos que bloquean publicación:**
1. No hay checkbox Loi 25 en formulario (legal compliance)
2. Meta Pixel ID es placeholder `TU_PIXEL_ID` (sin tracking real)
3. "Pré-approuvé" automático en financement (engañoso)
4. `submitForm()` no conecta a Zapier (leads perdidos)
5. `submitForm()` no conecta a Pipedrive (leads perdidos)

**Pendientes de Daniel para desbloquear:**
- Meta Pixel ID real → Meta Business Suite → Events Manager → Pixels
- Zapier webhook URL → configurar Zap y obtener URL

---

## OBJETIVOS DE NEGOCIO 2026

| Objetivo | Detalle |
|---------|---------|
| Revenue objetivo | $7M CAD en 2026 |
| Ticket promedio proyecto | $8,000–$75,000+ |
| Mercado | Grand Montréal: Laval, Rive-Sud, Rive-Nord, Montréal |
| Volumen leads necesario | ~15–25 leads calificados/semana (estimado) |
| Servicios prioritarios | Cour arrière complète, pavé uni, piscine + aménagement |

---

## AUDIENCIA OBJETIVO (personas)

### Persona 1 — Família établie (55% del tráfico)
- Propietarios 35–55 ans, maison avec terrain
- Budget disponible $15,000–$50,000
- Motivación: aumentar valor del inmueble, proyecto sueño
- Zona: Laval, Rive-Sud, Rive-Nord
- Comportamiento: investigan varios meses, comparan 3+ cotizaciones

### Persona 2 — Proyecto urgente (30% del tráfico)
- Propietarios 30–45 ans, recién mudados o vendiendo
- Budget $8,000–$25,000
- Motivación: entrega rápida, estética inmediata
- Zona: Grand Montréal general
- Comportamiento: contactan 1–2 empresas, deciden rápido

### Persona 3 — Investisseur / Premium (15% del tráfico)
- Propietarios 45–65 ans, segunda propiedad o proyecto grande
- Budget $35,000–$100,000+
- Motivación: calidad premium, garantía, empresa confiable
- Zona: Laval, Brossard, Mont-Saint-Hilaire, Lorraine
- Comportamiento: piden referencias, visitan proyectos previos

---

## LANDING PAGES PLANEADAS 2026

| Servicio | LP | Estado |
|---------|-----|--------|
| Cour arrière | cour-arriere.html | 🔄 En corrección (V1→V2) |
| Pavé uni seul | pave-uni.html | ⏳ Pendiente |
| Piscine + aménagement | piscine.html | ⏳ Pendiente |
| Terrasse composite | terrasse.html | ⏳ Pendiente |
| Cour avant | cour-avant.html | ⏳ Pendiente |
| Pergola / Gazebo | pergola.html | ⏳ Pendiente |
| Cuisine extérieure | cuisine-ext.html | ⏳ Pendiente |

**Prioridad de desarrollo:**
1. Cour arrière (V2) — esta semana
2. Pavé uni — siguiente
3. Piscine + aménagement — alta temporada julio

---

## CRM Y AUTOMATIZACIÓN

### Pipeline CRM actual (Pipedrive)
- **Lead nuevos → etapa:** Nouveau Lead
- **Leads calificados → etapa:** Rendez-vous planifié
- **Leads soumission enviada → etapa:** Soumission envoyée
- **Ganados → etapa:** Projet démarré

### Secuencia de emails (Zapier)
- **Envío inmediato:** Confirmación de recepción (email desde info@jardin-ideal.com)
- **+24h si no hay contacto:** Recordatorio de soumission
- **+72h si no hay contacto:** "Vos questions?" email educativo
- **+7 días:** Galería de proyectos similares

### Alertas de leads calificados
- Notificación SMS a Daniel: leads PRE-A (score ≥75)
- Notificación email: todos los leads nuevos

---

## COMPETIDORES PRINCIPALES (referencia)

| Empresa | Posicionamiento | Diferencial vs Jardin Idéal |
|---------|----------------|----------------------------|
| Paysagistes Montréal (genérico) | Bajo costo | Nosotros: calidad + garantía |
| Pavé Plus | Especialista pavé | Nosotros: servicio integral |
| Les Experts en Aménagement | Haut de gamme | Nosotros: misma calidad, más accesible |

---

## MENSAJES CLAVE PARA COPY DE LP

**H1 recomendado (cour arrière):**
> "Votre cour arrière de rêve au Québec — De la conception à la réalisation"

**Propuesta de valor:**
1. 15+ ans d'expérience · 1 500+ projets réalisés
2. RBQ #5773-1983-01 · Assurance 2 M$
3. Garantie 5 ans sur les travaux de pavé
4. Financement disponible dès 89$/mois

**Urgencia de temporada:**
> "Saison 2026 : places limitées — Réservez votre créneau maintenant"

---

## DATOS QUE FALTAN CONFIRMAR

| Dato | Estado | Acción |
|------|--------|--------|
| Meta Pixel ID | ⏳ PENDIENTE | Daniel → Meta Business Suite |
| Zapier webhook URL | ⏳ PENDIENTE | Daniel → configurar Zap |
| Garantías servicios (no pavé) | ⏳ PENDIENTE | Daniel confirmar por servicio |
| Google Ads estado | ⏳ PENDIENTE | Daniel verificar dashboard |
| Budget Meta Ads actual | ⏳ PENDIENTE | Daniel verificar / ajustar |
| Texte légal politique confidentialité | ✅ OK | Ya existe en V1 HTML |
| Courriel oficial | ✅ CONFIRMADO | info@jardin-ideal.com |

---

*Contexto campaña Jardín Ideal — v1.0 · 2026-06-24*
*Revisar y actualizar semanalmente o cuando cambien prioridades de campaña*
