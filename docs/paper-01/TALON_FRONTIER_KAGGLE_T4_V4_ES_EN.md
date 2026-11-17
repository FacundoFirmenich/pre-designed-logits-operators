# TALON · alternativas de hardware en Kaggle / Kaggle hardware successor

**ES.** Kaggle [retiró P100 el 15 de septiembre de 2026](https://www.kaggle.com/product-announcements/735239). La [CLI oficial](https://github.com/Kaggle/kaggle-cli/blob/main/skills/references/kernels.md) identifica que pedir `NvidiaTeslaP100` puede ejecutar en el acelerador por defecto, no en P100. No se envió el cuaderno V3 ni se gastó GPU en esta gestión.

V4 es un candidato explícito para **dos T4** (CUDA 12.8), validado localmente y por defecto sin generación. Conserva los diez problemas y tres semillas, el mismo Phi, los once brazos, NF4/FP4 con cómputo FP16, asignación emparejada y órdenes de formatos opuestos. Plan: 660 generaciones y 220 sondas; techo operativo de una hora. El nuevo enclave cambia el hardware y su wheel CUDA: la comparación interna sigue emparejada, pero latencias T4 no se combinan con P100. Sin ejecución ni resultados nuevos.

**EN.** Kaggle retired P100 on September 15, 2026. The official CLI documents replacement of retired accelerators with the default GPU. V4 explicitly targets two T4s, CUDA 12.8, and is validated locally in no-generation mode. All scientific design factors are unchanged; keep hardware-specific latency strata separate. No job was submitted.

**V4 SHA‑256:** `9c8f040b759e32b2431f812b3d41600604f9629f12c42ac140cf36c0d8f12984`.
