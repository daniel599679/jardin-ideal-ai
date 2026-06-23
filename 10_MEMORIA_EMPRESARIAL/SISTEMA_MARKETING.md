# SISTEMA DE MARKETING — JARDÍN IDEAL
**Versión:** 1.1 | **Fecha:** 2026-06-23 | **Actualización:** Decisiones Alex aprobadas — Fase 2 en sprint
**Objetivo:** Documentar el sistema completo de atracción, captura y calificación de leads.

---

## ARQUITECTURA DEL SISTEMA DE MARKETING

```
TRÁFICO
  ↓
META ADS (Facebook / Instagram)
  ↓
LANDING PAGE + ALEX Fase 1 (guía conversacional)
  ↓
FORMULARIO DE CONTACTO
  ↓ webhook (ZAPIER — Fase 2 en sprint)
LANDING_PRE_SCORE calculado automáticamente (Zap 1)
  ↓
PIPEDRIVE DEAL CREADO AUTOMÁTICAMENTE
  + PRE-SCORE + PRE-Clasificación + Guía de llamada
  ↓
ALERTA A DANIEL (email/WhatsApp — Zap 2)
  PRE-A → <2h | PRE-B → <4h | PRE-C → <24h
  ↓
VENDEDOR LLAMA (modelo humano asistido — aprobado)
  Con: Guía de llamada Alex + datos del formulario
  Score: INTERNAL ONLY — el lead nunca ve el score
  ↓
CALL_QUALIFICATION_SCORE registrado en Pipedrive
  ↓
CLASIFICACIÓN FINAL A/B/C/D
  ↓
LEAD_INTELLIGENCE_REPORT → vendedor
  ↓
VISITA PREPARADA

ARQUITECTURA FUTURA (post Fase 2):
  Alex chat → migrar a Voiceflow
  Fase 3 calificación voz → VAPI
```

---

## 1. CANALES DE CAPTACIÓN ACTIVOS

| Canal | Estado | Tipo de lead | Pre-Score disponible |
|-------|--------|-------------|---------------------|
| Meta Ads (Facebook/Instagram) | ✅ Activo | Lead Form + Mensajes | Sí (datos del formulario) |
| Landing Page Jardín Ideal | 🟡 Prototipo | Formulario + Alex | Sí (Pre-Score Alex) |
| Google (orgánico/ads) | 🔴 Por activar | Formulario web | No aún |
| Referidos (boca a boca) | ✅ Activo | Contacto directo | No (calificación manual) |
| Instagram Orgánico | ✅ Activo | Mensajes directos | No (calificación manual) |

---

## 2. FLUJO DE LEAD — ESTADO ACTUAL

### Por Meta Ads (Lead Form)
```
1. Visitante ve el anuncio → clic en "Obtenir une soumission gratuite"
2. Se abre el formulario de Facebook (pre-llenado con datos del perfil)
3. El lead completa: tipo proyecto + tiempo + presupuesto + contacto
4. Los datos llegan a → [actualmente: manual / Pipedrive pendiente de configurar]
5. El equipo recibe notificación → llama manualmente
6. Calificación manual según ICS → clasificación A/B/C/D
```

### Por Landing Page + Alex
```
1. Visitante llega a la landing page (desde ad o tráfico orgánico)
2. Alex lo recibe → guía → explica servicios
3. El visitante llega al formulario de contacto
4. Completa los 4 campos: tipo proyecto + tiempo + presupuesto + contacto
5. Los datos → [actualmente: manual / sin integración Pipedrive]
6. El equipo recibe notificación → llama manualmente
7. Calificación manual según ICS → clasificación A/B/C/D
```

---

## 3. DATOS CAPTURADOS VS DATOS NECESARIOS

### Lo que captura el formulario actual
| Campo | Para calificar | Limitación |
|-------|---------------|-----------|
| Tipo de proyecto | Factor 5 del ICS | Solo parcial (no especifica magnitud) |
| Tiempo estimado | Factor 2 (urgencia) | Declarativo — puede no ser real |
| Presupuesto estimado | Factor 1 | Declarativo — suele ser más bajo del real |
| Nombre + teléfono + email | Identificación | No califica |

### Lo que falta para calificación completa
| Dato faltante | Factor ICS | Cómo obtenerlo |
|--------------|-----------|----------------|
| Autoridad de decisión | Factor 3 (15 pts) | Llamada de calificación |
| Zona exacta | Factor 4 (10 pts) | Formulario (campo pendiente de agregar) |
| Propietario vs. inquilino | Factor 7 (5 pts) | Llamada o campo adicional |
| Interés real | Factor 6 (10 pts) | Comportamiento previo + llamada |

**Conclusión:** Con el formulario se puede calcular un PRE-SCORE de 0–55 pts.
El SCORE COMPLETO (0–100 pts) requiere la llamada de calificación.

---

## 4. ALEX — ROL EN EL SISTEMA DE MARKETING

**Archivo de referencia completo:** `10_MEMORIA_EMPRESARIAL/AGENTES/ALEX_LANDING_PAGE_CONTEXT.md`

