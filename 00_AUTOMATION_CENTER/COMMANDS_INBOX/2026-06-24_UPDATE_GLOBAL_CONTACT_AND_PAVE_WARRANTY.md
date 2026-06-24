# COMANDO GLOBAL — Actualizar email oficial y garantía pavé
**ID:** CMD-001
**TIPO:** GLOBAL
**FECHA_CREACION:** 2026-06-24
**PRIORIDAD:** ALTA
**ESTADO:** PENDIENTE
**APROBACION_HUMANA:** NO (correcciones técnicas locales, no publicación)
**EJECUTADO_POR:** Claude Code (cuando Daniel lo solicite)

---

## CONTEXTO

Daniel confirmó el 2026-06-24 dos datos oficiales de Jardín Ideal que deben propagarse a todos los archivos del sistema:

1. **Email oficial** para todas las landing pages: `info@jardin-ideal.com`
2. **Garantía pavé / pavé uni**: exactamente **5 ans** (solo este servicio)
3. **Garantía otros servicios**: "Garantie selon le type de projet, les matériaux sélectionnés et les conditions du contrat" (no inventar años específicos)

---

## ACCIONES A EJECUTAR

### ACCIÓN 1 — Aplicar email oficial en todas las LPs

**Buscar en todos los archivos HTML del repositorio:**
- Cualquier instancia de `daniel@groupe-ideal.com` en contexto de LP cliente
- Cualquier instancia de `contact@jardin-ideal.com` (si existe)
- Cualquier placeholder `[EMAIL]`, `votre@email.com`, `email@entreprise.com`

**Regla de aplicación:**
- Si el email aparece en formulario, footer, política de privacidad o sección de contacto de LP → reemplazar por `info@jardin-ideal.com`
- Si el email aparece en documentación interna de Claude Code (notas operacionales) → mantener `daniel@groupe-ideal.com` como correo interno
- Si ya dice `info@jardin-ideal.com` → no cambiar nada (ya correcto)

**Archivos en scope:**
```
05_MARKETING/LANDING_PAGES/**/*.html
00_INBOX_MANUS/LANDING_PAGES/**/*.html
00_OUTBOX_CLAUDE_PARA_MANUS/**/*.md (si contienen email para cliente)
```

---

### ACCIÓN 2 — Aplicar garantía pavé 5 ans

**Buscar en todos los archivos del repositorio:**
- Cualquier texto que diga garantía de 5, 10, o X años para servicios que NO sean pavé/pavé uni
- Cualquier "Garantie X ans" aplicado genéricamente a "tous les travaux"
- Cualquier "Garantie 5 ans" en hotspot de piscine, terrasse, clôture, pergola, etc.

**Regla de aplicación:**
- Servicio = Pavé / Pavé uni → "Garantie de 5 ans sur les travaux de pavé" ✅
- Servicio = cualquier otro → "Garantie selon le type de projet, les matériaux sélectionnés et les conditions du contrat" ✅
- Trust pill genérico "Garantie 5 ans" en hero → acceptable si se refiere al servicio principal de pavé de la LP

**Archivos en scope:**
```
05_MARKETING/LANDING_PAGES/**/*.html
00_INBOX_MANUS/LANDING_PAGES/**/*.html
00_OUTBOX_CLAUDE_PARA_MANUS/PROMPTS_MANUS/**/*.md
00_OUTBOX_CLAUDE_PARA_MANUS/PAQUETES_CONTEXT_MANUS/**/*.md
```

---

### ACCIÓN 3 — Actualizar reglas de marca

Verificar que los siguientes documentos ya reflejan los datos confirmados (si fueron creados en esta sesión, probablemente ya están correctos):

- `00_OUTBOX_CLAUDE_PARA_MANUS/PAQUETES_CONTEXT_MANUS/ACTUAL/02_REGLAS_DE_MARCA_Y_ESTILO.md`
- `00_OUTBOX_CLAUDE_PARA_MANUS/PAQUETES_CONTEXT_MANUS/ACTUAL/03_REGLAS_LANDING_PAGES.md`
- `05_MARKETING/LANDING_PAGES/COUR_ARRIERE/CHANGEMENTS_TECHNIQUES.md`

Si algún documento dice `[CONFIRMAR EMAIL]`, `[EMAIL PENDIENTE]` o variante → actualizar a `info@jardin-ideal.com`.

---

### ACCIÓN 4 — Generar reporte de archivos afectados

Después de completar las acciones 1-3, crear un reporte en:
```
00_AUTOMATION_CENTER/PATCHES/2026-06-24_GLOBAL_PATCH_EMAIL_GARANTIE.md
```

El reporte debe incluir:
- Lista completa de archivos revisados
- Lista de archivos modificados (con líneas cambiadas)
- Lista de archivos sin cambios necesarios (ya correctos)
- Lista de archivos donde no aplicó (contexto interno, correcto mantener)

---

### ACCIÓN 5 — Mover este comando a COMMANDS_DONE

Cuando todas las acciones anteriores estén completas y el commit esté hecho:

```
MOVER: 00_AUTOMATION_CENTER/COMMANDS_INBOX/2026-06-24_UPDATE_GLOBAL_CONTACT_AND_PAVE_WARRANTY.md
HACIA: 00_AUTOMATION_CENTER/COMMANDS_DONE/2026-06-24_UPDATE_GLOBAL_CONTACT_AND_PAVE_WARRANTY.md
```

Añadir al final del archivo:
```markdown
## RESULTADO DE EJECUCIÓN
ESTADO: COMPLETADO
FECHA_EJECUCION: [fecha real]
COMMIT: [hash]
ARCHIVOS_MODIFICADOS: [N]
ARCHIVOS_SIN_CAMBIOS: [N]
```

---

## LO QUE ESTE COMANDO NO HACE

- **No publica** ninguna landing page
- **No activa** ninguna campaña
- **No modifica** textos legales (política de privacidad)
- **No cambia** precios, cálculos de estimación ni fórmulas
- **No toca** Meta Pixel ID ni Zapier webhook (pendientes de Daniel)
- **No cambia** testimonios reales de clientes
- **No reescribe** archivos completos — solo reemplazos específicos

---

## CRITERIO DE ÉXITO

El comando se considera completado cuando:
1. `grep -r "daniel@groupe-ideal.com" ./05_MARKETING/LANDING_PAGES/` devuelve 0 resultados
2. `grep -r "Garantie [0-9]* ans" ./05_MARKETING/LANDING_PAGES/` solo muestra resultados para pavé/pavé uni
3. Reporte de patch generado en `PATCHES/`
4. Commit pusheado al repositorio
5. Este archivo está en `COMMANDS_DONE/`

---

## DATOS CONFIRMADOS (referencia)

| Dato | Valor | Confirmado por | Fecha |
|------|-------|---------------|-------|
| Email oficial LPs | info@jardin-ideal.com | Daniel | 2026-06-24 |
| Email interno | daniel@groupe-ideal.com | Daniel | 2026-06-24 |
| Garantie pavé / pavé uni | 5 ans | Daniel | 2026-06-24 |
| Garantie otros servicios | Según contrato | Daniel | 2026-06-24 |
| Meta Pixel ID | ⏳ PENDIENTE | — | — |
| Zapier webhook | ⏳ PENDIENTE | — | — |

---

*Comando CMD-001 — Jardín Ideal Automation Center · 2026-06-24*
*Para ejecutar: "Claude Code, ejecuta el comando CMD-001" o "ejecuta el UPDATE_GLOBAL"*
