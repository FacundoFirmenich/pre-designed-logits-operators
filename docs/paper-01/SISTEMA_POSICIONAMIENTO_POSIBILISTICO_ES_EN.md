# Sistema de Posicionamiento Posibilístico / Possibilistic Positioning System

**ID:** P01-METHOD-SPP-001 · v1.0 · 2026-11-16  
**Autoridad / Authority:** formulación y mandato metodológico explícitos del autor / explicit author formulation and methodological instruction.  
**Alcance / Scope:** canon metodológico; no cambia operadores, parámetros, código, resultados ni el alcance editorial de Paper 01 / methodology canon; no change to operators, parameters, code, results or Paper 01 scope.

## Castellano

### Formulación de autor

> «Un sistema de posicionamiento posibilístico que no probabilístico.»  
> «Somos el azote de los promedios, las gaussianidades y la ingobernabilidad estocástica.»  
> «Pero no nos gobierna lo estocástico.»

El autor describe así el papel de lo aleatorio: «lo aleatorio implica por definición parametrizar y interiorizar en el modelo paquetizaciones de causalidad compleja no estructurable». Se adopta como término de trabajo del proyecto, no como definición matemática universal ni como prueba de una ontología determinista. «si no hay nada mejor, pues no hay nada mejor» fija la excepción epistemológica: utilizar el mejor dato disponible sin fingir que posee más resolución.

### Definición y glosario

| Término | Definición operativa |
|---|---|
| **Sistema de Posicionamiento Posibilístico (SPP)** | Cartografía que ubica acciones, rescates, fallos y fronteras en sus condiciones de validez. Conserva alternativas simultáneas, conflictos y falta de soporte. Responde «¿qué puede ocurrir o sostenerse aquí y con qué evidencia?», antes de preguntar «¿con qué frecuencia o bajo qué probabilidad?». |
| **Jurisdicción local** | Región declarada de aplicabilidad: modelo y revisión, caso o segmento, presupuesto —incluidos plazos cuando apliquen—, precisión y protocolo. Dentro de ella se conservan las filas por semilla y brazo; no se reemplaza el caso por el promedio del segmento. |
| **Arista / frontera** | Dos jurisdicciones conectadas por un contraste identificable. Una arista experimental registra qué factor cambia y cuáles se mantienen; si cambian varios sin un diseño que los separe, la arista es descriptiva y no identifica un mecanismo. |
| **Resolución nativa y trazabilidad** | Conservar la observación original, el modo de medirla y la cadena hasta el veredicto. Código inspeccionable e información empírica inspeccionable son propiedades distintas: ver una fórmula no permite recuperar lo que el promedio descartó. |
| **Paquetización de causalidad compleja** | Representación explícita de dependencias que no se han descompuesto al nivel disponible: qué se deja indeterminado, cómo se parametriza y a qué parte del modelo afecta. La aleatorización puede representar esa opacidad, pero no se presume que la identifique causalmente ni que toda fuente aleatoria sea de ese tipo. |
| **Estocasticidad confinada** | Muestreo, Monte Carlo u otro mecanismo aleatorio dentro de un módulo con alcance, entradas, salidas, presupuesto, procedimiento de aleatorización, diagnósticos y condiciones de fallo declarados. Sus salidas son insumos bajo una regla de admisión explícita; no cambian por sí solas la jurisdicción, el protocolo ni la autoridad. |
| **Agregado subsidiario** | Resumen diagnóstico cuando se dispone de observaciones finas; insumo degradado sólo cuando no hay dato más informativo y es indispensable operar. Declarar fuente, cobertura, denominador, supuestos y pérdida de resolución. No autoriza reconstruir celdas ni adjudicar rescates locales. La gaussianidad es una hipótesis local que requiere justificación, nunca un valor por defecto. |

### Formalización mínima

Sea $j=(m,r,i,b,q,p)$ la jurisdicción: modelo $m$, revisión $r$, caso $i$, presupuesto $b$, precisión $q$ y protocolo $p$. Para cada brazo $a$ y semilla $s$, sea $Y_{j,s,a}$ su adjudicación, con estados $\{1,0,\bot\}$: éxito, fallo observado según el evaluador y dato no adjudicable. Guardar por separado la salida, evaluación, latencia, motivo de ausencia y procedencia disponibles. Un timeout registrado puede ser fallo bajo un plazo predefinido; un registro perdido no lo es.

