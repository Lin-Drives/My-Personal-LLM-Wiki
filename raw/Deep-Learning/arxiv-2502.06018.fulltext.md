# arXiv:2502.06018 — PDF 原文文本提取

- Source: https://arxiv.org/abs/2502.06018
- Local PDF: `2025-02-09-kolmogorov-arnold-fourier-networks-arxiv-2502.06018.pdf` (local only)
- PDF SHA-256: `ff9a12aa9250abd07df98503a1827e81dda204d20ee5a20a60aa6dbb6b7b0a39`
- Converted at: 2026-10-06T23:51:12.002106+00:00
- Extractor: pypdf/6.10.0
- Pages: 26
- Pages without extractable text: none

> 逐页提取 PDF 文本，未使用模型改写或翻译，未进行内容核验。保留页码；多栏阅读顺序、公式、表格和图片可能不能准确还原。无文字页需要另行 OCR，不能视为完整文本覆盖。基础 ID 的具体版本尚未解析，以 PDF 哈希标识本次原文件。

## PDF page 1

```text
Journal of Machine Learning Research xx (2026) 1-26 Submitted x/xx; Revised x/xx; Published x/xx
Kolmogorov-Arnold Fourier Networks
Jusheng Zhangzhangjusheng19981128@gmail.com
Sun Yat-sen University
Yijia Fanf anyj28@mail2.sysu.edu.cn
Sun Yat-sen University
Kaitong Caicaikt3@mail2.sysu.edu.cn
Sun Yat-sen University
Keze Wang∗ w angkz@mail.sysu.edu.cn
Sun Yat-sen University
Wenhao Wang∗ w angwenhao@v astilab.com
Vast Intelligence Lab
Editor:-
Abstract
Although Kolmogorov-Arnold-based interpretable networks (KANs) possess strong theoreti-
cal expressiveness, they suffer from severe parameter explosion and limited ability to capture
high-frequency features in high-dimensional tasks. To address these issues, we propose
the Kolmogorov-Arnold Fourier Network(KAF), which fundamentally redefines the KAN
paradigm through spectral reparameterization. Our key contributions include:(1)propos-
ing a fundamental basis transformation from the local, grid-based B-spline representation to
a global, adaptive spectral representation. This shift changes the network’s inductive bias,
reducing parameter complexity fromO(G)to O(1)while preserving expressiveness;(2)intro-
ducing trainable Random Fourier Features (RFF) initialized via a spectral alignment strategy,
which allows the model to break the smoothness limitation of fixed kernels and accurately
capture high-frequency components; and(3)implementing an adaptive hybrid GELU-
Fourier activation mechanism that progressively enhances frequency representation during
training. Comprehensive experiments demonstrate the superiority of KAF across computer
vision (CV), natural language processing (NLP), audio, and partial differential equation
(PDE) solving tasks, achieving state-of-the-art performance with improved efficiency. The
code is available athttps://github.com/kolmogorovArnoldFourierNetwork/KAF.
Keywords:Kolmogorov-Arnold networks, random Fourier features, spectral neural
networks, function approximation, neural architecture design
1 Introduction
The interpretability of deep neural networks (Howard et al., 2017; Han et al., 2016) has long
been one of the core challenges in the field of machine learning. The Kolmogorov-Arnold (Liu
et al., 2024; Kolmogorov, 1933) theorem states that any continuous multivariate function can
be represented through a combination of univariate functions (Mhaskar, 1996; Barron, 1993).
This theory provides significant inspiration for the design of interpretable neural network
∗. Corresponding authors.
©2026 Jusheng Zhang, Yijia Fan, Kaitong Cai, Keze Wang, and Wenhao Wang.
License: CC-BY 4.0, see https://creativecommons.org/licenses/by/4.0/. Attribution requirements are provided at
http://jmlr.org/papers/vxx/21-0000.html.
arXiv:2502.06018v3  [cs.LG]  24 May 2026
```

## PDF page 2

```text
Kolmogorov-Arnold Fourier Networks
architectures. Based on this theory, Kolmogorov-Arnold Networks (KAN) (Liu et al., 2024;
Schmidt-Hieber, 2021) have been proposed, which replace the fixed activation functions in
traditional multilayer perceptrons (MLPs (Rumelhart et al., 1986)) with learnable B-spline
(De Boor, 1972) basis functions, theoretically demonstrating strong expressive potential and
flexibility. By introducing trainable nonlinear activation functions, KAN enables the network
to dynamically adjust the shape of the activation functions according to the characteristics
of the data, thereby enhancing the adaptability and performance of the model.
However, despite the significant theoretical advantages of KAN, its practical application
faces two fundamental issues that severely limit its generalization and adoption in high-
dimensional tasks.(1) Inefficient parameter utilization.The dual-matrix architecture
of KAN, namely the activation function matrix and the B-spline coefficient matrix, leads to
a rapid increase in the number of parameters. Compared to traditional MLPs, where the
parameter count scales with input× output plus bias, KAN’s parameter count grows several
times larger. This makes it challenging to apply KAN to high-dimensional tasks such as
computer vision. The explosion in parameters (Rahaman et al., 2019; Mhaskar, 1996; Barron,
1993) not only increases storage and computational costs, but also significantly reduces the
efficiency of both training and inference (Tan and Le, 2020, 2021).(2) Limited spectral
representation.The B-spline basis functions employed by KAN (De Boor, 1972; Hung
et al., 2025; Chen et al., 2015) exhibit inherent spectral limitations when performing function
approximation in high-dimensional spaces. Their smoothness makes it difficult to accurately
capture high-frequency components, leading to suboptimal performance on data with rich
spectral features, such as natural images or audio waveforms. This limitation adversely
affects model performance and stability in practical applications (Rahaman et al., 2019).
Together, these limitations create a paradox between theory and practice: although KAN
theoretically encompasses the functionality of MLPs, its inefficiency and spectral distortion
force practitioners to trade interpretability for scalability.
a b
h = W ( G E L U ( x ) ) + b h = W ( a     G E L U ( x ) + b     Φ ( x ) ) + C~
P r o j e c t i o n
M a t r i x
A c t i v a t i o n
F u n c t i o n
M L P ( G E L U )
P r o j e c t i o n
M a t r i x
R F F
S c a l e
P a r a m e t e r
A c t i v a t i o n
F u n c t i o n
K A F ( G E L U )
Figure 1: Comparison between a standard GELU-MLP
layer and the proposed GELU-KAF layer. KAF aug-
ments the GELU branch with trainable Random Fourier
Features (RFF) and learnable scaling parameters, en-
abling more flexible spectral feature transformations.
To address the aforementioned is-
sues, the key challenge is bal-
ancing the inherent trade-off be-
tween model interpretability and
parameter efficiency, which has
long plagued traditional neural
networks. This paper makes
an attempt to fundamentally
redefine the traditional KAN
paradigm (Bracewell, 1986). Specif-
ically, this paper introduces an
innovative neural network ar-
chitecture,Kolmogorov-Arnold-
FourierNetworks(KAF),which
employs Fourier domain reparame-
terization and dynamic activation evolution, aiming to bridge the gap between interpretability
and parameter efficiency. Fig. 1 illustrates the difference between a standard GELU-MLP
layer and the proposed KAF layer.
Our main contributions include:
2
```

## PDF page 3

```text
Kolmogorov-Arnold Fourier Networks
• By leveraging the associative property of matrix multiplication, we merge the two large
matrices (W A and W B) of KAN, thereby reducing the parameter complexity from
O(din ×d out × (G + K + 3))to O(din ×d out), while preserving the expressive power of
the model. This approach not only effectively reduces the number of parameters but also
enhances the model’s scalability in high-dimensional tasks.
• We replace the traditional B-spline basis functions with trainable Random Fourier Features
(RFF) to eliminate the need for the spline coefficient matrix. An initialization strategy
based on the Central Limit Theorem (σ = 1.64) aligns the RFF spectrum with the prior
knowledge of natural signals, avoiding spectral leakage issues. This significantly enhances
the model’s spectral fidelity and expressive power in high-dimensional spaces.
• We design a hybrid GELU-Fourier activation function with learnable coefficients{a, b}.
During training, these coefficients are dynamically adjusted through gradient backprop-
agation, enabling an automatic transition from fixed activation functions to hybrid
Fourier-symbolic representations. This dynamic activation mechanism not only optimizes
the model’s learning trajectory but also ensures the stability and efficiency of the final
Fourier-driven inference mode.
2 Related Work
Multi-Layer Perceptrons and Current Challenges.The design and optimization of
deep learning (Touvron et al., 2021) models remain central to machine learning research.
Traditional MLPs (Rumelhart et al., 1986), among the earliest neural networks (Han et al.,
2016), offer simplicity and scalability, with rich theoretical foundations. While ResNet
(He et al., 2015b) and Transformer (Vaswani et al., 2023) models have shown remarkable
performance across various tasks, MLPs face challenges in theoretical interpretability and
practical bottlenecks. Traditional activation functions like ReLU (Nair and Hinton, 2010;
Glorot et al., 2011) and Sigmoid (Elfwing et al., 2017) often fail to adapt to complex data, and
despite their efficiency, MLPs struggle with high-frequency features and complex distributions.
Improving activation mechanisms and parameter efficiency has become crucial for enhancing
MLPs’ adaptability to high-dimensional data.
Kolmogorov-Arnold Networks and Scalability Issues.The Kolmogorov-Arnold (Han
et al., 2019) Theorem underpins networks for approximating continuous multivariable func-
tions. The pioneering KAN replaced fixed activations with B-spline (De Boor, 1972) functions
but faces challenges in high-dimensional applications due to parameter explosion and GPU
inefficiency. Recent improvements include KAN-Transformer, MLP-KAN with sparse pa-
rameters, and FAN (Dong et al., 2025) with Fourier activations, all seeking to balance
interpretability with scalability.
Enhancing Spectral Representation with KAF.To address high-frequency modeling
challenges, Random Fourier Features (RFF (Rahimi and Recht, 2007b)) enable spectral
domain mapping, with variants like Learnable RFF and SIREN enhancing expressiveness. Our
proposed KAF incorporates GELU and learnable Fourier features, with scale factor control
and variance initialization. This reduces parameters while improving spectral representation.
KAF maintains KAN’s interpretability while enhancing scalability and efficiency, showing
3
```

