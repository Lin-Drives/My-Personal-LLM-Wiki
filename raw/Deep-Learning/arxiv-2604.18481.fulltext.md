# arXiv:2604.18481 — PDF 原文文本提取

- Source: https://arxiv.org/abs/2604.18481
- Local PDF: `arxiv-2604.18481.pdf` (local only)
- PDF SHA-256: `3e535e5bb4602fb1a2da52ea0e5cafc87ce6486db4044df2fe84173437dfcd02`
- Converted at: 2026-10-06T23:51:12.364501+00:00
- Extractor: pypdf/6.10.0
- Pages: 22
- Pages without extractable text: none

> 逐页提取 PDF 文本，未使用模型改写或翻译，未进行内容核验。保留页码；多栏阅读顺序、公式、表格和图片可能不能准确还原。无文字页需要另行 OCR，不能视为完整文本覆盖。基础 ID 的具体版本尚未解析，以 PDF 哈希标识本次原文件。

## PDF page 1

```text
PHYSICS-INFORMED NEURAL NETWORKS: A DIDACTIC
DERIVATION OF THE COMPLETE TRAINING CYCLE
ABDELADHIM TAHIMI ∗
Abstract.This paper is a step-by-step, self-contained guide to the complete training cycle of
a Physics-Informed Neural Network (PINN) — a topic that existing tutorials and guides typically
delegate to automatic differentiation libraries without exposing the underlying algebra. Using a
first-order initial value problem with a known analytical solution as a running example, we walk
through every stage of the process: forward propagation of both the network output and its tempo-
ral derivative, evaluation of a composite loss function built from the ODE residual and the initial
condition, backpropagation of gradients — with particular attention to the product rule that arises
in hidden layers — and a gradient descent parameter update. Every calculation is presented with
explicit, verifiable numerical values using a 1-3-3-1 multilayer perceptron with two hidden layers and
22 trainable parameters. From these concrete examples, we derive general recursive formulas —
expressed as sensitivity propagation relations — that extend the gradient computation to networks
of arbitrary depth, and we connect these formulas to the automatic differentiation engines used in
practice. The trained network is then validated against the exact solution, achieving a relativeL 2
error of 4.290×10 −4 using only the physics-informed loss, without any data from the true solution.
A companion Jupyter/PyTorch notebook reproduces every manual calculation and the full training
pipeline, providing mutual validation between hand-derived and machine-computed gradients.
Key words.Physics-Informed Neural Networks, Scientific Machine Learning, backpropagation,
initial value problem, automatic differentiation, neural network training, didactic introduction
MSC codes.65L05, 68T07, 65M99, 97M10
1. Introduction.
What is a PINN, in one paragraph..Physics-Informed Neural Networks [17],
building on earlier work embedding differential equations into neural network training
[13], are a framework in Scientific Machine Learning (SciML) [10] that uses a neural
network to approximate the solution of a problem governed by known physical laws.
The key idea is to embed these laws — typically expressed as differential equations,
but potentially including integral constraints, conservation principles, or symmetry
conditions — directly into the loss function. The network is trained to minimize
the residual of the governing equations at a set of collocation points, while simul-
taneously satisfying prescribed initial or boundary conditions and, when available,
incorporating experimental or observational data. Since their introduction, PINNs
have been applied in fluid dynamics [18], inverse problems [10], and a broad range
of computational science applications [4]. The methodology continues to evolve, with
recent work addressing gradient pathologies [22], adaptive loss balancing [15], and
broader methodological challenges reviewed in [21]. However, while the frontier ad-
vances rapidly, the foundational training mechanics remain the same — and it is these
mechanics that we dissect here.
The pedagogical gap..Despite the breadth of this literature, a detailed, step-by-
step account of what a PINN computes during a single training step — from the
forward pass through the backward pass to the parameter update — is not available
in any single resource. Introductory tutorials have been developed for mechanics
[11], astrophysics and plasma physics [2], and classroom settings using notebook-
based pedagogical frameworks [16]. At the expert level, Wang et al. [23] provide a
∗ Campus de Engenharias e Ciˆ encias Agr´ arias (CECA), Universidade Federal de Alagoas (UFAL),
Rio Largo, Alagoas, 57100-000, Brazil (abdeladhim.tahimi@ceca.ufal.br). Submitted to the editors
April 21, 2026.
1
arXiv:2604.18481v1  [math.NA]  20 Apr 2026
```

## PDF page 2

```text
2A. TAHIMI
comprehensive guide to training best practices. Standard deep learning references
[6] cover backpropagation thoroughly. Yet in all of these, the precise sequence of
operations by which a physics-informed loss and a backward pass produce the gradient
that updates each weight is either delegated to automatic differentiation libraries or
presented without exposing the underlying algebra — in particular, the additional
structure that arises when a differential equation is embedded in the loss function
receives no explicit treatment. A notable exception is Almqvist [1], who derives
the cost function gradients symbolically for a single-hidden-layer PINN applied to the
Reynolds equation. That work demonstrates the power of explicit derivation, but with
one hidden layer the gradient follows a direct chain rule — the recursive structure
that emerges when parameter perturbations must propagate through multiple hidden
layers, accumulating product rules, higher order derivatives of the activation function,
and fan-out summations at each stage, does not arise.
What this paper covers..The present paper addresses this gap. We take a first-
order initial value problem with a known analytical solution —y ′(t) +y(t) = 0,
y(0) = 1 — and use it as a vehicle to expose every detail of the PINN training cycle.
A small 1-3-3-1 multilayer perceptron with fixed, hand-verifiable parameters serves as
our working example. Specifically, we cover:
1. The formulation of a composite loss function comprising an ODE residual
term and an initial condition term, weighted by a hyperparameterλ.
2. The simultaneous forward propagation of the network output ˆy(t) and its
temporal derivative ˆy′(t) through the network, layer by layer. This dual
propagation is what makes the additional gradient structure of the backward
pass visible.
3. The computation of parametric gradients via backpropagation, with partic-
ular attention to theproduct rulethat arises in hidden layers because ˆy ′
depends on the network weights through both the activations and their de-
rivatives.
4. The parameter update via gradient descent.
5. General recursive formulas that express the parametric gradients for any
weight or bias at any layer in terms of two sensitivity quantities — one for
the activation, one for its time derivative — propagated forward through the
network. These formulas extend the concrete examples to networks of arbi-
trary depth and connect naturally to the automatic differentiation engines
used in frameworks such as PyTorch.
6. The validation of the fully trained network against the known analytical so-
lutiony(t) =e −t, demonstrating that the physics-informed loss alone —
without any data from the true solution — is sufficient to recover the correct
physical behavior.
Every calculation in this paper is presented with explicit numerical values that the
reader can (and should) verify by hand. To support this, the paper is accompanied
by an interactive Jupyter/Google Colab Notebook that serves a dual purpose: it
reproduces every manual calculation using PyTorch’s automatic differentiation engine,
and it independently executes the full training and validation pipeline, generating the
results and figures reported here. The exact agreement between the hand-derived
values and PyTorch’s output serves as mutual validation: the theory verifies the code,
and the code verifies the theory.
How this paper is organized..Section 2 introduces the IVP, the neural network
architecture, and the complete forward pass leading to the loss function computa-
tion. Section 3 details the gradient computation via backpropagation — first through
```

## PDF page 3

