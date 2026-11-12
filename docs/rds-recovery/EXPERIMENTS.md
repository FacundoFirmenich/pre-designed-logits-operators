# Registro experimental y programa prospectivo / Experiment record and prospective program

## Castellano

**Ancla de recuperación.** El registro y ledger de la superauditoría del 26 de junio preservan jurisdicciones de Qwen3.5 Base, Phi‑4, Qwen3‑VL y Gemma, con alcances diferentes. No todo se ejecutó dentro del 24–27; la fecha de la auditoría no es la fecha de generación. Los ejemplos siguientes son comparaciones históricas, no un ranking común.

| Artefacto / cohorte | Evidencia y límite |
|---|---|
| Qwen3.5 Base, evaluación interna | El registro señala siete casos favorables a TALON y `p11` favorable a TALM en una matriz con 18 prompts adjudicables, muchos empates y censura. El resultado por envolvente es post hoc; no valida un router. |
| Phi‑4, 30 prompts | La adjudicación histórica reporta 14/12/4 frente a la envolvente Min‑P. Los cuatro casos externos importan; el presupuesto corto limita la lectura de terminación. No se mezcla con Qwen. |
| Qwen3‑VL reparado | 20/20 empates en CFL menos envolvente externa reportados: jurisdicción de no discriminación, no mejora escondida. |
| `CFLDR_PLUS` v0.4 | Registro de 240 generaciones. La auditoría reporta que inline apenas aportó beneficio neto y que hubo desajuste de snapshot preroute/inline. Guardar el resultado adverso; no atribuir toda diferencia al operador. |
| CFL_dr/RDS v1.4.1, locked20 | Registro de 60/60 baseline por modo de router por penalización de protocolo no visto y coste. El control aleatorio sí activaba ramas. Es fallo/nulidad de la decisión en ese soporte, no refutación de TALM/TALON. |
| RDS v3.3 QAS | Registro de 180 generaciones y prior que concentró las rutas en un Right High conductualmente nulo. Contraejemplo de prior dominando evidencia, no etiqueta para cualquier Bayes. |
| Gemma 4 E4B CFLDecoder v2.2 `p01–p10` | Se recuperaron 270/270 filas `ok`: diez prompts, nueve métodos, semillas 11/22/33. CSV y JSONL coinciden con hashes del manifiesto y claves únicas. El manifiesto fecha el comienzo el **16 de junio**. No identifica por sí solo la ejecución de seis semillas citada el 25–26. `p11–p20`: se localizaron parciales de al menos 100/270; no se suman ni se declara cierre. |
| Z_xpl de ese Gemma | 270 filas válidas, 210 pareadas no baseline, cartografía declaradamente post hoc. Incluye TFS como candidato comparador; no tiene tabla válida de márgenes contra decoders estándar en ese artefacto. No es el Z actuador. |
| RDS v3.5 FINAL252 | Runtime heurístico ejecutado, separado del Bayes jerárquico. Auditoría maestra: 96/96 textos iguales full–QAS con máscara media de 207,88/248.320 (0,0837%) y aproximadamente 8,4% de sobrecoste en esa versión. Fidelidad, no aceleración ni utilidad semántica; no extrapolar a una línea CPU distinta. |

**Fuentes de identificación:** `DEFINITIVE_CAMPAIGN_REGISTRY.csv` (36 registros; SHA‑256 `ec38d66f487440e39972776b0cac878da36668f8f9a443d18951211f4993e93e`), `DEFINITIVE_CLAIM_LEDGER.csv` (12; `8e4341d6faa1925d64a336c6b7f183aceed803dd36b496d4644c46f87e30e7bf`), checkpoint Gemma E4B `0270_final_or_pause_cell09` (`adf5608e754b5987bb0058cf739db8ecd35fabc4e243ab62ea0fb38fa728ee54`) y Z_xpl Gemma (`63de34f2636da7e0b578010b63560e866c50ead3a87a1a8d7fde66f48d401abf`). Los resúmenes históricos no son re-adjudicación ciega propia. Se publica la descripción y la huella, no los textos crudos o los archivos privados.