## PDF page 4

```text
Kolmogorov-Arnold Fourier Networks
superior performance in capturing high-frequency (Sitzmann et al., 2020) details across NLP,
vision, audio, and traditional machine learning tasks.
3 Methodology
This section presents the proposed Kolmogorov-Arnold Fourier Network (KAF). We first
review the Kolmogorov-Arnold theorem and the standard KAN formulation to identify the
sources of parameter growth and spectral limitations, and then introduce KAF, which replaces
spline-based edge functions with trainable Random Fourier Features and a GELU-Fourier
hybrid activation.
3.1 Kolmogorov-Arnold Theorem
The Kolmogorov-Arnold (Bracewell, 1986; Kolmogorov, 1933) theorem, proposed by Soviet
mathematicians Vladimir Arnold and Andrey Kolmogorov in the 1950s, states that any
continuous (Kidger and Lyons, 2020) multivariate functionf : [0, 1]d →R can be represented
as a superposition of univariate functions:
f(x 1, x2, . . . , xd) =
2d+1X
q=1
Φq


dX
p=1
ϕq,p(xp)

 ,(1)
whereΦ q : R→R and ϕq,p : [0, 1] →R are univariate continuous functions. This theorem
provides a theoretical foundation for dimensionality reduction in high-dimensional function
approximation.
In (Berner et al., 2022), the theorem suggests that high-dimensional functions can be captured
through low-dimensional (Rahaman et al., 2019) transformations, resembling the hierarchical
structure of neural networks. However, compared to traditional neural networks, the number
of parameters required by the Kolmogorov-Arnold theorem may lead to a more lengthy and
resource-consuming training process. Due to the non-smoothness of certain low-dimensional
functions and the difficulties in training optimization, this theorem has not been practically
applied in the field of neural networks for a long time.
3.2 Kolmogorov-Arnold Network (KAN)
Although the Kolmogorov-Arnold (Bracewell, 1986) theorem was proposed quite early, (KAN
(Liu et al., 2024)) is proposed according to this theorem, demonstrating that this structure
can, in a sense, serve as an alternative to traditional MLP models. In the KAN network,
each layer can be represented by the following formula:
f(x) = Φ◦x=
" dinX
i=1
ϕ1,i(xi)· · ·
dinX
i=1
ϕdout,i(xi)
#
,(2)
whereΦis a matrix of basis functions. This formula aligns with the form of the Kolmogorov-
Arnold theorem. However, in practical applications, they chose B-spline (Bach, 2016) basis
functions as the basis functionsϕq,p, and added an external activation functionSILU to
4
```

## PDF page 5

```text
Kolmogorov-Arnold Fourier Networks
guide the update of the KAN layer (Ramachandran et al., 2017; Elfwing et al., 2017). The
formula can be expressed as
ϕ(x) =w h silu(x) +w s spline(x),wherespline(x) =
X
i
ciBi(x).(3)
Among them,Φrepresents the basis function matrix, where B-spline basis functions and
the SiLU activation function were used. However, KAN suffers from excessive parameter
growth, with a parameter count ofdout ×d out × (G + K + 3) + dout, far exceeding MLP’s
din ×d out + dout, while also being computationally inefficient on GPUs and failing to capture
high-frequency components, limiting its practical applicability.
3.3 Kolmogorov-Arnold Fourier Network (KAF)
In the previous discussion, we pointed out that traditional networks based on the Kolmogorov-
Arnold theorem (KAN) often face multiple challenges in practical applications. To address
these issues, we propose an alternative approach,i.e., Kolmogorov-Arnold Fourier Network
(KAF). By replacing B-spline basis functions with Random Fourier Features (RFF (Fathony
et al., 2021; Tancik et al., 2020; Bracewell, 1986)), which are more efficient for GPU
acceleration, and introducing hybrid spectral correction for the activation functions, the
network retains the advantages of the Kolmogorov-Arnold theory while achieving training
efficiency and inference speed closer to that of MLPs (Rumelhart et al., 1986). This section
provides a detailed explanation of the overall architecture of the KAF network, the utilization
of Random Fourier Features within the network, the design and scaling principles of the
GELU-Fourier hybrid activation function, as well as the RFF weight initialization strategy
and the theoretical justification forσ= 1.64.
Overall Architecture.In the overall framework of KAF, we follow the core idea of the
Kolmogorov-Arnold theorem, which approximates high-dimensional target functions through
the composition of several low-dimensional learnable functions. Unlike the KAN network,
which directly utilizes B-spline basis functions, KAF employs Random Fourier Features
(RFF) in each layer to perform a nonlinear mapping of the input, and then uses linear
transformations to achieve the composition of the "outer function" and the "inner function."
Specifically, the core computational process of each KAF layer can be formulated as:
h(l) =W (l)
|{z}
outer function

a(l) ⊙GELU( ˜x(l)) +b (l) ⊙ ˜ϕ(˜x(l))| {z }
inner function composition

 +c (l),(4)
where: ˜x(l) = LayerNorm(x(l))is the normalized input at layerl; ˜ϕ(·)represents the nonlinear
mapping based on Random Fourier Features (RFF) (detailed in Section 3.3.2);a(l), b(l) ∈R n
are learnable scaling parameters, used to modulate the contributions of GELU activation and
RFF features, respectively;W(l) ∈R m×n is the linear transformation weight, andc(l) ∈R m
is the bias term.
By stacking multiple layers of the above transformation, the KAF network constructs an
efficient multi-layer approximation structure. Since RFF has excellent parallelism on GPUs,
this structure avoids the high computational burden of B-spline basis functions, significantly
5
```

## PDF page 6

```text
Kolmogorov-Arnold Fourier Networks
improving training and inference efficiency while maintaining strong function approximation
capabilities.
Random Fourier Features (RFF).Given an input spaceX ⊆R d, we define the Random
Fourier Feature (RFF (Tancik et al., 2020)) mapping as a learnable embedding from the
input space to a Reproducing Kernel Hilbert Space (RKHS (Werneburg, 2023; Aronszajn,
1950; Schölkopf and Smola, 2018)). For any input vectorx∈ X , the feature mapping is
formally defined as:
z(x;W, b) =
r
1
m

cos(⟨x, W⟩+b)⊕sin(⟨x, W⟩+b)

∈R 2m,(5)
where W∈R d×m and b∈R m. Here, ⟨·,·⟩ denotes the Euclidean inner product, and⊕
represents the vector concatenation operation. The frequency matrixW = [w1, . . . , wm]is
initialized according to an input-dimension-adaptive spectral distribution:wij ∼ N (0, σ2/d),
where σ2 represents the empirical variance of the input data. The phase shiftb is sampled
from a uniform distributionbi ∼ U [0, 2π], which ensures phase diversity, a crucial property for
capturing local features of signals. See Appendix A for more information on RFF convergence,
gradient calculation, and initialization strategies.
This mapping comes with the following theoretical guarantees:
•Translation Invariance: For anyx, y∈ X, asm→ ∞, we haveE[z(x) T z(y)]→e − ∥x−y∥2
2σ2 .
• Differentiability: The partial derivatives ∂z
∂W and ∂z
∂b have analytical expressions, enabling
end-to-end differentiation.
GELU-Fourier Hybrid Activation.Design Motivation: To balance low-frequency smooth-
ness and high-frequency representation capability, we propose a hybrid activation function:
H(x) =α⊙GELU(x)| {z }
Low-Frequency Basis
+β⊙Vψ(x)| {z }
High-Frequency Correction
(6)
where α, β∈R d are learnable channel-wise scaling factors,V∈R d×2k is the frequency-
domain projection matrix, and⊙represents element-wise multiplication.
Initialization Strategy of KAF.
α(0) ←1, β (0) ←ϵ1,(ϵ= 10 −2),V (0)
ij ∼ N(0,0.01)(7)
The dynamic property of this initialization manifests in the following way: At the early
stage of training, the small initialization of the high-frequency componentβ ensures that its
norm is much smaller than that of the low-frequency componentα, prioritizing the learning
of low-frequency features. As training progresses, the natural growth of weights allows the
norm of β to increase approximately proportionally to the training timet, thereby gradually
enhancing the representation of high-frequency features.
Implementation of the Kolmogorov-Arnold Architecture and RFF Initialization.
Theorem Definition: The Kolmogorov-Arnold representation theorem states that any contin-
uous function f∈C ([0, 1]d)can be expressed as a finite composition of univariate functions:
f(x) =
2dX
q=0
Φq


dX
p=1
ϕq,p(xp)

 ,(8)
6
```

