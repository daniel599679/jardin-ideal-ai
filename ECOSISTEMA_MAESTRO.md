# ECOSISTEMA MAESTRO — GROUPE IDEAL
**Versión:** 1.0 | **Fecha:** 2026-06-23
**Archivo raíz del sistema de inteligencia artificial empresarial**

---

## VISIÓN DEL SISTEMA

Un único ecosistema de IA opera simultáneamente para dos empresas hermanas.
Los procesos, automatizaciones y agentes se construyen una vez y se replican a ambas.
No se duplica trabajo. Se escala metodología.

---

## EMPRESAS DEL GRUPO

| Campo | Jardín Ideal | Groupe Ideal |
|-------|-------------|--------------|
| **ID sistema** | `JARDIN_IDEAL` | `GROUPE_IDEAL` |
| **Idioma clientes** | Francés | Francés |
| **Idioma interno** | Español | Español |
| **Objetivo 2026** | 7M CAD | Por definir |
| **Horario** | Lun-Vie 07:00-18:00 | Lun-Vie 07:00-18:00 |
| **Reunión diaria** | 09:00 AM | 09:00 AM |
| **Teléfono CTA** | 514-266-2504 | Por confirmar |
| **Web** | jardin-ideal.com | Por confirmar |
| **Perfil** | `01_EMPRESAS/JARDIN_IDEAL/PERFIL_EMPRESA.md` | `01_EMPRESAS/GROUPE_IDEAL/PERFIL_EMPRESA.md` |

---

## CONFIGURACIÓN ACTIVA

El archivo `01_EMPRESAS/EMPRESA_ACTIVA.md` determina qué empresa está operando.
**Todos los agentes deben leerlo antes de ejecutar cualquier tarea.**

```
EMPRESA_ACTIVA = JARDIN_IDEAL   ← cambiar a GROUPE_IDEAL cuando corresponda
```

---

## MAPA DEL SISTEMA

```
Jardin_Ideal_AI_System/
│
├── ECOSISTEMA_MAESTRO.md              ← ESTE ARCHIVO — documento raíz
│
├── 00_EMPRESA/                        ← perfil histórico Jardín Ideal (legacy)
├── 01_EMPRESAS/                       ← estructura dual-empresa (activo)
│   ├── EMPRESA_ACTIVA.md              ← CONFIG GLOBAL — empresa en operación
│   ├── JARDIN_IDEAL/
│   │   ├── PERFIL_EMPRESA.md
│   │   ├── SERVICIOS/
│   │   ├── CONTENIDO/
│   │   ├── REPORTES/
│   │   └── CAMPANAS/
│   └── GROUPE_IDEAL/
│       ├── PERFIL_EMPRESA.md
│       ├── SERVICIOS/
│       ├── CONTENIDO/
│       ├── REPORTES/
│       └── CAMPANAS/
│
├── 01_AGENTES/                        ← agentes operacionales del grupo
│   ├── agente_crm.md
│   ├── agente_marketing.md
│   ├── agente_operaciones.md
│   ├── AGENTE_REPORTES.md             ← nuevo
│   └── AGENTE_AUTOMATIZACIONES.md    ← nuevo
│
├── 05_MARKETING/
│   ├── 99_BRANDING_GLOBAL/            ← identidad visual compartida
│   │   ├── PALETA_COLORES.txt
│   │   ├── FONT_GUIDE.txt
│   │   ├── BRAND_RULES.md
│   │   └── logos/
│   │       ├── jardin ideal/
│   │       └── groupe ideal/
│   └── AGENTES_CALIDAD_Y_VIDEO/       ← agentes de producción de contenido
│       ├── AGENTE_CONTROL_CALIDAD_MAGAZINE.md
│       ├── DIRECTOR_VIDEO_IA.md
│       ├── AGENTE_MONTAJE_VIDEO.md
│       └── AGENTE_MARKETING.md
│
├── 06_CRM/                            ← compartido entre empresas
├── 07_AUTOMATIZACIONES/               ← compartido entre empresas
└── 08_REPORTES/                       ← compartido, separado por empresa
```

