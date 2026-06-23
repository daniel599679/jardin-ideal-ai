# CONFIGURACIÓN GLOBAL — EMPRESA ACTIVA
**Archivo de configuración del ecosistema IA**
**Última actualización:** 2026-06-23

---

## ESTADO ACTUAL

```
EMPRESA_ACTIVA = JARDIN_IDEAL
```

---

## INSTRUCCIÓN PARA TODOS LOS AGENTES

**Antes de ejecutar cualquier tarea, leer este archivo.**

El valor de `EMPRESA_ACTIVA` determina:
- Qué perfil de empresa cargar
- Qué logos utilizar
- Qué servicios están disponibles
- Qué teléfono y web incluir en los CTAs

---

## CÓMO CAMBIAR DE EMPRESA

Editar la línea `EMPRESA_ACTIVA =` arriba.

```
# Para Jardín Ideal:
EMPRESA_ACTIVA = JARDIN_IDEAL

# Para Groupe Ideal:
EMPRESA_ACTIVA = GROUPE_IDEAL
```

---

## RUTAS QUE CAMBIAN SEGÚN EMPRESA_ACTIVA

| Recurso | JARDIN_IDEAL | GROUPE_IDEAL |
|---------|-------------|--------------|
| Perfil | `01_EMPRESAS/JARDIN_IDEAL/PERFIL_EMPRESA.md` | `01_EMPRESAS/GROUPE_IDEAL/PERFIL_EMPRESA.md` |
| Servicios | `01_EMPRESAS/JARDIN_IDEAL/SERVICIOS/` | `01_EMPRESAS/GROUPE_IDEAL/SERVICIOS/` |
| Logos | `99_BRANDING_GLOBAL/logos/jardin ideal/` | `99_BRANDING_GLOBAL/logos/groupe ideal/` |
| Contenido | `01_EMPRESAS/JARDIN_IDEAL/CONTENIDO/` | `01_EMPRESAS/GROUPE_IDEAL/CONTENIDO/` |
| Reportes | `01_EMPRESAS/JARDIN_IDEAL/REPORTES/` | `01_EMPRESAS/GROUPE_IDEAL/REPORTES/` |
| Campañas | `01_EMPRESAS/JARDIN_IDEAL/CAMPANAS/` | `01_EMPRESAS/GROUPE_IDEAL/CAMPANAS/` |

---

## CAMPO OBLIGATORIO EN TODOS LOS DOCUMENTOS

Todo reporte, paquete, activo o entregable generado por el sistema debe incluir:

```
EMPRESA_ACTIVA: JARDIN_IDEAL
Fecha         : 2026-06-23
Agente        : [nombre del agente que generó el documento]
```
