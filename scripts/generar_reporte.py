#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Motor de Reportes - Jardin Ideal
Uso:
  python generar_reporte.py diario
  python generar_reporte.py semanal
  python generar_reporte.py mensual
"""

import json
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path

# Forzar UTF-8 en stdout para Windows
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# ── Rutas base ────────────────────────────────────────────────────────────────
BASE_DIR    = Path(__file__).parent.parent
DATOS_DIR   = BASE_DIR / "00_DATOS_REALES"
REPORTES_DIR = BASE_DIR / "08_REPORTES"

HOY   = datetime.now().strftime("%Y-%m-%d")
AYER  = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
SEMANA = datetime.now().strftime("W%V")
MES   = datetime.now().strftime("%Y-%m")

# ── Colores de consola ────────────────────────────────────────────────────────
ROJO    = "\033[91m"
VERDE   = "\033[92m"
AMARILLO = "\033[93m"
RESET   = "\033[0m"
NEGRITA = "\033[1m"


def log(msg, nivel="info"):
    prefijos = {"ok": f"{VERDE}[OK]{RESET}   ", "warn": f"{AMARILLO}[AVISO]{RESET}",
                "error": f"{ROJO}[FALTA]{RESET}", "info": "        "}
    print(f"{prefijos.get(nivel, '        ')} {msg}")


# ── Lectura de datos ──────────────────────────────────────────────────────────
def leer_json(ruta):
    """Lee un JSON. Devuelve (datos, error_mensaje)."""
    p = Path(ruta)
    if not p.exists():
        return None, f"NO ENCONTRADO: {p.relative_to(BASE_DIR)}"
    try:
        with open(p, encoding="utf-8") as f:
            contenido = f.read().strip()
        if not contenido:
            return None, f"VACÍO: {p.relative_to(BASE_DIR)}"
        return json.loads(contenido), None
    except json.JSONDecodeError as e:
        return None, f"JSON INVÁLIDO en {p.name}: {e}"


def leer_todos_los_datos():
    """Lee todas las fuentes. Devuelve (datos_dict, alertas_list)."""
    datos = {}
    alertas = []

    fuentes = {
        "crm":          (DATOS_DIR / "CRM"        / f"leads_pipeline_{HOY}.json",    "crítico"),
        "leads":        (DATOS_DIR / "LEADS"       / f"leads_nuevos_{HOY}.json",      "crítico"),
        "meta_ads":     (DATOS_DIR / "META_ADS"    / f"meta_ads_{AYER}.json",         "crítico"),
        "google_ads":   (DATOS_DIR / "GOOGLE_ADS"  / f"google_ads_{AYER}.json",       "crítico"),
        "proyectos":    (DATOS_DIR / "PROYECTOS"   / "proyectos_activos.json",         "crítico"),
        "tareas":       (DATOS_DIR / "TAREAS"      / "tareas_pendientes.json",         "medio"),
        "materiales":   (DATOS_DIR / "MATERIALES"  / "materiales_pendientes.json",     "medio"),
        "fotos":        (DATOS_DIR / "FOTOS_VIDEOS"/ f"fotos_videos_{HOY}.json",       "bajo"),
        "operaciones":  (DATOS_DIR / "OPERACIONES" / "operaciones_hoy.json",           "medio"),
    }

    print(f"\n{NEGRITA}Leyendo fuentes de datos:{RESET}")
    for clave, (ruta, criticidad) in fuentes.items():
        d, err = leer_json(ruta)
        if err:
            nivel_log = "error" if criticidad == "crítico" else "warn"
            log(f"{clave.upper():<15} {err}", nivel_log)
            alertas.append({"fuente": clave, "criticidad": criticidad, "mensaje": err})
        else:
            log(f"{clave.upper():<15} OK — {ruta.name}", "ok")
            datos[clave] = d

    return datos, alertas


# ── Construcción del reporte ──────────────────────────────────────────────────
def construir_reporte_diario(datos, alertas):
    """Genera el markdown del reporte diario a partir de los datos JSON."""

    lineas = []
    lineas.append(f"# REPORTE DIARIO — JARDÍN IDEAL")
    lineas.append(f"**Fecha:** {HOY}  |  **Generado:** {datetime.now().strftime('%H:%M')}  |  **Sistema:** Motor de Reportes v1.0")
    lineas.append("")

    # ── Alertas de datos faltantes ────────────────────────────────────────────
    criticas = [a for a in alertas if a["criticidad"] == "crítico"]
    medias   = [a for a in alertas if a["criticidad"] == "medio"]

    if alertas:
        lineas.append("---")
        lineas.append("## ⚠️ ALERTAS DE DATOS")
        lineas.append("")
        for a in criticas:
            lineas.append(f"- 🔴 **{a['fuente'].upper()}** — {a['mensaje']}")
        for a in medias:
            lineas.append(f"- 🟡 **{a['fuente'].upper()}** — {a['mensaje']}")
        if criticas:
            lineas.append("")
            lineas.append("> Los datos marcados en 🔴 son críticos. Las secciones correspondientes")
            lineas.append("> muestran `[SIN DATOS]`. Actualizar los archivos y regenerar el reporte.")
        lineas.append("")

    # ── 1. Resumen ejecutivo ──────────────────────────────────────────────────
    lineas.append("---")
    lineas.append("## 01 · RESUMEN EJECUTIVO")
    lineas.append("")

    total_leads_hoy = 0
    if "leads" in datos:
        total_leads_hoy = datos["leads"].get("resumen", {}).get("total_leads_hoy", 0)
    else:
        total_leads_hoy = "[SIN DATOS]"

    gasto_meta = "[SIN DATOS]"
    cpl_meta   = "[SIN DATOS]"
    if "meta_ads" in datos:
        t = datos["meta_ads"].get("totales", {})
        gasto_meta = f"{t.get('gasto_total_cad', 0):.2f} CAD"
        cpl_meta   = f"{t.get('cpl_promedio_cad', 0):.2f} CAD"

    proyectos_activos = "[SIN DATOS]"
    bloqueos = "[SIN DATOS]"
    if "proyectos" in datos:
        r = datos["proyectos"].get("resumen", {})
        proyectos_activos = r.get("total_activos", 0)
        bloqueos = r.get("proyectos_con_bloqueo", 0)

    lineas.append(f"| Métrica | Valor |")
    lineas.append(f"|---------|-------|")
    lineas.append(f"| Leads nuevos hoy | {total_leads_hoy} |")
    lineas.append(f"| Gasto Meta Ads (ayer) | {gasto_meta} |")
    lineas.append(f"| CPL promedio Meta (ayer) | {cpl_meta} |")
    lineas.append(f"| Proyectos activos | {proyectos_activos} |")
    lineas.append(f"| Proyectos con bloqueo | {bloqueos} |")
    lineas.append("")

    # ── 2. Prioridades antes de las 09:00 AM ─────────────────────────────────
    lineas.append("---")
    lineas.append("## 02 · PRIORIDADES ANTES DE LAS 09:00 AM")
    lineas.append("")

    prioridades = []

    # Leads sin contactar
    if "leads" in datos:
        sin_contacto = datos["leads"].get("resumen", {}).get("sin_primer_contacto", 0)
        if sin_contacto > 0:
            prioridades.append(f"🔴 **CRÍTICO** — {sin_contacto} lead(s) sin primer contacto → revisar CRM ahora")
    elif "crm" in datos:
        sin_c = datos["crm"].get("alertas", {}).get("sin_contacto_mas_24h", 0)
        if sin_c > 0:
            prioridades.append(f"🔴 **CRÍTICO** — {sin_c} lead(s) sin contacto >24h → actuar antes del resto")

    # Materiales que bloquean obra
    if "materiales" in datos:
        bloquean = [p for p in datos["materiales"].get("pedidos", []) if p.get("bloquea_obra")]
        for mat in bloquean:
            prioridades.append(f"🔴 **CRÍTICO** — Material '{mat['material']}' bloquea {mat['proyecto_afectado']} → llamar {mat['proveedor']}")

    # Visitas sin confirmar
    if "operaciones" in datos:
        visitas = datos["operaciones"].get("visitas_tecnicas", [])
        for v in visitas:
            if not v.get("confirmado_cliente"):
                prioridades.append(f"🟠 **ALTO** — Visita {v['hora']} con {v['cliente']} sin confirmar → llamar antes de las 08:30")

    # Tareas críticas
    if "tareas" in datos:
        tcrit = [t for t in datos["tareas"].get("tareas", [])
                 if t.get("prioridad") == "critica" and t.get("estado") == "pendiente"]
        for t in tcrit:
            prioridades.append(f"🔴 **CRÍTICO** — {t['descripcion']} ({t.get('plazo', 'hoy')})")

    # Agenda reunión
    if "operaciones" in datos:
        if not datos["operaciones"].get("reunion_0900", {}).get("agenda_lista"):
            prioridades.append("🟠 **ALTO** — Preparar agenda reunión 09:00 AM (máx. 15 min)")

    if not prioridades:
        if criticas:
            lineas.append("_[SIN DATOS suficientes para calcular prioridades — ver alertas arriba]_")
        else:
            lineas.append("✅ Sin prioridades críticas detectadas en los datos actuales.")
    else:
        for i, p in enumerate(prioridades, 1):
            lineas.append(f"{i}. {p}")
    lineas.append("")

    # ── 3. Leads nuevos ───────────────────────────────────────────────────────
    lineas.append("---")
    lineas.append("## 03 · LEADS NUEVOS")
    lineas.append("")
    if "leads" not in datos:
        lineas.append("_[SIN DATOS — actualizar LEADS/leads_nuevos_{}.json]_".format(HOY))
    else:
        r = datos["leads"].get("resumen", {})
        lineas.append(f"**Total hoy:** {r.get('total_leads_hoy', 0)} leads")
        lineas.append("")
        lineas.append("| Fuente | Cantidad |")
        lineas.append("|--------|---------|")
        for fuente, cantidad in r.get("por_fuente", {}).items():
            if cantidad > 0:
                lineas.append(f"| {fuente.replace('_', ' ').title()} | {cantidad} |")

        leads_lista = datos["leads"].get("leads", [])
        sin_contacto = [l for l in leads_lista if not l.get("primer_contacto_realizado")]
        if sin_contacto:
            lineas.append("")
            lineas.append("**Leads sin primer contacto:**")
            for l in sin_contacto:
                horas = l.get("horas_esperando", "?")
                lineas.append(f"- {l['nombre']} | {l.get('fuente','')} | {l.get('servicio_interes','')} | esperando {horas}h")
    lineas.append("")

    # ── 4. Campañas activas ───────────────────────────────────────────────────
    lineas.append("---")
    lineas.append("## 04 · CAMPAÑAS ACTIVAS")
    lineas.append("")

    lineas.append("### Meta Ads")
    if "meta_ads" not in datos:
        lineas.append("_[SIN DATOS — actualizar META_ADS/meta_ads_{}.json]_".format(AYER))
    else:
        t = datos["meta_ads"].get("totales", {})
        lineas.append(f"**Gasto:** {t.get('gasto_total_cad',0):.2f} CAD  |  "
                      f"**Leads:** {t.get('leads_totales',0)}  |  "
                      f"**CPL:** {t.get('cpl_promedio_cad',0):.2f} CAD  |  "
                      f"**CTR:** {t.get('ctr_promedio_pct',0):.2f}%")
        lineas.append("")
        lineas.append("| Campaña | Gasto | Leads | CPL | CTR | Estado |")
        lineas.append("|---------|-------|-------|-----|-----|--------|")
        for c in datos["meta_ads"].get("campanas", []):
            estado_txt = {"normal": "[OK]", "atencion": "[ATENCIÓN]", "problema": "[PROBLEMA]", "pausada": "[PAUSADA]"}.get(c.get("estado",""), "?")
            cpl = c.get("cpl_cad")
            cpl_txt = f"{cpl:.0f} CAD" if cpl is not None else "N/D"
            lineas.append(f"| {c['nombre'][:30]} | {c.get('gasto_cad',0):.0f} CAD | "
                          f"{c.get('leads',0)} | {cpl_txt} | "
                          f"{c.get('ctr_pct',0):.1f}% | {estado_txt} |")

        alertas_meta = datos["meta_ads"].get("alertas", {})
        if alertas_meta.get("frecuencia_alta"):
            lineas.append(f"\n⚠️ Frecuencia >3.5: {', '.join(alertas_meta['frecuencia_alta'])} → rotar creatividades esta semana")

    lineas.append("")
    lineas.append("### Google Ads")
    if "google_ads" not in datos:
        lineas.append("_[SIN DATOS — actualizar GOOGLE_ADS/google_ads_{}.json]_".format(AYER))
    else:
        t = datos["google_ads"].get("totales", {})
        lineas.append(f"**Gasto:** {t.get('gasto_total_cad',0):.2f} CAD  |  "
                      f"**Leads:** {t.get('leads_totales',0)}  |  "
                      f"**CPL:** {t.get('cpl_promedio_cad',0):.2f} CAD  |  "
                      f"**CTR:** {t.get('ctr_promedio_pct',0):.2f}%")
        lineas.append("")
        lineas.append("| Campaña | Gasto | Leads | CPL | CTR | Estado |")
        lineas.append("|---------|-------|-------|-----|-----|--------|")
        for c in datos["google_ads"].get("campanas", []):
            estado_emoji = {"normal": "✅", "atencion": "⚠️", "problema": "🔴"}.get(c.get("estado",""), "❓")
            lineas.append(f"| {c['nombre'][:30]} | {c.get('gasto_cad',0):.0f} CAD | "
                          f"{c.get('conversiones',0)} | {c.get('cpl_cad',0):.0f} CAD | "
                          f"{c.get('ctr_pct',0):.1f}% | {estado_emoji} {c.get('estado','')} |")
    lineas.append("")

    # ── 5. Proyectos activos ──────────────────────────────────────────────────
    lineas.append("---")
    lineas.append("## 05 · PROYECTOS ACTIVOS")
    lineas.append("")
    if "proyectos" not in datos:
        lineas.append("_[SIN DATOS — actualizar PROYECTOS/proyectos_activos.json]_")
    else:
        proyectos = datos["proyectos"].get("proyectos", [])
        if not proyectos:
            lineas.append("Sin proyectos activos registrados.")
        else:
            lineas.append("| Proyecto | Cliente | Servicio | Etapa | Días | Bloqueo |")
            lineas.append("|----------|---------|----------|-------|------|---------|")
            for p in proyectos:
                bloqueo_txt = "🔴 " + p["descripcion_bloqueo"][:40] if p.get("bloqueo_activo") else "✅"
                lineas.append(f"| {p['id']} | {p['cliente'][:20]} | {p['servicio']} | "
                              f"{p['etapa']} | {p['dias_transcurridos']}/{p['dias_estimados']} | {bloqueo_txt} |")
    lineas.append("")

    # ── 6. Tareas críticas ────────────────────────────────────────────────────
    lineas.append("---")
    lineas.append("## 06 · TAREAS CRÍTICAS")
    lineas.append("")
    if "tareas" not in datos:
        lineas.append("_[SIN DATOS — archivo TAREAS/tareas_pendientes.json no encontrado]_")
    else:
        tareas = [t for t in datos["tareas"].get("tareas", [])
                  if t.get("estado") == "pendiente"]
        criticas_t = [t for t in tareas if t.get("prioridad") == "critica"]
        altas_t    = [t for t in tareas if t.get("prioridad") == "alta"]

        if criticas_t:
            lineas.append("**Críticas:**")
            for t in criticas_t:
                lineas.append(f"- 🔴 [{t['agente']}] {t['descripcion']} — {t.get('responsable','')} — plazo: {t.get('plazo','hoy')}")
        if altas_t:
            lineas.append("\n**Altas:**")
            for t in altas_t:
                lineas.append(f"- 🟠 [{t['agente']}] {t['descripcion']} — {t.get('responsable','')} — plazo: {t.get('plazo','hoy')}")
        if not criticas_t and not altas_t:
            lineas.append("✅ Sin tareas críticas o altas pendientes.")
    lineas.append("")

    # ── 7. Siguientes acciones ────────────────────────────────────────────────
    lineas.append("---")
    lineas.append("## 07 · SIGUIENTES ACCIONES")
    lineas.append("")

    acciones = []

    if "crm" in datos:
        seg_hoy = datos["crm"].get("alertas", {}).get("seguimientos_vencen_hoy", [])
        for s in seg_hoy:
            acciones.append(f"CRM — Seguimiento con {s['nombre']}: {s['tipo']}")

    if "operaciones" in datos:
        for v in datos["operaciones"].get("visitas_tecnicas", []):
            acciones.append(f"Operaciones — Visita {v['hora']}: {v['cliente']} ({v['proposito']})")

    if "proyectos" in datos:
        for p in datos["proyectos"].get("proyectos", []):
            if p.get("bloqueo_activo"):
                acciones.append(f"Operaciones — Resolver bloqueo {p['id']}: {p['descripcion_bloqueo'][:50]}")

    if not acciones:
        lineas.append("_Completar con las acciones del día una vez revisados todos los datos._")
    else:
        for i, a in enumerate(acciones, 1):
            lineas.append(f"{i}. {a}")

    lineas.append("")
    lineas.append("---")
    lineas.append(f"_Reporte generado automáticamente por el Motor de Reportes Jardín Ideal — {datetime.now().strftime('%Y-%m-%d %H:%M')}_")
    lineas.append("_El prompt maestro fue usado como instrucción, no como contenido de este reporte._")

    return "\n".join(lineas)


def construir_reporte_semanal(datos, alertas):
    """Genera el markdown del reporte semanal."""
    iso_semana = datetime.now().isocalendar()
    semana_str = f"W{iso_semana.week:02d}"
    inicio_semana = datetime.now() - timedelta(days=datetime.now().weekday())
    fin_semana    = inicio_semana + timedelta(days=6)

    lineas = []
    lineas.append(f"# REPORTE SEMANAL — JARDÍN IDEAL")
    lineas.append(f"**Semana:** {semana_str} · {inicio_semana.strftime('%d')}–{fin_semana.strftime('%d %B %Y')}  |  "
                  f"**Generado:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lineas.append("")

    if alertas:
        lineas.append("---")
        lineas.append("## ⚠️ DATOS FALTANTES PARA ESTA SEMANA")
        for a in alertas:
            lineas.append(f"- {'🔴' if a['criticidad']=='crítico' else '🟡'} **{a['fuente'].upper()}** — {a['mensaje']}")
        lineas.append("")
        lineas.append("> Para un reporte semanal completo, los reportes diarios de lunes a viernes")
        lineas.append("> deben existir en 08_REPORTES/. Este reporte consolida los datos disponibles.")
        lineas.append("")

    lineas.append("---")
    lineas.append("## BLOQUE 1 — RESUMEN EJECUTIVO")
    lineas.append("")
    lineas.append("| Métrica | Esta semana | Objetivo semanal |")
    lineas.append("|---------|------------|-----------------|")
    lineas.append("| Leads totales | [ver datos diarios] | ≥25 |")
    lineas.append("| CPL promedio | [ver META_ADS + GOOGLE_ADS] | <75 CAD |")
    lineas.append("| Proyectos cerrados | [ver CRM] | — |")
    lineas.append("| Valor cerrado | [ver CRM] | — |")
    lineas.append("")

    # Datos de hoy como proxy del estado semanal
    if "meta_ads" in datos:
        t = datos["meta_ads"].get("totales", {})
        lineas.append("**Datos más recientes disponibles (Meta Ads):**")
        lineas.append(f"- Gasto (ayer): {t.get('gasto_total_cad',0):.2f} CAD")
        lineas.append(f"- Leads (ayer): {t.get('leads_totales',0)}")
        lineas.append(f"- CPL (ayer): {t.get('cpl_promedio_cad',0):.2f} CAD")
        lineas.append(f"- CTR (ayer): {t.get('ctr_promedio_pct',0):.2f}%")
        lineas.append("")

    if "proyectos" in datos:
        r = datos["proyectos"].get("resumen", {})
        lineas.append("**Estado operaciones (actual):**")
        lineas.append(f"- Proyectos activos: {r.get('total_activos',0)}")
        lineas.append(f"- Proyectos con bloqueo: {r.get('proyectos_con_bloqueo',0)}")
        lineas.append(f"- Entregas esta semana: {r.get('entregas_esta_semana',0)}")
        lineas.append("")

    lineas.append("---")
    lineas.append("## BLOQUE 2 — LEADS Y CRM")
    lineas.append("")
    lineas.append("_Consolidar sumando los campos `resumen.total_leads_hoy` de los 5 reportes diarios de la semana._")
    lineas.append("")

    if "crm" in datos:
        pipeline = datos["crm"].get("pipeline", {})
        lineas.append("**Pipeline al cierre de semana:**")
        lineas.append("")
        lineas.append("| Etapa | Leads |")
        lineas.append("|-------|-------|")
        for etapa, leads in pipeline.items():
            lineas.append(f"| {etapa.replace('_',' ').title()} | {len(leads)} |")
        ind = datos["crm"].get("indicadores", {})
        lineas.append(f"\n**Valor pipeline activo:** {ind.get('valor_pipeline_cad', '[N/D]')} CAD")
    else:
        lineas.append("_[SIN DATOS CRM]_")

    lineas.append("")
    lineas.append("---")
    lineas.append("## BLOQUE 3 — MARKETING DE PAGO")
    lineas.append("")
    lineas.append("_Ver sección de campañas en los reportes diarios de la semana para consolidado._")
    lineas.append("")

    if "meta_ads" in datos or "google_ads" in datos:
        lineas.append("| Plataforma | Gasto (último día) | Leads | CPL |")
        lineas.append("|------------|-------------------|-------|-----|")
        if "meta_ads" in datos:
            t = datos["meta_ads"]["totales"]
            lineas.append(f"| Meta Ads | {t.get('gasto_total_cad',0):.2f} CAD | {t.get('leads_totales',0)} | {t.get('cpl_promedio_cad',0):.2f} CAD |")
        if "google_ads" in datos:
            t = datos["google_ads"]["totales"]
            lineas.append(f"| Google Ads | {t.get('gasto_total_cad',0):.2f} CAD | {t.get('leads_totales',0)} | {t.get('cpl_promedio_cad',0):.2f} CAD |")

    lineas.append("")
    lineas.append("---")
    lineas.append("## BLOQUE 4 — PLAN PARA LA SEMANA QUE INICIA")
    lineas.append("")

    if "tareas" in datos:
        tareas = [t for t in datos["tareas"].get("tareas", []) if t.get("estado") == "pendiente"]
        if tareas:
            lineas.append("**Tareas abiertas que pasan a la próxima semana:**")
            for t in tareas:
                lineas.append(f"- [{t['agente']}] {t['descripcion']}")
    lineas.append("")

    lineas.append("---")
    lineas.append(f"_Reporte semanal generado automáticamente — {datetime.now().strftime('%Y-%m-%d %H:%M')}_")

    return "\n".join(lineas)


def construir_reporte_mensual(datos, alertas):
    """Genera el markdown del reporte mensual."""
    mes_nombre = datetime.now().strftime("%B %Y")

    lineas = []
    lineas.append(f"# REPORTE MENSUAL — JARDÍN IDEAL")
    lineas.append(f"**Mes:** {mes_nombre}  |  **Generado:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lineas.append(f"**Objetivo anual:** 7,000,000 CAD")
    lineas.append("")

    if alertas:
        lineas.append("---")
        lineas.append("## ⚠️ DATOS FALTANTES")
        lineas.append("")
        lineas.append("> El reporte mensual requiere todos los reportes semanales del mes.")
        lineas.append("> Los datos mostrados corresponden al estado actual disponible.")
        lineas.append("")
        for a in alertas:
            lineas.append(f"- {'🔴' if a['criticidad']=='crítico' else '🟡'} {a['fuente'].upper()} — {a['mensaje']}")
        lineas.append("")

    lineas.append("---")
    lineas.append("## SCORECARD DEL MES")
    lineas.append("")
    lineas.append("| KPI | Real | Objetivo | Estado |")
    lineas.append("|-----|------|---------|--------|")
    lineas.append("| Leads totales | [consolidar semanales] | 130 (junio) | — |")
    lineas.append("| CPL promedio | [consolidar] | <75 CAD | — |")
    lineas.append("| Proyectos cerrados | [consolidar] | — | — |")
    lineas.append("| Facturación | [consolidar] | — | — |")
    lineas.append("| Tasa de cierre | [consolidar] | >35% | — |")
    lineas.append("")

    if "meta_ads" in datos or "google_ads" in datos:
        lineas.append("---")
        lineas.append("## MARKETING DE PAGO — ESTADO ACTUAL")
        lineas.append("")
        lineas.append("_(Último día disponible — consolidar con histórico mensual)_")
        lineas.append("")
        if "meta_ads" in datos:
            t = datos["meta_ads"]["totales"]
            lineas.append(f"**Meta Ads (último día):** Gasto {t.get('gasto_total_cad',0):.2f} CAD · "
                          f"Leads {t.get('leads_totales',0)} · CPL {t.get('cpl_promedio_cad',0):.2f} CAD")
        if "google_ads" in datos:
            t = datos["google_ads"]["totales"]
            lineas.append(f"**Google Ads (último día):** Gasto {t.get('gasto_total_cad',0):.2f} CAD · "
                          f"Leads {t.get('leads_totales',0)} · CPL {t.get('cpl_promedio_cad',0):.2f} CAD")

    lineas.append("")
    lineas.append("---")
    lineas.append("## OPERACIONES DEL MES")
    lineas.append("")

    if "proyectos" in datos:
        r = datos["proyectos"].get("resumen", {})
        lineas.append(f"- Proyectos activos al cierre: {r.get('total_activos',0)}")
        lineas.append(f"- Proyectos con bloqueo: {r.get('proyectos_con_bloqueo',0)}")
        lineas.append(f"- Entregas programadas esta semana: {r.get('entregas_esta_semana',0)}")
    else:
        lineas.append("_[SIN DATOS DE PROYECTOS]_")

    lineas.append("")
    lineas.append("---")
    lineas.append("## ANÁLISIS Y APRENDIZAJES")
    lineas.append("")
    lineas.append("```")
    lineas.append("Qué funcionó este mes:    _______________________________________________")
    lineas.append("Qué no funcionó:          _______________________________________________")
    lineas.append("Causa probable:           _______________________________________________")
    lineas.append("Acción correctiva:        _______________________________________________")
    lineas.append("Dato sorprendente:        _______________________________________________")
    lineas.append("```")
    lineas.append("")
    lineas.append("---")
    lineas.append(f"_Reporte mensual generado automáticamente — {datetime.now().strftime('%Y-%m-%d %H:%M')}_")

    return "\n".join(lineas)


# ── Guardar reporte ───────────────────────────────────────────────────────────
def guardar_reporte(contenido, tipo):
    REPORTES_DIR.mkdir(parents=True, exist_ok=True)

    if tipo == "diario":
        nombre = f"reporte_diario_{HOY}.md"
    elif tipo == "semanal":
        nombre = f"reporte_semana_2026-{SEMANA}.md"
    elif tipo == "mensual":
        nombre = f"reporte_mensual_{MES}.md"
    else:
        nombre = f"reporte_{tipo}_{HOY}.md"

    ruta = REPORTES_DIR / nombre

    # No sobrescribir si ya existe
    if ruta.exists():
        timestamp = datetime.now().strftime("%H%M%S")
        nombre = nombre.replace(".md", f"_{timestamp}.md")
        ruta = REPORTES_DIR / nombre
        log(f"Archivo ya existe — guardando como: {nombre}", "warn")

    with open(ruta, "w", encoding="utf-8") as f:
        f.write(contenido)

    return ruta


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    tipo = sys.argv[1].lower() if len(sys.argv) > 1 else "diario"

    if tipo not in ("diario", "semanal", "mensual"):
        print(f"{ROJO}Error: tipo debe ser 'diario', 'semanal' o 'mensual'{RESET}")
        print("Uso: python generar_reporte.py [diario|semanal|mensual]")
        sys.exit(1)

    print(f"\n{NEGRITA}{'='*55}{RESET}")
    print(f"{NEGRITA}  MOTOR DE REPORTES - JARDIN IDEAL{RESET}")
    print(f"{NEGRITA}  Tipo: {tipo.upper()}  |  Fecha: {HOY}{RESET}")
    print(f"{NEGRITA}{'='*55}{RESET}")

    datos, alertas = leer_todos_los_datos()

    print(f"\n{NEGRITA}Generando reporte {tipo}...{RESET}")
    if tipo == "diario":
        contenido = construir_reporte_diario(datos, alertas)
    elif tipo == "semanal":
        contenido = construir_reporte_semanal(datos, alertas)
    else:
        contenido = construir_reporte_mensual(datos, alertas)

    ruta = guardar_reporte(contenido, tipo)

    print(f"\n{NEGRITA}{'='*55}{RESET}")
    log(f"Reporte generado exitosamente", "ok")
    print(f"\n  Archivo: {NEGRITA}{ruta.name}{RESET}")
    print(f"  Ruta:    {ruta}")

    datos_ok    = len(datos)
    datos_total = 9
    datos_falt  = len(alertas)
    print(f"\n  Fuentes: {datos_ok}/{datos_total} disponibles", end="")
    if datos_falt:
        print(f" · {AMARILLO}{datos_falt} con alerta{RESET}")
    else:
        print(f" · {VERDE}todas OK{RESET}")
    print(f"{NEGRITA}{'='*55}{RESET}\n")


if __name__ == "__main__":
    main()
