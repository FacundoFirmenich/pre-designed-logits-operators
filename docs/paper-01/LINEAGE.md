# Paper 01 · Referencias de implementación / Implementation references

[Canon de arquitectura / Architecture canon](CANON.md)

**Clasificación / Classification:** contexto histórico, no evidencia de Paper 01 / historical implementation context, not Paper 01 evidence. No se publican outputs originales ni fuentes privadas / no raw outputs or private sources are included.

## Castellano

| Fuente recuperada | Hecho de implementación | Límite de atribución |
|---|---|---|
| DirectComp Qwen3.5‑4B ENNative V3, cuaderno homónimo; celdas 10 y 12 | Mass Right selecciona por masa descendente incluyendo el cruce del umbral 0,92; estandariza por mediana y MAD; aplica delta tanh con pesos asimétricos, intensidad 0,70 y reparación de top‑1 si hay cruce. Mass Left cambia orientación y pesos efectivos, no el umbral o intensidad de ese par. | Configuraciones históricas, no parámetros del brazo actual. La temperatura interna 0,8 y el warper 0,8 dan un escalado de base efectivo 0,64 en ese cuaderno; no confundirlo con el efecto del delta. El diagnóstico interno se calcula antes del cast de retorno; no basta como prueba post-warper. |
| TALM en el mismo DirectComp; registros Qwen 2B, Phi‑4 y Gemma | Selección por rango, masa o híbrido; modulación específica por lado. La familia admite cruces, pero los brazos TALM de aquel DirectComp activaban preserve_top1. El índice enlaza cuadernos Qwen 2B, Phi‑4 y Gemma por manifiesto. | Un vínculo por similitud nominal, como algunos de v0.6.4, no identifica el código que generó un ZIP. No extrapolar entre ramas, modelos ni suites nativas. |
| Runtime RDS v3.5, QAS | Combina masa/probabilidad de referencia, energía contrafactual y coordenadas protegidas; identidad de logits de referencia fuera de soporte. | Fidelidad conductual, preservación de distribución y coste son resultados separados. El antiguo FINAL252 no demuestra aceleración. La variante CPU aceleradora, CAS general y una eventual equivalencia full–QAS del Mass Right actual no quedan establecidas por este runtime. |
| Scripts Z_xpl recuperados de Qwen 2B/Gemma E2B | Score compuesto: suma de componentes estandarizados de diversidad, entropía y reducción de repetición; término de distancia estandarizada de peso 0,25 y penalización 0,50 por exceso de distancia sobre el control. | La escala depende de la referencia. Los CSV DirectComp Qwen EN/ZH y Phi‑4 contienen mapas y casos extremos; no certifican que todos usen exactamente ese script. No fusionar por nombre ZPH, BZ, ZH o la segunda variante no resuelta de Z‑Explorer. |
| DirectComp «960», Gemma E4B v2.2, Phi‑4 Min‑p y RDSS/Kaggle | DirectComp inspeccionado tiene 480 filas previstas y 420 filas cartográficas pareadas, no 960 ejecuciones; Gemma E4B v2.2 conserva extremos sin tabla de márgenes; Z_xplr del 30 de junio es un control Phi‑4 Min‑p sin TALON; RDSS candidato es una corrida distinta, no el cartógrafo. | No sumar checkpoints, réplicas, observaciones ni suites. Los bundle final y claim con igual cantidad de filas no son automáticamente intercambiables. Los rótulos de corrida completa y la identificación de un operador no prueban utilidad semántica. |

**Scoring documental, no de calidad.** F: 0 no identificado, 1 rol documentado, 2 contrato parcial, 3 código/configuración de una versión inspeccionados. C: 0 no adjudicable, 1 descriptivo, 2 control o pares con atribución parcial, 3 diferencia aislada. Sin suma ni orden global. Estos scores describen el material de referencia, no son resultados del paper.

| Objeto | F | C | Base |
|---|---:|---:|---|
| Mass Right vs. Mass Left, DirectComp ENNative V3 | 3 | 2 | Configuración separable; no se readjudica el outcome. |
| Mass Right vs. temperatura efectiva | 3 | 2 | Control identificado; no todos los contrastes históricos están aislados. |
| TALM vs. TALON, DirectComp V3 | 3 | 1 | Selección, deltas, temperatura y preservación varían por brazo. |
| QAS v3.5 vs. full | 3 | 2 | Código y pares históricos; sin extrapolación a la versión actual. |
| CAS general | 1 | 0 | QAS es instancia particular; no se recuperó la especificación de toda la familia. |
| Z_xpl compuesto | 3 | 2 | Fórmula inspeccionada y tablas históricas; no prueba exclusividad universal. |
| Phi‑4 Min‑p del 30 de junio | 2 | 0 para TALON | Control sin candidato TALON ni margen candidato–rival. |

