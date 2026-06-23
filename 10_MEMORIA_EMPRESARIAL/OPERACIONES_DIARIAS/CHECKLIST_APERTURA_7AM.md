# CHECKLIST DE APERTURA — 7:00 AM
**Jardín Ideal | Ejecutar cada mañana laborable**
**Tiempo máximo: 10 minutos exactos**
**Al terminar: commit + push + actualizar HISTORIAL_CAMBIOS.md**

---

## EJECUTAR EN ORDEN — NO SALTARSE NINGÚN PASO

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CHECKLIST APERTURA — [FECHA] — JARDÍN IDEAL
Hora de inicio: ___:___ | Hora de cierre: ___:___
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[ ] 1. SISTEMA — Abrir Claude Code y ejecutar START_DAY_ENGINE (2 min)
        → Instrucción: "ejecutar START_DAY_ENGINE"
        → Recibir DAILY_BRIEF completo
        → Leer sección 5 (Tareas Críticas) y sección 8 (Próxima Acción)

[ ] 2. LEADS — Revisar leads nuevos desde ayer a las 18:00 (2 min)
        → Abrir CRM / Meta Ads / WhatsApp de empresa
        → ¿Hay leads A (score ≥85)? → LLAMAR AHORA, antes de hacer cualquier otra cosa
        → ¿Leads B o C? → programar llamada o mensaje para antes de las 10:00
        → Anotar en el DAILY_BRIEF sección 2

[ ] 3. CAMPAÑAS — Revisar Meta Ads en 60 segundos (1 min)
        → Abrir Meta Business Manager → Aperçu des publicités
        → ¿CPL > $100 en alguna campaña? → marcar como ALERTA en el brief
        → ¿CTR < 1.5% por 3 días? → marcar como ALERTA
        → ¿Todo normal? → no hacer nada

[ ] 4. PROYECTOS EN CAMPO — Verificar estado de obras activas (1 min)
        → ¿Algún proyecto con problema reportado por el equipo? (WhatsApp del equipo)
        → ¿Alguna entrega programada para hoy? → confirmar con el jefe de obra
        → Anotar en el DAILY_BRIEF sección 1

[ ] 5. CONTENIDO — Verificar material disponible en INBOX_MARKETING (1 min)
        → ¿Hay fotos/videos nuevos de ayer? (Drive / carpeta compartida)
        → ¿Cuántas fotos? ¿Tienen oportunidad de llegar a 90/100?
        → Anotar en el DAILY_BRIEF sección 4

[ ] 6. IDEAS — Revisar IDEA_INBOX.md (1 min)
        → ¿Hay ideas nuevas marcadas como 🆕 NUEVA?
        → Si sí: clasificar como P1/P2/P3 rápido (ver PROTOCOLO_CAPTURA_IDEAS)
        → Si no: continuar

[ ] 7. PRÓXIMA ACCIÓN — Confirmar la #1 del día (1 min)
        → Leer la sección 8 del DAILY_BRIEF: ¿qué es lo ÚNICO más importante ahora?
        → Escribirlo aquí: _______________________________________________
        → No empezar otra cosa hasta completar esta acción

[ ] 8. REUNIÓN 09:00 — Preparar agenda (1 min)
        → Leer REUNIONES_DIARIAS.md
        → Confirmar los 3 puntos de la reunión de hoy
        → ¿Hay una decisión crítica para Daniel? → ponerla como punto 1

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CHECKLIST COMPLETADO: ☐ Sí  | Hora: ___:___
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## AL FINALIZAR EL CHECKLIST — COMMIT + PUSH + HISTORIAL

Ejecutar en Claude Code:

```
"Checklist de apertura completado. Ejecuta el cierre:
 1. Actualiza HISTORIAL_CAMBIOS.md con lo que se hizo hoy
 2. Haz commit con el mensaje: 'ops: apertura [FECHA] — [resumen de 1 línea]'
 3. Push a GitHub"
```

**O manualmente en terminal:**

```bash
cd C:/Users/Daniel/Desktop/Jardin-ideal-AI/Jardin_Ideal_AI_System
git add 10_MEMORIA_EMPRESARIAL/
git commit -m "ops: apertura [FECHA] — [resumen]"
git push origin master
```

---

## SEÑALES DE QUE EL DÍA EMPEZÓ MAL (actuar de inmediato)

```
🔴 Hay un lead A sin contactar de ayer → llamar ANTES de terminar el checklist
🔴 Una campaña lleva 24h sin leads con presupuesto activo → revisar Meta Ads
🔴 Un proyecto tiene problema reportado → hablar con el jefe de obra ahora
🔴 No hay material ≥90/100 para el Hero de hoy → activar plan de contingencia:
   → Usar el mejor proyecto del archivo con nuevo copy
   → O producir contenido 100% educativo del día
```

---

## PLAN DE CONTINGENCIA — SI EL DÍA SE SALE DE CONTROL

```
PRIORIDAD ABSOLUTA (en este orden si todo explota):
  1. Responder leads A → nadie espera más de 2 horas
  2. Verificar proyectos en campo → si hay un problema de obra, resolverlo primero
  3. Revisar campañas Meta → si hay gasto sin leads, pausar temporalmente
  4. El contenido puede esperar hasta mañana si los primeros 3 tienen problema

REGLA: Un día sin contenido no arruina la empresa.
       Un lead A sin respuesta sí puede arruinar una semana.
```

---

## HISTORIAL DE APERTURAS

| Fecha | Completado | Hora inicio | Hora fin | Líder A contactado | Problema detectado |
|-------|-----------|------------|---------|-------------------|-------------------|
| [hoy] | ☐ Sí ☐ No | ___:___ | ___:___ | Sí/No | Sí/No |

---

## INSTRUCCIÓN PARA ACTUALIZAR HISTORIAL_CAMBIOS.md

Al completar el checklist, añadir esta entrada al final de HISTORIAL_CAMBIOS.md:

```markdown
## [FECHA] — Apertura operativa

| Acción | Resultado |
|--------|-----------|
| Checklist apertura 7AM | ✅ Completado en ___ minutos |
| Leads revisados | ___ leads (A:___ B:___ C:___ D:___) |
| Campañas revisadas | ✅ Normal / ⚠️ Alerta: ___ |
| Material contenido | ___ fotos/videos | Score máximo: ___/100 |
| Commit | [hash] |
```
