# arXiv:2601.06244 — PDF 原文文本提取

- Source: https://arxiv.org/abs/2601.06244
- Local PDF: `arxiv-2601.06244.pdf` (local only)
- PDF SHA-256: `fa40b8efaff3f822ad902f16748e36cc844f8f727e72b8d1e007c7b2dae015c2`
- Converted at: 2026-10-06T23:51:12.085865+00:00
- Extractor: pypdf/6.10.0
- Pages: 6
- Pages without extractable text: none

> 逐页提取 PDF 文本，未使用模型改写或翻译，未进行内容核验。保留页码；多栏阅读顺序、公式、表格和图片可能不能准确还原。无文字页需要另行 OCR，不能视为完整文本覆盖。基础 ID 的具体版本尚未解析，以 PDF 哈希标识本次原文件。

## PDF page 1

```text
Accepted manuscript of the paper presented at ParCFD2024
35th International Conference on Parallel Computational Fluid Dynamics
Sep 02-04 2024, Bonn, Germany
The final published version is available at https://doi.org/10.34734/FZJ-2025-02453
HARD CONSTRAINT PROJECTION IN A PHYSICS
INFORMED NEURAL NETWORK
Miranda J. S. Horne ∗, Peter K. Jimack ∗, Amirul Khan†, AND He Wang ‡
∗†University of Leeds
∗School of Computing, †School of Civil Engineering
Woodhouse Lane, Leeds, LS2 9JT, UK
scmho, p.k.jimack, a.khan@leeds.ac.uk, www.leeds.ac.uk
‡University College London
Department of Computer Science
Gower Street, London, WC1E 6BT, UK
he wang@ucl.ac.uk, https://profiles.ucl.ac.uk/93306-he-wang
Key words:Physics Informed Machine Learning, Hard Constraints, Navier Stokes Equa-
tions, Non-Linear PDE
Summary:In this work, we embed hard constraints in a physics informed neural network
(PINN) which predicts solutions to the 2D incompressible Navier Stokes equations. We
extend the hard constraint method introduced by Chen et al. (arXiv:2012.06148) from
a linear PDE to a strongly non-linear PDE. The PINN is used to estimate the stream
function and pressure of the fluid, and by differentiating the stream function we can
recover an incompressible velocity field. An unlearnable hard constraint projection (HCP)
layer projects the predicted velocity and pressure to a hyperplane that admits only exact
solutions to a discretised form of the governing equations.
1 INTRODUCTION
Machine learning provides a promising framework to simulate fluid dynamics at a
fraction of the computational cost of traditional numerical methods[1]. Furthermore, the
incorporation of domain knowledge into a neural network can improve the prediction
accuracy, increase the model’s explainability, and result in a neural network that is less
reliant on training data. Typically, the incorporation of the physical constraints into
a neural network is only weakly enforced, for example, a PINN[2] weakly enforces the
governing equation by incorporating a penalty term (often the equation’s residuals) into
the loss function. In the cases where a physical constraint is strongly imposed, the enforced
governing equation is often either linear[3], or an additional conservation law (such as the
incompressibility constraint[4]). In this paper we propose a method to strictly enforce the
discretised form of a nonlinear partial differential equation, through projection, inspired
by the linear analogue used by Chen et al. in 2021[3].
arXiv:2601.06244v1  [physics.flu-dyn]  9 Jan 2026
```

## PDF page 2

