# SPRINT OPERATIVO — SEMANA 2026-06-24 AL 2026-06-30
**Generado:** 2026-06-24 — sincronización con datos reales (reporte-diario-2026-06-24.json)
**Principio:** Solo tareas que generan ingresos o eliminan pérdidas confirmadas. Dato real prevalece sobre sprint anterior.

> ⚠️ **Sprint anterior invalidado parcialmente:** Referencias a "Paul Gagné" y "François Bergeron" como urgencias no aparecen en el JSON real. Las urgencias reales son las listadas a continuación.

---

## URGENCIAS CRÍTICAS — EJECUTAR HOY ANTES DE 10:00h

Estas no son tareas del sprint — son deudas activas que cuestan dinero o leads ahora mismo.

| # | Acción | Responsable | Impacto |
|---|--------|------------|---------|
| 1 | **Corregir email Zapier**: `daniel@grupoideal.com` → `daniel@groupe-ideal.com` | Daniel | 4 leads recuperados + flujo Cuisines reparado |
| 2 | **Pausar `cour avant`** en Meta Ads Manager (JI) | Daniel | Ahorro $25 CAD/día inmediato |
| 3 | **Pausar `BANOS`** en Meta Ads Manager (GI) | Daniel | Ahorro $25 CAD/día inmediato |
| 4 | **Aumentar `cour arriere`** de $30 → $55/día | Daniel | Escalar mejor campaña ($23.72 CPL) |

---

## BLOQUE 1 — RECUPERAR LEADS VENCIDOS (días 1-2)

**Objetivo:** Salvar los 9 leads con actividades vencidas antes de que se enfríen definitivamente.
**Impacto:** Cada lead costó ~$23 CAD generar. 9 leads = ~$207 CAD en riesgo.

### Día 1 — Daniel llama

| Lead | Servicio | Días vencido | Acción |
|------|---------|-------------|--------|
| Emilie Fournelle | Cour Arriere | 12 | Primera llamada — urgencia máxima |
| JF Gen Gilbert | Cour Arriere | 9 | Llamar — reagendar visita |
| Michele Boileau | Cour Arriere | 5 | Llamar — calificar |
| Colin Maclachlan | Cour Arriere | 2 | Llamar hoy |
| Elise Valcourt | Amenagement | vencida | Agendar fecha de visita |

### Día 1 — Lyes llama

| Lead | Servicio | Estado | Acción |
|------|---------|--------|--------|
| Amelie Duguay | Cour Arriere | 1 día vencido | Llamar esta mañana |
| Charles-emrik Noel | Cour Arriere | 1 día vencido | Llamar esta mañana |
| Rehan Sheikh | Cour Arriere | 2 días vencido | Llamar hoy |
| Genevieve Duchesne | Cuisine | Sin notificación recibida | Llamar — no sabe que llegó |
| Paramjeet Singh | Cuisine | Sin notificación recibida | Llamar — no sabe que llegó |
| Rudis Merlos Escobar | Cuisine | Sin datos en Zap | Verificar datos + llamar |

### Día 1 — Jonathan confirma

| Lead | Estado | Acción |
|------|--------|--------|
| Catherine Archambault | RDV vencido 8 días | Confirmar visita o reagendar |
| Daniela Everon | Visite réalisée — sin propuesta | Confirmar propuesta enviada |

**KPI:** 9/9 leads contactados o redefinidos (sin contacto = cambiar a "Ne répond pas" + reactivar +15 días)

---

## BLOQUE 2 — CIERRES ACTIVOS (días 1-3)

**Objetivo:** Cerrar las propuestas que ya están en etapa avanzada. Estas no necesitan nutrición — necesitan una acción de cierre.

| Lead | Etapa | Acción urgente | Quién |
|------|-------|---------------|-------|
| Anthony Sleiman | RDV mañana 25 jun | Alain Bazinet confirma asistencia | Alain |
| Elise Valcourt | RDV confirmé sin fecha | Daniel agenda fecha de visita HOY | Daniel |
| Daniela Everon | Visite réalisée | Confirmar propuesta → seguimiento | Jonathan |
| Thierry Sicuro | Actividad programada hoy | Ejecutar contacto hoy | Lyes |
| Claudy Querette | Actividad mañana | Lyes prepara llamada | Lyes |

**KPI:** ≥2 propuestas enviadas o visitas concretadas esta semana

