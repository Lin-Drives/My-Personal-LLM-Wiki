---
title: EgoVerse: An Egocentric Human Dataset for Robot Learning from Around the World
authors: Ryan Punamiya, Simar Kareer, Zeyi Liu, Josh Citron, Ri-Zhao Qiu, Xiongyi Cai, Alexey Gavryushin, Jiaqi Chen, Davide Liconti, Lawrence Y. Zhu, Patcharapong Aphiwetsa, Baoyu Li, Aniketh Cheluva, Pranav Kuppili, Yangcen Liu, Dhruv Patel, Aidan Gao, Hye-Young Chung, Ryan Co, Renee Zbizika, Jeff Liu, Xiaomeng Xu, Haoyu Xiong, Geng Chen, Sebastiano Oliani, Chenyu Yang, Xi Wang, James Fort, Richard Newcombe, Josh Gao, Jason Chong, Garrett Matsuda, Aseem Doriwala, Marc Pollefeys, Robert Katzschmann, Xiaolong Wang, Shuran Song, Judy Hoffman, Danfei Xu
venue: arXiv preprint, 2026
date: 2026-04-08
url: https://arxiv.org/abs/2604.07607
topics: World-Models, Robotics, Egocentric Data, Human-to-Robot Transfer, Dataset
---

## Abstract

Robot learning increasingly depends on large and diverse data, yet robot data collection remains expensive and difficult to scale. Egocentric human data offer a promising alternative by capturing rich manipulation behavior across everyday environments. However, existing human datasets are often limited in scope, difficult to extend, and fragmented across institutions. We introduce EgoVerse, a collaborative platform for human data-driven robot learning that unifies data collection, processing, and access under a shared framework, enabling contributions from individual researchers, academic labs, and industry partners. The current release includes 1,362 hours (80k episodes) of human demonstrations spanning 1,965 tasks, 240 scenes, and 2,087 unique demonstrators, with standardized formats, manipulation-relevant annotations, and tooling for downstream learning. Beyond the dataset, we conduct a large-scale study of human-to-robot transfer with experiments replicated across multiple labs, tasks, and robot embodiments under shared protocols. We find that policy performance generally improves with increased human data, but that effective scaling depends on alignment between human data and robot learning objectives. Together, the dataset, platform, and study establish a foundation for reproducible progress in human data-driven robot learning. Videos and additional information can be found at https://egoverse.ai/.

## Key Points

- **EgoVerse-A** (academic component): 受控协议下标准化采集，支持可复现研究
- **EgoVerse-I** (industry component): 工业伙伴在野外采集，强调规模和多样性
- **EgoDB**: 统一数据管理访问系统，支持持续数据注入（"living dataset"）
- **规模**: 1,362 hours / 80k episodes / 1,965 tasks / 240 scenes / 2,087 demonstrators
- **人类到机器人迁移**: 跨多个实验室、任务、机器人 embodiment 的联合训练实验
- **核心发现**: 策略性能随人类数据量增加而提升，但有效缩放取决于数据与机器人学习目标的对齐
- **手机采集管线**: 支持轻量级 egocentric 录制，降低贡献门槛

## Links

- PDF: [2026-04-08-egoverse-egocentric-human-dataset.pdf](2026-04-08-egoverse-egocentric-human-dataset.pdf)
- Website: https://egoverse.ai/
- Related: 
  - [EgoMimic](https://arxiv.org/abs/2410.24221)
  - [EgoBridge](https://arxiv.org/abs/2509.19626)
  - [EgoScale](https://arxiv.org/abs/2602.16710)
  - [EMMA](https://arxiv.org/abs/2509.04443)
  - [EgoVLA](https://arxiv.org/abs/2507.12440)
  - [EgoZero](https://arxiv.org/abs/2505.20290)
