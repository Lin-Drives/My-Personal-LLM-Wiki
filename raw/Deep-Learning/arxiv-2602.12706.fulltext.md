# arXiv:2602.12706 — PDF 原文文本提取

- Source: https://arxiv.org/abs/2602.12706
- Local PDF: `2026-02-13-physics-informed-laplace-neural-operator-for-solving-partial-differential-equations-arxiv-2602.12706.pdf` (local only)
- PDF SHA-256: `870c6bc46e3a78a70e63b61a3af0dd9b0c7422d8eba6a6b67b07e2b4ef0eb5e4`
- Converted at: 2026-10-06T23:51:12.277471+00:00
- Extractor: pypdf/6.10.0
- Pages: 38
- Pages without extractable text: none

> 逐页提取 PDF 文本，未使用模型改写或翻译，未进行内容核验。保留页码；多栏阅读顺序、公式、表格和图片可能不能准确还原。无文字页需要另行 OCR，不能视为完整文本覆盖。基础 ID 的具体版本尚未解析，以 PDF 哈希标识本次原文件。

## PDF page 1

```text
Physics-Informed Laplace Neural Operator for Solving Partial
Differential Equations
Heechang Kima, Qianying Caob, Hyomin Shina, Seungchul Leec, George Em Karniadakisb,
Minseok Choia,∗
aDepartment of Mathematics, Pohang University of Science and Technology (POSTECH), Pohang, 37673, Republic of
Korea
bDivision of Applied Mathematics, Brown University, Providence, 02906, Rhode Island, United States
cDepartment of Mechanical Engineering, Korea Advanced Institute of Science and Technology
(KAIST), Daejeon, 34141, Republic of Korea
Abstract
Neural operators have emerged as fast surrogate solvers for parametric partial differential equations
(PDEs). However, purely data-driven models often require extensive training data and can general-
ize poorly, especially in small-data regimes and under unseen (out-of-distribution) input functions
that are not represented in the training data. To address these limitations, we propose thePhysics-
Informed Laplace Neural Operator(PILNO), which enhances the Laplace Neural Operator (LNO)
by embedding governing physics into training through PDE, boundary condition, and initial condi-
tion residuals. To improve expressivity, we first introduce anAdvanced LNO(ALNO) backbone that
retains a pole–residue transient representation while replacing the steady-state branch with an FNO-
style Fourier multiplier. To make physics-informed training both data-efficient and robust, PILNO
further leverages (i)virtual inputs: an unlabeled ensemble of input functions spanning a broad spec-
tral range that provides abundant physics-only supervision and explicitly targets out-of-distribution
(OOD) regimes; and (ii)temporal-causality weighting: a time-decaying reweighting of the physics
residual that prioritizes early-time dynamics and stabilizes optimization for time-dependent PDEs.
Across four representative benchmarks—Burgers’ equation, Darcy flow, a reaction–diffusion sys-
tem, and a forced KdV equation—PILNO consistently improves accuracy in small-data settings
(e.g.,N train ≤27), reduces run-to-run variability across random seeds, and achieves stronger OOD
generalization than purely data-driven baselines.
Keywords:Partial differential equations, Neural operators, Physics-informed learning,
Out-of-distribution generalization, Small-data regimes
∗Corresponding author
Email addresses:heechangkim@postech.ac.kr(Heechang Kim),qianying_cao@brown.edu
(Qianying Cao),zhainl@postech.ac.kr(Hyomin Shin),seunglee@kaist.ac.kr(Seungchul Lee),
george_karniadakis@brown.edu(George Em Karniadakis),mchoi@postech.ac.kr(Minseok Choi)
arXiv:2602.12706v1  [cs.LG]  13 Feb 2026
```

## PDF page 2

```text
1. Introduction
Recent advances in machine learning, supported by modern GPUs and software frameworks [1–
3], have accelerated progress in scientific computing for partial differential equations (PDEs) [4–9].
In many applications, learned surrogate models complement classical numerical solvers [10] by en-
abling fast evaluation across varying geometries, parameters, and boundary/initial conditions [8, 11,
12]. Within this landscape, operator learning has emerged as a promising paradigm: it aims to learn
mappings between infinite-dimensional function spaces, providing fast surrogates for parametric
PDEs in many scientific and engineering applications [13, 14].
Operator learning methods can be broadly grouped into two main directions. The first is exem-
plified by DeepONet [6], which leverages the universal approximation theorem for nonlinear opera-
tors [15, 16] and uses a branch–trunk architecture to encode the input functions and the coordinates
of evaluation points. DeepONet’s branch–trunk decomposition has since motivated a broad class
of extensions and variants [14, 17–21]. In parallel, the second direction comprises integral–kernel
neural operators [5, 13, 22–26], which generalize deep networks to the operator setting by compos-
ing learnable integral operators with pointwise nonlinearities. Representative examples include the
Graph Neural Operator (GNO) [23], the Fourier Neural Operator (FNO) [5], and the Laplace Neural
Operator (LNO) [25], where kernel integration is parameterized via a pole–residue representation in
the Laplace domain [27–29]. These approaches have demonstrated strong empirical performance in
a wide range of applications [30–33].
Despite these successes, existing neural operators face two persistent challenges.(i) Data effi-
ciency:high accuracy typically requires many paired input–output samples, which may be expen-
sive to obtain from high-fidelity simulations or experiments [21, 34, 35]. In small-data regimes,
limited supervision often fails to constrain fine-scale dynamics, and performance can degrade sub-
stantially [19, 20].(ii) Robust generalization:test error can increase sharply when inputs differ
from the training distribution (out-of-distribution, OOD) [36]. These limitations motivate operator-
learning approaches that remain reliable both in the small-data regimes and under OOD inputs.
Physics-informed operator learning addresses these issues by augmenting the training objective
with PDE constraints [8, 35, 37–39]. Inspired by physics-informed neural networks (PINNs) [4],
such methods penalize PDE, boundary-condition, and initial-condition residuals evaluated on model
predictions, guiding the learned operator toward physically consistent solutions even when observa-
tions are scarce or partially missing [40–42]. For example, PINO [35] uses multi-resolution residual
evaluation to improve accuracy, and PI-DeepONet [37] improves performance when training and
testing conditions differ moderately. Zhu et al. [36] study extrapolation systematically and propose
physics- and data-informed adaptation strategies to correct pre-trained operators under distribution
shift.
However, existing physics-informed operator frameworks remain limited in how they address
small-data training and better generalization to OOD inputs. First, many approaches incorporate
2
```

## PDF page 3

```text
physics primarily on the given training distribution and then rely on fine-tuning to handle extrapola-
tion [36], rather than training the operator from the outset to be robust across a deliberately broadened
family of inputs (e.g., sweeping over correlation length-scales or spectral content). Second, many
physics-informed operator methods still require intermediate-to-large training data sets [35, 37] and
rarely quantify how test performance scales as the number of training data decreases. In particular,
there is little quantitative analysis of the extent to which physics-informed operator architectures
can temper the growth of test error as training data become extremely scarce. These gaps open a
central question: to what extent can physics-informed operator learning genuinely improve data effi-
ciency and robustness on test inputs that differ from the training distribution, compared with purely
data-driven neural operators?
In this work, we propose thePhysics-Informed Laplace Neural Operator(PILNO), which builds
on an Advanced Laplace Neural Operator (ALNO) backbone and incorporates physics-informed
training with two mechanisms designed for data efficiency and better generalization. ALNO re-
tains the pole–residue transient component of LNO [27, 28, 43, 44] while replacing the steady-state
response with an FNO-style Fourier multiplier [5], improving expressivity without sacrificing in-
terpretability. Note that ALNO was previously outlined in the supplementary material of our prior
work [25] and is fully developed in this paper. On top of ALNO, PILNO incorporates: (i)vir-
tual inputs, an unlabeled ensemble of admissible inputs spanning a broad range of input spectra,
which provides abundant physics-only supervision and explicitly targets OOD regimes; and (ii)
temporal-causality weighting[7, 45], a time-decaying reweighting of the physics residual that em-
phasizes early-time dynamics at the beginning of the training, moves forward in time, and stabilizes
optimization for time-dependent PDEs. By combining PDE/BC/IC residuals with supervised data
when available, PILNO reduces dependence of training data and improves physical fidelity relative
to purely data-driven LNO, particularly in small-data and OOD settings. While physics-informed
losses, virtual inputs, and causal training strategies have been explored in the PINNs, to the best of
our knowledge, this work is the first to systematically integrate these mechanisms into a Laplace
neural operator with explicit transient-steady separation, and quantify their impact on operator gen-
eralization, data efficiency, and OOD robustness. Our main contributions are:
•Advanced LNO (ALNO).We provide a complete formulation of ALNO with an explicit
transient–steady decomposition: a pole–residue transient representation and a Fourier-multiplier
steady-state representation, yielding a more expressive and efficient backbone.
•Virtual inputs.We introduce a label-free input ensemble that broadens the training spectrum,
improves data efficiency and OOD generalization compared to data-driven LNO.
•Temporal-causality weighting. (semigroup-aware residual weighting)We propose a causal,
time-decaying weighting of the physics residual that emphasizes early-time dynamics; from
3
```

## PDF page 4

```text
an operator viewpoint, this stabilizes the learned evolution operators and mitigates error accu-
mulation in long-horizon predictions, and stabilizes optimization.
•Numerical experiments.We systematically evaluate and ablate these components at the oper-
ator level on four representative PDE benchmarks, quantifying gains in accuracy in small-data
regimes, robustness across random seeds, and OOD generalization.
The rest of the paper is organized as follows. Section 2 reviews LNO and introduces ALNO. Sec-
tion 3 presents PILNO, including physics residuals, virtual inputs, and temporal-causality weighting.
Section 4 reports numerical results on four representative examples: Burgers’ equation (initial condi-
tion→solution mapping), Darcy flow (coefficient→solution mapping), reaction–diffusion system
(forcing→solution mapping), and a forced Korteweg-de Vries (KdV) equation (forcing, boundary,
initial condition combined→solution mapping) together with ablation studies on data efficiency
and OOD generalization under a common evaluation protocol. Section 5 concludes with a summary,
limitations, and directions for future work.
2. Problem setting and Laplace Neural Operator Backbone
This section first formalizes the PDE problem setting and notation, then reviews the Laplace
Neural Operator (LNO), and finally introduces the proposed Advanced LNO (ALNO) that serves as
the backbone for PILNO.
2.1. Problem setting and operator learning formulation
LetD ⊂R d be a spatial domain andt∈[0, T]a time horizon. We consider (possibly parameter-
ized) time-dependent PDEs of the form
∂u
∂t +N[u;c] =finD ×(0, T],
B(u) = 0on∂D ×(0, T],
u(·,0) =u 0,
(1)
whereu:D ×[0, T]→R m is them-dimensional solution field,Nis a (possibly nonlinear) differ-
ential operator,fis a forcing term, andBis a boundary operator (periodic or Dirichlet/Neumann,
depending on the problem). We denote the initial condition byu 0 and collect the problem data in
a= (c, u 0, f)∈ A, wherecrepresents PDE coefficients andAis the admissible input space.
The PDE (1) induces a solution operator
G:A → U, a= (c, u 0, f)7→u=G(a),(2)
whereUdenotes a suitable space of spatio-temporal fields onD×[0, T](e.g.U=C([0, T];L 2(D;R m))).
We approximateGby a parametric neural operatorG θ :A → Uwith learnable parametersθ∈Θ:
ˆu=Gθ(a), θ∈Θ,(3)
4
```

