# Paper 01 · Canon de arquitectura / Architecture canon

**Registro:** P01-ARCH-001 · v1.0 · 2026-11-12 (Europe/Madrid)  
**Autoridad / Authority:** decisiones explícitas del autor registradas en la conversación del proyecto / explicit author decisions recorded in the project conversation.  
**Alcance / Scope:** canon documental; no modifica código, freeze, parámetros ni ejecuciones / documentation canon; does not change code, freezes, parameters or executions.

## Castellano

### Decisión del autor

**TALON Mass Right + QAS + Z‑Explorer.** El enrutador no forma parte de Paper 01. La investigación histórica se usa para entender implementaciones, no como evidencia del paper. TALM conserva su identidad y su linaje; no es coprotagonista ni requisito de la arquitectura. No se importa el plan editorial del marco de julio ni se adopta una agenda de RDSS por defecto.

### Narrativa integradora

Una intervención puede conservar el token de mayor rango y, aun así, cambiar el abanico de continuaciones disponibles bajo muestreo. La pregunta científica es **qué transformación introduce TALON, cuánto de ella conserva una intervención localizada y qué efectos locales quedan invisibles si sólo se mira el máximo o una distancia global**. Son tres preguntas sobre el mismo objeto —la respuesta de una distribución final a una intervención— y no tres intentos de ganar el mismo ranking.

| Pieza | Entrada → salida | Responsabilidad | No es |
|---|---|---|---|
| **TALON Mass Right** | Logits finales del modelo → logits modulados | Intervención prediseñada, completamente training-free, pre-softmax, sin modificar pesos, capas ni activaciones internas. Preserva top‑1 en el punto declarado del contrato; redistribuye masa al normalizar. | Truncador de soporte, entrenamiento, contraste multicapa o garantía de utilidad. |
| **QAS** | Logits de referencia y cambio candidato → soporte de intervención y logits localizados | Instancia particular de **CAS**. Cualifica dónde aplicar el cambio y permite contrastar fidelidad y coste frente a la intervención full. | Warper, límite del vocabulario de salida, garantía de equivalencia o de velocidad. |
| **Z‑Explorer** | Salidas y controles comparables → cartografía, aristas y casos extremos | Diagnóstico con capacidad de descubrimiento: señala regiones de transformación no necesariamente priorizadas por otros diagnósticos. | Sampler, router, actuación automática o métrica de corrección. |

La intervención y la localización forman el contraste generativo; la cartografía lee sus efectos y los de sus controles. **Z no devuelve autoridad al selector ni cambia una decisión de la misma corrida.** El corpus histórico no demuestra que las tres piezas ya hayan sido ejecutadas y validadas como conjunto.

### Invariantes y criterio de lectura

- **El objetivo es complementariedad local.** Unidad mínima de lectura: modelo/revisión × caso × semilla × brazo × presupuesto × precisión × protocolo. Un rescate frente a baseline exige fallo de baseline y acierto del brazo en la celda comparable. Un rescate exclusivo exige que fallen todos los rivales especificados y observados; una exclusiva aislada no establece una jurisdicción estable. Conservar pérdidas, empates, faltantes y casos no estimables. Un agregado puede contextualizar, no reemplazar la adjudicación local.
- **Preservar el máximo no preserva la distribución.** Si el selector es codicioso y el máximo se conserva hasta él en todos los prefijos correspondientes, la intervención no cambia la elección. Bajo muestreo, sí puede cambiar el recorrido. Distinguir argmax del operador, precisión de retorno, efecto de warpers y elección efectiva.
- **Identificar mecanismo antes de atribuir resultado.** Comparar modulación con un control de temperatura efectiva y con un control que preserve top‑1; documentar el orden de procesadores y warpers. Comparar QAS y full para el mismo brazo; medir fidelidad y coste por separado. Para Z, usar las mismas salidas nuevas y distinguir la señal compuesta de distancia, entropía y corrección.
- **Sólo evidencia nueva en el paper.** Artefactos y cifras viejos son antecedentes técnicos excluidos de tablas, figuras, resultados y afirmaciones empíricas del manuscrito. Los casos históricos sirven para definir preguntas, no para elegir retroactivamente qué resultados cuentan. No se incorpora una definición de parámetros actuales a partir de un cuaderno de otra campaña.
- **Custodia y búsqueda.** Drive, Descargas y Objetos 3D en C:/D:, biblioteca de ChatGPT y GitHub; lectura de lo ya presente en disco, sin nuevas descargas ni extracción local. Comprimidos primero para ubicar una ejecución; cuaderno homónimo sólo si una cuestión de implementación lo exige. No declarar revisada una superficie inaccesible.

