# HOME WORKFLOW PROTOCOL
**Cómo trabajar desde casa sin perder contexto**
**Versión:** 1.0 | **Fecha:** 2026-06-23
**Para:** Daniel — trabajo remoto desde cualquier ubicación (casa, oficina, móvil)
**Objetivo:** Producir al mismo nivel que en la oficina, con cualquier herramienta disponible.

---

## EL PRINCIPIO FUNDAMENTAL

El ecosistema de Jardín Ideal está en GitHub. GitHub es la fuente de verdad.
Cualquier IA puede acceder a ese contexto si se le da correctamente.
**La clave no es la herramienta — es el contexto que le das al inicio.**

---

## MAPA DE HERRAMIENTAS POR SITUACIÓN

```
SITUACIÓN                           → HERRAMIENTA IDEAL
─────────────────────────────────────────────────────
Crear/editar archivos del sistema   → Claude Code
Trabajo estratégico largo           → Claude Web o Claude Desktop
Brainstorming y creatividad         → ChatGPT
Producir video (reel MP4)          → Manus
Trabajo en el móvil (caminando)     → Claude Web (mobile) o ChatGPT mobile
Automatizar con herramientas web    → Manus
Revisión rápida de métricas         → Claude Web con contexto pegado
Emergencia (sin laptop)             → Claude Web mobile + contexto compacto
```

---

## 1. QUÉ DECIRLE A CHATGPT

### Cuándo usar ChatGPT

- Cuando quieres ideas sin restricciones del sistema actual
- Research de competidores (Techo-Bloc, paysagistas premium QC)
- Variantes de copy para A/B test
- Ideas de contenido educativo
- Cuando Claude está ocupado o lento

### Cómo iniciar la sesión (copiar y pegar)

```
Eres el consultor de marketing de Jardín Ideal, empresa de paisajismo premium en Montreal, Quebec, Canadá.

CONTEXTO:
- Objetivo 2026: 7 millones CAD en facturación
- Mercado: propietarios de casas 35-65 años, francófonos, ingresos medios-altos
- Servicios: Cour avant, cour arrière, pavé-uni, balcons, escaliers, piscines, renovación exterior
- Posicionamiento: nivel Techo-Bloc / Permacon / Architectural Digest — NO económico, PREMIUM
- Idioma con clientes: francés québécois | Idioma interno: español
- CTA siempre: "Soumission gratuite · 514-266-2504"
- Copy: declarativo (no interrogativo), hook ≤8 palabras, sin "meilleur" sin dato concreto
- Sin signos de exclamación en headlines

HOY NECESITO:
[Describir la tarea específica aquí]
```

### Cómo cerrar la sesión con ChatGPT

```
Al terminar, copiar los outputs más útiles.
Pegarlos en:
  → IDEA_INBOX.md si es una idea
  → El archivo del sistema correspondiente si es contenido listo para usar
  → DAILY_CONTENT_QUEUE.md si es copy listo para programar
```

---

## 2. QUÉ DECIRLE A CLAUDE WEB

### Cuándo usar Claude Web

- Trabajo desde el móvil
- Sesiones largas de análisis sin necesidad de editar archivos
- Cuando no tienes acceso a Claude Code (sin laptop)
- Revisión de estrategia, briefings, planning

### Cómo iniciar la sesión (copiar y pegar)