## PDF page 7

```text
Kolmogorov-Arnold Fourier Networks
where ϕq,p : R→R are univariate nonlinear functions, andΦq : R→R are composition
functions.
Architecture Implementation: We modularize the neural network to efficiently approximate
this mapping, establishing the following correspondences:
ϕq,p(xp)7→GELU
 
w(q)
p xp +b (q)
p

| {z }
Low-Frequency Basis
+β⊤
q ψRFF(xp)| {z }
High-Frequency Basis
,
Φq(·)7→α ⊤
qLinear(·).
(9)
Here, ψRFF(xp) = [cos(ω1xp+θ1),sin (ω1xp+θ1), . . .]represents the Random Fourier Features
(RFF), andα q,β q ∈R k are learnable modulation parameters.
Spectral Complementarity Mechanism: (1) GELU Properties: The activation functionσ(wx +
b)provides a smooth gating effect in the low-frequency domain, satisfying E[σ(wx)] ∝
N (0, 1/
√
2). (2) RFF Enhancement: The use of mixed-frequency bases{cos(ωmx + θm)}M
m=1
expands spectral coverage. (3) Dynamic Balancing: The learnable parametersα,β enable
an adaptive trade-off:
˜ϕ(x) =α·GELU(x) +β·ψ RFF(x),(10)
where the initial values are set toα(0) = 1andβ (0) = 10−2 to ensure training stability.
RFF Initialization Strategy: To fully leverage spectral complementarity, we adopt a refined
initialization scheme:
• Frequency Matrix W: To ensure spectral balance and avoid bias towards low or high
frequencies, we initializeW using a scaled normal distribution (Glorot and Bengio, 2010;
He et al., 2015a):
ωij ∼ N
 
0, γp
din ·E[∥σ(x)∥ 2]
!
,(11)
This initialization is designed to align with the spectral distribution of the input data.
The denominator normalizes the standard deviation based on input dimensionalitydin
and the expected squared norm of the activation functionE[∥σ(x)∥2], ensuring a stable
variance propagation during training. For the GELU activation function, whyσ(x) = 1.64
will be proved later in Appendix B.
•Phase Shiftb: Uniformly sampled to cover a complete period,
bi ∼ U(0,2π).(12)
•Linear Projection Layer: Initialized using Xavier initialization,
V ij ∼ U

−
p
6/(din +d out),
p
6/(din +d out)

.(13)
Parameter and FLOPs Comparison.To evaluate the scale of parameters and computa-
tional overhead of KAF, we compare the number of parameters and floating-point operations
(FLOPs) for KAF, KAN, and MLP in a single layer setting.
Table 1 summarizes the parameter count and FLOPs for each model. KAN exhibits the
highest parameter count due to its recursive B-spline computations, while KAF, by leveraging
Random Fourier Features (RFF), achieves a balance between parameter efficiency and
spectral representation. MLP remains the simplest in terms of computation. For the detailed
derivation of these calculations, please refer to Appendix C.
7
```

## PDF page 8

```text
Kolmogorov-Arnold Fourier Networks
Table 1: Comparison of parameter count and FLOPs per layer for KAN, KAF, and MLP
models.
Model Param Count (Single Layer) FLOPs (Single Layer)
KAN dindout(G+K+ 3) +d out 7din + (dindout) [9K(G+ 1.5K) + 2G−2.5K+ 3]
KAF dinM+M+ 2d in +d indout +d out 4dinM+ 2d in + 2dindout + 5din
MLP dindout +d out 2dindout + 5dout
4 Experiments
The objective of this section is to evaluate the performance of mainstream models when
their MLP (Rumelhart et al., 1986) or KAN components are replaced with KAF. We
conduct experiments across a variety of tasks, including visual classification, natural language
processing, audio classification, traditional machine learning benchmarks, function fitting,
and differential equation solving. These evaluations use representative architectures such as
ResNet-18 (He et al., 2015b), DeiT (Touvron et al., 2021), MLP-Mixer (Tolstikhin et al.,
2021), and GPT-2 (Brown et al., 2020). Unless otherwise specified, all experiments use the
Adam optimizer (Kingma and Ba, 2014), with learning rates selected according to the task.
All experiments are conducted on an NVIDIA RTX 4090D GPU.
4.1 Comprehensive Evaluation Based on Kanbefair
Based on Kanbefair (Yu et al., 2024), we conduct a comprehensive evaluation of KAF on
vision (Dosovitskiy et al., 2021), NLP (Brown et al., 2020), audio, and machine learning tasks
to compare its performance with existing models. We selected MLP (with GELU activation),
KAN, FAN (Dong et al., 2025), and GPKAN (Yang and Wang, 2024) for experimentation.
Note that we use the original input by default in all experiments, leaving layernorm disabled.
Experimental setup.To account for differences in model convergence speeds, KAN was
trained for 100 epochs, while other models were trained for 40 epochs. During training,
the maximum test accuracy was recorded as the primary evaluation metric, focusing on
classification tasks across 8 vision datasets, 2 NLP datasets, 2 audio datasets, and 4 additional
machine learning datasets. For all models, hidden layer sizes were explored in the range
of 2, 4, 8, 16, 32, 64, 128, 256, 512, and 1024. For KAF, the key parameters included 9
grids, an activation expectation of 1.64, and GELU as the activation function. For KAN, the
number of B-spline grids was set to 3, 5, 10, or 20; B-spline degrees were configured as 2, 3,
or 5; and the B-spline range was [-1, 1], [-2, 2], or [-4, 4]. For MLP, we experimented with
both GELU (Hendrycks and Gimpel, 2016) and ReLU (Nair and Hinton, 2010; Glorot et al.,
2011) activations. FAN’s p_ratio was set to 0.25 to regulate the proportion of preserved
information during transformation, and GPKAN used GELU-based initialization for enhanced
convergence.
Experimental results.As shown in Fig. 2, we conduct a systematic comparison of KAF
and several baseline models (e.g., ResNet, ViT, MLP-Mixer) on vision datasets, including
MNIST (LeCun et al., 2002), EMNIST (Cohen et al., 2017), KMNIST (Clanuwat et al.,
2018), CIFAR 10/100 (Krizhevsky, 2009), and SVHN (Netzer et al., 2011). The results in
Fig. 2 demonstrate that KAF consistently achieves the highest accuracy under the same
parameter settings across different scales. Notably, on more challenging tasks such as CIFAR-
10 and SVHN, KAF exhibits significant accuracy improvements compared to other models.
8
```

## PDF page 9

```text
Kolmogorov-Arnold Fourier Networks
0 1 2 3 4
Number of Parameters 1e5
75
80
85
90
95Accuracy
MNIST
KAN
MLP
GPKAN
FAN
KAF
0 1 2 3 4
Number of Parameters 1e5
30
40
50
60
70
80Accuracy
EMNIST-Balanced
KAN
MLP
GPKAN
FAN
KAF
0 1 2 3 4
Number of Parameters 1e5
30
40
50
60
70
80
90Accuracy
EMNIST-Letters
KAN
MLP
GPKAN
FAN
KAF
0 1 2 3 4
Number of Parameters 1e5
70
75
80
85
90Accuracy
FMNIST
KAN
MLP
GPKAN
FAN
KAF
0 1 2 3 4
Number of Parameters 1e5
50
60
70
80
90Accuracy
KMNIST
KAN
MLP
GPKAN
FAN
KAF
0.0 0.5 1.0 1.5 2.0
Number of Parameters 1e6
30
35
40
45
50
55Accuracy
Cifar10
KAN
MLP
GPKAN
FAN
KAF
0.0 0.5 1.0 1.5 2.0
Number of Parameters 1e6
5
10
15
20
25
30Accuracy
Cifar100
KAN
MLP
GPKAN
FAN
KAF
0.0 0.5 1.0 1.5 2.0
Number of Parameters 1e6
40
50
60
70
80Accuracy
SVHN
KAN
MLP
GPKAN
FAN
KAF
Figure 2: Comparison of different models (KAN, MLP, GPKAN, FAN, and KAF) across
multiple datasets, including MNIST, EMNIST, FMNIST, KMNIST, CIFAR-10, CIFAR-100,
and SVHN. The results demonstrate that KAF consistently achieves higher accuracy while
using fewer parameters.
These results highlight KAF’s robustness in addressing high-dimensional data challenges. In
addition to vision tasks, we evaluate KAF on NLP, audio, and traditional machine learning
datasets. As shown in Fig. 3, KAF consistently achieves higher accuracy than the baseline
models under comparable parameter budgets, especially on datasets such as Bean, Rice, and
AG News. These results indicate that KAF is not only effective for visual recognition but
also generalizes to text, audio, and tabular learning tasks.
4.2 Experiments on Using KAF Components in Complex Vision Models
To comprehensively evaluate the performance of KAF in large-scale vision models after
replacing corresponding layers, we assess its impact on accuracy, computation time, and
generalization across various models. In this section, we conduct comparative experiments on
commonly used large-scale vision models, including ResNet-18, ViT-Tiny, and MLP-Mixer-
S/16, as well as the latest model incorporating KAN components, MLP_KAN (based on
DeiT). In each case, we replace the original KAN or MLP modules with KAF, KAN, MLP,
GPKAN, and FAN, respectively, to analyze their performance differences.
Experimental setup.The experiments utilize CIFAR-10, CIFAR-100 (Krizhevsky, 2009),
and ImageNet-1K for training and testing. ResNet-18 and MLP-Mixer-S/16 are trained for
100 epochs, while ViT-Tiny (He et al., 2024; Dosovitskiy et al., 2021) and MLP_KAN are
trained for 300 epochs. All other training hyperparameters follow the official recommended
settings for each model. Both KAF and MLP use GELU as the activation function; for
KAN, we set the grid size to 5 and the B-spline degree to 3; FAN’s p_ratio is fixed at 0.25;
9
```

