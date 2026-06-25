# PROTOCOLO DE ACTIVOS VISUALES — JARDÍN IDEAL
**Versión:** 1.0 | **Fecha:** 2026-06-25
**Tipo:** Regla permanente del sistema — no modificar sin aprobación de Daniel
**Propósito:** Define cómo Claude selecciona, evalúa y usa activos visuales en todas las tareas.

---

## REGLA CARDINAL

> **La carpeta Premium de Francisco es la fuente oficial y absoluta de activos visuales de Jardín Ideal.**
>
> Las imágenes reales de proyectos tienen prioridad absoluta sobre imágenes IA, stock o genéricas.
> Esta regla no tiene excepciones mientras existan imágenes reales equivalentes disponibles.

---

## 1. FUENTE OFICIAL DE ACTIVOS

| Prioridad | Fuente | Cuándo usar |
|-----------|--------|------------|
| 🥇 **1 — OBLIGATORIA** | Carpeta Premium Francisco | Siempre que existan imágenes del servicio solicitado |
| 🥈 2 — Secundaria | Fotos reales de proyectos en campo (actuales) | Cuando Francisco no tiene del servicio específico |
| 🥉 3 — Emergencia | Biblioteca general del proyecto | Solo si no hay ninguna real disponible |
| ❌ **PROHIBIDA** | Stock genérico / imágenes IA | Nunca si existe cualquier imagen real equivalente |

**Ruta oficial de la biblioteca:**
```
05_MARKETING/00_BIBLIOTECA_VISUAL/Photo selectionné par francisco/
```

**Regla de campo (obras activas):**
Proyectos en ejecución HOY tienen prioridad para captura y uso inmediato:
- Stéphane Parisien (2x Balcon + Tourelle) — inicio 2026-06-25
- Alain Breault (Balcon + Amen. Ext.)
- Vincent Goudreault (Balcon + Amen. Ext.)
- Karine Rousseau (Aménagement Extérieur)

---

## 2. SELECCIÓN AUTOMÁTICA — FLOAT VISUAL SCORE

Claude debe aplicar el sistema de puntuación `03_PREMIUM_VISUAL_SCORE.md` (100 puntos) para seleccionar automáticamente las mejores imágenes.

### Criterios de selección (ponderación Francisco Standard)

| Criterio | Puntos | Descripción |
|----------|--------|-------------|
| Luz natural — cielo azul + nubes | 20 | Condición ideal Quebec |
| Color del pavé/material | 15 | Beige, gris-clair — sin manchas |
| Verde del césped | 15 | Bright green — bien mantenido |
| Arquitectura Quebec visible | 15 | Ladrillo rojo, madera típica |
| Composición y encuadre | 15 | Regla de tercios, sin distorsión |
| Ausencia de elementos negativos | 10 | Sin basura, logos, personas borrosas |
| Nitidez y resolución | 10 | Mínimo 1080px en el lado corto |

### Gate de publicación

| Score | Decisión |
|-------|---------|
| ≥90/100 | ✅ HERO — publicar en Meta Ads y contenido premium |
| 75–89 | ✅ SECUNDARIO — redes orgánicas, stories |
| 60–74 | ⚠️ REVISIÓN — usar solo si no hay alternativa mejor |
| <60 | ❌ RECHAZADA — no publicar |

---

## 3. IDENTIFICACIÓN DE SERVICIO POR NOMBRE DE ARCHIVO

Claude identifica el servicio usando palabras clave en el nombre del archivo:

| Palabras clave en filename | Servicio identificado |
|---------------------------|----------------------|
| `balcon`, `balcone`, `balcons`, `terrasse_balcon` | Balcon |
| `cour_arriere`, `cour-arriere`, `patio_arriere`, `backyard` | Cour Arrière |
| `cour_avant`, `cour-avant`, `patio_avant`, `frontyard` | Cour Avant |
| `pave`, `pave_uni`, `pave-uni`, `pavé`, `interlock` | Pavé-Uni |
| `piscine`, `pool`, `spa` | Piscine |
| `deck`, `composite`, `terrasse_composite` | Deck Composite |
| `escalier`, `stairs`, `marche` | Escaliers |
| `mur`, `beton`, `retaining`, `gabion` | Murs de béton |
| `amenagement`, `amen_ext`, `aménagement`, `landscaping` | Aménagement Extérieur |
| `entretien`, `gazon`, `pelouse`, `tonte` | Entretien |
| Nombre no reconocido | → Clasificar como "GENERAL" y alertar a Daniel |

