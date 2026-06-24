# README — SISTEMA DE APROBACIONES HUMANAS
**Automation Center — Jardín Ideal AI System**
**Versión:** 1.0 · **Fecha:** 2026-06-24

---

## PRINCIPIO FUNDAMENTAL

**Claude Code nunca publica, activa ni envía nada sin aprobación explícita de Daniel.**

La automatización está diseñada para preparar, corregir y organizar. La decisión final de cualquier acción que tenga impacto externo (visible para clientes, activa presupuesto, envía mensajes) siempre es humana.

---

## ACCIONES QUE SIEMPRE REQUIEREN APROBACIÓN

### 1. PUBLICAR LANDING PAGE

**Por qué:** Una landing publicada capta leads reales. Un error en el formulario, un texto ilegal o un cálculo incorrecto puede generar pérdidas o responsabilidades legales.

**Requisitos antes de aprobar:**
- [ ] Score auditoría Claude Code ≥ 85/100
- [ ] Formulario testado y enviando datos reales
- [ ] Meta Pixel ID real (no `TU_PIXEL_ID`)
- [ ] Zapier webhook configurado y testado
- [ ] Loi 25 checkboxes presentes y funcionales
- [ ] Texto legal revisado (no "Pré-approuvé", no garantías inventadas)
- [ ] Revisión en mobile completada
- [ ] Daniel aprueba explícitamente ("sí, publica" o equivalente)

**Cómo aprobar:** Daniel escribe en chat: `"Apruebo publicar [nombre LP]"` o mueve el archivo de APPROVAL_REQUIRED a una carpeta de confirmación.

---

### 2. ACTIVAR CAMPAÑA PUBLICITARIA

**Por qué:** Una campaña activa gasta presupuesto real desde el primer segundo. Sin validaciones previas, el dinero se pierde sin leads.

**Requisitos antes de aprobar:**
- [ ] Landing page publicada y funcionando
- [ ] Meta Pixel disparando `PageView` correctamente
- [ ] Formulario enviando a Pipedrive (test con lead real)
- [ ] Audiencia definida y revisada
- [ ] Budget diario confirmado por Daniel
- [ ] Copy de anuncios revisado (sin precios exactos inventados)
- [ ] Daniel aprueba explícitamente

---

### 3. SUBIR PRESUPUESTO DE CAMPAÑA

**Por qué:** Aumentar budget sin validar que el funnel convierte es dinero quemado.

**Requisitos antes de aprobar:**
- [ ] Datos de conversión de los últimos 7 días revisados
- [ ] Costo por lead actual documentado
- [ ] Nuevo budget diario confirmado por Daniel
- [ ] Landing page estable (sin errores reportados)

**Montos de referencia:**
- Budget actual (estimado): $35–$45/día
- Budget objetivo cour arrière: $55/día
- Cambios de más de $20/día requieren aprobación especial

---

### 4. CAMBIAR TEXTO LEGAL

**Por qué:** Los textos de política de privacidad, consentimiento (Loi 25) y financiamiento tienen implicaciones legales en Quebec. Un error puede resultar en multas o reclamaciones.

**Incluye:**
- Politique de confidentialité
- Textos de consentement (Loi 25)
- Disclaimers de financiamiento
- Garantías (no añadir garantías no confirmadas)
- Términos de contrato mencionados en LP

**Requisitos antes de aprobar:**
- [ ] Texto propuesto citado completamente en el comando
- [ ] Razón del cambio documentada
- [ ] Daniel confirma el texto palabra por palabra
- [ ] Si hay duda legal → consultar antes de aplicar

---

### 5. CAMBIAR CONFIGURACIÓN DE FINANCIAMIENTO

**Por qué:** Los cálculos de financiamiento se muestran a clientes potenciales. Un error puede crear expectativas falsas o compromisos imposibles de cumplir.

**Incluye:**
- Tasa de interés mostrada en calculadora
- Duración máxima/mínima de amortización
- Capital mínimo/máximo
- Texto del disclaimer de financiamiento
- Nombre del socio financiero (no mencionar "Desjardins" sin confirmación)

