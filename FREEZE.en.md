# Freeze v1.0 — Prompt-local decoding jurisdictions on 4-bit Qwen

**Identifier:** `CFL-QWEN-GSM8K-10SEED-v1`. **Status:** design frozen before new outcomes; physical model admission, destination repository, and launch are pending at the time of freezing. This is neither the Qwen3.5‑4B pilot nor its extension. Do not reuse their outputs as rows in this campaign. No LLaMA, Gemma, Phi, RDS, P07, or TALON Mass Left is run in v1.0. [Original Spanish freeze](FREEZE.md) · [Shared machine-readable design](DESIGN.json).

## 1. Objective, unit, and panel

Identify where each method wins, ties, loses, or changes direction. **The scientific unit is the prompt**, with ten paired repetitions. The physical row key is `(dataset_revision, item_id, mode, seed, model_revision, quantization, arm, protocol)`. An overall score is a descriptive inventory, not an adjudication rule. A method can lose overall yet solve a local case no other method solves; do not discard that case.

Original GSM8K test set: [OpenAI, commit 3101c7d](https://github.com/openai/grade-school-math/blob/3101c7d5072418e28b9008a6636bde82a006892c/grade_school_math/data/test.jsonl), 1,319 rows, zero-based indices, SHA‑256 `3730d312f6e3440559ace48831e51066acaca737f6eabec99bccb9e4b3c39d14`. Use 60 new items. Exclude the union of the 32 pilot items and 24 items in the preceding contrast (the left extension shares those 24). Sort the remaining items by the SHA‑256 of UTF‑8 `CFL-QWEN-GSM8K-10SEED-v1:item:<id>` in ascending order, break ties by ID, and take the first 60. Selection does not inspect utility.

| Block | IDs in frozen order |
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

**Seeds:** `11, 22, 33, 44, 55, 66, 77, 88, 99, 110`. Use all ten for every planned prompt, arm, and mode. Reset the Python, NumPy, and Torch CPU/CUDA RNGs before each row; no cell consumes another cell's residual RNG state. A shared seed pairs the design but does not guarantee identical trajectories or effective random draws across different generation loops. Order by SHA‑256 of `CFL-QWEN-GSM8K-10SEED-v1:arm:<id>:<mode>:<seed>:<arm_id>`, breaking ties by arm ID.

## 2. Largest eligible Qwen and test-blind admission

Resources: the GPUs actually available on Kaggle, initially **two T4s**; one model sharded across them for the heavy tier. Do not assume a paid GPU, two model copies, CPU/disk offload, or available VRAM simply by adding advertised capacities. Choose the **largest nominal total-parameter tier** among official general-purpose Qwen candidates that run at 4-bit with the same intervention stack; follow the listed order within a tier. Record active MoE parameters separately: they do not represent memory for all resident experts. Official Qwen models in the 72B, 80B, 122B, 180B, and larger tiers are ineligible on two T4s: the lower bound for their 4-bit weights already exceeds the combined nominal memory, before KV state or compute overhead.

| Order | Official checkpoint | Fixed HF revision | Weight quantization |
|---|---|---|---|
| 1 | Qwen3.6‑35B‑A3B | `345d467b117d1fd5eda9b879a5988de9ae5f47a7` | NF4 with double quantization |
| 2 | Qwen3.5‑35B‑A3B‑GPTQ‑Int4 | `3af5ca2972faf6de1fd6f4efc4d8d319ca751e8b` | Qwen's official GPTQ Int4 |
| 3 | Qwen3.5‑35B‑A3B | `59d61f3ce65a6d9863b86d2e96597125219dc754` | NF4 |
| 4 | Qwen3‑32B | `9216db5781bf21249d130ec9da846c4624c16137` | NF4 |
| 5 | Qwen2.5‑32B‑Instruct | `5ede1c97bbab6ce5cda5812749b4c0bdf79b18dd` | NF4; eligible only if both modes are natively supported |
| 6 | Qwen3‑30B‑A3B | `ad44e777bcd18fa416d9da3bd8f70d33ebb85d39` | NF4 |
| 7 | Qwen3.8‑27B | `37561816e66b5b9153b1b64c10968c18c1e6f4a0` | NF4 |
| 8 | Qwen3.6‑27B | `8f33b98937c6031bb49e713dee3e8e185aafd26f` | NF4 |
| 9 | Qwen3.5‑27B‑GPTQ‑Int4 | `8f0c09f227ae570e79617c6d9172b59df9c16081` | Official GPTQ Int4 |

Revisions were pinned using official metadata. This is an **admission** order, not an observed quality ranking. If none passes, stop and amend the design before testing; do not fall back automatically to 4B. Primary references: [Qwen 35B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B), [official GPTQ Int4](https://huggingface.co/Qwen/Qwen3.5-35B-A3B-GPTQ-Int4), [Qwen 32B](https://huggingface.co/Qwen/Qwen3-32B), and [Qwen 27B](https://huggingface.co/Qwen/Qwen3.8-27B).

Admission: check **remote** temporary storage and load the fixed revision with a GPU-only device map. For NF4, use FP16 compute and double quantization. Accept GPTQ only with an Int4 backend that works on T4 and exposes logits to the same pipeline. Inventory effective precision by tensor family, including experts and projections: `load_in_4bit=True` is insufficient if block experts remain at 16 bits. Declared exceptions: embeddings, normalizations, and the output head if the official implementation does not quantize them. Use the first five **train** examples only as mechanical canaries and perform a length stress test up to the maximum panel input length plus 1,024 new tokens, without using test answers. Require both native modes, logit callbacks, the exact pipeline, finite outputs, TALON's contract, and at least 1 GiB of headroom per GPU at peak. Only compatibility, memory, storage, or resource limits may disqualify a candidate in favor of the next one; scores may not. Persist device map, precision, versions, canaries, exclusion reasons, and the admission receipt. Seal the executable recipe and dependencies in a launch manifest before generating test outputs. Starting point: Kaggle image `gcr.io/kaggle-private-byod/python@sha256:9a6bcfda6d03b2cd9aa347ee8c1bae62043328ed0f4afe9bda014e4f8bbf9435`, Transformers 5.16.1, and bitsandbytes 0.50.2 for NF4. Any technical adaptation is fixed before testing and does not vary by arm.

## 3. Modes, common protocol, and arms

- **Main:** `enable_thinking=False`, 60 prompts. **Inverse mini-panel:** `enable_thinking=True`, the five prompts of block 01 only. Same admitted arms, ten seeds, model, quantization, budget, and input wording. Do not rerun the main block 01. If the checkpoint does not natively support both modes, do not simulate one through a textual instruction.
- One sequence per cell, batch size 1, no beam search, **T=1**, at most **1,024 new tokens in both modes**, native EOS and cache. No repetition penalty, reranking, or tools. Zero-shot prefix: `Solve the math problem below. Show a concise calculation, then end with exactly one line of the form #### NUMBER.\n\n`, followed by the original problem. The template varies only with the native mode; persist its hash. If “Eagle” refers to [EAGLE](https://arxiv.org/abs/2401.15077), do not enable speculative acceleration, a draft, or an assistant model. If it means `eager`, do not override the attention backend; record the effective default.
- One baseline: no intervention, Top‑k 20 followed by Top‑p 0.95. Transport operators and DoLa share this **downstream** truncation. Truncation competitors **replace** that chain; do not stack Top‑k/Top‑p on them. Full/QAS pairs use the same downstream pipeline within each method. Between families, the comparison is between complete pipelines; within each pair it isolates qualification under the frozen contract.

| Fixed method | Without QAS | With QAS | Identity and parameters |
|---|---|---|---|
| Baseline | `baseline` | Identity, no additional generation | QAS on a null transformation leaves scores unchanged. Check identity before sharing the row; if it fails, stop rather than impute. |
| TALON Mass Right | `talon_mass_right` | `talon_mass_right_qas` | Runtime v1.2; strength 0.70, mass 0.92, internal T=1, right side, top‑1 preservation. |
| TALON Soft Left | `talon_soft_left_v064` | `talon_soft_left_v064_qas` | Soft v0.6.4; hybrid-head 0.10 ∪ mass 0.90, strength 0.45, internal T=0.8, weights 0.65/1.20, minimum 3, tanh, median/MAD ε=10⁻⁶, KL 0.015, projection blend 0.35, `side_policy=left`. |
| TALM Soft Left | `talm_mass_left_soft` | `talm_mass_left_soft_qas` | Runtime v1.2; strength 0.70, mass 0.025, left/right weights 0.80/0.20, boosts 0.08/0.28, caps 8/4096, internal T=1, no mandatory projection. |
| Min‑p | `min_p_0p10` | `min_p_0p10_qas` | Min‑p 0.10, keeps at least one token, native implementation in the frozen stack. |
| Min‑k | `min_k_tau_2` | `min_k_tau_2_qas` | τ=2, default in the authors' class used in the previous contrast; distinct from the paper's τ=3 protocol. [Pinned source](https://github.com/YecanLee/Mink/blob/39fa4cb070212c04eb32897898e383b42da530ae/llm_mink.py). |
| Top‑H | `top_h_alpha_0p40` | `top_h_alpha_0p40_qas` | α=0.40, top‑N=100; same entropy criterion, with the full prefix retained when no crossing occurs. [Authors' source](https://github.com/ErfanBaghaei/Top-H-Decoding/blob/8b94d62b238ed62793627f4a2556d90188560854/logit_processor.py). |
| TFS | `tfs_z_0p95` | `tfs_z_0p95_qas` | z=0.95, the laboratory's previously fixed curvature variant, minimum one token. |
| Conditional DoLa | `dola_low` | `dola_low_qas` | Dynamic low-layer contrast on the same Qwen, with qualified support only if both canaries pass. Otherwise mark both cells `NOT_ADMITTED`; do not substitute LLaMA for Qwen or suppress the failure. |

**First-party code identity:** runtime v1.2 `f41318f04188e88d7a28bcdeff19ca4d388370cb68165fd81285f0f600d9f78c`; historical Soft core `4238fb56642e3d173e6108022e5c5f4f29519d680ccbe163ecff696a68a041b4`. For both TALON branches, check the actual argmax before and after the warper in the tensor consumed by the sampler. The prospective wrapper preserves scores when the argmax already agrees. After a crossing, raise the original token to the next representable value above the maximum competitor in the effective dtype. If the value is not finite or the contract fails, mark the cell nonconforming. Do not transfer the historical Soft Right result to Soft Left. TALM records crossings without correcting them.

**DoLa did evaluate GSM8K:** [paper, Appendix B, Table 5](https://arxiv.org/html/2309.03883v2) and [authors' script](https://github.com/voidism/DoLa/blob/main/gsm8k_eval.py). The benchmark matches; checkpoint, precision, prompt, and protocol do not. Published results are contextual references, not paired rows. The community implementation pinned at `af6cdc351e7e0bd28a86ce32aac461494a09a9c1` rejected the preceding stateful Qwen3.5. Attempt it on the admitted model without disabling safeguards for convenience. The QAS canary must access **both** mature and contrasted logits from the same step; do not reconstruct them from text.

## 4. Universal QAS: one question, different types of intervention

QAS qualifies **where to apply an action**; it does not select the arm. Given the same finite input z and raw counterfactual u: (a) for finite edits use energy `|u_i-z_i|*sqrt(max(p_i*(1-p_i),1e-8))`; (b) for intrinsic exclusions `u_i=-∞`, use mask energy `p_i`, with p=softmax(z). Do not subtract infinities. If both channels are nonzero, normalize each by its sum and average them with weights 1/2 and 1/2. If only one is nonzero, use it; if neither is nonzero, return z.

Take the union of the original top‑1, a 0.95 mass prefix within baseline top‑256, and a 0.90 energy prefix within top‑512, with a 64-token minimum per list when candidates are available and a 1,024-token union cap. Break ties by token ID. Measure retention against the full vocabulary, not just the candidate list. Copy u on the qualified support and preserve z outside it. For a truncator, this means **applying its exclusions only within the qualified region**; tokens initially finite that the full truncator would have removed can remain eligible. It does not reopen tokens forbidden in z, invent a finite delta for an exclusion, or reproduce the original unmodified truncator. Use the same final TALON contract in both support modes; do not impose it on TALM. Preserve exact mechanical ties. This extension of QAS to exclusions is prospective and distinct from the earlier finite-delta-only implementation.

## 5. Z‑Explorer at the extremes, not in place of a router

Include **black-swan candidate search in the probability tails** as a cross-cutting probe. Frozen experimental protocol: at prefill and offsets 8/32 along each seed's baseline continuation when available, compare arms on the **same prefix**. Define the two regions on baseline logits **before any warper**, ordering finite tokens by log probability and ID. From each extreme take the shortest prefix reaching 0.01 mass or exhausting 512 tokens; assign overlaps to the low end first and deduplicate. Retain boundaries and actual mass covered; a single token may suffice at the high end. Within each region record mass gains/losses, entries/exits from support, and rank shifts relative to baseline **after** each sampling pipeline. Persist the first eight per sign by absolute shift, breaking ties by token ID, together with total masses. Reuse a shared prefill observation across the ten seeds without counting it ten times as independent evidence. An extreme finding is a black-swan **candidate**, not proof of semantic value. Link it to local and exclusive wins afterwards without using it to select an arm. This probe does not sample or receive a fictitious score. Any future generative Z arm would need both full and QAS modes and its own freeze. Do not define the other Z‑Explorer variant by analogy.

## 6. Evaluation and five-prompt checkpoints on Kaggle

- **Adjudication:** exact Decimal equality with official gold for the last visible-answer line when it has the form `#### NUMBER` and is the only valid marker. Independent sensitivity: the last number of the visible answer. Do not count thinking traces as the answer; persist text/tokens and split segments using the native protocol. Record absent/multiple markers, no visible answer, cap hits, exceptions, crossings, OOM, and non-admission. Do not impute an infrastructure failure as an incorrect answer.
- **Local first:** table by prompt and seed, method pair A/B, W/T/L, response, mass/support, timing, and first divergence. Across the ten seeds, A observationally dominates B with at least one win, no losses, and all ten pairs available. Both a win and a loss within the same prompt is MIXED. Keep all-tie and `NOT_ESTIMABLE` separate. Report seed-level exclusivity when exactly one arm in the admitted and complete set solves the case, and prompt-level recurrence from zero to ten. Name the comparator set: a non-admitted DoLa is not a loss. Separate rescues outside Mass Right's envelope from losses; one seed does not establish universal jurisdiction. Any aggregates retain prompt grouping and do not govern promotion.
- **Compute:** 15 mandatory arms × 60 × 10 = **9,000** main generations; the inverse mini-panel adds 750. DoLa adds 1,200 + 100 if admitted. Total **9,750** without DoLa, **11,050** with it. The baseline/QAS identity and Z replays are not new generations. Measure wall time, time to first distribution, ms/token, GPU, and memory. Do not promise completion within a single quota window; estimate from canaries, use available quotas, and retain all ten seeds on resume. Parallelize by block or sub-batch where account and memory permit, without over-allocating or assuming two concurrent jobs.
- **Persistent state every five prompts:** a confirmed Kaggle checkpoint is a **private terminal notebook-version output** or a **derived private dataset version** with a manifest, not merely `/kaggle/working` within a live job. Close a checkpoint every five complete prompts (15×5×10 mandatory cells, plus DoLa if admitted) and separately for the thinking mini-panel. If GPU time requires subdivision, preserve each sub-batch output and close the checkpoint only when the block is complete. Do not sacrifice seeds or rerun an identical job merely because a process was lost.
- **Resume:** retain completed and adverse partial outputs, keys, configuration, provider terminal status, and row/file hashes. Write each cell atomically to staging and persist a version at block close. Resume from the confirmed version manifest; skip only completed keys from the same freeze, and reuse the exact seed. A repair retains the earlier attempt and its cause. Do not change candidates, budgets, rules, seeds, or cases in response to a checkpoint's scores. A compatibility failure before any test execution permits an amendment; an adverse result does not.
- **Evaluate every five:** preserve prompt×seed CSVs, W/T/L, exclusive wins, and adverse examples within the checkpoint. Interpret a completed block without waiting for all twelve and without turning it into a tuning decision. Deliver a prompt-level consolidation, indexes, logs, QAS contrasts, and the Z‑Explorer map at completion. Use private Kaggle custody and then the user-authorized destination. Never store large weights or caches on the local PC.

## 7. Continuation

GSM8K is the first external panel. Do not report 60/1,319 as the complete GSM8K test, or compare scores from different papers as if paired. A subsequent reasoning option is **MATH‑500**, with its own freeze and evaluator. **IFEval** is a complementary instruction-following option; do not mix criteria. Gemma 4 and Phi‑4 follow Qwen as distinct phases, not DoLa fallbacks or already-launched extensions. This freeze does not authorize branch redefinition or adding RDS.
