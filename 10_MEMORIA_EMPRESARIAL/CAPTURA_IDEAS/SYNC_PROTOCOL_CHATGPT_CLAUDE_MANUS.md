# PROTOCOLO DE SINCRONIZACIÓN — ChatGPT × Claude × Manus
**Cómo mantener contexto coherente en todas las herramientas de IA**
**Versión:** 1.0 | **Fecha:** 2026-06-23
**Objetivo:** Trabajar desde cualquier dispositivo o herramienta sin perder el hilo de lo que se está construyendo.

---

## EL PROBLEMA QUE RESUELVE ESTE PROTOCOLO

Cada sesión de IA empieza desde cero. Sin un protocolo, esto pasa:
- Le dices a Claude Web algo que ya sabe Claude Code → trabajo duplicado
- Manus produce contenido sin saber el estándar FLOAT V2 Premium → material que no sirve
- ChatGPT da consejos genéricos porque no sabe el contexto de Jardín Ideal
- Pierdes 10–15 minutos al inicio de cada sesión explicando el contexto

**La solución:** Un bloque de contexto estandarizado que se pega al inicio de cada sesión, específico para cada herramienta.

---

## BLOQUE DE CONTEXTO MAESTRO

Este es el contexto completo. Los bloques por herramienta son versiones compactas de este.

```
CONTEXTO JARDÍN IDEAL — [FECHA]

EMPRESA: Jardín Ideal | Montreal, Quebec, Canadá
OBJETIVO 2026: 7,000,000 CAD facturación
SERVICIOS: Cour Avant, Cour Arrière, Pavé-Uni, Balcons, Escaliers, Piscines (9 servicios)
IDIOMA CLIENTES: Francés (québécois) | IDIOMA INTERNO: Español
TELÉFONO CTA: 514-266-2504 | WEB: jardin-ideal.com
HORARIO: Lun-Vie 07:00-18:00 | REUNIÓN DIARIA: 09:00 AM fija

SISTEMAS ACTIVOS:
  FLOAT V2 Premium → 05_MARKETING/FLOAT_V2_PREMIUM/ (5 módulos + guardrails)
  Producción Continua → 05_MARKETING/PRODUCCION_CONTINUA/ (4 módulos)
  ICS (calificación leads) → score 0-100pts, perfiles A+/A/B/C
  Agentes: CRM, Marketing, Operaciones (con prompts completos)
  Memoria empresarial → 10_MEMORIA_EMPRESARIAL/

ESTÁNDARES DE CONTENIDO:
  Visual Score mínimo para publicar: 90/100 (gate absoluto)
  Tipografía: Playfair Display Bold Italic (headlines) + Montserrat (body)
  Paleta: #052B16 verde / #008E3F verde claro / #C8A45A dorado (solo teléfono) / #F5F2EB crema
  Copy: declarativo, ≤8 palabras en hook, sin "meilleur/qualité" sin dato concreto

CALENDARIO DE CONTENIDO:
  Lunes: Autoridad | Martes: Educación | Miércoles: Transformación
  Jueves: Prueba Social | Viernes: Oferta | Sáb: BTS | Dom: Inspiración

ÚLTIMO COMMIT GITHUB: [insertar hash del último commit]
REPOSITORIO: https://github.com/daniel599679/jardin-ideal-ai.git rama master

LO QUE SE ESTÁ CONSTRUYENDO AHORA: [insertar tarea actual de PROXIMOS_PASOS.md]
```

---

## BLOQUE POR HERRAMIENTA

### CHATGPT — Bloque de contexto

```
USAR CHATGPT PARA:
  ✓ Brainstorming de ángulos creativos (sin restricciones de contexto del sistema)
  ✓ Investigación de competidores (Techo-Bloc, Permacon, paysagistas premium QC)
  ✓ Redacción de variantes de copy para A/B testing
  ✓ Generación de ideas de contenido educativo
  ✓ Análisis de tendencias de paisajismo en Quebec
  ✗ NO usar para modificar archivos del sistema (no tiene acceso)
  ✗ NO usar para producción de agentes o prompts del ecosistema

BLOQUE DE INICIO PARA CHATGPT (copiar y pegar al inicio):
---
Contexto: Trabajo para Jardín Ideal, empresa de paisajismo premium en Montreal, Quebec.
Objetivo 2026: 7 millones CAD. Mercado: propietarios 35-65 años, francófonos, ingresos medios-altos.
Servicios: Cour avant, cour arrière, pavé-uni, balcons, escaliers, piscines.
Idioma con clientes: francés québécois. Idioma interno: español.
Posicionamiento: nivel Techo-Bloc / Architectural Digest. No somos económicos. Somos premium.
CTA siempre: 514-266-2504. Teléfono en dorado. Sin precios en copy orgánico.
Copy: declarativo, ≤8 palabras en hook, voz austera (sin signos de exclamación, sin "meilleur" sin dato).
[Añadir: qué necesitas específicamente hoy]
---

CIERRE DE SESIÓN CHATGPT:
  Al terminar, copiar el output más valioso
  → Pegarlo en IDEA_INBOX.md si es una idea nueva
  → Pegarlo en el archivo correspondiente del sistema si es copy listo para usar
```