**Texto prohibido sin aprobación:** "Pré-approuvé", "Garanti", "Approuvé par [banco]"

---

### 6. PUBLICAR ANUNCIOS (Meta, Google, TikTok)

**Por qué:** Los anuncios son la cara pública de Jardín Ideal. Un error de copy, precio o promesa puede dañar la reputación o crear expectativas incorrectas.

**Incluye:**
- Anuncios de imagen (carrusel, imagen única)
- Anuncios de video (reel, video corto)
- Anuncios de texto (Google Search)
- Stories patrocinadas

**Requisitos antes de aprobar:**
- [ ] Copy revisado por Daniel
- [ ] Precios/offers son reales y actuales
- [ ] Landing de destino funcionando
- [ ] Pixel trackea correctamente
- [ ] Audiencia revisada

---

### 7. PUBLICAR IMÁGENES, VIDEOS, REELS O CARRUSELES (orgánico)

**Por qué:** El contenido orgánico en redes sociales construye o daña la reputación de marca. Aun siendo "gratuito", tiene impacto directo en la percepción del cliente.

**Incluye:**
- Posts en Instagram/Facebook
- Reels en Instagram/TikTok
- Carruseles educativos
- Stories orgánicas
- Posts en LinkedIn

**Requisitos:**
- [ ] Contenido revisado por Daniel o responsable de marketing
- [ ] Precios mencionados son actuales
- [ ] No hay errores ortográficos en francés
- [ ] Fecha de publicación confirmada
- [ ] Imágenes de proyectos: confirmar que son proyectos reales de Jardín Ideal

---

### 8. ENVIAR COMUNICACIONES A CLIENTES

**Por qué:** Emails, SMS o mensajes a clientes son irreversibles una vez enviados. Un error puede generar confusión, cancelaciones o quejas.

**Incluye:**
- Emails de seguimiento a leads
- Secuencias automatizadas de Zapier
- SMS de recordatorio
- Emails de confirmación de soumission
- Cualquier comunicación masiva

**Requisitos:**
- [ ] Texto del email revisado por Daniel
- [ ] Lista de destinatarios confirmada
- [ ] Mensaje de remitente correcto (`info@jardin-ideal.com`)
- [ ] Link de unsubscribe presente (si aplica)
- [ ] No contiene precios exactos sin confirmar

---

## CÓMO CREAR UNA SOLICITUD DE APROBACIÓN

Cuando Claude Code requiere aprobación antes de continuar, crea un archivo en `APPROVAL_REQUIRED/` con este formato:

```markdown
# APROBACIÓN REQUERIDA — [descripción breve]
FECHA: YYYY-MM-DD
TIPO: PUBLICAR_LP | ACTIVAR_CAMPANA | TEXTO_LEGAL | ...
PRIORIDAD: CRITICA | ALTA | MEDIA

## Qué se quiere hacer
[descripción clara de la acción]

## Por qué se necesita aprobación
[razón específica]

## Qué pasa si se aprueba
[consecuencia de aprobar]

## Qué pasa si se rechaza
[alternativa o estado actual]

## Checklist antes de aprobar
- [ ] Requisito 1
- [ ] Requisito 2

## Para aprobar
Escribir: "Apruebo [descripción]" en el chat con Claude Code
```

---

## ACCIONES QUE NO REQUIEREN APROBACIÓN

Claude Code puede ejecutar estas acciones de forma autónoma:
- Leer y analizar archivos HTML locales
- Generar reportes y diagnósticos
- Crear documentos de planificación y contexto
- Aplicar correcciones técnicas en archivos locales (sin publicar)
- Hacer commit y push de cambios locales al repositorio
- Crear paquetes de contexto para Manus
- Mover comandos de INBOX a DONE o FAILED
- Actualizar el CHANGELOG y LOGS

---

*README Approvals — Jardín Ideal Automation Center · v1.0 · 2026-06-24*