```
Eres el sistema operativo de IA de Jardín Ideal (Montreal, Quebec, Canadá).

IDENTIDAD:
Empresa de paisajismo premium. Objetivo 2026: 7M CAD. Idioma clientes: francés québécois.
Teléfono: 514-266-2504. Posicionamiento: Techo-Bloc / Architectural Digest level.

SISTEMAS ACTIVOS:
- FLOAT V2 Premium: gate visual 90/100 para publicar, 5 módulos de producción
- Producción Continua: 5 piezas diarias (Hero + Reel + Story + Educativo + Remarketing)
- ICS: calificación leads 0-100pts, perfiles A+/A/B/C
- Calendario: Lun=Autoridad, Mar=Educación, Mié=Transformación, Jue=Prueba Social, Vie=Oferta

ESTÁNDARES:
- Visual: score ≥90/100 para hero, ≥75 para secundarias
- Copy: hook ≤8 palabras, declarativo, sin "meilleur/qualité" sin dato concreto
- Tipografía: Playfair Display Bold Italic (headlines) + Montserrat (body)
- Colores: #052B16 / #008E3F / #C8A45A dorado (SOLO teléfono) / #F5F2EB / #FFFFFF

HOY ES: [FECHA]
ÚLTIMA SESIÓN: [qué se completó la última vez]
HOY NECESITO: [tarea específica]
```

### Instrucción de cierre de sesión Claude Web

Al terminar, pedirle a Claude:

```
"Resume esta sesión en máximo 5 puntos para actualizar el ESTADO_ACTUAL_ECOSISTEMA.md.
Formato:
  Fecha: [hoy]
  Completado: [lista]
  En progreso: [lista]
  Próxima sesión debe: [lista]"
```

Copiar ese resumen. Al volver a Claude Code, pegarlo en el archivo correspondiente.

---

## 3. QUÉ DECIRLE A CLAUDE DESKTOP

### Cuándo usar Claude Desktop

- Trabajo diario desde casa (tiene herramientas MCP configuradas)
- Acceso a Drive, Calendar u otras herramientas integradas
- Cuando quieres que Claude pueda leer o escribir archivos locales vía MCP

### Configuración permanente (hacer una vez)

Crear el archivo `CLAUDE.md` en la raíz del proyecto:
`C:\Users\Daniel\Desktop\Jardin-ideal-AI\Jardin_Ideal_AI_System\CLAUDE.md`

```
# CLAUDE.md — Contexto permanente Jardín Ideal

Este proyecto es el sistema operativo de IA de Jardín Ideal (Montreal, Quebec, Canadá).
Al iniciar cualquier sesión, leer:
  1. 10_MEMORIA_EMPRESARIAL/ESTADO_ACTUAL_ECOSISTEMA.md
  2. 10_MEMORIA_EMPRESARIAL/PROXIMOS_PASOS.md
  3. 10_MEMORIA_EMPRESARIAL/CAPTURA_IDEAS/IDEA_INBOX.md

Empresa: Jardín Ideal | Objetivo 2026: 7M CAD | Teléfono: 514-266-2504
Sistema activo: FLOAT V2 Premium (gate 90/100) + Producción Continua (5 piezas/día)
Idioma clientes: francés | Idioma interno: español
GitHub: https://github.com/daniel599679/jardin-ideal-ai.git rama master
```

Si el CLAUDE.md está configurado, Claude Desktop lo lee automáticamente.
Si no, usar el mismo bloque de Claude Web al inicio.

### Instrucción de inicio rápido (con CLAUDE.md)

```
"Lee el ESTADO_ACTUAL_ECOSISTEMA y el PROXIMOS_PASOS. Dime qué hay que hacer hoy."
```

---

## 4. QUÉ DECIRLE A CLAUDE CODE

### Cuándo usar Claude Code

- SIEMPRE que necesitas crear o editar archivos del sistema
- Para hacer commits y push a GitHub
- Para el START_DAY_PROTOCOL (tiene el hook de voz)
- Para la sesión de cierre al final del día

### Claude Code ya sabe el contexto

Claude Code lee los archivos del proyecto directamente. No necesitas pegar contexto.

### Instrucción de inicio de sesión

```
"Lee 10_MEMORIA_EMPRESARIAL/ESTADO_ACTUAL_ECOSISTEMA.md y
 10_MEMORIA_EMPRESARIAL/PROXIMOS_PASOS.md.
 Dime el estado actual y cuál es la P1 de hoy."
```

### Instrucción de cierre de sesión (OBLIGATORIO)