**Regla de empate:** Si el filename contiene múltiples servicios (ej: `balcon_pave_2024.jpg`), clasificar por el primer término encontrado.

---

## 4. RANKING DE CALIDAD POR ACTIVO

Cuando Claude trabaja con la biblioteca, debe generar un ranking antes de seleccionar:

### Formato de ranking (output esperado)

```
RANKING ACTIVOS — [SERVICIO] — [FECHA]

🥇 #1: nombre_archivo.jpg | Score: 94/100 | Uso: HERO Meta Ads
   → Luz: ✅ | Color: ✅ | Composición: ✅ | Arquitectura: ✅

🥈 #2: nombre_archivo2.jpg | Score: 87/100 | Uso: Story / Orgánico
   → Luz: ✅ | Color: ✅ | Composición: ⚠️ | Arquitectura: ✅

🥉 #3: nombre_archivo3.jpg | Score: 76/100 | Uso: Carrusel interno
   → Luz: ⚠️ | Color: ✅ | Composición: ✅ | Arquitectura: ❌

❌ RECHAZADAS: [lista de archivos con score <60 y motivo]
```

---

## 5. ALERTAS DE COBERTURA POR SERVICIO

Claude debe evaluar la cobertura de la biblioteca y generar alertas cuando un servicio tiene poco material.

### Umbrales de alerta

| Estado | Imágenes disponibles (≥75/100) | Alerta |
|--------|-------------------------------|--------|
| ✅ CUBIERTO | ≥10 imágenes | Sin alerta |
| ⚠️ BAJO | 5–9 imágenes | Alerta amarilla — planificar sesión fotográfica |
| 🔴 CRÍTICO | 1–4 imágenes | Alerta roja — bloquear campaña hasta sesión |
| ❌ VACÍO | 0 imágenes | Alerta roja — usar campo si obra activa, sino suspender |

### Formato de alerta de cobertura

```
⚠️ ALERTA COBERTURA VISUAL — [SERVICIO]
Imágenes disponibles (≥75/100): X
Estado: [BAJO / CRÍTICO / VACÍO]
Acción: [Planificar sesión con Matt/Karim/Steven en próximo proyecto]
Proyecto disponible para sesión: [nombre si hay obra activa]
```

---

## 6. PROTOCOLO DE USO POR TAREA

### Para Meta Ads (creativos de campaña)
1. Abrir biblioteca Francisco → filtrar por servicio de la campaña
2. Aplicar FLOAT Visual Score → seleccionar top 3 (score ≥90)
3. Si <3 imágenes con score ≥90 → buscar en proyectos activos en campo
4. Si aún insuficiente → generar alerta de cobertura + proponer sesión fotográfica
5. **Nunca usar stock** mientras exista imagen real con score ≥75

### Para carruseles Manus (TASK-002, TASK-003, etc.)
1. Seleccionar 6–8 imágenes por servicio (mínimo score 75/100)
2. Diversificar: ángulos distintos, momentos distintos (inicio/proceso/resultado)
3. Incluir al menos 1 imagen con arquitectura Quebec visible
4. Incluir al menos 1 imagen con cielo azul visible

### Para contenido orgánico (Instagram, Facebook)
1. Mínimo score 75/100 para feeds
2. Stories: score ≥60 aceptable si la narrativa lo justifica
3. Dar preferencia a imágenes "proceso" para Stories (detrás de cámara)

---

## 7. REGLAS ABSOLUTAS (no negociables)

1. **Imagen real > imagen IA** — siempre, sin excepción
2. **Francisco library > cualquier otra fuente** cuando el servicio está cubierto
3. **Score <60 = no publicar** — aunque no haya alternativa en ese momento
4. **No inventar proyectos** — solo usar imágenes de obras reales confirmadas
5. **Alert antes de usar stock** — siempre avisar a Daniel si hay que recurrir a stock
6. **Capturar hoy** — cuando hay obra activa en campo, capturar desde día 1 (como Parisien hoy)

---

## 8. RESPONSABILIDADES

| Quién | Responsabilidad |
|-------|----------------|
| **Francisco** | Selección y curación de imágenes en la biblioteca oficial |
| **Matt / Karim / Steven** | Captura de fotos en campo según instrucciones de calidad |
| **Daniel** | Aprueba publicación de cualquier activo en Meta Ads o redes |
| **Claude** | Scoring automático, ranking, alertas de cobertura, selección para tareas |

---

*Protocolo Activos Visuales — Jardín Ideal AI System · v1.0 · 2026-06-25*
*Regla permanente — requiere aprobación de Daniel para modificar*
