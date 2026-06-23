# ECOSISTEMA DE MEMORIA UNIFICADA V1
**Versión:** 1.0 | **Fecha:** 2026-06-23
**Propósito:** Sincronizar el contexto de Jardín Ideal entre todas las herramientas de IA.

---

## EL PROBLEMA QUE RESUELVE

Sin este sistema, cada conversación empieza desde cero:
- "¿Cuáles son tus servicios?" — décima vez que se responde
- "¿Cuál era el plan de contenido?" — perdido en el hilo anterior
- "¿Qué decidimos sobre el sistema de leads?" — nadie recuerda

Con este sistema: **cualquier IA, en cualquier herramienta, puede tomar el contexto completo en 2 minutos.**

---

## ARQUITECTURA DE MEMORIA

```
MEMORIA
  │
  ├── REPOSITORIO GIT (fuente de verdad)
  │     Jardin_Ideal_AI_System/10_MEMORIA_EMPRESARIAL/
  │     ↑ Todo lo que se hace se sube aquí
  │
  ├── CLAUDE CODE (memoria automática)
  │     Lee el repositorio directamente
  │     Tiene historial de sesión persistente
  │     Hook de voz activo
  │
  ├── CLAUDE DESKTOP (memoria semi-automática)
  │     Lee archivos del repositorio con herramientas
  │     Requiere indicar el path al inicio
  │
  ├── CLAUDE WEB (memoria manual)
  │     Contexto pegado al inicio de sesión
  │     Sin acceso directo a archivos locales
  │
  ├── MANUS (memoria manual con guía)
  │     Guía específica en 10_MANUS/
  │     Puede acceder a archivos si se configuran
  │
  └── CHATGPT (memoria manual)
        Contexto pegado al inicio de sesión
        Memory de OpenAI si está activada
```

---

## FUENTE DE VERDAD: EL REPOSITORIO GIT

El repositorio local es siempre la fuente de verdad.
**Ruta:** `C:\Users\Daniel\Desktop\Jardin-ideal-AI\Jardin_Ideal_AI_System\`
**GitHub:** Sincronizado vía `git push`

**Regla:** Si hay conflicto entre lo que dice un chat y lo que dice el repo → el repo gana.

---

## CÓMO SINCRONIZA CADA HERRAMIENTA

### CLAUDE CODE

**Tipo de memoria:** Persistente automática dentro del proyecto
**Cómo funciona:**
- Acceso directo a todos los archivos del repositorio
- Historial de sesión conservado en `.claude/projects/`
- Hook de voz activado (notificación de audio al terminar)
- Lee `MEMORIA_GLOBAL.md` si se le pide

**Setup al iniciar:** Ninguno. El contexto está disponible.

**Al terminar sesión:**
```bash
git add 10_MEMORIA_EMPRESARIAL/
git commit -m "Actualizar memoria - [fecha]"
git push
```

---

### CLAUDE DESKTOP

**Tipo de memoria:** Semi-automática — accede a archivos locales con herramientas
**Cómo funciona:**
- Puede leer archivos con la herramienta de lectura
- No tiene historial entre sesiones por defecto
- Puede acceder al repositorio completo si se le indica el path

**Setup al iniciar:**
```
"Lee el archivo:
C:\Users\Daniel\Desktop\Jardin-ideal-AI\Jardin_Ideal_AI_System\10_MEMORIA_EMPRESARIAL\MEMORIA_GLOBAL.md
Luego lee ESTADO_ACTUAL_ECOSISTEMA.md y PROXIMOS_PASOS.md del mismo directorio."
```

**Al terminar sesión:**
- Pedir a Claude que actualice los archivos de memoria correspondientes
- Commit y push manual o vía Claude Code

---

### CLAUDE WEB

**Tipo de memoria:** Manual — contexto pegado
**Cómo funciona:**
- No tiene acceso a archivos locales (a menos que se compartan)
- El contexto debe pegarse al inicio de cada sesión
- La memoria de Claude.ai puede guardar información de usuario (limitada)

**Setup al iniciar:**
```
Copiar y pegar el contenido de MEMORIA_GLOBAL.md como primer mensaje:

"Eres el asistente del sistema Jardín Ideal. Aquí está el contexto completo:
[CONTENIDO DE MEMORIA_GLOBAL.md]