| Fase | Función de Alex | Estado |
|------|----------------|--------|
| Fase 1 — Landing Page Guide | Navegar + explicar servicios + guiar al formulario | 🟡 Prototipo |
| Fase 2 — Form Assistant | Asistir el llenado + calcular pre-score + enviar a Pipedrive | 🔴 Por construir |
| Fase 3 — Call Qualification Agent | Calificación post-formulario + briefing vendedor | 🔴 Futuro |

---

## 5. SISTEMA DE CALIFICACIÓN (ICS) — RESUMEN

**Archivo completo:** `10_MEMORIA_EMPRESARIAL/SISTEMA_CLIENTE_IDEAL.md`
**Motor diario:** `10_MEMORIA_EMPRESARIAL/OPERACIONES_DIARIAS/LEAD_REVIEW_ENGINE.md`

| Clasificación | Score | Acción |
|--------------|-------|--------|
| A — Cliente Premium | 85–100 pts | Llamar en <2h. Visita en <24h. |
| B — Cliente Potencial | 65–84 pts | Llamar en 4h. Visita en 48–72h. |
| C — Seguimiento | 40–64 pts | Mensaje en 24h. Seguimiento en 7 días. |
| D — Descalificar | < 40 pts | Respuesta amable. No visitar. |

**Pre-clasificación desde formulario (antes de la llamada):**

| Pre-Clasificación | Pre-Score | Urgencia de la llamada |
|------------------|-----------|----------------------|
| PRE-A | ≥ 70/55 pts formulario | Llamar HOY — puede ser A o A+ |
| PRE-B | 50–69 pts | Llamar dentro de 4h |
| PRE-C | < 50 pts | Llamar en 24h para confirmar o descartar |

---

## 6. CAMPAÑAS META ADS — PARÁMETROS OPERATIVOS

| Parámetro | Objetivo | Alerta |
|-----------|---------|--------|
| CPL (Costo por Lead) | < $80 CAD | Si > $100 → pausar y revisar |
| CTR (Click-Through Rate) | > 2.5% | Si < 1.5% por 3 días → cambiar creatividades |
| Frecuencia del anuncio | < 3.5 en 7 días | Si > 3.5 → rotar creatividades |
| Presupuesto diario mínimo | $20–30 CAD por campaña | — |
| Presupuesto días clave | Hasta $60 CAD (viernes/miércoles) | — |

**Tipos de campaña activos:**
- Conversión (leads directos) — presupuesto principal
- Remarketing (visitantes que no convirtieron) — presupuesto secundario
- Awareness (zona premium: Westmount, TMR, Laval) — presupuesto bajo

---

## 7. CONTENIDO Y LEAD GENERATION

El contenido orgánico e impulsado por FLOAT V2 Premium alimenta directamente las campañas:

```
PROYECTO COMPLETADO
    ↓
FLOAT V2 PIPELINE (gate ≥90/100)
    ↓
HERO POST + REEL EMOCIONAL + META AD
    ↓
ALCANCE ORGÁNICO + PAID
    ↓
LEADS NUEVOS
    ↓
PRE-SCORE → ICS → CLASIFICACIÓN → VISITA
```

**Referencia FLOAT V2:** `05_MARKETING/FLOAT_V2_PREMIUM/`
**Producción diaria:** `05_MARKETING/PRODUCCION_CONTINUA/DAILY_CONTENT_QUEUE.md`

---

## 8. KPIs DE MARKETING — OBJETIVOS 2026

| KPI | Objetivo semanal | Objetivo mensual |
|-----|-----------------|-----------------|
| Leads nuevos totales | ≥ 15 | ≥ 60 |
| Leads clasificados A | ≥ 3 | ≥ 12 |
| Visitas realizadas | ≥ 8 | ≥ 32 |
| Tasa de cierre (visitas → ventas) | ≥ 25% | — |
| CPL promedio | < $80 CAD | — |
| Contenido publicado | 5 piezas/día | ~100 piezas |

**Dashboard completo:** `10_MEMORIA_EMPRESARIAL/KPIS_EMPRESA.md`
**CEO Dashboard diario:** `10_MEMORIA_EMPRESARIAL/OPERACIONES_DIARIAS/CEO_DASHBOARD_TEMPLATE.md`

---

## 9. BRECHAS ACTUALES — LO QUE FALTA PARA QUE EL SISTEMA SEA COMPLETO

| Brecha | Impacto | Solución | Fase |
|--------|---------|---------|------|
| Formulario no envía a Pipedrive automáticamente | Manual → lento | Zapier + Webhook | Fase 2 |
| Alex no calcula pre-score en tiempo real | Pre-score se hace manualmente | Integración Form + Alex | Fase 2 |
| Sin notificación automática a Daniel | Leads esperan >2h | Zapier → WhatsApp | Fase 2 |
| Sin briefing pre-visita automático | Vendedor llega sin preparar | LEAD_INTELLIGENCE_REPORT auto | Fase 3 |
| Google Ads sin activar | Tráfico limitado a Meta | Configurar campaña Google | P2 |
| Sin seguimiento automático a leads C | Se pierden leads rescatables | Secuencia email/SMS | Fase 3 |
