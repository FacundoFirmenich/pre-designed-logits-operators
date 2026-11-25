# Canon V3: recetas de autores y receta efectiva / Author recipes and effective recipe

**ID:** `TALON_AUTHOR_RECIPES_CANON_V3_20261125` · **Fecha / Date:** 2026-11-25 · **Versión / Version:** 3.0.0

## Castellano: qué queda fijado

La regla no es adaptar los rivales a TALON: es usar su receta autoral documentada y conservar la nuestra sin recalibración. Esta ficha corrige la atribución de Min-K, incorpora η-sampling y Mirostat con fuentes originales y congela los valores para campañas futuras. No altera los resultados ni los cuadernos anteriores. Es un canon de recetas, no una afirmación de que todos los backends estén ya validados.

**Corrección concreta:** τ3/T1 para Min-K está prescrito por el README oficial. No es una receta inventada aquí. El constructorτ2 y la CLI sin argumentos T4 son otros niveles de defaults; se documentan, pero no desplazan al comando de reproducción explícito.

**TALON no cambia:** rama `talon_mass_right`, T externa0,85, fuerza0,7, masa0,92, mediana/MAD, tanh, pesos izquierdo0,65/derecho1,2, protección externa. Sin Top-K/Top-P externos (K0/P1), sin QAS añadido. Baseline único T1. Semillas64,12,24,48,96. El JSON compañero contiene todos los campos internos, incluida la diferencia entre preserve_top1 internoFalse y guardia externaTrue.

**Qué significa convencional:** receta concreta publicada por sus autores, con función, variante, orden y fuente fijados. Si hay varios protocolos autorales se identifica el elegido; no se inventa un default universal ni se elige según nuestro resultado. Una adaptación estructural a otro vocabulario se declara, no se camufla como ejecución original del paper.

## Tabla operativa bilingüe / Bilingual operational table

| Perfil / Profile | Receta del autor / Author recipe | Receta en esta comparación / Effective comparison recipe | Estado / Status |
|---|---|---|---|
| talon_mass_right | T0,85; núcleo sellado / sealed core | Igual; K0/P1 / same, K0/P1 | UNCHANGED_SEALED_OPERATOR_PER_BACKEND_ADMISSION_STILL_REQUIRED |
| baseline_t100 | Identidad térmica / thermal identity | T1; único / only baseline | SINGLE_BASELINE_NO_T085_DUPLICATE |
| min_k | README: τ3; T1 | τ3; T1; autoral / author-prescribed | AUTHOR_RECIPE_CONFIRMED_NO_NUMERIC_CHANGE |
| top_h | Constructor: α0,4; top_n100; T1 | Mismos valores; HF histórico explícito / same values; historical HF identified | PARAMETERS_CONFIRMED_IMPLEMENTATION_EQUIVALENCE_REQUIRED_BEFORE_NEW_FREEZE |
| min_p | Rango0,05–0,10; T variable / varying T | p0,10; T1; standalone | AUTHOR_RECOMMENDED_VALUE_AND_ORDER_CONFIRMED_IMPLEMENTATION_PIN_REQUIRED |
| p_less | p_less_decode; sum(p²) | Original; T1; no norm | AUTHOR_FUNCTION_CONFIRMED_NO_VARIANT_SUBSTITUTION |
| top_nsigma | Default n1; torch.std | n1; corrección1; T1 / correction1 | PAPER_DEFAULT_CONFIRMED |
| eta_sampling | Evaluación humana: ε0,0006; T1; K0/P1 | Misma receta transportada / same transported recipe | PUBLISHED_RECIPE_FROZEN_TRANSPORT_NOT_YET_BENCHMARKED |
| mirostat_original | Original: τ3; η1; μ0=6; feedback | Misma receta; N del modelo / same recipe, actual model N | AUTHOR_RECIPE_FROZEN_STATEFUL_DECODING_INTEGRATION_AND_BACKEND_TEST_REQUIRED |
| dola | Greedy; relative_top0,1; repetición1,2 / repetition1.2 | Mismo perfil; capas validadas / same profile, validated layer map | LAYER_NORM_HEAD_CACHE_COMPATIBILITY_REQUIRED_PER_MODEL |
| ees | θ1; versión final no sincronizada / final code not synchronized | No admitido / not admitted | BLOCKED_CAMERA_READY_CODE_PARITY_NOT_CLAIMED |

### talon_mass_right

**Autor / Author:** Facundo Firmenich

Receta propia del autor conservada íntegra: T externa0,85, masa0,92, strength0,7, mediana/MAD, tanh, rama right y protección externa. Sin K/P externos ni QAS.

