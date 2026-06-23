# HISTORIAL DE CAMBIOS
**Propósito:** Registro cronológico de todos los cambios al ecosistema.
**Regla:** Cada sesión de trabajo que produce cambios debe agregar una entrada aquí.

---

## 2026-06-23 — Sesión de construcción FLOAT V1 + Memoria

### Sistemas creados
| Archivo | Descripción |
|---------|-------------|
| `FLOAT_V2_ROADMAP.md` | Roadmap de 7 módulos para evolución de la fábrica de contenido |
| `CONTENT_OPERATING_SYSTEM.md` | Protocolo de producción de 60 minutos para 9 servicios |
| `JARDIN_IDEAL_BRAND_STYLE_GUIDE_V1.md` | Guía visual oficial — paleta, tipografía, Lightroom, reel, Meta Ads |
| `JARDIN_IDEAL_IDEAL_CUSTOMER_SYSTEM.md` | Sistema de calificación de leads 0–100 pts + scripts de venta |
| `ECOSISTEMA_MAESTRO.md` | Arquitectura dual Jardín Ideal + Groupe Ideal |
| `AUTOMATION_AUDIT_REPORT.md` | Auditoría de automatizaciones del sistema |
| `10_MEMORIA_EMPRESARIAL/` | Carpeta de memoria unificada — 13 archivos |

### Sistemas corregidos
| Archivo | Cambio |
|---------|--------|
| `~/.claude/settings.json` | Hook de voz: backslashes `\\` → forward slashes `/` |
| `~/.claude/speak.py` | Agregado Modo 1 (CLI args), duración dinámica del audio |
| `.gitignore` | Agregados: `*.mp4`, `*.mov`, `*.zip`, `.claude.json`, `.gitconfig` |

### Git
| Commit | Descripción |
|--------|-------------|
| `36f3d31` | Add Ideal Customer System - Lead qualification + sales framework |
| `4c827bb` | FLOAT V1 completed - Content Operating System + Brand Style Guide |

---

## 2026-06-22 — Sesión de auditoría y estructura dual

### Cambios
- Creado `ECOSISTEMA_MAESTRO.md` — arquitectura para gestionar dos empresas con un solo sistema
- Creado `01_EMPRESAS/` — carpeta con perfil de Jardín Ideal y Groupe Ideal
- Creado `AGENTE_REPORTES.md` y `AGENTE_AUTOMATIZACIONES.md`
- Creado `AUTOMATION_AUDIT_REPORT.md`

### Git
| Commit | Descripción |
|--------|-------------|
| `9705888` | Sistema automatizacion Jardin Ideal y Groupe Ideal |
| `00a930c` | Sistema de Branding Global v1.0 — Jardín Ideal / Groupe Ideal |

---

## 2026-06 — Fase inicial: Fábrica de Contenido

### Cambios
- Producción de primeros 3 paquetes COUR_AVANT con agente de video
- Creados agentes: CRM, Marketing, Operaciones, Control Calidad, Video, Montaje
- Estructura base del repositorio (00–10 carpetas)
- Primeros prompts de agentes

### Git
| Commit | Descripción |
|--------|-------------|
| `258cda0` | Agente Montaje Video v1.1 + assets físicos empaquetados CA-003 Puschak |
| `4dd6acc` | Agente Montaje Video v1.0 + primera ejecución CA-003 Puschak |
| `0083182` | Fábrica Contenido IA — paquetes producción final 3 proyectos COUR_AVANT |
| `d13a274` | primera prueba real Fábrica Contenido IA — 3 proyectos COUR_AVANT |
| `3f0102e` | feat: biblioteca visual 10 servicios + plan produccion continua |
| `6ec5021` | feat: estructura biblioteca visual — 4 servicios x 6 carpetas cada uno |

---

## FORMATO PARA NUEVAS ENTRADAS

```markdown
## YYYY-MM-DD — [Descripción breve de la sesión]

### Sistemas creados
| Archivo | Descripción |

### Sistemas modificados
| Archivo | Cambio |

### Sistemas eliminados
| Archivo | Motivo |

### Git
| Commit | Descripción |

### Notas
[Cualquier contexto relevante]
```