```
"Sesión de cierre del día [FECHA]. Hicimos:
[lista de lo que se hizo]

Por favor:
1. Actualiza ESTADO_ACTUAL_ECOSISTEMA.md con lo de hoy
2. Actualiza PROXIMOS_PASOS.md con los próximos pasos
3. Revisa si hay ideas nuevas para agregar a IDEA_INBOX.md
4. Haz commit con mensaje descriptivo y push a GitHub"
```

### Casos de uso específicos

```
CREAR UN NUEVO MÓDULO:
  "Crea [nombre del módulo] en [carpeta] integrando FLOAT V2 Premium. Guarda y haz commit."

ACTUALIZAR UN AGENTE:
  "Modifica [agente] para agregar [funcionalidad]. Lee el archivo primero."

CAPTURAR UNA IDEA:
  "Agrega esta idea al IDEA_INBOX: [idea bruta]"

PRIORIZAR IDEAS:
  "Lee el IDEA_INBOX y clasifica todas las ideas 🆕 NUEVA como P1/P2/P3.
   Actualiza IDEAS_PRIORIZADAS con tus recomendaciones."
```

---

## 5. QUÉ ENVIAR A MANUS

### Cuándo usar Manus

- Producción de reels (tiene ffmpeg y herramientas de video)
- Tareas que requieren navegar por internet o usar apps
- Automatizaciones que requieren hacer clic (Meta Business Suite, Drive, etc.)
- Tareas largas que pueden ejecutarse sin supervisión

### Manus no tiene memoria — siempre incluir contexto completo

### Formato de tarea para Manus

```
CONTEXTO:
Trabajo para Jardín Ideal (Montreal, Quebec). Empresa de paisajismo premium.
Idioma clientes: francés. Teléfono: 514-266-2504 (siempre en dorado #C8A45A).
Standard: FLOAT V2 Premium — audio a -14 LUFS, formato 9:16, 1080×1920.
Tipografía: Playfair Display Bold Italic + Montserrat.

TAREA:
[Descripción exacta y completa de lo que debe hacer]

ARCHIVOS DE ENTRADA:
[Rutas exactas o descripción de los archivos]

OUTPUT ESPERADO:
[Formato, nombre del archivo, carpeta de destino]

VERIFICACIÓN:
[Cómo sabe Manus que la tarea está bien hecha]
```

### Ejemplos de tareas para Manus

```
PRODUCCIÓN DE REEL:
"Usa el archivo 3_PROMPT_MANUS_VIDEO.txt en:
 CONTENIDO_PARA_PUBLICAR/COUR_AVANT/PUSCHAK/2_REEL_CAPCUT/
 Produce el reel siguiendo exactamente las instrucciones.
 Output: PUSCHAK_REEL_FINAL.mp4 en la raíz del paquete.
 Verificar: reproducir el MP4 y confirmar que tiene las escenas correctas."

SUBIR A DRIVE:
"Sube el archivo [ruta] a la carpeta Drive: DISPONIBLE/HERO/[proyecto].
 Confirma el link compartible cuando esté listo."

PROGRAMAR EN META:
"Abre Meta Business Suite. Programa esta publicación para [fecha] a las [hora]:
 Imagen: [ruta o link]
 Copy: [texto exacto en francés]
 Plataformas: Instagram + Facebook simultáneamente."
```

---

## 6. CÓMO SINCRONIZAR AL DÍA SIGUIENTE

### La noche anterior (5 minutos)

```
EN CLAUDE CODE O CLAUDE DESKTOP:
1. "Sesión de cierre: actualiza los archivos de memoria con lo de hoy."
2. Revisar el IDEA_INBOX: ¿hay ideas nuevas de la jornada?
3. Git commit + push: "el sistema queda en GitHub"

EN EL TELÉFONO:
4. Revisar WhatsApp propio: ¿hay mensajes "IDEA:" del día?
5. Si hay → dejar una nota de voz resumiendo para procesar mañana
```

### La mañana siguiente (15 minutos — antes de las 09:00)

