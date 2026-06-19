---
title: HumanEgo: Zero-Shot Robot Learning from Minutes of Human Egocentric Videos
authors: Zhi Wang, Botao He, Kelin Yu, Seungjae Lee, Ruohan Gao, Furong Huang, Yiannis Aloimonos
venue: arXiv preprint, 2026
date: 2026-05-28
url: https://arxiv.org/abs/2605.24934
topics: World-Models, Robotics, Zero-Shot Learning, Human-to-Robot Transfer
---

## Abstract

Human egocentric video captures rich manipulation demonstrations without any robot hardware, yet transferring these skills to robots remains challenging due to the embodiment gap between human and robot in both visual appearance and kinematics. We present HumanEgo, a framework that bridges the embodiment gap by lifting each human demonstration to an entity-level representation of hand–object interaction, and training a flow matching policy with dense auxiliary objectives that amplify supervision from every trajectory. HumanEgo is robot-data-free, hardware-agnostic, data-efficient, and zero-shot human-to-robot transferable. With only 30 minutes of human videos per task, HumanEgo achieves 92.5% average success across four real-world tasks (75% with just 15 minutes), outperforms matched-time robot teleoperation by 41%, and robustly transfers zero-shot across novel robots, cameras, and environments.

## Key Points

- **Robot-data-free**: No robot teleoperation data needed — purely from human egocentric videos
- **Data-efficient**: 30 minutes per task → 92.5% success; 15 minutes → 75% success
- **Four-stage pipeline**: (1) Aria glasses collection → (2) Visual preprocessing (arm inpainting + virtual gripper rendering) → (3) Interaction-Centric Tokens (ICT) → (4) Flow matching policy with 3 auxiliary objectives
- **Embodiment gap bridging**: SAM2 + LaMa inpainting removes human arm; virtual gripper + object keypoints rendered into image
- **Interaction-Centric Tokens (ICT)**: Entity-level pose representation relative to other task entities
- **Flow matching policy**: Multi-modal bimanual action generation with dense auxiliary objectives
- **Zero-shot transfer**: Novel robots, cameras, environments without retraining
- **Outperforms**: 41% better than matched-time robot teleoperation (ACT)
- **Open source**: https://github.com/TX-Leo/HumanEgo

## Links

- PDF: [2026-05-28-humanego-arxiv-2605.24934.pdf](../raw/World-Models/2026-05-28-humanego-arxiv-2605.24934.pdf)
- arXiv: https://arxiv.org/abs/2605.24934
- Website: https://humanego-ai.github.io/
- Code: https://github.com/TX-Leo/HumanEgo