```text
PINNS: DIDACTIC DERIVATION OF THE TRAINING CYCLE3
worked examples at the output and hidden layers, then through general recursive
formulas that extend to networks of arbitrary depth. Section 4 trains the network
to convergence and validates it against the analytical solution. Section 5 presents
concluding remarks and perspectives for further study.
2. Explanatory Example of PINN Modeling.To demystify the PINN train-
ing process, we now work through a complete example with every intermediate value
written out explicitly. Figure 1 provides a visual overview of the complete training
cycle; this section covers the forward propagation and loss computation stages, while
Section 3 details the gradient computation and parameter update.
Initialization
Set parametersθ={W(ℓ),b (ℓ)}3
ℓ=1; sample collocation points{ti}Nc
i=1⊂[0,1]
Forward Pass
Propagate both ˆy(ti) and ˆy′(ti) simultaneously through the network
Loss Computation
L= 1
Nc
Nc∑
i=1
[
ˆy′(ti) + ˆy(ti)
]2
  
LR
+λ
(
ˆy(0)−1
)2
  
LIC
Backpropagation
Compute∇θLvia chain rule —includes the prod-
uct rule arising from the time derivativeˆy ′
Parameter Update
θ←θ−η∇ θL
Repeat until convergence
Fig. 1.The PINN training cycle. After a one-time initialization (dashed box), the network
iterates through four stages: a dual forward pass computing both the predictionˆyand its derivativeˆy′,
evaluation of the composite loss, backpropagation of parametric gradients — where the product rule
arising from the time derivativeˆy′ enters in hidden layers — and a gradient-based parameter update.
This cycle repeats until the total loss converges to a prescribed tolerance.
2.1. Definition of the Initial Value Problem.Our goal is to find the solution
to the first-order ODE
(2.1)y ′(t) +y(t) = 0,
```

## PDF page 4

```text
4A. TAHIMI
subject to the initial conditiony(0) = 1. This is the “hello world” of physics-informed
learning: simple enough to serve as a first exercise with hand-verifiable numbers, yet
rich enough to expose every mechanism by which the network encodes physics —
a residual loss, an initial condition constraint, and a derivative that introduces the
product rule during backpropagation. The analytical solutiony(t) =e −t will be used
in Section 4 to assess the accuracy of the trained network.
2.2. Neural Network Configuration.We employ aMultilayer Perceptron
(MLP)with a 1-3-3-1 architecture: one input neuron (for the variablet), two hidden
layers with 3 neurons each, and one output neuron producing the approximation ˆy(t).
The hidden layers use the hyperbolic tangent (tanh) activation function, and the
output layer uses the identity — a standard choice for regression, since the network
output must be free to take any real value. Figure 2 shows the full architecture.
t
h1,1
h1,2
h1,3
h2,1
h2,2
h2,3
ˆy(t)
Input Output
Fig. 2.Architecture of the 1-3-3-1 MLP. The number of trainable parameters for a dense layer
is(w in ×w out)+w out, wherew in is the layer input dimension andw out is the number of its neurons.
For example, the transition between the two hidden layers (both with 3 neurons) has(3×3) + 3 = 12
parameters.
To fully understand the forward propagation, it helps to look at what a single
neuron does. As illustrated in Figure 3, a neuron in hidden layerℓreceives outputs
from the previous layer,a (ℓ−1). It performs an affine transformation: multiply the
inputs by weightsW (ℓ), sum the results, and add a biasb (ℓ) to produce the pre-
activationz (ℓ). A non-linear activation functionϕ(·) is then applied to produce the
neuron’s output,a (ℓ) =ϕ(z (ℓ)).
The choice ofϕ(·) deserves a careful remark, because it is not arbitrary. Without
a non-linear activation, every layer would compute an affine transformation, and com-
posing affine transformations yields another affine transformation — regardless of the
number of layers. The network would be limited to representing straight lines, and
could never capture the curvature of a solution likee −t. The non-linear activation is
precisely what breaks this limitation: the Universal Approximation Theorem [8] guar-
antees that a feedforward network with at least one hidden layer and a non-constant,
bounded, continuous activation function can approximate any continuous function on
a compact set to arbitrary accuracy, provided sufficiently many neurons. Without the
non-linearity, this result fails entirely.
For PINNs, however, non-linearity alone is not enough. The loss function in-
volves physical derivatives — ˆy′ in our case, and potentially ˆy ′′ or higher for other
equations — computed via automatic differentiation through the network. This im-
poses a second requirement: the activation function must besufficiently smooth. The
```

## PDF page 5

```text
PINNS: DIDACTIC DERIVATION OF THE TRAINING CYCLE5
Σ ϕ
a(ℓ−1)
1
a(ℓ−1)
2
...
a(ℓ−1)
n
b(ℓ)
j
W (ℓ)
j,1
W (ℓ)
j,2
W
(ℓ)
j,n
a(ℓ)
j = tanh(z (ℓ)
j )
Pre-activation:z (ℓ)
j = ∑
kW (ℓ)
j,ka(ℓ−1)
k +b (ℓ)
j
Fig. 3.Detailed operation of a single artificial neuron. The inputs are linearly combined using
weights and biases to formz, which is then passed through the non-linear activation functionϕ(z)
to produce the outputa.
Rectified Linear Unit (ReLU), the default activation in standard deep learning, is
non-linear and satisfies the universal approximation property, but it is not smooth:
it is non-differentiable atz= 0 and its second derivative is zero everywhere else. A
ReLU-based network simply cannot represent the physics of second-order differential
equations. PINNs therefore require activations that are both non-linear and continu-
ously differentiable. The output layer is the exception: it uses the identity function
ϕ(z) =z, because the network prediction must be free to take any real value — tanh,
being bounded to (−1,1), would impose an artificial constraint on the solution range.
We use tanh here, which is the standard activation in the PINN literature since
the foundational work of Raissi et al. [17]. It is infinitely differentiable, zero-centered
— meaning its output range (−1,1) is symmetric around the origin, which promotes
balanced gradient flow during training — and its derivative,ϕ ′(z) = 1−tanh 2(z), is
both smooth and easy to compute analytically. For the smooth, non-periodic solution
treated here, tanh is a natural and sufficient choice. Other smooth activations have
been explored in the PINN literature, including sinusoidal activations [19], which are
well suited for problems with oscillatory or periodic solutions, and adaptive activations
such as Swish and its variants, which have shown improvements in convergence for
certain problem classes [9]. The choice of activation remains an active area of research
[21]; the key requirement for any PINN application is thatϕ(·) be smooth enough to
support the order of differentiation demanded by the governing equation.
The network parameters (weightsWand biasesb) are fixed for this example to
allow numerical verification. In a real application, these would be set using a standard
initialization scheme — such as Xavier [5] or Kaiming [7] — which draw random values
from distributions carefully designed to maintain stable gradient flow across layers.
The training configuration in Section 4 uses Kaiming uniform initialization. The
values are given in Tables 1 to 3.
```

## PDF page 6

```text
6A. TAHIMI
Table 1
Parameters of Hidden Layer 1.
WeightsW (1) Biasesb (1)


0.2
−0.5
0.8




−0.1
0.3
−0.2


Table 2
Parameters of Hidden Layer 2.
WeightsW (2) Biasesb (2)


0.1−0.3 0.5
0.6 0.2−0.4
−0.2 0.7 0.1




0.2
−0.1
0.4


2.3. Loss Function Computation: Forward Propagation.The total loss
functionLis what guides the training, and it has two parts:
1.Residual Loss (L R):This term enforces the ODE. It is computed over a
set of collocation points{t i}Nc
i=1. At each pointt i, the residual isR(t i) =
ˆy′(ti) + ˆy(ti) — which would be zero if the network output satisfied the ODE
exactly. The loss is the mean squared residual:
(2.2)L R = 1
Nc
NcX
i=1
R(ti)2.
2.Initial Condition Loss (L IC):This term enforcesy(0) = 1. It is simply
the squared error at the initial point:
(2.3)L IC =
 
ˆy(0)−1
2
.
The total loss is the weighted sumL=L R +λ·L IC , whereλis a hyperparameter
that balances the two terms. Since our purpose here is to illustrate every detail of
the training process, we keep things as simple as possible: a single collocation point
tc = 0.5 andλ= 10. The following subsections trace the computation of ˆyand ˆy ′ at
this point and att= 0.
2.3.1. Forward Propagation for the Residual Loss (L R).The first step is
to compute the network prediction and its derivative at the collocation pointt c = 0.5.
The network input isa (0) = 0.5 and — since the input is simplyt— its derivative
with respect totis ˙a (0) = 1.0.
Step 1: First Hidden Layer (ℓ= 1)..We compute the pre-activationz (1) and its
temporal derivative ˙z(1):
(2.4)z (1) =W (1)a(0) +b (1) and ˙z (1) =W (1) ˙a(0).
Table 3
Parameters of the Output Layer (Layer 3).
WeightsW (3) Biasesb (3)
 0.9−0.6 0.3    −0.3
```

