# PROTOCOLO DE COMUNICACIÓN MANUS ↔ CLAUDE CODE
**Archivo:** `07_REPORTES/LANDING_PAGES/PROTOCOLO_MANUS_CLAUDE_CODE.md`
**Última actualización:** 2026-06-24
**Estado:** Activo

---

## Por qué existe este protocolo

Manus opera en servidores temporales con URLs del tipo `us2.manus.computer`. Estas URLs expiran cuando la sesión está inactiva y retornan `502 Bad Gateway`. Intentar que Claude Code acceda directamente a URLs de Manus es un flujo frágil que falla por diseño.

Este protocolo reemplaza el flujo por-URL con un flujo por-archivo local, que es estable, reproducible y no depende de sesiones activas.

**Lección aprendida el 2026-06-24:** Al analizar `lp-cour-arriere.html`, la URL de Manus respondió 502. El análisis tuvo que realizarse sin acceso al HTML real. Con este protocolo, ese escenario no vuelve a ocurrir.

---

## Flujo completo

```
┌─────────────────────────────────────────────────────────────────┐
│  MANUS — Entorno de ejecución (servidor temporal)               │
│                                                                  │
│  1. Manus crea prototipo de landing page                        │
│     ↓                                                            │
│  2. Usuario exporta HTML o ZIP desde Manus                      │
│     ↓                                                            │
│  3. Usuario guarda archivo en:                                   │
│     00_INBOX_MANUS/LANDING_PAGES/                               │
│     Nombre: YYYY-MM-DD_SERVICIO_VERSION_HTML.html               │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                    [archivo local guardado]
                               │
┌──────────────────────────────▼──────────────────────────────────┐
│  CLAUDE CODE — Entorno local                                     │
│                                                                  │
│  4. Lee el archivo HTML local (no por URL)                      │
│     ↓                                                            │
│  5. Analiza la estructura completa:                             │
│     - Secciones presentes / ausentes                            │
│     - Formularios: campos, validaciones, consentimiento         │
│     - Calculadoras: lógica, fórmulas, disclaimers              │
│     - Precios: niveles, claridad, cumplimiento                  │
│     - UX: mobile, navegación, CTAs                              │
│     - Legal: Loi 25, política de privacidad                     │
│     ↓                                                            │
│  6. Genera diagnóstico →                                        │
│     07_REPORTES/LANDING_PAGES/ANALISIS_[SERVICIO]_[VN].md      │
│     ↓                                                            │
│  7. Genera lista de correcciones →                              │
│     00_OUTBOX_CLAUDE_PARA_MANUS/CORRECCIONES/                   │
│     [FECHA]_[SERVICIO]_[VERSION]_CORRECCIONES.md               │
│     ↓                                                            │
│  8. Genera prompt completo para Manus →                         │
│     00_OUTBOX_CLAUDE_PARA_MANUS/PROMPTS_MANUS/                  │
│     [FECHA]_[SERVICIO]_PROMPT_SESION.md                        │
└──────────────────────────────┬──────────────────────────────────┘
                               │
               [usuario copia y pega prompt en Manus]
                               │
┌──────────────────────────────▼──────────────────────────────────┐
│  MANUS — Nueva sesión (reiniciada si hubo 502)                  │
│                                                                  │
│  9. Manus aplica correcciones al HTML                           │
│     ↓                                                            │
│  10. Usuario exporta nueva versión                              │
│      Nombre: YYYY-MM-DD_SERVICIO_V[N+1]_HTML.html              │
│      Guarda en: 00_INBOX_MANUS/LANDING_PAGES/                   │
└──────────────────────────────┬──────────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────────┐
│  CLAUDE CODE — Comparación de versiones                         │
│                                                                  │
│  11. Lee V_anterior y V_nueva                                   │
│  12. Genera DIFF:                                               │
│      - Cambios aplicados de la lista                            │
│      - Cambios faltantes                                        │
│      - Nuevos problemas introducidos                            │
│      - Veredicto: lista para publicar / requiere otra iteración │
│  13. Guarda comparación →                                       │
│      00_INBOX_MANUS/LANDING_PAGES/                              │
│      [FECHA]_[SERVICIO]_V[N]_DIFF.md                           │
└─────────────────────────────────────────────────────────────────┘
```

---

## Reglas del protocolo

### Regla 1 — No depender de URLs temporales de Manus
Claude Code nunca debe intentar hacer fetch a `*.manus.computer` como flujo principal. Si se intenta y retorna 502, la regla 2 aplica.

### Regla 2 — Si Manus responde 502, continuar con archivos locales
Si no hay archivo local disponible: documentar que el análisis está pendiente, notificar al usuario que debe exportar el HTML, y continuar con otras tareas.

Si hay archivo local de versión anterior: trabajar con ese archivo y documentar que el análisis corresponde a la versión anterior.

### Regla 3 — Si el HTML no existe localmente, pedir exportación
Mensaje estándar al usuario:
> "El archivo HTML de [SERVICIO] no está disponible en `00_INBOX_MANUS/LANDING_PAGES/`. Para continuar el análisis, exporta el HTML desde Manus y guárdalo con el nombre `YYYY-MM-DD_SERVICIO_VERSION_HTML.html`."