Author's sealed TALON recipe preserved: external T0.85, mass0.92, strength0.7, median/MAD, tanh, right branch, outer guard; no external K/P or QAS.

**Fuentes fijadas / Pinned sources:** Núcleo sellado y acción autoral / sealed core and author action

**Receta efectiva íntegra / Complete effective recipe:**

```json
{
  "external_top_k": 0,
  "external_top_p": 1.0,
  "additional_repetition_penalty": 1.0,
  "qas": false,
  "temperature": 0.85,
  "do_sample": true,
  "operator_config": {
    "strength": 0.7,
    "temperature": 1.0,
    "head_fraction": 0.12,
    "mass_threshold": 0.92,
    "left_weight": 0.65,
    "right_weight": 1.2,
    "side_policy": "right",
    "selection_mode": "mass",
    "preserve_top1": false,
    "top1_preserve_momentum": 0.2,
    "kl_threshold": 0.0,
    "delta_form": "tanh",
    "absolute_min_tokens": 8,
    "std_method": "median_mad",
    "robust_eps": 1e-06,
    "debug": true
  },
  "outer_top1_projection": true,
  "pipeline": [
    "Effective",
    "TemperatureLogitsWarper",
    "AfterWarper"
  ]
}
```

### baseline_t100

**Autor / Author:** identity control

Único baseline T1. Es control de la comparación, no una temperatura universalmente óptima ni un control que aísle por sí solo el efecto de TALON de T0,85.

One T1 baseline; a comparison control, not a universal optimum or a temperature-matched causal isolation of TALON.

**Fuentes fijadas / Pinned sources:** Núcleo sellado y acción autoral / sealed core and author action

**Receta efectiva íntegra / Complete effective recipe:**

```json
{
  "external_top_k": 0,
  "external_top_p": 1.0,
  "additional_repetition_penalty": 1.0,
  "qas": false,
  "temperature": 1.0,
  "do_sample": true
}
```

### min_k

**Autor / Author:** Yuanhao Ding et al.

τ3/T1 procede expresamente del README de los autores. La diferencia con constructorτ2 y CLI sin argumentos T4 no lo convierte en una invención nuestra. Se fija el comando documentado, no defaults accidentales.

Tau3/T1 is explicitly prescribed by the authors' README. Constructor tau2 and bare CLI T4 are distinct artifacts; the documented reproduction command is the authority.