## PDF page 7

```text
PINNS: DIDACTIC DERIVATION OF THE TRAINING CYCLE7
The tanh activation is then applied. A useful identity is that the derivative of tanh
can be written in terms of the activation itself:ϕ ′(z) = 1−tanh 2(z), soϕ ′(z(1)
j ) =
1−(a (1)
j )2. The time derivative of the activation then follows from the chain rule:
˙a(1)
j =ϕ ′(z(1)
j ) ˙z(1)
j . In vector form:
(2.5)a (1) = tanh(z(1)) and ˙a (1) =
 
1−(a (1))2
⊙˙z(1),
where⊙denotes the Hadamard (element-wise) product. Take a moment to verify a
few entries in Table 4 before moving on.
Table 4
Values at the First Hidden Layer forL R (t= 0.5).
Neuron (j)z (1)
j ˙z(1)
j a(1)
j ˙a(1)
j
1 0.0000 0.2000 0.0000 0.2000
2 0.0500−0.5000 0.0500−0.4988
3 0.2000 0.8000 0.1974 0.7688
Step 2: Second Hidden Layer (ℓ= 2)..The process repeats, using the outputs of
the previous layer as inputs:
(2.6)z (2) =W (2)a(1) +b (2),˙z (2) =W (2) ˙a(1),
(2.7)a (2) = tanh(z(2)),˙a (2) =
 
1−(a (2))2
⊙˙z(2).
The results are in Table 5.
Table 5
Values at the Second Hidden Layer forL R (t= 0.5).
Neuron (k)z (2)
k ˙z(2)
k a(2)
k ˙a(2)
k
1 0.2837 0.5540 0.2763 0.5117
2−0.1690−0.2873−0.1673−0.2792
3 0.4547−0.3123 0.4257−0.2559
Step 3: Output Layer (ℓ= 3)..The output layer uses the identity activation
(ϕ(z) =z), so the network output ˆyequals the final pre-activationz (3), and the
output derivative ˆy′ equals ˙z(3):
(2.8)z (3) =W (3)a(2) +b (3) and ˙z (3) =W (3) ˙a(2).
Table 6 gives the numerical values.
Table 6
Values at the Output Layer forL R (t= 0.5).
z(3)
1 ˙z(3)
1 ˆyˆy ′
0.1768 0.5513 0.1768 0.5513
```

## PDF page 8

```text
8A. TAHIMI
Residual Loss Computation..With these values in hand, the ODE residual at
t= 0.5 is:
(2.9)R(0.5) = ˆy ′(0.5) + ˆy(0.5) = 0.5513 + 0.1768 = 0.7281.
The residual loss is the square of this value:
(2.10)L R =R(0.5) 2 = (0.7281)2 ≈0.5301.
2.3.2. Forward Propagation for the Initial Condition Loss (L IC).Next,
we compute the network prediction att= 0 to evaluate the initial condition loss. The
network input isa (0) = 0 and its derivative is ˙a(0) = 1.
Step 1: First Hidden Layer (ℓ= 1)..Sincea (0) = 0, the pre-activation reduces
to the bias vector, and the derivative of the pre-activation equals the weight vector:
(2.11)z (1) =W (1) ·0 +b (1) =b (1) and ˙z (1) =W (1) ·1 =W (1).
Table 7 collects the results.
Table 7
Values at the First Hidden Layer forL IC (t= 0).
Neuron (j)z (1)
j ˙z(1)
j a(1)
j ˙a(1)
j
1−0.1000 0.2000−0.0997 0.1980
2 0.3000−0.5000 0.2913−0.4576
3−0.2000 0.8000−0.1974 0.7688
Step 2: Second Hidden Layer (ℓ= 2)..Table 8 presents the results.
Table 8
Values at the Second Hidden Layer forL IC (t= 0).
Neuron (k)z (2)
k ˙z(2)
k a(2)
k ˙a(2)
k
1 0.0039 0.5415 0.0039 0.5415
2−0.0226−0.2802−0.0226−0.2801
3 0.6041−0.2830 0.5398−0.2005
Step 3: Output Layer (ℓ= 3)..Table 9 gives the final values.
Table 9
Values at the Output Layer forL IC (t= 0).
z(3)
1 ˙z(3)
1 ˆyˆy ′
−0.1210 0.5953−0.1210 0.5953
Initial Condition Loss Computation..Since ˆy(0) =−0.1210, we get:
(2.12)L IC =
 
ˆy(0)−1
2
= (−0.1210−1) 2 = (−1.1210)2 ≈1.2566.
2.3.3. Total Loss and the Start of Optimization.With the forward pass
complete, we can now put the pieces together.
```

## PDF page 9

```text
PINNS: DIDACTIC DERIVATION OF THE TRAINING CYCLE9
Total Loss Computation..From the calculations above,L R ≈0.5301 andL IC ≈
1.2566. Withλ= 10, the total loss is:
(2.13)L=L R +λ·L IC ≈0.5301 + 10·1.2566 = 13.0961.
This single number tells us how far the network is from a correct solution at its current
parameter state.
Why we need the weighting..In practice, whenL R is evaluated over hundreds
or thousands of collocation points, it tends to dominate the total loss, makingL IC
negligible. The hyperparameterλcorrects this imbalance by amplifying the initial
condition contribution. Typical values reported in the literature are 10, 50, 100, 200,
and 1000 [24], and the choice is critical for model performance.
Optimization via Gradient Descent..The training objective is to find the pa-
rameters that minimizeL. Thetrainable parameters, collectively denoted by
θ={W (ℓ), b(ℓ)}L
ℓ=1, are updated iteratively usingGradient Descent:
(2.14)θ new =θ old −η∇ θL,
whereηis thelearning rate. We useη= 0.01 here — small enough to ensure stable
convergence, and a common default for gradient descent.
The need for backpropagation..To apply (2.14), we need the gradient∇ θL. It
is worth pausing to note an important distinction: thetemporal derivative(d/dt)
computed during the forward pass tells us how the output changes with the inputt; the
parametric derivative(∂/∂θ) computed during backpropagation tells us how the
loss changes with the weights and biases. These are fundamentally different quantities,
and it is essential not to confuse them. The next section details the backpropagation
computation for our example.
3. Gradient Computation: Backpropagation.With the forward pass com-
plete and the total loss computed, we now turn to the backward pass. The goal is to
compute the gradient of the loss with respect to every trainable parameter,∇ θL. By
linearity of differentiation, the total gradient is the weighted sum of the gradients of
each loss component:
(3.1)∇ θL=∇ θLR +λ· ∇ θLIC .
The backpropagation algorithm applies the chain rule systematically, moving from
the output layer back toward the input. We demonstrate the computation for one
weight and one bias from both the output and hidden layers — enough to expose all
the key mechanisms. The same logic applies to every other parameter.
3.1. Gradients for the Output Layer.
WeightW (3)
1,2 ..This is the weight connecting the second neuron of the second
hidden layer to the output neuron (see Figure 2). The lossL R =R 2 = (ˆy+ ˆy′)2
depends onW (3)
1,2 through both ˆyand ˆy′. By the chain rule:
(3.2) ∂LR
∂W (3)
1,2
= 2R
 
∂ˆy
∂W (3)
1,2
+ ∂ˆy′
∂W (3)
1,2
!
.
Since the output layer uses the identity activation, we have ∂ˆy
∂W (3)
1,2
=a (2)
2 and ∂ˆy′
∂W (3)
1,2
=
˙a(2)
2 . For the initial condition loss:
(3.3) ∂LIC
∂W (3)
1,2
= 2
 
ˆy(0)−1

a(2)
2 .
```