## PDF page 10

```text
Kolmogorov-Arnold Fourier Networks
0 1 2 3
Number of Parameters 1e4
75.0
77.5
80.0
82.5
85.0
87.5
90.0
92.5Accuracy
Bean
KAN
GPKAN
MLP
FAN
KAF
0 1 2 3
Number of Parameters 1e4
60
65
70
75
80
85
90Accuracy
Rice
KAN
GPKAN
MLP
FAN
KAF
0 1 2 3
Number of Parameters 1e4
0
20
40
60
80Accuracy
Titanic
KAN
GPKAN
MLP
FAN
KAF
0 1 2 3
Number of Parameters 1e4
42
44
46
48
50
52
54
56Accuracy
Wine
KAN
GPKAN
MLP
FAN
KAF
0 1 2 3 4 5
Number of Parameters 1e5
4
5
6
7Accuracy
SpeechCommand
KAN
GPKAN
MLP
FAN
KAF
0 1 2 3 4 5
Number of Parameters 1e5
12
14
16
18
20
22Accuracy
UrbanSound8K
KAN
GPKAN
MLP
FAN
KAF
0 1 2 3 4 5
Number of Parameters 1e5
68.50
68.75
69.00
69.25
69.50
69.75Accuracy
CoLA
KAN
GPKAN
MLP
FAN
KAF
0 1 2 3 4 5
Number of Parameters 1e5
86
87
88
89
90
91Accuracy
AG_NEWS
KAN
GPKAN
MLP
FAN
KAF
Figure 3: Comparison of KAN, GPKAN, MLP, FAN, and KAF across NLP, audio, and
traditional machine learning datasets. KAF consistently achieves higher accuracy with fewer
parameters, especially on datasets such as Bean, Rice, and AG News.
GPKAN adopts GELU-based initialization; LayerNorm is disabled by default; and Dropout
follows each model’s standard setting.
Experimental results.Table 2 summarizes performance across multiple datasets when
various feature Mixers replace the original modules. KAF generally meets or exceeds baseline
accuracy while maintaining a reasonable parameter count and computational cost. For
instance, in ResNet-18 on CIFAR-10, KAF achieves 91.72% Top-1 accuracy (compared to
MLP’s91.19%), andonImageNet-1K,itimprovesMLP-Mixerfrom63.5%to64.7%. Although
compact approaches like FAN can reduce parameters, they often yield lower accuracy (e.g.,
58.2% on ImageNet-1K). Similarly, with ViT-T/16, KAF’s moderate parameter increment
still outperforms MLP, while in MLP_KAN (DeiT), KAF boosts baseline accuracy from
49.0% to 53.8%. Overall, KAF demonstrates gains and stable training on challenging tasks
and architectures, including attention-rich models. These results highlight its potential
as a more efficient and effective Mixer replacement in modern vision networks, balancing
parameter overhead with performance improvements.
4.3 Experiments on LLMs with KAF Components
To evaluate the potential of KAF in language models, we integrate it into the GPT-2
architecture by replacing the Feed-Forward Network (FFN)’s MLP with KAF or KAN. We
then train and evaluate the models on large-scale text datasets, assessing their impact on
language modeling quality and model complexity.
Experimental setup.We conduct experiments using OpenWebText and WikiText, two
widely used text datasets. The base model is GPT-2 (Small version), where the two-layer
MLP in the Feed-Forward Network (FFN) is replaced with KAF or KAN while maintaining
10
```

## PDF page 11

```text
Kolmogorov-Arnold Fourier Networks
Table 2: Comparison of different feature mixers in common vision architectures. Parameters
refer to the total model size, and FLOPs are computed for forward propagation.
(a) ResNet-18 on CIFAR-10 and ViT-T/16 on ImageNet-1K
Model Dataset Mixer #Param. FLOPs Top-1
ResNet/18 CIFAR-10 MLP 11.1M 0.56G 91.19
ResNet/18 CIFAR-10 KAF 12.0M 0.63G91.72
ResNet/18 CIFAR-10 GPKAN 11.3M 0.56G 90.98
ResNet/18 CIFAR-10 FAN 8M 0.42G 90.69
ResNet/18 CIFAR-10 KAN Too large – –
ViT-T/16 ImageNet-1K MLP 5.7M 1.08G 72.3
ViT-T/16 ImageNet-1K KAF 5.9M 1.12G73.2
ViT-T/16 ImageNet-1K GPKAN 5.7M 1.13G 74.6
ViT-T/16 ImageNet-1K FAN 4.2M 0.96G 65.7
ViT-T/16 ImageNet-1K KAN Too large – –
(b) MLP-Mixer/S on ImageNet-1K and MLP-KAN/DeiT on CIFAR-100
Model Dataset Mixer #Param. FLOPs Top-1
MLP-Mixer/S ImageNet-1K MLP 18.2M 3.8G 63.5
MLP-Mixer/S ImageNet-1K KAF 18.8M 4.2G64.7
MLP-Mixer/S ImageNet-1K GPKAN 18.8M 4.0G 62.9
MLP-Mixer/S ImageNet-1K FAN 15.7M 3.2G 58.2
MLP-Mixer/S ImageNet-1K KAN Too large – –
MLP-KAN/DeiT CIFAR-100 MLP 1.3M 0.12G 49.0
MLP-KAN/DeiT CIFAR-100 KAF 1.4M 0.15G 53.8
MLP-KAN/DeiT CIFAR-100 KAN 1.9M 0.19G 51.2
MLP-KAN/DeiT CIFAR-100 GPKAN 1.4M 0.14G54.3
MLP-KAN/DeiT CIFAR-100 FAN 1.0M 0.1G 46.7
the same parameter scale. All other Transformer configurations (Vaswani et al., 2023),
including multi-head attention, token embeddings, and positional encoding, remain consistent
with the official GPT-2 implementation.
Experimental results.Table 3 presents a comparison of GPT-2 using MLP, KAF, and KAN
as the FFN components on the WikiText and OpenWebText datasets. The results show that
KAF boosts language modeling performance and training efficiency. On WikiText, it reduces
PPL from 184.53 to 180.85 while cutting training time from 20h37m to 19h20m, indicating
improved performance without significant overhead. In contrast, KAN converges poorly,
with PPL escalating to 39,782 and training time rising sharply due to large parameter scales,
revealing severe optimization challenges. A similar pattern emerges on OpenWebText: KAF
again surpasses MLP by lowering PPL from 151.27 to 145.64 and further reducing training
time, whereas KAN remains unstable (PPL reaching 27,832), reaffirming its vulnerability
in large-scale language modeling. Overall, swapping MLP for KAF in GPT-2 consistently
enhances language modeling across WikiText and OpenWebText, while preserving reasonable
training costs. The experiment demonstrates that substituting MLP with KAF in GPT-2’s
FFN not only yields measurable improvements in perplexity and training efficiency across
datasets of varying scales but also highlights KAF’s robustness compared to large, more
unstable alternatives like KAN.
11
```

## PDF page 12

