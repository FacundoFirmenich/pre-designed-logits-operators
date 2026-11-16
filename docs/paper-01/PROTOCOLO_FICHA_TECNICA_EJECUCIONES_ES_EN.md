# Protocolo obligatorio de ficha técnica de ejecución / Mandatory run brief

**ID:** P01-OPS-RUN-BRIEF-001 · v1.0 · 2026-11-16. Protocolo del proyecto por instrucción del autor. Aplica a pilotos, corridas completas, reanudaciones y relanzamientos. No modifica los operadores ni autoriza gasto o publicación por sí mismo.

## Castellano

Antes de lanzar, **mostrar al autor una ficha en castellano y conservar la misma especificación con el manifiesto de ejecución**. Una ficha no es un log retrospectivo ni un resumen estadístico. Cambios de panel, operador, entorno, semilla, hardware o presupuesto requieren una revisión identificable, con la diferencia y su motivo. No convertir un cambio de entorno en «recalibración» del operador.

| Campo obligatorio | Contenido |
|---|---|
| Pregunta y contraste | Qué diferencia se quiere identificar, qué se mantiene fijo y qué conclusiones quedarían fuera. |
| Benchmark y prompts | Nombre, split, revisión y conjunto exacto de IDs; enlace o anexo con enunciados exactos y orden. Distinguir nuevos frente a qué inventario, reutilizados y no verificables. Declarar exclusiones y selección. No anunciar datos «nuevos» por un cambio de nombre. |
| Modelo y entorno | Modelo y revisión, proveedor y cuenta autorizada, hardware, pesos/quant y cómputo por separado, plantilla y modo de razonamiento, runtime y versiones. |
| Brazos y presupuesto | Operadores exactos y controles, temperatura por brazo, orden de operaciones, top-k/top-p u otros filtros, QAS u otros módulos on/off, semillas concretas, tope de tokens, plazos cuando apliquen y número total de celdas desglosado. Sondas se cuentan por separado de generaciones. |
| Evaluación | Evaluador y versión/reglas; tratamiento de empates, fallos de contrato, faltantes y timeouts. Presentar contrastes pareados por jurisdicción; no reemplazarlos por medias. |
| Operación y custodia | Ruta/ID del cuaderno y del plan sellado, estado real, checkpoint previsto, destino privado de evidencia, tope de gasto cuando aplique, condición de parada y prueba terminal exigida. Si no hay ID remoto, decir «preparado» o «sin lanzamiento confirmado», no «en marcha». |

Al iniciar, añadir el ID remoto de versión/ejecución, hora observada y estado. En cada checkpoint material informar de las celdas observadas frente a las previstas, fallos y qué evidencia existe. Al cerrar, verificar salida terminal y preservar resultados adversos; dar el resultado científico en el chat. Manifiestos privados (prompts privados, respuestas esperadas, rutas, datos de cuenta) se mantienen fuera de superficies públicas; una ficha pública usa sólo datos publicables o referencias apropiadas.

## English

Before a pilot, full run, resume, or rerun, **show the author a brief in Spanish and retain the same specification with the run manifest**. Record any change to the panel, operator, environment, seeds, hardware, or budget as a revision and give its reason. Pipeline changes are not operator recalibration.

| Required field | Content |
|---|---|
| Question and contrast | Target contrast, held-fixed conditions and limits on interpretation. |
| Benchmark and prompts | Name, split, revision, exact ordered IDs, and a link or appendix containing exact prompts. Classify as reused, novel relative to a named inventory, or unverified; record exclusions and selection. |
| Model and environment | Model and revision, provider and authorized account, hardware, weight representation and compute dtype separately, template/reasoning setting, runtime and versions. |
| Arms and budget | Exact arms and controls; temperature per arm, processing order, filters, QAS and other modules on/off; fixed seeds, token and time budgets, and complete cell arithmetic. Count probes separately. |
| Evaluation | Evaluator and rules for ties, failed contracts, missing rows and timeouts. Retain paired within-jurisdiction contrasts; aggregates do not replace them. |
| Execution and custody | Notebook and frozen plan identifiers, actual state, checkpoint schedule, private evidence destination, spend limit when applicable, stop condition and terminal evidence. Without a remote run ID, do not report a launch as confirmed. |

Record the observed start time, remote version/run identity and state at launch. Report observed versus planned cells at material checkpoints and preserve failures. At closure verify terminal outputs and explain the scientific result in chat. Keep private manifests and operational details off public surfaces.