## PDF page 10

```text
10A. TAHIMI
Table 10 shows the numerical results.
Table 10
Gradient computation for weightW (3)
1,2 .
Component F ormula Result
∂LR/∂W (3)
1,2 2R·(a (2)
2 + ˙a(2)
2 ) 2(0.7281)(−0.1673−0.2792) =−0.6502
∂LIC /∂W (3)
1,2 2(ˆy−1)·a (2)
2 2(−0.1210−1)(−0.0226) =0.0507
The total gradient is:
(3.4) ∂L
∂W (3)
1,2
=−0.6502 + 10·(0.0507) =−0.1432.
Biasb (3)
1 ..This is the bias of the output neuron. The computation is analogous,
with the simplification ∂ˆy
∂b(3)
1
= 1 and ∂ˆy′
∂b(3)
1
= 0, since the bias is not multiplied by any
t-dependent variable. Table 11 shows the details.
Table 11
Gradient computation for biasb (3)
1 .
Component F ormula Result
∂LR/∂b(3)
1 2R·(1 + 0) 2(0.7281)·1 =1.4562
∂LIC /∂b(3)
1 2(ˆy−1)·1 2(−1.1210) =−2.2420
The total gradient is:
(3.5) ∂L
∂b(3)
1
= 1.4562 + 10·(−2.2420) =−20.9638.
3.2. Gradients for the Hidden Layers.Here is where things get interesting
— and where the time derivative in the loss introduces additional complexity in the
gradient computation.
WeightW (2)
1,2 ..This is the weight connecting the second neuron of the first hidden
layer to the first neuron of the second hidden layer (see Figure 2). For parameters in
hidden layers, the influence on the output is indirect. The dependence of ˆyonW (2)
1,2
follows the pathW (2)
1,2 →z (2)
1 →a (2)
1 →z (3)
1 →a (3)
1 = ˆy, and the chain rule gives:
(3.6) ∂ˆy
∂W (2)
1,2
= ∂ˆy
∂z (3)
1|{z}
= 1
· ∂z (3)
1
∂a(2)
1|{z}
=W (3)
1,1
· ∂a(2)
1
∂z (2)
1|{z}
=ϕ ′(z(2)
1 )
· ∂z (2)
1
∂W (2)
1,2| {z }
=a (1)
2
=W (3)
1,1 ·ϕ ′(z(2)
1 )·a (1)
2 .
Now here is the key point. The residual loss depends on both ˆyand ˆy ′, so the
gradient∂L R/∂W (2)
1,2 requires both∂ˆy/∂W (2)
1,2 — which we just computed in (3.6)
— and∂ˆy ′/∂W (2)
1,2 . To see where this second term leads, recall from the forward
pass ((2.8)) that ˆy′ =W (3)
1,1 ˙a(2)
1 +W (3)
1,2 ˙a(2)
2 +W (3)
1,3 ˙a(2)
3 . SinceW (2)
1,2 only affects the
first neuron of the second hidden layer, only the ˙a (2)
1 term contributes, and we need
```

## PDF page 11

```text
PINNS: DIDACTIC DERIVATION OF THE TRAINING CYCLE11
∂˙a(2)
1 /∂W (2)
1,2 . From the forward pass ((2.7)), this activation derivative is the product
˙a(2)
1 =ϕ ′(z(2)
1 ) ˙z(2)
1 . The parameterW (2)
1,2 influencesbothfactors through two distinct
paths:
•W (2)
1,2 →z (2)
1 →ϕ ′(z(2)
1 ),
•W (2)
1,2 →˙z(2)
1 .
Since both factors depend on the same parameter, differentiating their product re-
quires the product rule:
(3.7) ∂˙a(2)
1
∂W (2)
1,2
= ∂ϕ′(z(2)
1 )
∂W (2)
1,2| {z }
=ϕ ′′(z(2)
1 )a (1)
2
·˙z(2)
1 +ϕ ′(z(2)
1 )· ∂˙z(2)
1
∂W (2)
1,2| {z }
= ˙a(1)
2
,
whereϕ ′′(z) =−2 tanh(z)(1−tanh 2(z)). Note thatϕ ′′ appears here even though the
governing ODE involves only a first-order time derivative: the second derivative of the
activation arises not from the physics, but from differentiating the gradientϕ ′(z(2)
1 )
with respect to the network parameters during backpropagation. This is a concrete
illustration of why PINNs require smooth activations — even a first-order equation
demandsϕ ′′ in the gradient computation, and higher-order equations would require
correspondingly higher derivatives. The full derivative of ˆy ′ with respect toW (2)
1,2 is
therefore:
(3.8) ∂ˆy′
∂W (2)
1,2
= ∂ˆy′
∂˙a(2)
1|{z}
=W (3)
1,1
· ∂˙a(2)
1
∂W (2)
1,2
=W (3)
1,1

ϕ′′(z(2)
1 )a (1)
2 ˙z(2)
1 +ϕ ′(z(2)
1 ) ˙a(1)
2

.
Table 12 presents the numerical evaluation.
Table 12
Gradient computation for weightW (2)
1,2 .
Component F ormula Result
∂LR/∂W (2)
1,2 2R
 
∂ˆy/∂W(2)
1,2 +∂ˆy′/∂W (2)
1,2

1.4562·(0.0416−0.4274) =−0.5619
∂LIC /∂W (2)
1,2 2(ˆy−1)∂ˆy/∂W(2)
1,2 −2.2420·(0.9·0.9999·0.2913) =−0.5878
The total gradient is:
(3.9) ∂L
∂W (2)
1,2
=−0.5619 + 10·(−0.5878) =−6.4399.
Biasb (2)
1 ..This is the bias of the first neuron of the second hidden layer. The
derivation follows the same logic as forW (2)
1,2 , with the simplifications ∂z (2)
1
∂b(2)
1
= 1 and
˙z(2)
1 independent ofb (2)
1 :
(3.10) ∂ˆy
∂b(2)
1
=W (3)
1,1 ·ϕ ′(z(2)
1 ) and ∂ˆy′
∂b(2)
1
=W (3)
1,1 ·ϕ ′′(z(2)
1 ) ˙z(2)
1 .
Table 13 shows the results.
```

## PDF page 12

```text
12A. TAHIMI
Table 13
Gradient computation for biasb (2)
1 .
Component F ormula Result
∂LR/∂b(2)
1 2R
 
∂ˆy/∂b(2)
1 +∂ˆy′/∂b(2)
1

1.4562·(0.8314−0.2546) =0.8400
∂LIC /∂b(2)
1 2(ˆy−1)∂ˆy/∂b(2)
1 −2.2420·(0.9·0.9999) =−2.0176
The total gradient forb (2)
1 is:
(3.11) ∂L
∂b(2)
1
= 0.8400 + 10·(−2.0176) =−19.3360.
3.3. Parameter Update.The backpropagation algorithm computes these gra-
dients forall22 parameters of the network. An optimizer then uses them to execute
the update step. With learning rateη= 0.01, the update forW (3)
1,2 is:
(3.12)W (3)
1,2,new =W (3)
1,2,old −η ∂L
∂W (3)
1,2
=−0.6−(0.01)(−0.1432)≈ −0.5986.
This cycle — forward pass (loss computation), backward pass (gradient computation),
and parameter update — is repeated thousands of times. Each iteration nudges the
network parameters a small step in the direction that reduces the loss, progressively
adjusting the network to find a solution that satisfies both the ODE and its initial
condition.
We demonstrated the gradient computation for specific parameters in the output
and second hidden layers. But what about the remaining parameters — in particu-
lar, those in the first hidden layer, where the influence must propagate through two
subsequent layers? The next subsection presents the general formulas that cover any
parameter at any layer.
3.4. General Gradient Formulas.With the full training cycle now complete
for specific parameters, we step back to see the general pattern. We begin with a first
hidden layer parameter — where the gradient is more involved than anything we have
seen so far — and then extract the general formulas that apply to any parameter at
any layer.
3.4.1. A First Hidden Layer Example: WeightW (1)
2,1 .This is the weight
connecting the input to the second neuron of the first hidden layer (see Figure 2). Its
influence on the output must propagate throughtwosubsequent hidden layers before
reaching ˆyand ˆy′. This is what makes it more complex than the second hidden layer
parameters treated earlier.
Derivative ofˆy..The dependence of ˆyonW (1)
2,1 starts at neuron 2 of layer 1, but
then fans out toall threeneurons of layer 2, sincea (1)
2 feeds into every neuron of the
next layer. The chain rule therefore produces a sum overk= 1,2,3:
(3.13) ∂ˆy
∂W (1)
2,1
=
3X
k=1
∂ˆy
∂z (3)
1|{z}
= 1
· ∂z (3)
1
∂a(2)
k|{z}
=W (3)
1,k
· ∂a(2)
k
∂z (2)
k|{z}
=ϕ ′(z(2)
k )
· ∂z (2)
k
∂a(1)
2|{z}
=W (2)
k,2
· ∂a(1)
2
∂z (1)
2|{z}
=ϕ ′(z(1)
2 )
· ∂z (1)
2
∂W (1)
2,1| {z }
=a (0)
.
```