```text
Kolmogorov-Arnold Fourier Networks
Table 3: Comparison of GPT-2 based MLP, KAF, and KAN models on WikiText and
OpenWebText: perplexity, training time, and parameter count.
Model Dataset PPL Training Time #Param.
MLP WikiText 184.53 20h 37m 117M
KAF WikiText180.8519h 20m 128M
KAN WikiText 39782 304h 06m 478M
MLP OpenWebText 151.27 60h 57m 117M
KAF OpenWebText145.6452h 45m 128M
KAN OpenWebText 27832 960h 19m 478M
Table 4: Types of test functions and their mathematical expressions.
Function Name Mathematical Expression
Bessel Functionf(x) =J 0(20x)
Chaoticf(x, y) =e sin(πx)+y 2
Simple Productf(x, y) =x·y
High-Freq-Sumf(x) = P100
k=1 sin
  kx
100

Highly-Nonlinearf(x 1, x2, x3, x4) =e sin(x2
1+x2
2)+sin(x2
3+x2
4)
Discontinuousf(x) =



−1, x <−0.5
x2,−0.5≤x <0
sin(4πx),0≤x <0.5
1, x≥0.5
Oscillating-Decayf(x) =e −x2
sin(10πx)
Rationalf(x 1, x2) = x2
1+x2
2
1+x2
1+x2
2
Multi-Scalef(x 1, x2, x3) = tanh(x1x2x3) + sin(πx1) cos(πx2)e−x2
3
Exp-Sinef(x 1, x2) = sin(50x1) cos(50x2) +e − (x1 −0.5)2 +(x2 −0.5)2
0.1
4.4 Performance of KAF in Function Approximation and Differential Equation
Solving Tasks
To comprehensively validate the capability of KAF in complex function approximation
and PDE solving (Raissi et al., 2017), we design experiments that cover a wide range of
complexities, dimensions, and degrees of nonlinearity. Specifically, we consider eight function
approximation tasks to evaluate KAF’s ability to capture complex nonlinear relationships, and
four PDE-solving problems involving multiple physical parameters to assess its applicability
to scientific computing. We use various hyperparameter configurations to evaluate the
reliability and generalization ability of the results.
Experimental setup.We conduct 8 function approximation and 4 PDE solving (Raissi
et al., 2017; Han et al., 2018) tasks, addressing varying complexities, dimensions, and
nonlinearities. For function approximation and PDE tasks, we train models with hidden
layer sizes ranging from 8 to 512 for up to 1000 epochs.
Function approximation tasks.Table 4 lists the benchmark functions used in our
evaluation, covering periodicity, nonlinearity, high dimensionality, discontinuity, and chaotic
behavior.
12
```

## PDF page 13

```text
Kolmogorov-Arnold Fourier Networks
101 102 103 104 105 106 107
10 9
10 8
10 7
10 6
10 5
10 4
10 3
10 2
10 1
100
101
T est RMSE
Bessel
101 102 103 104 105 106 107
10 9
10 8
10 7
10 6
10 5
10 4
10 3
10 2
10 1
100
101
Chaotic
(2D)
101 102 103 104 105 106 107
10 9
10 8
10 7
10 6
10 5
10 4
10 3
10 2
10 1
100
101
Discontinuous
(1D)
101 102 103 104 105 106 107
10 9
10 8
10 7
10 6
10 5
10 4
10 3
10 2
10 1
100
101
Exp-Sine
101 102 103 104 105 106 107
10 9
10 8
10 7
10 6
10 5
10 4
10 3
10 2
10 1
100
101
High-Freq-Sum
101 102 103 104 105 106 107
Number of parameters
10 9
10 8
10 7
10 6
10 5
10 4
10 3
10 2
10 1
100
101
T est RMSE
Highly-Nonlinear
(3D)
101 102 103 104 105 106 107
Number of parameters
10 9
10 8
10 7
10 6
10 5
10 4
10 3
10 2
10 1
100
101
Multi-Scale
101 102 103 104 105 106 107
Number of parameters
10 9
10 8
10 7
10 6
10 5
10 4
10 3
10 2
10 1
100
101
Oscillating-Decay
(1D)
101 102 103 104 105 106 107
Number of parameters
10 9
10 8
10 7
10 6
10 5
10 4
10 3
10 2
10 1
100
101
Rational
(2D)
101 102 103 104 105 106 107
Number of parameters
10 9
10 8
10 7
10 6
10 5
10 4
10 3
10 2
10 1
100
101
Simple-Product
MLP
KAN
FAN
GPKAN
KAF
Figure 4: Comparison of KAN, GPKAN, MLP, FAN, and KAF on function approximation
tasks. We report test RMSE versus the number of parameters. KAF consistently achieves
lower RMSE across a wide range of functions.
As shown in Fig. 4, KAF achieves lower test RMSE than MLP, GPKAN, and FAN on most
function approximation tasks, demonstrating stronger fitting and generalization ability. For
example, on the Bessel task, KAF achieves a test RMSE of2.55 × 10−6, compared with
1.43 × 10−5 for MLP. On the Highly-Nonlinear and Multi-Scale tasks, KAF obtains RMSE
values of3.18 ×10−5 and4 .98 ×10−5, while MLP has substantially larger errors of1.41 ×10−4
and1.85×10 −2, respectively.
PDE solving tasks.As shown in Fig. 5, we evaluate KAF on four PDE-solving problems:
Poisson, 1D Wave, Heat, and Burgers equations. Traditional MLPs show larger errors or
lower stability, whereas KAF generally achieves better or comparable accuracy. For Poisson
and Heat equations, both KAF and KAN significantly reduce errors compared with MLP,
while FAN remains competitive. GPKAN is less stable in some cases due to its sensitivity to
parameter scale and initialization. Overall, these results suggest that KAF provides flexible
and robust function approximation for PDE-solving tasks.
4.5 Ablation Experiment
4.5.1 Ablation on CIF AR-10
We use a single-layer KAF trained on CIFAR-10 as the baseline model, with a hidden layer
size of 128.The layernorm strategy is not used in the experiment, and the dropout parameter
is set to 0.1 We evaluate the following strategies:
•No GELU activation function:Only the scaling factor and RFF strategy are used.
•No scaling factor strategy:The model is trained without the scaling factor.
•No RFF strategy:The model uses the scaling factor and GELU activation instead.
• Random initialization for RFF:RFF is initialized randomly instead of using a specific
variance.
• Effect of differentσ values:We report the highest test accuracy for different selections
ofσ.
13
```

## PDF page 14

```text
Kolmogorov-Arnold Fourier Networks
MLP KAN KAF FAN GPKAN
0.2450
0.2475
0.2500
0.2525
0.2550
0.2575
0.2600
2.50e-01
2.47e-01 2.47e-01
2.52e-01
2.50e-01
Poisson Equation
MLP KAN KAF FAN GPKAN
0.00
0.00
0.01
0.10
1.00
×10 6
7.16e-10
1.94e-10
1.92e-08
5.52e-09
9.15e-07
1D Wave Equation
MLP KAN KAF FAN GPKAN
0.5
1.0
1.5
2.0
2.5 2.39e+00
1.52e-01 1.49e-01 1.55e-01
2.38e+00
Heat Equation
MLP KAN KAF FAN GPKAN
0.0
0.0
0.0
0.0
0.1
1.0
×10 5
1.85e-07
5.02e-11
3.92e-08
3.95e-10
1.69e-06
Burgers Equation
Model Performance Comparison on Different PDEs
Models
MLP
KAN
KAF
FAN
GPKAN
Figure 5: Comparison of MLP, KAN, KAF, FAN, and GPKAN on Poisson, 1D Wave, Heat,
and Burgers equations. KAF consistently delivers strong performance.
Table 5: Ablation results for the RFF initialization scaleσ and the number of grids on
CIFAR-10.
(a) Effect of differentσvalues
σ0.1 0.5 1 1.5 1.6 1.64 1.7 1.8 2 2.5 3
ACC (%) 46.83 52.50 54.02 54.41 54.32 54.96 54.64 54.68 54.36 54.07 53.21
(b) Effect of differentnum_gridsvalues
num_grids2 4 6 8 9 10 12 14 16 18 20
ACC (%) 54.23 54.67 54.41 54.80 54.96 54.87 54.94 54.82 54.76 54.79 55.01
• Effect of different num_grids values:We report the highest test accuracy for different
selections of num_grids= 9.
Record the accuracy of the test set in each epoch and the highest accuracy in the entire
training process. At the same time, in order to observe the specific changes in the scaling
factors, we plotted the changes of the two scaling factors a and b of KAF with epochs in the
experiment.
The results of strategies 1–4 are shown in Fig. 6, and the hyperparameter ablations for
strategies 5–6 are reported in Table 5. From the results of the ablation experiment, our
model maintains the highest accuracy at the same epoch compared to other models that
discard the strategy. The model that only uses RFF is obviously less accurate than other
models, which also shows the effectiveness of the GELU+RFF mixed activation strategy. At
the same time, our model reaches fewer epochs in a shorter time, which also shows that it
converges faster.
14
```

## PDF page 15

```text
Kolmogorov-Arnold Fourier Networks
0 5 10 15 20 25 30 35 40
Epoch
30
35
40
45
50
55T est Accuracy (%)
Model T est Accuracy Comparison
only_rff
random_init
no_scale
only_GELU
KAF(original)
Figure 6: The curve of the test set accuracy of different strategies in the ablation experiment
on CIFAR-10 changes with epoch. KAF (original) demonstrates the effectiveness of our
model design, consistently achieving higher test accuracy compared to other strategies across
epochs.
At the same time, the ablation experiment of hyperparameters also proves the rationality
of our choice of σ = 1 .64, num_grids = 9as the default model configuration. When
σ = 1.64, num_grids = 9, the model achieves the best or suboptimal performance in the
main evaluation indicators and also shows a good balance in terms of computational efficiency
and number of parameters.
In Fig. 7, we show how the Base Scale and RFF Scale inside KAF change during training on
CIFAR-10. Both scales increase over training, with the RFF Scale growing more rapidly,
suggesting that the model increasingly relies on Fourier features to capture complex high-
dimensional information.
4.5.2 Fitting experiment of sin(x) and cos(x)
To evaluate the model’s capability in approximating periodic functions, we conduct a fitting
experiment on sin(x)and cos(x). Specifically, we train the model to learn the mapping
x7→sin (x)and x7→cos (x)using a dataset of uniformly sampled points from the interval
[−20, 20]. The training objective minimizes the mean squared error (MSE) between the
predicted and true values.
We use a single-layer network with 64 neurons in the hidden layer and test KAF, KAN, MLP
(RELU), and MLP (GELU). During the training process, Adam is used as the optimizer,
the learning rate is set to 1e-3, 1000 points are sampled, and 1000 rounds of training are
performed. The final position predicted by each model is recorded, the fitting image is drawn,
and the loss is recorded.
15
```

