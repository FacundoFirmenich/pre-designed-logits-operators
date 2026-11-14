# Paper 01 — Actualización experimental / Experimental update

## Expansión y alcance editorial / Expansion and editorial scope

Kaggle aceptó Gemma 4 E4B-it y Granite 4.0 H Micro, ambas v1, con estado inicial `QUEUED`. Son 300 celdas previstas por configuración; conservan los cinco casos, cuatro semillas, cinco métodos, tres condiciones QAS y el diagnóstico ZX. Phi y Qwen: 600/600 celdas verificadas. Gemma E2B, Granite Micro sin H, Falcon Mamba, Ministral y Liquid: preparados, sin enviar en este corte. / Kaggle accepted Gemma 4 E4B-it and Granite 4.0 H Micro v1; both were initially queued. Phi and Qwen remain verified at 600/600; the remaining five notebooks were prepared but not submitted at this checkpoint.

Paper 01 evalúa un subconjunto del repertorio y reporta aportes por jurisdicción; un total de reemplazo indiscriminado es un control secundario, no el criterio que define autoridad. En la Discusión se propone situar estos resultados dentro del **enrutador bayesiano jerárquico, dinámico y reinformador**, con desarrollo experimental previo. Una onda fija puede actuar como generadora, como sonda contrafactual en sombra o en ambos papeles, según la jurisdicción; Top-H es un comparador externo y un candidato de doble uso. La cobertura exclusiva observada no prueba que el router sepa elegir ex ante ni mide el valor informativo de la sonda. / Paper 01 evaluates a subset of the portfolio and prioritizes jurisdiction-level contributions. The broader research program concerns a **hierarchical, dynamic Bayesian router with feedback**: a fixed intervention can generate, serve as a shadow counterfactual probe, or do both in different jurisdictions. Observed portfolio coverage does not validate ex-ante routing or the value of the probe.

## Cierre Phi y Qwen / Phi and Qwen closeout

600/600 generaciones verificadas en dos configuraciones NF4 del mismo panel diagnóstico GSM8K: cinco problemas ya vistos, cuatro semillas y 15 brazos por modelo; no son 600 problemas independientes. Phi-4-mini usa su chat instruct nativo; Qwen3.5-4B tiene el modo explícito de razonamiento desactivado. Se mantuvo el recíproco a 1 nat; véase el [sello SHA-256](NR_TALON_FREEZE_SHA256_ES_EN.md), que consolida recibos previos al envío y no se retrofecha.

| Modelo / Model | QAS | Marcador estricto / Strict marker | Numérico flexible / Flexible numeric |
|---|---|---|---|
| Phi | No / Off | 12/14/14/11/18 | 17/17/17/16/20 |
| Phi | Referencia / Exact v2 | 12/14/14/11/17 | 17/17/17/16/20 |
| Qwen | No / Off | 13/14/15/15/15 | 13/14/15/15/15 |
| Qwen | Referencia / Exact v2 | 13/14/15/15/14 | 13/14/15/15/14 |

Orden / Order: baseline / Mass Right / inversión simple (odds reversal) / recíproco / Top‑H. Cada valor es sobre 20. Las dos variantes de QAS coinciden token a token en los 100 pares por modelo; ZX registró 45 prefijos válidos por modelo, no 45 resultados generativos.

- **Phi, 1265/66:** el recíproco es el único de cinco que acierta con marcador estricto, en los tres modos QAS, incluso a 6 s. Con evaluación flexible no es exclusivo. Frente a inversión simple, el saldo estricto por semilla es 1 rescate y 4 pérdidas; en 1242 la inversión gana dos semillas. Top-H lidera ambos totales en Phi.
- **Qwen:** recíproco e inversión coinciden en los 20 veredictos finales en cada modo QAS. En 430 sin QAS ambos marcan 2/4 frente a 0/4 de Top-H; en 85, Top-H 4/4 frente a 2/4 de ambos. Empatar a 15/20 sin QAS no significa resolver los mismos problemas.

**English.** The reciprocal and simple reversal are not behaviorally equivalent across models: Phi yields a strict-marker rescue unique to the reciprocal, not a flexible-numeric exclusive. The reverse control wins more often on this Phi panel. Qwen reproduces the identical final verdicts of the two variants and shows opposing local edges versus Top-H. Treat this as a diagnostic of local complementarity, not prevalence on new prompts or cost savings. The seven other configurations are frozen, not yet reported as run. ARC‑AGI‑2 remains paused.

**Segundo despacho / Second dispatch.** Qwen v1 también fue aceptado y se observó en ejecución. Los dos modelos suman 600 generaciones previstas, no verificadas aún; los siete restantes estaban preparados pero no enviados. / Qwen v1 was accepted and observed running, for 600 planned cells across the two models; seven further configurations were prepared, not submitted.

**Primer despacho / First dispatch.** Kaggle aceptó Phi v1 y se observó en ejecución: 300 generaciones previstas, sin evidencia terminal aún; las otras ocho configuraciones estaban preparadas pero no enviadas en este corte. / Phi v1 was accepted and observed running; 300 planned generations are not results. The other eight configurations were prepared but not submitted at this checkpoint.

Continúa el canon del commit `6c13da3069dba4d6fb8bb9d0ecac5d3c90e41a95`. La variante recíproca se incorpora como experimento independiente; no modifica el operador Mass Right congelado. / Continues the previous canon. The reciprocal variant is experimental and does not modify frozen Mass Right.

| Frente / Workstream | Evidencia / Evidence |
|---|---|
| Qwen holdout | 576 respuestas; al final, baseline/TALON/Top-H: 142/153/148 numérico y 131/146/147 estricto. Cortes descriptivos: 6/8/11/14 s y final. |
| Phi prospectivo | 1.200/1.200 respuestas. TALON vs baseline: 13/10/7 por problema en estricto y 6/22/2 en numérico; vs Top-H, 12/6/12 y 5/19/6. |
| QAS GPU Exact v2 | 600/600 respuestas; 150/150 pares idénticos en tokens frente al QAS de referencia. Mejora del componente, no aceleración demostrada de la generación completa. |
| ZX | Cartografía de colas sobre prefijos compartidos (208 registros válidos y 2 fuera de trayectoria en el contraste GPU v2), separada del replay histórico y del muestreo. |
| Gemma y transporte / Transfer | Se conservan resultados adversos y diferencias por arquitectura. No se adjudica el mecanismo softcap a partir de un mero estado terminal. |
| NR-TALON piloto | Qwen3.5-4B NF4, 2×T4; 80/80. Baseline/Mass Right/inversión simple/recíproco: 13/14/15/15 finales. El recíproco ganó dos y perdió uno frente a Mass Right por semilla; coincidió con la inversión simple en los 20 veredictos finales. Hubo un caso con ventaja de entrega a 11 s. |
| Expansión / Expansion | Nueve configuraciones, cinco problemas compartidos, cuatro semillas, cinco métodos (baseline, Mass Right, inversión simple, recíproco y Top-H) × tres variantes de cualificación (sin QAS, QAS de referencia y Exact v2). 2.700 generaciones previstas; no son resultados. ZX diagnostica y no genera. |

**English.** Final numeric and strict extraction outcomes remain separate. The Qwen reciprocal pilot was diagnostic on five previously observed prompts, not a replication or a cost claim. Across nine model configurations the new factorial tests local rescues and losses, qualified inference and transport. ARC‑AGI‑2 is paused during this block; HumanEval+ remains subsequent. The evidence boundary and historical adverse results are retained.
