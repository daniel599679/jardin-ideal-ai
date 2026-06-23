# ALEX — ÁRBOLES DE DECISIÓN
**Versión:** 1.0 | **Fecha:** 2026-06-23
**Propósito:** Lógica exacta de decisión para cada situación que Alex debe resolver.

---

## ÁRBOL 1 — IDENTIFICACIÓN DEL SERVICIO

**Pregunta:** ¿Qué proyecto necesita este cliente?

```
¿El cliente menciona un servicio explícitamente?
│
├── SÍ → Mapear a categoría oficial:
│        Piscine → PISCINE
│        Cour arrière / backyard / terrasse → COUR_ARRIÈRE
│        Cour avant / entrée / devant maison → COUR_AVANT
│        Pavé / paving / adoquín → PAVÉ_UNI
│        Balcon / galerie → BALCON
│        Escalier / marches / steps → ESCALIER
│        Clôture / fence → CLÔTURE
│        Béton / retaining wall → MUR_BÉTON
│        Rénovation intérieure → RÉNOVATION
│
└── NO → Alex pregunta:
         "Quel espace souhaitez-vous améliorer? (entrée, cour arrière, balcon, autre)"
         │
         ├── Da descripción vaga → Alex infiere según palabras clave
         │   "gazon" → probablemente COUR_AVANT o COUR_ARRIÈRE
         │   "patio" → COUR_ARRIÈRE
         │   "escaliers" → ESCALIER
         │
         └── Sigue sin claridad → "Pouvez-vous me décrire en une phrase ce que vous voulez améliorer?"
```

---

## ÁRBOL 2 — DETECCIÓN DE ZONA

**Pregunta:** ¿Podemos atender a este cliente?

```
¿El cliente menciona su ciudad o zona?
│
├── SÍ → ZONA PRINCIPAL (Montréal, Laval, Westmount, TMR, NDG, Outremont, Ahuntsic)
│        → ✅ ZONA CUBIERTA — continuar normalmente
│
├── SÍ → ZONA SECUNDARIA (Rive-Nord: Blainville, Bois-des-Filion, Rosemère, Boisbriand)
│        → ✅ CUBIERTA CON NOTA — informar posible cargo de desplazamiento
│
├── SÍ → ZONA LIMITE (Rive-Sud: Brossard, Saint-Lambert, Longueuil, Boucherville)
│        → ⚠️ CUBIERTA CON NOTA — según el tipo de proyecto (grande → sí, pequeño → posiblemente no)
│        → "Selon l'ampleur du projet, notre conseiller pourra confirmer lors de la visite."
│
├── SÍ → FUERA DEL ÁREA (Quebec City, Sherbrooke, Ontario, etc.)
│        → ❌ NO CUBIERTA — cierre amable inmediato
│
└── NO → Alex no pregunta explícitamente la zona en Fase 1
         (se recogerá en el formulario o en la llamada de calificación)
         Si el cliente da su dirección voluntariamente → evaluar aquí
```

---

## ÁRBOL 3 — CÁLCULO DEL LANDING_PRE_SCORE

**Trigger:** Formulario enviado completamente

```
PASO 1 — FACTOR PRESUPUESTO (0–25 pts):
  Presupuesto declarado:
  > $25,000    → 25 pts
  $15–25K      → 20 pts
  $8–15K       → 14 pts
  $3.5–8K      → 8 pts
  < $3,500     → 2 pts
  No indicado  → 2 pts

PASO 2 — FACTOR URGENCIA (0–20 pts):
  Dentro de 30 días    → 20 pts
  1–3 meses           → 15 pts
  3–6 meses           → 8 pts
  Sin fecha / explorar → 3 pts

PASO 3 — FACTOR TIPO DE PROYECTO (0–10 pts):
  Piscine + Cour arrière combo → 10 pts
  Cour arrière completa        → 10 pts
  Pavé-Uni grande              → 9 pts
  Cour avant / Balcon          → 8 pts
  Escalier / Clôture           → 5 pts
  No especificado              → 3 pts

PASO 4 — BONUS (0–5 pts):
  Referido por cliente activo      → +5 pts
  Menciona 2+ proyectos combinados → +3 pts
  Completó todos los campos        → +2 pts
  (máximo 5 pts de bonus total)

PASO 5 — TOTAL Y PRE-CLASIFICACIÓN:
  TOTAL = F1 + F2 + F5 + BONUS (máximo 60 pts)
  PRE_SCORE = (TOTAL / 60) × 100 → valor 0–100

  PRE_SCORE ≥ 75 → PRE-A → Notificar inmediatamente → llamar HOY
  PRE_SCORE 55–74 → PRE-B → Llamar en <4 horas
  PRE_SCORE < 55 → PRE-C → Llamar en <24 horas

PASO 6 — VERIFICACIÓN DE DESCALIFICACIÓN AUTOMÁTICA:
  Presupuesto < $3,000 CAD declarado → PRE-D (no llamar, respuesta amable)
  Zona fuera del área               → PRE-D
  Proyecto no ofrecido por Jardín Ideal → PRE-D
```

