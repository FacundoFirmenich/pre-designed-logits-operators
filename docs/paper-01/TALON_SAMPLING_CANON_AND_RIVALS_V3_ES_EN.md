# TALON · entorno canónico y ficha de los rivales / canonical sampling setup and rival run card

**Canon de entorno de este proyecto, confirmado por el autor:** tras TALON y la temperatura externa, **top‑k 50 → top‑p 0,95**. La selección expresa de top‑k 20 en un cuaderno exploratorio no se hereda como canon. Ningún cambio de estos filtros altera las reglas ni los parámetros internos de TALON. Esta entrada documenta la orden del autor; no afirma que todos los cuadernos anteriores hayan respetado el entorno.

| Brazo | Temperatura externa de esta campaña | Cadena de muestreo fijada |
|---|---:|---|
| TALON Mass Right, dos brazos | 0,85 y 0,88 | TALON → temperatura → **top‑k 50 → top‑p 0,95**. No hay brazo TALON a 1,00. |
| Baseline emparejado | 1,00 | top‑k 50 → top‑p 0,95, sin TALON. Es un control de esta campaña, no un default universal de Phi. |
| Top‑H | 1,00 | `TopHLogitsWarper(top_h=0.40)` de [Transformers 5.16.1](https://github.com/huggingface/transformers/blob/v5.16.1/src/transformers/generation/logits_process.py), con su límite interno de 100; sin top‑k/top‑p externos. |
| Min‑k | 1,00 | Clase de autores con [fallback τ=3 del paper](https://arxiv.org/html/2604.11012), no el τ=2 del control histórico. |
| Min‑p, tres brazos | 1,00 | 0,05 / 0,10 / 0,20, independientes y sin filtros encadenados; 0,10 es el ancla publicada, los otros dos son sensibilidades. |
| VCM | 1,00 | α=0,10, ventana 128, prior BOS y **top‑p 0,90 sin top‑k** ([§4 y Tabla 8](https://arxiv.org/html/2606.22511v1)). Es la adaptación a Phi de las ecuaciones del paper; no réplica bit a bit del código del autor. |
| Presencia y repetición | 1,00 | Presencia 0,20 sobre tokens generados / repetición estándar 1,10 sobre el historial; luego cadena del baseline. Son controles declarados, no defaults universales. |

**Ficha.** Phi‑4‑mini‑instruct, pesos FP16 sin cuantizar y cómputo FP16, mismas diez preguntas GSM8K test y tres semillas (11, 14, 29), dos T4 en Kaggle, 330 generaciones y 110 sondas. Sin QAS, sin Colab. Se comprueban el número, orden y valores de los filtros realmente instalados antes de generar. La versión anterior con top‑k 20 queda como antecedente separado. Una diferencia entre ambas versiones no aísla top‑k por sí solo, porque también cambian recetas de rivales; no se imputa esa diferencia como efecto demostrado ni se revisa el canon mirando resultados.

**EN.** The author-confirmed TALON sampling backbone is **top-k 50 → top-p .95**, applied after the operator and external temperature. The exploratory k=20 setting must not become the default. For this campaign TALON uses external T=.85 and T=.88 only; baseline and rival arms use T=1.00. Use the reference recipes listed above, including bounded native Top-H, paper fallback for Min-k, and VCM with top-p .90 without top-k. The nonzero penalties and Min-p sensitivity settings are explicitly benchmark controls. Same unquantized FP16 checkpoint, ten prompts, three matched seeds and dual T4; preserve previous outputs separately and do not infer a pure top-k effect from simultaneous rival changes.