## PDF page 16

```text
Kolmogorov-Arnold Fourier Networks
1.0
1.1
1.2
1.3
1.4
1.5Base Scale (a)
Base Scale
0 50 100 150 200 250 300 350
Time
0.0
0.2
0.4
0.6
0.8
1.0RFF Scale (b)
RFF Scale
Activation Parameters over Time
Figure 7: Evolution of scaling factors over time: Base Scale (a) and RFF Scale (b).
Fig. 8 illustrates the fitting results of different models forsin(x)and cos(x). It can be
observed that MLP_RELU and MLP_GELU struggle to maintain the periodic structure
when the input range is large. While KAN performs relatively well in certain regions, it
still exhibits significant deviations in the low-frequency range. In contrast, the KAF model
more accurately captures the periodicity of the target functions and provides superior fitting
performance across most regions.
Fig. 9 presents the frequency spectrum analysis of different models onsin(x)and cos(x). The
true signal’s spectral energy is primarily concentrated in the low-frequency region, and the
spectral distribution of the KAF model closely matches the true signal, effectively preserving
the spectral characteristics of the target function. On the other hand, MLP_RELU and
MLP_GELU exhibit significant deviations in the high-frequency components, indicating
their difficulty in accurately representing high-frequency features. Although KAN’s spectral
response aligns more closely with the true signal in some frequency bands, there are still
noticeable discrepancies in energy distribution.
5 Conclusion
We present Kolmogorov-Arnold Fourier Networks (KAF), a spectral reparameterization
of Kolmogorov-Arnold Networks that replaces spline-based basis functions with trainable
Random Fourier Features and a hybrid GELU-Fourier activation mechanism. The proposed
16
```

## PDF page 17

```text
Kolmogorov-Arnold Fourier Networks
60
 40
 20
 0 20 40 60
x
1.0
0.5
0.0
0.5
1.0
y
MLP_RELU (sin)
60
 40
 20
 0 20 40 60
x
1.0
0.5
0.0
0.5
1.0
y
KAN (sin)
60
 40
 20
 0 20 40 60
x
1.5
1.0
0.5
0.0
0.5
1.0
1.5
y
MLP_RELU (cos)
60
 40
 20
 0 20 40 60
x
1.5
1.0
0.5
0.0
0.5
1.0
1.5
y
KAN (cos)
60
 40
 20
 0 20 40 60
x
1.0
0.5
0.0
0.5
1.0
y
MLP_GELU (sin)
60
 40
 20
 0 20 40 60
x
1.0
0.5
0.0
0.5
1.0
y
KAF (sin)
60
 40
 20
 0 20 40 60
x
1.5
1.0
0.5
0.0
0.5
1.0
1.5
y
MLP_GELU (cos)
60
 40
 20
 0 20 40 60
x
1.5
1.0
0.5
0.0
0.5
1.0
1.5
y
KAF (cos)
Function Approximation Results
Figure 8: Four models fitted on the standard sin/cos function after training 1000 epochs.
0.0 0.1 0.2 0.3 0.4 0.5
Frequency
10 6
10 4
10 2
100
102
Magnitude
Frequency Spectrum (sin)
MLP_RELU
KAN
KAF
MLP_GELU
Ground Truth
0.0 0.1 0.2 0.3 0.4 0.5
Frequency
10 4
10 3
10 2
10 1
100
101
102
103
104
Magnitude
Frequency Spectrum (cos)
MLP_RELU
KAN
KAF
MLP_GELU
Ground Truth
Figure 9: Frequency spectrum analysis of different models forsin(x)andcos(x).
architecture combines the smooth low-frequency behavior of standard activations with the
high-frequency representation ability of Fourier features, improving parameter efficiency and
spectral expressiveness while retaining the function-approximation perspective of KANs.
Through experiments across vision, natural language processing, audio classification, function
approximation, andPDE-solvingtasks, weshowthatKAFcanserveasapracticalreplacement
for KAN and MLP components in modern neural architectures. The results demonstrate that
KAF achieves competitive or improved accuracy with better scalability than spline-based
KAN variants. Future work will investigate more robust initialization strategies, adaptive
frequency selection mechanisms, and extensions of KAF to larger-scale architectures and
more demanding scientific computing applications.
Future Directions.The current KAF design uses a fixed number of Fourier features
and a predefined initialization scale across tasks. A promising direction is to make the
frequency basis more adaptive, allowing the model to allocate spectral capacity according
to the data distribution, model depth, and task complexity. Another useful extension is to
study task-dependent initialization and regularization strategies for the RFF branch, which
may further improve convergence stability and reduce the need for manual hyperparameter
tuning.
17
```

## PDF page 18

```text
Kolmogorov-Arnold Fourier Networks
Appendix A. Kernel Approximation and Gradient Derivation of Random
Fourier Features (RFF)
A.1 Convergence Proof of RFF Kernel Approximation
A.1.1 Bochner’s Theorem and the Fourier Duality of Kernel Functions
According to Bochner’s (Rahimi and Recht, 2007a; Gradshteyn and Ryzhik, 2014) theorem,
any translation-invariant positive definite kernel functionk(x, y) = k(x−y )can be expressed
as the Fourier transform of a Gaussian measure:
k(x−y) =
Z
Rd
eiω⊤(x−y)p(ω)dω,(14)
where p(ω)is the spectral distribution corresponding to the kernel function. For the Gaussian
kernelk(x, y) =e −∥x−y∥2/(2σ2), its spectral distribution is:
p(ω) =N(ω; 0, σ −2Id).(15)
A.1.2 Expectation of Inner Product of Random Fourier Features
Define the RFF mapping:
z(x) =
r
1
m
h
cos(ω⊤
1 x+b 1),sin(ω ⊤
1 x+b 1), . . . ,cos(ω ⊤
mx+b m),sin(ω ⊤
mx+b m)
i⊤
,(16)
whereω i ∼p(ω), andb i ∼ U[0,2π]. The expectation of the inner product is:
E
h
z(x)⊤z(y)
i
= 1
m
mX
i=1
E
h
cos(ω⊤
i x+b i) cos(ω⊤
i y+b i) + sin(ω⊤
i x+b i) sin(ω⊤
i y+b i)
i
= 1
m
mX
i=1
E
h
cos(ω⊤
i (x−y))
i
→E ω∼p(ω)
h
cos(ω⊤(x−y))
i
=k(x−y).
(17)
A.1.3 Error Bound and Convergence Rate
According to Rahimi & Recht (Rahimi and Recht, 2007a), when usingm random frequencies,
for anyx, y∈ X, we have:
P

sup
x,y
z(x)⊤z(y)−k(x, y)
 ≥ϵ

≤2 8
 σp diam(X)
ϵ
2
exp

− mϵ2
4(d+ 2)

.(18)
where σp is the variance ofp(ω), anddiam(X )is the diameter of the input space. Thus, the
convergence rate isO(1/√m).
18
```

## PDF page 19

```text
Kolmogorov-Arnold Fourier Networks
A.2 Differentiability and Gradient Computation of RFF
A.2.1 Analytical Gradient Expressions
Let ω∈R d be a row of the frequency matrixW, and b be the corresponding phase shift. For
an inputx∈R d:
•Gradient of the cosine term:
∂
∂ω cos(ω⊤x+b) =−xsin(ω ⊤x+b), ∂
∂b cos(ω⊤x+b) =−sin(ω ⊤x+b)(19)
•Gradient of the sine term:
∂
∂ω sin(ω⊤x+b) =xcos(ω ⊤x+b), ∂
∂b sin(ω⊤x+b) = cos(ω ⊤x+b)(20)
For a matrixW∈R d×m, gradients accumulate row-wise. ForWij (the i-th row,j-th column):
∂cos(W ⊤
j x+b j)
∂Wij
=−x i sin(W ⊤
j x+b j),(21)
whereW j is thej-th column ofW.
A.2.2 Implementation in Backpropagation
In automatic differentiation frameworks (Baydin et al., 2018) (e.g., PyTorch), the gradient
computation for RFF follows these steps:
•Forward pass: Computecos(W ⊤x+b)andsin(W ⊤x+b).
• Backward pass: Using the chain rule, the gradient tensor forW is −x⊗sin (W ⊤x + b)
(outer product) andx⊗cos (W ⊤x + b). The gradient forb is directly −sin (W ⊤x + b)and
cos(W ⊤x+b).
• Numerical stability: (1) Input normalization: Use LayerNorm or BatchNorm onx to
prevent exploding gradients. (2) Gradient clipping: Restrict ∥∇W ∥2 ≤τ to avoid
instability from high-frequency noise.
A.3 RFF Initialization Strategy Derivation
A.3.1 Frequency Sampling and Kernel Bandwidth Correspondence
ThespectraldistributionoftheGaussiankernel k(x, y) = e−∥x−y∥2/(2σ2) is p(ω) = N (0, σ−2Id).
Hence, frequencies should be sampled asω∼ N (0, σ−2Id). However, if input data is stan-
dardized such that each dimension satisfiesE[x2
i ] = 1/d, then the variance ofω⊤xis:
V[ω⊤x] =E[x ⊤ωω⊤x] =Tr(E[ωω ⊤]E[xx⊤]) =σ −2 ·Tr(I d/d) =σ −2.(22)
To makeω⊤x independent of input scale, frequency variance should be adjusted toσ−2/d,
i.e.,ω ij ∼ N(0, σ −2/d).
19
```