Con un conjunto **declarado** de comparadores $C_j$ no vacío, hay rescate exclusivo observado en la celda si $Y_{j,s,a}=1$ y $Y_{j,s,c}=0$ para todo $c\in C_j$, bajo el mismo protocolo de comparación. Si otro brazo tiene éxito, no hay exclusividad; si el brazo objetivo tiene éxito, no hay éxitos rivales observados y falta alguno, la exclusividad queda **no estimable**. El rescate frente a baseline se adjudica por separado; la reciprocidad exige conservar también los casos en los que rescatan los otros. «Nadie más» significa sólo «ningún comparador de ese conjunto, en esa celda observada». Una celda no demuestra estabilidad ni transporte.

Para posicionar una alternativa, fijar la proposición local $\phi_j(a)$, sus criterios y el alcance de la evidencia antes de adjudicar: **respaldada**, **refutada**, **abierta/no estimable** o **fuera de soporte**. El mapa devuelve cada alternativa con su estado y las filas que lo justifican; no normaliza, no fuerza un ganador ni convierte «aún no observado» en «imposible». No se hereda un estado al atravesar una frontera de modelo, cuantización, evaluador o presupuesto sin datos que avalen ese traslado.

**Distinción formal.** Una probabilidad es aditiva en eventos disjuntos. Si alguna aplicación exige grados numéricos de posibilidad, el puente opcional con la teoría clásica consiste en una escala justificada $\pi_j(a)\in[0,1]$, con $\max_a\pi_j(a)=1$ en un dominio finito no vacío y $\Pi_j(A)=\max_{a\in A}\pi_j(a)$, con $\Pi_j(\varnothing)=0$. Así $\Pi_j(A\cup B)=\max(\Pi_j(A),\Pi_j(B))$: dos alternativas mutuamente excluyentes pueden ser máximamente posibles, sin que tengan probabilidad uno. Si no hay evidencia para asignar grados, no se construye la escala. Esta extensión no es requisito del SPP ni una descripción del cómputo de TALON. Referencia del puente, no del diseño de autor: [Zadeh, informe original, UC Berkeley](https://www2.eecs.berkeley.edu/Pubs/TechRpts/1977/29351.html).

### Consecuencia científica y jurisdicciones

1. **TALON y Paper 01:** el operador interviene sobre logits y modifica la distribución de muestreo; el SPP gobierna cómo se leen y delimitan sus efectos. Ni un RMS global ni el saldo medio sustituyen las celdas de victoria, empate, derrota o rescate. El contraste central conserva los rescates en ambos sentidos frente al baseline y al comparador fuerte, y separa hallazgo retrospectivo de confirmación en casos nuevos. No se declara que rechazar el promedio *cause* un rescate: preserva la evidencia necesaria para detectarlo y preguntarse por el mecanismo.
2. **Retroalimentación virtuosa:** conservar los casos permite detectar una arista; la arista informa una hipótesis para una prueba siguiente; una prueba nueva puede confirmarla, acotarla o refutarla. Es un diseño para acumular conocimiento, no una demostración de atractor extraño, estabilidad ni transportabilidad. La hipótesis nueva nunca devuelve autoridad a la misma corrida ni reclasifica retroactivamente sus observaciones.
3. **RDSS y AADTCS:** el RDSS jerárquico bayesiano puede aportar inferencia condicionada y reinformar decisiones futuras sin convertir el posterior en un permiso automático. La posibilidad de recurrir a un promedio no lo vuelve decisor universal. AADTCS es una jurisdicción aparte: gobierno constitucional y decisional determinista a través de un modelo adversarial; no se incorpora al deep learning ni al Paper 01 por analogía. Una regla decisional determinista puede consumir evidencia de un proceso aleatorio sin que ambos niveles se confundan.

**Criterios de conformidad:** (i) un informe que sólo contiene medias no adjudica exclusividad; (ii) un rival faltante no cuenta como derrota; (iii) un caso exclusivo bien observado no se borra aunque el saldo agregado sea adverso; (iv) una prueba estocástica sin alcance y protocolo declarados no otorga autoridad; (v) cuando sólo se dispone de un agregado, el informe identifica expresamente qué no se puede concluir. Estos criterios son especificación documental; no certifican una implementación ni resultados nuevos.

## English

### Author's formulation

“A possibilistic positioning system, not a probabilistic one.” The author's stance is against using averages, Gaussian defaults, or stochastic processes as governing authorities. The project term *operational randomness* refers to making unresolved, complex causal structure explicit through bounded representations; it is not a universal definition of randomness or a proof of a deterministic ontology. If nothing more informative exists, use the best available input without pretending it has finer resolution.

### Definition and glossary

| Term | Operational meaning |
|---|---|
| **Possibilistic Positioning System (SPP)** | A map of where actions, rescues, failures and boundaries are supported. It preserves concurrent alternatives, conflict and lack of support. It asks what can occur or be supported here, and by what evidence, before asking how probable it is. |
| **Local jurisdiction** | A declared domain of applicability: model and revision, item or segment, budget (including deadlines when applicable), precision and protocol. Retain per-seed and per-arm records within it. |
| **Edge / boundary** | A link between jurisdictions defined by a contrast. An experimental edge identifies what changed and what was held fixed; inseparable changes yield a descriptive edge, not an identified mechanism. |
| **Native resolution and traceability** | Preserve the observation, how it was measured and how it led to adjudication. Code inspectability and evidence inspectability are different: reading a formula cannot recover information discarded by averaging. |
| **Packaging of complex causality** | An explicit representation of dependencies unresolved at the available resolution: what is left unknown, how it is parameterized and which module it affects. Randomization may represent the unresolved part; it does not, by itself, identify its causes. |
| **Confined stochasticity** | Sampling or another stochastic mechanism in a module with declared scope, inputs, outputs, budget, randomization procedure, diagnostics and failure criteria. Its results are inputs to an explicit admission rule and cannot confer authority or amend the protocol. |
| **Subsidiary aggregate** | A secondary diagnostic when fine-grained data exist; a degraded fallback only when nothing more informative is available and an input is indispensable. Record provenance, coverage, denominator, assumptions and lost resolution. No imputation of rescues from aggregates; Gaussianity needs local justification and is not a default. |

### Formal core

Let $j=(m,r,i,b,q,p)$ index model, revision, item, budget, precision and protocol, and let $Y_{j,s,a}\in\{1,0,\bot\}$ denote success, observed failure under the evaluator, or unadjudicable data for seed $s$ and arm $a$. Keep available output, evaluation, timing, missingness and provenance separately. A recorded timeout can count as failure under a declared deadline; a lost record cannot.

For a nonempty declared comparator set $C_j$, a cell is an observed exclusive rescue exactly when $Y_{j,s,a}=1$ and every $c\in C_j$ has $Y_{j,s,c}=0$ in the same comparison protocol. A successful rival rules out exclusivity; if the target succeeds, no rival is observed to succeed and any rival is missing, exclusivity is not estimable. Score rescue against baseline separately and preserve rescues by rival arms. “No one else” means “none of the named comparators in that observed cell”; it does not establish stability or transfer.

For each local proposition $\phi_j(a)$, predeclare the relevant criteria and evidence. Return the state — supported, refuted, open/not estimable, or out of support — along with the underlying evidence, without compulsory normalization or a forced winner. Crossing a model, quantization, evaluator or budget boundary does not transfer a finding without supporting data.

Probability is additive over disjoint events. An optional bridge to classical possibility theory, if justified grades are available on a nonempty finite domain, is a scale $\pi_j(a)\in[0,1]\text{ with }\max_a\pi_j(a)=1$ and $\Pi_j(A)=\max_{a\in A}\pi_j(a)$, $\Pi_j(\varnothing)=0$, and $\Pi_j(A\cup B)=\max(\Pi_j(A),\Pi_j(B))$. Distinct alternatives can both be maximally possible without either having probability one. No scale is assigned when evidence does not justify grades. This bridge is not a TALON implementation claim. See [Zadeh's original Berkeley report](https://www2.eecs.berkeley.edu/Pubs/TechRpts/1977/29351.html).

### Scientific and architectural consequences

TALON acts on logits and affects sampling probabilities; SPP governs how its effects are situated and read. Neither a pooled score nor a global RMS substitutes for paired wins, ties, losses and exclusive rescues in both directions. Retaining resolution can reveal a rescue; it does not cause one. Mapping an edge can inform a subsequent test but cannot modify the same run or retrospectively confer authority. This feedback design makes no strange-attractor or transport claim.

Hierarchical Bayesian RDSS can inform future decisions without turning a posterior into automatic permission. AADTCS remains a separate jurisdiction of deterministic constitutional and decision governance via an adversarial model; it is not imported into deep learning or Paper 01. A deterministic decision rule can accept evidence generated by a stochastic module without conflating the two levels.

**Conformance criteria:** aggregate-only data cannot adjudicate exclusivity; missing comparators are not counted as losses; a valid exclusive rescue survives an unfavorable aggregate; an undeclared stochastic module cannot confer authority; aggregate fallback must state what remains unidentified. This is a methodological specification, not validation of a software implementation or a new experimental result.