## PDF page 13

```text
PINNS: DIDACTIC DERIVATION OF THE TRAINING CYCLE13
Compare this with the single-path chain rule forW (2)
1,2 in (3.6): the structure is the
same, but now there are three paths (one per neuron in layer 2), and we must sum
over all of them.
Derivative ofˆy′..This is where the complexity grows. Recall that at each hidden
layer, the time derivative of the activation is ˙a (ℓ)
i =ϕ ′(z(ℓ)
i ) ˙z(ℓ)
i , and we saw in (3.7)
that differentiating this product with respect to a parameter that affects both factors
requires the product rule. ForW (1)
2,1 , this product rule applies attwolayers — both
layer 1 and layer 2 — because the parameter’s influence propagates through both.
Product rule at layer 1..At layer 1, the situation is identical to what we saw for
W (2)
1,2 at layer 2. The parameterW (1)
2,1 influences both factors of ˙a (1)
2 =ϕ ′(z(1)
2 ) ˙z(1)
2
through two paths:
•W (1)
2,1 →z (1)
2 →ϕ ′(z(1)
2 ),
•W (1)
2,1 →˙z(1)
2 .
Applying the product rule:
(3.14) ∂˙a(1)
2
∂W (1)
2,1
= ∂ϕ′(z(1)
2 )
∂W (1)
2,1| {z }
=ϕ ′′(z(1)
2 )a (0)
·˙z(1)
2 +ϕ ′(z(1)
2 )· ∂˙z(1)
2
∂W (1)
2,1| {z }
= ˙a(0)
.
Product rule at layer 2..Here is the new element. At layer 2, the product ˙a (2)
k =
ϕ′(z(2)
k ) ˙z(2)
k also depends onW (1)
2,1 — indirectly, through the layer 1 outputs. Both
factors are again affected:
•W (1)
2,1 →a (1)
2 →z (2)
k →ϕ ′(z(2)
k ),
•W (1)
2,1 →˙a(1)
2 →˙z(2)
k .
Applying the product rule at this layer:
(3.15) ∂˙a(2)
k
∂W (1)
2,1
=ϕ ′′(z(2)
k ) ∂z (2)
k
∂W (1)
2,1| {z }
=W (2)
k,2 P (1)
2
·˙z(2)
k +ϕ ′(z(2)
k )· ∂˙z(2)
k
∂W (1)
2,1| {z }
=W (2)
k,2 Q(1)
2
,
where we have introduced a compact notation for the sensitivities arriving from the
previous layer:
(3.16)P (1)
2 = ∂a(1)
2
∂W (1)
2,1
=ϕ ′(z(1)
2 )a (0), Q (1)
2 = ∂˙a(1)
2
∂W (1)
2,1
,
withQ (1)
2 given by (3.14). The notation is suggestive:Pcarries the standard chain
rule sensitivity, whileQcarries the additional sensitivity from the time derivative —
including the product rule contribution from layer 1. Notice howQ (1)
2 from the first
product rule now feeds into the second product rule at layer 2 through (3.15). The
product rulesaccumulateas we move forward through the network.
Assembling the result..The full derivative of ˆy ′ with respect toW (1)
2,1 sums over
all three neurons of layer 2:
(3.17) ∂ˆy′
∂W (1)
2,1
=
3X
k=1
W (3)
1,k
∂˙a(2)
k
∂W (1)
2,1
,
where each term in the sum contains the product rule from (3.15), which itself carries
the accumulated product rule from (3.14).
```

## PDF page 14

```text
14A. TAHIMI
3.4.2. The General Pattern.The first hidden layer example reveals a pattern
that extends to networks of any depth. We now state it precisely as a set of recursive
relations.
For any parameterθat layerℓ, the gradient of the total loss requires∂ˆy/∂θand
∂ˆy′/∂θ. To compute these, we define two sensitivity quantities at each neuronjof
layerm:
(3.18)P (m)
j =
∂a(m)
j
∂θ , Q (m)
j =
∂˙a(m)
j
∂θ .
At the output layer (m=L, identity activation)..The quantities we seek are:
(3.19) ∂ˆy
∂θ =
X
j
W (L)
1,j P (L−1)
j , ∂ˆy′
∂θ =
X
j
W (L)
1,j Q(L−1)
j .
So we needP (L−1)
j andQ (L−1)
j — the sensitivities at the last hidden layer.
At the last hidden layer (m=L−1)..This layer uses a non-linear activation, so
the sensitivities involveϕ ′ andϕ ′′. They are expressed in terms of those arriving from
the previous layer:
P (L−1)
j =ϕ ′(z(L−1)
j )
X
k
W (L−1)
j,k P (L−2)
k ,
(3.20)
Q(L−1)
j =ϕ ′′(z(L−1)
j )
 X
k
W (L−1)
j,k P (L−2)
k
!
˙z(L−1)
j +ϕ ′(z(L−1)
j )
X
k
W (L−1)
j,k Q(L−2)
k .
(3.21)
So we needP (L−2)
k andQ (L−2)
k . The pattern is now clear: each layer’s sensitivities
depend on those of the previous layer.
General recursive relations (m=ℓ+1, . . . , L−1)..The relations above generalize
to any hidden layerm:
P (m)
j =ϕ ′(z(m)
j )
X
k
W (m)
j,k P (m−1)
k ,(3.22)
Q(m)
j =ϕ ′′(z(m)
j )
 X
k
W (m)
j,k P (m−1)
k
!
˙z(m)
j +ϕ ′(z(m)
j )
X
k
W (m)
j,k Q(m−1)
k .(3.23)
These are applied from layerL−1 backward to layerℓ+ 1, where they meet the
initialization at the parameter’s own layer.
Initialization at the parameter’s layer (m=ℓ)..For a weightθ=W (ℓ)
i,j , only
neuronihas nonzero sensitivities:
P (ℓ)
i =ϕ ′(z(ℓ)
i )a (ℓ−1)
j ,(3.24)
Q(ℓ)
i =ϕ ′′(z(ℓ)
i )a (ℓ−1)
j ˙z(ℓ)
i +ϕ ′(z(ℓ)
i ) ˙a(ℓ−1)
j ,(3.25)
withP (ℓ)
n =Q (ℓ)
n = 0 for alln̸=i. For a biasθ=b (ℓ)
i , replacea (ℓ−1)
j with 1 and
˙a(ℓ−1)
j with 0.
```

## PDF page 15

