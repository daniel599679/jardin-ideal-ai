# DECISIONES ESTRATÉGICAS
**Última actualización:** 2026-06-25
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
**Motivo:** Claude Code (Node.js) trata las barras invertidas como secuencias de escape JavaScript, corrompiendo la ruta.
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

---

## DECISIONES ESTRATÉGICAS DE CAMPAÑA

### DS-011 — Balcones = Servicio Prioritario
**Fecha:** 2026-06-25
**Decisión:** Balcones es el servicio prioritario para contenido y campañas en junio–agosto 2026.
**Motivo:** Dato de campo confirmado (Cowork brief 25/06): 3 proyectos activos simultáneos ($145,000, 52% del portfolio), inicio de nuevo proyecto hoy (Parisien 2x Balcon + Tourelle $71K). Máximo contenido real disponible ahora mismo.
**Implicación:**
- Próxima campaña Meta a lanzar: Balcon (esta semana)
- Contenido FLOAT: Balcon = prioridad #1 sobre cualquier otro servicio
- Budget sugerido campaña Balcon: $25–40/día
- CPL objetivo: <$35 CAD
**Proyectos fuente de contenido:** Parisien, Breault, Goudreault
**Revisión:** 2026-08-01 (post temporada alta)

---

### DS-012 — Cour Arrière = Campaña Ganadora Actual
**Fecha:** 2026-06-25 (confirmado desde datos 24/06)
**Decisión:** Cour arrière es la campaña activa con mejor rendimiento — mantener y escalar.
**Dato que la sostiene:** CPL $23.72 — 12 leads en 17 días — mejor resultado de todas las campañas.
**Acción:** Presupuesto $30/día → $55/día.
**Implicación:** No pausar esta campaña bajo ninguna circunstancia mientras el CPL esté ≤$35.

---

### DS-013 — Cour Avant = Pausada
**Fecha:** 2026-06-25 (decisión tomada 24/06)
**Decisión:** Campaña cour avant pausada hasta reevaluación.
**Motivo:** 0 leads en 17 días. $67.31 gastados sin resultado. Sin justificación de reactivar ahora.
**Condición de reactivación:** Nuevas creatividades FLOAT V2 + presencia de material de obra real.
**Revisión:** 2026-07-15

---

### DS-014 — Baños = Pausada
**Fecha:** 2026-06-25 (decisión tomada 24/06)
**Decisión:** Campaña BANOS (Groupe Ideal) pausada hasta reevaluación.
**Motivo:** 0 leads en 30 días. $44.76 gastados sin resultado. Sin proyectos activos en campo.
**Condición de reactivación:** Material real de obra + redefinición de audiencia y creatividades.
**Revisión:** 2026-07-15

---

### DS-015 — Piscinas = Bajo Revisión
**Fecha:** 2026-06-25
**Decisión:** Campaña piscines activa pero en observación. No pausar todavía.
**Motivo:** CPL $146.07 — supera umbral de alerta $100 CAD. Sin embargo, hay 1 proyecto completado (St-Hilaire $50K) que puede servir de contenido.
**Condición de pausa:** Si no hay nuevos leads en 7 días → pausar y reasignar presupuesto a Balcon.
**Revisión:** 2026-07-02
**Alternativa:** Planificar campaña con material real del proyecto St-Hilaire para agosto (pre-temporada 2027).

---

### DS-016 — Obras Reales = Fuente Principal de Contenido
**Fecha:** 2026-06-25
**Decisión:** Todo contenido de marketing debe basarse primero en proyectos reales activos o recién completados. No crear contenido genérico cuando hay obras disponibles.
**Motivo:** Dato de campo (brief 25/06): 6 proyectos activos con material visual disponible. Contenido real convierte mejor y es más auténtico para el mercado de Quebec.
**Jerarquía de fuentes:**
1. Proyectos activos en campo hoy (fotos/video en tiempo real)
2. Proyectos completados esta semana
3. Proyectos completados este mes
4. Biblioteca Francisco (archivo)
5. Stock/recreaciones — ÚLTIMA OPCIÓN
**Implicación:** Antes de producir cualquier pieza, consultar `PROJECT_REGISTRY/MANUS_PROJECTS.md` y el snapshot operativo del día.

---

### DS-017 — Reglas de Alerta Automática del Sistema
**Fecha:** 2026-06-25
**Decisión:** El sistema genera alertas automáticas en las siguientes condiciones. No esperar a la reunión de 09:00 AM para escalar.

| Condición | Umbral | Acción |
|-----------|--------|--------|
| Leads estancados "Nouveau lead reçu" | >10 | Escalar a Daniel inmediatamente |
| CPL de cualquier campaña | >$100 CAD | Revisar o pausar campaña |
| Campaña sin leads | 48 horas | Verificar status urgente |
| Contradicción producción real vs. campaña | Cualquiera | Reportar y proponer corrección |
| Lead A+ sin respuesta | >2 horas | Escalar a Daniel |
| Proyecto retrasado | >3 días | Comunicar al cliente |

---

### DS-018 — Claude Code = Fuente de Verdad / Manus = Editor Visual
**Fecha:** 2026-06-25
**Decisión:** Claude Code (GitHub) es la única fuente de verdad del sistema. Manus es exclusivamente el editor visual/prototipador. Ningún cambio técnico en landing pages se aplica primero en Manus.
**Motivo:** Evitar pérdida de control sobre el código. Los cambios deben fluir Claude Code → Manus, no al revés.
**Implicación:**
- Landing pages: cambios técnicos primero locales → luego Manus regenera si es visual
- Datos de marca (email, garantías, precios): solo los que Claude Code confirma son válidos
- Publicación: siempre requiere aprobación humana — Manus no publica directamente

---

*Decisiones Estratégicas — Jardín Ideal AI System · v2.0 · 2026-06-25*
*Actualizar con cada decisión importante tomada en reunión o sesión de trabajo*