---

### CLAUDE WEB — Bloque de contexto

```
USAR CLAUDE WEB PARA:
  ✓ Sesiones largas de análisis y síntesis (sin límite de contexto visible)
  ✓ Revisión de documentos completos
  ✓ Generación de contenido complejo (reels, scripts, prompts)
  ✓ Sesiones estratégicas que no requieren modificar archivos
  ✓ Colaboración móvil (desde el teléfono)
  ✗ NO usar para editar archivos del sistema (no tiene acceso al filesystem)

BLOQUE DE INICIO PARA CLAUDE WEB (copiar y pegar):
---
Eres el asistente de operaciones de Jardín Ideal (Montreal, Quebec, Canadá).
Empresa de paisajismo premium. Objetivo: 7M CAD en 2026.
Idioma interno: español. Idioma con clientes: francés québécois.
Teléfono CTA: 514-266-2504. Posicionamiento: Techo-Bloc / Architectural Digest level.
Sistema de producción: FLOAT V2 Premium (gate visual 90/100 para publicar).
Calendario: Lun=Autoridad, Mar=Educación, Mié=Transformación, Jue=Prueba Social, Vie=Oferta.
Copy: hook ≤8 palabras, declarativo, sin "meilleur/qualité" sin dato concreto.
Tipografía: Playfair Display Bold Italic (headlines) + Montserrat (body/CTA).
Colores: #052B16 verde / #008E3F / #C8A45A dorado (solo teléfono) / #F5F2EB / #FFFFFF.

Hoy es [FECHA]. Última sesión: [qué se hizo]. Hoy necesito: [tarea específica].
---

CIERRE DE SESIÓN CLAUDE WEB:
  Antes de terminar, pedirle a Claude:
  "Genera un bloque de resumen de esta sesión para pegar en ESTADO_ACTUAL_ECOSISTEMA.md"
  Copiar ese resumen y actualizarlo en el sistema en la próxima sesión de Claude Code
```

---

### CLAUDE DESKTOP — Bloque de contexto

```
USAR CLAUDE DESKTOP PARA:
  ✓ Sesiones de trabajo diario completo (tiene CLAUDE.md para contexto permanente)
  ✓ Acceso a herramientas MCP (si están configuradas: Drive, Calendar, etc.)
  ✓ Revisión de archivos locales (puede leer archivos del sistema)
  ✓ Producción de contenido con acceso a la identidad visual
  ✓ Ejecutar el START_DAY_PROTOCOL diariamente

VENTAJA CLAUDE DESKTOP: Si tienes CLAUDE.md en la raíz del proyecto, Claude Desktop
lo lee automáticamente al inicio de cada sesión → contexto persistente sin pegar bloque.

CONFIGURAR CLAUDE.MD (hacer una vez):
  Crear: C:\Users\Daniel\Desktop\Jardin-ideal-AI\Jardin_Ideal_AI_System\CLAUDE.md
  Contenido: el Bloque de Contexto Maestro de este documento

BLOQUE DE INICIO CLAUDE DESKTOP (si no hay CLAUDE.md):
  → Usar el mismo bloque que Claude Web (son el mismo modelo)

CIERRE DE SESIÓN CLAUDE DESKTOP:
  "Actualiza los archivos de memoria que correspondan con lo que hicimos hoy"
  Claude Desktop puede editar los archivos directamente con MCP filesystem
```

---

### CLAUDE CODE — Bloque de contexto

```
USAR CLAUDE CODE PARA:
  ✓ TODO lo que implica crear, editar o eliminar archivos del sistema
  ✓ Git commits y push a GitHub
  ✓ Modificar agentes, prompts y automatizaciones
  ✓ Crear nuevos módulos del sistema
  ✓ Sincronización al final del día (actualizar archivos de memoria + commit)

VENTAJA CLAUDE CODE: Lee automáticamente los archivos de memoria al inicio de la sesión
(settings.json tiene configurado el hook de voz y el contexto del proyecto).

NO NECESITA BLOQUE MANUAL: Claude Code tiene acceso directo al filesystem y lee
los archivos del proyecto. Pero si el contexto está disperso, usar:

INSTRUCCIÓN DE ORIENTACIÓN (inicio de sesión):
  "Lee 10_MEMORIA_EMPRESARIAL/ESTADO_ACTUAL_ECOSISTEMA.md y
   10_MEMORIA_EMPRESARIAL/PROXIMOS_PASOS.md y dime qué hay que hacer hoy."

CIERRE DE SESIÓN CLAUDE CODE (obligatorio — crea el registro):
  "Al terminar:
   1. Actualiza ESTADO_ACTUAL_ECOSISTEMA.md con lo que hicimos
   2. Actualiza PROXIMOS_PASOS.md con los próximos pasos
   3. Haz commit y push a GitHub
   4. Genera el bloque de resumen para la próxima sesión"
```

