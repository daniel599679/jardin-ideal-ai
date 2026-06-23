# MORNING BRIEF — JARDÍN IDEAL
**Template para generación automática diaria**
**Completar antes de las 09:00 AM**

---

## INSTRUCCIONES PARA CLAUDE

Al recibir la solicitud "Genera el Morning Brief de hoy", Claude debe:

1. Leer `KPIS_EMPRESA.md` → extraer datos de Meta Ads del día anterior
2. Leer `PROYECTOS_ACTIVOS.md` → extraer proyectos en ejecución y estados
3. Leer `PROXIMOS_PASOS.md` → extraer top 3 prioridades del día
4. Leer `REUNIONES_DIARIAS.md` → extraer agenda de la reunión
5. Completar el template a continuación con los datos reales
6. Entregar el brief en formato imprimible (o copiar al chat)

**Solicitud tipo:**
```
"Claude, genera el Morning Brief de hoy [FECHA].
Datos Meta Ads de ayer: [gasto $X, leads Y, CPL $Z]
Proyectos en campo: [lista]
¿Hay visitas hoy? [sí/no + nombre]"
```

---

## TEMPLATE DEL MORNING BRIEF

*(Copiar y completar con los datos del día)*

```
╔══════════════════════════════════════════════════════════════╗
║         MORNING BRIEF — JARDÍN IDEAL                        ║
║         [DÍA DE LA SEMANA], [DD] de [MES] de [AÑO]         ║
╚══════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ESTADO GENERAL DEL DÍA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  🟢 VERDE — Todo bajo control
  🟡 AMARILLO — Requiere atención
  🔴 ROJO — Urgencia / acción inmediata

Estado: [🟢 / 🟡 / 🔴]
Motivo: [una línea explicando el estado]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 META ADS — AYER [FECHA AYER]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Gasto:        $[X] CAD
  Leads:        [X] leads | CPL: $[X]
  Alcance:      [X] personas | CTR: [X]%
  ROAS:         [X]× | Impresiones: [X]

  ▶ ALERTA: [si hay algo fuera de rango — si todo OK escribir "Sin alertas"]

  Campaña más rentable:     [nombre] — CPL $[X]
  Campaña con más leads:    [nombre] — [X] leads
  Campaña a revisar:        [nombre] — [motivo]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 LEADS — ESTADO DEL PIPELINE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Leads nuevos ayer:        [X]
  Leads calificados (≥70):  [X]
  En espera de contacto:    [X]
  Propuestas pendientes:    [X]
  Propuestas venciendo hoy: [X] ← follow-up urgente

  PERFIL PIPELINE HOY:
  A+ (≥85 pts): [X] leads | Acción: contactar en 2h
  A  (70–84):   [X] leads | Acción: contactar antes del mediodía
  B  (55–69):   [X] leads | Acción: responder esta tarde
  C  (<55):     [X] leads | Acción: respuesta cortés + redirigir

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 PROYECTOS EN CAMPO HOY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  [PROYECTO 1] — [Servicio] — [Ciudad]
    Estado: [En ejecución / Día X de Y]
    Equipo: [X personas]
    Nota: [si hay algo a vigilar o "Sin alertas"]

  [PROYECTO 2] — [Servicio] — [Ciudad]
    Estado: [En ejecución / Terminando hoy → activar FLOAT]
    Equipo: [X personas]
    Nota: [notas]

  [Sin proyectos en campo hoy]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 VISITAS AGENDADAS HOY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  [HORA] — [NOMBRE CLIENTE] — [CIUDAD]
    Perfil: [A+ / A / B] | Score: [X]/100
    Servicio: [tipo de proyecto]
    Presupuesto estimado: $[X]
    Ambos decisores presentes: [Sí / No → REAGENDAR]
    LIR preparado: [Sí / No → PREPARAR ANTES DE IR]
    Nota clave: [objeción anticipada o punto a destacar]

  [Sin visitas hoy]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 TOP 3 PRIORIDADES DE HOY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  #1 ► [Tarea más importante del día]
       Por qué hoy: [motivo de la urgencia]
       Responsable: [Daniel / Claude / Equipo]
       Tiempo estimado: [X horas]

  #2 ► [Segunda prioridad]
       Por qué hoy: [motivo]
       Responsable: [quién]

  #3 ► [Tercera prioridad]
       Por qué hoy: [motivo]
       Responsable: [quién]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 CONTENIDO FLOAT — OPORTUNIDADES DE HOY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Proyectos terminando hoy con fotos disponibles:
  [PROYECTO] — [Servicio] → ACTIVAR PROTOCOLO FLOAT (60 min)
  [Ninguno hoy]

  Piezas de contenido en cola:
  [lista o "pipeline vacío"]

  Campañas activas por servicio:
  [Cour Avant: activa / pausada]
  [Pavé-Uni: activa / pausada]
  [...otros servicios]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 AGENDA DE LA REUNIÓN 09:00 AM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  09:00 — KPIs de ayer [2 min]
  09:02 — Estado proyectos en campo [5 min]
  09:07 — Leads y propuestas urgentes [5 min]
  09:12 — Prioridades del día [5 min]
  09:17 — Decisiones necesarias [5 min]
  09:22 — Cierre y confirmación [3 min]

  Decisiones que requieren debate:
  → [decisión 1 o "Ninguna — reunión informativa"]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ALERTAS DEL DÍA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  🔴 URGENTE:   [alerta crítica o "Sin alertas críticas"]
  🟡 ATENCIÓN:  [alerta moderada o "Sin alertas moderadas"]
  📋 RECORDAR:  [recordatorio del día]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 CLIMA — [CIUDAD, QC]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  [X]°C — [Soleado / Nublado / Lluvia / Tormenta]
  Impacto en operaciones: [Sin impacto / Posible retraso en proyecto X]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 GENERADO POR: Claude Code | [FECHA] [HORA]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## EJEMPLO DE BRIEF COMPLETADO

*(Ejemplo con datos ficticios para referencia)*

```
╔══════════════════════════════════════════════════════════════╗
║         MORNING BRIEF — JARDÍN IDEAL                        ║
║         LUNES, 23 de junio de 2026                          ║
╚══════════════════════════════════════════════════════════════╝

