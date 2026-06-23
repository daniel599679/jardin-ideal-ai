# APRENDIZAJES Y ERRORES
**Última actualización:** 2026-06-23
**Propósito:** No repetir los mismos errores. No debatir decisiones ya resueltas.

---

## ERRORES TÉCNICOS RESUELTOS

### AE-001 — Backslashes en rutas de hooks Windows
**Fecha:** 2026-06-23
**Error:** Hook de voz mostraba "Hook script appears to be missing" con ruta corrupta `UsersDaniel.claudespeak.py`
**Causa raíz:** Claude Code (Node.js) procesa el path `C:\Users\Daniel\.claude\speak.py` como string JS, tratando `\U`, `\D`, `\.` como secuencias de escape → resultado: `C:UsersDaniel.claudespeak.py` → ruta relativa que no existe.
**Solución:** Usar `/` en lugar de `\` en rutas de hooks. Python acepta ambos en Windows.
**Regla:** Todo script en hooks de Claude Code en Windows → rutas con forward slashes.
**Documentación:** `HOOK_PATH_FIX_REPORT.md`

---

### AE-002 — GitHub rechaza archivos >100MB
**Fecha:** 2026-06-23
**Error:** Push fallaba por archivos ZIP (319MB) y videos MP4 (185MB, 73MB, 48MB)
**Causa:** GitHub tiene límite de 100MB por archivo y 2GB por repositorio
**Solución:** Agregar `*.mp4`, `*.mov`, `*.zip` al `.gitignore` antes del commit
**Regla:** El contenido audiovisual NUNCA va a Git. Usar Google Drive o similar.
**Archivo:** `.gitignore`

---

### AE-003 — speak.py solo aceptaba stdin, no argumentos CLI
**Fecha:** 2026-06-23
**Error:** `python speak.py "Texto"` no funcionaba — el script solo procesaba JSON por stdin
**Causa:** El script original solo tenía Modo 2 (hook stdin)
**Solución:** Agregar `MODE 1` al inicio de `main()`: si `sys.argv >= 2`, usar ese texto directamente
**Regla:** Los scripts de hook deben funcionar también como CLI para facilitar pruebas

---

### AE-004 — Sleep fijo de 25 segundos en speak.py
**Fecha:** 2026-06-23
**Error:** El script esperaba 25 segundos aunque el texto tuviera 3 palabras
**Causa:** Sleep fijo sin considerar longitud del texto
**Solución:** Función `estimate_duration()`: `max(3, int(palabras × 0.46) + 2)`, cap a 30 seg
**Regla:** Los timers de audio deben ser dinámicos según la longitud del contenido

---

## APRENDIZAJES DE PROCESO

### AP-001 — Los sistemas ejecutables valen más que la documentación perfecta
**Aprendizaje:** Es mejor un sistema de calificación de leads que un equipo puede usar mañana que un framework de 50 páginas que nadie lee.
**Aplicado en:** ICS — el Lead Intelligence Report es de una página, no un PDF de 20.

---

### AP-002 — El protocolo de 60 minutos fuerza las decisiones
**Aprendizaje:** Al definir que cada proyecto debe producir contenido en 60 minutos, se eliminan las "sesiones de creatividad sin fin". El constraint de tiempo es la disciplina.
**Aplicado en:** Content Operating System — todos los servicios tienen protocolo exacto.

---

### AP-003 — El dorado escaso vale más
**Aprendizaje:** Cuando un color se usa en todos lados, pierde poder de llamada a la acción. Reservar el dorado `#C8A45A` exclusivamente para el CTA de teléfono crea condicionamiento: el cliente asocia ese color con "llamar".
**Aplicado en:** Brand Style Guide — regla irrompible.

---

### AP-004 — Visitas sin ambos decisores = tasa de cierre cercana a cero
**Aprendizaje:** En servicios de renovación residencial, la decisión es siempre de la pareja. Si solo está uno, el otro siempre "necesita verlo" → segunda visita → enfriamiento → pérdida.
**Aplicado en:** ICS — regla absoluta de no visitar sin ambos tomadores de decisión.

---

### AP-005 — Forward slashes en Windows como estándar
**Aprendizaje:** En cualquier configuración JSON, YAML o script que corra en Windows a través de Node.js, Python u otras herramientas, preferir `/` sobre `\` para máxima compatibilidad.
**Python:** Acepta ambos. **Node.js JSON paths:** A veces procesa `\` como escape. **URLs:** Solo `/`.

---

### AP-006 — Commits frecuentes previenen pérdida de trabajo
**Aprendizaje:** El primer commit de la sesión fue con 141 archivos de múltiples fechas. Si hubiera faltado un archivo o el push hubiera fallado, se habría perdido trabajo de semanas.
**Regla:** Commit al finalizar cada bloque de trabajo — no solo al final del día.

---

## PREGUNTAS QUE NO DEBEN REPETIRSE

| Pregunta | Respuesta consolidada |
|----------|----------------------|
| ¿Backslashes o forward slashes en hooks? | Forward slashes siempre en Windows |
| ¿Videos en Git? | No. Gitignore permanente. |
| ¿Dorado `#C8A45A` en títulos? | No. Solo CTA de teléfono. |
| ¿Visitar lead sin pareja? | No. Reagendar siempre. |
| ¿Crear contenido sin protocolo COS? | No. 60 minutos o no se hace. |
| ¿Cuál es el idioma interno del sistema? | Español. Siempre. |