**Siguiente contraste, aún no lanzado.** Primero enlazar código/contrato/resultados de la campaña prioritaria y separar la versión recuperada de cualquier implementación incompatible. Después congelar una matriz ajena a la selección histórica: vía ordinaria, brazo fijo Mass Right, ramas históricas elegibles, rival externo y política heurística/bayesiana con y sin sondas. Para Z/K/warper usar ablación factorial: cada pieza sola, combinación, orden y control de presupuesto. Adjudicar rescates, pérdidas, soporte, abstención y coste por prompt × semilla; exigir independencia temporal para promover/reingresar desde shadow. Una ganancia post hoc no autoriza un agente ex ante. GSM8K en curso se conserva como contraste de brazos, no se vuelve un ensayo de router.

## English

**Recovery anchor.** The June 26 campaign register and claim ledger preserve distinct Qwen3.5 Base, Phi‑4, Qwen3‑VL and Gemma jurisdictions. Not every run occurred during June 24–27: audit date is not run date. These are separate historical comparisons, not a common ranking.

| Artifact / cohort | Evidence and boundary |
|---|---|
| Qwen3.5 Base internal evaluation | The register records seven TALON-favorable cases and TALM-favorable `p11` among 18 adjudicable prompts, with ties and censoring. Envelope evidence is post hoc, not router validation. |
| Phi‑4, 30 prompts | Historical adjudication reports 14/12/4 versus the Min‑P envelope. Keep the four external wins; short budgets constrain termination interpretations. Do not pool with Qwen. |
| Repaired Qwen3‑VL | Reported 20/20 ties for CFL versus the external envelope: a non-discriminating regime, not hidden utility. |
| `CFLDR_PLUS` v0.4 | 240 recorded generations. The audit reports essentially no net inline gain and initial-snapshot mismatch in some preroute/inline contrasts. Retain the adverse result without attributing all differences to the operator. |
| CFL_dr/RDS v1.4.1 locked20 | Register reports baseline 60/60 per router mode under unseen-protocol and cost penalties. Random control did activate branches. This concerns decision failure or nullity in that support, not operator invalidation. |
| RDS v3.3 QAS | Register reports 180 generations and prior-driven concentration on behaviorally null Right High. Counterexample to prior dominance, not a verdict on all Bayesian approaches. |
| Gemma 4 E4B CFLDecoder v2.2 `p01–p10` | Recovered 270/270 `ok` rows: ten prompts, nine methods, seeds 11/22/33. CSV and JSONL match manifest hashes and unique keys. The manifest dates the start to **June 16**. It does not identify the six-seed run mentioned June 25–26. At least a 100/270 `p11–p20` partial was found; do not add snapshots or call it terminal. |
| Gemma Z_xpl | 270 valid rows, 210 paired non-baseline rows; explicitly post-hoc mapping. TFS appears as a comparison candidate, but the artifact does not provide a valid standard-decoder margin table. Not the Z actuator. |
| RDS v3.5 FINAL252 | Executed heuristic runtime, distinct from hierarchical Bayes. Master audit: 96/96 full–QAS exact texts with mean intervention mask 207.88/248,320 (0.0837%) and roughly 8.4% overhead for this version. Fidelity, not speedup or semantic value; do not extrapolate to a separate CPU lineage. |

**Sources:** the campaign/claim ledgers and Gemma artifacts are identified by the hashes above. The historical summaries are not a new blinded re-adjudication. Raw text and private artifacts are not published here.

**Next contrast, not launched.** First bind code, contract and results for the priority run; keep incompatible implementations distinct. Then freeze a fresh matrix covering the ordinary path, fixed Mass Right, eligible historical arms, external rival and heuristic/Bayesian policies with and without probes. Use factorial Z/K/warper ablations with single components, combination, order and budget control. Adjudicate rescue, loss, support, abstention and cost by prompt × seed; require temporal independence for promotion/reactivation from shadow. A post-hoc gain cannot authorize an ex-ante agent. Keep the ongoing GSM8K arm contrast unchanged; it is not a router trial.
