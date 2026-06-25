# COBERTURA DE SERVICIOS — BIBLIOTECA VISUAL FRANCISCO
**Última actualización:** 2026-06-25 — v1.1 (alias semánticos BALCON aplicados)
**Total activos en biblioteca:** 62 archivos (61 únicos — 1 duplicado detectado)
**Ruta oficial:** `05_MARKETING/00_BIBLIOTECA_VISUAL/Photo selectionné par francisco/`
**Fuente de scoring:** `FRANCISCO_VISUAL_STANDARD.md` + `05_MARKETING/FLOAT_V2_PREMIUM/03_PREMIUM_VISUAL_SCORE.md`

---

## ALIAS SEMÁNTICO PERMANENTE

> **BALCON = TERRASSE + DECK + PERGOLA + PATIO ÉLEVÉ**
>
> "Terrasse" y "Deck Composite" no son servicios independientes en el sistema de clasificación visual.
> Todo archivo con prefijo `terrasse_`, `deck_`, `pergola_`, `patio_salon_`, `patio_balancoire_`,
> `terrasse_store_`, `terrasse_composite_`, `terrasse_bois_` se clasifica automáticamente como **BALCON**.
>
> Referencia completa: `10_MEMORIA_EMPRESARIAL/PROTOCOLO_ACTIVOS_VISUALES.md` sección 3

---

## INSTRUCCIONES DE ACTUALIZACIÓN PARA CLAUDE

> Cada vez que se agreguen imágenes nuevas a la carpeta Francisco, Claude debe:
> 1. Leer el contenido actualizado de la carpeta
> 2. Clasificar nuevos archivos por servicio usando el mapping de sección 3 del `PROTOCOLO_ACTIVOS_VISUALES.md`
>    (incluir alias BALCON — cualquier `terrasse_*`, `deck_*`, `pergola_*`, `patio_salon_*`, `patio_balancoire_*`)
> 3. Aplicar FLOAT_VISUAL_SCORE a cada imagen nueva
> 4. Actualizar el contador, score promedio y top 5 del servicio correspondiente
> 5. Actualizar la fecha de este documento y el número de versión
> 6. Generar alerta si algún servicio baja del umbral crítico (<5 imágenes ≥75/100)
> 7. Hacer commit con mensaje: `chore: actualizar COBERTURA_SERVICIOS — [servicio] +N imágenes`

**Scores confirmados:** `patio_rotin_pub.png` (98/100), `cour_arriere_facebook_45.png` (96/100),
`patio_arriere_pub.png` (95/100), `cour_arriere_pave_pub.png` (93/100)
**Scores pendientes:** todos los demás — marcados como `[PE]` hasta evaluación visual formal.

---

## RESUMEN EJECUTIVO — ESTADO DE COBERTURA (v1.1)

| Servicio | Imágenes | Score prom. | Estado | Alerta |
|---------|----------|-------------|--------|--------|
| **BALCON** *(= Terrasse + Deck + Pergola + Patio Élevé)* | **11** | [PE] | ✅ **CUBIERTO** | — |
| Cour Avant / Entrée | 10 | [PE] | ✅ CUBIERTO | — |
| Cour Arrière | 8 | 95.5* | ✅ CUBIERTO | — |
| Piscine | 9 (1 duplic.) | [PE] | ✅ CUBIERTO | Eliminar duplicado |
| Escaliers / Marches | 8 | [PE] | ✅ CUBIERTO | — |
| Pavé-Uni | 6 | [PE] | ✅ CUBIERTO | — |
| Clôtures | 3 | [PE] | ⚠️ BAJO | Planificar sesión |
| Aménagement Extérieur | 3 | [PE] | ⚠️ BAJO | Rousseau — capturar semana 4 |
| Murs de béton | 2 | [PE] | 🔴 CRÍTICO | Sin obra activa — suspender campaña |
| Terrasse / Deck | — | — | ✅ FUSIONADO EN BALCON | Ver sección BALCON |
| Sin clasificar | 1 | — | ⚠️ REVISAR | UUID — identificar servicio |