---

## BLOQUE 3 — REPARACIÓN TÉCNICA (días 1-2)

**Objetivo:** Eliminar pérdidas de leads causadas por bugs técnicos. Mientras no se corrijan, cada lead nuevo de Cuisine/Balcon puede perderse.

### TAREA 3.1 — Corregir Zapier email (prioridad #1 del día)

| Campo | Detalle |
|-------|---------|
| **Responsable** | Daniel |
| **Cuándo** | Día 1, antes de 10:00h |
| **Acción** | Zapier → Zap "Cuisine" + Zap "Balcon" → editar email de notificación: cambiar `daniel@grupoideal.com` a `daniel@groupe-ideal.com` → guardar → activar → test |
| **KPI** | Test manual: enviar lead ficticio → email llega a la dirección correcta |

### TAREA 3.2 — Confirmar email de Francisco

| Campo | Detalle |
|-------|---------|
| **Responsable** | Daniel |
| **Cuándo** | Día 1, durante mañana |
| **Acción** | Preguntar directamente a Francisco su email real — no usar `fnerlos@groupe-ideal.com` (no existe) |
| **KPI** | Email confirmado → actualizar MEMORIA_GLOBAL |

### TAREA 3.3 — Limpiar test leads en Pipedrive

| Campo | Detalle |
|-------|---------|
| **Responsable** | Daniel / Jonathan |
| **Cuándo** | Día 2-3 |
| **Acción** | Identificar y archivar los ~8 deals de prueba en pipeline "Leads qualifiés" |
| **KPI** | Pipeline muestra solo leads reales (≤26 affaires activos) |

### TAREA 3.4 — HubSpot bot Teams

| Campo | Detalle |
|-------|---------|
| **Responsable** | Daniel |
| **Cuándo** | Día 2 |
| **Acción** | Instalar bot manualmente (falló instalación automática el 23/06). Llamar Connor Starkey: 437-294-4278 para reagendar reunión perdida el 22/06 |
| **KPI** | Bot visible en Teams + reunión reagendada |

---

## BLOQUE 4 — OPTIMIZACIÓN META ADS (días 2-4)

**Objetivo:** Escalar lo que funciona, eliminar lo que no. Post-pausas y corrección Zapier.

### TAREA 4.1 — Campaña cour arriere: escalar presupuesto

| Campo | Detalle |
|-------|---------|
| **Responsable** | Daniel |
| **Cuándo** | Día 1 (junto con las pausas) |
| **Acción** | Meta Ads Manager → cour arriere → editar presupuesto diario: $30 → $55 CAD |
| **KPI** | Presupuesto actualizado visible en Ads Manager |

### TAREA 4.2 — Campaña piscines: evaluar pausa o creatividad nueva

| Campo | Detalle |
|-------|---------|
| **Responsable** | Daniel + Claude Code |
| **Cuándo** | Día 3-4 |
| **Acción** | Con 1 lead en todo el período, CPL $146.07 — decidir: ¿nuevas creatividades FLOAT V2 o pausa? Si pausa: reasignar $25/día a cour arriere |
| **KPI** | Decisión tomada y documentada |

### TAREA 4.3 — GI_Cuisines: evaluar resultados post-corrección Zap

| Campo | Detalle |
|-------|---------|
| **Responsable** | Daniel |
| **Cuándo** | Días 3-4 (después de corregir Zap) |
| **Acción** | Con Zap funcionando correctamente, evaluar si el flujo de leads Cuisine funciona. Si CPL sigue >$80 → revisar creatividades |
| **KPI** | ≥1 lead Cuisine procesado correctamente end-to-end |

---

## BLOQUE 5 — PRODUCCIÓN FLOAT V2 (días 3-5)

**Objetivo:** Publicar contenido con la campaña que funciona (cour arriere). COUR_AVANT_TEST_01 ya está lista — adaptar para cour arriere.

### TAREA 5.1 — Adaptar COUR_AVANT_TEST_01 a cour arriere

| Campo | Detalle |
|-------|---------|
| **Responsable** | Daniel + Claude Code |
| **Cuándo** | Día 3 |
| **Tiempo** | 2 horas |
| **Acción** | Seleccionar imágenes cour arriere de la biblioteca Francisco. Generar copies para publicar Hero Post esta semana. |
| **KPI** | ≥1 pieza publicada en Instagram antes del viernes |