## PDF page 5

```text
and, for brevity, we henceforth omit the explicit dependence ofc, u 0, fona.
LetS data ={(a i, ui)}Ndata
i=1 be a paired dataset, where eacha i ∈ Acollects the coefficients, initial
conditions, and forcing for a given PDE instance, andui ∈ Uis the corresponding reference solution.
In the purely data-driven setting,θis learned by minimizing the empirical loss
Ldata(θ) = 1
Ndata
NdataX
i=1
Gθ(ai)−u i2
(4)
where∥ · ∥denotes the discreteL 2 norm over the space-time grid. We denote byθ ∗ a minimizer of
Ldata overΘ. In Section 3, we extend this data-driven operator learning formulation to a physics-
informed setting.
2.2. Laplace Neural Operator
We briefly recall the Laplace Neural Operator (LNO) of Cao et al. [25]. For notational simplicity,
in this subsection we focus on the special case where the only varying input is the forcing termf,
and the PDE coefficientscand the initial conditionu 0 are fixed. First, the inputf∈R dx is lifted to
a higher-dimensional representationv=P(f)∈R dz by a lift operatorP. Then, a single LNO layer
computes
u1(t) =σ
 
(Kv)(t) +Wv(t)

, n= 1,2, . . . , d
whereσis a nonlinear activation,Wis a linear transformation, andKis a kernel integral operator
(Kv)(t) =
Z t
0
κ(t−τ)v(τ) dτ= (κ∗v)(t),(5)
under the simplifying assumption that the kernel is translation invariant,κ(t, τ) =κ(t−τ). Applying
the Laplace transform to the kernel integral of (5) yields
U1(s) =L{(κ∗v)(t)}(s) =K ϕ(s)V(s),(6)
whereV(s) =L{v}(s). Here,K ϕ(s)is directly parameterized by
Kϕ(s) =
NX
n=1
βn
s−µ n
,(7)
with learnable poles{µ n}N
n=1 and residues{β n}N
n=1 (collectivelyϕ= (µ 1, . . . , µN , β1, . . . , βN)),
whereNdenotes the number of system modes. If we expand the input as a sum of exponentials
v(t) =
X
ℓ
αℓeiωℓt,(8)
then applying the inverse Laplace transform to (6) leads to an explicit time-domain decomposition
(Klnov)(t) =L −1 {U1(s)}(t)
=
NX
n=1
 ∞X
ℓ=−∞
βnαℓ
µn −iω ℓ

eµnt
| {z }
transient
+
∞X
ℓ=−∞
 NX
n=1
αℓβn
iωℓ −µ n

eiωℓt
| {z }
steady-state
.(9)
5
```

## PDF page 6

```text
The first term corresponds to a transient response governed by the system poles{µ n}, while the
second term captures the steady-state response operated in the frequency domain. After applying the
LNO layer iteratively, we use a projection operatorQ:R dz → Uto map the final latent representa-
tion back to the solution space. The same construction extends to more general inputsa= (c, u 0, f)
by lifting all components into the latent representation.
2.3. Advanced Laplace Neural Operator (ALNO): decoupled transient-steady branches
The Laplace layer output in Eq. (9) decomposes the response into a transient and a steady-state
term. This pole-residue representation provides a physically interpretable parameterization and en-
ables LNO to capture non-periodic signals and rich transient dynamics more effectively than purely
Fourier-based operators. However, because both components are tied to the same pole–residue pa-
rameterization, the original LNO can be overly restrictive in deeper architectures and limit the repre-
sentation of complex dynamics, as we also observe empirically in Appendix A. To increase flexibility
while preserving interpretability, we retain the transient component in pole–residue form, where the
poles encode characteristic time scales, and replace the steady component with a learnable Fourier
multiplierH(ω)in the spirit of FNO [5].
We next present a complete mathematical formulation of the idea—previously outlined in the
supplementary material of our work [25]—that the steady-state term of the LNO can be expressed
as a Fourier multiplier. Applying the Fourier transform to the kernel integral in Eq. (5) gives
˜U1(ω) =F {(k∗v)(t)}(ω) =F {κ}(ω) ˜V(ω) = ˜Kϕ(ω) ˜V(ω),(10)
where ˜V(ω) =F {v}(ω)and ˜Kϕ(ω) =F {κ}(ω)denotes the Fourier transform of the kernel.
Formally, by evaluating the Laplace transfer function on the imaginary axis, we recover this Fourier
multiplier via
˜Kϕ(ω) =K ϕ(iω)(11)
Using the expansionv(t) = P
ℓ αℓeiωℓt, we have ˜V(ω ℓ) =α ℓ, and on a discrete frequency grid{ω ℓ}
we obtain
˜U1(ωℓ) =K ϕ(iωℓ) ˜V(ω ℓ) =K ϕ(iωℓ)αℓ (12)
Finally, the inverse discrete Fourier transform yields
F −1{ ˜U1(ω)}(t) =
∞X
ℓ=−∞
˜U1(ωℓ)e iωℓt =
∞X
ℓ=−∞
αℓKϕ(iωℓ)e iωℓt.(13)
rewritingK ϕ(iωℓ)by Eq. (7) yields
F −1{ ˜U1(ω)}(t) =
∞X
ℓ=−∞
αℓKϕ(iωℓ)e iωℓt =
∞X
ℓ=−∞
 NX
n=1
αℓβn
iωℓ −µ n

eiωℓt (14)
6
```

## PDF page 7

```text
The representation in Eq. (14) coincides with the steady-state term in Eq. (9). Consequently, an FNO
layer with Fourier multiplierH(ω)acting as
(Kfnov)(t) =F −1
H(ω)F {v}(ω)

(t)
recovers the steady–state branch of LNO whenH(ω)is chosen to approximateK ϕ(iω). In this
sense, the LNO steady–state response can be viewed as a particular Fourier neural operator, while
LNO augments it with an additional transient branch governed by the learned poles{µ n}.
These observations motivate the Advanced LNO (ALNO), in which we explicitly decouple the
two branches:
(Kalnov)(t) =
NX
n=1
 ∞X
ℓ=−∞
βnαℓ
µn −iω ℓ

eµnt +F −1
h
H(ω)F {v}(ω)
i
.(15)
In ALNO, the transient branch remains a pole–residue system with learnable poles{µn}and residues
{βn}, while the steady branch is implemented as an FNO-style spectral convolution via a flexible
multiplierH(ω). This decoupled design preserves the interpretability of LNO through explicit tran-
sient poles, while the more expressive spectral steady branch supports deeper and more accurate
operator models.
3. Physics-Informed Laplace Neural Operator (PILNO)
Building on the ALNO backbone introduced in Section 2, we define the Physics-Informed
Laplace Neural Operator (PILNO), which augments ALNO with physics-informed training. Beyond
standard PDE/BC/IC residuals, PILNO further leverages label-free “virtual inputs” and a temporal-
causality weighting scheme to improve data efficiency and robustness. In the following, we detail
the physics-informed objective, the construction of the virtual-input ensemble, and the temporal-
causality weighting scheme.
In addition, PILNO combines supervised data (if available) with physics/BC/IC residuals:
L=λ pdeLpde +λ bcLbc +λ icLic +λ dataLdata| {z }
if available
with definitions deferred to Sec. 3.1.
3.1. Physics-informed residuals
We first define the physics-informed training objective. Following prior physics-informed opera-
tor learning methods [4, 35, 37], we evaluate PDE and BC/IC residuals directly on model predictions—
via automatic differentiation or consistent finite differences—thereby turning the governing physics
into additional supervision signals.
A physics-only regime—training solely on PDE/BC/IC residuals without paired input-output
data—is possible; however, when paired datasets are available, the data term typically supplies
7
```

## PDF page 8

```text
stronger, lower-variance gradients and a smoother optimization landscape. Given a paired dataset
Sdata ={(a i, ui)}Ndata
i=1 , the data, PDE, boundary, and initial condition losses are defined as follows:
Ldata(θ) = 1
Ndata
NdataX
i=1
ui
θ −u i2
2,(16)
Lpde(θ) = 1
Ndata
NdataX
i=1

∂ui
θ
∂t +N[u i
θ;c i]−f i

2
2
,(17)
Lic(θ) = 1
Ndata
NdataX
i=1
ui
θ(·,0)−u i(·,0)
2
2 ,(18)
Lbc(θ) = 1
Ndata
NdataX
i=1
B
 
ui
θ
2
2,(19)
whereu i
θ =G θ(ai). The base physics-informed objective is then
L(θ) =λ dataLdata +λ pdeLpde +λ icLic +λ bcLbc.(20)
A purely physics-driven regime is recovered by settingλdata = 0, in which case no solution labelsu i
are available. By employing the above training loss, we can directly embed the governing physics
into the training objective, thereby improving the model’s learning performance.
Fig. 1:Schematic of PILNO architecture.Given input dataa, a lifting operatorPembeds the input into a higher-
dimensional latent space; the temporal module applies an advanced laplace layer, and a projection mapQreturns the
output field. Training uses supervised data (when available) together with physics-based losses: PDE residuals (via
derivatives such asu t, ux, uxx) and boundary/initial-condition penalties. The total objective combines data loss with
PDE residuals to enforce the governing equations during training.
3.2. Virtual inputs
Generating paired data (inputs with ground-truth solutions) is often expensive: each sample may
require costly experiments or high-fidelity time-dependent simulations. In practice, this typically
8
```

## PDF page 9

