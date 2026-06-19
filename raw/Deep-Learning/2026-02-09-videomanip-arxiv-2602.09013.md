---
title: Dexterous Manipulation Policies from RGB Human Videos via 3D Hand-Object Trajectory Reconstruction
authors: Hongyi Chen, Tony Dong, Tiancheng Wu, Liquan Wang, Yash Jangir, Yaru Niu, Yufei Ye, Homanga Bharadhwaj, Zackory Erickson, Jeffrey Ichnowski
venue: arXiv preprint, 2026
date: 2026-02-09
url: https://arxiv.org/abs/2602.09013
topics: Deep-Learning, Robotics, Dexterous Manipulation, RGB Video, Hand-Object Reconstruction
---

## Abstract

Multi-finger robotic hand manipulation and grasping are challenging due to the high-dimensional action space and the difficulty of acquiring large-scale training data. Existing approaches largely rely on human teleoperation with wearable devices or specialized sensing equipment to capture hand-object interactions, which limits scalability. We propose VideoManip, a device-free framework that learns dexterous manipulation directly from RGB human videos. Leveraging recent advances in computer vision, VideoManip reconstructs explicit 3D robot-object trajectories from monocular videos by estimating human hand poses, object meshes, and retargets the reconstructed human motions to robotic hands for manipulation learning. To make the reconstructed robot data suitable for dexterous manipulation training, we introduce hand-object contact optimization with interaction-centric grasp modeling, as well as a demonstration synthesis strategy that generates diverse training trajectories from a single video, enabling generalizable policy learning without additional robot demonstrations. In simulation, the learned grasping model achieves a 70.25% success rate across 20 diverse objects using the Inspire Hand. In the real world, manipulation policies trained from RGB videos achieve an average 62.86% success rate across seven tasks using the LEAP Hand, outperforming retargeting-based methods by 15.87%.

## Key Points

- **Device-free**: No wearable sensors or specialized equipment — only RGB human videos
- **3D trajectory reconstruction**: Hand pose estimation + object mesh reconstruction + motion retargeting to robotic hands
- **Hand-object contact optimization**: Interaction-centric grasp modeling for dexterous manipulation suitability
- **Demonstration synthesis**: Generate diverse training trajectories from a single video
- **Simulation results**: 70.25% grasping success across 20 objects (Inspire Hand)
- **Real-world results**: 62.86% success across 7 tasks (LEAP Hand), +15.87% vs retargeting baselines
- **No robot demonstrations needed**: Policy learning purely from reconstructed human video data

## Links

- PDF: [2026-02-09-videomanip-arxiv-2602.09013.pdf](../raw/Deep-Learning/2026-02-09-videomanip-arxiv-2602.09013.pdf)
- arXiv: https://arxiv.org/abs/2602.09013