### TAREA 5.2 — Publicar COUR_AVANT_TEST_01 (si Daniel quiere ejecutar la campaña)

| Campo | Detalle |
|-------|---------|
| **Nota** | La campaña cour avant está pausada en Meta Ads — pero se puede publicar orgánicamente en Instagram. Las 7 piezas están listas en `05_MARKETING/CAMPAGNES_TEST/COUR_AVANT_TEST_01/`. |
| **Decisión de Daniel** | ¿Publicar orgánico mientras la campaña Meta está pausada? O ¿esperar a reactivar Meta antes de publicar? |

---

## CRONOGRAMA CONSOLIDADO

```
MARTES 24 JUNIO — "APAGAR INCENDIOS"
  Antes 10:00  Corregir Zap email (Tarea 3.1)
  Antes 10:00  Pausar cour avant + BANOS en Meta Ads
  Antes 10:00  Aumentar cour arriere a $55/día
  Mañana       Daniel llama: Emilie Fournelle, JF Gilbert, Michele Boileau, Colin Maclachlan
  Mañana       Lyes llama: Amelie Duguay, Charles-emrik Noel, Rehan Sheikh, Genevieve Duchesne, Paramjeet Singh
  Mañana       Jonathan: Catherine Archambault (visita), Daniela Everon (propuesta)
  Durante día  Confirmar email Francisco (Tarea 3.2)

MIÉRCOLES 25 JUNIO — "CIERRES"
  09:00  Anthony Sleiman — RDV con Alain Bazinet
  10:00  HubSpot bot Teams + llamar Connor Starkey (Tarea 3.4)
  14:00  Limpiar test leads Pipedrive (Tarea 3.3)
  Resto  Seguimiento cierres activos (Elise Valcourt, Daniela Everon)

JUEVES 26 JUNIO — "META ADS + FLOAT"
  09:00  Evaluar piscines — ¿pausar o nuevas creatividades? (Tarea 4.2)
  10:00  Iniciar adaptación FLOAT V2 para cour arriere (Tarea 5.1)
  Tarde  Evaluar resultados GI_Cuisines post-Zap (Tarea 4.3)

VIERNES 27 JUNIO — "PRODUCCIÓN"
  10:00  Finalizar Hero Post cour arriere (Tarea 5.1)
  17:30  Publicar en Instagram
  17:00  Resumen semanal — KPIs reales vs. sprint
```

---

## KPIs DE ÉXITO DEL SPRINT

| KPI | Objetivo al viernes 28 | Crítico si... |
|-----|----------------------|---------------|
| Zap email corregido | Sí (hoy) | No → más leads Cuisine perdidos |
| Campañas sin leads pausadas | 2/2 (cour avant + BANOS) | 0 → $50/día desperdiciados |
| Leads vencidos contactados | 9/9 | <6 → leads fríos irrecuperables |
| Propuestas enviadas o visitas | ≥2 | 0 → pipeline no avanza |
| Pieza FLOAT V2 publicada | ≥1 | 0 → sin contenido premium esta semana |
| Leads Cuisines notificados a Lyes | 4/4 (post-Zap) | 0 → dinero gastado sin retorno |
| Test leads Pipedrive limpios | 8/8 | 0 → pipeline datos sucios |

---

## LO QUE NO ESTÁ EN ESTE SPRINT (decisión consciente)

| Excluido | Por qué |
|----------|---------|
| Alex Fase 2 — Zapier formulario | El Zapier actual está roto — arreglar primero antes de agregar más Zaps |
| Nuevos módulos FLOAT V2 | COUR_AVANT_TEST_01 ya tiene 7 piezas listas — ejecutar antes de crear más |
| Documentación adicional | El sistema tiene suficiente. Lo que falta es implementación. |
| Google Ads | No tocar — no hay datos de rendimiento en el JSON del 24/06 |
| BANOS creatividades nuevas | Sin resultados en 30 días — pausar y evaluar en 2 semanas |

---

**Referencia START_DAY_ENGINE:** `08_REPORTES/RESUMENES_DIARIOS/START_DAY_ENGINE_2026-06-24.md`
**Al finalizar el sprint:** Actualizar `ESTADO_ACTUAL_ECOSISTEMA.md` con resultados reales.
**Objetivo:** Recuperar $50/día desperdiciados + salvar 9 leads en riesgo + reparar Zapier.
