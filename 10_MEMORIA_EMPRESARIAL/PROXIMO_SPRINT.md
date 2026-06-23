# SPRINT OPERATIVO — 7 DÍAS
**Período:** 2026-06-24 al 2026-06-30
**Generado:** 2026-06-23 post-backtest
**Principio:** Solo tareas que generan ingresos, ahorran tiempo o mejoran cierres. Cero documentación nueva.

---

## CONTEXTO DEL SPRINT

El backtest reveló que el sistema tiene **32% de implementación real**.
Las 5 áreas de trabajo de esta semana llevan ese número a ~55%.

**Urgencias activas (no esperan al sprint):**
- Paul Gagné — propuesta $35,000 CAD, 8 días sin respuesta → contactar HOY antes de iniciar el sprint
- François Bergeron — lead pavé-uni Laval, sin contactar → calificar HOY con LEAD_REVIEW_ENGINE

---

## BLOQUE 1 — PRODUCCIÓN PREMIUM FLOAT V2

**Objetivo:** Publicar la primera pieza de contenido premium real a través del sistema FLOAT V2. Romper el ciclo de cero producción.

### TAREA 1.1 — Evaluación de material disponible
| Campo | Detalle |
|-------|---------|
| **Responsable** | Daniel |
| **Cuándo** | Día 1 (lunes 24) — mañana, antes de las 09:00 |
| **Tiempo estimado** | 20 minutos |
| **Acción exacta** | Abrir galería del teléfono + Google Drive. Buscar fotos de proyectos recientes completados. El candidato principal: **Proyecto Bouchard** (mencionado en reporte W26). |
| **Dependencia** | Ninguna. Solo tener fotos disponibles. |
| **Resultado esperado** | Lista de 3-5 proyectos con fotos disponibles, con fecha y tipo de proyecto |
| **KPI de éxito** | Al menos 1 proyecto identificado con ≥10 fotos de calidad |

### TAREA 1.2 — Evaluación con PREMIUM_VISUAL_SCORE
| Campo | Detalle |
|-------|---------|
| **Responsable** | Daniel + Claude Code |
| **Cuándo** | Día 1 (lunes 24) — 09:00–09:30 |
| **Tiempo estimado** | 30 minutos |
| **Acción exacta** | Compartir las mejores 5 fotos del proyecto elegido. Claude evalúa con `05_MARKETING/FLOAT_V2_PREMIUM/03_PREMIUM_VISUAL_SCORE.md`. Si score ≥75/100 → avanzar. Si <75/100 → buscar otro proyecto. |
| **Dependencia** | Tarea 1.1 completa |
| **Resultado esperado** | Score numérico del material + lista de mejoras si es necesario |
| **KPI de éxito** | Score ≥75/100 en al menos 1 proyecto (primera vez: meta flexible 75, no 90) |

### TAREA 1.3 — Producción Hero Post + Reel
| Campo | Detalle |
|-------|---------|
| **Responsable** | Daniel + Claude Code (copy) + herramienta de edición |
| **Cuándo** | Día 2 (martes 25) — bloque 10:00–13:00 |
| **Tiempo estimado** | 3 horas (primera vez, se acelera con repetición) |
| **Acción exacta** | Seguir el pipeline de `CONTENT_EXECUTION_ENGINE.md`: seleccionar hero image → generar copy con Claude → producir reel avec musique → preparar story. Una pieza de cada tipo. |
| **Dependencia** | Tarea 1.2 aprobada. Suscripción Epidemic Sound o Artlist activa (o usar audio original). |
| **Resultado esperado** | 1 Hero Post listo + 1 Reel listo para publicar |
| **KPI de éxito** | Pieza publicada en Instagram. CTR en Story >5% en primeras 24h. |

### TAREA 1.4 — Publicación y medición
| Campo | Detalle |
|-------|---------|
| **Responsable** | Daniel |
| **Cuándo** | Día 2 (martes 25) — 17:30–18:00 (horario óptimo Quebec: Feed 17:30-19:30) |
| **Tiempo estimado** | 15 minutos |
| **Acción exacta** | Publicar Hero Post en Instagram + Facebook. Programar Reel para miércoles 17:00. |
| **Dependencia** | Tarea 1.3 completa |
| **Resultado esperado** | Pieza publicada, métricas iniciales en 24h |
| **KPI de éxito** | ≥500 alcance orgánico en 48h. ≥1 solicitud de soumission directa. |

---

## BLOQUE 2 — IMPLEMENTACIÓN ALEX FASE 2

