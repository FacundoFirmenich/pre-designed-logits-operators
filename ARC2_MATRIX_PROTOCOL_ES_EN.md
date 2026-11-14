# ARC-AGI-2: contraste de inducción matricial / matrix induction contrast

## Castellano

Se comparan cuatro políticas sobre el mismo modelo, Qwen3.5-4B revisión `851bf6e806efd8d0a36b00ddf55e13ccb7b8cd0a`, en una NVIDIA T4 con pesos NF4 de doble cuantización y cómputo FP16. Los brazos son baseline de referencia del piloto (top-k 20, top-p 0,95), TALON Mass Right con ese mismo truncamiento posterior, Top-H 0,40 y TALON Mass Right sin truncamiento posterior. TALON conserva su configuración histórica congelada. No se ejecutan QAS, Z Explorer, Min-p ni Min-k en esta admisión.

Las tareas de desarrollo son `1e81d6f9` y `5751f35e` del split público de entrenamiento del commit `f3283f727488ad98fe575ea6a5ac981e4a188e49`. Se verificó en CPU la existencia de una regla que reproduce exactamente cada salida, incluidas las de prueba. Las reglas de referencia no están en el cuaderno distribuido ni en el prompt. La gramática fue desarrollada con estos casos; no hay afirmación de validación ciega ni puntuación oficial.

Preflight: 16 generaciones emparejadas, una por celda tarea × semilla (11, 33) × brazo, con 8.192 tokens máximos de razonamiento y 512 reservados para respuesta. Si un razonamiento o respuesta se corta por el tope, el bloque de la tarea, completo, pasa a 16.384 tokens de razonamiento. Se registran por separado cierre nativo, cierre forzado, fin antes de responder, error de análisis, error de ejecución, ajuste a demostraciones y coincidencia exacta de la matriz de prueba. No se consulta la salida de prueba para generar ni seleccionar programas.

El endpoint principal local es regla ejecutable que satisface todas las demostraciones y acierta la matriz nueva. Se informa también acierto exacto sin la exigencia adicional de consistencia en demostraciones. Se mantienen distintos los aciertos conjuntos, fallos conjuntos, rescates y pérdidas entre pares; un empate por fallo conjunto no demuestra equivalencia. La campaña no fue diseñada para inferencia poblacional.

El cuaderno se abrió desde Drive en Colab visible. Drive solicitó permiso de acceso a todos los archivos y el montaje agotó el plazo antes de cargar pesos; la reanudación usa el mismo manifiesto y la misma T4, sin montar Drive, mostrando la evidencia en el cuaderno. Ningún entorno ajeno se detuvo. No confundir el preflight en CPU con un resultado de Qwen.

Enmienda operacional: la primera carga en GPU llegó al checkpoint de Qwen, pero la clase no expuso `hf_device_map`. La reanudación verifica que todos los parámetros residan realmente en `cuda:0` y, si existe un mapa de despacho, verifica además que no indique CPU ni disco. El cuaderno conserva ambos intentos y enlaza el nuevo manifiesto con el anterior; sin cambios en el experimento.

Segunda enmienda de runtime: la pasada separada de respuesta volvió a preprocesar la cadena larga y falló por memoria (6,46 GiB solicitados con 3,18 GiB libres) antes de producir la primera fila. El intento siguiente conserva una sola caché a través del límite razonamiento/respuesta. Se preservan las cuotas, la misma máquina, las semillas y los brazos; no se presume equivalencia bit a bit entre ambas implementaciones. El cuaderno registra el manifiesto nuevo `830649a4f280f7855bbc1c5ea0e55096ce4c28c26266f1c78f71235443549cec`; el intento anterior no tiene ninguna fila adjudicable.

## English

Four policies share one Qwen3.5-4B revision, one T4, double-quantized NF4 weights and FP16 compute: the inherited top-k 20/top-p 0.95 baseline, TALON Mass Right followed by the same truncation, author Top-H at 0.40, and TALON Mass Right without downstream truncation. The historical TALON configuration is unchanged. QAS, Z Explorer, Min-p and Min-k are outside this admission.

Two public-training tasks, `1e81d6f9` and `5751f35e`, were checked on CPU with reference rules that are not embedded in the distributed notebook or supplied to the model. The DSL was developed on these cases. This is a development diagnostic, not blind validation or a leaderboard score.

The first tier consists of 16 paired cells with seeds 11 and 33, a reasoning limit of 8,192 tokens, and a separate 512-token answer budget. Any budget-censored output triggers a full task-block rerun at 16,384 reasoning tokens. Statuses distinguish syntax, execution, demonstration consistency, exact test output, and censoring. The primary local endpoint requires both demonstration consistency and an exact test grid; exact-only is recorded separately.

The notebook was opened from Drive in visible Colab. Drive mounting timed out before model load; the same plan was resumed on the same T4 without a Drive mount, with evidence emitted to the notebook. No unrelated runtime was stopped. CPU executor checks are not Qwen scores.

Operational amendment: the first attempt loaded Qwen but the class did not expose `hf_device_map`. The resumed run checks the actual residency of every parameter in `cuda:0` and additionally checks the dispatch map when present. The notebook retains both attempts and links their manifests without changing the experiment.

Second runtime amendment: a separate answer-generation prefill exhausted GPU memory (6.46 GiB requested against 3.18 GiB free) before any row was committed. The next attempt uses one continuous KV cache across reasoning and answer generation under the same task, seed, arm and token budget. This does not assert bitwise equivalence between implementations. The notebook records the new linked manifest.
