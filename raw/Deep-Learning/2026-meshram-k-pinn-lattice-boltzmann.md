# Lattice-Boltzmann-Driven Physics-Informed Neural Networks for Droplet Wettability on Rough Surfaces

> Source: https://arxiv.org/abs/2604.03481
> Collected: 2026-05-31
> Published: 2026-04-03

**Authors:** Ganesh Sahadeo Meshram, Partha Pratim Chakrabarti, Suman Chakraborty

## Abstract

The paper introduces a Lattice-Boltzmann-driven kinetic physics-informed neural network (K-PINN) for modeling droplet behavior on structured surfaces. Unlike traditional PINNs based on macroscopic equations, this framework operates at the mesoscopic kinetic level by embedding the discrete Boltzmann-BGK equation. The K-PINN successfully models phenomena including contact pinning, anisotropic spreading, and capillary hysteresis across various surface morphologies. It maintains mass conservation within 1.5% and uses a U-Net-based encoder-decoder structure yielding 50-75% reduction in error compared to conventional networks, achieving L2 ~ 0.021-0.026, R2 ~ 0.999 relative to high-resolution Lattice-Boltzmann simulations. Training convergence is ensured via curriculum learning and adaptive two-phase optimization. Once trained, the K-PINN achieves over 10^4 evaluations per second for real-time prediction. This work establishes a new paradigm for fast, physically consistent modeling of multiphase flows on complex surfaces.