## PDF page 20

```text
Kolmogorov-Arnold Fourier Networks
A.3.2 Determination of Scaling F actorγ
Assuming the activation functionσ(x)has an output variance ofE[∥σ(x)∥2] = c, the frequency
matrix should be initialized such that:
σ−2
d ·E[∥W∥ 2
F ] =γ 2 =⇒γ= σ−1
√
d
.(23)
Thus, the initialization strategy isωij ∼ N(0, γ 2/d), whereγ=σ −1/
p
E[∥σ(x)∥2].
Appendix B. Fourier theory proof of GELU activation function
initialization factorσ= 1.64
B.1 Definition and Assumptions
Consider an input signalx∼ N(0, σ 2), whose Fourier transform is:
F {x}(ω) =
Z ∞
−∞
xe−iωxdx.(24)
The GELU activation function is defined as:
GELU(x) =x·Φ(x),(25)
whereΦ( x)is the cumulative distribution function (CDF) of a standard normal distribution.
B.2 Fourier Transform of GELU
Using the differentiation property and the convolution theorem of Fourier transforms, we
have:
F {GELU(x)}(ω) =F {xΦ(x)}(ω) =i d
dω F {Φ(x)}(ω).(26)
The Fourier transform ofΦ(x)is known as:
F {Φ(x)}(ω) =
r π
2 e−ω2/2

1 +erf
 iω√
2

.(27)
Taking its derivative yields:
F {GELU(x)}(ω) =
r π
2

−ωe−ω2/2

1 +erf
 iω√
2

+ i√
2 e−ω2

.(28)
B.3 Spectral Energy Distribution
The spectral energy density of GELU is:
S(ω) =|F {GELU(x)}(ω)| 2 .(29)
Through numerical integration, it can be observed that most energy is concentrated in the
low-frequency region (|ω|< ω c), and the high-frequency components decay exponentially
with increasingω.
20
```

## PDF page 21

```text
Kolmogorov-Arnold Fourier Networks
B.4 Scaling FactorαOptimization in Frequency Spectrum
B.4.1 Objective Function Definition
To minimize the spectral distortion of the scaled activation function, we define:
L(α) =
Z ∞
−∞
Starget(ω)−α 2SGELU(ω)
2
dω.(30)
Assuming the target spectrum follows white noise, i.e.,Starget(ω) = 1.
B.4.2 Optimization Solution
Expanding the objective function:
L(α) =
Z ∞
−∞
 
1−α 2SGELU(ω)
2
dω.(31)
Taking the derivative with respect toαand setting it to zero:
dL
dα =−4α
Z ∞
−∞
SGELU(ω)
 
1−α 2SGELU(ω)

dω= 0.(32)
Solving for the optimalα:
αopt =
sR ∞
−∞ SGELU(ω)dωR ∞
−∞ S2
GELU(ω)dω .(33)
B.4.3 Numerical Integration Results
Using Monte Carlo integration, we compute:
Z ∞
−∞
SGELU(ω)dω≈0.168,
Z ∞
−∞
S2
GELU(ω)dω≈0.062.(34)
Substituting these values:
αopt =
r
0.168
0.062 ≈1.64.(35)
B.5 Dynamic Adaptation of Fourier Characteristics
B.5.1 Spectrum Matching Mechanism
Random Fourier features (RFF) sample frequenciesωi ∼ N (0, σ−2)to approximate the
target spectrum. When the GELU cutoff frequencyωc matches the sampling bandwidth of
RFF (i.e., σ≈ 1.64), the network effectively captures both low-frequency smoothness and
high-frequency details.
B.5.2 Dynamic Balance in Training
Initially, a small scaling factor β = 10 −2 suppresses high-frequency noise. As training
progresses, β gradually increases to enhance high-frequency correction, eventually achieving
full spectral coverage.
21
```

## PDF page 22

```text
Kolmogorov-Arnold Fourier Networks
Appendix C. Detailed derivation of parameter quantities and FLOPs
calculations
C.1 KAN with B-splines: Parameter Counting
Number of B-spline Basis Parameters.Let the B-spline (De Boor, 1972) order beK,
and divide the domain intoGsegments. Then:
•Each segment needsK+ 1control points, total(G+K+ 1).
•Boundary smoothness of orderK−1adds2(K−1)virtual points.
•Total per univariate spline:G+ 3K−1. (Sometimes simplified toG+K+ 3.)
Single-Layer Parameter Decomposition in KAN.For dimensiondin →d out:Internal
function (B-spline projection):din ×d out splines, each with(G + K + 3)parameters. Hence,
ParamsKAN =d in dout (G+K+ 3) +d out.(36)
C.2 KAF with RFF: FLOPs Decomposition
Single-layer KAF.
• Random Fourier Feature (RFF (Rahimi and Recht, 2007b)) mapping:cos(W ⊤x + b)and
sin(W ⊤x + b)each require one matrix multiplication. Total FLOPs (Tang et al., 2018):
2×(d in ×M)×2 = 4d inM.
• Linear combination (GELU + RFF):Element-wisescalingofa⊙GELU(x)andb ⊙ϕRFF(x).
Total FLOPs:2×(d in ×M)×2 = 4d inM.
• Final linear projection: Matrix multiplicationW(l) · (·)and bias addition. Total FLOPs:
2dindout.
•Activation function: GELU activation requires5d in FLOPs.
Total FLOPs: FLOPsKAF = 4dinM+ 2d in + 2dindout + 5din.
C.3 MLP FLOPs Computation
Standard MLP.
•Linear layerW∈R dout×din:2d in dout FLOPs (multiply+add).
• Activation: (1) ReLU:1FLOP per output (comparison), total dout. (2) GELU: about
5d out FLOPs.
Hence, for a GELU-MLP: FLOPsMLP = 2d in dout + 5d out.
C.4 Summary Comparison
•KAN: Param and FLOPs scale with spline orderKand segment countG.
•KAF: RFF-based expansion is more GPU-friendly than B-spline recursion.
•MLP: Minimal overhead with no extra basis expansions.
22
```

## PDF page 23

```text
Kolmogorov-Arnold Fourier Networks
References
Nachman Aronszajn. Theory of reproducing kernels.Transactions of the American Mathe-
matical Society, 68(3):337–404, 1950.
Francis Bach. Breaking the curse of dimensionality with convex neural networks, 2016. URL
https://arxiv.org/abs/1412.8690.
Andrew R Barron. Universal approximation bounds for superpositions of a sigmoidal function.
IEEE Transactions on Information theory, 39(3):930–945, 1993.
Atilim Gunes Baydin, Barak A. Pearlmutter, Alexey Andreyevich Radul, and Jeffrey Mark
Siskind. Automatic differentiation in machine learning: a survey, 2018. URL https:
//arxiv.org/abs/1502.05767.
JuliusBerner, PhilippGrohs, GittaKutyniok, andPhilippPetersen.The Modern Mathematics
of Deep Learning, page 1–111. Cambridge University Press, December 2022. ISBN
9781316516782. doi: 10.1017/9781009025096.002. URL http://dx.doi.org/10.1017/
9781009025096.002.
Ronald N Bracewell.The Fourier Transform and Its Applications. McGraw-Hill, New York,
1986.
Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla
Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini
Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya
Ramesh, Daniel M. Ziegler, Jeffrey Wu, Clemens Winter, Christopher Hesse, Mark Chen,
Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner,
Sam McCandlish, Alec Radford, Ilya Sutskever, and Dario Amodei. Language models are
few-shot learners, 2020. URLhttps://arxiv.org/abs/2005.14165.
Sheng Chen, Xia Hong, Emad Khalaf, Ali Morfeq, and Naif D. Alotaibi. Adaptive b-spline
neural network based nonlinear equalization for high-order qam systems with nonlinear
transmit high power amplifier.Digital Signal Processing, 40:238–249, 2015. ISSN 1051-2004.
doi: https://doi.org/10.1016/j.dsp.2015.02.006. URL https://www.sciencedirect.com/
science/article/pii/S1051200415000494.
Tarin Clanuwat, Mikel Bober-Irizar, Asanobu Kitamoto, Alex Lamb, Kazuaki Yamamoto, and
David Ha. Deep learning for classical japanese literature.arXiv preprint arXiv:1812.01718,
2018.
Gregory Cohen, Saeed Afshar, Jonathan Tapson, and Andre Van Schaik. Emnist: Extending
mnist to handwritten letters.2017 International Joint Conference on Neural Networks
(IJCNN), pages 2921–2926, 2017.
Carl De Boor. On calculating with b-splines.Journal of Approximation theory, 6(1):50–62,
1972.
23
```