```text
places neural operators in a small-data regime, where only a limited set of initial/forcing condi-
tions and coefficients are observed. In such settings, we would like physics-informed training to
compensate for the lack of labels and stabilize learning.
However, when physics residuals are applied only to this small paired dataset, the supervision is
effectively restricted to the narrow spectrum of inputs present in those samples (e.g., a limited range
of correlation length-scales). We observe that this can bias the operator toward those few configura-
tions, leading to overfitting and degraded generalization—both on out-of-distribution (OOD) inputs
and even on trained distribution test cases. In other words, naive physics-informed training does
not by itself resolve the small-data problem and may even reinforce the spectral bias of the training
distribution.
To decouple physics supervision from label availability, we make virtual inputs a central com-
ponent of PILNO. We construct an unlabeled input ensemble—“virtual inputs”—by randomly sam-
pling admissible problem dataa(typically the initial condition, and when relevant the forcing and
PDE coefficients) at negligible cost, without computing the corresponding reference solutions. Let
a= (u 0, f,B)∈ Adenote problem data. We draw virtual inputsa virt ∼P virt from a prescribed distri-
bution (e.g., Gaussian random fields with controlled spectrum/energy). Unlike prior works [35, 37],
we designP virt so that the ensemble spans broad spectral ranges (e.g., varying correlation length-
scales), explicitly training the operator to remain accurate across out-of-distribution regimes rather
than only within a narrow training distribution.
LetL data,L pde,L ic,L bc be defined as in Section 3.1. During training, each mini-batch mixes
paired and virtual samples. Paired samples(a i, ui)contribute both data and physics losses. Virtual
samplesa j
virt contribute only physics terms,
Lvirt
pde(θ) = 1
Nvirt
NvirtX
j=1
 ∂uj
θ
∂t +N[u j
θ;c j]−f j

2
2
,(21)
Lvirt
ic (θ) = 1
Nvirt
NvirtX
j=1
uj
θ(·,0)−u j
0
2
2,(22)
Lvirt
bc (θ) = 1
Nvirt
NvirtX
j=1
B(uj
θ)
2
2,(23)
and the total objective is
L(θ) =λ dataLdata +λ pde
 
Lpde +L virt
pde

+λ ic
 
Lic +L virt
ic

+λ bc
 
Lbc +L virt
bc

.(24)
Because virtual inputs are label-free, we can generate them abundantly and diversify their spec-
tra, which (i) supplies rich supervision at negligible cost, (ii) improves data efficiency in the small-
data regime, and (iii) strengthens OOD generalization by exposing the model to a deliberately
widened range of input spectra during training. Conversely, when virtual inputs are absent and
9
```

## PDF page 10

```text
physics residuals are applied only to a small set of paired instances, the supervision concentrates
on a narrow input spectrum; empirically, we observe that this exacerbates overfitting and degrades
generalization in the small-data regime (see Section 4.2).
3.3. Temporal causality weighting
When computing physics losses for time-dependent PDEs, it is important to respect temporal
causality: minimizing the residual at late times can be misleading if early-time predictions remain
inaccurate, because early discrepancies can dominate downstream dynamics (“late-time masking”).
Following causal training strategies [7, 45], we introduce temporal-causality weighting (TCW),
which biases the physics residual toward early times so that the model first fits the short-time evo-
lution before learning later states. This choice can also be interpreted from an operator viewpoint
through error propagation under repeated composition of rollout-based operators.
Lpde(θ;a i) =

∂ui
θ
∂t +N[u i
θ]

2
=
KX
k=0

∂ui
θ
∂t (·, tk) +N[u i
θ](·, tk)

2
=
KX
k=0
Lr(tk, θ;a i)
(25)
We denote byL r(tk, θ;a i)the per-time-step residual at timet k, so thatL pde is the sum of these
per-time-step terms over the temporal grid. To enforce temporal causality, we reweight these con-
tributions by a positive, monotonically decreasing schedulew k :=w(t k). We then normalize the
weights so that their average is one, which keeps the overall loss scale stable:
˜wk = wk
1
K+1
PK
j=0 wj
, k= 0, . . . , K.
Finally the causal PDE loss is defined as
Lcausal
pde (θ;a i) =
KX
k=0
˜wk Lr(tk, θ;a i).(26)
Typical choices forw(t)include
(Exp)w(t) =e −γt,(Inv)w(t) = 1
1 +αt ,(Piecewise)w(t) =



wmax, t≤t 0,
wmin, t > t 0,
(27)
with hyperparametersγ, α >0,w max > wmin >0, and a cutofft 0. Adaptive weighting based on
gradients or scale of each per-time-step residual is also possible.
Temporal causality weighting (TCW) stabilizes optimization for time-dependent PDEs by em-
phasizing early-time residuals, preventing late-time minimization from masking early errors. In
10
```

## PDF page 11

```text
practice, combining TCW with the physics residual and (optionally) multi-resolution collocation
yields faster and more stable training, and improves long-horizon accuracy in the benchmarks of
Section 4.
On the other hand, from an operator perspective, consider a discrete-time flow mapu(·, t k+1) =
S∆t(u(·, tk))(a semigroup in the autonomous case), and a learned one-step operatorR θ used in
rollout formu θ(·, tk+1) =R θ(uθ(·, tk)). Writing the rollout errore k :=u θ(·, tk)−u(·, t k)and
the one-step defectδ k :=R θ(u(·, tk))− S ∆t(u(·, tk)), a first-order decomposition yieldse k+1 =
Rθ(uθ(·, tk))− R θ(u(·, tk)) +δ k ≈J kek +δ k, whereJ k =∂R θ/∂uis the Jacobian evaluated along
the trajectory. Unrolling this recursion exposes the multiplicative (product) structure induced by
composition:
eK ≈
 K−1Y
j=0
Jj
!
e0 +
K−1X
k=0
 K−1Y
j=k+1
Jj
!
δk,(28)
so defects incurred at early times are propagated through longer Jacobian products and can dom-
inate long-horizon error. In particular, ifR θ is (locally)L-Lipschitz, we can induce
∥eK∥ ≤L K∥e0∥+
K−1X
k=0
LK−1−k ∥δk∥,(29)
showing that early-time defects can have a larger downstream influence due to repeated composi-
tion. Although PILNO is not an explicit autoregressive rollout model (it predicts the full space-time
field in one forward pass), our physics loss still decomposes across time slices (Eq. (25)); without
temporal causality weighting, optimization can reduce late-time residuals while leaving early-time
inconsistencies that would dominate under causal evolution. TCW serves as a tractable surrogate for
these downstream sensitivity factors by prioritizing early-time residuals, thereby promoting causally
coherent long-horizon predictions.
Figure 1 presents a schematic of PILNO’s core architecture. In addition, Algorithm 1 details the
training workflow, including how virtual inputs are integrated and how temporal-causality weighting
is applied within the physics-informed loss.
To mitigate overfitting and enhance generalization performance, we construct a physics dataset
by augmenting the labeled training inputsawith virtual inputsa virt. Formally,
{ak
phy}Ntrain+Nvirt
k=1 :={a i}Ntrain
i=1 ∪ {aj
virt}Nvirt
j=1 .
We then evaluate the physics-based lossesL pde,L bc,L ic on{a k
phy}, while the data lossL data is com-
puted only on the labeled subset{(a i, ui)}Ntrain
i=1 .
4. Numerical Results
Experimental setup and baselines.We evaluate PILNO in the small-data regime and under out-
of-distribution (OOD) tests on four canonical PDE benchmarks. Throughout all experiments, we
11
```

## PDF page 12

```text
Algorithm 1Training procedure for PILNO
Input:training set{(a i, ui)}Ntrain
i=1 , virtual inputs{a j
virt}Nvirt
j=1 (optional), weightsλ data, λpde, λbc, λic,
temporal weightsw k =w(t k)(optional)
1:Construct physics set{a k
phy}={a i} ∪ {aj
virt}
2:Initialize parametersθ
3:forepoch= 1, . . . , Edo
4:foreach batcha phy from physics setdo
5:Sample (optionally) paired batch(a, u)from training set
6:Compute predictionu θ =G θ(aphy)
7:iftemporal causality weighting is usedthen
8:ℓ pde ← Lcausal
pde (θ;a phy)
9:else
10:ℓ pde ← Lpde(θ;a phy)
11:Computeℓ bc, ℓic ona phy
12:ifpaired labels are available in batchthen
13:ℓ data ← Ldata(θ;a, u)
14:else
15:ℓ data ←0
16:ℓ total ←λ dataℓdata +λ pdeℓpde +λ bcℓbc +λ icℓic
17:Updateθusing∇ θℓtotal
instantiate the Advanced Laplace Neural Operator (ALNO) from Section 2 as the purely data-driven
backbone, and build PILNO on top of the same architecture by adding physics-informed training,
virtual inputs, and temporal-causality weighting. For notational convenience, we refer to this ALNO
baseline simply as ’LNO’ unless otherwise specified. As summarized in Table 1, PILNO achieves
substantially lower relativeL 2 error than the LNO backbone in small-data settings (N train = 25for
Burgers and reaction–diffusion,N train = 10for Darcy flow, andN train = 27for forced KdV). Across
all benchmarks, we enforce PDE/BC/IC residuals for PILNO and, when enabled, virtual inputs
and temporal-causality weighting to further enhance stability and robustness for time-dependent
problems: virtual inputs and temporal-causality for Burgers’ equation, reaction-diffusion equation,
and forced KdV equation, virtual inputs for Darcy flow.
Tasks and operator mappings.We consider four representative operator-learning tasks that span
both time-dependent and steady-state problems and probe different types of input operators.
• Burgers’ equation: learn the mapping from the initial conditionu 0(x)to the spatio-temporal
solutionu(x, t), i.e.,u 0 7→u(·,·).
• Darcy flow: learn the mapping from the coefficient/permeability fielda(x)to the steady pres-
sure solutionu(x), i.e.,a7→u(·).
• Reaction–diffusion system: mapping either the initial conditionu 0(x)or the forcing profile
f(x)to the spatio-temporal solutionu(x, t).
12
```

## PDF page 13