### Regla 4 — Todo análisis técnico basado en archivo local cuando exista
Si existe `00_INBOX_MANUS/LANDING_PAGES/YYYY-MM-DD_SERVICIO_VERSION_HTML.html`, ese archivo es la fuente de verdad — no una URL, no una captura, no descripción del usuario.

### Regla 5 — Idiomas de trabajo
- **Trabajo interno, diagnósticos, correcciones:** Español
- **Prompts para Manus que generan contenido visible al cliente:** Francés (Canada)
- **Código HTML/CSS/JS:** Comentarios en español, texto de UI en francés

### Regla 6 — Control de versiones de landing pages
- Nunca sobreescribir una versión existente
- Crear siempre una nueva versión (V1 → V2 → V3...)
- Mantener tabla de versiones en `FORMATO_NOMBRE_ARCHIVOS.md`
- Guardar DIFF entre versiones consecutivas

### Regla 7 — Datos y precios
- Todo análisis que detecte precios inventados o garantías no confirmadas debe marcarlo como Crítico
- El prompt generado para Manus siempre debe incluir la sección "REGLA FUNDAMENTAL — NO INVENTAR DATOS"

---

## Árbol de decisión — ¿Cómo proceder?

```
¿Hay archivo HTML local disponible?
│
├─ SÍ → Leer archivo local → Analizar → Generar diagnóstico + correcciones + prompt Manus
│
└─ NO → ¿La URL de Manus está accesible?
         │
         ├─ SÍ → Hacer fetch → Guardar localmente → Analizar
         │
         └─ NO (502) → ¿Hay versión anterior del mismo servicio?
                        │
                        ├─ SÍ → Analizar versión anterior → Documentar versión analizada
                        │
                        └─ NO → Notificar al usuario → Pedir exportación → Detener análisis
```

---

## Criterios de publicación — Cuándo una landing está lista

Una landing page está lista para conectarse a Meta Ads o Google cuando pasa TODOS estos criterios:

### Legal (bloqueante — no publicar sin estos)
- [ ] Política de privacidad presente y enlazada
- [ ] Checkbox de consentement en formulario soumission (Loi 25)
- [ ] Checkbox de consentement en formulario financiamiento
- [ ] Disclaimer en calculadora de estimación
- [ ] Disclaimer legal en calculadora de financiamiento (texto exacto aprobado)
- [ ] Precios marcados como estimativos ("environ", "à partir de")

### Técnico (bloqueante)
- [ ] Formulario soumission: mínimo 10 campos incluyendo consentement
- [ ] Todos los campos mapeados a Pipedrive via Zapier
- [ ] Nota automática generada en Pipedrive al recibir lead
- [ ] Teléfono clickeable (`tel:514-266-2504`) en header y footer
- [ ] Página funciona correctamente en mobile (375px)
- [ ] Velocidad de carga <3s (verificar con Lighthouse o similar)

### Contenido (bloqueante)
- [ ] Hero: imagen con score PREMIUM_VISUAL_SCORE ≥90/100
- [ ] Mínimo 6 réalisations avant/après (fotos reales, no stock)
- [ ] Mínimo 3 testimonios reales con barrio y tipo de proyecto
- [ ] FAQ: mínimo 10 preguntas

### Conversión (recomendado)
- [ ] CTA visible en los primeros 100px de la página (above the fold)
- [ ] Número de teléfono en color dorado en header
- [ ] Sticky CTA en mobile
- [ ] Calculadora de estimación operativa

---

## Historial de versiones por servicio

| Servicio | V1 | V2 | V3 | Estado actual | Publicada |
|----------|----|----|----|----|---|
| Cour Arrière | ⏳ pendiente exportar | — | — | Esperando HTML local | No |

*Actualizar esta tabla en cada ciclo de iteración.*

---

## Archivos relacionados

| Documento | Propósito |
|-----------|-----------|
| `00_INBOX_MANUS/README_MANUS_INBOX.md` | Cómo y qué guardar desde Manus |
| `00_INBOX_MANUS/LANDING_PAGES/FORMATO_NOMBRE_ARCHIVOS.md` | Convención de nombres |
| `00_OUTBOX_CLAUDE_PARA_MANUS/README_OUTBOX_MANUS.md` | Cómo leer los outputs de Claude Code |
| `00_OUTBOX_CLAUDE_PARA_MANUS/PROMPTS_MANUS/PROMPT_BASE_CORRECCION_LANDING.md` | Prompt maestro reutilizable |
| `07_REPORTES/LANDING_PAGES/ANALISIS_LP_COUR_ARRIERE.md` | Primer diagnóstico (sin archivo local) |
| `05_MARKETING/LANDING_PAGES/COUR_ARRIERE/PLAN_OPTIMISATION_LANDING.md` | Plan de 5 fases |
| `05_MARKETING/LANDING_PAGES/COUR_ARRIERE/CHANGEMENTS_TECHNIQUES.md` | Lista técnica de cambios |

---

*Jardín Ideal AI System · 2026-06-24*
*Protocolo activo — revisar y actualizar si cambian las condiciones de Manus o de Pipedrive*