## PDF page 24

```text
Kolmogorov-Arnold Fourier Networks
Yihong Dong, Ge Li, Yongding Tao, Xue Jiang, Kechi Zhang, Jia Li, Jinliang Deng, Jing
Su, Jun Zhang, and Jingjing Xu. Fan: Fourier analysis networks.Advances in Neural
Information Processing Systems, 38:66267–66296, 2025.
Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai,
Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly,
Jakob Uszkoreit, and Neil Houlsby. An image is worth 16x16 words: Transformers for
image recognition at scale, 2021. URLhttps://arxiv.org/abs/2010.11929.
Stefan Elfwing, Eiji Uchibe, and Kenji Doya. Sigmoid-weighted linear units for neural network
function approximation in reinforcement learning, 2017. URLhttps://arxiv.org/abs/
1702.03118.
Rizal Fathony, Anit Kumar Sahu, Devin Willmott, and J Zico Kolter. Multiplicative filter
networks.International Conference on Learning Representations, 2021.
Xavier Glorot and Yoshua Bengio. Understanding the difficulty of training deep feedfor-
ward neural networks.Proceedings of the thirteenth international conference on artificial
intelligence and statistics, pages 249–256, 2010.
Xavier Glorot, Antoine Bordes, and Yoshua Bengio. Deep sparse rectifier neural networks.
Proceedings of the fourteenth international conference on artificial intelligence and statistics,
pages 315–323, 2011.
Izrail Solomonovich Gradshteyn and Iosif Moiseevich Ryzhik.Table of integrals, series, and
products. Academic press, 2014.
Jiequn Han, Arnulf Jentzen, and Weinan E. Solving high-dimensional partial differential
equations using deep learning.Proceedings of the National Academy of Sciences, 115(34):
8505–8510, 2018.
Jiequn Han, Yingzhou Li, Lin Lin, Jianfeng Lu, Jiefu Zhang, and Linfeng Zhang. Universal ap-
proximation of symmetric and anti-symmetric functions.arXiv preprint arXiv:1912.01765,
2019.
Song Han, Huizi Mao, and William J. Dally. Deep compression: Compressing deep neural
networks with pruning, trained quantization and huffman coding, 2016. URLhttps:
//arxiv.org/abs/1510.00149.
Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Delving deep into rectifiers:
Surpassing human-level performance on imagenet classification. InProceedings of the IEEE
International Conference on Computer Vision, pages 1026–1034, 2015a.
Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Deep residual learning for image
recognition, 2015b. URLhttps://arxiv.org/abs/1512.03385.
Yunhong He, Yifeng Xie, Zhengqing Yuan, and Lichao Sun. Mlp-kan: Unifying deep
representation and function learning, 2024. URLhttps://arxiv.org/abs/2410.03027.
24
```

## PDF page 25

```text
Kolmogorov-Arnold Fourier Networks
Dan Hendrycks and Kevin Gimpel. Gaussian error linear units (gelus).arXiv preprint
arXiv:1606.08415, 2016.
Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang, Tobias
Weyand, Marco Andreetto, and Hartwig Adam. Mobilenets: Efficient convolutional neural
networks for mobile vision applications, 2017. URLhttps://arxiv.org/abs/1704.04861.
Noah Yi-Ting Hung, Li-Hsiang Lin, and Vince D. Calhoun. Deep p-spline: Theory, fast
tuning, and application, 2025. URLhttps://arxiv.org/abs/2501.01376.
Patrick Kidger and Terry Lyons. Universal approximation with deep narrow networks.
Mathematics of Computation, 89(324):2549–2570, 2020.
Diederik P Kingma and Jimmy Ba. Adam: A method for stochastic optimization.arXiv
preprint arXiv:1412.6980, 2014.
Andrey Nikolaevich Kolmogorov.Grundbegriffe der Wahrscheinlichkeitsrechnung. Springer,
Berlin, 1933.
Alex Krizhevsky. Learning multiple layers of features from tiny images. 2009.
Yann LeCun, Léon Bottou, Yoshua Bengio, and Patrick Haffner. Gradient-based learning
applied to document recognition.Proceedings of the IEEE, 86(11):2278–2324, 2002.
Ziming Liu, Yixuan Wang, Sachin Vaidya, Fabian Ruehle, James Halverson, Marin Soljačić,
Thomas Y. Hou, and Max Tegmark. Kan: Kolmogorov-arnold networks, 2024. URL
https://arxiv.org/abs/2404.19756.
Hrushikesh N Mhaskar. Neural networks for optimal approximation of smooth and analytic
functions.Neural computation, 8(1):164–177, 1996.
Vinod Nair and Geoffrey E Hinton. Rectified linear units improve restricted boltzmann
machines. InICML, 2010.
Yuval Netzer, Tao Wang, Adam Coates, Alessandro Bissacco, Bo Wu, and Andrew Y Ng.
Reading digits in natural images with unsupervised feature learning. InNIPS workshop
on deep learning and unsupervised feature learning, volume 2011, page 5, 2011.
NasimRahaman, AristideBaratin, DevanshArpit, FelixDraxler, MinLin, FredA.Hamprecht,
Yoshua Bengio, and Aaron Courville. On the spectral bias of neural networks, 2019. URL
https://arxiv.org/abs/1806.08734.
Ali Rahimi and Benjamin Recht. Random features for large-scale kernel machines.Advances
in Neural Information Processing Systems, 20:1177–1184, 2007a.
Ali Rahimi and Benjamin Recht. Random features for large-scale kernel machines.Advances
in Neural Information Processing Systems (NeurIPS), 20:1177–1184, 2007b.
Maziar Raissi, Paris Perdikaris, and George Em Karniadakis. Physics informed deep learning
(part i): Data-driven solutions of nonlinear partial differential equations, 2017. URL
https://arxiv.org/abs/1711.10561.
25
```

## PDF page 26

```text
Kolmogorov-Arnold Fourier Networks
Prajit Ramachandran, Barret Zoph, and Quoc V. Le. Searching for activation functions,
2017. URLhttps://arxiv.org/abs/1710.05941.
David E Rumelhart, Geoffrey E Hinton, and Ronald J Williams. Learning representations
by back-propagating errors.Nature, 323(6088):533–536, 1986.
Johannes Schmidt-Hieber. The kolmogorov-arnold representation theorem revisited, 2021.
URLhttps://arxiv.org/abs/2007.15884.
Bernhard Schölkopf and Alexander J Smola.Learning with kernels: support vector machines,
regularization, optimization, and beyond. MIT press, 2018.
Vincent Sitzmann, Julien NP Martel, Alexander Bergman, David B Lindell, and Gordon
Wetzstein. Implicit neural representations with periodic activation functions.Advances in
Neural Information Processing Systems (NeurIPS), 33:7462–7473, 2020.
Mingxing Tan and Quoc V. Le. Efficientnet: Rethinking model scaling for convolutional
neural networks, 2020. URLhttps://arxiv.org/abs/1905.11946.
Mingxing Tan and Quoc V. Le. Efficientnetv2: Smaller models and faster training, 2021.
URLhttps://arxiv.org/abs/2104.00298.
Matthew Tancik, Pratul P Srinivasan, Ben Mildenhall, Sara Fridovich-Keil, Nithin Raghavan,
Utkarsh Singhal, Ravi Ramamoorthi, Jonathan T Barron, and Ren Ng. Fourier features
let networks learn high frequency functions in low dimensional domains. InAdvances in
Neural Information Processing Systems, pages 7537–7547, 2020.
Raphael Tang, Ashutosh Adhikari, and Jimmy Lin. Flops as a direct optimization objective
for learning sparse neural networks, 2018. URLhttps://arxiv.org/abs/1811.03060.
Ilya O Tolstikhin, Neil Houlsby, Alexander Kolesnikov, Lucas Beyer, Xiaohua Zhai, Thomas
Unterthiner, Jessica Yung, Andreas Steiner, Daniel Keysers, Jakob Uszkoreit, et al. Mlp-
mixer: An all-mlp architecture for vision.Advances in neural information processing
systems, 34:24261–24272, 2021.
Hugo Touvron, Matthieu Cord, Matthijs Douze, Francisco Massa, Alexandre Sablayrolles, and
Hervé Jégou. Training data-efficient image transformers & distillation through attention,
2021. URLhttps://arxiv.org/abs/2012.12877.
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N.
Gomez, Lukasz Kaiser, and Illia Polosukhin. Attention is all you need, 2023. URL
https://arxiv.org/abs/1706.03762.
Eric Arthur Werneburg. Training neural networks using reproducing kernel space interpolation
and model reduction, 2023. URLhttps://arxiv.org/abs/2308.16754.
Xingyi Yang and Xinchao Wang. Kolmogorov-arnold transformer, 2024. URL https:
//arxiv.org/abs/2409.10594.
Runpeng Yu, Weihao Yu, and Xinchao Wang. Kan or mlp: A fairer comparison, 2024. URL
https://arxiv.org/abs/2407.16674.
26
```
