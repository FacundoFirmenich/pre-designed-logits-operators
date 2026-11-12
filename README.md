# Pre-designed Logits Operators

[Español](#español) · [English](#english)

## Español

Investigación de operadores de inferencia **white-box, pre-softmax y prediseñados**. TALM y TALON redistribuyen masa de probabilidad; TALON preserva top‑1 y TALM permite cruces locales. El objetivo es identificar **jurisdicciones por prompt**, no declarar un ganador global.

- [Freeze completo en español](FREEZE.md) · [Versión en inglés](FREEZE.en.md)
- [Manifiesto común](DESIGN.json) · [SHA‑256 del freeze original](SHA256SUMS.txt)

**Primer protocolo:** GSM8K, Qwen 4-bit, 60 prompts nuevos, diez semillas fijas por prompt, pares con/sin QAS para operadores propios y ajenos, búsqueda de colas con Z‑Explorer y mini panel inverso de thinking en cinco prompts. Checkpoint y evaluación cada cinco prompts. DoLa se admite únicamente en el mismo Qwen si su mecanismo es compatible. El freeze es un diseño: no contiene resultados de esta campaña.

**Convención bilingüe.** Documentación, notas de ejecución, checkpoints e interpretación se publicarán en español e inglés. IDs, semillas, código, métricas, datos crudos y hashes tienen una sola identidad compartida. La traducción no abre un nuevo experimento ni cambia el diseño.

## English

Research on **white-box, pre-softmax, pre-designed** inference operators. TALM and TALON redistribute probability mass; TALON preserves top‑1, while TALM allows local crossings. The objective is to identify **prompt-local jurisdictions**, not declare a global winner.

- [Full freeze in English](FREEZE.en.md) · [Spanish original](FREEZE.md)
- [Shared design manifest](DESIGN.json) · [Original freeze SHA‑256 sums](SHA256SUMS.txt)

**First protocol:** GSM8K, 4-bit Qwen, 60 new prompts, ten fixed seeds per prompt, with/without QAS pairs for first-party operators and external competitors, Z‑Explorer tail search, and a five-prompt inverse thinking panel. Checkpoint and evaluate every five prompts. Admit DoLa only if its mechanism works on the same Qwen. The freeze is a design: it contains no results from this campaign.

**Bilingual convention.** Publish documentation, run notes, checkpoint reports, and interpretation in Spanish and English. IDs, seeds, code, metrics, raw data, and hashes have one shared identity. Translation does not create a new experiment or change its design.
