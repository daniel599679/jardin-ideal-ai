# START DAY ENGINE
**Motor de arranque diario — Jardín Ideal**
**Versión:** 1.0 | **Activar:** 07:00 AM cada día laborable

---

## INSTRUCCIÓN DE ACTIVACIÓN

Cuando Daniel escriba `ejecutar START_DAY_ENGINE` o `arrancar el día`:

1. Leer los 4 archivos de contexto (en orden)
2. Generar el DAILY_BRIEF con el formato exacto de abajo
3. No preguntar nada — ejecutar y entregar el brief completo

---

## PASO 1 — LEER (en este orden exacto)

```
ARCHIVO 1: 10_MEMORIA_EMPRESARIAL/MEMORIA_GLOBAL.md
  → Extraer: empresa activa, objetivo del mes, sistemas activos

ARCHIVO 2: 10_MEMORIA_EMPRESARIAL/ESTADO_ACTUAL_ECOSISTEMA.md
  → Extraer: qué está completado, qué está en progreso, qué está bloqueado

ARCHIVO 3: 10_MEMORIA_EMPRESARIAL/PROXIMOS_PASOS.md
  → Extraer: P1 del día, P2 de la semana, bloqueos activos

ARCHIVO 4: 10_MEMORIA_EMPRESARIAL/REUNIONES_DIARIAS.md
  → Extraer: agenda de la reunión de 09:00, decisiones pendientes
```

---

## PASO 2 — GENERAR EL DAILY_BRIEF

Usar exactamente este formato. Completar cada sección con datos reales de los 4 archivos leídos. Si un dato no está disponible, escribir `→ Actualizar` en lugar de inventar.

---

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DAILY BRIEF — JARDÍN IDEAL
Fecha: [YYYY-MM-DD] | Día: [Lunes–Domingo]
Generado: 07:00 AM | Próxima revisión: reunión 09:00
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 1. PROYECTOS ACTIVOS

| Proyecto | Cliente | Servicio | Etapa | Fecha entrega | Responsable |
|---------|---------|---------|-------|--------------|-------------|
| [nombre] | [cliente] | [Cour Avant/Pavé-Uni/etc.] | [Inicio/Proceso/Cierre] | [fecha] | [nombre] |

Bloqueos en proyectos: [listar o escribir "Ninguno"]

---

## 2. LEADS NUEVOS (últimas 24h)

| # | Fuente | Nombre | Servicio | Score ICS | Clasificación | Próxima acción |
|---|--------|--------|---------|-----------|--------------|---------------|
| 1 | [Meta/Google/Referido] | [nombre] | [servicio] | [X/100] | [A/B/C/D] | [acción exacta] |

Total leads activos en pipeline: ___
Leads A (acción inmediata): ___
Leads B (seguimiento esta semana): ___

---

## 3. CAMPAÑAS ACTIVAS META ADS

| Campaña | Presupuesto/día | Gasto ayer | Leads ayer | CPL | CTR | Estado |
|---------|----------------|-----------|-----------|-----|-----|--------|
| [nombre] | $___CAD | $___CAD | ___ | $___CAD | ___% | ✅/⚠️/🔴 |

Alerta activa: [describir si CPL>$100 o CTR<1.5% o frecuencia>3.5]

---

## 4. CONTENIDO PENDIENTE

| Pieza | Proyecto | Estado | Score Visual | Deadline |
|-------|---------|--------|-------------|---------|
| Hero Post | [proyecto] | [PENDIENTE/EN PROD/APROBADO] | [X/100] | [fecha/hora] |
| Reel | [proyecto] | [estado] | [X/100] | [fecha/hora] |
| Story | — | [estado] | — | [fecha/hora] |
| Post Educativo | — | [estado] | — | [fecha/hora] |
| Remarketing | — | [estado] | — | [fecha/hora] |

Material disponible en INBOX_MARKETING: [sí/no + N fotos/videos]
Material con score ≥90/100: [N items]

---

## 5. TAREAS CRÍTICAS DEL DÍA

🔴 URGENTE (antes de las 12:00):
  1. [tarea] → [responsable] → [acción exacta]
  2. [tarea] → [responsable] → [acción exacta]

🟠 IMPORTANTE (antes del cierre):
  1. [tarea] → [responsable]
  2. [tarea] → [responsable]

🟡 PENDIENTE (si hay tiempo):
  1. [tarea]

---

## 6. BLOQUEOS DETECTADOS

| Bloqueo | Impacto | Solución propuesta | Quién lo resuelve |
|---------|---------|-------------------|------------------|
| [descripción] | [impacto en ingresos/producción] | [acción concreta] | [Daniel/equipo/agente] |

Si no hay bloqueos: "Sin bloqueos activos"

---

## 7. PRIORIDADES DEL DÍA

**PRIORIDAD A** (impacto directo en ingresos — hacer primero):
→ [acción exacta con verbo + objeto + resultado esperado]

**PRIORIDAD B** (impacto en producción — hacer si se completa A):
→ [acción exacta]

**PRIORIDAD C** (infraestructura — hacer si sobra tiempo):
→ [acción exacta]

---

## 8. PRÓXIMA ACCIÓN EXACTA

```
AHORA MISMO, lo primero que debe pasar es:

[Una sola acción. Verbo + objeto + tiempo + responsable]

Ejemplo: "Llamar al lead García (A+, score 92) antes de las 09:00 — él espera confirmación de visita para esta tarde."
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AGENDA REUNIÓN 09:00 (máx. 30 minutos)
  1. [punto 1 — 5 min]
  2. [punto 2 — 10 min]
  3. [punto 3 — 10 min]
  Decisión pendiente: [qué debe decidir Daniel hoy]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## PASO 3 — ACTUALIZAR DESPUÉS DEL BRIEF

Una vez generado y revisado el DAILY_BRIEF, ejecutar:

```
"Actualiza el DAILY_CONTENT_QUEUE.md con las 5 piezas de hoy según el material disponible."
```

---

## REGLAS DE EJECUCIÓN

```
REGLA 1: El brief se genera siempre — aunque falten datos → escribir "→ Actualizar"
REGLA 2: Máximo 2 minutos leyendo los 4 archivos, máximo 3 minutos generando el brief
REGLA 3: Si una sección no tiene datos → no inventar — escribir el dato faltante claramente
REGLA 4: La "Próxima acción exacta" es siempre UNA SOLA ACCIÓN — no una lista
REGLA 5: El brief se entrega completo o no se entrega — no entregas parciales
```
