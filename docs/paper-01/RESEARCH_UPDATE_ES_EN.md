# Paper 01 — Actualización experimental / Experimental update

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