Estado: 🟡 AMARILLO
Motivo: CPL en $42 — por encima del objetivo de $25

META ADS — AYER 22/06
  Gasto:        $87 CAD
  Leads:        2 leads | CPL: $43.50
  Alcance:      4,200 personas | CTR: 1.8%
  ROAS:         6.2× | Impresiones: 18,500

  ▶ ALERTA: CPL fuera de objetivo — revisar segmentación Pavé-Uni

LEADS — ESTADO DEL PIPELINE
  Leads nuevos ayer:        2
  Leads calificados (≥70):  1 (A — score 76/100)
  Propuestas pendientes:    3
  Propuestas venciendo hoy: 1 (Famille Tremblay — enviada hace 7 días)

PROYECTOS EN CAMPO HOY
  CA-007 Cour Arrière — Laval — Día 3 de 5
    Equipo: 4 personas | Sin alertas

VISITAS AGENDADAS HOY
  14:00 — Famille Martin — Westmount
    Perfil: A+ | Score: 88/100 | Presupuesto: ~$35K
    Servicio: Pavé-Uni + Escaliers
    Ambos decisores presentes: Sí ✓
    LIR preparado: Sí ✓
    Nota: Mencionó que tiene referencia de vecino — buscar quién

TOP 3 PRIORIDADES DE HOY
  #1 ► Visita Famille Martin 14:00 → cerrar contrato
  #2 ► Follow-up Famille Tremblay (propuesta 7 días) → llamar antes de 11AM
  #3 ► Revisar segmentación campaña Pavé-Uni (CPL fuera de objetivo)
```

---

## CÓMO SOLICITAR EL BRIEF A CLAUDE

### Opción A — Solicitud completa (recomendado)
```
"Claude, genera el Morning Brief del [FECHA].
Datos de Meta Ads de ayer: gasto $[X], leads [X], CPL $[X], CTR [X]%, alcance [X].
Proyectos en campo hoy: [nombres y estados]
Visitas hoy: [nombre cliente, hora, ciudad]
Propuestas urgentes: [nombre cliente, días transcurridos]"
```

### Opción B — Solicitud mínima
```
"Claude, genera el Morning Brief de hoy.
Lee KPIS_EMPRESA.md, PROYECTOS_ACTIVOS.md y PROXIMOS_PASOS.md para completarlo."
```

### Opción C — Brief automático al abrir sesión
Claude Code puede generar el brief automáticamente al iniciar una sesión si detecta que:
- Es antes de las 09:00 AM
- No hay un brief del día en el historial de la sesión

*(Configurar en un futuro FLOAT V2 Módulo 7 — KPI de Producción)*

---

*MORNING_BRIEF_TEMPLATE v1.0 — 2026-06-23*
*Jardín Ideal AI System — 10_MEMORIA_EMPRESARIAL/PROTOCOLOS_DIARIOS/*