```text
• forced Korteweg-de Vries equation: learn the mapping from forcing termf x(x, t), initial con-
ditionu 0(x), boundary conditionu(−L, t), u(L, t), u x(L, t), and PDE coefficientsα, βto the
spatio-temporal solutionu(x, t). In short,[f x(x, t), u(L, t), u(−L, t), ux(L, t), u(x,0), α, β]7→
u(x, t).
This suite of benchmarks therefore covers the mappings of the IC→solution, coefficient→solution,
forcing→solution, as well as more complex mixed regimes where initial condition, boundary condi-
tions, coefficients and forcing are provided jointly as inputs to the solution, providing a diverse set
of operator regimes to assess data efficiency and out-of-distribution (OOD) generalization.
Architectures and training protocol.All models are initialized with the Glorot–normal scheme and
trained for up toE= 1000epochs. We use the Adam optimizer with(β 1 = 0.9, β 2 = 0.999),
weight decay10 −4, and a step learning-rate scheduler (step size 100, decay factorγ= 0.5). Unless
otherwise noted, PILNO and LNO share this optimizer and schedule, and are matched in parameter
count to ensure a fair capacity comparison. Problem-specific architectural details (e.g., network
width, number of modes in the spectral layers, and temporal-causality weighting schedules) are
reported in the corresponding subsections for each PDE.
Example RelativeL 2 error
PILNO LNO
Burgers 1.420e-2 9.345e-2
Darcy 1.235e-2 1.467e-1
Reaction-Diffusion 2.877e-2 1.467e-1
forced KdV 1.372e-1 4.479e-1
Table 1: RelativeL 2 errors of PILNO and LNO over 5 experiments on small training data for four PDE problems
(Ntrain = 25for Burgers, Reaction-Diffusion,N train = 10for Darcy flow, andN train = 27for forced KdV).
Data generation and evaluation protocols.For all benchmarks, inputs (initial conditions, coeffi-
cients, and forcings) are sampled from Gaussian random fields with an exponentiated squared–sine
kernel parametrized by a correlation length–scaleℓ. We use two complementary protocols:
• Data-efficiency experiments: To isolate the effect on the number of paired samples, we fix a
single length–scale (typically a relatively oscillatory field, smallℓ) and vary only the training-
set sizeN train. These experiments quantify how rapidly the test error grows as paired data
become scarce.
• OOD generalization experiments: To probe robustness across input statistics, we generate ten
datasets withℓ∈ {0.5,1.0, . . . ,5.0}. For eachℓ train, a model is trained on the correspond-
ing dataset and evaluated on the test sets of allℓ test, yielding a10×10grid of train–test
combinations. The resulting error heatmaps summarize in-distribution (diagonal) and out-of-
distribution (off-diagonal) performance.
13
```

## PDF page 14

```text
The specific choice ofℓused in each data-efficiency plot, and the precise role ofℓ train andℓ test in the
OOD heatmaps, are detailed in the subsections for each PDE.
4.1. Burgers’ equation
The first example uses Burgers’ equation to assess PILNO in terms of data efficiency and out-of-
distribution (OOD) generalization, compared to the purely data-driven LNO. Burgers’ equation is a
prototypical nonlinear PDE arising in fluid mechanics and wave propagation:
∂u
∂t +u ∂u
∂x −ν ∂2u
∂x2 = 0, x∈[0,1], t∈[0,1],
u(t,0) =u(t,1)
(30)
whereu(t, x)denotes the solution field (e.g., velocity) andνis the viscosity coefficient. We set
ν= 0.01for this example.
Reference solutions are generated by a high-fidelity solver: spatial derivatives are approxi-
mated using a fourth-order central finite-difference scheme on a uniform grid with 128 points,
and the resulting semi-discrete system is advanced in time using the classical explicit fourth-order
Runge–Kutta method (RK4) with time step∆t= 10 −4. Initial conditionsu 0 are sampled from a
zero-mean Gaussian random fieldµ=GP(0, k exp-sin), with an exponentiated sine-squared covari-
ance kernel
kexp-sin(x, x′) =σ 2 exp
 
−2 sin2 
π(x−x ′)/p

ℓ2
!
,
withp= 1andσ= 0.2, and a length-scale parameterℓthat controls the spatial smoothness. The
operator-learning models are trained and evaluated on a downsampled space–time grid: the interval
[0,1]is discretized with step sizeh= 1/25, yielding26snapshots{t k}25
k=0, and we useN x = 32
equidistant spatial nodes in[0,1]. Each trajectory is therefore represented on a26×32grid. In all
Burgers’ experiments, the input to LNO/PILNO is the initial conditionu 0(x)and the target is the
corresponding spatio-temporal solutionu(x, t).
Data efficiency of PILNO.To assess performance in the small-data regime, we fix the length-scale
atℓ= 0.5and vary only the number of paired training samplesN train ∈ {25,50,100,150,200}.
For eachN train, LNO and PILNO are trained on identical paired datasets; in addition, PILNO uses
Nvirt = 1000virtual inputs drawn from the same Gaussian random field prior. All reported results
are averaged over five random seeds.
Figure 2 reports the relativeL 2 test error versusN train. AsN train decreases, LNO’s error increases
sharply (reaching approximately9.35%atN train = 25), while PILNO remains much more stable
(about1.42%atN train = 25). In particular, PILNO with25training samples attains a test error
comparable to LNO trained with100samples (roughly1.1%), indicating a substantial gain in data
efficiency. This improvement is attributable to the physics-informed structure and the additional
14
```

## PDF page 15

```text
Fig. 2: RelativeL 2 errors over the number of training samples for Burgers’ equation. Points denote means and shaded
bands indicate±1standard deviation over five random seeds. AsN train decreases, the error of LNO increases sharply
(9.35%atN train = 25), whereas PILNO maintains lower error level (1.42%atN train = 25).
supervision from virtual inputs, which together regularize the operator and curb overfitting in the
small-data regime.
To further illustrate the qualitative behavior, Figure 3 shows time-slice comparisons for the two
test cases on which LNO incurs its largest relativeL 2 errors. For these same initial conditions,
PILNO produces markedly more accurate predictions, tracking the reference solution more faith-
fully. This suggests that the physics-driven training objective in PILNO effectively constrains the
governing physics and helps preserve key spatio-temporal features even under limited supervision.
Fig. 3: Worst–case time–slicing comparisons on the test set for the two LNO cases with the largest relativeL 2 error.
PILNO approximates the reference solution more accurately than LNO.
15
```

## PDF page 16

```text
OOD generalization performance.We next evaluate OOD generalization with respect to the corre-
lation length-scale of the initial condition. We construct ten independent datasets by samplingu0(x)
from the same Gaussian random field at length-scalesℓ∈ {0.5,1.0, . . . ,5.0}. For eachℓ train, we train
LNO and PILNO usingN train = 200paired samples (andN virt = 1000virtual inputs for PILNO),
then evaluate on test sets drawn from all ten length-scalesℓ test. Each(ℓ train, ℓtest)pair defines one cell
in a10×10error heatmap, shown separately for LNO and PILNO in Figure 4.
When trained on smooth initial conditions (ℓ train = 5.0) and tested on highly oscillatory fields
(ℓtest = 0.5), LNO suffers from substantial degradation, with relativeL2 error around23.6%. In con-
trast, PILNO, despite being trained only on smooth data, maintains significantly lower error in this
challenging extrapolation regime (about7%), and exhibits uniformly improved performance off the
diagonal. These results indicate that embedding the governing PDE into the operator-learning objec-
tive, together with virtual inputs that broaden the input spectrum, leads to robust OOD generalization
across a wide range of initial-condition regularities.
Overall, the Burgers’ equation experiments show that PILNO achieves a more favorable trade-off
between accuracy and data efficiency than the purely data-driven LNO. Physics residuals, combined
with virtual inputs, yield more stable training and lower error both in the extreme small-data regime
and under pronounced mismatches between training and test initial-condition statistics.
(a)
 (b)
Fig. 4: Generalization across initial–condition length–scales. Heatmaps show relativeL 2 error when training at
length–scaleℓ train (vertical axis) and testing atℓ test (horizontal axis), for (a) LNO and (b) PILNO. PILNO maintains
low errors even when extrapolating from smooth (ℓ= 5.0) to oscillatory (ℓ= 0.5) regimes. PILNO consistently
demonstrates better generalization, showing robust predictive performance even on data distributions not included dur-
ing training.
16
```

## PDF page 17

```text
4.2. Darcy flow
We next consider the two-dimensional steady-state Darcy flow on the unit squareΩ = (0,1) 2, a
second-order linear elliptic PDE with Dirichlet boundary conditions. This example evaluates PILNO
in the small-data regime and highlights the role of virtual inputs for improving performance when
only a limited number of labeled samples is available. The governing equation is
−∇·
 
a(x)∇u(x)

=f(x)inΩ = (0,1) 2, u(x) =g(x)on∂Ω,(31)
whereu: Ω→Rdenotes the pressure field,a∈L ∞(Ω)is the piecewise–constant permeability
coefficient, andf≡1is a fixed forcing (following [5, 35]). Unless otherwise stated, we take
homogeneous Dirichlet boundary conditiong≡0. The learning task is to approximate the solution
operator from the permeability field to the corresponding pressure solution,
GΘ :a(x)7− →u(x),(32)
using the PILNO training strategy from Section 3 (data loss when available, plus PDE/BC residuals).
Random permeability field and data generation.We follow the data-generation procedure of PINO [5,
35]. First, we sample a mean-zero Gaussian random fieldϕ:D→Ron the periodic domain
D= [0,1]×[0,1]with covariance operator
ϕ(·)∼ N
 
0,(−∆ + 9I) −2
.
The permeability fielda:D→ {3,12}is obtained by a sign-thresholding map
a(x) =ψ(ϕ(x)), ψ(z) =



12, z≥0,
3, z <0.
so that each realization consists of high- and low-permeability regions.
For each sampled permeabilitya, we solve (31) on a fine241×241grid to obtain an accurate ref-
erence solutionu. These fine-grid solutions are used as ground truth for evaluation and to construct
coarse training labels. To mimic a realistic low-resolution data setting, we construct the supervised
training pairs(a, u)on a coarse11×11grid by downsampling the reference solutions. To inject
higher-resolution physics information without requiring fine-grid labels, we additionally evaluate
the PDE residualL pde on an intermediate61×61collocation grid, while the supervised data loss
remains defined only on the11×11grid. Thus, training combines coarse-grid data supervision with
a finer-grid physics loss.
Zero boundary conditions are enforced for all methods by multiplying the mollifier
m(x, y) = sin(πx) sin(πy),
so that the network outputs satisfyu= 0on∂Ωby construction. Unless otherwise noted, we report
the mean and standard deviation of the relativeL2 error over100test instances, evaluated at both the
17
```

## PDF page 18