*Score promedio Cour Arrière calculado sobre 4 imágenes evaluadas formalmente.

### Cambio v1.0 → v1.1

| Servicio | Antes | Ahora | Motivo |
|---------|-------|-------|--------|
| BALCON | 🔴 CRÍTICO (0 img) | ✅ CUBIERTO (11 img) | Alias semántico: terrasse + deck + pergola + patio_salon + patio_balancoire |
| Cour Arrière | 10 img | 8 img | patio_salon y patio_balancoire reclasificados a BALCON |
| Terrasse / Deck Composite | ✅ CUBIERTO (9 img) | FUSIONADO EN BALCON | Servicio no existe como categoría independiente |

---

## ALERTAS ACTIVAS (v1.1)

```
✅ RESUELTO — BALCON
   Era CRÍTICO (0 imágenes). Ahora CUBIERTO (11 imágenes).
   Alias semántico aplicado: terrasse + deck + pergola + patio élevé.
   Fuente adicional: fotos reales Parisien en captura hoy (ampliarán el pool).

🔴 CRÍTICO — MURS DE BÉTON
   2 imágenes disponibles (umbral mínimo: 5)
   Impacto: no lanzar campaña de este servicio
   Acción: planificar sesión fotográfica en próximo proyecto de muros

⚠️ BAJO — CLÔTURES
   3 imágenes disponibles (umbral mínimo: 5)
   Acción: capturar en próxima obra con clôture

⚠️ BAJO — AMÉNAGEMENT EXTÉRIEUR
   3 imágenes disponibles (umbral mínimo: 5)
   Oportunidad inmediata: Karine Rousseau — semana 4 — capturar esta semana

⚠️ DUPLICADO — PISCINE
   piscine_patio_pub - Copie.png = copia exacta de piscine_patio_pub.png (ambas 8.6MB)
   Acción: eliminar la copia para limpiar biblioteca

⚠️ ARCHIVO SOSPECHOSO
   2863ff2f-2292-4ce0-afaf-9b5d1bca7d52.jpg — nombre UUID, tamaño 9.4KB
   Probable archivo corrupto o placeholder — verificar y eliminar
```

---

## DETALLE POR SERVICIO

---

### 1. BALCON ✅ CUBIERTO
**= Terrasse + Deck + Pergola + Patio Élevé (alias semántico)**
**Imágenes:** 11 | **Score promedio:** [PE] | **Estado:** ✅ CUBIERTO
**Próxima oportunidad:** Fotos reales proyecto Stéphane Parisien (2x Balcon + Tourelle — inicio 2026-06-25)
**Última actualización:** 2026-06-25 (v1.1 — alias aplicado)

| # | Archivo | Patrón | Tamaño | Score | Uso recomendado |
|---|---------|--------|--------|-------|----------------|
| 🥇 1 | `patio deck et pergola.png` | `deck` + `pergola` | 8.0MB | [PE] | Candidata HERO (pergola = premium) |
| 🥈 2 | `terrasse_store_vue1_pub.png` | `terrasse_store_` | 7.8MB | [PE] | Meta Ads |
| 🥉 3 | `terrasse_store_vue2_pub.png` | `terrasse_store_` | 7.8MB | [PE] | Meta Ads |
| 4 | `terrasse_mur_pub.png` | `terrasse_` | 7.7MB | [PE] | Carrusel |
| 5 | `terrasse2_pub.png` | `terrasse_` | 7.5MB | [PE] | Carrusel |
| — | `patio_balancoire_pub.png` | `patio_balancoire_` | 8.6MB | [PE] | Candidata HERO |
| — | `patio_salon_pub.png` | `patio_salon_` | 8.0MB | [PE] | Carrusel |
| — | `terrasse_bois2_pub.png` | `terrasse_bois_` | 7.4MB | [PE] | Pendiente |
| — | `terrasse_bois1_pub.png` | `terrasse_bois_` | 7.1MB | [PE] | Pendiente |
| — | `terrasse1_pub.png` | `terrasse_` | 7.3MB | [PE] | Pendiente |
| — | `terrasse_composite_grise_pub.png` | `terrasse_composite_` | 7.0MB | [PE] | Pendiente |