```text
PINNS: DIDACTIC DERIVATION OF THE TRAINING CYCLE15
Total gradient..Combining (3.19) with the loss function, the gradient with re-
spect to any parameterθis:
(3.26) ∂L
∂θ = 2R
 ∂ˆy
∂θ + ∂ˆy′
∂θ

t=tc
+λ2
 
ˆy(0)−1
 ∂ˆy
∂θ

t=0
,
where the initial condition loss contributes only throughP(sinceL IC depends on
ˆy(0) but not on ˆy′(0)).
In practice, none of these sensitivities need to be computed explicitly. Frame-
works such as PyTorch implement automatic differentiation (commonly calledauto-
grad): during the forward pass, every operation is recorded in a computational graph
along with the intermediate quantities — activations, pre-activations, and their deriv-
atives — that appear in the recursive relations above. Callingloss.backward()then
traverses this graph in reverse, combining these stored quantities to compute∇ θLfor
all parameters simultaneously. Higher-order time derivatives, needed for second-order
ODEs or PDEs, are obtained by applying autograd to the output of a previous auto-
grad call, extending the computational graph with each application. The companion
notebook verifies this: every gradient computed by hand in this section is reproduced
identically by PyTorch’s autograd engine.
With the gradient computation now established both by example and in full
generality, a natural question remains: does this training cycle actually converge to
the correct solution? The next section answers this question.
4. Validation: Comparison with the Analytical Solution.The preced-
ing sections dissected a single iteration of the PINN training cycle in full numerical
detail: one forward pass to evaluate the composite loss, one backward pass to com-
pute parametric gradients, and one parameter update via gradient descent. At this
point you might reasonably ask: does this actually work? If we repeat this forward–
backward–update cycle thousands of times, will the network actually find the right
solution?
This section answers that question affirmatively. The 1-3-3-1 MLP is trained to
convergence and its prediction ˆy(t) is compared against the known analytical solution
y(t) =e −t over the continuous domaint∈[0,1]. The goal is to demonstrate that
minimizing a loss function built exclusively from the ODE residual and the initial
condition — without any data sampled from the true solution — is sufficient to
recover the correct physical behavior.
4.1. Training Configuration.To transition from the single-step didactic ex-
ample to a fully trained model, we retain the same 1-3-3-1 MLP architecture and the
tanh activation function from Section 2. However, the manually chosen parameters
from Tables 1 to 3 — which served the specific purpose of enabling hand-verifiable
calculations — are now replaced by astandard random initialization, as would
be used in any practical application. Specifically, we use PyTorch’s default initializa-
tion scheme (Kaiming uniform) with a fixed random seed for full reproducibility. The
training configuration is:
•Collocation points:N c = 30 uniformly spaced points int∈[0,1].
•Optimizer:Adam [12] with learning rateη= 10 −3. This adaptive op-
timizer adjusts step sizes per-parameter, leading to faster and more stable
convergence than the basic gradient descent used in the single-step example
(Section 3).
•Training epochs:15,000 complete iterations of the forward–backward–
update cycle.
```

## PDF page 16

```text
16A. TAHIMI
•Loss weighting:λ= 10, consistent with the value used in the single-step
example.
The composite loss function remains the same as in (2.13):
(4.1)L=L R +λ·L IC = 1
Nc
NcX
i=1

ˆy′(ti) + ˆy(ti)
2
+λ
 
ˆy(0)−1
2
,
where the temporal derivative ˆy ′(ti) at each collocation point is computed via Py-
Torch’s automatic differentiation engine with respect to the network inputt. Note
that this is the same derivative that was computed analytically via forward-mode
differentiation in Section 2; the two approaches yield identical numerical results, as
the reader can verify in the companion notebook.
4.2. Evaluation Protocol and Error Metrics.After training, the network
is evaluated on a fine grid ofN eval = 500 uniformly spaced points in [0,1]. This grid
is deliberately denser than theN c = 30 collocation points used during training, so
that the comparison also tests the network’s ability togeneralizeto unseen locations
within the domain. At each evaluation pointt i, the PINN prediction ˆy(ti) is compared
with the analytical solutiony(t i) =e −ti using two standard error metrics.
Mean Squared Error (MSE)..This metric quantifies the average squared devia-
tion:
(4.2) MSE = 1
Neval
NevalX
i=1
 
ˆy(ti)−y(t i)
2
.
RelativeL 2 Error..This dimensionless metric normalizes the error by the mag-
nitude of the true solution:
(4.3)ϵ L2 = ∥ˆy−y∥2
∥y∥2
=
vuut
NevalX
i=1
 
ˆy(ti)−y(t i)
2
vuut
NevalX
i=1
y(ti)2
.
4.3. Results.
Training Convergence..Table 14 summarizes the evolution of the loss components
during training. The total loss decreases by approximately 6.3 orders of magnitude,
from 1.213×10 1 at the first epoch to 6.273×10 −6 at epoch 15,000. A clear two-
phase dynamic is visible. In the first phase, the heavily weighted initial condition
lossL IC dominates the optimization: it drops from 1.212×10 0 to below 10 −5 by
epoch 2,090, meaning the network learns the correct value att= 0 within the first
∼14% of training. In the second phase, withL IC effectively satisfied, the optimizer
dedicates its full effort to reducingL R across the domain. By the end of training,
the residual loss accounts for nearly all of the total loss (L R = 6.210×10 −6 versus
LIC = 6.341×10 −9, a ratio of approximately 979:1).
Figure 4 visualizes this convergence on a logarithmic scale. The dominance ofL R
in the final training phase is clearly visible: after approximately epoch 3,000, the total
loss curve and theL R curve become virtually indistinguishable, confirming thatL IC
has been fully satisfied. It is worth noting thatL IC exhibits a non-monotonic behavior
at late epochs: after reaching a minimum of 3.139×10 −11 at epoch 12,000, it increases
```

## PDF page 17

```text
PINNS: DIDACTIC DERIVATION OF THE TRAINING CYCLE17
Table 14
Evolution of the loss components during training.
Epoch T otal LossLL R LIC
1 1.213×10 1 1.096×10 −2 1.212×10 0
3 000 7.954×10 −3 7.911×10 −3 4.251×10 −6
6 000 3.069×10 −4 3.067×10 −4 2.845×10 −8
9 000 3.609×10 −5 3.609×10 −5 5.914×10 −10
12 000 1.432×10 −5 1.432×10 −5 3.139×10 −11
15 000 6.273×10 −6 6.210×10 −6 6.341×10 −9
slightly to 6.341×10 −9 at epoch 15,000. This fluctuation is a known consequence of
multi-objective optimization in PINNs [24]: as the optimizer continues to reduceL R,
it may marginally compromiseL IC , since the two loss components share the same set
of parameters. In this case, the fluctuation is entirely inconsequential —L IC remains
nine orders of magnitude below its initial value, and its contribution to the total loss
is negligible.
2000 4000 6000 8000 10000 12000 14000
Epoch
10 13
10 11
10 9
10 7
10 5
10 3
10 1
101
Loss (log scale)
Training Loss History
Total Loss L
LR (ODE residual)
LIC (initial condition)
Fig. 4.Evolution of the total lossLand its components (L R andλ·L IC ) during15,000
training epochs, displayed on a logarithmic scale. The total loss decreases by approximately 6.3
orders of magnitude. After the initial phase,L R dominates the optimization.
Solution Accuracy..Figure 5 presents the central result. The left panel displays
the PINN prediction ˆy(t) superimposed on the analytical solutiony(t) =e −t, evalu-
ated on a fine grid ofN eval = 500 points. The two curves are visually indistinguishable
over the entire domain.
The right panel quantifies this agreement by displaying the pointwise absolute
error|ˆy(ti)−y(t i)|on a logarithmic scale. The maximum error of 5.038×10 −4 occurs
att≈0.26. This spatial error distribution is noteworthy: the region neart= 0
benefits from the strong anchor provided byL IC , while the interior of the domain
relies entirely on theN c = 30 collocation points to enforce the ODE residual. The
error peak in the intermediate region reflects the transition between these two sources
of constraint. The mean absolute error across the domain is 2.294×10 −4, with a
standard deviation of 1.643×10 −4.
Table 15 summarizes the global error metrics, and Table 16 provides the network
predictions at five representative points.
```