**Documentos vinculados:** [contratos y contrastes](CONTRASTS.md) · [referencias de implementación y scoring](LINEAGE.md) · [Sistema de Posicionamiento Posibilístico](SISTEMA_POSICIONAMIENTO_POSIBILISTICO_ES_EN.md).

## English

### Author decision

**TALON Mass Right + QAS + Z‑Explorer.** Routing is outside Paper 01. Historical work informs implementation only and is excluded as paper evidence. TALM retains a distinct lineage and is neither a co-lead nor a dependency. The July editorial plan and any RDSS agenda are not adopted here.

### Integrating narrative

An intervention can preserve the highest-ranked token while changing the range of likely sampled continuations. The scientific questions are **what TALON changes, how much a localized intervention retains, and which local effects are missed by a maximum or an overall distance**. These are three views of the same distributional intervention, not three methods competing on the same scoreboard.

| Component | Input → output | Responsibility | Not |
|---|---|---|---|
| **TALON Mass Right** | Final model logits → modulated logits | Predesigned, completely training-free pre-softmax intervention, without changes to weights, layers, or internal activations. Preserves top‑1 at the declared contract point and redistributes mass upon normalization. | Support truncation, training, cross-layer contrast, or guaranteed utility. |
| **QAS** | Reference logits and candidate change → intervention support and localized logits | A particular instance of **CAS**. Qualifies where to apply the change and enables fidelity and cost comparisons with full intervention. | A warper, an output-vocabulary limit, or guaranteed equivalence or speedup. |
| **Z‑Explorer** | Comparable outputs and controls → maps, edges, and tail cases | Discovery-capable diagnostic that flags regions of transformation not necessarily prioritized by other diagnostics. | Sampler, router, automatic actuator, or correctness score. |

Intervention and localization define the generative comparison; mapping reads their effects and those of their controls. **Z does not confer selection authority or revise decisions from the same run.** Historical artifacts do not establish joint validation of the three components.

### Invariants and interpretation

- **Local complementarity is the objective.** Retain model/revision × case × seed × arm × budget × precision × protocol. A rescue means baseline fails while the arm succeeds in a comparable cell. An exclusive rescue requires failure of every named, observed comparator; a single exclusive rescue does not establish a stable jurisdiction. Preserve losses, ties, missingness, and non-estimable cases. Aggregates contextualize; they do not replace local adjudication.
- **Preserving the maximum does not preserve the distribution.** Greedy selection is unchanged only when the maximum is preserved through the selector at all corresponding prefixes. Sampled trajectories may still change. Distinguish operator argmax, returned precision, post-warper state, and actual selection.
- **Identify mechanism before attributing outcomes.** Contrast modulation with matched effective temperature and a top‑1-preserving control; record processor and warper order. Compare QAS with full for the same arm and separate fidelity from cost. Apply Z to the same new outputs and separate its composite signal from distance, entropy, and correctness.
- **New evidence only.** Historical artifacts and numbers are technical background, excluded from manuscript tables, figures, results, and empirical claims. They inform questions, not retrospective selection of outcomes or unannounced import of current parameters from older notebooks.
- **Custody and discovery.** Search Drive, Downloads and 3D Objects on C:/D:, ChatGPT Library, and GitHub. Read existing local files without new downloads or extraction. Locate runs through archives; inspect a same-name notebook only when an implementation question requires it. Do not claim coverage of an inaccessible surface.

**Companion documents:** [contracts and contrasts](CONTRASTS.md) · [implementation references and scoring](LINEAGE.md) · [Possibilistic Positioning System](SISTEMA_POSICIONAMIENTO_POSIBILISTICO_ES_EN.md).