---

### MANUS — Bloque de contexto

```
USAR MANUS PARA:
  ✓ Ejecución de tareas con herramientas externas (navegador, apps, APIs)
  ✓ Producción de reels con ffmpeg (usar PROMPT_MANUS_VIDEO.txt del paquete de producción)
  ✓ Subir contenido a plataformas (Meta, Drive, etc.)
  ✓ Automatizaciones que requieren hacer clic y navegar
  ✓ Tareas de larga duración que no requieren supervisión constante

MANUS NO TIENE MEMORIA PERSISTENTE → siempre iniciar con el contexto completo

BLOQUE DE INICIO PARA MANUS (copiar y pegar al inicio):
---
Empresa: Jardín Ideal (paisajismo premium Montreal, Quebec).
GitHub: https://github.com/daniel599679/jardin-ideal-ai.git rama master
Idioma clientes: francés. Idioma interno: español.
Teléfono siempre en dorado #C8A45A: 514-266-2504.
Standard visual mínimo: 90/100 (FLOAT V2 Premium).
Audio reels: -14 LUFS (estándar Instagram).
Tipografía: Playfair Display Bold Italic + Montserrat.
Colores: #052B16 / #008E3F / #C8A45A / #F5F2EB / #FFFFFF.

TAREA DE HOY: [descripción exacta de lo que debe hacer Manus]
ARCHIVOS NECESARIOS: [rutas exactas de los archivos que debe usar]
OUTPUT ESPERADO: [qué debe producir y dónde guardarlo]
---

CÓMO ENVIAR TAREAS A MANUS (formato óptimo):
  Tarea: [verbo + objeto + destino]
  Archivos de entrada: [rutas]
  Output esperado: [formato + destino]
  Ejemplo:
    "Produce el reel del proyecto Puschak usando el paquete en:
     CONTENIDO_PARA_PUBLICAR/COUR_AVANT/PUSCHAK/2_REEL_CAPCUT/3_PROMPT_MANUS_VIDEO.txt
     Output: archivo MP4 en la carpeta raíz del proyecto.
     Audio: -14 LUFS. Formato: 9:16, 1080×1920, MP4 H.264."

CIERRE SESIÓN MANUS:
  "Cuando termines, sube el output a Drive en la carpeta [X] y notifica el link."
```

---

## PROTOCOLO DE SINCRONIZACIÓN AL DÍA SIGUIENTE

### Al inicio de cada día (07:30 AM)

```
PASO 1 (2 min): Revisar IDEA_INBOX.md
  → ¿Hay ideas nuevas de ayer que no se procesaron? Clasificarlas.

PASO 2 (3 min): Leer ESTADO_ACTUAL_ECOSISTEMA.md
  → ¿Qué cambió ayer? ¿Hay algo bloqueado?

PASO 3 (2 min): Leer PROXIMOS_PASOS.md
  → ¿Cuál es la P1 de hoy?

PASO 4 (3 min): Generar DAILY_CONTENT_QUEUE del día
  → ¿Hay material ≥90/100 para el Hero?
  → Completar la plantilla de las 5 piezas

PASO 5 (5 min): Revisar WhatsApp propio / notas de voz
  → ¿Hay mensajes marcados con "IDEA:" de ayer? Capturarlos en IDEA_INBOX.md.

TOTAL: 15 minutos de orientación antes de la reunión de las 09:00
```

### Al final de cada día (17:30 – 18:00)

```
EN CLAUDE CODE:
  "Sesión de cierre: actualiza ESTADO_ACTUAL_ECOSISTEMA.md,
   PROXIMOS_PASOS.md e IDEA_INBOX.md con lo de hoy.
   Haz commit y push."

ANTES DE CERRAR EL LAPTOP:
  Preguntar: "¿Hay algo que aprendí hoy que debo capturar como idea?"
  Si sí → agregar al IDEA_INBOX (10 segundos, no 10 minutos)
```

---

## TABLA RESUMEN — QUÉ HACE CADA HERRAMIENTA

| Herramienta | Fortaleza | Debilidad | Cuándo usarla |
|-------------|-----------|-----------|---------------|
| ChatGPT | Creatividad, research, variantes | Sin memoria, sin acceso al sistema | Brainstorming, investigación |
| Claude Web | Análisis largo, síntesis, móvil | Sin acceso al filesystem | Sesiones estratégicas, trabajo móvil |
| Claude Desktop | MCP tools, CLAUDE.md persistente | Menos potente que Code en filesystem | Trabajo diario con herramientas externas |
| Claude Code | Acceso completo al filesystem, git | Requiere laptop | TODO lo que modifica el sistema |
| Manus | Automatización con herramientas externas | Sin memoria, requiere contexto completo | Producción de video, uploads, automatizaciones |

---

*SYNC PROTOCOL v1.0 — ChatGPT × Claude × Manus — Jardín Ideal*
*10_MEMORIA_EMPRESARIAL/CAPTURA_IDEAS/SYNC_PROTOCOL_CHATGPT_CLAUDE_MANUS.md*