**Objetivo:** Completar los 5 días del sprint Alex para que el formulario de landing genere PRE-SCORE automáticamente y alerte a Daniel sin intervención humana.

### TAREA 2.1 — SPRINT DÍA 1: Campos Pipedrive (45 min)
| Campo | Detalle |
|-------|---------|
| **Responsable** | Daniel |
| **Cuándo** | Día 1 (lunes 24) — tarde, 14:00–15:00 |
| **Tiempo estimado** | 45 minutos |
| **Acción exacta** | Entrar a Pipedrive → Configuración → Campos personalizados. Crear los 8 campos definidos en `ALEX_PIPEDRIVE_FIELDS.md` (sección "Campos Obligatorios Fase 2"): Fuente del lead, Tipo de proyecto, Descripción, Presupuesto declarado, Urgencia, Landing PRE-SCORE, Landing PRE-Clasificación, Guía de llamada. |
| **Dependencia** | Acceso admin a cuenta Pipedrive |
| **Resultado esperado** | 8 campos visibles en cada deal de Pipedrive |
| **KPI de éxito** | Abrir cualquier deal en Pipedrive y ver los 8 campos nuevos |

### TAREA 2.2 — SPRINT DÍA 0 (PRERREQUISITO): Confirmar plataforma formulario
| Campo | Detalle |
|-------|---------|
| **Responsable** | Daniel |
| **Cuándo** | Día 1 (lunes 24) — antes de cualquier trabajo en Zapier |
| **Tiempo estimado** | 10 minutos |
| **Acción exacta** | Confirmar: ¿el formulario de la landing usa Typeform / Gravity Forms / formulario custom / otro? Verificar si tiene integración nativa con Zapier o si necesita webhook. Esta respuesta desbloquea o bloquea el Día 2. |
| **Dependencia** | Acceso a la landing page o al desarrollador que la hizo |
| **Resultado esperado** | Plataforma de formulario confirmada + si soporta Zapier |
| **KPI de éxito** | Respuesta clara: "el formulario usa X y soporta Zapier: SÍ/NO" |

### TAREA 2.3 — SPRINT DÍA 2: Zap 1 — Formulario → Pipedrive + PRE-SCORE (2h)
| Campo | Detalle |
|-------|---------|
| **Responsable** | Daniel + Claude Code (configuración del código JS) |
| **Cuándo** | Día 2 (martes 25) — mañana, 09:00–11:00 |
| **Tiempo estimado** | 2 horas |
| **Acción exacta** | En Zapier: Trigger = nuevo envío del formulario → Paso 1 = Code (JavaScript PRE-SCORE del `ALEX_FASE2_IMPLEMENTATION_ROADMAP.md`) → Paso 2 = Pipedrive: crear deal con todos los campos. Usar el código JS exacto del roadmap. |
| **Dependencia** | Tareas 2.1 y 2.2 completas. Cuenta Zapier con plan multi-step. |
| **Resultado esperado** | Cada envío del formulario crea automáticamente un deal en Pipedrive con PRE-SCORE calculado |
| **KPI de éxito** | Test manual: llenar formulario → verificar deal creado en Pipedrive con score numérico correcto |

### TAREA 2.4 — SPRINT DÍA 3: Zap 2 — Alerta a Daniel (1h)
| Campo | Detalle |
|-------|---------|
| **Responsable** | Daniel |
| **Cuándo** | Día 3 (miércoles 26) — 09:00–10:00 |
| **Tiempo estimado** | 1 hora |
| **Acción exacta** | En Zapier: Trigger = nuevo deal en Pipedrive con PRE-SCORE → Filtro por clasificación → Acción = email a daniel@groupe-ideal.com con resumen del lead (nombre, proyecto, presupuesto, PRE-SCORE, PRE-Clasificación). PRE-A → asunto "🔴 LEAD PRE-A — Contactar <2h". PRE-B → "🟡 LEAD PRE-B — Contactar <4h". |
| **Dependencia** | Tarea 2.3 completa y probada |
| **Resultado esperado** | Daniel recibe email automático en <2 minutos de cada nuevo lead con su clasificación |
| **KPI de éxito** | Test: llenar formulario → email llega a daniel@groupe-ideal.com en <2 minutos |

