# PLAN DE PRODUCCIÓN CONTINUA
**Jardín Ideal — Fábrica Multiservicio de Contenido**
**Versión:** 1.0 | **Fecha:** 23 junio 2026

---

## PRINCIPIO FUNDAMENTAL

Cada proyecto terminado genera contenido. Sin excepción.
El día que se termina un chantier, alguien toma el teléfono y filma.
Esa noche, el material entra al sistema.

---

## SERVICIOS ACTIVOS

### Nivel 1 — Producción máxima (publicar semanalmente)
| Servicio | Ticket promedio | Mejor ángulo |
|----------|----------------|-------------|
| COUR_AVANT | CA$5,500–15,000 | "Carte de visite de la maison" — vacío competitivo |
| PAVE_UNI | CA$8,000–45,000 | TCO 20 ans vs asphalte |
| BALCONS | CA$8,000–20,000 | Composite vs bois traité, urgencia estival |
| COUR_ARRIERE | CA$12,000–45,000 | Espace de vie d'été — familia |

### Nivel 2 — Producción regular (1-2 piezas por semana)
| Servicio | Ticket promedio | Ángulo |
|----------|----------------|--------|
| ESCALIERS | CA$3,500–12,000 | Sécurité + esthétique |
| CLOTURES | CA$2,500–8,000 | Intimité + valeur |
| RENOVATION_EXTERIEURE | CA$15,000–60,000 | Transformation complète |

### Nivel 3 — Producción de autoridad (2-4 piezas por mes)
| Servicio | Objetivo |
|----------|---------|
| RENOVATION_INTERIEURE | Upsell — cliente extérieur → intérieur |
| CONTENIDO_EDUCATIVO | SEO + autorité marché |
| TESTIMONIOS | Preuve sociale — cierre de ventas |

---

## CUOTA SEMANAL DE CONTENIDO

**Meta: 7 piezas publicadas por semana**

| Tipo | % | Piezas/semana | Descripción |
|------|---|--------------|-------------|
| Comercial | 40% | 3 | Reels y carruseles con CTA directo |
| Avant/Après | 30% | 2 | Transformaciones reales de proyectos |
| Educativo | 20% | 1-2 | Tips, guías, comparativos |
| Autoridad/Marca | 10% | 1 | Testimonios, equipo, behind-the-scenes |

---

## FLUJO OPERATIVO DIARIO

### Lunes — Planificación (09:00–09:30)
1. Revisar `00_BIBLIOTECA_VISUAL/` — ¿hay material nuevo de la semana pasada?
2. Verificar qué servicios tienen proyectos terminados pendientes de fotografiar
3. Asignar tareas de filmación para los chantiers activos de la semana

### Martes o Miércoles — Carga de material
1. Copiar fotos/videos en la carpeta correcta:
   ```
   00_BIBLIOTECA_VISUAL/[SERVICIO]/PROJ_[COD]_[ZONA]_[MES]/[AVANT|APRES|etc]/
   ```
2. Nombrar archivos con la convención:
   ```
   [SERVICIO]_[PROJ]_[TIPO]_[NUM].[ext]
   Ejemplo: CA_003_APRES_01.jpg | BALC_007_DETAIL_garde-corps_02.jpg
   ```

### Miércoles — Control de calidad (AGENTE_CONTROL_CALIDAD_MAGAZINE)
1. Abrir Claude con el prompt de `AGENTES_CALIDAD_Y_VIDEO/AGENTE_CONTROL_CALIDAD_MAGAZINE.md`
2. Enviar todas las fotos nuevas
3. Guardar fichas QC en la misma carpeta del proyecto: `QC_[archivo].txt`
4. Separar: APROBADOS → pasan al director | RECHAZADOS → anotar qué refotografiar

### Jueves — Dirección y brief (DIRECTOR_VIDEO_IA)
1. Abrir Claude con `AGENTES_CALIDAD_Y_VIDEO/DIRECTOR_VIDEO_IA.md`
2. Enviar material aprobado + servicio + audiencia objetivo
3. Guardar el brief de dirección: `BRIEF_REEL_[SERVICIO]_[PROJ].md`
4. Enviar brief al editor (CapCut o agencia)

### Viernes — Producción y programación
1. Montar Reel en CapCut siguiendo el brief
2. Armar carrusel en Canva
3. Redactar copy final en francés (usar `CONTENIDO_PARA_PUBLICAR/[SERVICIO]/`)
4. Programar publicación en Meta Business Suite para la semana siguiente

---

## SISTEMA DE PROYECTOS

### Cómo nombrar cada proyecto
```
PROJ_[SERVICIO]_[NÚMERO]_[ZONA]_[MES]

Ejemplos:
PROJ_CA_001_LAVAL_JUN2026        → Cour Avant, Laval, junio 2026
PROJ_PAVE_003_MTLNORD_JUL2026    → Pavé-Uni, Montréal-Nord, julio 2026
PROJ_BALC_007_RIVENORD_JUL2026   → Balcons, Rive-Nord, julio 2026
```