## PDF page 18

```text
18A. TAHIMI
0.0 0.2 0.4 0.6 0.8 1.0
t
0.4
0.5
0.6
0.7
0.8
0.9
1.0y(t)
(a) PINN Prediction vs. Analytical Solution
Exact: y(t) = e t
PINN: y(t)
IC: y(0) = 1
0.0 0.2 0.4 0.6 0.8 1.0
t
10 7
10 6
10 5
10 4
|y(t) y(t)|
MSE = 7.96e-08
Rel. L2 = 4.29e-04
Max Err = 5.04e-04
(b) Pointwise Absolute Error
Fig. 5.Validation of the trained PINN against the analytical solutiony(t) =e −t.(a)PINN
predictionˆy(t)(dashed line with circle markers) overlaid on the exact solution (solid line); the curves
are visually indistinguishable.(b)Pointwise absolute error|ˆy(t)−y(t)|on a logarithmic scale. The
maximum error of5.038×10 −4 occurs att≈0.26.
Table 15
Error metrics for the trained PINN evaluated onN eval = 500points in[0,1].
Metric V alue
Mean Squared Error (MSE) 7.961×10 −8
RelativeL 2 Error 4.290×10 −4
Maximum Absolute Error 5.038×10 −4
These results confirm that the 1-3-3-1 MLP, despite its minimal capacity of only
22 trainable parameters, achieves a relativeL 2 error of 0.043% in approximating the
true solution. It bears repeating that at no point during the 15,000 training epochs was
the model given access to any value of the functiony(t) =e −t. The physics encoded
in the loss function was the sole source of information guiding the optimization.
4.4. Discussion and Scope of the Validation.Let us be clear about what
this result does and does not show.
The first-order linear ODEy ′(t) +y(t) = 0 is an elementary problem for which
classical numerical methods — such as fourth-order Runge-Kutta schemes [3] — pro-
vide solutions with machine precision at a fraction of the computational cost required
by the PINN training loop. For this class of well-posed, low-dimensional initial value
problems, PINNs arenotcompetitive with established solvers, nor is it the purpose
of this didactic example to suggest otherwise.
The value of this validation is, instead,conceptual and pedagogical. It demon-
strates the core mechanism of the PINN framework: a neural network, guided solely
by the structure of a differential equation and an initial condition, can discover the
correct physical solution without ever being shown a single data point from that solu-
tion. This “learning from physics alone” paradigm is the foundational building block
upon which all advanced PINN applications are constructed.
The true potential of the PINN methodology emerges in problem classes where
classical methods face significant limitations:
•Inverse problems:Identifying unknown parameters within the governing
```

## PDF page 19

```text
PINNS: DIDACTIC DERIVATION OF THE TRAINING CYCLE19
Table 16
PINN predictions and absolute errors at selected points.
tˆy(t)(PINN)y(t) =e −t (Exact) Absolute Error
0.00 0.999889 1.000000 1.109×10 −4
0.25 0.777907 0.778411 5.032×10 −4
0.50 0.605947 0.605923 2.402×10 −5
0.75 0.471494 0.471657 1.631×10 −4
1.00 0.367655 0.367879 2.244×10 −4
equation — such as diffusion coefficients, reaction rates, or material properties
— from sparse and potentially noisy experimental observations. In an inverse
PINN formulation, these physical parameters are simply added to the set of
trainable variablesθand are learned jointly with the network weights during
optimization [17, 10].
•Data-physics fusion:Combining incomplete or noisy experimental mea-
surements with known physical laws to reconstruct full-field solutions. A
landmark example is the reconstruction of hidden velocity and pressure fields
from flow visualizations [18], a task for which no classical solver can be di-
rectly applied without full boundary condition specification.
•High-dimensional and complex-geometry problems:Partial differen-
tial equations defined on irregular domains or in high-dimensional parameter
spaces, where mesh generation is prohibitive or where classical methods suf-
fer from the curse of dimensionality. Because PINNs are mesh-free, they
circumvent the need for domain discretization entirely.
In each of these settings, the training mechanics remainexactlythose detailed in
this paper: a composite loss function is constructed from the governing equations
and available data, and backpropagation adjusts the network parameters to satisfy
all imposed constraints simultaneously. By mastering these mechanics on the simple
problem treated here, the reader is equipped with the foundational understanding
necessary to approach these more challenging and impactful applications with confi-
dence.
5. Conclusion.This paper has presented a didactic and self-contained intro-
duction to the complete training cycle of a Physics-Informed Neural Network, applied
to a first-order initial value problem. Existing PINN tutorials and guides either del-
egate the internal training mechanics to automatic differentiation libraries or, in the
case of Almqvist [1], derive them explicitly but for a single hidden layer only. The
present work extends this explicit treatment to a multi-layer network, where a richer
gradient structure emerges. Through a fully verifiable numerical example and a sub-
sequent validation against the analytical solutiony(t) =e −t (Section 4), we gave
explicit treatment to four aspects of the training process that are not readily visible
in library-based implementations:
1.Dual forward propagation:During the forward pass, the network output
ˆyand its temporal derivative ˆy′ are propagated simultaneously through the
network, layer by layer, using the chain rule at each stage. This dual propa-
gation is what makes the additional gradient structure of the backward pass
visible.
2.The product rule in backpropagation:For hidden layer parameters, the
temporal derivative ˆy′ depends on both the activations and their derivatives
```

## PDF page 20

```text
20A. TAHIMI
through the same parameter, requiring the product rule — and introducing
the second derivative of the activation functionϕ ′′ even for a first-order ODE.
This is the structural complication that distinguishes PINN backpropagation
from standard neural network backpropagation.
3.The role of the hyperparameterλ:The validation in Section 4 pro-
vided direct empirical evidence of a two-phase training dynamic: theλ= 10
weighting droveL IC below 10 −5 within the first 2,090 epochs, after which
the optimizer redirected its full effort toward minimizing the ODE residual
across the domain.
4.General gradient formulas:The product rule structure observed in the
worked examples was generalized into recursive relations for two sensitivities
—P (m)
j for the activation andQ (m)
j for its time derivative — that prop-
agate from the parameter’s layer through successive layers to the output,
accumulating product rules and fan-out summations at each stage. These
relations extend the gradient computation to networks of arbitrary depth
without requiring case-by-case derivations, and they correspond directly to
the intermediate quantities that automatic differentiation engines store and
combine duringloss.backward().
The validation confirmed that the minimization of the physics-informed loss —
without access to any data from the true solution — is sufficient to recover the correct
physical behavior, achieving a relativeL 2 error of 4.290×10 −4 (0.043%) with a mini-
mal 22-parameter network. While PINNs are not competitive with classical solvers for
this class of elementary problems, the exercise establishes the conceptual foundation
necessary for tackling the problem classes where the framework offers unique ad-
vantages, namely inverse problems, data-physics fusion, and high-dimensional PDEs
(Subsection 4.4).
To bridge the gap between mathematical derivation and practical implementation,
this work is accompanied by an interactive Jupyter Notebook that reproduces every
manual calculation presented in the text using PyTorch’s automatic differentiation
engine, and independently replicates the full training and validation pipeline. The
exact agreement between the hand-derived gradients and PyTorch’s autograd output
serves as mutual validation: the theory verifies the code, and the code verifies the
theory.
As natural extensions of this didactic framework, we envision:
•Higher-order and multi-dimensional problems:Generalizing the didac-
tic analysis to second-order ODEs and to PDEs in two spatial dimensions,
where the interplay between multiple differential operators and boundary
conditions introduces additional complexity in the loss function and gradient
computation.
•Training dynamics and optimization:Investigating the impact of alter-
native activation functions (such as GELU and Swish) on the gradient flow
through the physics-informed loss, and comparing the convergence behavior
of first-order optimizers (Adam [12]) with second-order methods (L-BFGS
[14]), which have shown strong performance in PINN training [17].
•Inverse problems:Extending the framework to identify unknown physi-
cal parameters from experimental or observational data, where the unknown
parameters are added to the trainable setθand learned jointly with the net-
work weights. Benchmarking against classical estimation methods on well-
characterized test problems would clarify both the advantages and limitations
```