### TAREA 2.5 — SPRINT DÍA 4: Test con 4 leads (1h)
| Campo | Detalle |
|-------|---------|
| **Responsable** | Daniel |
| **Cuándo** | Día 4 (jueves 27) — 10:00–11:00 |
| **Tiempo estimado** | 1 hora |
| **Acción exacta** | Llenar el formulario 4 veces con datos ficticios definidos en el roadmap: Test A (PRE-A — piscine + urgente + >$25K), Test B (PRE-B), Test C (PRE-C), Test D (incompleto). Verificar que cada uno produce el score y la alerta correctos. |
| **Dependencia** | Tareas 2.3 y 2.4 completas |
| **Resultado esperado** | 4 deals creados en Pipedrive con scores distintos. 4 alertas recibidas con clasificación correcta. |
| **KPI de éxito** | Test A → PRE-A en Pipedrive + alerta "Contactar <2h". Cero errores en los 4 tests. |

### TAREA 2.6 — SPRINT DÍA 5: Go live + monitoreo (30 min)
| Campo | Detalle |
|-------|---------|
| **Responsable** | Daniel |
| **Cuándo** | Día 5 (viernes 28) — 09:00–09:30 |
| **Tiempo estimado** | 30 minutos |
| **Acción exacta** | Activar los Zaps en producción real. Borrar los 4 deals de test en Pipedrive. Verificar que el formulario de la landing está conectado al Zap activo. Monitorear el primer lead real que entre. |
| **Dependencia** | Tarea 2.5 con 0 errores |
| **Resultado esperado** | Sistema Alex Fase 2 en producción. Próximo lead real → deal automático en Pipedrive |
| **KPI de éxito** | Primer lead real procesado automáticamente sin intervención manual |

---

## BLOQUE 3 — INTEGRACIÓN ZAPIER + PIPEDRIVE (AUTOMATIZACIÓN ADICIONAL)

**Objetivo:** Aprovechar la cuenta Zapier activa de Alex para capturar también los leads de Meta Ads automáticamente. Costo adicional: ~1 hora.

### TAREA 3.1 — Zap 3: Meta Ads Lead Form → Pipedrive
| Campo | Detalle |
|-------|---------|
| **Responsable** | Daniel |
| **Cuándo** | Día 4 (jueves 27) — tarde, 15:00–16:00 (después de tests Alex) |
| **Tiempo estimado** | 1 hora |
| **Acción exacta** | En Zapier: Trigger = nuevo lead en Meta Lead Ads → Acción = crear deal en Pipedrive (Fuente: Meta Ads, campos disponibles del formulario). Sin PRE-SCORE inicialmente (el formulario de Meta tiene menos campos). Alerta a Daniel por email igual que Zap 2. |
| **Dependencia** | Cuenta Zapier activa (ya usada para Alex). Meta Business Manager con acceso a Lead Ads. |
| **Resultado esperado** | Cada lead de Meta Ads crea deal en Pipedrive automáticamente + alerta a Daniel |
| **KPI de éxito** | Lead real de Meta Ads → aparece en Pipedrive sin acción manual. Fin de semana: 0 leads perdidos. |

### TAREA 3.2 — Pipeline Pipedrive: configurar las 10 etapas
| Campo | Detalle |
|-------|---------|
| **Responsable** | Daniel |
| **Cuándo** | Día 1 (lunes 24) — junto con Tarea 2.1, 15 min adicionales |
| **Tiempo estimado** | 15 minutos |
| **Acción exacta** | En Pipedrive: verificar que el pipeline tiene las 10 etapas definidas en `ALEX_PIPEDRIVE_FIELDS.md`. Si el pipeline actual tiene menos etapas, agregar las faltantes: Nouveau lead → PRE-A → En qualification → Classifié A/B → Visite confirmée → Soumission envoyée → Négociation → Gagné / Nurturing C / Perdu |
| **Dependencia** | Acceso admin Pipedrive |
| **Resultado esperado** | Pipeline visual con 10 etapas correctas |
| **KPI de éxito** | Abrir el tablero Kanban de Pipedrive y ver las 10 etapas configuradas |

---

## BLOQUE 4 — REPORTES OPERATIVOS

**Objetivo:** Establecer el ritmo diario de reporte sin automatización (eso viene después). El objetivo esta semana: que ningún día cierre sin CEO_DASHBOARD_TEMPLATE lleno.

### TAREA 4.1 — Ritual diario CEO Dashboard (cada día de la semana)
| Campo | Detalle |
|-------|---------|
| **Responsable** | Daniel |
| **Cuándo** | Cada día 17:00–17:15 (15 minutos) |
| **Tiempo estimado** | 15 min/día × 5 días = 75 minutos total |
| **Acción exacta** | Abrir `OPERACIONES_DIARIAS/CEO_DASHBOARD_TEMPLATE.md`. Llenar los campos con datos del día: leads nuevos (de Pipedrive), gasto Meta Ads (de Ads Manager), proyectos activos, contenido producido. Guardar como archivo con fecha (`CEO_DASHBOARD_2026-06-24.md`). |
| **Dependencia** | Ninguna. Solo disciplina. |
| **Resultado esperado** | 5 dashboards diarios con datos reales al final de la semana |
| **KPI de éxito** | 5/5 días con dashboard completado antes de las 17:30 |

