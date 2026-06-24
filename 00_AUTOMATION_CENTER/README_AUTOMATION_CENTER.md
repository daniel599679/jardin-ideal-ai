# AUTOMATION CENTER — Jardín Ideal AI System
**Versión:** 1.0 · **Creado:** 2026-06-24
**Propósito:** Centro de control de automatización para proyectos Manus y landing pages

---

## ¿QUÉ ES ESTE CENTRO?

El Automation Center es el sistema de control que permite a **Claude Code** actuar como **fuente de verdad** sobre todos los proyectos de Jardín Ideal: landing pages, piezas de contenido, campañas, y documentos de marca.

En lugar de depender únicamente de chats manuales con Manus, este centro define:
- Qué cambios aplicar (COMMANDS_INBOX)
- Qué proyectos existen y en qué estado están (PROJECT_REGISTRY)
- Qué cambios requieren revisión humana antes de aplicarse (APPROVAL_REQUIRED)
- Cómo aplicar cambios técnicos sobre archivos locales (PATCHES)
- Historial completo de todo lo ejecutado (LOGS)

---

## ARQUITECTURA DEL SISTEMA

```
Claude Code / GitHub
      │
      ▼
00_AUTOMATION_CENTER/           ← Centro de control
├── COMMANDS_INBOX/             ← Comandos pendientes de ejecutar
├── COMMANDS_DONE/              ← Comandos ejecutados exitosamente
├── COMMANDS_FAILED/            ← Comandos fallidos (con razón)
├── PROJECT_REGISTRY/           ← Registro de proyectos activos
├── APPROVAL_REQUIRED/          ← Cola de aprobaciones humanas
├── PATCHES/                    ← Diffs y scripts de cambio
└── LOGS/                       ← Historial de automatizaciones

      │                               │
      ▼                               ▼
Archivos locales              Manus (prototipado)
(fuente de verdad)            (editor visual)
```

---

## PRINCIPIOS DEL SISTEMA

| Principio | Detalle |
|-----------|---------|
| **Fuente de verdad** | Claude Code + GitHub. Ningún archivo publicado sin pasar por aquí. |
| **Manus = editor visual** | Manus prototipa y genera HTML. Claude Code aplica correcciones técnicas. |
| **No publicar sin aprobación** | Todo contenido para clientes requiere revisión humana. |
| **No inventar datos** | Pixel ID, webhook, garantías, precios: solo datos confirmados. |
| **Idioma interno** | Español (documentación, comandos, registros). |
| **Idioma cliente** | Francés (todo resultado final visible al público). |

---

## FLUJO DE TRABAJO ESTÁNDAR

### Para cambios técnicos (email, garantías, textos legales)

```
1. Crear comando en COMMANDS_INBOX/
2. Claude Code lee el comando
3. Claude Code identifica archivos afectados
4. Claude Code aplica cambios localmente (PATCHES)
5. Claude Code genera reporte de cambios
6. Claude Code hace commit + push
7. Comando se mueve a COMMANDS_DONE/
8. Si requiere publicación → entra a APPROVAL_REQUIRED/
```

### Para cambios visuales / rediseños

```
1. Claude Code genera paquete de contexto (PAQUETES_CONTEXT_MANUS)
2. Manus recibe el paquete + prompt específico
3. Manus genera HTML/imagen/video
4. Resultado va a 00_INBOX_MANUS/
5. Claude Code audita el resultado
6. Si OK → APPROVAL_REQUIRED/ para publicación
```

---

## SUBCARPETAS — PROPÓSITO

| Carpeta | Quién escribe | Quién lee | Propósito |
|---------|--------------|-----------|-----------|
| `COMMANDS_INBOX/` | Daniel / Claude | Claude Code | Comandos de cambio a ejecutar |
| `COMMANDS_DONE/` | Claude Code | Daniel | Historial de comandos ejecutados |
| `COMMANDS_FAILED/` | Claude Code | Daniel | Comandos que fallaron con diagnóstico |
| `PROJECT_REGISTRY/` | Claude Code | Daniel / Manus | Registro de proyectos activos |
| `APPROVAL_REQUIRED/` | Claude Code | Daniel | Cola de aprobaciones antes de publicar |
| `PATCHES/` | Claude Code | Daniel / Manus | Diffs y cambios aplicados |
| `LOGS/` | Claude Code | Daniel | Historial de ejecuciones |

---

## REGLAS ABSOLUTAS

1. **No publicar** ninguna landing page sin aprobación humana explícita.
2. **No activar campañas** sin validar: Zapier webhook, Pipedrive, Meta Pixel activo, formulario funcional.
3. **No inventar**: Pixel ID, URL webhook, garantías no confirmadas, precios exactos no acordados, texto legal modificado sin revisión.
4. **Siempre hacer commit** después de aplicar un cambio local.
5. **Mover el comando** de INBOX → DONE después de ejecutar exitosamente.
6. **Mover el comando** de INBOX → FAILED si hay error, con diagnóstico adjunto.
7. **No eliminar archivos de referencia** sin crear un backup o nota en LOGS.

---

## ESTADO DEL SISTEMA

| Componente | Estado |
|-----------|--------|
| Estructura de carpetas | ✅ Creada 2026-06-24 |
| Project Registry | ✅ LP Cour Arrière V1 registrada |
| Primer comando | ✅ UPDATE_GLOBAL_CONTACT_AND_PAVE_WARRANTY |
| Integración Zapier | ⏳ Pendiente (webhook URL) |
| Integración Meta Pixel | ⏳ Pendiente (Pixel ID) |
| Integración Pipedrive auto | ⏳ Pendiente |

---

*Automation Center — Jardín Ideal AI System · v1.0 · 2026-06-24*