**Top 5 recomendadas (pendiente evaluación formal):** evaluar patio_balancoire + patio deck et pergola como HERO candidates — mayor tamaño = potencialmente mayor resolución.

> **Nota para campaña Balcon activa:** Los 11 activos existentes son suficientes para lanzar creativos esta semana. Priorizar evaluación formal con FLOAT_VISUAL_SCORE antes del viernes 27 jun. Las fotos de campo Parisien añadirán imágenes reales de obra al pool.

---

### 2. COUR AVANT / ENTRÉE
**Imágenes:** 10 | **Score promedio:** [PE] | **Estado:** ✅ CUBIERTO
**Próxima oportunidad:** Fotos de cour avant en próxima obra nueva
**Última actualización:** 2026-06-25

| # | Archivo | Tamaño | Score | Uso recomendado |
|---|---------|--------|-------|----------------|
| 🥇 1 | `entree_stationnement2_pub (1).png` | 9.4MB | [PE] | Candidata HERO (mayor resolución) |
| 🥈 2 | `entree_marches_flottantes_pub.png` | 8.5MB | [PE] | Meta Ads |
| 🥉 3 | `entree_garage_pave1_pub.png` | 8.4MB | [PE] | Carrusel |
| 4 | `entree_pavee_pub.png` | 8.3MB | [PE] | Carrusel |
| 5 | `entree_pierre_pave_pub.png` | 8.1MB | [PE] | Carrusel |
| — | `facade_stationnement_pub.png` | 7.8MB | [PE] | Pendiente |
| — | `entree_escalier_pub.png` | 7.9MB | [PE] | Pendiente |
| — | `entree1_pub.png` | 7.6MB | [PE] | Pendiente |
| — | `stationnement_asphalte_pub.png` | 7.0MB | [PE] | Pendiente |
| — | `entree2_pub.png` | 7.4MB | [PE] | Pendiente |

---

### 3. COUR ARRIÈRE
**Imágenes:** 8 | **Score promedio:** 95.5/100* | **Estado:** ✅ CUBIERTO
*(patio_salon y patio_balancoire reclasificados a BALCON en v1.1)*
**Próxima oportunidad:** Fotos de campo Breault / Goudreault (obras activas)
**Última actualización:** 2026-06-25 (v1.1 — 2 imágenes migradas a BALCON)

| # | Archivo | Tamaño | Score | Uso recomendado |
|---|---------|--------|-------|----------------|
| 🥇 1 | `patio_rotin_pub.png` | 8.6MB | **98/100** ✅ | HERO Meta Ads |
| 🥈 2 | `cour_arriere_facebook_45.png` | 7.5MB | **96/100** ✅ | Reel / Video Ad |
| 🥉 3 | `patio_arriere_pub.png` | 7.6MB | **95/100** ✅ | Story / Carrusel |
| 4 | `cour_arriere_pave_pub.png` | 7.5MB | **93/100** ✅ | Remarketing |
| 5 | `patio_triplex_pub.png` | 8.1MB | [PE] | Candidata siguiente |
| — | `cour_arriere_facebook_169.png` | 8.3MB | [PE] | Pendiente |
| — | `cour_verandah_pub.png` | 7.5MB | [PE] | Pendiente |
| — | `gazebo_patio_pub.png` | 7.4MB | [PE] | Pendiente |

**Top 5 recomendadas:** patio_rotin → cour_arriere_facebook_45 → patio_arriere → cour_arriere_pave → patio_triplex

---

### 4. PISCINE
**Imágenes:** 9 únicas (+ 1 duplicado) | **Score promedio:** [PE] | **Estado:** ✅ CUBIERTO
**Nota:** `piscine_patio_pub - Copie.png` es duplicado exacto — eliminar
**Última actualización:** 2026-06-25