```text
FNO LNO PIFNO PILNO
RelativeL 2 Error at
low resolution (11×11) 5.41e-2 1.29e-2 5.23e-2 1.19e-2
RelativeL 2 Error at
high resolution (61×61) 9.01e-2 3.73e-2 1.56e-2 1.21e-2
Table 2: RelativeL 2 errors on Darcy flow. All models are trained onN train = 800coarse11×11samples. PIFNO
and PILNO additionally enforce the PDE residual on a finer61×61collocation grid, which substantially improves test
accuracy compared with data-driven baselines trained only on coarse labels.
coarse (11×11) and fine (61×61) resolutions. The primary metric is the relativeL 2 error of the
pressure field.
Table 2 summarizes the performance of FNO, LNO, PIFNO, and PILNO when trained with
Ntrain = 800paired samples. PIFNO and PILNO incorporate the same coarse labels as FNO and
LNO, but also exploit a higher-resolution PDE residual evaluated on the61×61collocation grid.
As a result, their errors remain low even when evaluated on the finer grid (1.56% and 1.21%, re-
spectively), whereas the purely data-driven models suffer noticeable degradation when moving from
11×11to61×61.
Figure 6-(a) shows the relativeL 2 test error as a function of the number of training samples.
Each model is trained five times with different random seeds; points denote means and shaded bands
indicate±1standard deviation. As the number of paired samples decreases, the error of LNO
increases sharply (reaching≈14.7%atN train = 10). In contrast, PILNO maintains low error across
allN train, remaining close to itsN train = 400performance (about1.2%). Figure 5 further compares
LNO and PILNO for the extreme small-data caseN train = 10. Because zero boundary conditions
are enforced as a hard constraint via the mollifier, both methods respect the boundary shape, but
LNO exhibits large interior discrepancies (relativeL 2 ≈14.7%), whereas PILNO closely matches
the reference solution with a relative error of≈1.2%.
Importance of virtual inputs.Figure 6-(b) examines the effect of virtual inputs. As discussed in
Section 3.2, enforcing PDE residuals can improve generalization by injecting the governing physics
into the model. However, when the physics residuals are applied only to the limited set of paired
samples, supervision is confined to a narrow input dataset; in the small-data regime, this can exac-
erbate overfitting and degrade test accuracy. Consistent with this, physics-informed models without
virtual inputs outperform purely data-driven baselines whenNtrain ≳200, but their advantage dimin-
ishes and can even vanish asN train becomes very small. These results highlight that virtual inputs
are crucial for reliable physics-informed operator learning under limited data.
4.3. Reaction-Diffusion equation
We consider a one-dimensional reaction-diffusion equation with a quadratic reaction term
D ∂2u
∂x2 +k u 2 − ∂u
∂t =f(x),(x, t)∈[0,1]×[0,1],(33)
18
```

## PDF page 19

```text
Fig. 5: Comparison atN train = 10(Darcy flow) on61×61resolution. LNO attains a relativeL 2 error of 14.67%, whereas
PILNO achieves 1.23%, indicating substantially better performance by PILNO under extremely limited training data.
whereu(t, x)is a scalar field,D >0is the diffusivity,k≥0the reaction strength, andf(x)
a time-independent forcing. Following prior operator-learning studies (e.g., LNO [25] and PI-
DeepONet [37]), we setD= 0.01andk= 0.01. Depending on the task, we either prescribe a
nontrivial initial conditionu 0(x)with zero forcing, or a nontrivial forcingf(x)with zero initial and
boundary conditions.
We study two operator mappings under a common experimental procedure:
•Task A (IC→solution, zero forcing):learns the mappingu 0(x)7→u(x, t)withf≡0, used
to evaluate out-of-distribution (OOD) generalization.
•Task B (forcing→solution, zero IC/BC):learns the mappingf(x)7→u(x, t)with zero
initial and boundary conditions. This setting is more challenging and is used to probe both
small-data performance and the impact of temporal-causality weighting.
Common discretization and data generation.Reference solutions are generated using the same high-
fidelity solver as in the Burgers’ experiments: spatial derivatives are approximated by a fourth-order
central finite difference scheme on a fine uniform grid withN x = 151points, and the semi-discrete
system is advanced in time using the classical explicit fourth-order Runge-Kutta (RK4) method with
time step∆t=1e-4. The resulting solutions are downsampled to a uniform grid withN x = 51
spatial points andN t = 51time snapshots on[0,1]×[0,1], so that each solution is represented on a
51×51space-time grid. In both tasks, the input to LNO/PILNO is a one-dimensional function (u 0
for Task A,ffor Task B), and the target is the corresponding solutionu(x, t)on this grid.
19
```

## PDF page 20

```text
(a)
 (b)
Fig. 6: Error plots on number of training samples and the role of virtual inputs for Darcy flow. (a) RelativeL 2 test
error versus the number of training samples for LNO and PILNO. Points denote means and shaded bands indicate±1
standard deviation over five random seeds. AsN train decreases, the error of LNO rises sharply (reaching≈14.7%at
Ntrain = 10), whereas PILNO maintains low error levels (around1.2%across allN train). (b) Effect of removing virtual
inputs. When physics-informed models are trained without virtual inputs (i.e., physics residuals applied only to paired
data), PILNO outperform purely data-driven baselines only for larger training sets (N train ≳200). For smaller training
sets (Ntrain ≲200), this advantage diminishes or even disappears, yielding errors comparable to data-driven methods
and underscoring the importance of virtual inputs in the small-data regime.
For both tasks, input functions are sampled from the same Gaussian process family used in
the Burgers’ example, namely a zero-mean Gaussian random field with exponentiated squared sine
kernel. For each correlation length-scaleℓ >0,
u0(·)∼ GP
 
0, k(ℓ)
exp-sin

, f(·)∼ GP
 
0, k(ℓ)
exp-sin

,
with covariance
k(ℓ)
exp-sin(x, x′) =σ 2 exp
 
−2 sin2 
π(x−x ′)/p

ℓ2
!
,
where we fixp= 1andσ= 0.2. For Task A, this kernel is used to sample initial conditionsu 0 with
f≡0; for Task B, it is used to sample forcingsfwithu 0 ≡0and homogeneous Dirichlet boundary
conditions enforced via a mollifier.
Similar to the Burgers’ experiments, we consider two complementary evaluation regimes. For
data-efficiency studies, we fix a representative length-scale (hereℓ= 0.5) and vary only the number
of paired training samplesN train, while keeping the test distribution and test set size fixed. For OOD
generalization, we construct ten datasets, one for each length-scaleℓ∈ {0.5,1.0, . . . ,5.0}, and for
a givenℓ train we train a model onN train samples drawn at that length-scale and evaluate on test sets
drawn at allℓ test. Each(ℓ train, ℓtest)pair thus defines a cell in a10×10error matrix, reported separately
for Tasks A and B. Unless otherwise stated, we useN virt = 500virtual inputs for PILNO.
Task A (IC→Solution; zero forcing).For Task A we setf≡0, so that (33) reduces to
D ∂2u
∂x2 +k u 2 − ∂u
∂t = 0,(x, t)∈[0,1]×[0,1],
20
```

## PDF page 21

```text
with periodic boundary conditionsu(0, t) =u(1, t). The operator to be learned is
GA
Θ :u 0(x)7→u(x, t).
To assess OOD performance under limited paired data, we generate datasets at ten correlation length-
scalesℓ∈ {0.5,1.0, . . . ,5.0}. For eachℓ train, we train a model usingN train = 25paired samples and
evaluate onN test = 100test instances at allℓ test. Each(ℓ train, ℓtest)pair defines one cell in the10×10
heatmaps in Fig. 7.
Figure 7 compares LNO and PILNO on this length-scale grid. For example, when trained on
smooth initial conditions (ℓ train = 5.0) and tested on highly oscillatory ones (ℓ test = 0.5), LNO
attains a relativeL 2 error of about33.6%, whereas PILNO reduces the error to approximately6.9%.
This demonstrates that PILNO provides substantially more robust OOD generalization than LNO
under the same limited amount of paired data.
(a)
 (b)
Fig. 7: Generalization across initial–condition length–scales for reaction-diffusion equation. Heatmaps show relative
L2 error when training at length–scaleℓ train (vertical axis) and testing atℓ test (horizontal axis), for (a) LNO and (b)
PILNO. PILNO sustains lower errors off the diagonal (mismatched smooth/oscillatory regimes), demonstrating stronger
out–of–distribution generalization.
Task B (Forcing→Solution; zero IC/BC).For Task B, we impose zero initial and boundary condi-
tions and learn the mapping from a spatial forcing profile to the full spatio-temporal solution, as in
PI-DeepONet [37]:
GB
Θ :f(x)7→u(x, t).
We use the same51×51space–time grid as in Task A. The inputs are forcingsf(x)sampled from
the GP family above, and the output is the corresponding solutionu(x, t). Zero initial and boundary
conditions are enforced via the mollifier
m(x, t) = sin(πx) sin(0.5πt),
21
```

## PDF page 22

```text
analogously to the Darcy-flow experiment.
Fig. 8: RelativeL 2 error on the test set versus the number of training samples (mean±std over 5 random seeds). As
Ntrain decreases, LNO’s error rises sharply, whereas PILNO degrades more gracefully (e.g.,≈2.5%atN train = 25).
Fig. 9: Comparison atN train = 25underℓ train =ℓ test = 0.5(reaction-diffusion). LNO attains a relativeL 2 error of
14.6%, whereas PILNO achieves 2.5%, indicating substantially better performance by PILNO under extremely limited
training data.
To study data efficiency in an in-distribution setting, we fixℓ train =ℓ test = 0.5and varyN train ∈
{25,50,100,150,200}, reporting mean±standard deviation over five random seeds. Figure 8 shows
22
```

## PDF page 23

```text
the resulting test errors: LNO’s error increases sharply asN train decreases (reaching roughly14%
atN train = 25), whereas PILNO degrades much more gracefully and remains near2.5%even at
Ntrain = 25. Figure 9 illustrates the extreme small-data caseN train = 25atℓ= 0.5: although
both methods satisfy the enforced zero IC/BC by the mollifier, LNO exhibits substantial interior
discrepancies (relativeL 2 ≈14.7%), whereas PILNO, aided by physics residuals, virtual inputs,
and temporal-causality weighting, closely matches the reference solution (relativeL 2 ≈2.5%).
(a)
 (b)
Fig. 10: Generalization across forcing term length–scales for reaction-diffusion equation. Heatmaps show relative
L2 error when training at length–scaleℓ train (vertical axis) and testing atℓ test (horizontal axis), for (a) LNO and (b)
PILNO. PILNO sustains lower errors off the diagonal (mismatched smooth/oscillatory regimes), demonstrating stronger
out–of–distribution generalization.
For OOD generalization, we generate datasets at the ten correlation length-scalesℓ∈ {0.5,1.0, . . . ,5.0},
train a separate model withN train = 25at eachℓ train, and evaluate onN test = 100test instances at
allℓ test. The resulting10×10error matrices are shown in Fig. 10. In this small-data regime, the
forcing-to-solution mapping is substantially more challenging than the IC-to-solution case: for Task
A, diagonal entries (ℓtrain =ℓ test) yield errors on the order of1%, whereas for Task B the correspond-
ing LNO errors exceed10%. Nevertheless, PILNO attains uniformly lower errors across the grid,
maintaining small diagonal errors and remaining robust when extrapolating from smooth forcings
(largeℓ train) to highly oscillatory forcings (smallℓtest). Representative line plots for selected train-test
pairs are given in Fig. 11, where PILNO consistently tracks the reference solution more closely than
LNO.
Importance of temporal-causality weighting.Consistent with Section 3.3, incorporating temporal
causality is crucial for learning time-dependent PDEs. Figure 12 compares LNO, PILNO (with
TCW), and PILNO without TCW atN train = 25andℓ train = 0.5, reporting validation relativeL 2
23
```