**Cobertura.** Los notebooks consultados estaban en Descargas y Objetos 3D. Drive conserva el marco maestro de julio, el registro multilingüe y los informes de Z; D: conserva paquetes y una réplica parcial de biblioteca. El árbol consultado de GitHub tenía documentación y prerregistros, no los cuadernos homónimos. La biblioteca nativa no se pudo verificar; no se sustituye por la réplica. Las fuentes históricas se conservan sin conferirles autoridad para Paper 01.

## English

| Recovered source | Implementation finding | Attribution boundary |
|---|---|---|
| DirectComp Qwen3.5‑4B ENNative V3 matching notebook, cells 10 and 12 | Mass Right selects by descending cumulative mass including the threshold crossing at 0.92; uses median/MAD standardization, a weighted asymmetric tanh delta, strength 0.70, and top‑1 repair on a crossing. Mass Left changes orientation and effective weights, not that pair's intensity or threshold. | Historical settings, not the current arm's settings. Internal 0.8 and warper 0.8 yield an effective base scale of 0.64 in this notebook; separate that from the delta. Internal telemetry precedes the return cast and does not establish post-warper preservation. |
| TALM in that DirectComp; Qwen 2B, Phi‑4, and Gemma records | Rank, mass, or hybrid selection and side-specific modulation. The family permits crossings, but those DirectComp TALM arms enabled preserve_top1. The index links Qwen 2B, Phi‑4, and Gemma notebooks via manifests. | Filename similarity, including some v0.6.4 matches, does not identify the code behind an output ZIP. Do not extrapolate across arms, models or native suites. |
| RDS v3.5 QAS runtime | Combines reference probability/mass, counterfactual energy, and protected coordinates; reference logits remain unchanged outside intervention support. | Behavioral fidelity, distributional preservation, and cost are separate. Old FINAL252 does not demonstrate acceleration. The faster CPU variant, general CAS specification, and fidelity for the current Mass Right remain unestablished by this runtime. |
| Qwen 2B/Gemma E2B Z_xpl scripts | Sum of standardized diversity, entropy, and repetition-reduction edges, plus standardized distance weighted by 0.25 and a 0.50 penalty for excess distance relative to control. | Scale depends on the reference. DirectComp EN/ZH Qwen and Phi‑4 tables contain maps and tail cases; this does not establish identical script lineage. Do not merge ZPH, BZ, ZH, or the unresolved second Z‑Explorer variant by name. |
| DirectComp “960,” Gemma E4B v2.2, Phi‑4 Min‑p, and RDSS/Kaggle | The inspected DirectComp has 480 planned results and 420 paired cartography rows, not 960 executions. Gemma E4B v2.2 retains extremes without a margin table. June 30 Z_xplr is a Phi‑4 Min‑p control without TALON. Candidate-only RDSS is a separate run, not the mapper. | Do not add checkpoints, replicas, observations, or suites. Final and claim bundles with equal row counts are not necessarily interchangeable. A completed run or identifiable operator does not establish semantic utility. |

**Documentary scoring, not quality.** F: 0 unidentified, 1 documented role, 2 partial contract, 3 code/configuration inspected for one version. C: 0 not adjudicable, 1 descriptive, 2 control or matched rows with partial attribution, 3 isolated difference. No aggregate or global ranking; these scores characterize background material, not paper results.

| Object | F | C | Basis |
|---|---:|---:|---|
| Mass Right vs. Mass Left, DirectComp ENNative V3 | 3 | 2 | Separable settings; outcomes not re-adjudicated. |
| Mass Right vs. matched effective temperature | 3 | 2 | Identified control; historical contrasts are not all isolated. |
| TALM vs. TALON, DirectComp V3 | 3 | 1 | Selection, deltas, temperature, and preservation vary by arm. |
| QAS v3.5 vs. full | 3 | 2 | Historical code and matched rows; no extrapolation to current version. |
| General CAS | 1 | 0 | QAS is a particular instance; full family specification not recovered. |
| Composite Z_xpl | 3 | 2 | Formula and historical tables; no universal exclusivity claim. |
| June 30 Phi‑4 Min‑p | 2 | 0 for TALON | Control without a TALON candidate or candidate–rival margin. |

**Coverage.** Notebooks were located in Downloads and 3D Objects. Drive holds the July framework, multilingual registry, and Z reports; D: holds packages and a partial Library replica. The inspected GitHub trees held documentation and preregistrations rather than matching notebooks. Native Library access remained unverified. Preserve the history without conferring Paper 01 evidentiary authority.
