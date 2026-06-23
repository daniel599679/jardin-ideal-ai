# SISTEMA DE VOZ — CLAUDE CODE
**Versión:** 1.0 | **Estado:** ✅ OPERATIVO | **Fecha:** 2026-06-23

---

## QUÉ HACE

Cada vez que Claude Code termina de responder, una voz en español lee en voz alta el final del mensaje.
Sin tocar el teclado. Sin mirar la pantalla. Sabes cuando Claude terminó.

---

## CONFIGURACIÓN ACTIVA

### Hook en `C:\Users\Daniel\.claude\settings.json`
```json
"hooks": {
  "Stop": [
    {
      "matcher": "",
      "hooks": [
        {
          "type": "command",
          "command": "python C:/Users/Daniel/.claude/speak.py"
        }
      ]
    }
  ]
}
```

**Nota crítica (Windows):** Usar forward slashes `/` en la ruta — no backslashes `\`.
Claude Code (Node.js) procesa `\U`, `\D`, `\.` como secuencias de escape JavaScript y corrompe la ruta.

---

## TECNOLOGÍAS

| Componente | Detalle |
|-----------|---------|
| Motor principal | `edge_tts` 7.2.8 — Microsoft Edge Neural TTS |
| Voz activa | `es-ES-ElviraNeural` — español España, femenino, natural |
| Motor fallback | Windows SAPI — Microsoft David/Zira Desktop (offline) |
| Reproductor | `System.Windows.Media.MediaPlayer` via PowerShell |
| Modo reproducción | Proceso separado (DETACHED) — no bloquea Claude Code |
| Requiere internet | Solo para edge_tts. Sin internet → SAPI automático |

---

## ARCHIVOS

| Archivo | Descripción |
|---------|-------------|
| `C:\Users\Daniel\.claude\speak.py` | Script principal del sistema de voz |
| `C:\Users\Daniel\.claude\settings.json` | Config de hooks de Claude Code |
| `C:\Users\Daniel\.claude\VOICE_SYSTEM_STATUS.md` | Documentación del sistema |
| `C:\Users\Daniel\.claude\HOOK_PATH_FIX_REPORT.md` | Reporte del bug de backslashes |

---

## CÓMO CAMBIAR LA VOZ

Editar `speak.py` línea 1:
```python
VOICE = "es-ES-ElviraNeural"    # actual
VOICE = "fr-CA-SylvieNeural"    # francés Quebec
VOICE = "es-MX-DaliaNeural"     # español México
VOICE = "es-ES-AlvaroNeural"    # español España masculino
```

---

## CÓMO DESACTIVAR TEMPORALMENTE

En `settings.json`, cambiar `"Stop"` por `"Stop_DISABLED"`.
Claude Code ignora eventos no reconocidos.

---

## PROBAR EL SISTEMA

```powershell
python C:/Users/Daniel/.claude/speak.py "Texto de prueba"
```

---

## BUG RESUELTO — 2026-06-23

**Error:** `Hook script appears to be missing` con ruta corrupta `UsersDaniel.claudespeak.py`
**Causa:** Node.js reinterpretaba `C:\Users\Daniel\.claude\speak.py` como template JS → eliminaba los backslashes → path relativo al CWD del proyecto
**Fix:** Cambiar `\\` por `/` en la ruta dentro de `settings.json`
**Documentación completa:** `C:\Users\Daniel\.claude\HOOK_PATH_FIX_REPORT.md`
