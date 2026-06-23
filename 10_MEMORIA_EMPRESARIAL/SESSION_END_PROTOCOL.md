# PROTOCOLO DE CIERRE DE SESIÓN
**Para:** Claude Web / Claude Desktop / Claude Code / Manus / ChatGPT
**Objetivo:** Garantizar que el sistema quede sincronizado y la próxima sesión pueda empezar sin fricción.

---

## PASO 1 — ACTUALIZAR ESTADO DEL ECOSISTEMA

Abrir `10_MEMORIA_EMPRESARIAL/ESTADO_ACTUAL_ECOSISTEMA.md` y actualizar:

```
☐ Cambiar estado de tareas completadas: 🔴 → ✅
☐ Cambiar estado de tareas iniciadas: 🔴 → 🟡
☐ Actualizar la sección "ÚLTIMA SESIÓN" con lo realizado hoy
☐ Actualizar la fecha de última actualización
```

---

## PASO 2 — ACTUALIZAR PRÓXIMOS PASOS

Abrir `10_MEMORIA_EMPRESARIAL/PROXIMOS_PASOS.md` y actualizar:

```
☐ Eliminar o tachar tareas completadas
☐ Agregar nuevas tareas identificadas durante la sesión
☐ Reordenar prioridades si cambió el contexto
☐ Actualizar la fecha
```

---

## PASO 3 — REGISTRAR CAMBIOS EN EL HISTORIAL

Abrir `10_MEMORIA_EMPRESARIAL/HISTORIAL_CAMBIOS.md` y agregar entrada:

```markdown
## [FECHA] — [Descripción en una línea]

### Sistemas creados
| Archivo | Descripción |

### Sistemas modificados
| Archivo | Cambio |

### Git
| Commit | Descripción |

### Notas
[Contexto relevante para la próxima sesión]
```

---

## PASO 4 — REGISTRAR APRENDIZAJES (si aplica)

Si durante la sesión se descubrió un error, una solución no obvia, o una decisión importante:

Abrir `10_MEMORIA_EMPRESARIAL/APRENDIZAJES_Y_ERRORES.md` y agregar entrada.

---

## PASO 5 — GIT COMMIT Y PUSH

```bash
# En Claude Code:
git add [archivos modificados o creados hoy]
git commit -m "Descripción clara de lo que se hizo"
git push
```

**Frecuencia:** Al menos una vez por sesión. Idealmente al finalizar cada bloque de trabajo.

**Archivos que NUNCA van a Git:**
- `*.mp4`, `*.mov`, `*.zip` (binarios pesados)
- `.claude.json`, `.gitconfig` (configuración privada)
- Archivos de `00_DATOS_REALES/` (datos de clientes)

---

## PASO 6 — RESUMEN DE SESIÓN

Producir un resumen en este formato antes de cerrar:

```
RESUMEN DE SESIÓN — [FECHA]
━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ COMPLETADO HOY:
  - [lista de lo terminado]

🟡 EN PROGRESO:
  - [lista de lo iniciado pero no terminado]

📋 PRÓXIMA SESIÓN DEBE:
  - [tarea #1 prioritaria]
  - [tarea #2]
  - [tarea #3]

⚠️ NOTAS PARA EL SIGUIENTE CLAUDE:
  - [cualquier contexto que no esté en los archivos]
```

---

## CHECKLIST COMPLETO DE CIERRE

```
☐ ESTADO_ACTUAL_ECOSISTEMA.md actualizado
☐ PROXIMOS_PASOS.md actualizado
☐ HISTORIAL_CAMBIOS.md con la entrada de hoy
☐ Aprendizajes registrados (si aplica)
☐ Git commit realizado
☐ Git push al repositorio
☐ Resumen de sesión producido
```

---

## PARA SESIONES EN CLAUDE WEB / CHATGPT / MANUS

Al no tener memoria persistente automática, es crucial:

1. **Exportar el resumen de sesión** y guardarlo en `10_MEMORIA_EMPRESARIAL/HISTORIAL_CAMBIOS.md`
2. **Descargar / copiar** cualquier archivo generado y añadirlo al repositorio
3. **Actualizar manualmente** los archivos de estado en Git

---

## TIEMPO ESTIMADO DE CIERRE

| Tarea | Tiempo |
|-------|--------|
| Actualizar ESTADO_ACTUAL_ECOSISTEMA.md | 3 min |
| Actualizar PROXIMOS_PASOS.md | 2 min |
| Entrada en HISTORIAL_CAMBIOS.md | 2 min |
| Git commit + push | 1 min |
| Resumen de sesión | 2 min |
| **Total** | **~10 min** |
