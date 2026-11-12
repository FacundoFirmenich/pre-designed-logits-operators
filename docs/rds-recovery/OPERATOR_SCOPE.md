# TALM / TALON — Contrato de intervención / Intervention contract

## Castellano

**TALM y TALON son operadores prediseñados, completamente training-free, de inferencia sobre los logits de salida, antes del softmax.** Reciben el vector final de logits que el modelo ya produjo y devuelven un vector transformado para la decodificación. No entrenan ni afinan el modelo, no cambian sus pesos, no intervienen capas o activaciones internas y no necesitan leer logits de capas intermedias. Aquí *white-box* significa acceso explícito al vector final de logits; no intervención interna.

Su operación propia es **redistribuir masa de probabilidad mediante la transformación de logits**, no truncar el soporte. TALON preserva el top‑1 en el punto de su contrato; TALM es casi preservador, pero permite cruces deliberadamente. Preservar el top‑1 no equivale a preservar toda la distribución ni el texto muestreado. El prediseño no es calibración retrospectiva sobre los resultados.

**Alcance vigente: operadores.** El enrutador es un componente independiente y tiene antecedentes propios. Los documentos de recuperación que lo describen se conservan como registro, no como plan activo, requisito de Paper 01 ni autorización para plantear horizontes del router. Esos horizontes requieren autorización expresa del autor.

## English

**TALM and TALON are predesigned, completely training-free inference-time operators on the final output logits, before softmax.** They take the final logit vector already produced by the model and return a transformed vector for decoding. They do not train or fine-tune the model, change its weights, intervene on internal layers or activations, or require reading intermediate-layer logits. Here, *white-box* means explicit access to the final logits, not an intervention inside the model.

Their defining operation is **redistribution of probability mass through a logit transformation**, not truncation of support. TALON preserves top‑1 at its contract point; TALM is near-preserving but deliberately permits crossings. Preserving top‑1 does not imply preserving the full distribution or sampled text. Predesign is not retrospective tuning on outcomes.

**Current scope: operators.** The router is a separate component with its own prior results. Recovery documents describing it are retained as a record, not as an active plan, a Paper 01 prerequisite, or permission to propose future router work. Such proposals require express authorization from the author.
