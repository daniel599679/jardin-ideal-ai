# DECISIONES ESTRATÉGICAS
**Última actualización:** 2026-06-23
**Propósito:** Registro de decisiones importantes para no repetir debates.

---

## DECISIONES DE SISTEMA

### DS-001 — Arquitectura dual empresa
**Fecha:** 2026-06-23
**Decisión:** Un solo repositorio y ecosistema IA gestiona Jardín Ideal y Groupe Ideal.
**Motivo:** Máximo de metodología compartida, cero duplicación de trabajo.
**Implicación:** Todo agente lee `01_EMPRESAS/EMPRESA_ACTIVA.md` antes de ejecutar.
**Archivo:** `ECOSISTEMA_MAESTRO.md`

---

### DS-002 — FLOAT como sistema de contenido
**Fecha:** 2026-06-23
**Decisión:** No crear contenido individual ad hoc — todo pasa por el protocolo FLOAT.
**Motivo:** 60 minutos de trabajo humano por proyecto vs. 3-6 horas sin sistema.
**Implicación:** Todo proyecto completado → activar `CONTENT_OPERATING_SYSTEM.md`.
**Archivo:** `CONTENT_OPERATING_SYSTEM.md`

---

### DS-003 — Brand Style Guide como única fuente de verdad visual
**Fecha:** 2026-06-23
**Decisión:** `JARDIN_IDEAL_BRAND_STYLE_GUIDE_V1.md` es la referencia absoluta para todo contenido.
**Motivo:** Coherencia visual en Meta Ads, redes sociales, material impreso.
**Implicación:** Cualquier desviación requiere actualizar el guide, no crear excepciones.
**Paleta aprobada:** `#052B16` / `#008E3F` / `#C8A45A` (solo CTA) / `#F5F2EB` / `#FFFFFF`

---

### DS-004 — Dorado solo para CTA de teléfono
**Fecha:** 2026-06-23
**Decisión:** El color `#C8A45A` (dorado) se reserva exclusivamente para el CTA de teléfono.
**Motivo:** Principio de escasez visual — el dorado debe activar la acción de llamar.
**Implicación:** No usar dorado en títulos, iconos, bordes u otros elementos.

---

### DS-005 — Sistema de calificación de leads antes de cualquier visita
**Fecha:** 2026-06-23
**Decisión:** Todo lead califica 0–100 puntos antes de agendar visita.
**Motivo:** Visitas a leads C (<40 pts) son tiempo perdido. El vendedor llega preparado como consultor.
**Implicación:** Lead sin score → no se agenda. Visita sin LEAD_INTELLIGENCE_REPORT → no se realiza.
**Regla absoluta:** NUNCA visitar sin ambos tomadores de decisión presentes.
**Archivo:** `JARDIN_IDEAL_IDEAL_CUSTOMER_SYSTEM.md`

---

### DS-006 — Reunión 09:00 AM es inamovible
**Fecha:** Desde el inicio del sistema
**Decisión:** La reunión diaria de las 09:00 AM no puede ser desplazada por ninguna otra tarea.
**Motivo:** Es el momento de sincronización del equipo — decisiones del día se toman aquí.
**Implicación:** El Agente de Operaciones entrega briefing antes de las 09:00 AM.

---

### DS-007 — Forward slashes en rutas de hooks Claude Code (Windows)
**Fecha:** 2026-06-23
**Decisión:** Usar `/` en lugar de `\` en las rutas de scripts de hooks en `settings.json`.
**Motivo:** Claude Code (Node.js) trata las barras invertidas como secuencias de escape JavaScript, corrompiendo la ruta. Python en Windows acepta `/` igual que `\`.
**Implicación:** Cualquier nuevo hook en Windows debe usar `/` en la ruta.
**Ejemplo correcto:** `"python C:/Users/Daniel/.claude/speak.py"`

---

### DS-008 — Videos y ZIPs excluidos de Git
**Fecha:** 2026-06-23
**Decisión:** `*.mp4`, `*.mov`, `*.zip` están en `.gitignore` permanentemente.
**Motivo:** GitHub rechaza archivos >100MB. El ZIP del sistema pesa 319MB.
**Implicación:** El contenido audiovisual se gestiona fuera de Git (Google Drive o similar).

---

### DS-009 — Idioma de operación
**Fecha:** Desde el inicio
**Decisión:** Comunicación interna (Claude ↔ Daniel) en español. Todo lo que ve el cliente en francés.
**Motivo:** Coherencia con el mercado de Quebec y facilidad operativa del equipo.
**Implicación:** Prompts de agentes en español. Copys de campaña en francés.

---

### DS-010 — Priorización de ventas sobre todo
**Fecha:** Desde el inicio
**Decisión:** Orden de prioridad: Ventas → Eficiencia operativa → Documentación.
**Motivo:** Sin ventas no hay empresa. La documentación perfecta no compensa las ventas perdidas.
**Implicación:** Si hay un lead caliente y una tarea de documentación pendiente, el lead va primero.
