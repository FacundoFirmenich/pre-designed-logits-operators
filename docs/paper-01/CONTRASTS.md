# Paper 01 · Contratos y contrastes / Contracts and contrasts

[Canon de arquitectura / Architecture canon](CANON.md)

## Castellano

**Intervención, soporte y mapa son objetos distintos.** Esquemáticamente: logits finales z; intervención full F(z); soporte S de QAS respecto de la referencia z; delta localizado 1_S·(F(z)−z); warper y muestreo; Z‑Explorer lee las salidas y sus controles. La expresión del delta es un contrato conceptual sobre coordenadas finitas, no una sustitución del código ni una afirmación de que proyección, máscaras y guardas numéricas conmuten. La máscara interna que TALON usa para calcular su delta y el soporte externo que QAS usa para localizarlo no son la misma cosa. Ninguno restringe por sí solo el conjunto de tokens elegibles.

| Pregunta | Contraste identificable | Reporte sin sobreclaim |
|---|---|---|
| ¿Qué añade la modulación Mass Right? | Baseline; control de temperatura efectiva; perturbación de control con preservación de top‑1. Mass Left puede aislar dirección si se mantienen iguales los otros parámetros. | En cada caso × semilla: corrección, formato, rescate, pérdida y empate. Registrar temperatura interna/externa, orden, presupuesto y punto de verificación top‑1. |
| ¿Qué retiene QAS del mismo brazo full? | Medición sobre el mismo prefijo para el efecto mecánico y generaciones emparejadas para el efecto conductual. | Coordenadas intervenidas, discrepancia distribucional, resultado y tiempo de pared/throughput, por separado. Un porcentaje pequeño de soporte no es aceleración. |
| ¿Qué encuentra Z que otros mapas no priorizan? | Mismas salidas nuevas y mismos controles para Z, distancia y entropía. Fijar referencia y regla de marcado; separar hallazgos y omisiones. | Caso, segmento, rival, componentes del score y razón de la divergencia. Exclusividad sólo frente a diagnósticos observados; la transformación no equivale a utilidad. |

La igualdad de semilla no garantiza por sí sola que se hayan acoplado los sorteos; documentar backend, política de aleatoriedad y unidad de emparejamiento. En análisis de incertidumbre no tratar las réplicas de semilla de un prompt como prompts independientes. Cuando los criterios estricto y numérico divergen, reportar ambos; no adjudicar un rescate matemático usando sólo formato.

**Comparadores por mecanismo.** Min‑p y Top‑H truncan soporte mediante criterios distintos; DoLa contrasta capas sin fine-tuning adicional. La temperatura global cambia escala, no implementa la modulación asimétrica de TALON. Esos métodos no son tipos intercambiables ni sus resultados publicados son scores emparejados con los nuestros. [Min‑p](https://arxiv.org/abs/2407.01082) · [Top‑H](https://arxiv.org/abs/2509.02510) · [DoLa](https://arxiv.org/abs/2309.03883).

Este documento define cómo distinguir afirmaciones, no autoriza nuevas corridas ni reconfigura las existentes. El freeze de la campaña conserva su identidad.

## English

**Intervention, support, and mapping are distinct objects.** Schematically: final logits z; full intervention F(z); QAS support S relative to z; localized delta 1_S·(F(z)−z); warper and sampling; Z‑Explorer reads outputs and controls. This describes finite-coordinate semantics, not executable code or a claim that projection, masks, and numerical guardrails commute. TALON's internal delta mask and QAS's external intervention support are distinct. Neither by itself truncates the eligible token set.

| Question | Identifiable comparison | Bounded report |
|---|---|---|
| What does Mass Right modulation add? | Baseline, matched effective temperature, and a top‑1-preserving perturbation control. Mass Left can isolate direction if other parameters match. | Per case × seed: correctness, format, rescues, losses, and ties. Record internal/external temperature, order, budget, and the top‑1 measurement point. |
| What does QAS retain of the same full arm? | Common-prefix mechanical measurement and matched generations for behavior. | Report affected coordinates, distributional discrepancy, outcomes, and wall time/throughput separately. Small support does not imply acceleration. |
| What does Z find that other maps do not prioritize? | Apply Z, distance, and entropy diagnostics to the same new outputs and controls. Fix reference and flagging rule; retain discoveries and misses. | Case, segment, comparator, score components, and source of the difference. Exclusivity is relative to observed diagnostics; transformation is not utility. |

Matching a seed does not establish coupled random draws. Record the backend, randomness policy, and pairing unit. Do not treat different seeds of one prompt as independent prompts. Report strict and numeric scoring separately when they disagree; format alone cannot establish mathematical rescue.

**Mechanistic comparators.** Min‑p and Top‑H truncate support using different criteria. DoLa contrasts layers without additional fine-tuning. Global temperature rescales logits without TALON's asymmetric modulation. These are not interchangeable methods and their published scores are not matched outcomes for our trials. [Min‑p](https://arxiv.org/abs/2407.01082) · [Top‑H](https://arxiv.org/abs/2509.02510) · [DoLa](https://arxiv.org/abs/2309.03883).

This document defines interpretive criteria; it does not authorize launches or reconfigure an existing experiment. The campaign freeze retains its identity.