Sesión de hoy: [tipo de sesión]
Objetivo: [objetivo específico]"
```

**Al terminar sesión:**
- Copiar cualquier archivo generado → guardarlo en el repositorio
- Actualizar archivos de memoria manualmente
- Git commit + push

---

### MANUS

**Tipo de memoria:** Manual con guía estructurada
**Cómo funciona:**
- Tiene acceso a archivos si se configuran correctamente
- Guía específica de operación en `10_MANUS/`
- Sesiones especiales documentadas en `10_MANUS/sesiones_especiales.md`

**Setup al iniciar:**
```
1. Compartir MEMORIA_GLOBAL.md como contexto inicial
2. Indicar tipo de sesión: "sesion_diaria" o nombre de sesión especial
3. Cargar: 10_MANUS/sesion_diaria.md (o la sesión especial correspondiente)
```

**Al terminar sesión:**
- Guardar outputs en las carpetas correspondientes del repositorio
- Actualizar HISTORIAL_CAMBIOS.md
- Git commit + push

---

### CHATGPT

**Tipo de memoria:** Manual + Memory de OpenAI (si está activada)
**Cómo funciona:**
- Contexto pegado al inicio o guardado en Instrucciones Personalizadas
- Memory de OpenAI puede retener información entre sesiones (variable)

**Setup en Instrucciones Personalizadas (una sola vez):**
```
Soy Daniel, opero Jardín Ideal, empresa de paisajismo en Montreal.
Objetivo 2026: 7M CAD.
Sistema IA activo con: FLOAT (fábrica de contenido), ICS (calificación de leads), Brand Style Guide.
Idioma interno: español. Clientes: francés.
Reunión diaria inamovible: 09:00 AM.
Prioridad: ventas → eficiencia → documentación.
```

**Al iniciar sesión de trabajo profundo:**
```
[Pegar contenido de MEMORIA_GLOBAL.md]
[Pegar contenido de ESTADO_ACTUAL_ECOSISTEMA.md]
```

---

## JERARQUÍA DE HERRAMIENTAS

```
TAREA                           HERRAMIENTA RECOMENDADA
─────────────────────────────────────────────────────
Crear/editar archivos del repo  → Claude Code (acceso directo)
Trabajo de contenido (fotos/video) → Manus (control de pantalla)
Estrategia + planificación      → Claude Web (sin límite de contexto)
Análisis rápido de un archivo   → Claude Desktop
Respuestas de texto / copy      → ChatGPT o Claude Web
```

---

## PROTOCOLO DE SINCRONIZACIÓN

### Diariamente
1. Sesión inicia → leer `MEMORIA_GLOBAL.md` + `PROXIMOS_PASOS.md`
2. Sesión termina → actualizar `ESTADO_ACTUAL_ECOSISTEMA.md` + git push

### Por sesión de trabajo
1. Antes de empezar → verificar `PROXIMOS_PASOS.md`
2. Al terminar → actualizar `HISTORIAL_CAMBIOS.md` + git commit

### Semanalmente
1. Revisar `PROYECTOS_ACTIVOS.md` — ¿hay algo que cambió de estado?
2. Revisar `DECISIONES_ESTRATEGICAS.md` — ¿hay nuevas decisiones que documentar?
3. Revisar `APRENDIZAJES_Y_ERRORES.md` — ¿hay nuevos aprendizajes?

---

## LO QUE NUNCA DEBE PERDERSE

Estos 3 archivos contienen el 80% del contexto necesario para cualquier sesión:

```
1. MEMORIA_GLOBAL.md           → Quiénes somos + todos los sistemas
2. ESTADO_ACTUAL_ECOSISTEMA.md → Dónde estamos hoy
3. PROXIMOS_PASOS.md           → Qué hacemos mañana
```

Si solo puedes leer uno: leer `MEMORIA_GLOBAL.md`.

---

## VERSIÓN COMPACTA DEL CONTEXTO (para pegar en cualquier IA)

```
JARDÍN IDEAL — CONTEXTO RÁPIDO
Empresa de paisajismo, Montreal, Quebec. Objetivo 2026: 7M CAD.
9 servicios: Cour Avant/Arrière, Pavé-Uni, Balcons, Clôtures, Piscines, Escaliers, Murs, Rénov.
Idioma interno: español. Clientes: francés.
Teléfono CTA: 514-266-2504.

SISTEMAS ACTIVOS:
- FLOAT V1: protocolo de contenido 60 min por proyecto
- Brand Style Guide: #052B16 / #008E3F / #C8A45A (solo CTA) / #F5F2EB
- ICS: calificación de leads 0–100 pts. Perfiles A+/A/B/C.
- Agentes: CRM, Marketing, Operaciones, Reportes, Automatizaciones

REGLAS:
- Reunión 09:00 AM inamovible
- Nunca visitar lead sin ambos tomadores de decisión
- Prioridad: ventas → eficiencia → documentación
- Git commit al finalizar cada bloque de trabajo
```