### TAREA 4.2 — START_DAY_ENGINE como ritual de inicio (cada día)
| Campo | Detalle |
|-------|---------|
| **Responsable** | Daniel |
| **Cuándo** | Cada día 07:00 AM (5 minutos) |
| **Tiempo estimado** | 5 min/día × 5 días = 25 minutos total |
| **Acción exacta** | Abrir Claude Code. Escribir exactamente: `ejecutar START_DAY_ENGINE`. Recibir DAILY_BRIEF. Imprimir mentalmente las 3 prioridades del día antes de las 09:00. |
| **Dependencia** | Claude Code abierto con el proyecto como working directory |
| **Resultado esperado** | DAILY_BRIEF generado cada mañana con los datos actualizados de la memoria |
| **KPI de éxito** | 5/5 días con START_DAY_ENGINE ejecutado antes de las 08:00 |

---

## BLOQUE 5 — AUTOMATIZACIONES CRÍTICAS

**Objetivo:** Las 2 automatizaciones que protegen ingresos activos. Sin ellas, los leads del fin de semana y las noches se pierden.

### TAREA 5.1 — Alerta: Lead >2h sin contactar (Pipedrive nativo)
| Campo | Detalle |
|-------|---------|
| **Responsable** | Daniel |
| **Cuándo** | Día 3 (miércoles 26) — tarde, 14:00–15:00 |
| **Tiempo estimado** | 1 hora |
| **Acción exacta** | En Pipedrive: Automatizaciones → Nueva automatización. Trigger: deal creado + etapa "Nouveau lead". Condición: si la etapa no cambia en 2h. Acción: enviar email a daniel@groupe-ideal.com con el resumen del deal. Esto usa la automatización nativa de Pipedrive (sin Zapier adicional). |
| **Dependencia** | Pipedrive con plan que incluya automatizaciones (verificar tier de la cuenta) |
| **Resultado esperado** | Email automático si Daniel no contacta un lead en 2h durante horario laboral |
| **KPI de éxito** | Test: crear deal manualmente, no moverlo por 2h → recibir alerta por email |

### TAREA 5.2 — Acción urgente: seguimiento leads activos en pipeline
| Campo | Detalle |
|-------|---------|
| **Responsable** | Daniel |
| **Cuándo** | HOY (antes del sprint formal) |
| **Tiempo estimado** | 45 minutos |
| **Acción exacta** | 1. Llamar a Paul Gagné → propuesta $35,000 CAD → usar plantilla de seguimiento 4.2 de `06_CRM/plantillas_mensajes.md`. 2. Calificar François Bergeron con LEAD_REVIEW_ENGINE (15 min, 8 preguntas). 3. Registrar ambos en Pipedrive con estado actualizado. |
| **Dependencia** | Ninguna. Solo tener el teléfono. |
| **Resultado esperado** | Paul Gagné: respuesta o definición. François Bergeron: clasificación A/B/C/D + próxima acción. |
| **KPI de éxito** | Paul Gagné: conversación antes del final del día. François Bergeron: score numérico asignado. |

---

## CRONOGRAMA CONSOLIDADO — 7 DÍAS