| # | Archivo | Tamaño | Score | Uso recomendado |
|---|---------|--------|-------|----------------|
| 🥇 1 | `piscine_plongeoir_pub.png` | 9.1MB | [PE] | Candidata HERO |
| 🥈 2 | `chaises_piscine_pub.png` | 8.9MB | [PE] | Meta Ads |
| 🥉 3 | `piscine_patio_pub.png` | 8.6MB | [PE] | Carrusel |
| 4 | `piscine_magazine.png` | 8.1MB | [PE] | Editorial |
| 5 | `piscine_vue_dessus_pub.png` | 8.2MB | [PE] | Story / Aérea |
| — | `piscine_cabane_pub.png` | 8.2MB | [PE] | Pendiente |
| — | `piscine_dalle_pub.png` | 8.1MB | [PE] | Pendiente |
| — | `piscine_angle2_pub.png` | 8.0MB | [PE] | Pendiente |
| — | `piscine_escalier_pub.png` | 7.6MB | [PE] | Pendiente |
| ❌ | `piscine_patio_pub - Copie.png` | 8.6MB | DUPLICADO | Eliminar |

---

### 5. ESCALIERS / MARCHES
**Imágenes:** 8 | **Score promedio:** [PE] | **Estado:** ✅ CUBIERTO
**Próxima oportunidad:** Marches en proyecto Parisien (tourelle incluye escaleras)
**Última actualización:** 2026-06-25

| # | Archivo | Tamaño | Score | Uso recomendado |
|---|---------|--------|-------|----------------|
| 🥇 1 | `entree_marches_flottantes_pub.png` | 8.5MB | [PE] | Candidata HERO |
| 🥈 2 | `escalier_noir_vue2_pub.png` | 8.3MB | [PE] | Meta Ads |
| 🥉 3 | `escalier_noir_vue1_pub.png` | 7.9MB | [PE] | Carrusel |
| 4 | `escalier_pave_pub.png` | 7.5MB | [PE] | Carrusel |
| 5 | `escalier_pave_facade_pub.png` | 7.5MB | [PE] | Story |
| — | `marches_beton_vue1_pub.png` | 7.5MB | [PE] | Pendiente |
| — | `marches_beton_vue2_pub.png` | 7.5MB | [PE] | Pendiente |
| — | `entree_escalier_pub.png` | 7.9MB | [PE] | Pendiente |

---

### 6. PAVÉ-UNI
**Imágenes:** 6 | **Score promedio:** [PE] | **Estado:** ✅ CUBIERTO
**Próxima oportunidad:** Fotos de pavé en proyectos Breault y Goudreault (activos)
**Última actualización:** 2026-06-25

| # | Archivo | Tamaño | Score | Uso recomendado |
|---|---------|--------|-------|----------------|
| 🥇 1 | `entree_garage_pave2_pub.png` | 8.1MB | [PE] | Candidata HERO |
| 🥈 2 | `allee_automne_pub.png` | 8.3MB | [PE] | Meta Ads |
| 🥉 3 | `allee_pavee_pub.png` | 8.2MB | [PE] | Carrusel |
| 4 | `entree_garage_pave1_pub.png` | 8.4MB | [PE] | Carrusel |
| 5 | `garage_pave_pub.png` | 7.6MB | [PE] | Story |
| — | `duplex_pave_pub.png` | 7.5MB | [PE] | Pendiente |

---

### 7. CLÔTURES ⚠️ BAJO
**Imágenes:** 3 | **Score promedio:** [PE] | **Estado:** ⚠️ BAJO — 2 por debajo del umbral (5)
**Próxima oportunidad:** Capturar en próxima obra que incluya clôture
**Última actualización:** 2026-06-25

| # | Archivo | Tamaño | Score | Uso recomendado |
|---|---------|--------|-------|----------------|
| 🥇 1 | `cloture_composite_pub.png` | 7.5MB | [PE] | Mejor candidata disponible |
| 🥈 2 | `portail_fer_pub.png` | 6.8MB | [PE] | — |
| 🥉 3 | `cloture_brun_pave_pub.png` | 6.7MB | [PE] | — |

> ⚠️ No lanzar campaña Clôtures hasta completar biblioteca (mínimo 5 imágenes).

---