```
07:30 — DAILY_IDEA_REVIEW (15 min):
  1. Leer IDEA_INBOX.md → clasificar ideas nuevas (5 min)
  2. Leer IDEAS_PRIORIZADAS.md → confirmar P1 del día (3 min)
  3. Leer ESTADO_ACTUAL_ECOSISTEMA.md → ¿qué cambió? (2 min)
  4. Leer PROXIMOS_PASOS.md → P1 de hoy (2 min)
  5. Abrir DAILY_CONTENT_QUEUE → ¿hay material ≥90/100 para las 5 piezas? (3 min)

07:45 — PREPARAR LA REUNIÓN DE 09:00:
  Leer REUNIONES_DIARIAS.md y preparar el agenda de la reunión de 9:00

09:00 — REUNIÓN DIARIA (30 min máximo, inamovible):
  Estructura: KPIs → Decisiones → Acciones del día → Cierre
```

---

## ESCENARIOS COMUNES RESUELTOS

### Escenario A — "Estoy en casa sin laptop, solo con el teléfono"

```
HERRAMIENTA: Claude Web (mobile) o ChatGPT mobile
BLOQUE DE INICIO: el bloque compacto de Claude Web (copiado de los favoritos del teléfono)
TAREA: puede hacer análisis, escribir copy, brainstorming — todo excepto modificar archivos
AL VOLVER AL LAPTOP: copiar outputs en Claude Code → hacer commit
```

### Escenario B — "Hay una idea urgente a las 11 PM"

```
CAPTURA: nota de voz WhatsApp enviada a uno mismo, prefijo "IDEA:"
PROCESO: no abrir Claude a las 11 PM — capturar y revisar mañana
EXCEPCIÓN: si es una idea P1 que mañana ya no será relevante (ej: oportunidad de temporada)
  → Abrir Claude Web mobile, capturar la idea completa
  → No ejecutar — solo capturar y priorizar
```

### Escenario C — "Cambié de laptop, ¿cómo recupero el contexto?"

```
1. Clonar el repo: git clone https://github.com/daniel599679/jardin-ideal-ai.git
2. Abrir Claude Code en la nueva laptop
3. Claude Code lee el ESTADO_ACTUAL_ECOSISTEMA.md automáticamente
4. Todo el contexto está en GitHub — sin pérdida de información
```

### Escenario D — "Estoy en reunión con un cliente y surge una idea"

```
CAPTURA INMEDIATA: en el teléfono, nota de voz discreta o WhatsApp a uno mismo
PREFIJO: "IDEA: [idea bruta]"
NO procesar en el momento — seguir con el cliente
DESPUÉS: revisar en el DAILY_IDEA_REVIEW de la mañana siguiente
```

### Escenario E — "Quiero trabajar una hora antes de que empiece el día"

```
06:00 — Abrir Claude Code
"Lee ESTADO_ACTUAL_ECOSISTEMA.md y PROXIMOS_PASOS.md. ¿Qué puedo completar en 1 hora?"
Claude identifica la tarea de mayor impacto ejecutable en 60 minutos.
Ejecutar. Commit. Cierre antes de las 07:00.
```

---

## EL BLOQUE DE CONTEXTO COMPACTO (para copiar en el teléfono)

Guardar esto en los favoritos o en notas del teléfono para acceso rápido:

```
Jardín Ideal | Montreal | 7M CAD 2026 | 514-266-2504
Paisajismo premium. Francés con clientes. Español interno.
FLOAT V2: gate 90/100. 5 piezas/día. Cal: Lun=Autoridad Mié=Transformación Vie=Oferta.
Copy: ≤8 palabras, declarativo, sin "meilleur" sin dato. Tipog: Playfair+Montserrat.
ICS: leads 0-100pts. A+=≥85, A=70-84, B=55-69, C=<55.
GitHub: daniel599679/jardin-ideal-ai rama master.
HOY: [completar]
```

---

*HOME WORKFLOW PROTOCOL v1.0 — Jardín Ideal*
*10_MEMORIA_EMPRESARIAL/HOME_WORKFLOW_PROTOCOL.md*
