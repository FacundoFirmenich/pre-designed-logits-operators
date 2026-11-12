# Freeze v1.0 — jurisdicciones locales de decodificación en Qwen 4-bit

**Identidad:** `CFL-QWEN-GSM8K-10SEED-v1`. **Estado:** diseño congelado antes de nuevos resultados; admisión física del modelo, repositorio de destino y lanzamiento pendientes. No es el piloto Qwen3.5‑4B ni su extensión. No usar sus salidas como filas de esta campaña. No se ejecutan LLaMA, Gemma, Phi, RDS, P07 ni TALON Mass Left en v1.0.

## 1. Objetivo, unidad y panel

Localizar dónde gana, empata, pierde o cambia de signo cada método. **La unidad científica es el prompt**, con diez repeticiones emparejadas; la fila física es `(dataset_revision, item_id, mode, seed, model_revision, quantization, arm, protocol)`. La puntuación global es un inventario descriptivo, no una regla de adjudicación. Un método puede perder globalmente y aportar un acierto exclusivo local; ese caso no se descarta.

GSM8K test original: [OpenAI, commit 3101c7d](https://github.com/openai/grade-school-math/blob/3101c7d5072418e28b9008a6636bde82a006892c/grade_school_math/data/test.jsonl), 1.319 filas, índices desde cero, SHA‑256 `3730d312f6e3440559ace48831e51066acaca737f6eabec99bccb9e4b3c39d14`. Usar 60 casos nuevos. Excluir la unión de los 32 del piloto y los 24 del contraste anterior (la extensión izquierda comparte esos 24). Entre los restantes ordenar por SHA‑256 de UTF‑8 `CFL-QWEN-GSM8K-10SEED-v1:item:<id>`, ascendente, desempate por id, y tomar los primeros 60. No se inspecciona utilidad al seleccionar.

| Bloque | IDs en orden fijado |
|---|---|
| 01 | 1193, 880, 630, 1087, 607 |
| 02 | 690, 70, 1120, 316, 730 |
| 03 | 719, 893, 1142, 1181, 708 |
| 04 | 61, 813, 431, 945, 835 |
| 05 | 149, 800, 1001, 814, 483 |
| 06 | 978, 451, 1254, 512, 507 |
| 07 | 650, 204, 400, 460, 1212 |
| 08 | 889, 881, 659, 458, 702 |
| 09 | 1057, 276, 996, 228, 1232 |
| 10 | 525, 123, 489, 839, 953 |
| 11 | 856, 289, 84, 394, 975 |
| 12 | 71, 1031, 1135, 705, 1189 |

**Semillas:** `11, 22, 33, 44, 55, 66, 77, 88, 99, 110`. Las diez en cada prompt, brazo y modo previsto. Reinicializar RNG Python/NumPy/Torch CPU y CUDA antes de cada fila; ninguna celda consume el RNG dejado por la anterior. La misma semilla empareja el diseño, no garantiza trayectoria ni número aleatorio efectivo idénticos entre bucles de generación distintos. Orden por SHA‑256 de `CFL-QWEN-GSM8K-10SEED-v1:arm:<id>:<mode>:<seed>:<arm_id>`, empate por arm_id.

## 2. Qwen más pesado elegible y admisión sin mirar el test

Recursos: GPU efectivamente disponibles en Kaggle, inicialmente **dos T4**; un modelo compartido entre ellas para el estrato pesado. No se presupone una GPU de pago, dos copias del modelo, CPU/disk offload ni VRAM disponible por sumar etiquetas. Se elige la **clase nominal de mayor número total de parámetros** entre candidatos oficiales Qwen de uso general que se puedan ejecutar con el mismo stack de intervención y 4-bit; dentro de la misma clase, aplicar el orden escrito. Parámetros activos de MoE se registran aparte: no equivalen a memoria de todos los expertos residentes. Los Qwen oficiales de 72B, 80B, 122B, 180B y superiores no son candidatos en dos T4: el límite inferior de pesos 4-bit supera su memoria nominal combinada, antes de KV y cómputo.

| Orden | Checkpoint oficial | Revisión HF fija | Cuantización de pesos |
|---|---|---|---|
| 1 | Qwen3.6‑35B‑A3B | `345d467b117d1fd5eda9b879a5988de9ae5f47a7` | NF4, doble cuantización |
| 2 | Qwen3.5‑35B‑A3B‑GPTQ‑Int4 | `3af5ca2972faf6de1fd6f4efc4d8d319ca751e8b` | GPTQ Int4 publicado por Qwen |
| 3 | Qwen3.5‑35B‑A3B | `59d61f3ce65a6d9863b86d2e96597125219dc754` | NF4 |
| 4 | Qwen3‑32B | `9216db5781bf21249d130ec9da846c4624c16137` | NF4 |
| 5 | Qwen2.5‑32B‑Instruct | `5ede1c97bbab6ce5cda5812749b4c0bdf79b18dd` | NF4; sólo elegible si cumple ambos modos nativos |
| 6 | Qwen3‑30B‑A3B | `ad44e777bcd18fa416d9da3bd8f70d33ebb85d39` | NF4 |
| 7 | Qwen3.8‑27B | `37561816e66b5b9153b1b64c10968c18c1e6f4a0` | NF4 |
| 8 | Qwen3.6‑27B | `8f33b98937c6031bb49e713dee3e8e185aafd26f` | NF4 |
| 9 | Qwen3.5‑27B‑GPTQ‑Int4 | `8f0c09f227ae570e79617c6d9172b59df9c16081` | GPTQ Int4 oficial |

Las revisiones se fijaron por los metadatos oficiales. El orden es de **admisión**, no de calidad observada. Si ninguno pasa, detenerse y enmendar el diseño antes del test; no volver automáticamente a 4B. Referencias primarias: [Qwen 35B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B), [GPTQ Int4 oficial](https://huggingface.co/Qwen/Qwen3.5-35B-A3B-GPTQ-Int4), [Qwen 32B](https://huggingface.co/Qwen/Qwen3-32B) y [Qwen 27B](https://huggingface.co/Qwen/Qwen3.8-27B).

Admisión: comprobar almacenamiento temporal **remoto** y cargar por revisión, con mapa GPU sin offload. NF4 con cómputo FP16 y doble cuantización; GPTQ sólo con backend Int4 que funcione en T4 y exponga los logits al mismo pipeline. Inventariar precisión real por familia de tensores, incluidos expertos y proyecciones; no basta `load_in_4bit=True` si quedan expertos de bloques a 16 bits. Excepciones declaradas: embeddings, normalizaciones y cabeza de salida si la implementación oficial no los cuantiza. Usar los primeros cinco ejemplos de **train** sólo como canarios mecánicos, y una prueba de longitud hasta el máximo de entrada del panel más 1.024 nuevos tokens sin usar las respuestas de test. Exigir ambos modos nativos, callbacks de logits, pipeline exacto, finite outputs, contrato de TALON y margen de al menos 1 GiB en cada GPU tras el pico. Sólo compatibilidad, memoria, almacenamiento o límite de recursos permiten pasar al siguiente candidato; no scores. Persistir mapa, precisión, versiones, canarios, motivos de exclusión y recibo de admisión. La receta ejecutable y dependencias se sellan en un manifiesto de lanzamiento antes de generar test. Punto de partida: imagen Kaggle `gcr.io/kaggle-private-byod/python@sha256:9a6bcfda6d03b2cd9aa347ee8c1bae62043328ed0f4afe9bda014e4f8bbf9435`, Transformers 5.16.1 y bitsandbytes 0.50.2 para NF4; cualquier adaptación técnica se fija antes del test, no se cambia por brazo.

## 3. Modos, protocolo común y brazos

- **Principal:** `enable_thinking=False`, 60 prompts. **Mini inverso:** `enable_thinking=True`, sólo los cinco prompts del bloque 01. Los mismos brazos admitidos, diez semillas, modelo, cuantización, presupuesto y texto de entrada. No requiere repetir el bloque 01 principal. Si el checkpoint no tiene ambos modos nativos, no simular uno por indicación textual.
- Una secuencia por celda, batch 1, sin beam, **T=1**, máximo **1.024 tokens nuevos en ambos modos**, EOS nativo y caché nativa. Sin penalización, reranking ni herramientas. Zero-shot: `Solve the math problem below. Show a concise calculation, then end with exactly one line of the form #### NUMBER.\n\n` más el enunciado original. La plantilla cambia sólo por el modo nativo; persistir su hash. Si «Eagle» significa [EAGLE](https://arxiv.org/abs/2401.15077), no se activa aceleración especulativa, draft ni assistant model. Si se refería a `eager`, no forzar backend de atención; registrar el valor efectivo por defecto.
- Baseline único: sin intervención, Top‑k 20 y luego Top‑p 0,95. Los operadores de transporte y DoLa comparten esta truncación **posterior**. Los rivales truncadores **reemplazan** esta cadena, no se les apila Top‑k/Top‑p. Parejas full/QAS conservan su mismo pipeline posterior. La comparación entre familias es de pipelines; los pares full/QAS aíslan la cualificación con el contrato fijado.

| Método fijo | Sin QAS | Con QAS | Identidad y parámetros |
|---|---|---|---|
| Baseline | `baseline` | Identidad, sin otra generación | QAS sobre transformación nula no cambia scores. Comprobar identidad antes de compartir la fila; si falla, detener, no imputar. |
| TALON Mass Right | `talon_mass_right` | `talon_mass_right_qas` | Runtime v1.2, fuerza 0,70, masa 0,92, T interna 1, lado right, top‑1 preserve. |
| TALON Soft Left | `talon_soft_left_v064` | `talon_soft_left_v064_qas` | Soft v0.6.4, selector hybrid-head 0,10 ∪ masa 0,90; fuerza 0,45, temperatura interna 0,8, pesos 0,65/1,20, mínimo 3, tanh, mediana/MAD ε=10⁻⁶, KL 0,015, mezcla de proyección 0,35, `side_policy=left`. |
| TALM Soft Left | `talm_mass_left_soft` | `talm_mass_left_soft_qas` | Runtime v1.2, fuerza 0,70, masa 0,025, pesos izquierda/derecha 0,80/0,20, boosts 0,08/0,28, caps 8/4096, T interna 1; sin proyección obligatoria. |
| Min‑p | `min_p_0p10` | `min_p_0p10_qas` | Min‑p 0,10, conserva al menos un token; implementación nativa del stack fijado. |
| Min‑k | `min_k_tau_2` | `min_k_tau_2_qas` | τ=2, default de la clase de autores usada en la tanda anterior; no confundir con τ=3 del protocolo del paper. [Fuente fijada](https://github.com/YecanLee/Mink/blob/39fa4cb070212c04eb32897898e383b42da530ae/llm_mink.py). |
| Top‑H | `top_h_alpha_0p40` | `top_h_alpha_0p40_qas` | α=0,40, top‑N=100; mismo criterio entrópico, borde de no cruce definido como prefijo completo. [Fuente de autores](https://github.com/ErfanBaghaei/Top-H-Decoding/blob/8b94d62b238ed62793627f4a2556d90188560854/logit_processor.py). |
| TFS | `tfs_z_0p95` | `tfs_z_0p95_qas` | z=0,95, variante de curvatura ya fijada en laboratorio, mínimo un token. |
| DoLa condicional | `dola_low` | `dola_low_qas` | Contraste dinámico de capas low, con el mismo Qwen y soporte cualificado sólo si ambos canarios pasan. Si no, ambas celdas se marcan `NOT_ADMITTED`; no sustituir Qwen por LLaMA ni omitir el fallo. |

**Identidad de código propio:** runtime v1.2 `f41318f04188e88d7a28bcdeff19ca4d388370cb68165fd81285f0f600d9f78c`; núcleo Soft histórico `4238fb56642e3d173e6108022e5c5f4f29519d680ccbe163ecff696a68a041b4`. En ambos TALON, verificar argmax real antes y después del warper en el tensor que consume el sampler. La envoltura prospectiva conserva scores cuando el argmax ya coincide; ante cruce, eleva el token original al siguiente valor representable sobre el máximo rival en dtype efectivo. Si el valor no es finito o el contrato falla, la celda no es conforme. No se traslada al brazo Soft Left el resultado histórico de Soft Right. TALM registra cruces sin corregirlos.

**DoLa sí hizo GSM8K:** [artículo, apéndice B, tabla 5](https://arxiv.org/html/2309.03883v2) y [script de los autores](https://github.com/voidism/DoLa/blob/main/gsm8k_eval.py). Coincide el benchmark, no el checkpoint, precisión, prompt o protocolo. Es referencia externa contextual, no una fila emparejada. La implementación de comunidad fijada `af6cdc351e7e0bd28a86ce32aac461494a09a9c1` rechazó el Qwen3.5 stateful previo. Se intenta con el modelo admitido sin quitarle protecciones por conveniencia. El canario QAS debe acceder al logit maduro **y** al contrastado del mismo paso, no reconstruirlo desde texto.

## 4. QAS universal: misma pregunta, cambios de distinto tipo

QAS cualifica **dónde se aplica la acción**, no elige el brazo. En la misma entrada finita z y el contrafactual bruto u: (a) para cambios finitos, energía `|u_i-z_i|*sqrt(max(p_i*(1-p_i),1e-8))`; (b) para exclusiones intrínsecas `u_i=-∞`, energía de máscara `p_i`, con p=softmax(z). No restar infinitos. Si coexisten ambos canales no nulos, normalizar cada uno por su suma y promediarlos 1/2–1/2. Si hay uno solo, usarlo; sin señal, devolver z. 

Tomar unión de top‑1 original, prefijo de masa 0,95 dentro de top‑256 baseline y prefijo de energía 0,90 dentro de top‑512, mínimos 64 por lista cuando haya candidatos y cap de unión 1024; empates por ID de token. Medir retención sobre el vocabulario completo, no sólo sobre la lista. Copiar u en el soporte cualificado y conservar z fuera. Para un truncador, esto significa **aplicar sus exclusiones sólo en la zona cualificada**; puede dejar vivos tokens inicialmente finitos que el truncador completo hubiera quitado. No reabre tokens prohibidos en z, no usa delta ficticio y no es el truncador original sin modificaciones. Para TALON usar el mismo contrato final en ambos modos; para TALM no imponerlo. Si una variante es mecánicamente idéntica en ciertas celdas, conservar ese empate. Esta extensión de QAS a exclusiones es prospectiva y se distingue de la versión anterior de sólo delta finito.

## 5. Z‑Explorer en los extremos, no como sustituto del enrutador

Incluir la **búsqueda de cisnes negros en los extremos de las colas** como módulo transversal de sondeo. Protocolo experimental congelado de esa variante: al prefill y a los offsets 8/32 de la trayectoria baseline de cada semilla cuando existan, comparar todos los brazos sobre el **mismo prefijo**. Definir las dos zonas en el vector baseline **antes de cualquier warper**, ordenando tokens finitos por log‑probabilidad e ID; desde cada extremo tomar el prefijo que alcance masa 0,01 o agote 512 tokens; si se solapan, asignar a la primera inclusión del extremo bajo y deduplicar. Conservar fronteras y masa efectivamente cubierta; en el extremo alto puede bastar un token. En cada zona registrar candidatos que ganan/pierden masa, entran/salen del soporte y desplazan rango frente al baseline **después** de cada pipeline de muestreo; persistir los primeros 8 por signo y magnitud absoluta de desplazamiento, desempate por token ID, más los totales de masa. En un mismo prefill se reutiliza la observación para las diez semillas sin contarla diez veces como evidencia independiente. Un hallazgo extremo es **candidato** a cisne negro, no prueba de valor semántico. Vincularlo luego con victorias/exclusividades locales sin usarlo para elegir el brazo. La variante de sondeo no muestrea ni recibe un score ficticio; cualquier futuro brazo generativo Z tendría dos versiones full/QAS y un freeze propio. La otra alternativa de Z‑Explorer no se define por analogía.

## 6. Evaluación y checkpoints de cinco prompts en Kaggle

- **Adjudicación:** comparar el número de la última línea de respuesta visible si cumple `#### NUMBER` y es el único marcador válido; igualdad Decimal con gold oficial. Sensibilidad independiente: último número de la respuesta visible. No contar trazas de thinking como respuesta; persistir texto/tokens y separar segmentos con el protocolo nativo. Registrar marcador ausente/múltiple, respuesta no emitida, límite, excepción, cruce, OOM y no admisión. Un fallo de infraestructura no es una respuesta incorrecta imputada.
- **Local primero:** tabla por prompt y semilla, métodos A/B, W/T/L, respuesta, masa/soporte, tiempo y primera divergencia. Sobre las diez semillas, A domina observacionalmente a B si hay ≥1 victoria y ninguna derrota con diez pares disponibles; cualquier victoria y derrota en el mismo prompt es MIXTO. Empates completos y `NOT_ESTIMABLE` van separados. Reportar acierto exclusivo por semilla cuando sólo un brazo del conjunto admitido y completo acierta, y la recurrencia 0…10 por prompt. Nombrar el conjunto de rivales; un DoLa no admitido no cuenta como derrotado. Desglosar rescates fuera del envelope de Mass Right y pérdidas; no inferir jurisdicción universal de una única semilla. Los agregados, si se muestran, conservan agrupación por prompt y no gobiernan promociones.
- **Cómputo:** 15 brazos obligatorios × 60 × 10 = **9.000** generaciones principales; mini inverso 750. DoLa añade 1.200 + 100 si se admite. Total **9.750** sin DoLa, **11.050** con DoLa. No contar baseline/QAS identidad ni replays de Z como generaciones nuevas. Medir wall, primera distribución, ms/token, GPU y memoria. No prometer que toda la tanda cabe en una cuota: estimar por canario, usar cuotas disponibles y conservar los diez seeds al reanudar. Se permite paralelismo por bloque o por sublote cuando la cuenta y memoria lo permitan; no duplicar el modelo a costa de desbordar ni asumir dos jobs simultáneos.
- **Memoria persistente cada cinco prompts:** en Kaggle, un checkpoint confirmado es un **output de versión privada terminal** o una **versión privada de dataset derivada** con manifiesto, no sólo `/kaggle/working` de un job activo. Checkpoint por cada bloque de 5 prompts completos (15×5×10 celdas obligatorias, más DoLa si se admitió) y un checkpoint separado para el mini thinking. Si el tiempo de GPU obliga a subdividir, conservar outputs de cada sublote y ensamblar el checkpoint sólo al reunir su bloque completo. No sacrificar semillas ni empezar un run idéntico porque se perdió el proceso.
- **Reanudación:** guardar salidas completas y parciales adversas, identificadores, configuraciones, terminal provider y hashes por fila/archivo. Escritura de celda atómica a staging y versión persistente al cerrar el bloque. Reanudar desde el manifiesto de versiones confirmado, saltar sólo claves completas del mismo freeze, reutilizar semilla exacta; las reparaciones conservan el intento anterior y su causa. No cambiar candidatos, presupuesto, reglas, seeds o caso al mirar resultados de un checkpoint. Una incompatibilidad antes de toda ejecución abre una enmienda; un resultado desfavorable no.
- **Evaluación cada cinco:** guardar CSV por prompt×semilla, W/T/L, aciertos exclusivos y ejemplos adversos en el propio checkpoint. Se puede interpretar ese bloque cuando cierra, sin esperar los doce ni convertirlo en decisión de tuning. Al terminar, entregar consolidación por prompt, índices, logs, tablas QAS y mapa de Z‑Explorer. Custodia privada Kaggle y luego destino autorizado por el usuario; pesos y cachés grandes nunca al PC.

## 7. Continuidad

GSM8K es el primer panel externo; no presentar 60/1.319 como todo GSM8K ni resultados de publicaciones diferentes como comparaciones pareadas. Siguiente opción de razonamiento: **MATH‑500**, con freeze separado y evaluador propio; opción complementaria para instrucciones: **IFEval**, sin mezclar criterios. Tras cerrar Qwen, Gemma 4 y Phi‑4 serán fases separadas, no fallback de DoLa ni extensiones ya lanzadas. Este freeze no autoriza a redefinir las ramas o a incorporar RDS.