### 8. AMÉNAGEMENT EXTÉRIEUR ⚠️ BAJO
**Imágenes:** 3 | **Score promedio:** [PE] | **Estado:** ⚠️ BAJO — 2 por debajo del umbral (5)
**Próxima oportunidad:** ⭐ Karine Rousseau — Amen. Ext. $135K — semana 4 (esta semana)
**Última actualización:** 2026-06-25

| # | Archivo | Tamaño | Score | Uso recomendado |
|---|---------|--------|-------|----------------|
| 🥇 1 | `jardin_damier_pub.png` | 8.6MB | [PE] | Mejor candidata disponible |
| 🥈 2 | `cuisine_exterieure_pub.png` | 7.6MB | [PE] | — |
| 🥉 3 | `Aménagement paysager de la cour arrière.jpg` | 1.4MB | [PE] ⚠️ | Resolución baja — verificar calidad |

> ⚠️ Capturar en proyecto Rousseau esta semana — oportunidad inmediata.

---

### 9. MURS DE BÉTON 🔴 CRÍTICO
**Imágenes:** 2 | **Score promedio:** [PE] | **Estado:** 🔴 CRÍTICO — 3 por debajo del umbral
**Próxima oportunidad:** Sin obra activa de muros — planificar para próximo proyecto
**Última actualización:** 2026-06-25

| # | Archivo | Tamaño | Score | Uso recomendado |
|---|---------|--------|-------|----------------|
| 🥇 1 | `asphalte_mur_pub.png` | 7.1MB | [PE] | Único disponible |
| 🥈 2 | `mur_escalier_pub.png` | 7.1MB | [PE] | Compartido con Escaliers |

> 🔴 No lanzar campaña Murs de béton hasta tener mínimo 5 imágenes premium.

---

### 10. SIN CLASIFICAR ⚠️ REVISAR
**Archivo:** `2863ff2f-2292-4ce0-afaf-9b5d1bca7d52.jpg` | **Tamaño:** 9.4KB

> Nombre UUID + tamaño de 9.4KB — probable archivo corrupto o placeholder. Verificar y eliminar.

---

## PLAN DE ACCIÓN — COMPLETAR BIBLIOTECA

| Prioridad | Servicio | Acción | Cuándo | Quién |
|-----------|---------|--------|--------|-------|
| 🔵 #1 | **BALCON** | Evaluar scoring formal de 11 imágenes existentes | Esta semana | Claude |
| 🔵 #2 | **BALCON** | Capturar fotos reales Parisien (2x balcon + tourelle) | HOY | Matt |
| 🔴 #3 | **Murs de béton** | Planificar sesión en próximo proyecto | Próximas 2 semanas | Steven/Karim |
| ⚠️ #4 | **Aménagement Ext.** | Capturar Karine Rousseau — semana 4 | Esta semana | Steven |
| ⚠️ #5 | **Clôtures** | Capturar en próxima obra con clôture | Próximas 3 semanas | Campo |
| 🔵 #6 | Todos [PE] | Evaluación formal FLOAT_VISUAL_SCORE | Próxima sesión Claude | Claude |

---

## REGISTRO DE ACTUALIZACIONES

| Versión | Fecha | Cambio | Quién |
|---------|-------|--------|-------|
| v1.0 | 2026-06-25 | Creación — inventario inicial completo (62 activos) | Claude |
| v1.1 | 2026-06-25 | Alias semántico BALCON aplicado: terrasse+deck+pergola+patio élevé → BALCON pasa de 0 a 11 imágenes, Cour Arrière pasa de 10 a 8, Terrasse/Deck fusionado | Claude |

---

*COBERTURA_SERVICIOS.md — Jardín Ideal AI System · v1.1 · 2026-06-25*
*Actualizar cada vez que se agreguen imágenes o cambien las reglas de clasificación*
*Protocolo completo: `10_MEMORIA_EMPRESARIAL/PROTOCOLO_ACTIVOS_VISUALES.md`*
*Alias semánticos: `05_MARKETING/FLOAT_V2_PREMIUM/03_PREMIUM_VISUAL_SCORE.md`*