## PDF page 21

```text
PINNS: DIDACTIC DERIVATION OF THE TRAINING CYCLE21
of the physics-informed approach.
In each case, the foundational training mechanics and the general gradient formulas
presented here carry over directly. We hope that this work lowers the barrier to entry
into Scientific Machine Learning and encourages the adoption of physics-informed
approaches in both research and education.
Code and Data Availability.This work does not involve experimental or ob-
servational datasets. All results are generated computationally from the governing
differential equation and its initial condition. To guarantee full reproducibility, the
following materials are provided:
1.Source code:The complete Python/PyTorch implementation is provided
as an interactive Jupyter Notebook, structured in two parts:
•Verification of manual calculations (Sections2and3):The notebook al-
gorithmically reproduces every hand-derived value presented in the text
using PyTorch’s automatic differentiation engine, serving as a didactic
bridge between theory and implementation.
•Training and validation (Section4):The notebook executes the full
PINN training pipeline, saves the trained model checkpoint and all eval-
uation metrics, and generates the publication figures.
2.Computational artifacts:The trained model checkpoint (pinn trained
model.pt), evaluation metrics and predictions (pinn results.json), and epoch-
by-epoch loss history (pinn loss history.npz) are provided as supplementary
files. All numerical values reported in Section 4 are read directly from these
saved files, ensuring that the manuscript numbers remain identical regardless
of hardware or re-execution.
The complete codebase, including all computational artifacts, is publicly available at
https://github.com/Tahimi/PINN-Didactic-Training-Cycle and archived with a per-
manent DOI via Zenodo [20].
Acknowledgments.During the development of this work, the authors used
AI-based language models (Claude, Anthropic, 2024–2025) as assistive tools for writ-
ing, code development, and computational verification. All conceptual and scientific
decisions — including the identification of the pedagogical gap, the design of the il-
lustrative example, the selection of which aspects of the training cycle to emphasize,
and the critical discussion of the method’s scope and limitations — originated with
the authors. All mathematical derivations, numerical values, and computational re-
sults were independently verified by the authors, who assume full responsibility for
the integrity, accuracy, and originality of the submitted work.
REFERENCES
[1]A. Almqvist,Fundamentals of physics-informed neural networks applied to solve the Reynolds
boundary value problem, Lubricants, 9 (2021), p. 82.
[2]H. Baty,A hands-on introduction to physics-informed neural networks for solving partial
differential equations with benchmark tests taken from astrophysics and plasma physics,
arXiv preprint, (2024). arXiv:2403.00599.
[3]R. L. Burden and J. D. F aires,Numerical Analysis, Cengage Learning, Boston, MA, 10th ed.,
2015.
[4]S. Cuomo, V. S. Di Cola, F. Giampaolo, G. Rozza, M. Raissi, and F. Piccialli,Scientific
machine learning through physics-informed neural networks: Where we are and what’s
next, J. Sci. Comput., 92 (2022), p. 88.
[5]X. Glorot and Y. Bengio,Understanding the difficulty of training deep feedforward neural
networks, in Proceedings of the 13th International Conference on Artificial Intelligence and
```

## PDF page 22

```text
22A. TAHIMI
Statistics (AISTATS), 2010, pp. 249–256.
[6]I. Goodfellow, Y. Bengio, and A. Courville,Deep Learning, MIT Press, Cambridge, MA,
2016.
[7]K. He, X. Zhang, S. Ren, and J. Sun,Delving deep into rectifiers: Surpassing human-
level performance on ImageNet classification, in Proceedings of the IEEE International
Conference on Computer Vision (ICCV), 2015, pp. 1026–1034.
[8]K. Hornik, M. Stinchcombe, and H. White,Multilayer feedforward networks are universal
approximators, Neural Netw., 2 (1989), pp. 359–366.
[9]A. D. Jagtap, K. Kawaguchi, and G. E. Karniadakis,Adaptive activation functions accel-
erate convergence in deep and physics-informed neural networks, J. Comput. Phys., 404
(2020), p. 109136.
[10]G. E. Karniadakis, I. G. Kevrekidis, L. Lu, P. Perdikaris, S. W ang, and L. Yang,Physics-
informed machine learning, Nat. Rev. Phys., 3 (2021), pp. 422–440.
[11]D. Katsikis, A. D. Muradova, and G. Stavroulakis,A gentle introduction to physics-
informed neural networks, with applications in static rod and beam problems, J. Adv.
Appl. Comput. Math., 9 (2022), pp. 103–128.
[12]D. P. Kingma and J. Ba,Adam: A method for stochastic optimization, in Proceedings of the
3rd International Conference on Learning Representations (ICLR), 2015.
[13]I. E. Lagaris, A. Likas, and D. I. Fotiadis,Artificial neural networks for solving ordinary
and partial differential equations, IEEE Trans. Neural Netw., 9 (1998), pp. 987–1000.
[14]D. C. Liu and J. Nocedal,On the limited memory BFGS method for large scale optimization,
Math. Program., 45 (1989), pp. 503–528.
[15]L. McClenny and U. Braga-Neto,Self-adaptive physics-informed neural networks using a
soft attention mechanism, J. Comput. Phys., 474 (2023), p. 111722.
[16]A. Ogueda-Oliva and P. Seshaiyer,Literate programming for motivating and teaching neural
network-based approaches to solve differential equations, Int. J. Math. Educ. Sci. Technol.,
55 (2024), pp. 2657–2685.
[17]M. Raissi, P. Perdikaris, and G. E. Karniadakis,Physics-informed neural networks: A deep
learning framework for solving forward and inverse problems involving nonlinear partial
differential equations, J. Comput. Phys., 378 (2019), pp. 686–707.
[18]M. Raissi, A. Yazdani, and G. E. Karniadakis,Hidden fluid mechanics: Learning velocity
and pressure fields from flow visualizations, Science, 367 (2020), pp. 1026–1030.
[19]V. Sitzmann, J. N. P. Martel, A. W. Bergman, D. B. Lindell, and G. Wetzstein,Implicit
neural representations with periodic activation functions, in Advances in Neural Informa-
tion Processing Systems (NeurIPS), vol. 33, 2020, pp. 7462–7473.
[20]A. Tahimi,Supplementary code for: Physics-informed neural networks: A didactic derivation
of the complete training cycle, 2026, https://doi.org/10.5281/zenodo.19641577. https://
github.com/Tahimi/PINN-Didactic-Training-Cycle.
[21]I. Thawon, D. Vo, T. Q. Bui, K. Rattanamongkhonkun, C. Chamroon, N. Tippayawong,
Y. Mona, R. W anison, and P. Suttakul,Physics-informed neural networks: Current
progress and challenges in computational solid and structural mechanics, Comput. Model.
Eng. Sci., 146 (2026), https://doi.org/10.32604/cmes.2026.077044.
[22]S. W ang, S. Sankaran, and P. Perdikaris,Respecting causality in forward and inverse
physics-informed neural networks, Comput. Methods Appl. Mech. Engrg., 418 (2024),
p. 116527.
[23]S. W ang, S. Sankaran, H. W ang, and P. Perdikaris,An expert’s guide to training physics-
informed neural networks, arXiv preprint, (2023). arXiv:2308.08468.
[24]S. W ang, Y. Teng, and P. Perdikaris,Understanding and mitigating gradient flow patholo-
gies in physics-informed neural networks, SIAM J. Sci. Comput., 43 (2021), pp. A3055–
A3081.
```