**Fuentes fijadas / Pinned sources:** [mink_readme](https://github.com/YecanLee/Mink/blob/39fa4cb070212c04eb32897898e383b42da530ae/README.md) · [mink_code](https://github.com/YecanLee/Mink/blob/39fa4cb070212c04eb32897898e383b42da530ae/llm_mink.py)

**Receta efectiva íntegra / Complete effective recipe:**

```json
{
  "external_top_k": 0,
  "external_top_p": 1.0,
  "additional_repetition_penalty": 1.0,
  "qas": false,
  "temperature": 1.0,
  "do_sample": true,
  "tau": 3.0,
  "implementation": "MinkLogitsProcessor",
  "range_epsilon": 1e-08,
  "pipeline": [
    "MinK_on_raw_logits",
    "temperature_once",
    "sample"
  ]
}
```

### top_h

**Autor / Author:** Erfan Baghaei Potraghloo, Seyedarmin Azizi, Souvik Kundu, Massoud Pedram

Valores del constructor autoral. La implementación histórica HF5.16.1 sigue identificada como tal; no se presupone equivalencia bit a bit con el código autoral. El bucle y dispositivo del código original requieren prueba de borde antes de portarlo. No se sustituye en silencio.

Author constructor parameters retained. Historical HF5.16.1 remains explicitly identified; raw author-code equivalence is not assumed. Boundary/device admission precedes any implementation replacement.

**Fuentes fijadas / Pinned sources:** [top_h_code](https://github.com/ErfanBaghaei/Top-H-Decoding/blob/8b94d62b238ed62793627f4a2556d90188560854/logit_processor.py) · [top_h_eval](https://github.com/ErfanBaghaei/Top-H-Decoding/blob/8b94d62b238ed62793627f4a2556d90188560854/lm_evaluate.sh)

**Receta efectiva íntegra / Complete effective recipe:**

```json
{
  "external_top_k": 0,
  "external_top_p": 1.0,
  "additional_repetition_penalty": 1.0,
  "qas": false,
  "temperature": 1.0,
  "do_sample": true,
  "alpha": 0.4,
  "top_n": 100,
  "implementation_identity": "historical HF5.16.1 TopHLogitsWarper; not silently relabeled as raw author code",
  "author_target": "TopH_LogitsProcessor"
}
```

### min_p

**Autor / Author:** Minh Nhat Nguyen et al.

p0,10 está dentro de la recomendación0,05–0,10 de sus autores. T1 conserva nuestro panel y pertenece a sus evaluaciones; no se impone T0,85 de TALON. Sin Top-P adicional tomado de un ejemplo ilustrativo.

p0.10 lies within the authors' recommended0.05–0.10 range. T1 is an evaluated setting, not TALON's T0.85. No unrelated top-p filter is inherited from an illustrative snippet.

**Fuentes fijadas / Pinned sources:** [min_p_readme](https://github.com/menhguin/minp_paper/blob/c21ceec41038ffd0ead508f56c60b7474175a62a/README.md)

**Receta efectiva íntegra / Complete effective recipe:**

```json
{
  "external_top_k": 0,
  "external_top_p": 1.0,
  "additional_repetition_penalty": 1.0,
  "qas": false,
  "temperature": 1.0,
  "do_sample": true,
  "min_p": 0.1,
  "min_tokens_to_keep": 1,
  "pipeline": [
    "temperature_once",
    "min_p_relative_cutoff",
    "sample"
  ]
}
```

### p_less

**Autor / Author:** Runyan Tan, Shuang Wu, Phillip Howard

Variante original p_less_decode; no norm ni affine. Umbral sin hiperparámetros. La temperatura se aplica una sola vez antes de formar probabilidades.

Original p_less_decode, not norm or affine. Hyperparameter-free cutoff; temperature applied once before probabilities.

**Fuentes fijadas / Pinned sources:** [p_less_code](https://github.com/ryttry/p-less/blob/a681f23682a329099306eea9cf7b1dd0447e2eec/p_less_samplers.py)

**Receta efectiva íntegra / Complete effective recipe:**

```json
{
  "external_top_k": 0,
  "external_top_p": 1.0,
  "additional_repetition_penalty": 1.0,
  "qas": false,
  "temperature": 1.0,
  "do_sample": true,
  "function": "p_less_decode",
  "variant": "original, not p_less_norm_decode",
  "pipeline": [
    "temperature_once",
    "softmax",
    "author_p_less_decode"
  ]
}
```

### top_nsigma

**Autor / Author:** Chenxia Tang, Jianchun Liu, Hongli Xu, Liusheng Huang

n1 es el default recomendado por sus autores. σ conserva torch.std con corrección1. Se aplica antes de truncadores que contaminen la desviación; no se mezcla con K/P externos.

n1 is the paper-recommended default. Preserve torch.std correction1 and apply before other truncators; no external K/P stack.

**Fuentes fijadas / Pinned sources:** [top_nsigma_code](https://github.com/Tomorrowdawn/top_nsigma/blob/82ac59a5c36da7d9d0f83b3a6e5ab57eaa9442d0/src/hf/hf_nsigma.py)

**Receta efectiva íntegra / Complete effective recipe:**

```json
{
  "external_top_k": 0,
  "external_top_p": 1.0,
  "additional_repetition_penalty": 1.0,
  "qas": false,
  "temperature": 1.0,
  "do_sample": true,
  "nsigma": 1.0,
  "std_correction": 1,
  "pipeline": [
    "TopNSigma_on_untruncated_logits",
    "temperature_once",
    "sample"
  ]
}
```

### eta_sampling

**Autor / Author:** John Hewitt, Christopher D. Manning, Percy Liang

Se transporta sin ajuste la receta autoral de evaluación humana ε0,0006/T1/K0/P1. No es un default universal para todos los modelos; el 0,0009 usado en otros papers comparativos no se atribuye a Hewitt et al. No cambiar según nuestros resultados.

Transport the original authors' human-evaluation epsilon0.0006/T1/K0/P1 recipe without retuning. Not a universal all-model optimum; do not misattribute another paper's0.0009 comparator setting to these authors.

**Fuentes fijadas / Pinned sources:** [eta_recipe](https://github.com/john-hewitt/truncation-sampling/blob/2f33a7498a4a6e6e2bb3ae2d54cb5178ebde9272/human_eval/README.md) · [eta_variants](https://github.com/john-hewitt/truncation-sampling/blob/2f33a7498a4a6e6e2bb3ae2d54cb5178ebde9272/src/simple_repetition.py) · [eta_code](https://github.com/john-hewitt/truncation-sampling/blob/2f33a7498a4a6e6e2bb3ae2d54cb5178ebde9272/src/warpers.py)

**Receta efectiva íntegra / Complete effective recipe:**

```json
{
  "external_top_k": 0,
  "external_top_p": 1.0,
  "additional_repetition_penalty": 1.0,
  "qas": false,
  "temperature": 1.0,
  "do_sample": true,
  "eta_cutoff": 0.0006,
  "adaptive_threshold": "min(epsilon,sqrt(epsilon)*exp(-H(p)))",
  "keep_argmax": true,
  "pipeline": [
    "temperature_once",
    "EtaWarper",
    "sample"
  ]
}
```

### mirostat_original

**Autor / Author:** Sourya Basu, Govardana Sachitanandam Ramachandran, Nitish Shirish Keskar, Lav R. Varshney

Original autoral: τ3bits, learning_rate1, μ0=6 y100 pares para estimar s en el script. Se exige feedback del token realmente muestreado. No sustituir por Mirostat2, por defaults de terceros τ5/η0,1 ni por el comparador sin feedback del repo Min-K. N se obtiene del modelo como en el algoritmo general del paper; se declara la adaptación del demo GPT2.

Original author recipe: tau3bits, learning_rate1, mu0=6 and100 rank pairs in the script. Update using the actual sampled token. No substitution by Mirostat2, downstream tau5/eta0.1 defaults or Min-K's stateless comparator. N is the model vocabulary as in the paper's general algorithm; the GPT2-demo adaptation is explicit.

**Fuentes fijadas / Pinned sources:** [mirostat_readme](https://github.com/basusourya/mirostat/blob/ea2e61b511f1316e663228c0def2c4c143b3c417/README.md) · [mirostat_code](https://github.com/basusourya/mirostat/blob/ea2e61b511f1316e663228c0def2c4c143b3c417/mirostat.py)

**Receta efectiva íntegra / Complete effective recipe:**

```json
{
  "external_top_k": 0,
  "external_top_p": 1.0,
  "additional_repetition_penalty": 1.0,
  "qas": false,
  "temperature": 1.0,
  "do_sample": true,
  "variant": "original",
  "tau_bits": 3.0,
  "learning_rate": 1.0,
  "mu_initial": 6.0,
  "estimate_s_rank_pairs": 100,
  "vocabulary_size": "actual model output vocabulary N, from paper Algorithm1; replaces GPT2-demo constant50000, not outcome-tuned",
  "surprise": "-log2(p_original[selected_token]) before adaptive truncation",
  "state_update": "mu <- mu -1.0*(surprise-3.0)",
  "state_reset": "mu=6 once per fresh prompt/seed, not per token",
  "k_rounding": "round(k)+1",
  "external_fixed_top_k_disabled": true,
  "pipeline": [
    "softmax_T1",
    "estimate_s",
    "adaptive_top_k_from_mu",
    "sample",
    "update_mu_from_actual_sample"
  ]
}
```

### dola

**Autor / Author:** Yung-Sung Chuang et al.

Un perfil greedy con plausibilidad0,1 y repetición1,2. La lista de capas depende de arquitectura/profundidad: no importar sin validar la lista de Llama a Qwen/Granite. T y P de muestreo son inactivos en greedy. El 110% es criterio de nuestra evaluación, no parámetro de los autores.

One greedy profile with relative_top0.1 and repetition1.2. Record model-specific layer mapping; no unvalidated Llama-layer transfer. Sampling T/P inactive in greedy.110% is our evaluation rule, not an author parameter.

**Fuentes fijadas / Pinned sources:** [dola_gsm8k](https://github.com/voidism/DoLa/blob/805230e57e63ca561cb759994681b122ff6f81f0/gsm8k_eval.py)

**Receta efectiva íntegra / Complete effective recipe:**

```json
{
  "do_sample": false,
  "relative_top": 0.1,
  "repetition_penalty": 1.2,
  "dola_layers": "low; exact supported-model mapping must be recorded",
  "temperature": "inactive in greedy",
  "qas": false,
  "time_budget_factor": 1.1,
  "time_adjudication": "paired final and on-time; not generation kill",
  "reference_membership": "freeze per actual campaign; never retroactively add new comparators"
}
```

### ees

**Autor / Author:** Xiaodong Cai et al.

Se documenta, pero no se inventa una receta ejecutable: el README autoral avisa de que el código público no está sincronizado con la versión final. No incluirlo ni asignarle resultados hasta resolver esa correspondencia.

Documented, not silently admitted: the authors explicitly state that public code predates camera-ready experiments. No executable parity or results are claimed.

**Fuentes fijadas / Pinned sources:** [ees_release_status](https://github.com/shuanncai/Entropy-Equilibrium-Sampling/blob/03eccde61c92dafce9bc67572f1ff276206f9a39/README.md)

**Receta efectiva íntegra / Complete effective recipe:**

```json
null
```

## Garantías y límites del cambio

1. No más cambios silenciosos: cualquier variante numérica, de orden, backend, implementación o filtros requiere versión explícita y diff; no se acumula dentro del mismo identificador.
2. El comando autoral explícito tiene prioridad sobre el default de constructor no invocado y sobre ejemplos de terceros. Los datos crudos históricos no cambian de etiqueta retrospectivamente.
3. η-sampling transporta una receta original ε0,0006/T1. El valor depende del protocolo publicado; no afirmamos que sus autores lo optimizaran en Qwen, Phi o Granite. Las alternativas originales quedan en el JSON. Mirostat usa el algoritmo original con aprendizaje por token, no Mirostat2 ni una aproximación sin feedback. Ese aprendizaje es parte del algoritmo, no calibración nuestra a posteriori.
4. Top-H mantiene explícita la identidad HF histórica. No se presume que igualar α/top_n/T haga idénticos dos códigos. La receta autoral y la implementación efectiva están separadas: cualquier sustitución requiere validación numérica. El top_n100 propio de Top-H y el k adaptativo propio de Mirostat no son un Top-K50 externo añadido.
5. EES permanece candidato: el propio README avisa de código anterior a la versión final. No lanzar el código antiguo bajo la etiqueta de reproducción camera-ready.
6. No se importan límites de200/256/512/1024 tokens, semillas, modelos o hardware de ejemplos autorales como si fueran hiperparámetros intrínsecos del operador. La campaña fija sus propios modelos y precisión de forma emparejada. EOS natural, contexto/proveedor y presupuesto total finitos; censuras separadas de fallos de respuesta.
7. El guardia adjunto verifica el canon y rechaza valores efectivos distintos. Está probado de forma autónoma; esta tarea no ha conectado el guardia a cuadernos remotos ni lanzado inferencia. No se afirma una protección operativa que todavía no se haya integrado.

### Cierre científico y operativo

Queda mejor identificada la comparación: Min-K recupera su atribución autoral correcta sin cambiar τ3/T1, TALON conserva intacta su acción y las dos incorporaciones tienen receta reproducible en vez de nombres ambiguos. Esto mejora procedencia y estabilidad metodológica; no produce victorias nuevas ni demuestra transporte multimodelo. Antes de una corrida nueva se debe comprobar la admisión del backend, que su receta efectiva coincide con este JSON y que existe ficha visible del experimento.

## English: governing contract

Use each comparator's documented author recipe, not TALON's settings. Min-K tau3/T1 is explicitly the authors' reproduction command: this correction changes attribution, not numbers. Constructor tau2 and bare CLI T4 remain separate provenance. TALON's sealed action, external T0.85 and no external K/P are unchanged; one T1 baseline and seeds64/12/24/48/96 remain.

A conventional recipe means an identified published protocol, not an invented universal optimum. Where authors publish several recipes, identify the selected one before test outcomes. Eta transports the authors' human-evaluation epsilon0.0006/T1 recipe. Mirostat uses the original stateful algorithm with tau3bits, learning_rate1, initial mu6 and actual-token feedback; not Mirostat2 or another paper's stateless approximation. Transporting the paper's vocabulary-size variable is declared, not hidden.

Historical HF Top-H remains distinguished from raw author code; matching hyperparameters does not prove implementation identity. EES remains unadmitted because its authors disclose unsynchronized camera-ready code. Frozen recipe values do not imply validated backend integration.

Future changes require explicit versioning and changed-field records. Preserve predecessor bytes, raw results and adverse evidence. Do not inherit incidental example token limits, model ids or seeds into this campaign. Declare finite context/provider/campaign limits and censoring separately. The standalone guard is tested, but no provider notebook is modified or launched by this document.

**Substantive closure:** provenance and reproducibility improve; empirical performance does not change. Next validate each execution adapter against the exact selected author mechanism, its order and this effective JSON before a visible run card and any new inference.

## Lectura y recuperación / Reading and recovery

The companion JSON contains the source registry with exact upstream commits and Git blob identities, full recipes, all TALON fields, admission boundaries and the change log. This Markdown is generated from that same JSON construction, not a second manually diverging recipe source. The checksum file covers exact bytes. A published receipt records actual remote object ids and commit after verification; it is not fabricated in advance.