```text
Miranda J. S. Horne, Peter K. Jimack, Amirul Khan, and He Wang
2 PHYSICS INFORMED NEURAL NETWORK (PINN)
We will consider the 2D incompressible Navier Stokes equations (1,2,3)[5]. The solution
of this system is given by the 2D instantaneous velocity (u(x,y,t),v(x,y,t)) and the
pressure (p(x,y,t)) of the fluid, wherex,yare the spatial coordinates, andtis the temporal
coordinate. The kinematic viscosity of the fluid is given byν, and the constant density
byρ.
0 = ∂u
∂t+
(
u∂u
∂x+v ∂u
∂y
)
−ν∂2u
∂x2−ν∂2u
∂y2 + 1
ρ
∂P
∂x (1)
0 = ∂v
∂t+
(
u∂v
∂x+v ∂v
∂y
)
−ν∂2v
∂x2−ν∂2v
∂y2 + 1
ρ
∂P
∂y (2)
0 = ∂u
∂x+ ∂v
∂y (3)
The network proposed is a feed forward neural network (FFNN) that takes as input the
coordinates of the system (x,y,t) and outputs a prediction of the stream function (ψ) and
the pressure (p) at those coordinates. The velocity components are defined asu=∂ψ/∂y,
v=−∂ψ/∂x, using the automatic differentiation[6] (AD) built into the network. This
method strictly imposes the incompressiblity (3) of the system.
As just coordinates alone would be insufficient to predict a unique solution, we useN
ground truth solutions (ui,vi) to anchor the model’s predictions (ˆui, ˆvi) to our test case.
The data error (DE, 4) measures the distance between the ground truth solutions and
the network predictions. We calculate the data error only on the velocity as in practice it
would be significantly more difficult to measure the pressure of a fluid through the domain
than the velocity when creating the ground truth data set.
DE = 1
N
N∑
i=1
(ui−ˆui)2 + 1
N
N∑
i=1
(vi−ˆvi)2 (4)
Training the FFNN using only the DE would neglect the other knowledge we have
of the system, the governing PDE. A PINN[2] appends the loss function to include some
measure of the prediction’s deviation from the governing equations, the physics error (PE,
5). The Navier Stokes equation residuals (NSER) are found by evaluating the RHS of (1)
and (2) using AD forMof the network predictions at locations (x i,yi,ti), denotedr x
i and
ry
i , fori∈{1,...,M}.
PE = 1
M
M∑
i=1
(rx
i )2 + 1
M
M∑
i=1
(ry
i )2 (5)
In some PINN literature (e.g.[2]) the error from the initial condition and boundary
conditions are incorporated in the loss function as separately weighted penalty terms.
In the models presented here, the values on the spatial and temporal boundaries are
incorporated into the data error, such that the loss function is defined only as a weighted
sum of the DE and PE.
```

## PDF page 3

```text
Miranda J. S. Horne, Peter K. Jimack, Amirul Khan, and He Wang
Figure 1: HCP-PINN architecture. The left box is the FFNN with learnable weights and
biases, and the right box is the unlearnable HCP.
3 HARD CONSTRAINT PROJECTION (HCP)
The HCP-PINN has the same learnable network and loss function as a PINN, but
between the initial prediction of the solution and the loss evaluation there is an unlearn-
able hard constraint projection layer (see figure 1). Following the methodology used by
Chen et al.[3], the governing equations (1,2) are discretised with a central finite difference
scheme for the spatial derivatives, and a backwards finite difference scheme for the tem-
poral derivatives. The discretised forms of the governing equations are then decomposed
into two matrices, the constraint matrixA(containing all the constant terms) and the
prediction matrixB(containing all of the transient terms) such that multiplyingAB
recovers the discretised governing equations (6).
Using tools from linear algebra we can define the projection matrix asP=I−
AT (AAT )−1A. When an arbitrary prediction matrix (B) is multiplied by the projection
matrix,PB=B ′, the outcome (B′) is the closest point toBthat lies on the hyperplane
AB= 0. Thus, the predictions after projection satisfy the discretised form of the gov-
erning equations exactly. For a proof of this, please see the appendix of the paper by
Chen et al.[3]. In practice, each prediction matrix contains only the values from one finite
difference stencil, so each of theB i in figure 1 corresponds to each of the input coordinate
tuples (x,y,t).
AB=


1/∆t
1/∆t
1/∆x
1/∆x
1/∆x
1/∆y
1/∆y
1/∆y
1/(∆x) 2
1/(∆y) 2


T 

u v
−u−∆t −v−∆t
1
2u(u+∆x−u−∆x) 1
2u(v+∆x−v−∆x)
1
2ρP+∆x 0
−1
2ρP−∆x 0
1
2v(u+∆y−u−∆y) 1
2v(v+∆y−v−∆y)
0 1
2ρP+∆y
0 −1
2ρP−∆y
ν(−u+∆x + 2u−u−∆x)ν(−v+∆x + 2v−v−∆x)
ν(−u+∆y + 2u−u−∆y)ν(−v+∆y + 2v−v−∆y)


(6)
```

## PDF page 4

