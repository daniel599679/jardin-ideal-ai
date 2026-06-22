# CRM — PIPELINE DE VENTAS
**Jardín Ideal | Temporada alta: Abril–Octubre | Objetivo 2026: 7M CAD**

---

## Las 6 Etapas del Pipeline

```
NUEVO → CONTACTADO → CALIFICADO → PROPUESTA ENVIADA → CERRADO GANADO → CERRADO PERDIDO
```

---

### ETAPA 1 — NUEVO
**Definición:** Lead que acaba de entrar al sistema y no ha sido contactado.

**Entra aquí cuando:**
- Completa un formulario de Meta Ads o Google Ads
- Escribe por DM en Instagram/Facebook
- Llama por primera vez
- Es referido por un cliente o conocido

**Sale de aquí cuando:**
- Se hace el primer contacto → pasa a **CONTACTADO**
- Es descartado inmediatamente (zona incorrecta, servicio inexistente) → pasa a **CERRADO PERDIDO**

**Tiempo máximo en esta etapa: 2 horas (horario laboral)**
**Alerta automática: >24h sin contacto = prioridad crítica**

**KPI clave:** Tasa de contacto en <2h

---

### ETAPA 2 — CONTACTADO
**Definición:** Se hizo primer contacto pero aún no se calificó el lead completamente.

**Entra aquí cuando:**
- Se envió el primer mensaje o se hizo la primera llamada

**Sale de aquí cuando:**
- Se obtiene información completa y hay interés real → pasa a **CALIFICADO**
- El cliente no responde después de la secuencia completa de seguimiento → pasa a **LEAD FRÍO** (subcategoría de espera)
- El cliente dice que no está interesado → pasa a **CERRADO PERDIDO**

**Tiempo máximo en esta etapa: 5 días**

**Campos obligatorios a completar antes de avanzar:**
- [ ] Servicio de interés confirmado
- [ ] Dirección del proyecto
- [ ] Presupuesto aproximado
- [ ] Fecha deseada

---

### ETAPA 3 — CALIFICADO
**Definición:** Lead con información completa, interés real y capacidad de compra probable. Visita técnica agendada o en proceso de agendar.

**Entra aquí cuando:**
- Se completó la calificación y el lead cumple los criterios (ver `calificacion_leads.md`)

**Sale de aquí cuando:**
- Se realiza la visita técnica y se prepara propuesta → pasa a **PROPUESTA ENVIADA**
- El cliente se enfría o cancela la visita → vuelve a **CONTACTADO** o pasa a **LEAD FRÍO**

**Tiempo máximo en esta etapa: 7 días**

**Acciones requeridas:**
- [ ] Visita técnica agendada con fecha y hora
- [ ] Responsable de la visita asignado
- [ ] Cliente confirmó la visita (no solo "quedó agendada")

---

### ETAPA 4 — PROPUESTA ENVIADA
**Definición:** Se realizó la visita técnica y se envió la cotización formal al cliente.

**Entra aquí cuando:**
- La propuesta/soumission fue enviada por email o entregada en persona

**Sale de aquí cuando:**
- El cliente acepta → pasa a **CERRADO GANADO**
- El cliente rechaza → pasa a **CERRADO PERDIDO** (registrar razón)
- No hay respuesta → aplicar secuencia de seguimiento de propuesta

**Tiempo máximo en esta etapa: 14 días**
**Alerta: >7 días sin respuesta = acción de seguimiento obligatoria**

**Campos a registrar al entrar:**
- [ ] Fecha de envío de la propuesta
- [ ] Monto de la propuesta
- [ ] Fecha límite de validez de la propuesta
- [ ] Canal de envío (email / entrega personal / WhatsApp)

---

### ETAPA 5 — CERRADO GANADO ✅
**Definición:** Cliente confirmó el proyecto. Contrato firmado o depósito recibido.

**Entra aquí cuando:**
- Cliente dice "sí" y hay confirmación formal (escrita, pago, o firma)

**Acciones al cerrar ganado:**
- [ ] Registrar monto final del proyecto
- [ ] Crear ficha de proyecto en Operaciones
- [ ] Notificar al equipo de obra
- [ ] Confirmar fecha de inicio con el cliente
- [ ] Programar seguimiento post-entrega (para solicitar reseña)

**No se mueve de aquí.** Es el destino positivo final.

---

### ETAPA 6 — CERRADO PERDIDO ❌
**Definición:** Lead que no va a convertirse en cliente en esta oportunidad.

**Entra aquí cuando:**
- Cliente rechaza la propuesta
- Cliente no responde después de la secuencia completa
- Lead no calificado (zona, servicio, presupuesto)

**Obligatorio al cerrar perdido — registrar razón:**
- Precio muy alto
- Eligió a un competidor
- Proyecto cancelado / pospuesto
- No calificado (zona / servicio / presupuesto)
- Sin respuesta / no localizable
- Otro (especificar)

**¿Se puede recuperar?**
- Razón "proyecto pospuesto" → programar reactivación en 60–90 días
- Razón "precio" → evaluar si hay versión reducida del proyecto posible
- Resto → archivar

---

## KPIs del Pipeline

| Métrica | Objetivo | Alerta si... |
|---|---|---|
| Tiempo primer contacto | <2 horas | >24 horas |
| Tasa contacto → calificado | >60% | <40% |
| Tasa calificado → propuesta | >80% | <60% |
| Tasa propuesta → ganado | >50% | <35% |
| Tiempo promedio cierre | <21 días | >35 días |
| Leads sin movimiento >7 días | 0 | >3 |

---

## Reglas del Pipeline

1. **Todo lead tiene siempre una fecha de próxima acción** — si no hay próxima acción, el lead está abandonado.
2. **Ningún lead puede estar en NUEVO más de 24 horas** — es la regla más importante.
3. **Cada cambio de etapa se documenta** — con fecha y nota mínima de qué pasó.
4. **CERRADO PERDIDO siempre tiene razón registrada** — sin razón, no se cierra.
5. **Propuestas vencidas (>14 días) se revisan** — no quedan abiertas indefinidamente.

---

## Vista semanal del pipeline (revisar cada lunes)

```
NUEVO:             ___ leads | Sin contactar >24h: ___
CONTACTADO:        ___ leads | Sin avance >5 días: ___
CALIFICADO:        ___ leads | Sin visita agendada: ___
PROPUESTA ENV.:    ___ leads | Sin respuesta >7 días: ___
CERRADO GANADO:    ___ (semana) | Monto total: ___ CAD
CERRADO PERDIDO:   ___ (semana) | Razón más común: ___

TASA DE CIERRE SEMANA: ___%
VALOR PIPELINE ACTIVO: ___ CAD
```