```
LUNES 24 JUNIO — "FOUNDATIONS"
  07:00  Ejecutar START_DAY_ENGINE → DAILY_BRIEF
  08:00  Revisar fotos disponibles (Tarea 1.1 — 20 min)
  09:00  PREMIUM_VISUAL_SCORE proyecto candidato (Tarea 1.2 — 30 min)
  10:00  Confirmar plataforma formulario landing (Tarea 2.2 — 10 min)
  14:00  Crear 8 campos Pipedrive + 10 etapas pipeline (Tareas 2.1 + 3.2 — 1h)
  17:00  CEO Dashboard del día

MARTES 25 JUNIO — "ALEX ZAP 1 + PRIMER CONTENIDO"
  07:00  START_DAY_ENGINE
  09:00  Configurar Zap 1: Formulario → Pipedrive + PRE-SCORE (Tarea 2.3 — 2h)
  11:00  ↑ Continuar si se extiende
  13:00  Producción hero post + reel (Tarea 1.3 — 3h)
  17:00  CEO Dashboard + publicar Hero Post 17:30 (Tarea 1.4)

MIÉRCOLES 26 JUNIO — "ALEX ZAP 2 + AUTOMATIZACIÓN ALERTA"
  07:00  START_DAY_ENGINE
  09:00  Configurar Zap 2: Alerta Daniel (Tarea 2.4 — 1h)
  10:00  ↑ Publicar Reel programado para las 17:00
  14:00  Alerta Pipedrive nativa >2h (Tarea 5.1 — 1h)
  17:00  CEO Dashboard

JUEVES 27 JUNIO — "TESTS ALEX + META ADS ZAP"
  07:00  START_DAY_ENGINE
  10:00  Test 4 leads ficticios (Tarea 2.5 — 1h)
  14:00  Si 0 errores: avanzar. Si hay errores: corregir (reservar 1h)
  15:00  Zap 3: Meta Ads → Pipedrive (Tarea 3.1 — 1h)
  17:00  CEO Dashboard

VIERNES 28 JUNIO — "GO LIVE ALEX + REVISIÓN SEMANAL"
  07:00  START_DAY_ENGINE
  09:00  Alex Fase 2: Go live (Tarea 2.6 — 30 min)
  10:00  Reporte semanal W26 con datos reales de la semana
  11:00  Revisión de métricas: leads capturados, CPL, contenido publicado
  17:00  CEO Dashboard final de semana

SÁBADO-DOMINGO (opcional)
  → Monitorear primer lead real procesado por Alex automáticamente
  → Si llega PRE-A → contactar el lunes antes de las 09:00
```

---

## KPIs DE ÉXITO DEL SPRINT

| KPI | Objetivo al viernes 28 | Crítico si... |
|-----|----------------------|---------------|
| Días con START_DAY_ENGINE ejecutado | 5/5 | <3/5 → no se establece el hábito |
| Días con CEO Dashboard lleno | 5/5 | <3/5 → no hay datos para el siguiente sprint |
| Campos Pipedrive creados | 8/8 | <8 → Zaps no pueden mapearse correctamente |
| Zaps activos en producción | 2 (formulario + Meta Ads) | 0 → el fin de semana se siguen perdiendo leads |
| Alerta >2h sin contacto: activa | Sí | No → leads siguen esperando horas |
| Piezas FLOAT V2 publicadas | ≥1 Hero Post | 0 → otro sprint sin producción real |
| Leads calificados con LEAD_REVIEW_ENGINE | ≥2 (Gagné + Bergeron + nuevos) | 0 → el sistema de ventas no se activa |
| Paul Gagné: respuesta obtenida | Sí (hoy) | No → $35K en riesgo real |

---

## DEPENDENCIAS QUE PUEDEN BLOQUEAR EL SPRINT

| Dependencia | Riesgo | Plan B |
|-------------|--------|--------|
| Formulario de landing sin soporte Zapier | Bloquea Zap 1 | Usar formulario alternativo (Typeform tiene integración nativa) |
| Cuenta Zapier sin plan multi-step | Bloquea Zaps | Upgrade a plan Starter ($20 USD/mes) antes del Día 2 |
| Pipedrive sin plan con automatizaciones nativas | Bloquea Tarea 5.1 | Usar Zapier para la alerta en lugar de Pipedrive nativo |
| Sin fotos de proyectos disponibles | Bloquea Bloque 1 | Usar un proyecto anterior aunque sea de hace 3 meses |
| Paul Gagné no responde llamada | Riesgo de perder $35K | Enviar email + mensaje WhatsApp el mismo día |

---

## LO QUE NO ESTÁ EN ESTE SPRINT (decisión consciente)

| Excluido | Por qué |
|----------|---------|
| Crear más documentación | El sistema tiene 85% de docs. Lo que falta es implementación. |
| FLOAT V2 módulos 2-5 adicionales | Una pieza publicada vale más que 5 módulos nuevos sin ejecutar |
| CLAUDE.md en raíz | No genera ingresos ni mejora cierres esta semana |
| Reportes automáticos con API | Requiere setup complejo. El Dashboard manual es suficiente para la semana. |
| Alex Fase 3 (voz VAPI) | Prerequisito: Fase 2 funcionando primero |
| Google Ads optimización | No tocar lo que ya funciona ($19.67 CPL — excelente) |

---

**Referencia:** `10_MEMORIA_EMPRESARIAL/ECOSISTEMA_BACKTEST_V1.md`
**Al finalizar el sprint:** Actualizar `ESTADO_ACTUAL_ECOSISTEMA.md` con implementación real alcanzada.
**Objetivo:** Pasar de 32% a ≥55% de implementación real en 5 días hábiles.
