# V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning

> Source: https://arxiv.org/abs/2506.09985
> Collected: 2026-05-31
> Published: 2025-06-11 (CVPR 2025)

**Authors:** Mido Assran, Adrien Bardes, David Fan, Quentin Garrido, Russell Howes, Mojtaba Komeili, Matthew Muckley, Ammar Rizvi, Claire Roberts, Koustuv Sinha, Artem Zholus, Sergio Arnaud, Abha Gejji, Ada Martin, Francois Robert Hogan, Daniel Dugas, Piotr Bojanowski, Vasil Khalidov, Patrick Labatut, Francisco Massa, Marc Szafraniec, Kapil Krishnakumar, Yong Li, Xiaodong Ma, Sarath Chandar, Franziska Meier, Yann LeCun, Michael Rabbat, Nicolas Ballas

## Abstract

The study proposes a self-supervised approach combining internet video with minimal interaction data. The model first pretrains a V-JEPA 2 architecture on over 1 million hours of internet video, achieving 77.3% top-1 accuracy on Something-Something v2 and state-of-the-art performance on human action anticipation (39.7 recall-at-5) on Epic-Kitchens-100. After alignment with an LLM, it achieves leading results on multiple video QA tasks at 8B parameter scale. For robot planning, the V-JEPA 2-AC variant is post-trained on less than 62 hours of unlabeled robot videos from the Droid dataset, then deployed zero-shot to perform pick-and-place tasks without collecting any data from the target robot environments. This provides empirical evidence for LeCun's JEPA vision — pure visual self-supervised learning can support physical robot planning without task-specific training, reward functions, or environment-specific data.