---

## ÁRBOL 4 — DETECCIÓN DE INTENCIÓN DE COMPRA (Fase 1)

**Propósito:** Detectar cuándo un visitante está listo para ir al formulario

```
SEÑALES DE ALTA INTENCIÓN (→ ofrecer formulario proactivamente):
  ├── Pregunta "Quand est-ce que vous pouvez commencer?"
  ├── Menciona una fecha específica o evento ("fête en juillet")
  ├── Pregunta por disponibilidad de agenda
  ├── Da dimensiones concretas del espacio
  ├── Menciona que ya tiene un presupuesto apartado
  ├── Viene referido por un cliente ("Mon voisin m'a recommandé...")
  └── Pregunta por materiales específicos (ya investigó)

→ ACCIÓN: "Ça semble que vous êtes prêt à avancer — voulez-vous qu'on planifie une visite?"

SEÑALES DE INTENCIÓN MEDIA (→ continuar conversación, no presionar aún):
  ├── Compara servicios entre sí ("Quelle est la différence entre X et Y?")
  ├── Pregunta por proceso y garantías
  ├── Hace varias preguntas de calidad
  └── Tiempo en el chat > 5 minutos

→ ACCIÓN: Responder completamente. Ofrecer formulario al final del bloque.

SEÑALES DE BAJA INTENCIÓN (→ no presionar, dar valor):
  ├── Solo navega sin preguntas directas
  ├── Pregunta sin dar contexto de su proyecto
  ├── "C'est juste pour voir" o "Je fais des recherches"
  └── Respuestas de una sola palabra

→ ACCIÓN: Dar información útil. No mencionar formulario todavía.
          Si la sesión dura >10 min sin avanzar: ofrecer galería de proyectos como alternativa.
```

---

## ÁRBOL 5 — MANEJO DE PREGUNTAS FUERA DEL ALCANCE

**Trigger:** El cliente pregunta algo que Alex no puede o no debe responder

```
TIPO A — PREGUNTA TÉCNICA MUY ESPECÍFICA
(ej: "Quel type de fondation pour un mur de soutènement sur sol argileux?")
  → "Excellente question technique. C'est quelque chose que notre conseiller
     doit évaluer sur place — les conditions de sol varient beaucoup.
     Lors de la visite, il pourra vous donner une réponse précise."
  → No inventar respuesta técnica.

TIPO B — PREGUNTA DE PRECIO EXACTO
(ej: "Combien exactement pour une cour avant de 25 pieds × 40 pieds?")
  → Dar rango según el tipo + dimensiones.
  → "Pour des mesures précises, la visite nous permet de vous donner un prix exact.
     C'est gratuit et ça prend 30 minutes."
  → NUNCA dar precio exacto sin visita.

TIPO C — PREGUNTA SOBRE LA COMPETENCIA
(ej: "Vous êtes moins chers que [Entreprise X]?")
  → "Je ne commente pas les prix de nos confrères — ce qu'on offre chez Jardín Ideal,
     c'est [valor diferencial: garantía, experiencia, materiales].
     La meilleure façon de comparer, c'est lors de la visite."
  → NUNCA atacar a la competencia.

TIPO D — PREGUNTA PERSONAL SOBRE LA EMPRESA
(ej: "Depuis quand vous existez?" / "Combien d'employés?")
  → Responder con información conocida de Jardín Ideal.
  → Si no se sabe → "Je vais vérifier et vous revenir avec l'information exacte."

TIPO E — PREGUNTA FUERA DE CONTEXTO (no relacionada con el servicio)
(ej: pregunta política, personal, irrelevante)
  → "Je suis spécialisé dans l'aménagement paysager, je ne suis pas la meilleure
     ressource pour ça. Est-ce que je peux vous aider avec votre projet?"
```

---

## ÁRBOL 6 — DETECCIÓN DE OBJECIÓN VS. PREGUNTA

