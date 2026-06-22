# GUÍA DE USO — MANUS
**Cómo integrar Manus como ejecutor del sistema operativo de Jardín Ideal**

---

## Qué es Manus en este sistema

Manus es el agente que ejecuta las tareas. Los documentos de este sistema son su memoria operativa. Sin los documentos, Manus improvisa. Con los documentos, Manus ejecuta con precisión.

**Analogía:** Los documentos son el manual de operaciones de la empresa. Manus es el empleado que lo sigue.

---

## Principios de uso

1. **Siempre cargar contexto antes de pedir tareas** — sin contexto, las respuestas son genéricas
2. **Una sesión = un agente** — no mezclar CRM con Marketing en la misma sesión
3. **Pedir outputs en el formato definido** — los formatos están en `02_PROMPTS/`
4. **Validar antes de actuar** — revisar el output de Manus antes de enviar mensajes a clientes
5. **Documentar lo que funcionó** — si Manus produce algo excelente, guardarlo como ejemplo

---

## Bloque de Contexto Permanente
**Copiar y pegar al inicio de CADA sesión de Manus antes de cualquier tarea.**

```
═══════════════════════════════════════════════════════
CONTEXTO OPERATIVO — JARDÍN IDEAL
═══════════════════════════════════════════════════════

Empresa: Jardín Ideal
Ubicación: Montreal, Quebec, Canadá
Objetivo 2026: Facturación de 7 millones CAD

Servicios:
- Cour avant / Cour arrière
- Pavé-uni (entrées, allées latérales)
- Escaliers extérieurs
- Piscinas
- Renovación exterior e interior

Idiomas:
- Trabajo interno: Español
- Comunicación con clientes: Francés québécois

Horario: Lunes–Viernes 07:00–18:00
Reunión diaria fija: 09:00 AM

Fecha de hoy: [INSERTAR FECHA]
Temporada actual: [Alta (Abr–Oct) / Baja (Nov–Mar)]

Rol que asumir en esta sesión: [AGENTE CRM / AGENTE MARKETING / AGENTE OPERACIONES]

Documentos de referencia adjuntos:
- [listar los archivos que se van a cargar en esta sesión]
═══════════════════════════════════════════════════════
```

---

## Documentos a Cargar por Tipo de Sesión

### Sesión CRM
```
Obligatorio:
├── 02_PROMPTS/prompt_agente_crm.md
├── 06_CRM/pipeline.md
├── 06_CRM/plantillas_mensajes.md
└── 06_CRM/secuencias_seguimiento.md

Opcional (si hay datos reales):
└── Exportación del CRM / hoja de leads del día
```

### Sesión Marketing
```
Obligatorio:
├── 02_PROMPTS/prompt_agente_marketing.md
├── 05_MARKETING/metricas_kpis.md
└── 05_MARKETING/estrategia_campanas.md

Opcional:
├── Datos de Meta Ads (exportación CSV o capturas)
├── Datos de Google Ads
└── 05_MARKETING/contenido_organico.md (si se pide contenido)
```

### Sesión Operaciones
```
Obligatorio:
├── 02_PROMPTS/prompt_agente_operaciones.md
└── 09_CHECKLISTS/checklist_apertura_diaria.md

Opcional:
└── Lista de proyectos activos (tabla o texto)
```

### Sesión Reportes
```
Obligatorio:
├── 08_REPORTES/reporte_diario.md (o semanal/mensual según corresponda)
├── Datos del día (leads, campañas, proyectos)
└── Reporte del día anterior (para comparación)
```

---

## Comandos Tipo para Manus

### Para activar un agente:
```
"Actúa como el [Agente CRM / Marketing / Operaciones] de Jardín Ideal.
He cargado los documentos de referencia.
Fecha de hoy: [FECHA].
[Dato adicional relevante: ej. "Hoy entraron 8 leads. Aquí están los datos: ..."]
Ejecuta tu rol completo y entrega el reporte en el formato definido."
```

### Para pedir contenido:
```
"Crea la publicación de hoy para Instagram.
Tipo: [Antes/Después / Consejo / Testimonio / Inspiración]
Foto disponible: [descripción de la foto]
Sigue las fórmulas de copy del documento de contenido orgánico.
Entrega: texto completo + hashtags + CTA. Todo en francés québécois."
```

### Para analizar campañas:
```
"Analiza estos datos de Meta Ads de la semana:
[Pegar datos]
Compara con los objetivos del documento de métricas.
Identifica los 3 problemas principales y propón soluciones concretas."
```

### Para generar seguimiento de lead:
```
"Este lead lleva [N] días sin respuesta.
Datos del lead: [Nombre, servicio, última interacción]
Usa la secuencia de seguimiento correcta del CRM.
Genera el mensaje listo para enviar en WhatsApp (en francés)."
```

---

## Limitaciones a Tener en Cuenta

| Limitación | Cómo manejarla |
|---|---|
| Manus no tiene acceso al CRM en tiempo real | Exportar los datos relevantes y pegarlos en la sesión |
| Manus no conoce los datos históricos de campañas | Pegar las métricas del período que se quiere analizar |
| Manus puede generar mensajes genéricos | Siempre revisar antes de enviar al cliente |
| Manus no recuerda sesiones anteriores | Cargar siempre el bloque de contexto permanente |
| Manus puede alucinar datos si no los tiene | Darle siempre los números reales — nunca pedirle que invente |

---

## Flujo de Trabajo Diario con Manus

```
07:00  Sesión 1 — OPERACIONES
       Cargar: prompt_agente_operaciones + checklist_apertura
       Pedir: prioridades del día + agenda de reunión

07:30  Sesión 2 — CRM
       Cargar: prompt_agente_crm + pipeline + datos de leads
       Pedir: reporte CRM completo + mensajes de seguimiento listos

08:00  Sesión 3 — MARKETING
       Cargar: prompt_agente_marketing + métricas + datos de campañas
       Pedir: estado de campañas + contenido del día

[Reunión 09:00 con outputs de las 3 sesiones]

17:00  Sesión 4 — REPORTE DIARIO
       Cargar: plantilla reporte_diario + datos consolidados del día
       Pedir: reporte diario completo listo para compartir
```

---

## Registro de Sesiones Notables

Cuando Manus produzca algo especialmente bueno — un análisis certero, un mensaje que convirtió, una publicación con alto engagement — guardarlo aquí:

```
SESIÓN NOTABLE #___
Fecha: ___________
Tipo: CRM / Marketing / Operaciones / Reporte / Contenido
Qué produjo de valor: _______________________________________
Prompt exacto usado: ________________________________________
Output guardado en: _________________________________________
```