---

## CAPA DE AGENTES — DOS NIVELES

### Nivel 1 — Agentes Operacionales (`01_AGENTES/`)
Operan para el **Grupo** — gestionan ambas empresas según `EMPRESA_ACTIVA`.

| Agente | Función | Empresas |
|--------|---------|---------|
| `agente_crm.md` | Gestión de leads y pipeline | Ambas |
| `agente_marketing.md` | Generación de leads, campañas | Ambas |
| `agente_operaciones.md` | Prioridades diarias, proyectos activos | Ambas |
| `AGENTE_REPORTES.md` | Reportes diarios, semanales, mensuales | Ambas |
| `AGENTE_AUTOMATIZACIONES.md` | Evalúa y propone automatizaciones | Ambas |

### Nivel 2 — Agentes de Producción (`05_MARKETING/AGENTES_CALIDAD_Y_VIDEO/`)
Especializados en producción de contenido audiovisual.

| Agente | Función |
|--------|---------|
| `AGENTE_CONTROL_CALIDAD_MAGAZINE` | QC de fotos y videos |
| `DIRECTOR_VIDEO_IA` | Briefs de reel/video |
| `AGENTE_MONTAJE_VIDEO` | Paquetes de producción completos |
| `AGENTE_MARKETING` | Copys y Meta Ads |

---

## PROTOCOLO EMPRESA_ACTIVA

### Al inicio de cualquier tarea, todo agente ejecuta:
```
1. Leer 01_EMPRESAS/EMPRESA_ACTIVA.md
2. Cargar perfil: 01_EMPRESAS/[EMPRESA_ACTIVA]/PERFIL_EMPRESA.md
3. Cargar logos: 05_MARKETING/99_BRANDING_GLOBAL/logos/[empresa]/
4. Aplicar branding: 99_BRANDING_GLOBAL/BRAND_RULES.md
5. Verificar: ¿Este proceso debe replicarse para la empresa hermana?
```

### Cambio de empresa activa
Para cambiar de empresa, editar `01_EMPRESAS/EMPRESA_ACTIVA.md`:
```
# Cambiar de:
EMPRESA_ACTIVA = JARDIN_IDEAL
# A:
EMPRESA_ACTIVA = GROUPE_IDEAL
```

---

## LÓGICA DE REPLICACIÓN

**Antes de crear cualquier activo, preguntarse:**

> ¿Este proceso debe replicarse para la empresa hermana?

| Si el proceso es... | Acción |
|--------------------|--------|
| Metodología (QC, briefs, timelines) | Replicar inmediatamente — misma estructura |
| Contenido específico de un proyecto | No replicar — es único por proyecto |
| Automatización operacional | Evaluar si aplica a ambas empresas |
| Template de campaña | Adaptar branding y replicar |
| Reporte | Generar versión por empresa |

---

## BRANDING COMPARTIDO Y DIFERENCIADO

Ambas empresas comparten:
- Paleta de colores base
- Tipografía (Georgia + Montserrat)
- Metodología de producción
- Estándares de calidad

Cada empresa tiene:
- Logo propio
- Servicios propios
- Audiencia objetivo propia
- Historial de proyectos propio

---

## OBJETIVO DEL SISTEMA

Construir una matriz empresarial donde:
- **Un solo equipo** opera con **dos identidades comerciales**
- **Un solo ecosistema IA** gestiona **ambas empresas**
- **Cero duplicación manual** de procesos
- **Escalabilidad total** — agregar una tercera empresa requiere solo crear `01_EMPRESAS/NUEVA_EMPRESA/` y cargar su perfil

---

## HISTORIAL DE VERSIONES

| Versión | Fecha | Cambio |
|---------|-------|--------|
| 1.0 | 2026-06-23 | Arquitectura dual Jardín Ideal + Groupe Ideal |
