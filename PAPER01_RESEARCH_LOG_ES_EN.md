# Paper 01 — Bitácora de investigación / Research log

## 2026-11-14 — Piloto ARC-AGI-2 en Colab / Colab ARC-AGI-2 pilot

### Castellano

- **Diseño congelado:** prueba de admisión en el split público de entrenamiento, 8 problemas y 9 entradas; dos semillas fijas (11 y 33) × tres brazos (baseline, `talon_mass_right`, `top_h_alpha_0p40`) = 54 generaciones. Qwen3.5-4B, misma revisión para los tres brazos, NF4 con doble cuantización, cómputo FP16, una T4; límite de 1024 tokens. Sin recalibrado. No es una medición en el split de evaluación.
- **Infraestructura y cronología:** en Paperspace se creó un proyecto, pero la GPU seleccionada exigía activar Gradient Pro; no se activó. Se migró a un cuaderno nuevo en Colab sin interrumpir otras sesiones. El autor disparó la ejecución. El 14 de noviembre a las 13:03 CET se verificó el archivo, se montó Drive y se creó la carpeta de ejecución. La instalación devolvió código 0 con una advertencia de incompatibilidad; la revisión fijada del modelo descargó sus 11 archivos. El proceso de inferencia terminó con código 1 al importar `AutoProcessor`.
- **Causa observada:** el entorno heredó `torchvision 0.29.1+cu130` (requiere `torch>=2.14.0`), incompatible con el `torch 2.11.0+cu128` congelado. El error raíz fue `RuntimeError: operator torchvision::nms does not exist`. El directorio de resultados solo contiene `ENV.json`: **0/54 generaciones**, sin veredicto científico ni comparación entre operadores.
- **Reparación acotada:** instalar `torchvision==0.26.0+cu128` desde el [índice oficial de PyTorch](https://download.pytorch.org/whl/cu128/torchvision/) sin reemplazar las dependencias congeladas y comprobar versión CUDA, registro de NMS e importación de `AutoProcessor` en un proceso limpio. La [matriz oficial](https://pytorch.org/get-started/previous-versions/) respalda el emparejamiento. Registrar un intento distinto y conservar intacto el anterior; no cambiar el modelo, operadores, semillas, entradas ni criterio de acierto. **Aún no se ha verificado la reparación en GPU.**
- **Custodia:** `INSTALL.log`, `EXECUTION.log`, `ENV.json`, protocolo y recibo del ZIP están en Drive privado. Esta nota omite enlaces e identificadores privados.

### English

- **Frozen design:** admission pilot on the public training split, 8 problems and 9 inputs; two fixed seeds (11 and 33) × three arms (baseline, `talon_mass_right`, `top_h_alpha_0p40`) = 54 generations. Qwen3.5-4B at one revision across arms, double-quantized NF4, FP16 compute, one T4, 1,024-token cap. No recalibration. This is not an evaluation-split measurement.
- **Infrastructure and chronology:** a Paperspace project was created, but the selected GPU required activating Gradient Pro; it was not activated. The run moved to a new Colab notebook without interrupting other sessions. The author started the run. At 13:03 CET on November 14, the input archive was verified, Drive was mounted, and the run folder was created. Package installation exited 0 with a compatibility warning; all 11 files for the pinned model revision were fetched. Inference exited 1 on the `AutoProcessor` import.
- **Observed cause:** Colab retained `torchvision 0.29.1+cu130` (requires `torch>=2.14.0`), incompatible with pinned `torch 2.11.0+cu128`. The root error was `RuntimeError: operator torchvision::nms does not exist`. The results directory contains only `ENV.json`: **0/54 generations**, no scientific outcome and no comparison between operators.
- **Bounded fix:** install `torchvision==0.26.0+cu128` from the [official PyTorch index](https://download.pytorch.org/whl/cu128/torchvision/) without replacing frozen dependencies, and check CUDA, NMS registration, and `AutoProcessor` import in a clean process. The [official compatibility table](https://pytorch.org/get-started/previous-versions/) supports the pairing. Record a separate attempt and preserve the original; do not change the model, operators, seeds, inputs, or scoring rule. **The fix has not yet been verified on GPU.**
- **Custody:** `INSTALL.log`, `EXECUTION.log`, `ENV.json`, the protocol, and the ZIP receipt remain in private Drive. Private links and identifiers are omitted here.

## 2026-11-14 — Reparación y arranque verificado / Repair and verified generation start

**Castellano.** El primer reintento instaló `torchvision 0.26.0+cu128` pero paró antes de inferencia: la comprobación previa detectó `torchaudio 2.11.0+cu130`, incompatible con el PyTorch congelado de CUDA 12.8. Ambos fallos se conservaron por separado en Drive. En un tercer intento, en la misma T4, se alinearon `torchvision 0.26.0+cu128` y `torchaudio 2.11.0+cu128` sin modificar PyTorch, el ZIP, la revisión de Qwen ni el protocolo. CUDA, NMS y `AutoProcessor` pasaron la comprobación. Se cargaron los pesos y se observaron **3/54 generaciones** al cierre de este checkpoint. No es un resultado terminal ni una comparación entre brazos. Una vez disponibles las 54 filas, se verificará la cobertura problema × entrada × semilla × brazo y se reportarán rescates y pérdidas locales de acierto exacto.

**English.** The first retry installed `torchvision 0.26.0+cu128` but stopped before inference: preflight exposed `torchaudio 2.11.0+cu130`, incompatible with the pinned CUDA 12.8 PyTorch. Both failed attempts were kept separately in Drive. In the third attempt, the same T4 used `torchvision 0.26.0+cu128` and `torchaudio 2.11.0+cu128`, with PyTorch, the input archive, Qwen revision, and protocol unchanged. CUDA, NMS, and `AutoProcessor` passed preflight. The weights loaded and **3/54 generations** had been observed at this checkpoint. This is neither a terminal result nor an arm comparison. Once all 54 rows are available, verify task × input × seed × arm coverage and report local exact-match rescues and losses.

## 2026-11-14 — Resultado terminal / Terminal result

**Castellano.** Piloto ejecutado en T4: **54/54** generaciones, 18 tríos completos; sello y SHA-256 de `ENV.json` y `ROWS.jsonl` verificados en lectura de vuelta. **0/18 aciertos exactos por brazo.** En TALON vs baseline y TALON vs Top-H: 0 victorias, 18 empates por fallo simultáneo, 0 derrotas, sin rescates. Solo baseline emitió una cuadrícula válida (también de forma correcta), pero sin acierto. TALON alcanzó una vez el tope de 1.024 tokens; los demás no. Los tiempos corresponden a generación sincronizada en esta T4, no a facturación ni a evidencia de aceleración. `92e50de0` concentra un contraste local de coste sin ganancia de acierto. El suelo de rendimiento impide inferir equivalencia o dominancia entre métodos. Próximo contraste propuesto: validar la representación de cuadrículas y medir por separado formato, forma y solución exacta en un nuevo piloto congelado. No usar el split de evaluación hasta que el instrumento produzca señal interpretable.

**English.** T4 pilot: **54/54** generations, 18 complete triplets; terminal seal and SHA-256 for `ENV.json` and `ROWS.jsonl` verified by read-back. **0/18 exact matches per arm.** TALON vs baseline and TALON vs Top-H each had 0 wins, 18 joint-failure ties, and 0 losses; no rescues. Baseline alone produced one valid, correctly shaped grid, but it was not an exact match. TALON hit the 1,024-token cap once; the other arms did not. Times reflect synchronized generation on this T4, not billable time or speedup evidence. `92e50de0` shows a local cost contrast with no accuracy benefit. This performance floor cannot establish equivalence or dominance. Proposed next contrast: validate the grid representation and measure format, shape, and exact solution separately in a newly frozen pilot. Keep the evaluation split untouched until the harness yields interpretable signal.

Orden de brazos / Arm order: **baseline / TALON Mass Right / Top-H (0.40)**. Segundos sumados y redondeados por celda / Generation seconds summed and rounded per cell.

| Problema / Task | n por brazo / per arm | Aciertos exactos / Exact | Cuadrículas válidas / Valid grids | Segundos / Seconds |
|---|---:|---|---|---|
| `e21a174a` | 4 | 0 / 0 / 0 | 1 / 0 / 0 | 59 / 44 / 43 |
| `92e50de0` | 2 | 0 / 0 / 0 | 0 / 0 / 0 | 88 / 194 / 166 |
| `e5790162` | 2 | 0 / 0 / 0 | 0 / 0 / 0 | 50 / 37 / 51 |
| `6d0aefbc` | 2 | 0 / 0 / 0 | 0 / 0 / 0 | 10 / 11 / 10 |
| `3d31c5b3` | 2 | 0 / 0 / 0 | 0 / 0 / 0 | 9 / 9 / 5 |
| `ed98d772` | 2 | 0 / 0 / 0 | 0 / 0 / 0 | 20 / 20 / 18 |
| `3618c87e` | 2 | 0 / 0 / 0 | 0 / 0 / 0 | 2 / 2 / 2 |
| `27a77e38` | 2 | 0 / 0 / 0 | 0 / 0 / 0 | 25 / 27 / 18 |
| **Total** | **18** | **0 / 0 / 0** | **1 / 0 / 0** | **262 / 344 / 313** |