## PDF page 24

```text
Fig. 11: Comparison of PILNO and LNO on the reaction-diffusion equation under three train-test length scale config-
urations. Left:ℓ train = 0.5, ℓ test = 0.5. Middle:ℓ train = 5.0, ℓ test = 0.5. Right:ℓ train = 5.0, ℓ test = 5.0. Across all
cases, PILNO produces predictions that more closely match the reference solution than LNO, as evidenced by the visual
agreement of the predicted profiles with the reference.
error versus training epochs. In this small-data setting, LNO plateaus near14%, which is reasonable
because its purely data-driven structure. Adding PDE constraints (PILNO) lowers the error, and
TCW further improves both final accuracy and convergence: PILNO+TCW reaches≈2.3%of
validation error, whereas PILNO without TCW settles around3.5%to4.0%. The steeper decay of
the PILNO with TCW model indicates faster optimization.
Figure 13 compares the distribution of relativeL 2 errors over 100 test cases for PILNO with
and without TCW. Each blue dot corresponds to a single test error from PILNO with TCW, while
green crosses denote errors from PILNO without TCW; red markers summarize the mean and one
standard deviation for each model. PILNO with TCW achieves a lower mean error (2.42%) than
its counterpart without TCW (3.90%), and its error distribution is more tightly concentrated, with
smaller standard deviation (1.47×10 −2 versus3.18×10 −2). This indicates that temporal-causality
weighting not only improves average prediction accuracy but also reduces variability across test
instances, leading to more reliable performance. Taken together, these results show that enforcing
temporal causality yields more accurate and stable training for time-dependent PDEs.
4.4. Forced KdV equation
We finally consider the one-dimensional forced Korteweg-de Vries (KdV) equation, a nonlin-
ear dispersive PDE with external forcing, to compare PILNO against the DeepOMamba [46], the
strong spatio-temporal operator learning model. This example evaluates an in-distribution data effi-
24
```

## PDF page 25

```text
Fig. 12: Validation relativeL2 error versus training epochs for the reaction-diffusion equation withNtrain = 25. Although
all three models reduce the validation error as training progresses, the purely data-driven LNO saturates at approximately
18%under this limited data regime. In contrast, PILNO achieves substantially lower error, and the inclusion of temporal
causality weighting further reduces the validation error to about2.5%, compared with roughly4%for PILNO without
temporal causality weighting.
ciency study. We adopt the same benchmark setting and data-generation procedure used in DeepO-
Mamba [46], and evaluate data efficiency by varying the number of paired training samples.
PDE formulation and operator-learning task.Following the same formulation adopted in DeepO-
Mamba [46], the forced KdV equation is
∂u
∂t +u ∂u
∂x +β ∂3u
∂x3 =α ∂f
∂x ,(x, t)∈(−L, L)×(0, T),(34)
withL= 5andT= 5. For well-posedness, the system is associated with three boundary conditions
u(L, t),u(−L, t), andu x(L, t)fort∈(0, T), together with an initial conditionu(x,0)forx∈
(−L, L). The operator learning objective is to map the initial-boundary conditions, the external
forcingf x(x, t), and PDE coefficients(α, β)to the full spatio-temporal solutionu(x, t)over the
entire domain.
GΘ : [u(L, t), u(−L, t), u x(L, t), u(x,0), f x(x, t), α, β]7− →u(x, t),(35)
Data generation and discretization.Following the data generation procedure of DeepOMamba [46],
we generate datasets from three analytic one-soliton solution families (Types A-C) with equal pro-
portions. All inputs and outputs are discretized on a uniform100×100space-time grid over
(x, t)∈(−5,5)×(0,5). We first generate a full training pool of 27K instances (one third per
type), and fix the validation and test sets toNval = 3000andN test = 3000instances, respectively. To
25
```

## PDF page 26

```text
Fig. 13: Distribution of relativeL 2 errors over 100 test cases for PILNO and PILNO without TCW. Blue dots indicate
the relativeL 2 errors of PILNO, green crosses indicate those of PILNO without TCW, and red markers denote the mean
error of each model with caps representing one standard deviation. PILNO and PILNO without TCW achieve mean
relativeL 2 errors of 2.42% and 3.90%, with standard deviations of1.47×10 −2,3.18×10 −2, respectively, indicating
that PILNO attains both a lower average error and reduced variability.
evaluate data efficiency in the small-data regime, we construct training data by subsampling from
the 27K training pool withN train ∈ {2700,270,135,54,27}, always drawing equal numbers from
Types A-C (e.g.,900/900/900samples from Type A, B, and C atN train = 2700).
Models and training protocol.DeepOMamba.We use the DeepOMamba architecture and forced-
KdV hyperparameter choices reported in DeepOMamba [46]. Details of data generation proce-
dure and model structure are provided in Appendix D.PILNO.We instantiate PILNO with the
same LNO/ALNO backbone used throughout this paper but with model depth of 2, and train it
with data loss and physics-informed residual losses. For forced KdV , the physics term enforces
Eq. (34), together with residual penalties for the required IC/BC constraints. In addition, PILNO
usesN virt = 1800virtual inputs drawn from the same procedure stated above and uses temporal-
causality weighting to stabilize time-dependent training.
For a fair comparison under the DeepOMamba benchmark, both models are trained using the
same train/validation splits. We report the relativeL 2 error on the test set, averaged over five ran-
dom seeds (mean±std). Figure 14 reports the test error as a function of the number of training
samples,N train, providing a systematic assessment of performance across large sample and small
sample regimes. AtN train = 2700, DeepOMamba achieves a test error of 3.24% compared with
6.89% for PILNO, showing the advantage of fully supervised spatio-temporal operator learning in
the data-abundant regime for time-dependent PDEs. AsNtrain is reduced, however, PILNO exhibits a
26
```

## PDF page 27

```text
Fig. 14: RelativeL 2 error on the test set versus the number of training samples (mean±std over 5 random seeds).
As the number of training samples decreases fromN train = 2700toN train = 27, the error of DeepOMamba increases
sharply from3.24%to47.13%, whereas PILNO’s error rises only moderately from6.89%to13.72%.
markedly more graceful degradation, which is consistent with the regularizing effect of physics loss
and virtual inputs in the small-data regime. This divergence is most evident atNtrain = 27, where the
paired training set is extremely limited: PILNO achieves a test error of 13.72%, whereas DeepO-
Mamba’s error increases sharply to 47.13%. Moreover, PILNO exhibits more stable performance in
this extreme low-data setting, with a substantially smaller standard deviation atN train = 27(0.48%)
than DeepOMamba (2.94%).
For qualitative visualization, we randomly sampled one representative test instance per solution
type (A/B/C) from the intersection of test cases whose per-instance relativeL 2 errors for DeepO-
Mamba and for PILNO each fall within±2percentage points of the corresponding model’s mean
test error. We then visualize the forcing, the reference solution, and the predictions (and absolute
errors) of both DeepOMamba and PILNO for the same instances. Figure 15 provides qualitative
comparisons in the small-data regime (N train = 27) across three representative forcing categories
(Types A–C). For each case, we report the input forcing, the corresponding reference solution, and
the predictions produced by DeepOMamba and PILNO. Across all types, PILNO exhibits closer
agreement with the reference solution than DeepOMamba, more faithfully capturing the evolution
of the solution and its salient spatiotemporal structures. Figure 16 presents, for the same cases as in
Figure 15, the input forcing, the reference solution, and the absolute error fields for DeepOMamba
and PILNO. The error visualizations further indicate that PILNO achieves higher fidelity reconstruc-
tions, with markedly smaller absolute errors over the domain relative to DeepOMamba.
Overall, this benchmark highlights a clear trade-off between fully supervised spatio-temporal op-
27
```

## PDF page 28

```text
Fig. 15: Qualitative comparison of DeepOMamba and PILNO atN train = 27on representative test instances. The
instances are randomly sampled from those whose errors fall within a±2%band around the mean error of DeepOMamba
and, simultaneously, within a±2%band around the mean error of PILNO. Rows correspond to Types A, B, and C (top
to bottom). Columns show the input forcingf(x, t), the corresponding reference solution, the DeepOMamba prediction,
and the PILNO prediction (left to right). The per-instance relativeL 2 error for DeepOMamba are 45.36%, 48.50%, and
45.71% for Type A, B, and C, respectively, while those for PILNO are 10.90%, 12.30%,14.14% on the same instances.
erator learning and physics-informed regularization. DeepOMamba attains the best accuracy when
paired supervision is abundant, whereas PILNO delivers substantially improved data efficiency and
stability as paired data become scarce, consistent with the combined effect of residual constraints,
virtual inputs, and temporal-causality weighting. Since both training and testing are drawn from
the same analytic families (Types A–C), these results should be interpreted as an in-distribution
data-efficiency and robustness study rather than an evaluation of out-of-distribution generalization.
Note that, under the same labeled (paired) data budget, PILNO further exploits the known gov-
erning equation through PDE/IC/BC residual losses (and, when enabled, additional virtual inputs
and temporal-causality weighting); accordingly, the comparison is intended to quantify the practical
benefit of physics-informed operator learning when labeled supervision is limited.
28
```

## PDF page 29

```text
Fig. 16: Absolute error comparison of DeepOMamba and PILNO atN train = 27on the same test instances as in Fig. 15.
Rows correspond to Types A, B, and C (top to bottom). Columns show the input forcingf(x, t), the corresponding
reference solution, the absolute error of DeepOMamba prediction, and the absolute error of PILNO prediction (left to
right).
5. Conclusion
This study enhances data-driven operator learning through the introduction of the Physics-Informed
Laplace Neural Operator (PILNO), an extension of the Laplace Neural Operator (LNO) that incor-
porates physical principles. PILNO augments the operator-learning objective with PDE, boundary,
and initial-condition residuals, and addresses two persistent challenges—scarce labeled data and
sensitivity to out-of-distribution (OOD) inputs—by complementing standard physics losses with
label-free virtual inputs. For time-dependent PDEs, we further employ temporal-causality weighting
(TCW) to bias the residual toward early times, promoting stable optimization and causally coherent
predictions. Together, these components yield a principled framework for physically constrained
and sample-efficient operator learning.
Empirically, across Burgers’ equation, Darcy flow, reaction–diffusion systems, and forced KdV
equation, PILNO consistently achieves lower errors than LNO, the data-driven baseline; on the
forced KdV benchmark, we additionally compare against DeepOMamba and observe substantially
improved data efficiency for PILNO as paired data become extremely scarce. In particular, test errors
29
```