### Una carpeta por proyecto, no una carpeta por fecha
Mantener todo el material de un proyecto junto — avant, pendant, après, détails —
en lugar de organizar por fecha. El antes/después de un mismo proyecto siempre
debe estar en la misma carpeta.

---

## BALANCE MULTISERVICIO

### Regla de los tres servicios activos
Cada semana debe haber contenido de al menos **3 servicios diferentes**.
Nunca publicar la misma semana más de 3 piezas del mismo servicio.

**Si hay semana sin proyecto terminado:**
- Usar material de archivo de proyectos anteriores aún no publicados
- Publicar contenido educativo (comparativos, tips, guías)
- Publicar un testimonio existente

### Rotación mínima semanal (ejemplo)
| Día | Publicación | Servicio | Tipo |
|-----|------------|----------|------|
| Martes | Reel | COUR_AVANT | Avant/Après |
| Miércoles | Carrusel | PAVE_UNI | Educativo comparatif |
| Jueves | Historia x5 | BALCONS | Urgence + tips |
| Viernes | Reel | COUR_ARRIERE | Comercial verano |
| Sábado | Post + testimonio | Cualquier nivel 1 | Autoridad |

---

## PROTOCOLO DE FOTOGRAFÍA EN CHANTIER

### Quién filma
El responsable del proyecto (Ingrid o quien esté en chantier) filma con teléfono.
No se necesita cámara profesional para el 80% del material.

### Qué filmar en cada visita al chantier
**Visita 1 — Avant (antes de empezar)**
- [ ] Plano general desde la calle (foto estática + video 10s)
- [ ] Close-up del problema principal (grietas, madera deteriorada, etc.)
- [ ] Video caminando hacia la propiedad (15s)

**Visita 2 — Pendant (durante la obra, día 1-2)**
- [ ] Equipo trabajando (sin identificar trabajadores si no hay autorización)
- [ ] Materiales: pavé, composite, piedra — close-up del material nuevo
- [ ] Proceso: excavación, pose de base, etc.

**Visita 3 — Après (obra terminada)**
- [ ] Mismos ángulos que el AVANT para hacer el match cut
- [ ] Plano general desde la calle — hora dorada (6-8pm en verano)
- [ ] Close-ups de acabados y detalles
- [ ] Video walking tour: caminar desde la calle hasta la entrada (20s)
- [ ] Si hay cliente presente y autoriza: 30s de reacción o testimonio espontáneo

### 5 reglas de filmación
1. **Luz natural siempre** — nunca filmar en días nublados si se puede evitar
2. **Limpiar el frame** — quitar herramientas, basura, conos naranjas antes de filmar
3. **Horizontal para videos** — vertical solo para historias y reels
4. **Estabilizar** — apoyar el teléfono en una superficie o usar gimbal para videos
5. **Mismo ángulo avant/après** — posicionarse exactamente en el mismo punto para que el match cut funcione

---

## INDICADORES DE PRODUCCIÓN

Revisar cada lunes en 5 minutos:

| Métrica | Meta semanal | Alerta si... |
|---------|-------------|-------------|
| Piezas publicadas | 7 | < 5 |
| Servicios distintos publicados | ≥ 3 | Solo 1 |
| Material nuevo cargado en biblioteca | ≥ 1 proyecto | 0 proyectos |
| Material pendiente de QC | 0 al viernes | > 10 fotos sin revisar |
| Piezas en cola programada | ≥ 5 para la semana siguiente | < 3 |

---

## ARCHIVOS DE REFERENCIA

| Archivo | Ubicación | Para qué |
|---------|-----------|---------|
| AGENTE_CONTROL_CALIDAD_MAGAZINE.md | AGENTES_CALIDAD_Y_VIDEO/ | Evaluar fotos/videos |
| DIRECTOR_VIDEO_IA.md | AGENTES_CALIDAD_Y_VIDEO/ | Diseñar estructura del reel |
| contenido_balcons.html | CONTENIDO_PARA_PUBLICAR/BALCONS/ | Copiar hooks y copy listo |
| contenido_cour_avant.html | CONTENIDO_PARA_PUBLICAR/COUR_AVANT/ | Copiar hooks y copy listo |
| contenido_cour_arriere.html | CONTENIDO_PARA_PUBLICAR/COUR_ARRIERE/ | Copiar hooks y copy listo |
| contenido_pave_uni.html | CONTENIDO_PARA_PUBLICAR/PAVE_UNI/ | Copiar hooks y copy listo |
| MASTER_CONTENT_CALENDAR.html | CONTENT_PRODUCTION/ | Calendario consolidado julio |

---

## CUÁNDO CREAR NUEVA CARPETA DE PROYECTO

Al terminar cada obra, antes de irse del chantier:
```
1. Crear carpeta: PROJ_[SERVICIO]_[NÚM]_[ZONA]_[MES]
2. Crear subcarpetas: AVANT / PENDANT / APRES / DETAILS / DRONE / VIDEOS
3. Cargar fotos del teléfono directamente desde el chantier (o esa noche)
4. Nunca dejar pasar más de 48h — la memoria se borra, la luz cambia
```