```text
Miranda J. S. Horne, Peter K. Jimack, Amirul Khan, and He Wang
Figure 2: Graphs comparing the value of the loss, data error, and physics error, on the
test and training set, during the training of both models.
4 PROVISIONAL RESULTS
To test the HCP-PINN, two models were trained, a PINN with no HCP layer, and a
HCP-PINN as depicted in figure 1. Both models had 6 hidden layers with 50 neurons each,
and were optimised with default settings of the Adam[7] optimiser with a loss function
defined asL= 0.9DE+0.1PE. The hyperbolic tangent was used as the activation function.
The discretisation used in the hard constraint projection has values ∆x= ∆y= ∆t=
0.01.
The models were trained and tested on one dataset of periodic vortex shedding past
a bluff body. The data domain is defined byt∈[0,10],x∈[1,8], andy∈[−2,2],
downstream of the bluff body and with the wake fully realised. The training dataset
was random uniformly sampled across the domain withN= 500 ground truth data
points (230 of which lie on the spatial and temporal boundaries) andM= 1000 physics
collocation points. The test dataset is selected on a grid witht={1.6,4.8,8.0}and
∆x= 0.7070,∆y= 0.8164 which both the test DE and the test PE are evaluated on
(Ntest =M test = 150).
The training trajectory of the performance of the models can be seen in figure 2,
and the predicted velocity fields att= 4.8 are displayed alongside the ground truth in
figure 3. We see that the training trajectories of the two models follow a similar shape,
implying that the HCP-PINN optimises in a similar manner to the vanilla PINN. This is
supported by the predictions in figure 3, where the two models predict similar flow fields
that qualitatively represent the key features of the flow. We would not expect the physics
error of the HCP-PINN to be exactly zero, as the governing equation is only exactly
obeyed in its discretised form, locally. Unfortunately, we also find that the physics error
associated with the HCP-PINN is not consistently lower than for the PINN, which was
one of the motivations behind this implementation.
An established issue in the literature on the training of PINNs is the imbalance between
loss function terms[8], and it was hoped by the authors that we would find the HCP-PINN
less sensitive to the hyperparameterwin the functionL= (w)DE + (1−w)PE. We had
also anticipated that the HCP-PINN would potentially be less dependent on the quantity
and sampling strategy for the physics collocation points, especially since the calculation of
the residual at these points is a computational bottle-neck for both models. We report that
the HCP-PINN and PINN appear to respond equally sensitively from our studies into this
```

## PDF page 5

```text
Miranda J. S. Horne, Peter K. Jimack, Amirul Khan, and He Wang
Figure 3: Ground truth velocity field, and corresponding model predictions at epoch 750,
of the velocity field att= 4.8.
(which have been omitted from the extended abstract for brevity). The authors suspect
that the hard constraint projection, despite requiring greater computational resources,
has a minimal effect on the predictions made during training, as implied by the similar
training trajectories and predictions in figures 2 and 3.
The authors intend to look into modifying the implementation of the HCP-PINN, with
the intention of more favourable results. We will look into the execution of the HCP, which
uses a low order and potentially unstable discretisation, and a non-unique decomposition
of the governing equation. We will also look at employing established machine learning
methods such as batch training and transfer learning with the goal of fully exploring
the potential of this method. We finally note that Chen et al.[3] investigated only one
linear PDE when originally proposing this method for hard constraint projection, and it
is possible that the HCP method is only appropriate for a subset of PDEs, such as linear
or weakly non-linear PDEs.
5 CURRENT WORK
We aim to refine the HCP-PINN further. The directions stated in the previous section
will be our immediate goals, however this model also has the potential to embed the
boundary conditions strictly through the use of ghost cells. Additionally, we would like
to investigate the model’s robustness to noise and outliers, generalisability to other flow
regimes, and extrapolation capabilities given only boundary and initial conditions.
REFERENCES
[1] S. L. Brunton, B. R. Noack, and P. Koumoutsakos, “Machine learning for fluid me-
chanics,”Annual Review of Fluid Mechanics, vol. 52, 2020.
[2] M. Raissi, P. Perdikaris, and G. Karniadakis, “Physics-informed neural networks: A
deep learning framework for solving forward and inverse problems involving nonlinear
```

## PDF page 6

```text
Miranda J. S. Horne, Peter K. Jimack, Amirul Khan, and He Wang
partial differential equations,”Journal of Computational Physics, vol. 378, 2019.
[3] Y. Chen, D. Huang, D. Zhang, J. Zeng, N. Wang, H. Zhang, and J. Yan, “Theory-
guided hard constraint projection (HCP): A knowledge-based data-driven scientific
machine learning method,”Journal of Computational Physics, vol. 445, 2021.
[4] A. T. Mohan, N. Lubbers, M. Chertkov, and D. Livescu, “Embedding hard physical
constraints in neural network coarse-graining of three-dimensional turbulence,”Phys.
Rev. Fluids, vol. 8, 2023.
[5] A. R. Paterson,A First Course in Fluid Dynamics. Cambridge University Press, 1983.
[6] A. G. Baydin, B. A. Pearlmutter, A. A. Radul, and J. M. Siskind, “Automatic dif-
ferentiation in machine learning: a survey,”Journal of Machine Learning Research,
vol. 18, 2018.
[7] D. P. Kingma and J. Ba, “Adam: A Method for Stochastic Optimization,”ArXiv,
2017. arxiv.org/abs/1412.6980.
[8] S. Wang, S. Sankaran, H. Wang, and P. Perdikaris, “An Expert’s Guide to Training
Physics-informed Neural Networks,”ArXiv, 2023. arxiv.org/abs/2308.08468.
```