## PDF page 30

```text
with respect to the number of training samples demonstrate improved data efficiency, while error
heatmaps over input length-scales demonstrate stronger OOD generalization, with PILNO sustaining
substantially lower errors on off-diagonal (OOD) train–test combinations than purely data-driven
operators. Ablations further highlight that virtual inputs are critical for maintaining accuracy in the
extreme small-data regime (e.g., Darcy flow), and that TCW further improves both training stability
and predictive accuracy for time-dependent problems (e.g., reaction–diffusion).
Because the use of physics residuals is rooted in the core premise of physics-informed neural
networks (PINNs) [4], and because both virtual inputs and temporal-causality weighting adapt tech-
niques proposed to mitigate known PINN pathologies [7, 45], systematically transferring, refining,
and assessing recent PINN advances within neural-operator architectures is a promising direction
for future work. Examples include adaptive residual weighting, curriculum strategies for collocation
sampling, and multi-physics constraints tailored to operator learning. We expect that such cross-
fertilization between PINNs and operator learning further improves robustness, data efficiency, and
long-horizon stability in scientific machine learning.
Acknowledgements
This work was supported by the National Research Foundation of Korea [NRF-2021R1C1C1007875]
and by the National Research Council of Science & Technology (NST) grant by the Korea govern-
ment (MSIT) (CRC20014-000).
Appendix A. Additional Comparison of ALNO, LNO, and FNO on Burgers’ Equation
In Section 2.3, we introduced the Advanced Laplace Neural Operator (ALNO), which retains
the interpretable pole-residue transient structure of LNO while increasing expressivity by replacing
the steady-state branch with an FNO-style spectral module. Here we provide a focused comparison
of ALNO, vanilla LNO, and FNO to assess whether this hybrid design yields tangible gains in
approximation accuracy.
All results in this appendix use the same Burgers’ equation setup as in Section 4.1: periodic
domainx∈[0,1], viscosityν= 0.01, time horizont∈[0,1]discretized withh= 1/25(26
snapshots), andN x = 32spatial nodes. Initial conditions are drawn from the Gaussian process with
exponentiated squared-sine kernel at length-scaleℓ train =ℓ test = 0.5. Each model is trained with
Ntrain = 200paired samples under the same optimizer, learning-rate schedule, and a comparable
number of parameters.
LNO ALNO FNO
RelativeL 2 Error3.444×10 −2 3.312×10 −3 8.089×10 −3
Table 3: RelativeL 2 errors on Burgers’ equation (periodic,ν= 0.01,h= 1/25,N x = 32). Lower is better.
30
```

## PDF page 31

```text
Fig. 17: Distribution of relativeL 2 errors over 50 test cases for LNO, ALNO, and FNO. Blue dots indicate the relative
L2 errors of LNO, green crosses indicate those of ALNO, and yellow triangles indicate those of FNO. Red markers
denote the mean error of each model with caps representing one standard deviation. LNO achieve mean relativeL2 error
of3.444×10 −2 and standard deviation of7.504×10 −3. ALNO achieve mean relativeL 2 error of3.312×10 −3 and
standard deviation of1.778×10 −3. FNO achieve mean relativeL 2 error of8.089×10 −3 and standard deviation of
4.816×10 −3
Table 3 shows that vanilla LNO incurs the largest test error (3.444×10 −2), FNO improves sub-
stantially (8.089×10 −3), and ALNO further reduces the error to3.312×10 −3, an order of magnitude
better than LNO and roughly a factor of2.4better than FNO. Figure 17 provides a finer view of the
error distribution across the 50 test instances. ALNO not only achieves the lowest mean error but
also exhibits the smallest spread, with noticeably fewer large-error outliers than either LNO or FNO.
These results support the claim that decoupling the transient and steady-state branches—while keep-
ing an interpretable pole-residue transient component and using a flexible Fourier multiplier for the
steady response—yields a strictly more expressive and robust backbone for operator learning.
Appendix B. Diffusion equation
Here we consider the diffusion equation, a canonical model for macroscopic transport emerging
from microscopic Brownian motion:
D ∂2u
∂x2 − ∂u
∂t =f(x, t), x∈[0,1], t∈[0,1],
u(t,0) =u(t,1)
(36)
whereu(t, x)denotes the scalar field andD >0is the diffusivity. To train and evaluate the models,
we discretize time step sizeh= 1/25, yielding 26 snapshots{t k}25
k=0, and selectN x = 32equidistant
31
```

## PDF page 32

```text
spatial nodes on[0,1], identical to the Burgers’ setup. The input to LNO and PILNO is the initial
condition, and the target is the corresponding spatio-temporal solution.
As our goal here is to assess generalization, we sample initialy 0(x)from a Gaussian random
field with the exponentiated squared sine kernel, using length-scalesℓ∈ {0.5,1.0,1.5, . . . ,5.0}.
For eachℓ train, a model is trained and then evaluated on allℓ test, producing a10×10heat map of
test errors (relativeL 2), analogous to the Burgers’ experiment.
Figure 18 reports generalization heatmaps for ALNO and PILNO. As expected, errors are lowest
near the diagonalℓ train ≈ℓ test. Off-diagonal evaluations (mismatch between smooth and oscillatory
initial conditions for training and test datasets) are more challenging: ALNO exhibits a pronounced
degradation when extrapolating across widely separated length-scales (e.g., from largeℓto smallℓ).
In contrast, PILNO maintains substantially lower errors across these off-diagonal regimes, indicating
that the physics-informed residual effectively constrains the learned dynamics beyond the training
distribution.
On diffusion, where the underlying operator favors smoothing dynamics, PILNO consistently
improves out–of–distribution performance across initial–condition length–scales, mirroring the ro-
bustness observed in Burgers’ equation while isolating the benefit of the physics–informed structure
under a linear parabolic PDE.
(a)
 (b)
Fig. 18: Generalization across initial–condition length–scales for diffusion equation. Heatmaps show relativeL 2 er-
ror when training at length–scaleℓ train (vertical axis) and testing atℓ test (horizontal axis), for (a) ALNO and (b)
PILNO. PILNO sustains lower errors off the diagonal (mismatched smooth/oscillatory regimes), demonstrating stronger
out–of–distribution generalization.
32
```

## PDF page 33

```text
Appendix C. Temporal-Causality Weighting (TCW) Ablation Study Without Virtual Inputs
In Section 4.2, we demonstrated the effect of virtual inputs, and in Section 4.3 we evaluated the
effect of temporal-causality weighting (TCW). Since the experiments in Section 4.3 were conducted
with virtual inputs, it is unclear whether TCW provides a standalone benefit when virtual inputs are
removed. To isolate this effect, we repeat the training protocol of Section 4.3 withN virt = 0; all
other models and hyperparameters are kept identical.
TCW is designed to address a temporal optimization pathology in physics-informed training:
during long-horizon prediction, early-time errors can propagate forward, and the physics loss may be
reduced by fitting late-time residuals while leaving substantial early-time inconsistencies (late-time
masking). TCW mitigates this instability by emphasizing early-time residuals. Its practical impact
is expected to be largest when the physics loss dominates optimization. Virtual inputs create such
a regime by removing supervised anchors on additional inputs, whereas in the fully labeled setting
(Nvirt = 0) the data loss typically anchors training and the physics loss acts more as a regularizer,
making TCW’s standalone gains harder to observe. In other words, the standalone effect of TCW
becomes harder to observe and may yield only marginal improvements.
Figure 19 supports this interpretation. Without virtual inputs, TCW and non-TCW models
achieve comparable mean test errors across training-set sizes, while TCW yields a modest reduc-
tion in the standard-deviation band, indicating improved run-to-run stability. Overall, TCW remains
mildly beneficial in the labeled-only regime, but its effect is substantially weaker than when com-
bined with virtual inputs, where physics-driven optimization is more prominent.
Appendix D. Detailed setting for forced KdV equation
In this section, we detail the data generation procedure used for the forced KdV example and
provide a description of the DeepOMamba model architecture employed in our experiments.
Data generation.Following the DeepOMamba [46] benchmark in forced KdV equation, we gener-
ate data from three analytic solution families, denoted as Types A, B, and C. We have three forcing
types, formulated as
fA(x, t) = 12kβ/α[k 3(4β−δ)−bA/(1 +A 2t2)−b 1]
cosh2[k(x−δk 2t)−barctan(At)−b 1t−b 0]
fB(x, t) = 12kβ/α[k 3(4β−δ)−(2b 2t+b 1) exp(b2t2 +b 1t+b 0)]
cosh2[k(x−δk 2t)−exp(b 2t2 +b 1t+b 0)]
fC(x, t) = 12βγ
α
6β(γ+ 1)
F(x, t) 2 − 8β(x+a) 2
H(x, t)2F(x, t) 3 − (t+b)H(x, t) 2
(x+a)F(x, t) − (t+b)H(x, t) 3
(x+a) 3 arctan(H(x, t))

(37)
33
```

## PDF page 34

```text
Fig. 19: RelativeL 2 error on the test set versus the number of training samples (mean±std over five random seeds). In
the absence of virtual inputs, TCW yields error curves comparable to those obtained without TCW across all training set
sizes.
and corresponding solutions
uA(x, t) = 12βk2
cosh2[k(x−δk 2t)−barctan(At)−b 1t−b 0]
uB(x, t) = 12βk2
cosh2[k(x−δk 2t)−exp(b 2t2 +b 1t+b 0)]
uC(x, t) = 12βγ
F(x, t)
(38)
whereF(x, t) = (x+a) 2+(t+b)2+dandH(x, t) = x+a√
d+(b+t)2 . Here,k, a, A, α, β, δ, γ, b 0, b1, b, b2, d
are the coefficients of the forced KdV equation.
DeepOMamba baseline.We use aN x×Nt = 100×100space-time grid withC in = 7input channels.
The Mamba model is configured with hidden dimensiond model = 256,n layer = 1. The network uses
LayerNorm withϵ= 10 −5 and linear projections map700→256at the input and256→100at the
output. Moreover, in training procedure, we use Adam with learning rate 0.001, batch size 16, and
E= 100epochs. We apply a linear learning-rate decay viaLambdaLRwithη e =η 0(1−e/E), and
optimize the relativeL 2 loss∥ˆu−u∥ 2/∥u∥2.
References
[1] M. Abadi, P. Barham, J. Chen, Z. Chen, A. Davis, J. Dean, M. Devin, S. Ghemawat, G. Irving,
M. Isard, et al., TensorFlow: a system for Large-Scale machine learning, in: 12th USENIX
34
```

## PDF page 35

