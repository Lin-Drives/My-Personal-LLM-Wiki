# A QPINN Framework with Quantum Trainable Embeddings for the Lid-Driven Cavity Problem

> Source: https://arxiv.org/abs/2605.13892
> Collected: 2026-05-31
> Published: 2026-05-12

**Authors:** Nahid Binandeh Dehaghani, Ban Q. Tran, Susan Mengel, Rafal Wisniewski, A. Pedro Aguiar

## Abstract

The steady incompressible Navier-Stokes equations pose significant computational challenges due to their nonlinear convective terms and pressure-velocity coupling. The paper proposes a quantum physics-informed neural network (QPINN) with a quantum neural network (QNN)-based trainable embedding for the lid-driven cavity problem. The QNN learns data-adaptive quantum feature maps that encode spatial coordinates before processing by a variational quantum circuit with a physics-informed loss. Numerical experiments show the proposed model exhibits stable training behavior and competitive solution accuracy compared to classical PINNs and hybrid quantum models using classical embeddings, while using significantly fewer trainable parameters. The findings indicate embedding design plays an important role in quantum-assisted PDE solvers.