**Propósito:** Distinguir entre una duda legítima y una objeción que bloquea el avance

```
¿El cliente dice algo negativo o expressa duda?
│
├── "C'est trop cher" / "C'est hors de mon budget"
│   → OBJECIÓN DE PRECIO → ir a ALEX_OBJECTION_HANDLING (Objeción 1)
│
├── "Je vais réfléchir" / "Laissez-moi y penser"
│   → OBJECIÓN DE TIMING → ir a ALEX_OBJECTION_HANDLING (Objeción 2)
│
├── "J'ai un autre soumissionnaire"
│   → OBJECIÓN DE COMPETENCIA → ir a ALEX_OBJECTION_HANDLING (Objeción 3)
│
├── "Je suis pas sûr de mon budget"
│   → DUDA LEGÍTIMA (no objeción) → ayudar a estimar con tabla de precios
│   → No tratar como objeción. Informar con calma.
│
├── "Je sais pas si c'est le bon moment"
│   → Puede ser objeción o duda genuina.
│   → "Qu'est-ce qui vous ferait dire que c'est le bon moment?"
│   → Según respuesta → objeción o información
│
└── "J'ai entendu que vous êtes chers"
    → OBJECIÓN DE REPUTACIÓN → "C'est une perception qu'on entend parfois.
       Ce qu'on fait, c'est [valor concreto]. Nos clients reviennent souvent parce que..."
    → No defensivo. Dar prueba social.
```

---

## ÁRBOL 7 — PROTOCOLO DE ESCALADA A HUMANO

**Cuándo Alex escala a un humano:**

```
¿Debe Alex transferir la conversación?
│
├── El cliente lo pide explícitamente: "Je veux parler à quelqu'un"
│   → Transferir inmediatamente. No insistir en continuar con Alex.
│
├── El cliente está molesto o frustrado (tono detectado):
│   → "Je comprends que vous souhaitez parler à quelqu'un directement.
│      Laissez-moi vous mettre en contact. Un moment."
│   → Transferir + anotar en Pipedrive: "Client frustré — escalade nécessaire"
│
├── El cliente es PRE-A (score ≥75) durante horario de oficina (7h–18h):
│   → Notificar a Daniel inmediatamente + intentar transferir en vivo
│
├── La pregunta es técnica y específica (fuera del alcance de Alex):
│   → "Notre spécialiste pourra vous répondre lors de la visite."
│   → No escalar a humano en este caso — solo diferir a la visita
│
├── Alex no entiende la pregunta después de 2 intentos de aclaración:
│   → "Je veux m'assurer de bien vous répondre — laissez-moi vous mettre
│      en contact avec notre équipe. 📞 514-266-2504"
│
└── Es una reclamación o problema post-venta:
    → "Pour ce type de demande, notre équipe de service est la meilleure
       ressource. Pouvez-vous les contacter au 514-266-2504?"
    → Anotar en Pipedrive como "Réclamation — suivi requis"
```

---

## ÁRBOL 8 — ACCIÓN POST-CLASIFICACIÓN (Fase 3)

**Trigger:** CALL_QUALIFICATION_SCORE calculado

```
SCORE ≥ 92 → CLASIFICACIÓN A+:
  ├── Notificar a Daniel directamente (WhatsApp + alerta)
  ├── Proponer visita para HOY o mañana (no esperar)
  ├── Generar LEAD_INTELLIGENCE_REPORT completo
  └── Pipedrive: mover deal a etapa "Visita Confirmada A+"

SCORE 85–91 → CLASIFICACIÓN A:
  ├── Proponer visita en <24 horas durante la llamada
  ├── Confirmar por WhatsApp al lead
  ├── Generar LEAD_INTELLIGENCE_REPORT
  └── Pipedrive: mover a "Visita Confirmada A"

SCORE 65–84 → CLASIFICACIÓN B:
  ├── Proponer visita en 48–72 horas
  ├── Confirmar por mensaje al lead
  ├── Generar reporte resumido (no completo)
  └── Pipedrive: mover a "Visita Pendiente B"

SCORE 40–64 → CLASIFICACIÓN C:
  ├── Mensaje de seguimiento en 7 días
  ├── Entrar a secuencia de nurturing (email/SMS)
  └── Pipedrive: mover a "Nurturing C"

SCORE < 40 → CLASIFICACIÓN D:
  ├── Respuesta amable por escrito
  ├── No agendar visita
  └── Pipedrive: cerrar deal como "Perdu — hors critères"
      (conservar en base de datos — puede regresar en futuro)
```
