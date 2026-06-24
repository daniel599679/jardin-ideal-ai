# README — SISTEMA DE PATCHES
**Automation Center — Jardín Ideal AI System**
**Versión:** 1.0 · **Fecha:** 2026-06-24

---

## ¿QUÉ ES UN PATCH?

Un patch es un cambio aplicado por Claude Code directamente sobre archivos locales del repositorio. A diferencia de Manus (que genera HTML nuevo), Claude Code aplica cambios quirúrgicos y precisos sobre archivos ya existentes.

Los patches son la herramienta principal para mantener los archivos locales actualizados sin necesidad de regenerar desde cero en Manus.

---

## TIPOS DE PATCH

| Tipo | Qué cambia | Archivos típicos |
|------|-----------|-----------------|
| `HTML_PATCH` | Estructura HTML, secciones, formularios | `*.html` |
| `JS_PATCH` | Funciones JavaScript, calculadoras, validaciones | `*.html` (inline JS) |
| `CSS_PATCH` | Estilos, colores, tipografía, layout | `*.html` (inline CSS) |
| `MD_PATCH` | Documentos de marca, reglas, prompts | `*.md` |
| `MULTI_PATCH` | Varios archivos simultáneamente | Múltiples |

---

## PROCESO DE APLICACIÓN DE UN PATCH

### Paso 1: Identificar archivos afectados

Claude Code busca en el repositorio todos los archivos que contienen el elemento a cambiar:

```
Búsqueda: [texto o patrón a cambiar]
Herramientas: Grep (búsqueda de contenido), Glob (búsqueda por nombre)
Resultado: Lista de archivos afectados con número de línea
```

### Paso 2: Leer el archivo completo

Antes de modificar, Claude Code lee el archivo completo para entender el contexto y no romper estructuras existentes.

```
Herramienta: Read
Riesgo mitigado: No aplicar cambio fuera de contexto
```

### Paso 3: Aplicar el cambio con Edit

Claude Code usa la herramienta `Edit` para reemplazos exactos. Nunca reescribe el archivo completo a menos que sea estrictamente necesario.

```
Herramienta: Edit (reemplazo exacto de string)
Regla: old_string debe ser único en el archivo
Regla: Preservar indentación exacta
Regla: No modificar nada fuera del old_string
```

### Paso 4: Generar reporte del patch

Después de aplicar, Claude Code documenta:
- Qué cambió
- En qué archivo(s)
- Número de línea(s) afectadas
- Texto anterior vs. nuevo
- Fecha y hora de aplicación

### Paso 5: Crear archivo de registro del patch

Guardar en `PATCHES/` un archivo con el historial:

```
PATCHES/YYYY-MM-DD_TIPO_DESCRIPCION.md
```

### Paso 6: Hacer commit y push

Cada patch exitoso se commitea inmediatamente:
```bash
git add [archivos modificados]
git commit -m "patch: [descripción breve]"
git push origin master
```

### Paso 7: Actualizar LOGS/CHANGELOG_AUTOMATION.md

Registrar la ejecución en el changelog de automatización.

### Paso 8: Mover comando a COMMANDS_DONE/

Si el patch viene de un comando en `COMMANDS_INBOX/`, moverlo a `COMMANDS_DONE/` después del commit exitoso.

---

## REGLAS ABSOLUTAS PARA PATCHES

### Lo que Claude Code PUEDE hacer sin aprobación:
- Aplicar cambios en archivos locales (HTML, MD, JS, CSS)
- Hacer commit y push del cambio al repositorio privado
- Generar reportes y diff de los cambios
- Actualizar documentos de registro y changelog

### Lo que Claude Code NUNCA hace sin aprobación:
- Publicar el archivo HTML en un servidor web
- Subir la landing a producción
- Activar campañas publicitarias
- Enviar emails o notificaciones a clientes
- Modificar configuración de Zapier directamente
- Modificar Meta Ads Manager directamente

---

## FORMATO DE ARCHIVO DE PATCH

```markdown
# PATCH — [descripción]
FECHA: YYYY-MM-DD HH:MM
TIPO: HTML_PATCH | JS_PATCH | CSS_PATCH | MD_PATCH | MULTI_PATCH
COMANDO_ORIGEN: [nombre del comando que generó este patch, si aplica]
ESTADO: APLICADO | FALLIDO | PARCIAL

## Archivos modificados

| Archivo | Líneas afectadas | Tipo de cambio |
|---------|-----------------|----------------|
| [ruta] | [línea(s)] | [inserción/reemplazo/eliminación] |

## Cambio aplicado

### Archivo: [ruta]
**Antes:**
```
[texto original]
```
**Después:**
```
[texto nuevo]
```

## Validación
- [ ] Archivo abre correctamente en navegador (si es HTML)
- [ ] No hay errores de sintaxis JS
- [ ] Estructura HTML válida
- [ ] Commit realizado: [hash]

## Notas
[observaciones, advertencias, próximos pasos]
```

---

## CONVENCIÓN DE NOMBRES DE ARCHIVOS PATCH

```
YYYY-MM-DD_TIPO_PROYECTO_DESCRIPCION.md
```

Ejemplos:
```
2026-06-24_HTML_PATCH_COUR_ARRIERE_LOI25_CHECKBOX.md
2026-06-24_MD_PATCH_GLOBAL_EMAIL_UPDATE.md
2026-07-01_JS_PATCH_COUR_ARRIERE_SUBMITFORM_ZAPIER.md
2026-07-15_MULTI_PATCH_ALL_LP_COPYRIGHT_2026.md
```

---

## VERIFICACIÓN POST-PATCH

Después de aplicar cualquier patch a un archivo HTML, verificar:

1. **Sintaxis HTML**: No etiquetas sin cerrar, no atributos rotos
2. **Sintaxis JavaScript**: Llaves balanceadas, no variables sin definir
3. **CSS**: No propiedades sin valor, no selectores rotos
4. **Contexto**: El cambio está en la sección correcta (no en comentarios, no en `<script>` cuando debería estar en `<style>`)
5. **Codificación**: Caracteres especiales franceses preservados (é, è, ê, à, ç, etc.)

---

## PATCH DE EMERGENCIA

Si un patch falla o rompe algo, el proceso de rollback es:

```bash
# Ver historial de commits
git log --oneline -10

# Revertir el último commit (manteniendo archivos editados para revisión)
git revert HEAD

# O restaurar un archivo específico a versión anterior
git checkout [hash-commit-anterior] -- [ruta-archivo]
```

**Siempre registrar el rollback en LOGS/CHANGELOG_AUTOMATION.md.**

---

*README Patches — Jardín Ideal Automation Center · v1.0 · 2026-06-24*