```text
Symposium on Operating Systems Design and Implementation (OSDI 16), 2016, pp. 265–283.
[2] J. Bradbury, R. Frostig, P. Hawkins, M. J. Johnson, C. Leary, D. Maclaurin, G. Necula,
A. Paszke, J. VanderPlas, S. Wanderman-Milne, et al., Jax: composable transformations of
python+ numpy programs (2018).
[3] A. Paszke, S. Gross, F. Massa, A. Lerer, J. Bradbury, G. Chanan, T. Killeen, Z. Lin,
N. Gimelshein, L. Antiga, et al., PyTorch: An imperative style, high-performance deep learning
library, Advances in Neural Information Processing Systems 32 (2019).
[4] M. Raissi, P. Perdikaris, G. E. Karniadakis, Physics-informed neural networks: A deep learning
framework for solving forward and inverse problems involving nonlinear partial differential
equations, Journal of Computational Physics 378 (2019) 686–707.
[5] Z. Li, N. B. Kovachki, K. Azizzadenesheli, B. Liu, K. Bhattacharya, A. Stuart, A. Anand-
kumar, Fourier neural operator for parametric partial differential equations, in: International
Conference on Learning Representations, 2021.
[6] L. Lu, P. Jin, G. Pang, Z. Zhang, G. Karniadakis, Learning nonlinear operators via deeponet
based on the universal approximation theorem of operators, Nature Machine Intelligence 3 (3)
(2021) 218–229.
[7] J. Jung, H. Kim, H. Shin, M. Choi, Ceens: Causality-enforced evolutional networks for solving
time-dependent partial differential equations, Computer Methods in Applied Mechanics and
Engineering 427 (2024) 117036.
[8] S. A. Faroughi, N. M. Pawar, C. Fernandes, M. Raissi, S. Das, N. K. Kalantari,
S. Kourosh Mahjour, Physics-guided, physics-informed, and physics-encoded neural networks
and operators in scientific computing: Fluid and solid mechanics, Journal of Computing and
Information Science in Engineering 24 (4) (2024) 040802.
[9] A. M. Propp, D. M. Tartakovsky, Transfer learning on multi-dimensional data: A novel ap-
proach to neural network-based surrogate modeling, Journal of Machine Learning for Model-
ing and Computing 6 (2) (2025).
[10] T. J. Hughes, The finite element method: linear static and dynamic finite element analysis,
Courier Corporation, 2012.
[11] E. Cardoso-Bihlo, A. Bihlo, Exactly conservative physics-informed neural networks and deep
operator networks for dynamical systems, Neural Networks 181 (2025) 106826.
35
```

## PDF page 36

```text
[12] T. De Ryck, S. Mishra, Generic bounds on the approximation error for physics-informed (and)
operator learning, Advances in Neural Information Processing Systems 35 (2022) 10945–
10958.
[13] N. Kovachki, Z. Li, B. Liu, K. Azizzadenesheli, K. Bhattacharya, A. Stuart, A. Anandkumar,
Neural operator: Learning maps between function spaces with applications to pdes, Journal of
Machine Learning Research 24 (89) (2023) 1–97.
[14] L. Lu, X. Meng, S. Cai, Z. Mao, S. Goswami, Z. Zhang, G. E. Karniadakis, A comprehensive
and fair comparison of two neural operators (with practical extensions) based on fair data,
Computer Methods in Applied Mechanics and Engineering 393 (2022) 114778.
[15] T. Chen, H. Chen, Universal approximation to nonlinear operators by neural networks with
arbitrary activation functions and its application to dynamical systems, IEEE Transactions on
Neural Networks 6 (4) (1995) 911–917.
[16] A. D. Back, T. Chen, Universal approximation of multiple nonlinear operators by neural net-
works, Neural Computation 14 (11) (2002) 2561–2566.
[17] V . Oommen, K. Shukla, S. Goswami, R. Dingreville, G. E. Karniadakis, Learning two-phase
microstructure evolution using neural operators and autoencoder architectures, npj Computa-
tional Materials 8 (1) (2022) 190.
[18] Q. Cao, S. Goswami, T. Tripura, S. Chakraborty, G. E. Karniadakis, Deep neural operators can
predict the real-time response of floating offshore structures under irregular waves, Computers
& Structures 291 (2024) 107228.
[19] K. Kontolati, S. Goswami, M. D. Shields, G. E. Karniadakis, On the influence of over-
parameterization in manifold based surrogates and deep neural operators, Journal of Com-
putational Physics 479 (2023) 112008.
[20] S. Lee, Y . Shin, On the training and generalization of deep operator networks, SIAM Journal
on Scientific Computing 46 (4) (2024) C273–C296.
[21] S. De, M. Reynolds, M. Hassanaly, R. N. King, A. Doostan, Bi-fidelity modeling of uncer-
tain and partially unknown systems using deeponets, Computational Mechanics 71 (6) (2023)
1251–1267.
[22] Z. Li, N. Kovachki, K. Azizzadenesheli, B. Liu, A. Stuart, K. Bhattacharya, A. Anandkumar,
Multipole graph neural operator for parametric partial differential equations, Advances in Neu-
ral Information Processing Systems 33 (2020) 6755–6766.
36
```

## PDF page 37

```text
[23] Z. Li, N. Kovachki, K. Azizzadenesheli, B. Liu, K. Bhattacharya, A. Stuart, A. Anandku-
mar, Neural operator: Graph kernel network for partial differential equations, arXiv Preprint
arXiv:2003.03485 (2020).
[24] T. Tripura, S. Chakraborty, Wavelet neural operator for solving parametric partial differential
equations in computational mechanics problems, Computer Methods in Applied Mechanics
and Engineering 404 (2023) 115783.
[25] Q. Cao, S. Goswami, G. E. Karniadakis, Laplace neural operator for solving differential equa-
tions, Nature Machine Intelligence 6 (6) (2024) 631–640.
[26] B. Bonev, T. Kurth, C. Hundt, J. Pathak, M. Baust, K. Kashinath, A. Anandkumar, Spherical
Fourier neural operators: Learning stable dynamics on the sphere, in: Proceedings of the 40th
International Conference on Machine Learning, PMLR, 2023, pp. 2806–2823.
[27] Y .-K. Lin, Probabilistic Theory of Structural Dynamics, R. E. Krieger Publishing Company,
Huntington, NY , 1976, reprint of the 1967 McGraw-Hill edition.
[28] S.-L. J. Hu, W.-L. Yang, H.-J. Li, Signal decomposition and reconstruction using complex
exponential models, Mechanical Systems and Signal Processing 40 (2) (2013) 421–438.
[29] Q. Cao, S.-L. James Hu, H. Li, Laplace-and frequency-domain methods on computing transient
responses of oscillators with hysteretic dampings to deterministic loading, Journal of Engineer-
ing Mechanics 149 (3) (2023) 04023005.
[30] J. Pathak, S. Subramanian, P. Harrington, S. Raja, A. Chattopadhyay, M. Mardani, T. Kurth,
D. Hall, Z. Li, K. Azizzadenesheli, et al., Fourcastnet: A global data-driven high-resolution
weather model using adaptive fourier neural operators, arXiv Preprint arXiv:2202.11214
(2022).
[31] R. Ranade, H. He, J. Pathak, N. Chang, A. Kumar, J. Wen, A thermal machine learning solver
for chip simulation, in: Proceedings of the 2022 ACM/IEEE Workshop on Machine Learning
for CAD, 2022, pp. 111–117.
[32] H. Jin, B. Zhang, Q. Cao, E. Zhang, A. Bora, S. Krishnaswamy, G. E. Karniadakis, H. D.
Espinosa, Characterization and inverse design of stochastic mechanical metamaterials using
neural operators, Advanced Materials (2025) 2420063.
[33] N. Ahmadi, Q. Cao, J. D. Humphrey, G. E. Karniadakis, Physics-informed machine learning
in biomedical science and engineering, arXiv Preprint arXiv:2510.05433 (2025).
37
```

## PDF page 38

```text
[34] H. Hersbach, B. Bell, P. Berrisford, S. Hirahara, A. Horányi, J. Muñoz-Sabater, J. Nicolas,
C. Peubey, R. Radu, D. Schepers, et al., The era5 global reanalysis, Quarterly Journal of the
Royal Meteorological Society 146 (730) (2020) 1999–2049.
[35] Z. Li, H. Zheng, N. Kovachki, D. Jin, H. Chen, B. Liu, K. Azizzadenesheli, A. Anandkumar,
Physics-informed neural operator for learning partial differential equations, ACM/IMS Journal
of Data Science 1 (3) (2024) 1–27.
[36] M. Zhu, H. Zhang, A. Jiao, G. E. Karniadakis, L. Lu, Reliable extrapolation of deep neural op-
erators informed by physics or sparse observations, Computer Methods in Applied Mechanics
and Engineering 412 (2023) 116064.
[37] S. Wang, H. Wang, P. Perdikaris, Learning the solution operator of parametric partial differen-
tial equations with physics-informed deeponets, Science Advances 7 (40) (2021) eabi8605.
[38] S. Goswami, A. Bora, Y . Yu, G. E. Karniadakis, Physics-informed deep neural operator
networks, in: Machine Learning in Modeling and Simulation: Methods and Applications,
Springer, 2023, pp. 219–254.
[39] N. Navaneeth, T. Tripura, S. Chakraborty, Physics informed wno, Computer Methods in Ap-
plied Mechanics and Engineering 418 (2024) 116546.
[40] S. G. Rosofsky, H. Al Majed, E. Huerta, Applications of physics informed neural operators,
Machine Learning: Science and Technology 4 (2) (2023) 025022.
[41] C. Kaewnuratchadasorn, J. Wang, C.-W. Kim, Physics-informed neural operator solver and
super-resolution for solid mechanics, Computer-Aided Civil and Infrastructure Engineering
39 (22) (2024) 3435–3451.
[42] A. Jiao, Q. Yan, J. Harlim, L. Lu, Solving forward and inverse pde problems on unknown
manifolds via physics-informed neural operators, arXiv Preprint arXiv:2407.05477 (2024).
[43] E. Kreyszig, K. Stroud, G. Stephenson, Advanced engineering mathematics, Integration 9 (4)
(2008) 1014.
[44] S.-L. J. Hu, F. Liu, B. Gao, H. Li, Pole-residue method for numerical dynamic analysis, Journal
of Engineering Mechanics 142 (8) (2016) 04016045.
[45] S. Wang, S. Sankaran, P. Perdikaris, Respecting causality is all you need for training physics-
informed neural networks, arXiv Preprint arXiv:2203.07404 (2022).
[46] Z. Hu, Q. Cao, K. Kawaguchi, G. E. Karniadakis, Deepomamba: State-space model for spatio-
temporal pde neural operator learning, Journal of Computational Physics (2025) 114272.
38
```
