# arXiv:2604.16592 — PDF 原文文本提取

- Source: https://arxiv.org/abs/2604.16592
- Local PDF: `2026-04-17-human-cognition-in-machines-a-unified-perspective-of-world-models-arxiv-2604.16592.pdf` (local only)
- PDF SHA-256: `3c60864cb9014b16ab5308b4b8ac45d25b2125fb5b55cc0ac79aff56413e9314`
- Converted at: 2026-10-06T23:51:14.258816+00:00
- Extractor: pypdf/6.10.0
- Pages: 54
- Pages without extractable text: none

> 逐页提取 PDF 文本，未使用模型改写或翻译，未进行内容核验。保留页码；多栏阅读顺序、公式、表格和图片可能不能准确还原。无文字页需要另行 OCR，不能视为完整文本覆盖。基础 ID 的具体版本尚未解析，以 PDF 哈希标识本次原文件。

## PDF page 1

```text
Human Cognition in Machines: A Unified Perspective of
World Models
TIMOTHY RUPPRECHT∗† ,Northeastern University, USA and EmbodyX Inc., USA
PU ZHAO∗,Northeastern University, USA
AMIR TAHERIN∗,Northeastern University, USA
ARASH AKBARI∗,Northeastern University, USA
ARMAN AKBARI∗,Northeastern University, USA
YUMEI HE∗,Tulane University, USA
TOOBA IMTIAZ∗,Northeastern University, USA
SEAN DUFFY,Northeastern University, USA
JUYI LIN,Northeastern University, USA
YIXIAO CHEN,Northeastern University, USA and EmbodyX Inc., USA
RAHUL CHOWDHURY,Northeastern University, USA
ENFU NAN,Northeastern University, USA
YIXIN SHEN,Northeastern University, USA and Cornell University, USA
YIFAN CAO,Northeastern University, USA and EmbodyX Inc., USA
HAOCHEN ZENG,EmbodyX Inc., USA
CHEN WANG,EmbodyX Inc., USA
WEIWEI CHEN,EmbodyX Inc., USA
GENG YUAN,Northeastern University, USA and University of Georgia, USA
JENNIFER DY,Northeastern University, USA
SARAH OSTADABBAS,Northeastern University, USA
XUAN ZHANG,Northeastern University, USA
DAVID KAELI,Northeastern University, USA
EDMUND YEH,Northeastern University, USA
YANZHI WANG† ,Northeastern University, USA
∗These authors contributed equally to this research.
†These authors are corresponding authors for this research.
Authors’ Contact Information: Timothy Rupprecht, Northeastern University, Boston, MA, USA and EmbodyX Inc., San
Mateo, CA, USA; Pu Zhao, Northeastern University, Boston, MA, USA; Amir Taherin, Northeastern University, Boston,
MA, USA; Arash Akbari, Northeastern University, Boston, MA, USA; Arman Akbari, Northeastern University, Boston,
MA, USA; Yumei He, Tulane University, New Orleans, LA, USA; Tooba Imtiaz, Northeastern University, Boston, MA, USA;
Sean Duffy, Northeastern University, Boston, MA, USA; Juyi Lin, Northeastern University, Boston, MA, USA; Yixiao Chen,
Northeastern University, Boston, MA, USA and EmbodyX Inc., San Mateo, CA, USA; Rahul Chowdhury, Northeastern
University, Boston, MA, USA; Enfu Nan, Northeastern University, Boston, MA, USA; Yixin Shen, Northeastern University,
Boston, MA, USA and Cornell University, Ithaca, NY, USA; Yifan Cao, Northeastern University, Boston, MA, USA and
EmbodyX Inc., San Mateo, CA, USA; Haochen Zeng, EmbodyX Inc., San Mateo, CA, USA; Chen Wang, EmbodyX Inc.,
San Mateo, CA, USA; Weiwei Chen, EmbodyX Inc., San Mateo, CA, USA; Geng Yuan, Northeastern University, Boston,
MA, USA and University of Georgia, Athens, GA, USA; Jennifer Dy, Northeastern University, Boston, MA, USA; Sarah
Ostadabbas, Northeastern University, Boston, MA, USA; Xuan Zhang, Northeastern University, Boston, MA, USA; David
Kaeli, Northeastern University, Boston, MA, USA; Edmund Yeh, Northeastern University, Boston, MA, USA; Yanzhi Wang,
Northeastern University, Boston, MA, USA.
©2026 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM XXXX-XXXX/2026/6-ART
https://doi.org/10.1145/nnnnnnn.nnnnnnn
, Vol. 1, No. 1, Article . Publication date: June 2026.
arXiv:2604.16592v2  [cs.RO]  15 Jun 2026
```

## PDF page 2

```text
2 Rupprecht et al.
This report of world models distinguishes prior works by the cognitive functions they innovate. Many works
claim an almosthuman-like cognitive capability in their world models. To evaluate these claims requires a
proper grounding in first principles from human and machine cognition theory. In moving towardshuman-like
world models we present a conceptual unified framework for world models that fully incorporates all the
cognitive functions (i.e., memory, perception, language, reasoning, imagining, motivation, and metacognition)
and identify gaps in existing research as a guide for future states of the art. In particular, we find that motivation
(especially intrinsic motivation) and metacognition remain drastically under-researched, and we propose
concrete directions to address these gaps informed by active inference and global workspace theory. We also
introduce epistemic world models, a new category encompassing agent frameworks for scientific discovery
that operate over structured knowledge. Our taxonomy, applied to video, embodied, and epistemic world
models, suggests research directions where prior taxonomies have not.
Additional Key Words and Phrases: World Models, Vision Language Action Models, World Action Models,
Machine Cognition
ACM Reference Format:
Timothy Rupprecht, Pu Zhao, Amir Taherin, Arash Akbari, Arman Akbari, Yumei He, Tooba Imtiaz, Sean
Duffy, Juyi Lin, Yixiao Chen, Rahul Chowdhury, Enfu Nan, Yixin Shen, Yifan Cao, Haochen Zeng, Chen Wang,
Weiwei Chen, Geng Yuan, Jennifer Dy, Sarah Ostadabbas, Xuan Zhang, David Kaeli, Edmund Yeh, and Yanzhi
Wang. 2026. Human Cognition in Machines: A Unified Perspective of World Models. 1, 1 (June 2026), 54 pages.
https://doi.org/10.1145/nnnnnnn.nnnnnnn
1 Introduction
World models have become a central abstraction for building intelligent machines. At their core,
world models learn internal representations of an external environment and use them to predict how
that environment may evolve over time [43]. Contemporary world models learn an environment’s
spatial and temporal characteristics for representation and generation [ 75]. More recently, the
definition has expanded to include a model’s capability to predict how an environment will evolve
under counterfactual actions [121]. Across video generation, embodied agents, and language-based
reasoning systems, world models are increasingly expected not only to represent the world, but
also to support imagination, decision-making, and adaptive behavior.
However, this rapid expansion has also created conceptual ambiguity. Many recent world models
are described using cognitive or anthropomorphic language. They are said to understand scenes,
imagine futures, reason about actions, remember past states, or behave in increasingly human-like
ways [1, 95, 109, 110, 228]. Such descriptions are useful when they point to concrete computational
capabilities, but they can also obscure what a model actually does. As a result, the field lacks a
shared vocabulary for distinguishing which cognitive functions are present, which are absent, and
which remain aspirational for world models.
This is why a human cognition perspective is necessary. When world models are evaluated,
compared, or advertised in cognitive terms, the comparison should be grounded in a principled
account of cognition. Cognitive Architecture Theory (CAT), especially the functional decomposition
proposed by Newell, provides a foundation by identifying key components of cognition, including
memory, perception, language, reasoning, imagination, motivation, and metacognition [149]. This
perspective allows us to move beyond broad claims of human-like intelligence and ask more precise
questions: What cognitive functions does a given world model implement? How are these functions
represented computationally? Which functions are underdeveloped in current systems? And how
might progress in one domain inform another?
In this survey, we use human cognition as an organizing lens for understanding contemporary
world models. Rather than treating world models as a single technical category, we analyze them
according to the cognitive functions they emulate, approximate, or neglect. From this synthesis, we
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 3

```text
Human Cognition in Machines: A Unified Perspective of World Models 3
identify two critically under-researched cognitive components: motivation and metacognition. Cur-
rent state-of-the-art world models depend on externally specified reward functions, hand-designed
objectives, or task-specific prompts, rather than intrinsic mechanisms for curiosity, uncertainty
reduction, or self-directed goal formation. Likewise, few of them possess metacognitive mechanisms
that monitor their own uncertainty, evaluate the reliability of their internal predictions, or regulate
reasoning and action based on self-assessment. These missing components limit the extent to which
current world models can support autonomous, adaptive, and robust intelligence.
Our report spans three domains of contemporary world model research, including 1) video
world models (Sec. 4) generate future visual states conditioned on observations and actions, where
maintaining spatial consistency and long-horizon temporal coherence remain central challenges. 2)
embodied world models (Sec. 5) extend these demands to physical settings, requiring perception of
contact geometry, memory of persistent environments, and reasoning over force propagation to
guide real-world task execution. Beyond these established domains, we propose a new category
we callepistemic world models(Sec. 6), in which the environment is not a physical scene but a
structured knowledge space interacted with by an agent framework. Epistemic world models are
contrasted with what we refer to as latent world models that learn spatial and temporal dynamics
over a learned latent state space, comprising most prior world model works. In the epistemic setting,
agents with an VLM or LLM backbone are already world models themselves [ 66, 72], but when
combined with an agent harness and a human-in-the-loop to provide additional reasoning and
motivation, an agent updates its world state within a global workspace defined through easy-to-
interpret language. Epistemic world models also provide early instantiations of the metacognitive
mechanisms that latent world models currently lack, making them both a distinct research domain
and a source of solutions for the gaps our taxonomy reveals.
The contributions of our report are as follows:
(1) We are among the first to provide a comprehensive review of contemporary world models
grounded in human-machine cognition.
(2) We propose a unified world model as a conceptual road-map for incorporating all the compo-
nent parts of cognitive architecture for robust world representation and generation.
(3) We identify motivation and metacognition as critical but underexplored components of
current world models and discuss research directions.
(4) We introduce epistemic world models as a new category of world model in which agents
represent, update, and reason over structured knowledge spaces.
2 Background
Our report spans these three interrelated research tracks as summarized in Figure 1. Previous
world model surveys create a coarse dichotomy in their taxonomies. They classify world models
as 1) world representations [10, 17, 63, 66, 79], and 2) world generators [91, 101, 210, 224, 226]. In
Figure 2 our finer dichotomy of world models is shown with exemplary works that innovate on their
primary cognitive function. Our taxonomy draws on lessons from the fields of human and machine
cognition that we will review in this section. While our taxonomy is not explicit in prior work, it
emerges naturally when aligning model capabilities with longstanding [7, 116, 118, 146, 149] and
recent [61, 162, 168] cognitive architectures. We discuss the research tracks from Figure 1 now, first
by reviewing world model research in Sec. 2.1, then by reviewing human and machine cognition in
Sec. 2.2.
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 4

```text
4 Rupprecht et al.
World
Models Dreamer GPT-3 JEPA
Encodings
COSMOS,
Pi-Model,
Marble
World Models
20252024202020192018
More
Human-like
World Models
2026 - ?
GlobalWorkspace
Theory
Language &Meta-
cognition
Shared
Intentions
Active
Inference
202220081990s1988
Mental
Models
1943
Hierarchical
Thinking
1972
Human Cognition
UnifiedTheories of
Cognition
ImageNet Attention
Networks
SoarCognitive
Architecture
TowardsAutonomous
Machines
Machine Cognition
20222019201720141990
ActiveInference &
ArtificialReasoning
2025
Fig. 1. Our survey studies the convergence of three different but inter-related fields: human cognition,
machine cognition, and world models.
2.1 World Models
The seminal work oncontemporaryworld Models is from Ha et al. (2018) [75] proposing a framework
enabling dreamer architectures [75]. However, world models have been in use long before this
framework solidified with antecedents in control theory [26], machine cognition [7, 118, 149, 150],
and early neural network theory [ 151]. Early world models were trained with Reinforcement
Learning (RL) to learn action policies for direct robotic motor control [75, 222]. The scope has since
expanded to include multi-modal video world models capable of generating vibrant visuals [202],
embodied WMs for mapping and locomotion [90, 96], and as we will argue, should also expand to
world models used within agent frameworks [69, 70, 155, 179].
A review of recent surveys of state-of-the-art World Models [51, 54, 126, 135, 136, 139, 232, 245]
shows that in order to support planning and decision-making, especially in embodied settings [84,
126, 139], world models consistently function as simulators that 1) represent current world structure
and 2) predict future world dynamics [ 51]. Recent works also survey advances in video world
models [245], embodiment [126], temporal–spatial modeling [136], and physical realism [135], all
highlighting challenges in long-horizon consistency, computational efficiency, and alignment to
real-world physics. The available surveys also focus on domain application [54, 126, 135, 139, 245],
architectural or input modality distinctions [136], or abstract taxonomies [51, 232]. For a benchmark
of video world models aligned with physical laws see recent work PhyGround [132] with its public
leader board [133].
As demonstrated in Table 1, we are among the first to systematically distinguish recent states of
the art by the cognitive functions they primarily innovate (further discussed in Sec. 2.3). Surveys
near-universally discuss the foundational models and works from state-of-the-art teams at META
AI with Yann LeCun [65, 80, 242], the Alibaba group [209], Cosmos from Nvidia [108], Berkeley
University’s Sergey Levine’s group [96] and Stanford University’s Fei-Fei Li’s group [90, 212, 234].
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 5

```text
Human Cognition in Machines: A Unified Perspective of World Models 5
Survey Year Video Embodied Simulation Phys. Align. Epistemic CAT Primary Distinction
Ding et al. [51] 2025✓ ✓World understanding vs. prediction
Li et al. [126] 2025✓ ✓Embodied AI and simulators
Yue et al. [245] 2025✓ ✓Roadmap for visual world simulation
Long et al. [139] 2025✓ ✓Simulators for embodied intelligence
Lin et al. [135] 2025✓ ✓Physics alignment in video gen.
Liu et al. [136] 2025✓ ✓Architectural and input distinctions
Xu et al. [232] 2026✓ ✓Specialist-to-generalist progression
Dong et al. [54] 2026✓ ✓Learning to model the world in AI
Ours 2026✓ ✓ ✓ ✓ ✓ ✓Cognitive architecture theory
Table 1. Comparison of world model survey scope. A check ( ✓) indicates that the survey explicitly covers the
corresponding domain. To the best of our knowledge, our survey is among the first to examine world models
from a human-cognition perspective by relating recent advances to the cognitive functions they emulate or
extend, using Cognitive Architecture Theory (CAT) as an organizing framework.
Additional states-of-the-art innovate on architecture by using Vision-Action [ 124] and Vision-
Action-Language models [203], auto-regression models [63], and diffusion models [128, 254]. Nev-
ertheless, a framework for a Unified World Model remains elusive to researchers. A divide remains
in the designs for general-purpose and domain-specific world models [232].
2.2 Cognitive Architecture Theory
The capabilities of world models regularly draw comparisons to the abilities of their human
counterparts [110, 221, 228]. This contributes to a widely held public belief that LLMs, world
models, and similar generative AI approach human-like reasoning capabilities, are conscious, or
herald imminent artificial general intelligence [38, 104, 173]. Without proper grounding in first-
principles thinking from Cognitive Architecture Theory, these comparisons are misleading and
often overstate the capabilities of our non-human counter-parts.
Any study of cognition, human or otherwise, begins with the work of Kenneth Craik who
was a pioneer of cognitive sciences, and amongst the first to describe the mental models humans
create of the world. In his seminal work [43], he theorized that humans use these models of the
world to predict future states of the world, much like the world models we discuss in this report.
Posthumously, his work compared humans to a servomechanism that performs discrete tasks from
taking in sensory input, making a decision, and then following through on the decision [41, 42].
More recently, Grush argues this same sensorimotor loop in humans, identified by Craik, creates
neural circuitry within the brain modeling the world and this can be emulated in motor control [71].
Sensorimotor engagement with the world confirms or rejects model expectations of the sensory
feedback to enhance and process sensory information of future events. This thinking will be used
in both human and machine cognitive architectures.
2.2.1 Cognitive Architecture in Humans.To say a world model achievesHuman-like capabilities
in cognition requires a first-principle investigation of Cognitive Architecture Theory in humans.
Human cognition includes component parts such as motor skills, adaptive learning, perception,
symbolic reasoning with language, and memory [43, 53, 71, 100, 204]. Human cognition also includes
metacognition, or consciousness, and refers to a human’s ability to self-monitor on more complex
tasks [11, 112, 170]. This simply put can be described asthinking about thinking,reasoning about
reasoning. This metacognition in humans can best be visualized through Baar’s theater analogy
used to describe his Global Workspace Theory as an explanation for human consciousness. In
Global Workspace Theory, there exist component parts of cognition such as memory, language,
and sensory processing, and these correspond to the actors, and props on stage with a director
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 6

```text
6 Rupprecht et al.
offstage giving feedback during rehearsal. A spotlight moves from component to component as a
human’s conscious thinking invokes memories and sensory processing one at a time. Despite the
spotlight’s illusion, all the component parts of the theater remain present, and interact even when
the spotlight moves on to focus attention on something else on the stage.
Language as symbolic reasoning is relevant to our understanding of world models because both
these and humans share the input and output modality of textual language. Early and modern
experts on the development of human language have argued that language is a tool in response to
external factors like natural selection [45, 163], and is used to influence the external world [27, 131].
An emerging view argues that language evolved from humans’ ability to share intentions (i.e.
humans’ ability to share goals, to share attention or to share common ground) [ 205]. Human
language exists in reference to a world model shared between a party of humans.
From a review of first principles regarding how both human cognition and consciousness
have evolved in humans, we assert the role of language is paramount. We look to the works of
evolutionary biologist Terrance Deacon [ 47] and psychologists Julian Jaynes [ 100] and Merlin
Donald [53]. Deacon succinctly asserts that in humans “symbolic thought does not come innately
built in, but develops by internalizing the symbolic process that underlies language. ” Similarly,
Jaynes asserts that “consciousness becomes embedded in language. ”
2.2.2 Cognitive Architecture in Machines.Machine cognition can be understood as a functional ana-
logue of human cognition [41, 42, 149]. There have been a variety of machine cognitive architectures
proposed over the years [ 7, 60, 116, 118, 146, 168]. ICARUS utilizes hierarchical skills and con-
cepts [117, 118]. ACT-R uses Bayesian-style activation in an Adaptive Control of Thought—Rational
loop [7, 168]. EPIC leverages perception–action timing, making it well-suited for human-computer
interaction in embodied settings [146]. Soar is a recursive cognitive architecture that models intel-
ligent behavior through a symbolic State–Operator–Result (or S-O-R) cycle, in which reasoning
proceeds through the selection and application of operators to representations of the world [116].
Across all these cognitive loops, an agent/world model in discrete steps observes the environment,
encodes and stores state information, forms symbolic or semantic abstractions, reasons over possible
transitions, simulates alternative futures, and selects actions according to goals or preferences.
Cognitive Scientist Allen Newell laid the groundwork for the Soar Cognitive Architecture by
first asserting a unified list of cognitive components seen in both human and machine cognition.
We list Newell’s component part of the function of cognition in Table 2. Laird synthesized Newell’s
taxonomy to implement with Newell the Soar machine cognitive architecture [116]. S-O-R was
proposed as𝑅=𝑓 rules (𝑆𝑡, 𝑂𝑡 )where𝑅is𝑆 𝑡+1. In our world model notation, this is respectively,
𝑧𝑡+1 =𝑊 𝜃 (𝑧𝑡, 𝑎𝑡 )(1)
The Soar system is capable of being applied in worlds that require visual and symbolic representative
reasoning [22], implying compatibility with our state-of-the-art world models. Soar provides a
unified framework for perception, decision-making, and learning via production rules operating
over a shared working memory similar to the Global Workspace Theory proposed for human
cognition [11]. Soar’s use in world models was validated empirically in recent work [241].
Recently, Yann LeCun outlined a machine cognition framework for autonomous machines [121].
A key argument LeCun makes is that “common sense” within machines can emerge as a hierarchy
of low level models to high level models allowing the machine to “fill in the blanks” from incomplete
world observations. This is exactly how JEPA operates, and is reminiscent of the recursive S-O-R
loop from machine cognition framework Soar [116] and “levels of processing” theory of Fergus
Craik [40].
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 7

```text
Human Cognition in Machines: A Unified Perspective of World Models 7
Function [149] Human & Machine Cognition World Model Analogue
PerceptionSenses the current world. Encodes observations into a world state𝑧 𝑡 .
MemorySaves past experience and context. Stores past states 𝑧0:𝑡 of context, maps, or external memory.
LanguageUses symbols to communicate abstract meaning. Tokenizes language, goals, states, and reasoning.
Reasoning Problem solving and action selection with inference Infers𝑧 𝑡+1 or𝑎 𝑡 from other cognitive components.
ImaginationSimulates possible and/or hypothetical futures. Rolls out generated, simulated, or hypothetical𝑧 𝑡+1 or𝑎 𝑡 .
MotivationBehavior from extrinsic or intrinsic rewards. Criteria for selecting𝑧 𝑡+1 or𝑎 𝑡 .
Metacognition Operates over own representations, predictions,
and decisions.
Self-reflection, self-evaluation, and self-control of all other
cognitive components
Table 2. We select Newell’s [149] component parts of human and machine cognition to ground our framework.
Alternative architectures offer different component decompositions but Newell’s are unified across both
human and machine cognition with plausible world model analogues applicable to all our explored domains.
2.3 Our Taxonomy
We select Newell’s component parts of Human and Machine cognition to ground our framework. His
prominence in early [150] and contemporaneous machine cognition [116, 149] makes the decision
defensible, but we admit other sets of component parts found throughout machine cognition would
likely also be defensible [59, 83, 115]. We unpack the core cognitive capabilities discussed in Tab. 2
and use these component parts as a framework to taxonomize world model research. We survey
works since Ha et al. (2018) that are highly relevant, appearing in top conferences or surveys, or
are found in repositories hosted on GitHub [87]. Newell’s original list of the functional parts of
human and machine cognition wereperception,memory,language,reasoning,imagination,
andmotivation. Newell’s assertion thatreasoningextends to action selection [ 149], allows us
to consider direct policy networks like Vision-Language-Action models in Sec. 5 which rely on
implicit world models to transition world states through action selection alone.
Due to its paramount role in regulating cognitive functions, within our taxonomy’s component
parts list we includemetacognition, which refers to a world model’s capacity to reflect on, evalu-
ate, and control each component part of its cognitive processes.Metacognitionis the recursive
application of the other cognitive functions to themselves, such as, reasoning about one’s own
reasoning, monitoring one’s own perception, evaluating one’s own memory retrieval. In world
models, this may be implemented through uncertainty estimation, self-evaluation, error detection,
reflection, model selection, re-planning, or control mechanisms that decide when to revise repre-
sentations, seek additional information, simulate alternatives, or defer action [11, 112, 170]. We can
map these cognitive functions to the two traditional functions attributed to world models: world
representation, and world generation. The first two items in Tab. 2 correspond to typical world
model tasks in world representation, and the last two correspond to world prediction or generation.
The middle two are found across both representation and generation tasks. This taxonomy is
depicted in Figure 2.
In many previous world model works most of the components of cognition appear. For example
H-JEPA as an autonomous machine [121] is proposed with capabilities to encode observations
of the current world state (perception), to learn this encoding with a latent predictive objective
(motivation), and stores queryable world states for later use (memory). In follow-up works
JEPA uses text tokens as an input (language), and can be paired with an action policy network
(reasoning) [120, 196]. However, this set of capabilities is not distinguishable from most other works
when considering all applications of a work. Any taxonomy requires sorting decisions that are
contestable at the margin. A review organized by application must decide whether a given robotics
paper is ’manipulation, ’ ’locomotion, ’ or ’mapping’ when its method plausibly serves all three. In our
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 8

```text
8 Rupprecht et al.
.
.
..
.
• KV-cache (2017)
• V-JEPA (2023)
• TD-MPC2 (2023)
• Physical Intelligence (2025)
• TesserAct (2025)
• SparseWorld  (2026)
• OccWorld (2023)
• BEVWorld (2024) 
• JEPA (2024)
• LaDi-WM (2025)
• LiDARCrafter  (2025)
• PointWorld  (2026)
• Safedreamer  (2023) 
• Dream to drive (2025)
• Dream2Flow (2025)
• VideoWeave  (2025)
• PAN World Model (2025)
• DreamZero (2026)
• Plan2Explore (2020)
• R-AIF (2024)
• NewtonRewards  (2025)
• Irl-vla (2025) 
• Cambrian -S (2025)
• InDRiVE (2025)
• Cosmos-Predict (2025)
• RLVR-world (2025)
• Epona (2025)
• LingBot-VA (2025)
• GigaWorld -Policy (2026)
• Flash-WAM (2026)
   REASONING
 World state prediction
and / or world traversal
IMAGINING
             Hypothetical reasoning
MEMORY
         Representations of 
past world states
PERCEPTION
  Representations  of the 
current world state from 
observation
• DrivingGPT  (2024)
• WorldGPT  (2024)
• Doe-1 (2024)
• SciSciGPT (2025)
• AI Co-scientist (2025)
• LingBot-VLA (2026)
LANGUAGE
                  Tokenization of language, 
goals, states, and reasoning
MOTIVATION
               Selection criteria for world      
state prediction or traversal
World Generation
Reason according to physical laws
.
. .
World Representation
Sense and learn real-world knowledge
Fig. 2. The taxonomy of world models under cognitive architecture [149].
case, rather than sorting works based on a cognitive function’s presence alone, our sorting criterion
is explicit and applies uniformly: we judge a work as innovative on a cognitive function when the
work’s stated contribution operates on that function; works claiming contributions on several are
placed under several. Then we sort our review by these innovations in world model cognition. This
makes our assignments inspectable and, where a reader disagrees, precisely locatable.
Using I-JEPA as an example [10], the authors state three research contributions: 1) I-JEPA learns
strong representations from input observations by predicting embeddings, not pixels, (we label a
perceptionandmotivationinnovation) 2) by using a simpler model with less rigid inductive bias,
I-JEPA is applicable to a wider set of tasks (we label a non-cognitive, evaluative consideration) and
3) JEPA is scalable and efficient (we label a non-cognitive, practical consideration). Subsequently, we
would taxonomize the I-JEPA work as innovating uponperceptionandmotivation. We also present
papers we deem exemplary of the cognitive innovations we survey in Figure 2. Our comprehensive
categorization of world model research can be found across Tables 3, 4 and 5.
Throughout our review, it is important to note that machine cognition functionally emulates,
and does not mechanistically emulate, these component parts of human cognition. For example,
when we say a world model has “memory, ” we mean it maintains state representations across time
steps, not that it has anything resembling episodic recall or the biological substrates of human
memory. Machine cognition emulates human cognition inmemory,perception, and some symbolic
reasoningtasks throughlanguage, andimaginationwith sim-to-real design paradigms. It is
ambiguous if machine cognition fully emulates true human-likereasoningand machine cognition
almost universally fails to emulate intrinsicmotivation. Machine intelligence has demonstrated
little capability in emulatingmetacognition.
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 9

```text
Human Cognition in Machines: A Unified Perspective of World Models 9
Unified Cognition Framework for World Models
World Representation:
Sense and learn real-world knowledge
World Generation:
Predict and generate world states
World Transition Action Selection
Meta-cognition: 
Self-reflection, self-evaluation, self-control of the
other cognitive components in a global workspace
Reasoning
World state prediction  
and / or world traversal 
Language
Tokenization of inputs,
goals, states, and
reasoning
Imagining
Hypothetical reasoning
Motivation
Selection criteria for world
state prediction or
traversal
Perception
Representations of world
state from observation
Memory
Representations of  
past world states 
"Previously it rained when cloudy"
"Sky is cloudy"
"It will rain" 
"If I take umbrella, I stay dry"
"I want to be dry"
"I take umbrella"
Fig. 3. Our Unified World Model derived from human-machine cognition [11, 149]. This serves as a conceptual
road-map for world model research. We also want to highlight that the component oflanguagemimics
metacognitionin that it can be used to operate over each other component of cognition.
3 Unified Cognition Framework for World Models
We report on world models in the context of video world models (discussed further in Sec. 4),
embodied world models (discussed further in Sec. 5), and what we define as epistemic world models,
or world models used by agents for scientific discovery (discussed further in Sec. 3.3 and 6). We
sub-categorize each section according to the component parts of machine and human cognition
listed in Sec. 2.2. We review exemplars for contemporary works that innovate on specific functions
of cognition as shown in Figure 2. We continue to taxonomize works across a more comprehensive
body of research available for all to see in Tables 3, 4, and 5. A trend emerges across all three tables
revealing a research gap regarding innovations targetingmetacognition. Furthermore, upon closer
inspection, innovations belonging to themotivationcolumn near always implement a form of
extrinsicmotivation, external to the world model itself. This differs fromintrinsicmotivation as
it is reliant on hand-crafted rewards, or actor-critic models trained with reinforcement learning.
As we stated in the introduction, if researchers want to claim that a world model hashuman-like
cognition, then we would expect to find all the components from Sec. 2.2 of cognition unified
within that world model framework.
We propose our conceptual unified world model framework that serves as a conceptual road
map for this report and future world model research through the research gaps we identify. World
models sense and learn from real-world knowledge, predict and generate world states, reason and
control according to physical laws implicitly, and can do all of this with or without a machine agent
or a human-in-the-loop. To accomplish this we propose a unified world model that holistically
incorporates every component part of the CAT concepts discussed in Sec. 2.2 into one conceptual
unified framework as seen in Figure 3.
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 10

```text
10 Rupprecht et al.
As a design paradigm, our conceptual unified framework for world models calls for standardizing
best practices in both world model representation, and world model generation. To fully span the
functions of cognition emulated, Unified World Models encourage researchers to:
(1) Encodeperceptionof world representations from sensory observations with multi-modal
state spaces (discussed further in Sec. 3.1.1),
(2) Leveragememoryfor robust world models with state-spaces that encode multiple temporal
scales, or store previous queryable states for efficient access (discussed further in Sec. 3.1.2),
(3) Includelanguagetokens as an input, intermediate reasoning space, or output to facilitate
human-in-the-loop cooperation (discussed further in Sec. 3.1.3),
(4) Enableimaginationas hypothetical reasoning during inference and sim-to-real transfer
learning during training when data is scarce (discussed further in Sec. 3.2.2),
(5) Performreasoningwith domain-specific models in Figs 4 to 9 (discussed further in Sec. 3.2.1),
(6) Provide reward signals to world models formotivationusing state-based rewards that make
salient robust measurements like active inference (discussed further in Sec. 3.3),
(7) Utilizemetacognitionthrough global workspaces enabling self-reflection, self-evaluation,
and self-control (discussed further in Sec. 3.3).
None of these suggestions conflict with each other, but some are setting specific or conditional. In
Sec. 3.3, we will argue that our proposed research directions regardingmotivationandmetacog-
nitionfill a real research gap our taxonomy has revealed.
Reviewing video world models in Sec. 4 shows us the importance of creating world representations
that enforce spatial consistency and meet memory constraints, using solutions like KV-cache,
while still enforcing longer temporal consistency. We show state-of-the-art video world model
architectures in Figures 4 to 6. When we review embodied world models in Sec. 5 we see the
importance of leveraging multi-modal inputs to make precise locomotion possible. We also see
in Sec. 5 that when training data is scarce, sim-to-real training can overcome this scarcity when
world models learn latent representations that are traversable and remain consistent under domain
shift to real-world applications (discussed more in Sec. 3.1). We show state-of-the-art embodied
world model architectures in Figure 7 and 8. We propose in Sec. 3.3 a new category of world models
calledepistemic world modelsthat we review in Sec. 6. This domain includes agent frameworks
for human-in-the-loop scientific discovery which serve as inspiration for overcoming one of the
research gaps that we have observed in the latent world model’smetacognitioncapability. We
show state-of-the-art epistemic world model architectures in Figure 9.
Latent world models learn state transition dynamics in video and embodied settings while
agent frameworks are not typically framed that way. However, epistemic world models in an agent
framework with a Global Workspace representation of the world (defined in Sec. 2.2) perfectly aligns
with Soar’s State Operation Result loop [116], and we argue, even the latent world model definition
as LLMs and VLMs are already considered to be world models [ 66, 72]. A Global Workspace is
not a learned latent encoding like JEPA [10]. Instead, a Global Workspace is alanguagebased
collection of all past prompts and responses including tool-call outputs. In the epistemic world
model setting, the initial world is static and represents structured knowledge from prompts, and
context supplied by the user. However, as the agent interacts with this world—through multimodal
Retrieval-Augmented Generation (RAG) queries, analyzing existing literature, and encoding inputs
and outputs of tool-calls into a global workspace (e.g., a chat history)—it creates a changing
environment. This transformation leads to a dynamic state space that aligns with the traditional
definition of a world model. Working within this agentic framework with a global workspace
implementation allows models like Gemini Co-scientist [69, 70], an LLM and world model itself, to
propose novel trajectories through an evolving state space to perform actual scientific discovery.
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 11

```text
Human Cognition in Machines: A Unified Perspective of World Models 11
3.1 World Representation
World representation refers to how spatio-temporal world knowledge is sensed and encoded ideally
enabling downstream world model tasks such as world prediction over time and action selection
within the world. World models use spatio-temporal world representations aligning with physical
laws (discussed in both Sec. 4.2 and 5.2), and can use language representations to enable self-
reflection, self-evaluation, and self-control (discussed further in Sec. 6.2). In our unified framework,
the functional components of world models for representation correspond to the cognitive functions
ofmemory,perception, andlanguage. Together they encode spatio-temporal representations of
the world.
3.1.1Multi-modal Perception.The state-of-the-art perception innovations in world model
research are multi-modal [90, 130, 197, 257, 263, 264]. This synchronizes with human-like perception
which is multi-modal due to our innate need to integrate information across at least five senses
used to represent the world [24]. Additional exemplary works are shown in Figure 2, with more
examples discussed in Sec. 4 to 6.
Perception is often where world model framework’s begin. We will start by considering an input
of multi-modal observations 𝑜𝑖
𝑡 for images, 𝑜ℓ
𝑡 forlanguage, 𝑜𝑎
𝑡 for audio, and so on. We define
𝜙𝜃 (·) as our multi-modal world model for representation, used to create 𝑧𝑡, our world’s latent
representation at step𝑡, or in other words,
𝑧𝑡 =𝜙 𝜃 (𝑜𝑖
𝑡, 𝑜 ℓ
𝑡 , 𝑜 𝑎
𝑡 , . . .)s.t.dim(𝑧 𝑡 ) ≤𝐵, 𝐼(𝑜 𝑡 ;𝑧 𝑡 ) ≤𝐶(2)
After input encoding, we have latent variable 𝑧𝑡 subject to the constraints for physically fitting 𝑧𝑡
within amemorybudget 𝐵, while also keeping mutual information below 𝐶, or a sufficient mutual
information between the observations and latent space at step 𝑡. At this stage, alignment with
physical laws is implicitly instilled through training data and handcrafted reward signals (the latter
is discussed more later on). To achieve sufficient world representation for downstream tasks, such
as action selection for state transition performed by operator T, we must select an ideal encoder
𝜙 ∗
𝜃 ()from among state-of-the-art world encodersF, or in other words,
𝜙 ∗
𝜃 =arg min
𝜙𝜃 ∈ F
𝐼 (𝑜𝑡 ;𝜙 𝜃 (𝑜𝑡 )) s.t.E [𝑅(T(𝜙 𝜃 (𝑜𝑡 ))) ] ≥𝜌(3)
The above selects an ideal encoder to compress the current observation while preserving enough
information for a downstream tasks that produce a sufficient reward for training and inference.
T may be a generative world model 𝑊𝜃 from Eq. (1), a direct policy network, or an MPC planner
model. This sufficiency value 𝜌 is task dependent, and selected by the researcher conditioned on
expected results from competing state-of-the-art representation strategies found inF.
Encoders for world representation often are both multi-modal and multi-scalar (spatially, or
as discussed in the next section, temporally). Both features complement each other in practice,
and innovativeperceptionworks rarely breakdown into one or the other [ 90, 130, 197, 257, 263,
264]. TesserAct and PointWorld utilize RGB, Depth, and Normal readings to create a point-cloud
representation of the world [ 90, 263]. StereoWorld, much likehuman-like perception, utilizes
disparity and epipolar constraints on two camera feeds to add a depth scale to 2D appearance [197].
Some embodied world models integrate encoded LiDAR measurements, 𝑜LiDAR
𝑡 , into the perceptual
pipeline and demonstrate that fusing complementary spatial modalities improves robustness and
downstream planning performance, particularly in navigation and autonomous systems [130, 264].
Similarly, BEVworld fuses camera and LiDAR readings to create a Birds Eye View occupancy grid
for world representation [257]. Across these works multi-modalperceptionserves as a mechanism
for reducing ambiguity in 𝑧𝑡 by grounding latent representations in multiple correlated spatial
observation streams.
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 12

```text
12 Rupprecht et al.
3.1.2Multi-scalar Memory.World representation models, world generation models, and unified
frameworks performing both representation and generation are meant to learn the state transition
dynamics of a world; this meanstemporalas well asspatialcharacteristics. This reveals a vulnera-
bility in Eq. (3) we left unaddressed and will correct now. Our ideal encoder from a single time step
𝜙 ∗
𝜃 (𝑜𝑡 )) captures no state transition dynamics to embed spatio-temporal features in our state space
𝑧𝑡. Furthermore, looking to our constraint, maximizing an expected scalar or low-dimensional
reward from a single observed state is likely to lead to reward collapse [46] and propagate a credit
assignment problem in long horizon tasks with delayed rewards [171]. We have two options for
addressing this, we can create a richer reward signal by enablingimaginationas hypothetical
reasoning over a future time horizon H (discussed more in Sec. 3.2.2, or as we show now, we can
add short-term memory to our observations as 𝑜 ≤𝑡 . The later adds state transition dynamics to 𝑧𝑡
as a restating of Eq. 2 such that,
𝑧𝑡 =𝜙 𝜃 (o𝑣
≤𝑡 ,o ℓ
≤𝑡 ,o 𝑎
≤𝑡 , . . .)s.t.dim(𝑧 𝑡 ) ≤𝐵, 𝐼(o 1:𝑡;𝑧 𝑡 ) ≤𝐶(4)
This updates our selection criteria for an ideal encoder for world representation re-expressed
through Eq. (3) as,
𝜙 ∗
𝜃 =arg min
𝜙𝜃 ∈ F
𝐼 (o≤𝑡 ;𝜙 𝜃 (o ≤𝑡 )) s.t.E [𝑅(T(𝜙 𝜃 (o ≤𝑡 ))) ] ≥𝜌(5)
In practical terms this is the difference between a researcher using V-JEPA [14] over I-JEPA [10]
when the world is represented through video frames as a sliding window of short-termmemory.
Short-termmemorywithin world model perception makes that perception morehuman-like.
Human perception at the mechanistic level in the human brain utilizes dual streams for spatial and
temporal representations of the world [246]. The field of computer vision already emulates this
human spatio-temporal perception by proposing dual stream architectures with one for spatial
representations and a second for temporal representations implying short-term memory [58, 192].
World models use this approach now [90, 130, 263, 264]. We see this spatio-temporal perception
in use by OccWorld and LiDAR crafter which use LiDAR to create an evolving map used by
downstream reasoning tasks [130, 264], and in TesserAct utilizing optical flow as one of its multiple
input modalities [263], as is the case in PointWorld which uses 3D point flows to perceive temporal
changes in the world [90].
Long-term memory is also used by many of these works to create queryable maps of past world
encodings saving compute at inference [ 44, 240]. Mosaicmem, a video diffusion world model,
encodes 2d observations as 3d observations leveraging latent memories of previous time-steps’ 2d
observations to create patch-level and scene level encodings [240]. SparseWorld’s perception is
similarly improved due to the presence of queryable memory [44].
Using memory to instill spatio-temporal characteristics also allows downstream tasks such as
sim-to-real “dreaming” during training and hypothetical reasoning during inference, which will be
discussed in Sec. 3.2. This perspective aligns with prior work on traversable latent spaces [25, 28, 73,
80, 211], and suggests that long-context memory in world models is inherently tied to the capacity
for spatio-temporal structured latent prediction. For instance, augmenting Dreamer-style [78] agents
with traversable spatial latent representations enables improved sim-to-real transfer, highlighting
the importance of jointly encoding spatial structure alongside temporal dynamics [28]. Similarly,
temporal hierarchy learning introduces multiple scales of abstraction inperception, allowing agents
to reason over both short-term transitions and long-horizon dependencies [73] again paralleling
human-cognition with multiple layers and abstract thinking [40, 121]. Hierarchical world models
extendhuman-like multi-layered thinking to control: Hansen et al. [ 80] couple a high-level world
model that reasons over abstract targets with a low-level model that produces motor commands.
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 13

```text
Human Cognition in Machines: A Unified Perspective of World Models 13
Finally, world model memory can also be learned through architectural enhancements to world
model frameworks. Autoregressive transformers as with Large Language Models (LLMs) and Vision
Language Models (VLMs) use memory in their reasoning towards output tokens corresponding
to state or action tokens when adapted as Vision Language Action (VLAs) models [96, 199, 224].
Autoregressive diffusion models from Video World Models behave the same way, where every
token in the output sequence is conditioned on the previous tokens in the output prompt, and
tokens from the input prompt [92, 141, 269]. Additionally, works have used architectural modules
to simulatememory, as is the case with Transformer State-Space Models (TSSMs) for bi-directional
diffusion models to learn long-range memory dependencies and predict future observations more
accurately, and more efficiently than their autoregressive alternatives [28]. We discuss more in
Sec. 4.3 the usage of memory in architectural reasoning and the usage of memory implementations
advances like KV-cache that lead to efficient and state-of-the-art world models [152, 207].
Adding memory to world models does not just make world models morehuman-like, it is what
makes their practical use possible. The encoding and learning of spatio-temporal features enhances
the cognitive function of all of the other component parts of cognition as we saw withperception
andlanguagebut alsomotivation,imaginationand other downstreamreasoningtasks such as
state transition prediction, or action selection. Additional examples ofmemoryinnovations are
summarized in Fig. 2 and discussed in Sec. 4–6. Unified world models seek an encoder 𝜙𝜃 (·) that
produces representations supporting sufficiently long temporal context, as required by Eq. (4) and
Eq. (5).
3.1.3Language.In world model settings, language can be used to represent the world, but also
be used in generative models for conditioned world prediction or action selection. Large Language
Models (LLMs) [185, 187, 188, 250, 260, 261] and Vision-Language Models (VLMs) [181, 183, 186,
231, 258], are innately world models themselves [66, 72]. How robust orhuman-like LLMs or VLMs
perform alone as world models requires more research. Empirically, LLMs show insensitivity to
meaning in comprehension tasks when compared to human counterparts [48]. LLMs still fail to
reason as humans do in the tasks we ask humans to perform [ 95, 158]. However, we know that
latent spaces learned by language models converge to similar embeddings across differing modal
inputs [94] and visual embeddings as well as activation patterns are aligned with the human
brain [52, 174]. Generally, when researchers align an LLM’slanguagecognitive function to humans’
languagecognitive function the LLM accuracy improves [122]. Leviathan et al. does so by repeating
LLM prompts to emulate a human’s innate ability to hold both the beginning and end of a spoken
sentence in their mind at once something an autoregressive LLM is innately unable to do.
Metacognition via Language.As discussed in Sec. 2.2languageplays a paramount role in human
cognition [205], with some arguing it is language that is directly responsible for human metacogni-
tion [47, 100]. Empirically one can see from our Figure 3 that language allows a machine to operate
over all the other components of cognition. This is a key element of metacognition, but it remains
to be seen if language is the ideal operator of all other components of cognition in machines. Still
when we explore epistemic world models, we repeatedly find language at the center of existing
global workspaces used in agent frameworks. We discuss this more in the Section 3.3.2.
3.1.4A Unified World Model Approach to Representation.Foundational representative
world models include Cosmos-Predict [2, 4], LingBot-WM [203], GIGA-World [200], RLVR-World [220],
and finally JEPA [10], which all learn to represent knowledge of the world implicitly aligning with
physical laws through training data. Joint-Embedding Predictive Architectures (JEPA) provides a
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 14

```text
14 Rupprecht et al.
canonical instantiation of the representation component within our unified world model frame-
work [9, 10, 49, 196, 208, 214]. Rather than reconstructing raw sensory inputs, JEPA learns repre-
sentations by predicting target embeddings from context embeddings in a shared latent space [10],
thereby directly optimizing for a more robust predictive structure. This predictive latent-space for-
mulation naturally supports multiple cognitive functions. JEPA encoders can integrateperception
across multiple modalities [39] in embodied settings [214], incorporatelanguageas inputs [ 208],
or to serve as intermediate representations for downstreamreasoning[ 196]. Crucially, when
combined with latent dynamics models, these spatio-temporal representations enable long-horizon
memorythrough compact latent world-encodings, and as we will see in the next section, enable
hypothetical action rollouts [ 9, 49]. In this sense, state-of-the-art world representation models
like JEPA act as 𝜙 ∗
𝜃 creating spatio-temporal features 𝑧𝑡 as is the case in our Eq. (4). These JEPA
encodings are not merely compressive, but structured to support prediction over imagined futures,
aligning directly with the requirements imposed by our reward-constrained information bottleneck
formulation in Eq. (5). We will see how world models in Sec. 4 to 6 sense and learn world knowledge
in each domain application.
3.2 World Model Prediction and Generation
While world representation defines how spatio-temporal world knowledge is sensed and encoded,
world model prediction and generation refers to how the world models make predictions over time
and select action traversals within the world. World models generate 3D scenes (discussed further
in Sec. 4.2), generate controlled real-world scenes (discussed further in both Sec. 4.2 and 5.2), select
actions for state traversal (discussed in Sec. 5.2) and can reason over Global Workspaces encoded
by language (discussed further in Sec. 6.2). In our unified framework, the functional components of
world models for generation correspond to the cognitive functions ofreasoning,imagination,
languageandmotivation. Together they enable structured planning, hypothetical simulation,
and decision-making over future trajectories.
3.2.1Reasoning.Within our taxonomy world model reasoning is defined both as the structured
prediction of future world states and as the selection of action rollouts. The transition model 𝑊𝜃
governs the evolution of latent states and when appropriate is conditioned on an action as was the
case in Eq. (1). From here, the reward function 𝑅(𝑧) evaluates the desirability of future latent states
and trajectories. We treat𝑊𝜃 (𝑧𝑡, 𝑎𝑡 ) as a parameterized world transition function, though it may in
practice represent a stochastic process.
In a search for the optimal action 𝑎∗
𝑡 at time step 𝑡, the reward signal is considered over the time
horizon𝐻,
𝑎∗
𝑡:𝑡+𝐻 =arg max
𝑎𝑡:𝑡+𝐻
E
" 𝐻∑︁
𝑘=0
𝑅(𝑧 𝑡+𝑘 )
#
(6)
Thus, action selection can be understood as inference over spatio-temporal latent trajectories,
where candidate futures are simulated and evaluated under the reward functional. The predicted
𝑧𝑡+1 is obtained by 𝑊𝜃 , our unified World Model for world model generation guided by principles
from Cognitive Architecture Theory.
We identify eight recurring design paradigms for how world model reasoning occurs, shown in
across Figures 4 to 9, that span the spectrum from purely discriminative action selection to full
generative world simulation. At one extreme lie Vision-Language-Action models (VLAs), such as
𝜋0.5 [96], LingBot-VLA [224], and other VLA methods that map observations directly to actions
through a VLM backbone augmented with a flow-matching action expert [86], bypassing explicit
future-state prediction entirely [49, 101, 134, 138, 196, 271]. At the other extreme, some world models
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 15

```text
Human Cognition in Machines: A Unified Perspective of World Models 15
only represent the world [208], and use a separate value [49] or policy models for action or future
state generation [2, 124]. These World Action Models leverage training data and are not conditioned
on any action. This decoupling of representation and action generation grants maximum flexibility
in imagination but introduces a two-system overhead, in which errors in world prediction and
errors in action selection compound independently. World Action Models [124, 236, 237] tend to be
more robust and work better with longer and noisier time horizons. Additional methods include
autoregressive transformer [37, 137, 248, 250, 272] and diffusion models [92, 93, 184, 239, 249, 254,
270]. Motus claims to be a unified world model because it successfully unites generating latent
action, future video states, and agent actions [18].
3.2.2Imagination.During world model training,imaginationmanifests as dreaming [ 75],
referring to a world model’s capability to learn to represent world dynamics through unsupervised
training. If these learned spatio-temporal latent representations are traversable and remain con-
sistent under domain shift, then an action-policy model can be trained with these latent spaces
and deployed in a real-world domain [57, 75, 144]. In real-world applications, training data can be
prohibitively scarce and expensive to create; sim-to-real training overcomes this problem [171].
Figures 6 through 8 show architectures that support hypothetical reasoning in inference, and
dreaming in training both in the video world model and embodied world model domains.
During inference,imaginationrefers to hypothetical reasoning, planning, or simulating future
states of the world over a set of possible action rollouts to find an optimal action [226, 230]. This is
only possible after applying lessons from Sec. 3.1, where Eq.(5) creates a traversable world-encoding
latent space. The optimal action, or 𝑎∗
𝑡 , maximizes the expected reward signal over the time horizon
of the possible action rollout. For action-planning we assume a decomposition of the world model
into a transition function and an observable reward functional. When our unified framework for
representation successfully encodes spatio-temporal representations upstream in Eq. (5) we are
ensured that imagined trajectories that remain consistent over extended horizons [57, 63, 73, 221,
226].
3.3 Cognitive Architecture in Unified World Models
Our taxonomy categorizes the surveyed works according to the cognitive functions. Many works
incorporate several cognitive functions in their designs and sometimes innovate along multiple
cognitive axes, which is why some works appear in multiple sections or have several check marks
in Tables 3, 4, and 5. Analyzing the innovation trends presented in our report through Tables 3, 4
and 5 show that a research gap exists regarding the cognitive functions ofmotivation, and
metacognition. The utilization of our taxonomy makes this research gap clear and may not
have become apparent otherwise. It is clear that machine and human cognition continue to be
intertwined.
An exciting new theory of human cognition, Active Inference [59, 61], explains human cognition
as a system that minimizes surprise about sensory inputs by continuously updating beliefs about
the world and taking actions that make the world match those beliefs. Active Inference has been
extended to machine cognition [60, 162] as a theory that novellymotivateslearning in machines
and informs our unified world model Framework (discussed further in Sec. 3.3). world model works
have already begun to incorporate Active Inference [144].
Across our report on state-of-the-art world models, we have identified two significant research
gaps regarding two components of our unified world models:motivationandmetacognition. This
issue is, in part, elucidated by evaluative benchmarks from recent studies [33, 109, 156, 165, 193, 216].
Furthermore, Tables 3, 4, and 5 clearly demonstrate the lack of innovation in the areas ofmotivation
andmetacognition. To address these gaps inmetacognition, we observe the importance of
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 16

```text
16 Rupprecht et al.
language in human cognition may be an indication of its importance in machine cognition, and
suggest that researchers focus on the agent frameworks, as illustrated in Figure 9 as what we
call epistemic world models. In terms ofmotivation, advancements in human-machine cognitive
architecture theory, particularly regarding Active Inference [59–61, 144, 162], should be explored.
3.3.1Motivation.Reinforcement Learning (RL) techniques instill external motivation into world
models through reward signals, using a reward function defined external to the world model itself.
Enablingimaginationor hypothetical reasoning, as described by Eq. (6), requires an observable
reward functional 𝑅(𝑧 𝑡 ) [79, 81, 107, 144, 147, 220]. Multi-task learning allows the pursuit of multi-
ple goals [144] and can help align models to the physical world when trained with an appropriate
reward signal [119]. Researchers construct RL agents as a potential solution to artificial general
intelligence, assuming that their reward signal is sufficient [ 191]. However, often RL provides
training mechanisms for world models using hand-crafted reward signals that do not general-
ize [171] and rewards that are misaligned with the intended operational goal [6, 77]. As such, they
require additional interventions such as Reinforcement Learning from Human Feedback in some
applications [135, 165].
Intrinsic Motivation.Promising research directions exist, such as maximizing influence over future
states [111] or minimizing energy (i.e. surprise) [60, 61, 162] to explore with training mechanisms
decoupled from an externally defined and action-based reward signal. Both maximizing the influence
of future states and active inference are compatible with the state-based reward function described
in Eq. (6). Active Inference formalizes “minimizing surprise” as the minimization of variational
free energy, a tractable upper bound on negative log model evidence, which decomposes into
accuracy and complexity and extends to action selection through expected free energy that balances
information gain and value. Concretely, given a latent world model with states 𝑧𝑡, observations 𝑜𝑡,
and actions𝑎 𝑡, the generative model is defined as
𝑝𝜃 (𝑜1:𝑇, 𝑧1:𝑇 |𝑎 1:𝑇 )=
𝑇Ö
𝑡=1
𝑝𝜃 (𝑜𝑡 |𝑧 𝑡 )𝑝 𝜃 (𝑧𝑡 |𝑧 𝑡−1 , 𝑎𝑡−1 ).(7)
Inference proceeds by introducing an approximate posterior 𝑞𝜙 (𝑧1:𝑇 |𝑜 1:𝑇 ) and minimizing the
variational free energy
F=E 𝑞𝜙 (𝑧1:𝑇 )

log𝑞 𝜙 (𝑧1:𝑇 ) −log𝑝 𝜃 (𝑜1:𝑇, 𝑧1:𝑇 )

,(8)
which upper bounds the surprise−log𝑝 𝜃 (𝑜1:𝑇 ). This objective decomposes as
F=𝐷 KL
 𝑞𝜙 (𝑧1:𝑇 ) ∥𝑝 𝜃 (𝑧1:𝑇 ) −E 𝑞𝜙 [log𝑝 𝜃 (𝑜1:𝑇 |𝑧 1:𝑇 )] ,(9)
corresponding to complexity and accuracy terms, respectively. For action selection, policies 𝜋 are
evaluated by minimizing the expected free energy
G (𝜋)=E 𝑞𝜙

𝐷KL
 𝑞𝜙 (𝑧𝑡+1:𝑇 |𝜋) ∥𝑝 𝜃 (𝑧𝑡+1:𝑇 )
|                                    {z                                    }
information gain
−log𝑝(𝑜 𝑡+1:𝑇 )
|         {z         }
value

,(10)
encouraging trajectories that both reduce uncertainty in latent dynamics and achieve preferred
outcomes. As such, world model research has already begun to incorporate Active Inference.
Using intrinsic motivation for world models is drastically unrealized, but there are some recent
works using intrinsic motivation within RL that validate this research direction [ 8, 16, 56, 105,
107, 159, 160, 169, 175, 182, 194, 234, 238]. Among these works, Active Inference is also being
deployed in embodied settings to promote exploration during training [8, 169], and in one case,
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 17

```text
Human Cognition in Machines: A Unified Perspective of World Models 17
even control swarms of unmanned autonomous vehicles [ 8]. Seven of these are explicit world
model works [56, 107, 169, 175, 194, 234, 238]. Three explicitly use Active Inference as a reward
signal for world models [56, 234, 238]. Cambrian-S explicitly references prediction error as a proxy
for measuring surprise but falls short of implementing Active Inference’s full exploratory learning
objective [234].
It is also worth noting that researchers are ultimately the ones selecting architectures, reward
criteria, and training sets within world model research. Peer review evaluates objectively if the
subsequent empirical results are novel and notable. It is researchers who breathe life into world
models by aligning experiment designs with broader research trends. It is here researchers lend
their human cognition in machine cognition with a single example being the selection of 𝐵, 𝐶,
and 𝜌 as thresholds found in the constraints described in Eq. (2) to (5) of our unified world model
framework. This is further demonstrated in the global workspaces of epistemic world models
used by agent frameworks for AI-Human Collaboration [69, 70, 179, 180] shown in Figure 9 and
discussed in Sec. 6.
3.3.2Metacognition.Soar’s usage of sub-tasks and recursive operator decomposition mimics
human metacognition by breaking bigger, more abstract tasks into smaller, more discrete tasks [40,
116]. For example, if an agent with a world model is navigating a problem and not experiencing
progress towards a goal, sub-tasks allow the debugging of this lack of progress by operating over
memory, perception, and other components of cognition to propose alternative routes to the goal;
demonstrating a minimal degree of self-reflection, self-evaluation and self-control. While world
models’ capability to align withhuman-like metacognition is theoretically possible, it still represents
a largely unsolved implementation problem [102, 158, 164].
Metacognition via Global Workspaces.Exploring metacognition through the use of agent systems
capable of self-reflection, self-evaluation, and self-control shows some progress towards the goal of
implementing truly metacognitive capabilities within world models [19, 213]. Figure 9 shows how
these agent frameworks provide a world model that enables some amount of metacognition through
the use of a Global Workspace [11] accessible by agents and human collaborators. Altogether, the
central limitation identified in world models is the absence of explicit metacognitive mechanisms
in latent world models, particularly in embodied and video domains seen in Sec. 4 and 5. While
these systems learn latent state representations 𝑧𝑡 and transition dynamics 𝑧𝑡+1 =𝑊 𝜃 (𝑧𝑡, 𝑎𝑡 ), they
lack a mechanism for monitoring, evaluating, or controlling the routing internal computations.
For latent world models in settings that cannot fully replicate a truly Global Workspace due to
context size constraints, we see research begin to approximate it using a mixture-of-experts (MoE)
paradigm with a world-aware router function. A router function selecting an expert exhibits some
behavior indicative of metacognition as self-control. The MoE implementation functions similarly
to specialists within multi-agent frameworks and is a growing trend in world models [98, 198, 223].
A world-aware router could be extended to select the amount of loops to be perform in a looped
transformer LLM [233] indicating self-control over an amount of reasoning performed (i.e. reasoning
about reasoning). Similarly, to improve self-reflection, increasing input modalities (i.e., increasing
the amount of specialists) to augmentperceptionfrom “first person” video alone to include an
additional “third person” video source. For a fully self-evaluating metacognitive process, using
imagination over an MoE implementation, or integrating a router function that can decide to
re-reason through a problem, would function similarly to an evaluation specialist operating in a
Global Workspace, as discussed in Sec. 6.
Drawing from Cognitive Architecture Theory [149] and the Global Workspace Theory (GWT) [11],
metacognition can be interpreted as the ability to self-reflect, self-evaluate, and self-control. Notably,
while such mechanisms are largely missing from latent world models, they emerge naturally in
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 18

```text
18 Rupprecht et al.
epistemic world models, where shared workspaces are instantiated through external artifacts such
as documents, tool outputs, and execution traces. These systems approximate the self-reflection,
self-evaluation, and self-control, albeit over distributed and externalized state representations, often
as interpretable language, rather than internal latent variables. As we will discuss in Sec. 6, recent
agentic systems for scientific discovery provide early instantiations of such global workspaces,
suggesting a viable pathway toward incorporating metacognitive capabilities into unified world
models using interpretable language. The typical architecture for such an agentic system is shown
in Figure 9.
4 Video World Models
Video world models aim to learn compact representations of visual environments together with
their temporal evolution. A common abstraction is a latent dynamical system:
𝑧𝑡+1 =𝑓 𝜃 (𝑧𝑡, 𝑎𝑡 ), 𝑥 𝑡 =𝑔 𝜙 (𝑧𝑡 ),(11)
where 𝑧𝑡 ∈R 𝑑 denotes a latent state encoding scene geometry, object configurations, physical
factors, and temporal context; 𝑎𝑡 denotes external inputs, actions or control signals; 𝑓𝜃 models state
transitions; and 𝑔𝜙 maps latent states back to observations. Under this view, video is generated
through state evolution and rendering, rather than direct frame-wise synthesis.
Recent advances have positioned video world models as powerful engines for simulating the visual
world in 2D space [15, 57, 65, 73, 99, 119, 197, 225, 234, 242, 243, 256, 259], 3D space [123, 202, 240],
and hybrid geometric settings [12, 28, 50, 63]. As summarized in Table 3, these models differ not
only in their geometric assumptions, but also in the cognitive functions they operationalize, namely
perception, memory, reasoning, imagination, motivation, and metacognition.
The defining characteristic of modern video world models is their ability to predict future
visual states conditioned on current observations and, more crucially, on latent or explicit actions.
Contemporary systems such as the open-source Wan [209], alongside models such as Sora [154]
and Kling [201], do not merely synthesize pixels; with proper latent representations and training
techniques, they can learn the underlying physical, causal, and temporal laws governing their
simulated environments. Overall, a world model must go beyond visually plausible synthesis; it
should support persistent state representation, causal transition modeling, controllable intervention,
and physically grounded prediction. This distinction marks the transition from passive text-to-video
generation toward interactive, controllable, and agent-facing environments.
In Sec. 4.1, we review how video world models construct internal representations of the world,
focusing on perception and memory. In Sec. 4.2, we discuss how these representations are used for
prediction and generation, emphasizing reasoning, imagination, and motivation. Sec. 4.3 summarizes
key trends and limitations of epistemic world models. Figures 4 5 and 6 illustrate representative
architectures encountered across 2D, 3D, and hybrid video world models.
Table 3. Comparison of recent video world models according to geometry and cognitive functions. A check
(✓) indicates that the work explicitly contributes to the corresponding cognitive function in the context of
video world models.
Work Year Geometry
Mem.
Perc.
Lang.
Reas.
Imag.
Moti.
Meta.Description
Representation: memory and/or perception
V-JEPA [15] 2024 2D✓ ✓ ✓ Self-supervised video learning by predict-
ing masked spatio-temporal regions in latent
space.
continued on next page
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 19

```text
Human Cognition in Machines: A Unified Perspective of World Models 19
Table 3 –continued from previous page
Work Year Geometry
Mem.
Perc.
Lang.
Reas.
Imag.
Moti.
Meta.Description
Gumbsch et al. [73] 2024 2D+temporal✓ ✓ ✓ ✓Learn when the world meaningfully changes
via discrete latent dynamics, then build a high-
level model that skips between change points.
VideoREPA [256] 2025 2D✓ ✓ Physics-aware video generation via relational
distillation.
Cosmos-Predict2.5 [4] 2025 2D✓ ✓ ✓ Unified flow-matching video generator
trained on clips for Physical AI simulation,
data augmentation, and policy evaluation.
VideoWeave [57] 2026 2D✓ Splice short captioned videos into synthetic
long videos to cheaply train better video-
language models.
Helios [243] 2026 2D✓ ✓ ✓ 14B model running real-time on one H100 via
context compression and drift-aware training.
LingBot-World [203] 2026 2D✓ ✓ ✓ ✓ Block-causal video generator with sub-second
latent rollout for agent training
Geometry-aware perception and spatial memory
LTX [76] 2024 2D✓ ✓ ✓ Uses video diffusion in a real-time open-
source world model.
Sparse World [44] 2025 4D✓ ✓ ✓ ✓ Range-Adaptive Perception module learns
queries modulated by the ego vehicle with
temporal-spatial associations to enable
extended-range perception. Some self-control
over learning during training.
MosaicMem [240] 2026 3D✓ ✓ Hybrid 3D-patch + latent memory for video
world models.
StereoWorld [197] 2026 2D+depth✓ ✓ Generate stereo video natively via camera-
aware RoPE and epipolar-constrained atten-
tion, grounding geometry from disparity.
ViewRope [225] 2026 2D+depth✓ ✓ ✓ Replace pixel-grid positional embeddings with
camera-ray-based RoPE so video world mod-
els stay 3D-consistent across viewpoints
Reasoning and action-conditioned prediction
DIAMOND [5] 2024 2D✓ ✓ ✓ Conditions on previous latent state and ac-
tions to produce future frames.
Dream2Flow [50] 2025 Hybrid✓ ✓ ✓ Generate human-interaction videos, extract
3D object trajectories, then have robots track
those trajectories to manipulate.
Garrido et al. [65] 2026 2D✓ ✓ Learn action-conditioned world models from
unlabeled in-the-wild videos by inferring con-
tinuous latent actions via inverse dynamics.
EgoWM [12] 2026 Hybrid✓ ✓ Fine-tune pretrained video diffusion models
with lightweight action conditioning to get
cross-embodiment egocentric world models.
EMERALD [28] 2026 Hybrid✓ ✓ ✓ MaskGIT-based parallel token prediction in
spatial latent space for accurate yet efficient
model-based RL world models.
Imagination / embodied world generation
AdaWorld [63] 2025 Hybrid✓ ✓ ✓ Pretrain world models with self-supervised
continuous latent actions from video, then
cheaply adapt to new environments by map-
ping real actions to latent ones.
GigaWorld-0 [200] 2025 3D✓ ✓ ✓ World model data engine integrating video
generation and 3DGS with physics simulation
TesserAct [263] 2025 3D✓ ✓ ✓ 4D embodied world model converting gener-
ated RGB-D-Normal video to point clouds for
action prediction
Genie [25] 2024 2D✓ ✓ ✓ ✓ Unsupervised training on unlabeled internet
video for conditional spatio-temporal world
representations enabling simulation training
with RL and downstream policy models.
continued on next page
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 20

```text
20 Rupprecht et al.
Table 3 –continued from previous page
Work Year Geometry
Mem.
Perc.
Lang.
Reas.
Imag.
Moti.
Meta.Description
Motivation / reward- or surprise-guided alignment
Le et al. [119] 2025 2D✓ ✓ ✓ Post-train video diffusion with verifiable New-
tonian rewards to enforce physically correct
motion. Self-evaluation during training.
WMReward [242] 2025 2D✓ ✓ ✓ ✓ Post-train an action-conditioned world model
for zero-shot robot planning. Self-reflection,
Self-control, self-evaluation at inference.
Cambrian-S [234] 2025 2D✓ ✓ ✓ ✓ Define spatial supersensing hierarchy, bench-
mark it, and use prediction-error as surprise
to drive memory/attention in long videos.
PhyWorld [259] 2026 2D✓ ✓ Direct Policy Optimization for physically
aligned video generation
Metacognition / self-improvement
RLVR-World [220] 2025 2D✓ ✓ ✓ ✓ Trains world models with RL using verifiable
rewards; enables self-improving world models
Jang et al. [99] 2026 2D✓ ✓ ✓ Self-reflection through iteratively denoise-
and-re-noise video latents at inference time
to self-evaluate for physics/motion artifacts.
4.1 World Model Representation
Effective video world models require representations that capture both the spatial structure of a
scene and its temporal evolution. In the language of Cognitive Architecture Theory (CAT), this
corresponds primarily toperception, which encodes the state space for world interaction, and
memory, which preserves information needed for temporal coherence, long-horizon prediction,
and persistent world understanding.
4.1.1Perception.Perception in video world models refers to the ability to encode visual observa-
tions into latent states that preserve object identity, spatial layout, motion, geometry, and physical
regularities. This is especially challenging in generated video, where small perceptual errors can
accumulate into temporal artifacts, geometric drift, or physically implausible motion.
Several works address perceptual consistency directly during inference time. Self-Refining Video
Sampling [99] uses the video generator itself as an inference-time refiner. Rather than relying on
an external verifier or additional training, it iteratively denoises and re-noises video latents to
reduce artifacts and improve motion consistency. PhysicsMind [143] complements such methods
by introducing a benchmark for evaluating physical perception and generation, including both
visual question answering (VQA) and video generation tasks.
Other works improve perception during training, with some vision-language models showing
that carefully curated multimodal data alone can help align models with physical laws. Order
of Chaos [29] shows that carefully curated multimodal data can implicitly align vision-language
models with physical regularities. Its PhysGame dataset uses question-answer pairs about glitches
and visual anomalies in video-game footage, suggesting that simulated environments can provide
scalable supervision for physical and perceptual alignment.
Geometry-aware perception has also become increasingly important for maintaining viewpoint
consistency and reducing spatial drift in video world models. ViewRope [225] replaces standard
pixel-grid positional encodings with camera ray-based rotary embeddings, allowing attention to
reason over viewpoint geometry. Similarly, StereoWorld [197] grounds stereo video generation
through disparity and epipolar constraints, while 3D and hybrid models such as MosaicMem [240]
and TesserAct [263] explicitly lift visual evidence into spatial representations. Together, these works
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 21

```text
Human Cognition in Machines: A Unified Perspective of World Models 21
Video World Models
T R A I N I N G
autoregressive self-rollout · holistic DMD on the full generated video
Video Chunks
pixel frames
z0
VAE Encoder
KV CACHE
causal context · persistent memory
self-rollout
read · append (K,V)
C A U S A L A R D i T · W a n 2 . 1 - 1 . 3 B
attn+FFN attn+FFN
 attn+FFN attn+FFN
× L causal layers
self-generated context · flow-matching denoising
generated latents x̃₀
full latent sequence ·
no decode required
DMD LOSS
∇θKL
DKL (pθ ‖p data )
holistic · video-level
∇θupdates causal student
(A) Self Forcing · Huang et al. 2025
T R A I N I N G
self-rollout · reward-weighted DMD (Re-DMD) on VLM motion-quality score
Video Chunks
pixel frames
z0
VAE Encoder
KV CACHE
causal context · persistent memory
self-rollout
read · append (K,V)
C A U S A L A R D i T · W a n 2 . 1 - 1 . 3 B
attn+FFN attn+FFN
 attn+FFN attn+FFN
× L causal layers
self-generated context · reward-weighted DMD
generated latents x̃₀
full latent sequence
DMD LOSS
∇θKL
DKL (pθ ‖p data )
reward-weighted ·
video-level
x̃₀
x0
VAE Decoder
Decoded Video
pixel frames
REWARD MODEL
VLM motion score
low
mid
high
r in [0,1]
Reward Function
r
×
DMD∇θ
r ·∇θKL (reward-weighted)
(B) Reward Forcing · Lu et al. 2025
T R A I N I N G
three-stage distillation · AR teacher→causal ODE distillation→asymmetric DMD
Video Chunks
pixel frames
z0
VAE Encoder
AR DiT (teacher)
teacher-forced
multi-step
AR Diffusion (teacher)
PF-ODE flowφ(x t, t)
xt
τ ∈ (0,1)
x₀
causal ODE
paired (x t, x 0)
KV CACHE
causal context · persistent memory
teacher-forced
read · append (K,V) of GT prefix
C A U S A L A R D i T ( s t u d e n t ) · W a n 2 . 1 - 1 . 3 B
attn+FFN attn+FFN
 attn+FFN attn+FFN
× L causal layers
injectivity preserved · learns flow map from AR-teacher
generated
latents x̃₀
asymmetric DMD
DMD LOSS
∇θKL
DKL (pθ ‖p data )
holistic · video-level
∇θupdates causal student
(C) Causal Forcing · Zhu, Zhao et al. 2026
Memory Perception Language Reasoning Motivation
Hypothetical reasoning Meta-cognition (rainbow)
Fig. 4. Representative architectural paradigms in video world models, including autoregressive causal rollout,
bidirectional or masked generation, and promptable or action-conditioned prediction.
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 22

```text
22 Rupprecht et al.
Video World Models
I N F E R E N C E
chunk-wise causal AR diffusion · 4-step few-step denoising · ~17–23 FPS streaming output
Noise Seed
xt ~ N(0, I)
noisy chunk per step
PERSISTENT MEMORY
SF / CF: fixed-size rolling window · RF: sliding window + EMA-sink
read · append (K,V)
CAUSAL AR DiT · Wan2.1-1.3B
attn+FFN attn+FFN
 attn+FFN attn+FFN
× L causal layers
4-step few-step denoising per chunk
clean chunk x̂₀
Streaming Video
3 latent frames per chunk · ~17–23 FPS
append (K,V) of clean chunk next iteration
Inference · shared across Self / Reward / Causal Forcing
Memory Perception Language Reasoning Motivation
Hypothetical reasoning Meta-cognition (rainbow)
Fig. 5. Representative architectural paradigms in video world models, including autoregressive causal rollout,
bidirectional or masked generation, and promptable or action-conditioned prediction.
suggest that robust perception in video world models increasingly requires not only appearance
modeling, but also geometry-aware latent structure.
4.1.2Memory.Memory enables video world models to maintain coherent latent states over time.
This includes short-term memory for local temporal consistency, long-term memory for persistent
objects and scene layout, and structural spatio-temporal memory for maintaining geometric or
semantic continuity across viewpoints, clips, and actions.
Cosmos-Predict2.5 [4] exemplifies a unified world model representation, learning a latent world
model:
𝑧𝑡+1 ∼𝑝 𝜃 (𝑧𝑡+1 |𝑧 𝑡, 𝑎𝑡, 𝑐),
where the conditioning signal 𝑐 may correspond to text, images, or video context. Its temporally
causal tokenizer supports incremental state updates, while flow matching and post-training improve
physical fidelity. This design unifies Text2World, Image2World, and Video2World generation,
though its dynamics remain largely implicit and may therefore be difficult to interpret or control.
Other models introduce more explicit memory mechanisms, since encoding a consistent repre-
sentation of the world for 2D and 3D scene generation requires an effective storage and retrieval
strategy. To construct a 3D model of the world, MosaicMem [240] stores and retrieves image patches
lifted to 3D using estimated depth and camera poses, enabling spatially consistent retrieval and
view-aligned composition. Marble world model [123, 202] instead represents the world through a
continuous 3D radiance-like structure, instead of patches or pixels. This large set of semitransparent
particles, known as 3D gaussian splats [106], is amongst the highest-fidelity representations for
scene generation. In 2-dimensional scene generation, to establish a robust state space encoding for
memory, V-JEPA [15] introduces a new space encoding for world representation that is trained
solely using a feature prediction objective, completely bypassing the use of pretrained image en-
coders or other sources of supervision. Similarly, VideoREPA [256] refines the model’s internal
state representations during training by aligning token-level relations across spatial and temporal
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 23

```text
Human Cognition in Machines: A Unified Perspective of World Models 23
Video World Models
P R O M P T A B L E G E N E R A T I O N
multilingual text + initial frame/video · end-to-end DiT with internal VAE & text encoders · flow-matching head · optional LLM backbone for stateful rollout
PAN's Hypothetical Reasoning · autoregressive backbone · optional
"drive through
a field of flowers"
a 1
… "…"
a T
AUTOREGRESSIVE VLM BACKBONE
Qwen2.5-VL-7B ŝ 1 … ŝ T
× T autoregressive
steps
"drive through
a field of flowers"
Language
text prompt · NL action
Initial Frame / Video
RGB conditioning
L A T E N T D I F F U S I O N D i T · W a n 2 . 1 - b a s e d
TEXT ENCODER
Cosmos-Reason1 / umT5
VAE ENCODER
Wan-VAE patchify
shared embedding
image patches + text tokens
⋯
attn + FFN attn + FFN attn + FFN attn + FFN
× L DiT layers
self-attn + cross-attn (text) + FFN
flow matching · video denoising head
noiseε →predicted video latent x ˆ 0
ŝ t PAN only
Future Frames
video output
ŝ t
per-step a t
xˆ
0→video
Ali et al. 2025 (Cosmos-Predict2.5) · Xiang et al. 2025 (PAN)
(A) Promptable Multi-Modal Video World Model
B I D I R E C T I O N A L D E C O D I N G
training: full self-attention over all tokens · inference: MaskGIT-style parallel decoding with cosine schedule
TRAINING
Full Context
spatiotemporal tokens
(from replay buffer)
BIDIRECTIONAL DiT / MaskGIT
⋯
× L layers · full bidir attn
zt input: τ ∼U[0,1) All Tokens Predicted
all filled · denoised
TSSM
temporal transformer · masked self-attn · ×L layers
fuses past frames z < t with past actions a < t
past actions
(from replay buffer)
ht−1 ht
z<t
a<t
real zₜwith random maskingτ ∼U[0,1) · predict the masked positions · conditioned on hₜfrom TSSM
INFERENCE (parallel decoding)
TSSM
temporal transformer · masked self-attn · ×L layers
fuses past frames z < t with past actions a < t
Past Frames
Past Actions
ht−1 ht
MaskGIT PARALLEL DECODING
τ=1 predict
τ≈0.7 unmask
τ≈0.4 unmask
τ=0 refine
Hi-Qual. Frames
parallel · denoised
ACTOR-CRITIC
π(a|s) · v(s)
reward + val · latent RL
Action a t
AR (sequential):
256 steps · 1 tok/step
≈4.6 s
MaskGIT (parallel):
8 steps · all toks/step
≈0.21 s
30×–64× speedup over VQGAN AR (Chang et al. 2022) · 27 FPS streaming on RTX 3090 (Burchi & Timofte 2025)
Chang et al. 2022 (MaskGIT) · Peebles & Xie 2023 (DiT) ·Burchi & Timofte 2025 (EMERALD)
(B) Bidirectional / Masked / Parallel Generation
Memory Perception Language Reasoning Motivation
Hypothetical reasoning Meta-cognition (rainbow)
Fig. 6. Representative architectural paradigms in video world models, including autoregressive causal rollout,
bidirectional or masked generation, and promptable or action-conditioned prediction.
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 24

```text
24 Rupprecht et al.
dimensions with a Token Relation Distillation (TRD) loss. In doing so, VideoREPA aligns the spatial
and temporal token relations of generative diffusion models with robust representations from
self-supervised foundation models.
Beyond structural coherence, a major challenge for video world models is extending memory
over long horizons. Gumbsch et al. [ 73] address this through hierarchical world models with
adaptive temporal abstractions, where discrete latent dynamics identify meaningful change points
and preserve stable contexts for long-horizon prediction. In this sense, memory is treated as a
hierarchy of stable states and temporally abstract events, instead of simply a longer context window.
VideoWeave [57] addresses long-context degradation from a data-centric perspective by splicing
short captioned videos into longer synthetic sequences, forcing models to track persistent latent
states across narrative transitions. Alternatively, Video-GPT [272] combines autoregressive memory
with diffusion throughNext Clip Diffusion. This enforces strict causal clip-to-clip dependence using
historical clean clips to maintain exceptionally stable internal memory over long-horizon video
generation.
Several works focus specifically on converting bidirectional video generators into long-horizon
autoregressive world models. Self-Forcing [92] addresses the train-test exposure bias by simulating
inference conditions during training, performing autoregressive rollouts with rolling KV caching
to condition future frames on the model’s own self-generated past. Building on this, Causal Forc-
ing [269] uses an autoregressive teacher for ODE distillation, encouraging strict causal history
mapping. Reward Forcing [141] takes a structural approach to long-term memory via theEMA-Sink
mechanism, which maintains fixed-size context tokens for long-term coherence. Finally, some
works achieve real-time speeds due to their effective and efficient world representation [76, 243].
Helios [243] approaches long-horizon memory through a highly optimized deep compression
flow. Rather than relying on standard anti-drifting memory heuristics like self-forcing, Helios
heavily compresses the historical and noisy context and explicitly simulates drifting during training.
Overall, these methods show that memory in video world models is not merely a matter of context
length, but of designing latent states that remain stable and causal under repeated rollout.
4.2 World Model Prediction and Generation
The generation phase evaluates whether a world model can use its internal state to predict coherent
future trajectories. Within the CAT framework, this phase primarily involvesreasoning, which
governs causal and temporal consistency,imagination, which enables hypothetical rollout and
counterfactual simulation, andmotivation, which introduces reward- or objective-driven pressure
toward physically or task-relevant futures. Figures 4 5 and 6 shows the various architectures
encountered in this review for 2D and 3D scene generation.
4.2.1Reasoning.Within video world models,reasoninggoverns future-state generation under
physical and temporal constraints. Architecturally, these mechanisms align with the paradigms
illustrated in Figures 4 5 and 6, each corresponding to a different instantiation of the world transition
function 𝑊𝜃 . Together, these paradigms define a spectrum, from strictly causal reasoning to globally
optimized trajectory generation, with action-conditioned models bridging toward embodied control.
Autoregressive causal rollouts.Autoregressive world models (Figures 4 and 8) generate future
states sequentially:
𝑧𝑡+1 =𝑊 𝜃 (𝑧 ≤𝑡 ),
conditioning each prediction on previously generated states. This enforces causality through
masked attention, recurrent state updates, or rolling context windows [57, 269, 270]. Reasoning in
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 25

```text
Human Cognition in Machines: A Unified Perspective of World Models 25
this paradigm emerges as a chain of locally consistent transitions, though compounding error over
long horizons remains a central challenge.
Promptable and action-conditioned world models.Action-conditioned models (Figure 6(A)) explic-
itly control transition dynamics:
𝑧𝑡+1 =𝑊 𝜃 (𝑧𝑡, 𝑎𝑡, 𝑐),
where 𝑎𝑡 denotes actions and 𝑐 may include language prompts, initial observations, goals, or
other conditioning signals. These models most closely align with embodied reasoning because
they simulate the visual consequences of interventions. EgoWM [12], for example, injects motor
commands into pretrained video diffusion backbones for controllable egocentric prediction, while
Dream2Flow [50] extracts 3D object flow from generated videos to ground predicted transitions in
physically meaningful transformations.
Bidirectional and masked generation.Bidirectional or diffusion-based world models (Figure 6(B))
instead model the joint distribution over a trajectory:
𝑧1:𝑇 ∼𝑝 𝜃 (𝑧1:𝑇 ),
and iteratively refine the sequence through denoising or masked token prediction [5, 28, 161]. Here,
reasoning is less strictly causal but more globally optimized, allowing the model to revise earlier
and later states jointly, correcting inconsistencies across space and time during generation.
Latent actions and geometric constraints.Several works improve reasoning by structuring the
latent transition space. Garrido et al. [65] jointly learn inverse and forward dynamics,
𝑎𝑡 ≈𝑓 −1 (𝑧𝑡, 𝑧𝑡+1 ), 𝑧 𝑡+1 =𝑓(𝑧 𝑡, 𝑎𝑡 ),
allowing continuous latent actions to be discovered from uncurated video. ViewRope [225] incor-
porates camera-ray geometry directly into attention, augmenting the transition function 𝑊𝜃 with
explicit spatial constraints to prevent geometric drift.
Hierarchical and Sim-to-Real reasoning.For embodied deployment, predicted trajectories must
remain meaningful under domain shift. Hierarchical world models address this by decomposing
prediction across temporal scales:
𝑧 (𝑙)
𝑡+1 =𝑊 (𝑙)
𝜃 (𝑧 (𝑙)
𝑡 , 𝑧(𝑙+1)
𝑡 ),
where higher-level abstractions guide lower-level transitions. Gumbsch et al. [73] show that learning
temporal abstractions around meaningful change points can support long-horizon consistency
while preserving executability in real-world settings. Dream2Flow [ 50] further contributes by
constraining transitions through 3D object flow, ensuring that imagined trajectories correspond to
physically realizable actions.
4.2.2Imagination.Imagination refers to the ability of a world model to generate hypothetical
futures that need not have been directly observed, but remain plausible enough to support planning,
exploration, or policy learning. In video world models, imagination is realized through control-
lable rollout,i.e., the model simulates how a scene may evolve under actions, prompts, or latent
interventions.
Genie [25] is an early example of this shift from passive video generation to interactive envi-
ronment modeling. Trained on unlabeled internet videos, Genie demonstrates that frame-level
controllability can emerge without ground-truth action labels or domain-specific robotic supervi-
sion. Expanding on this, Dream2Flow [50] extracts 3D object flow from dreamed videos to serve
as a modality-agnostic intermediate representation for open-world manipulation. By translat-
ing AI-generated video rollouts into executable trajectory tracking actions without task-specific
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 26

```text
26 Rupprecht et al.
demonstrations, it bridges the gap between hallucinated video generation and physical robotic
control.
AdaWorld [63] addresses the adaptation problem by pretraining world models with self-supervised
continuous latent actions extracted from unlabeled video. At deployment time, real actions can be
mapped into the learned latent action space, reducing the need to retrain for each new environ-
ment. Finally, EMERALD [28] enhances DIAMOND [5] and Dreamer-style agents with MaskGIT-
based [31] parallel token prediction in a spatio-temporal latent representation. This allows jointly
encoding spatial structure alongside temporal dynamics to improve accuracy and efficiency in
model-based RL for sim-to-real transfer. Astra [270] extends this with an autoregressive denoising
framework that supports long video horizons sufficient for future prediction comparable to motor
control, addressing the practical requirement of imagined rollouts for real-world environments.
4.2.3Motivation.Motivation introduces objective-driven constraints into video world models.
Rather than generating only visually plausible sequences, motivated world models are guided by
rewards, prediction errors, or physical constraints that encourage useful and realistic futures.
Le et al. [119] explicitly align generated videos with physical laws by introducing verifiable,
physics-grounded rewards during post-training. These rewards penalize violations of Newtonian
dynamics, such as gravity and momentum, steering the model toward physically consistent rollouts.
Similarly, PhyWorld [259] grounds video generation to physical laws with direct policy optimization.
We also see VJEPA-2 [9] use a latent world model with strong intuitive physics as an inference-time
critic, scoring candidate trajectories and favoring predictions that better satisfy physical plausibility.
In terms of spatial and temporal awareness, Cambrian-S [234] introduces a complementary form
of motivation based on surprise. Its sensing mechanism uses prediction error to guide memory
updates and event segmentation in long visual streams, connecting video world models to principles
from active inference [59–61, 162]. Here motivation is not limited to external rewards, but can also
arise from internal signals that identify when the world has changed in a meaningful way.
4.3 Trends and limitations.
In summary, video world models are shifting from passive video synthesis toward structured,
controllable world simulation. The field increasingly emphasizes geometry-aware perception,
persistent latent memory, long-horizon rollout, and action-conditioned generation. Approaches
such as ViewRope [225], StereoWorld [197], MosaicMem [240], and TesserAct [263] illustrate this
trend by lifting visual evidence into spatial representations to maintain viewpoint consistency.
Yet key limitations remain: learned dynamics are often implicit and difficult to verify; long-
horizon predictions are still subject to drift and compounding error; and 3D consistency often
depends on additional depth, pose, or geometric priors. It is noteworthy that, motivation and
metacognition also remain weakly developed. For example, Cambrian-S [ 234] uses prediction
error as a surprise-like signal, resembling Active Inference. Yet it does not explicitly formulate
intrinsic motivation through Active Inference’s exploration reward nor optimize a loss that models
intrinsic latent dynamics. Instead, Cambrian-S relies on pixel-level prediction error as a proxy for
surprise, omitting the information-gain term that drives exploratory behavior. This reduction is
valid if the next-latent predictive distribution is taken to be Gaussian with fixed variance, in which
case the accuracy (negative log-likelihood) term of the free energy reduces to a scaled squared
error between the predicted and observed means, i.e., MSE [21, 59, 82]. A predictive objective that
additionally captures epistemic uncertainty would more closely realize the full active-inference
objective. Addressing these gaps will require video world models that couple scalable generative
priors with explicit spatial structure, physically grounded objectives, intrinsic motivation, and
mechanisms for evaluating and regulating their own predictions.
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 27

```text
Human Cognition in Machines: A Unified Perspective of World Models 27
Embodied World Models
Current Frame
RGB / RGB-D visual tokens
"pick up the cup"
Language Task
task instruction
V L M B A C K B O N E
VIT / SIGLIP
TEXT EMBED
shared embedding
image patches + text tokens
attn + FFN attn + FFN
···
attn + FFN
× L layers
self-attn (vis + lang) · cross-modal attn
diffusion head · flow matching
noise→continuous action tokens
VLM / Direct Policy
Action Output
trajectory
Black et al. 2025 (π 0.5)· Wu et al. 2026 (LingBot-VLA)· GigaAI 2025 (GigaBrain-0)
(A) Vision–Language–Action Model
KV CACHE
causal context · persistent memory
read · append (K,V)
Current Frame
RGB / RGB-D visual tokens
"open the drawer"
Language Task
task instruction
S H A R E D G E N E R A T O R
VIT / SIGLIP
TEXT EMBED
shared embedding
image patches + text tokens
attn + FFN attn + FFN
···
attn + FFN
× L layers
cross-modal attention · video-action shared
imagined rollout · flow matching
noise→joint v + a denoising · cached prefix · new chunk only
VLM Initialized
Future Frames
visual rollout
Action Output
trajectory rollout
Ye et al. 2026 (DreamZero)· Li et al. 2026 (LingBot-VA)· Yuan et al. 2026 (Fast-WAM)
(B) World Action Model
Memory Perception Language Reasoning Motivation
Hypothetical reasoning Meta-cognition (rainbow)
Fig. 7. Above are the typical architectures encountered when reviewing embodied world models.
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 28

```text
28 Rupprecht et al.
Embodied World Models
Obs + History
pixels · proprioception
z
Encoder
CNN / VAE
Imagined Rollout · no real env
R S S M · W O R L D M O D E L
GRU
ht
GRU
ht+1
GRU
ht+H
× H imagined steps
recurrent dynamics ·
prior-only rollout
s t s t+1
imagined
model
states
ACTOR-CRITIC
critic v( s )
Action Output
deployed in env
z
Ha & Schmidhuber 2018 (World Models) · Hafner et al. 2019 (Dreamer) · Hafner et al. 2025 (DreamerV3)
(A) Dreamer-style Latent World Model
RGB-D / LiDAR
point clouds
occupancy grids
Geom. Encoder
3D feature extract · downsample
G E O M E T R I C W O R L D M O D E L
Gt
H
steps
 Gt+H
× H geometric rollout
action-conditioned
scene deformation
MPC / PLANNER
CEM sampling
Action Output
trajectory
candidate actions a ~ q(a)
Shi et al. 2024 (RoboCraft) · Zhang et al. 2024 (AdaptiGraph)· Huang et al. 2025 (ParticleFormer)· Huang et al. 2026 (PointWorld)
(B) Planner over Structured Geometry
Memory Perception Language Reasoning Motivation
Hypothetical reasoning Meta-cognition (rainbow)
Fig. 8. Above are the typical architectures encountered when reviewing embodied world models.
5 Embodied World Models
Embodied world models not only demand visual understanding and linguistic reasoning, but also
perceive, act, and anticipate how their actions reshape the physical world. This physical grounding
constraint distinguishes embodied world models from their video generation counterparts (Sec-
tion 4). A video world model succeeds when its generated frames are photorealistic and temporally
coherent. However, an embodied world model succeeds when its predictions are physically accurate
enough to guide a body with mass, kinematics, and contact surfaces toward successful task execution.
These demands on embodied world models heighten the demands for a Unified World Model, as seen
in Figure 3, capable of emulating a broad range of cognitive functions. We explore embodied world
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 29

```text
Human Cognition in Machines: A Unified Perspective of World Models 29
models in robotics [1, 9, 13, 18, 20, 30, 34, 55, 74, 88, 90, 93, 96, 97, 103, 108, 124, 140, 142, 145, 148, 175–
178, 194, 196, 199, 212, 217–219, 222, 224, 236, 237, 244, 253, 266–268], navigation with explo-
ration [103, 177, 194], and autonomous driving [17, 23, 32, 35, 37, 44, 64, 81, 85, 91, 101, 107, 125,
127, 130, 147, 166, 172, 210, 215, 235, 247, 254, 255, 257, 262, 264, 265].
Perceptionmust encode contact geometry and six-degree-of-freedom pose, not merely visual
appearance;Memorymay need to maintain a persistent, spatially-grounded model of the physical
world across interactions, not merely temporal coherence across frames.Reasoningmay need to
capture physical causality and force propagation rather than narrative causality; andImagina-
tionmust generate action conditioned futures that are physically executable, not merely visually
plausible. We explore these novelties following the CAT structure of our unified framework: world
representation in Sec. 5.1 and world generation in Sec. 5.2. Sec. 5.3 summarizes key trends and
limitations of embodied world models.
Table 4. Embodied world model works in Section 5 mapped to Cognitive Architecture Theory (CAT) functions
(Memory, Perception, Language, Reasoning, Imagination, Motivation, Metacognition). A check (✓) indicates
a clear contribution.
Work Year App.
Mem.
Perc.
Lang.
Reas.
Imag.
Moti.
Meta.Description
Foundational / Platform Models
Being-H0.7 [1] 2026 Robot✓ ✓ Action prediction occurs in an action-
centric spatio-temporal latent space, not
pixel-space, eliminating predictive video
Cosmos-Policy [108] 2026 Robot✓ ✓ ✓ ✓ Post-trains Cosmos-Predict-2 for visuo-
motor robot control and planning
DreamZero [237] 2026 Robot✓ ✓ ✓ World Action Model jointly predicting
video and actions; zero-shot policy from
video pretraining
Fast-WAM [244] 2026 Robot✓ ✓ Decouples action prediction from video
generation at inference for faster WAM
deployment
GigaBrain-0 [199] 2025 Robot✓ ✓ ✓ VLA trained on world-model-generated
data with RGBD input and embodied
chain-of-thought
Motus [18] 2025 Robot✓ ✓ ✓ Unified latent action world model via
Mixture-of-Transformers; optical flow as
embodiment-agnostic action
VLA / Language-Grounded Embodied Models
𝜋0.5 [96] 2025 Robot✓ ✓ ✓ Flow-matching VLA decomposing lan-
guage into causally grounded multi-step
physical plans
LingBot-VLA [224] 2026 Robot✓ ✓ ✓ Cross-morphology VLA on 20,000h bi-
manual data with geometry-aware depth
distillation
LingBot-VA [124] 2026 Robot✓ ✓ ✓ ✓ Interleaves video and action tokens for
joint imagination and action decoding
VLA-JEPA [196] 2026 Robot✓ ✓ ✓ ✓ ✓ Leakage-free JEPA grounding visual en-
coder in action-relevant dynamics
VAGEN [212] 2025 Robot✓ ✓ ✓ RL-structured world model reasoning
into state estimation and transition mod-
eling for VLM agents
Being-H0.5 [142] 2026 Robot✓ ✓ ✓ ✓ A foundational VLA for robust cross-
embodiment generalization across di-
verse robotic platforms
World Models for Manipulation
Flash-WAM [3] 2026 Robot✓ ✓ ✓ Step-distillation framework for achiev-
ing inference latency under 350 ms.
continued on next page
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 30

```text
30 Rupprecht et al.
Table 4 –continued from previous page
Work Year App.
Mem.
Perc.
Lang.
Reas.
Imag.
Moti.
Meta.Description
PointWorld [90] 2026 Robot✓ ✓ ✓ ✓ Unifies state and action as 3D point flows
with MPC over imagined scene deforma-
tions
ManiGaussian [140] 2024 Robot✓ ✓ ✓ Dynamic 3DGS world model predicting
future Gaussian scenes under action for
manipulation
RoboScape [178] 2025 Robot✓ ✓ ✓ Physics-informed world model jointly
learning video, depth, and keypoint dy-
namics
EnerVerse-AC [88] 2025 Robot✓ ✓ ✓ ✓ Chunk-wise autoregressive video diffu-
sion with sparse memory and 4DGS for
action-conditioned prediction
UWM [267] 2025 Robot✓ ✓ ✓ Couples video and action diffusion in one
transformer; pretrained on video-only
and video+action data
GR-1 [219] 2024 Robot✓ ✓ ✓ ✓ GPT transformer pretrained on 800K
Ego4D clips jointly predicting actions
and future frames
GR-2 [34] 2024 Robot✓ ✓ ✓ ✓ ✓ Scaled video-language-action model
(719M) achieving 97.7% success across
100+ real tasks
UniPi [55] 2023 Robot✓ ✓ Text-conditioned video diffusion as pol-
icy; extracts actions via inverse dynamics
SuSIE [20] 2024 Robot✓ ✓ ✓ ✓ Image-editing diffusion synthesizing sub-
goal images for goal-conditioned manip-
ulation policy
IRASim [268] 2024 Robot✓ ✓ ✓ Diffusion transformer with frame-level
action conditioning for manipulation
simulation
LaDi-WM [93] 2025 Robot✓ ✓ ✓ ✓ Predicts latent state evolution via diffu-
sion; more generalizable than pixel-level
prediction
FlowDreamer [74] 2025 Robot✓ ✓ ✓ RGB-D world model using optical flow as
explicit physically interpretable motion
supervision
MWM [176] 2023 Robot✓ ✓ ✓ ✓ ✓ Decouples MAE visual representation
from RSSM dynamics; 81.7% on Meta-
World tasks
PIVOT-R [253] 2024 Robot✓ ✓ ✓ ✓ Waypoint-aware world model focusing
prediction on task-relevant key states
Plan2Explore [175] 2020 Robot✓ ✓ world model exploration via ensemble
disagreement for zero-shot task adapta-
tion
DayDreamer [222] 2022 Robot✓ ✓ ✓ Dreamer-style world model learning di-
rectly on physical robots from sparse re-
wards
Dream to Manipulate [13] 2024 Robot✓ ✓ Compositional 3DGS with object decom-
position for imagination-based imitation
learning
RoboDreamer [266] 2024 Robot✓ ✓ ✓ Compositional diffusion world model fac-
torizing language instructions into task
primitives
GenRL [145] 2024 Robot✓ ✓ ✓ ✓ Foundation world models for generaliza-
tion in embodied RL via multimodal pri-
ors
V-JEPA 2 [9] 2025 Robot✓ ✓ Representation-space prediction on 1M
video hours; zero-shot planning via MPC
WorldVLA [30] 2025 Robot✓ ✓ ✓ ✓ Autoregressive action world model uni-
fying video prediction and VLA action
generation
AdaptiGraph [252] 2024 Robot✓ ✓ ✓ Graph Neural Network for world repre-
sented as particles for general purpose
manipulation
RoboCraft [190] 2024 Robot✓ ✓ ✓ ✓ Graph Neural Network for world repre-
sented as particles for elastic materials
continued on next page
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 31

```text
Human Cognition in Machines: A Unified Perspective of World Models 31
Table 4 –continued from previous page
Work Year App.
Mem.
Perc.
Lang.
Reas.
Imag.
Moti.
Meta.Description
Particle Former [89] 2025 Robot✓ ✓ ✓ ✓ Transformer-based reasoning from 3d
point cloud scene observations
Locomotion / Navigation World Models
DreamWaQ [148] 2023 Robot✓ ✓ ✓ ✓ Implicit terrain imagination from propri-
oception for quadrupeds
DreamerNav [218] 2025 Robot✓ ✓ ✓ ✓ DreamerV3 for quadruped navigation
with depth and occupancy; zero-shot sim-
to-real
BADGR [103] 2021 Robot✓ ✓ Self-supervised terrain affordance learn-
ing for outdoor navigation via MPC
ViNT [177] 2023 Robot✓ ✓ ✓ ✓ Visual navigation model with diffusion
subgoal proposals across robot platforms
NoMaD [194] 2024 Robot✓ ✓ ✓ Unifies goal navigation and exploration
with diffusion policy and goal-masking
EVA [217] 2026 Robot✓ Trains a video world model with an in-
verse dynamics reward signal aligns to
physical constraints in world dynamics.
VLM-Safe [166] 2025 Robot✓ ✓ VLM-guided safety rewards steering
imagined rollouts for constrained AV pol-
icy inspired by human cognition
GeNIE [211] 2025 AD✓ ✓ Traversable state prediction enables gen-
eralizing across a wide range of real-
world environments.
Autonomous Driving World Models
OccWorld [264] 2023 AD✓ ✓ ✓ VQVAE tokenizer with GPT transformer
for joint 3D occupancy and ego trajectory
forecasting
Copilot4D [255] 2023 AD✓ ✓ Discrete diffusion over BEV LiDAR to-
kens; 65% Chamfer distance reduction
BEVWorld [257] 2024 AD✓ ✓ ✓ Multimodal tokenizer fusing camera and
LiDAR into unified BEV latent for fore-
casting
SparseWorld [44] 2025 AD✓ ✓ ✓ Sparse dynamic queries modulated by
ego-vehicle state for adaptive scene mem-
ory
Epona [254] 2025 AD✓ ✓ ✓ Decouples temporal memory from spa-
tial generation via causal transformer
and twin diffusion
LiDARCrafter [130] 2025 AD✓ ✓ ✓ ✓ Language-conditioned tri-branch diffu-
sion for 4D LiDAR scene generation
DrivingGPT [37] 2024 AD✓ ✓ ✓ ✓ Interleaved image–action tokens unify-
ing world modeling and planning as next-
token prediction
DOE-1 [265] 2024 AD✓ ✓ ✓ ✓ Closed-loop end-to-end AV model using
free-form text as perceptual interface
LAW [127] 2024 AD✓ ✓ ✓ Self-supervised latent prediction of fu-
ture scene features from observations
and ego trajectories
MILO [32] 2021 AD✓ ✓ Model-based imitation learning mitigat-
ing covariate shift via offline data
KG-based WM [17] 2025 AD✓ ✓ Knowledge graphs with sensor data for
material-aware obstacle reasoning in AVs
PWM [262] 2025 AD✓ ✓ Collaborative state-action prediction for
anticipatory planning in AVs
AdaWM [210] 2025 AD✓ Adaptive world model planning with dy-
namic model selection for autonomous
driving
Think2Drive [125] 2024 AD✓ ✓ Efficient RL via latent world model imag-
ination in CARLA-v2
Raw2Drive [235] 2025 AD✓ ✓ End-to-end AV aligning RL policy with
imagination from raw sensors
continued on next page
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 32

```text
32 Rupprecht et al.
Table 4 –continued from previous page
Work Year App.
Mem.
Perc.
Lang.
Reas.
Imag.
Moti.
Meta.Description
Dream to Drive [147] 2025 AD✓ ✓ ✓ ✓ Analytic world model for dreamer-style
vehicle control without environment in-
teraction
Dream2Drive [64] 2024 AD✓ ✓ ✓ RL in predictive world model imagina-
tion with intention-aware latent states
Large Video Planner [35] 2025 AD✓ Foundation-scale video model for zero-
shot robot video plans to actions
SafeDreamer [91] 2023 AD✓ ✓ Dreamer safe RL pairing imagined trajec-
tories with safety estimations
IRL-VLA [101] 2025 AD✓ ✓ Inverse RL reward world model for effi-
cient closed-loop reward computation in
VLA training
InDRiVE [107] 2025 AD✓ Intrinsic disagreement reward in
Dreamer MBRL for curiosity-driven
vehicle exploration
RDAR [23] 2025 AD✓ ✓ Reward-driven relevance estimation for
safety-critical agents in AV planning
Latent-WAM [215] 2026 AD✓ ✓ ✓ Uses causal transformer to jointly learn
visual and motion dynamics from geom-
etry conditioned world representations
Synthetic Training Data
GAIA-1 [85] 2023 AD✓ ✓ ✓ Generative world model with discrete la-
tent space for scalable synthetic data
GAIA-2 [172] 2025 AD✓ ✓ ✓ Controllable multi-view generative
world model with continuous latent
space for scalable synthetic data
Dream4Drive [247] 2025 AD✓ Repurposes world model imagination for
scalable synthetic data
MoSim [81] 2025 AD✓ ✓ ✓ Motion-grounded simulation generating
diverse controllable traffic scenarios
DreamGen [97] 2025 Robot✓ ✓ Fine-tunes Cosmos-Predict-2.5 as syn-
thetic data engine for policy training
5.1 World Model Representation
5.1.1Perception.In embodied world models perception must encode the physical structure of the
scene rather than visual appearance alone. This makes 3D occupancy a natural representation for
world models as it is expressive, efficient, and versatile across both vision and LiDAR inputs [264].
OccWorld operationalizes this by learning in 3D semantic occupancy space, using a VQVAE-based
scene tokenizer to produce discrete scene tokens that jointly forecast future occupancy and ego
trajectory through a GPT-like spatial-temporal transformer, all without requiring instance or map
annotations [264]. Building on the same tokenize-then-predict philosophy, Copilot4D [255] further
addresses the scalability of this perceptual pipeline by applying discrete diffusion over BEV tokens
derived from raw LiDAR point clouds, reducing prior state-of-the-art Chamfer distance by over
65% for one-second prediction across multiple benchmarks [255].
5.1.2Memory.A central challenge in embodied world models is maintaining a compact yet suffi-
ciently rich state space encoding of the scene across time. BEVWorld addresses this by compressing
heterogeneous multimodal inputs including camera imagery and LiDAR point clouds into a unified
Bird’s Eye View latent space through a self-supervised multimodal tokenizer, enabling temporally
consistent future scene forecasting via a latent BEV sequence diffusion model conditioned on action
tokens [257]. While BEVWorld [257] establishes a shared spatial memory across modalities, it relies
on static grid-based representations that struggle to adapt to the dynamic and continuous nature of
real driving environments. SparseWorld addresses this limitation directly by replacing fixed grid
embeddings with sparse and dynamic queries modulated by the ego vehicle’s state, allowing the
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 33

```text
Human Cognition in Machines: A Unified Perspective of World Models 33
memory encoding to scale its perception range with vehicle speed and adapt to foreground object
dynamics rather than treating all voxels uniformly [44].
Epona [254] takes a complementary approach to the memory problem by identifying that
conventional video diffusion models entangle temporal memory with spatial generation, leading to
error accumulation in long-horizon rollouts. By decoupling the two through a GPT-style causal
transformer that handles temporal context in compressed latent space separately from twin diffusion
transformers that handle spatial rendering and trajectory generation, Epona achieves stable long-
duration prediction with a 7.4% FVD improvement over prior works [ 254]. Further advancing
perception, LaDi-WM [93] finds that predicting the evolution of the latent space is easier to learn
and substantially more generalizable than directly predicting pixel-level images in diffusion models.
5.1.3Language.In the CAT framework, language serves as a semantic and symbolic encoding
that connects human intent to world state, and in embodied driving this role becomes particularly
concrete. LiDARCrafter [130] demonstrates this most directly by using free-form natural language
instructions as the entry point for 4D LiDAR world modeling, parsing text into ego-centric scene
graphs that condition a tri-branch diffusion network to generate object structures, motion trajec-
tories, and geometry, with an autoregressive module then extending the result into temporally
coherent LiDAR sequences [130]. Where LiDARCrafter [130] uses language to control a geometric
representation, DrivingGPT [ 37] uses it to unify the entire driving pipeline by constructing a
multimodal driving language from interleaved image and action tokens, treating world modeling
and trajectory planning as a single next-token prediction problem over this shared symbolic vocab-
ulary [37]. DOE-1 [265] takes this unification further by closing the loop entirely, using free-form
text scene descriptions as the perceptual interface and autoregressively generating perception,
prediction, and planning tokens within one multimodal transformer, achieving the first closed-loop
end-to-end autonomous driving model under this paradigm [265].
5.2 World Model Generation
5.2.1Reasoning.Architectures for embodied world models primarily differ along the following
axes (with some sampled in Fig. 7 and 8):
Geometric world models.PointWorld [ 90] and other geometric world models [89, 90, 130, 140, 178,
190, 252, 257, 264] represent the opposite extreme, grounding reasoning directly in 3D structure by
predicting scene flow Δx =𝑓 𝜃 (x, 𝑎𝑡 ) over point clouds. This enforces physically meaningful state
transitions and enables cross-embodiment generalization without task-specific heads. However, it
depends on strong geometric supervision and may be less flexible for abstract or semantic tasks.
Language-conditioned planning. 𝜋0.5 [96] treats reasoning as long-horizon planning conditioned
on language, implicitly learning
𝑎1:𝑇 ∼𝜋 𝜃 (𝑎1:𝑇 |𝑧 0, ℓ)
where ℓ encodes task structure. This enables coherent multi-step behavior across diverse environ-
ments, but places significant burden on the latent representation to maintain causal consistency
over long horizons. Vision-Language-Action (VLAs) models [30, 96, 101, 124, 142, 196, 212, 224]
excel in reactive and instruction-following settings but rely on either external planners or hybridiza-
tion with World Action Models (WAMs) when long-horizon physical reasoning or counterfactual
simulation is required. A central limitation of WAMs is the number of denoising steps, which can
be as high as 10 in LingBot-VA, leading to higher latencies.
Autoregressive world-action models.Because VLAs are reactive and under-supervised and map ac-
tion directly, with no explicit model of future researchers turn to World Action Models (WAMs) [1, 17,
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 34

```text
34 Rupprecht et al.
18, 30, 32, 81, 124, 215, 236, 237, 244, 262]. Two such works, LingBot-VA [124] and DreamZero [237]
unifies imagination and control by modeling joint sequences
(𝑧𝑡+1, 𝑎𝑡 ) ∼𝑝 𝜃 (𝑧𝑡+1, 𝑎𝑡 |𝑧 ≤𝑡 )
with causal or block-causal attention. These approaches improve temporal consistency and enable
efficient rollout, but remain sensitive to representation quality and training stability.
Representation-driven reasoning.VLA-JEPA [ 196] highlights that reasoning quality depends
critically on the learned state space, enforcing dynamics-consistent representations 𝑧𝑡 =𝜙(𝑜 𝑡 ) that
are invariant to irrelevant visual variation. This improves generalization, but shifts complexity into
representation learning as recent works show [9, 93, 127, 176, 196, 210].
Planning-centric extensions.Across paradigms, there is a convergence toward explicit planning
over learned dynamics [64, 90, 91, 127, 166, 175, 210] to predict actions in the form,
𝑎∗
𝑡 =arg max
𝑎𝑡:𝑡+𝐻
E
" 𝐻∑︁
𝑘=0
𝑟(𝑧 𝑡+𝑘 )
#
,
as seen in model-predictive control (PointWorld [90]), self-supervised world models (LAW [127]),
and latent RL pipelines [210]. These approaches improve controllability and robustness, but depend
on accurate forward models.
Figures 7 and 8 can thus be interpreted as a spectrum: generative models offer scalability
and multimodal unification; geometric models provide strong physical grounding; and planning-
based approaches enable controllable long-horizon reasoning. Most recent systems hybridize these
axes, suggesting that effective reasoning emerges from combining expressive latent models with
structured representations and explicit planning.
5.2.2Imagining.In embodied world models, imagination manifests as dreaming [ 64, 91, 107,
147, 148, 218, 222], as well as action-conditioned hypothetical reasoning, where agents simulate
future trajectories in latent space to guide policy learning and planning [35, 85, 97, 147, 172, 247].
Works such as Think2Drive [125] and Raw2Drive [235] leverage world models to generate imagined
rollouts for training driving policies, while autoregressive approaches model multiple probabilistic
futures to reason under uncertainty [227]. Dream2Drive [64] further demonstrates this paradigm
by operating within a learned imagination space (PIWM), using intention-aware latent states to
evaluate candidate trajectories for urban navigation [64]. More recent systems integrate imagination
directly into the training loop, enabling policies to be optimized through interaction with an internal
simulator rather than the real environment [68].
Beyond policy learning, imagination enables safety-aware planning and scalable data generation.
world models can pair imagined roll outs with safety estimates to guide actor–critic optimization
under additional constraints, such as VLM-based safety signals [166]. At larger scale, foundation
video models generate zero-shot trajectory plans from internet-scale data, which can be converted
into executable robot actions [ 35], while broader dreaming pipelines [ 147], including Cosmos-
Drive-Dreams [167], GAIA-1, GAIA-2 [85, 172], and Dream4Drive [247] use synthetic rollouts as
training data. Benchmarks such as WorldLens evaluate the physical fidelity of these imagined
trajectories [129], reinforcing imagination as a core mechanism for bridging perception, reasoning,
and action in embodied settings.
5.2.3Motivation.Motivation in embodied world models defines how agents evaluate imagined
trajectories during learning and control [ 23, 64, 89–91, 101, 107, 127, 166, 175, 190, 210]. IRL-
VLA [101] learns a lightweight reward world model via Inverse Reinforcement Learning for efficient
closed-loop optimization [101], while InDRiVE [107] leverages intrinsic disagreement-based rewards
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 35

```text
Human Cognition in Machines: A Unified Perspective of World Models 35
within a Dreamer-style MBRL framework to drive exploration [107]. Additional approaches refine
reward signals for task relevance in autonomous driving settings [23], reflecting a shift toward
learned and uncertainty-aware objectives over hand-crafted rewards. Safe-Dreamer motivates
models to conform to safety criteria by incorporating Lagrangian-based methods into planning [91].
5.3 Trends and Limitations
Typical implementations of World Action Models though capable of robust reasoning lack the
efficiency of direct policy networks such as VLAs. Some World Action Model works [124, 237, 244]
achieve efficiency gains through the practical implementation ofmemorymechanisms such as
KV-cache. KV-cache allows the reuse of previously generated transformer activations allowing the
models to avoid recomputation across subsequent forward passes as depicted in Fig. 7
Another recent work combines the utility of both WAMs and VLAs in what they call a latent
World Action Model or BeingH-0.7 [1]. BeingH-0.7 argues that pixel-space WAMs are inefficient
(e.g. VLAs can be up to 60x cheaper in compute) and imperfectly predicted pixels can lead to
bad downstream actions. The solution they argue is to combine VLAs and WAMs by bridging
direct action prediction and world modeling through a shared latent space. It is this efficiency in
reasoningthat allows multiple queries of hypothetical reasoning which was previously considered
unobtainable in traditional WAM settings.
Many embodied world models suffer from inefficiencies inreasoning, require expensive hard-
ware for robustperception, or rely on training data that is costly to create. Efficiency in the
Embodied setting arises inmemory-enabled efficient WAM’s and hybrid VLA-WAM models. The
later innovate across all components of cognition, by introducing to VLAs a robustmemory
mechanic for conditioning action selection on latent future world states, while maintaining effi-
ciency enabling hypothetical reasoning. These hybrid VLA-WAMs are true Unified world models
as depicted in Fig. 3 only lacking intrinsic motivation and metacognition. Even more recently,
World Action Models are showing future video prediction can be expendable achieving highly
efficient runtime latencies [ 3, 244]. However, Fast-WAM removes the capability for imagining
future states in its model for further performance gains with little quality drop raising the ques-
tion of the importance ofimaginingin current embodied settings [ 244]. This achieves 190ms
inference latency, or over4 × faster than measured states of the art. Flash-WAM proposes a step
distillation framework deployed on Lingbot-VA reducing action denoising steps to two, and video
denoising steps to one providing 348ms inference latency or23 × speedup over Lingbot-VA during
inference [3]. Both works demonstrate the potential cost savings that can come from reducing
reliance on computationally burdensome future state prediction.
6 Epistemic World Models
World models in agentic frameworks extend beyond latent dynamics prediction to operate over the
scientific process, orchestrating multi-step workflows that integrate perception, memory, reasoning,
and tool use in service of discovery. In contrast to latent world models, which encode external
environments into learned state representations with explicit transition dynamics, these systems
treat structured knowledge as the world itself. In suchepistemic world models, the environment
is a knowledge space defined by literature, databases, and experimental outputs, where domain
expertise induces the state space and scientific artifacts act as observations. Rather than evolving
an internal latent state, the agent updates this epistemic state through reasoning and tool-mediated
operations, effectively controlling externalized cognitive functions.
This distinction highlights two complementary strategies for world modeling: latent compression
of external environments versus explicit maintenance and updating of structured knowledge. Im-
portantly, epistemic world models also instantiate a form of global workspace, where intermediate
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 36

```text
36 Rupprecht et al.
Epistemic World Models
GLOBAL WORKSPACE
Human
developer
R E S E A R C H O R C H E S T R A T O R
× L layers
causal self-attn + FFN
Specialist Prompt
tool-call
LLM Action Orchestrator
plan + route
$ run
ERR 42
Debugger
runtime errors
</>
Code Writer
source · diffs
Project Context
files · CLAUDE.md
Tool Interface
CI · linter · git · MCP
LANGUAGE
Meta-cognition Meta-cognition
(A) Claude Code · Anthropic (2025) · Chatlatanagulchai et al. 2025
GLOBAL WORKSPACE
Human
biologist
R E S E A R C H O R C H E S T R A T O R
× L layers
causal self-attn + FFN
Specialist Prompt
tool-call
LLM Action Orchestrator
plan + route
Cell Annotator
cell sequences
Embedding Engine
sequence→vector
Cell Atlas
tissue ontology Experiment Data
assays · matrices
LANGUAGE
Meta-cognition Meta-cognition
(B) CellAtria · Nouri et al. 2026
GLOBAL WORKSPACE
Human
scientist
R E S E A R C H O R C H E S T R A T O R
× L layers
causal self-attn + FFN
Specialist Prompt
tool-call
LLM Action Orchestrator
plan + route
Literature Review
research corpus · RAG
Analysis Engine
experiment data · Python
Reasoning Engine
hypothesis generation
Debate Agents
critique · review
LANGUAGE
Meta-cognition Meta-cognition
(C) AI Co-Scientist · Gottweis et al. 2025
Memory Perception Language Reasoning Motivation
Hypothetical reasoning Meta-cognition (rainbow)
Fig. 9. Above are the typical architecture and Global Workspace frameworks encountered when reviewing
world models for scientific discovery used with a human-in-the-loop subject-matter expert.
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 37

```text
Human Cognition in Machines: A Unified Perspective of World Models 37
results, tool outputs, and shared context are broadcast across agents and processes. In the sense of
Baars’ Global Workspace Theory [11], these systems approximate metacognition by enabling self-
reflection, self-evaluation, and self-control with selective routing of information across distributed
components and even self-evaluation. As introduced in Sec. 3.3, such workspace-based mechanisms
provide a candidate solution to the lack of metacognition in latent world models. Agentic systems
therefore emphasize reasoning, tool coordination, and persistent memory, while introducing early
forms of metacognitive control through execution tracing and human-in-the-loop feedback. These
capabilities suggest a concrete pathway toward addressing the gaps inmetacognitionandmo-
tivationoutlined in Sec. 3.3, by externalizing and structuring the global workspace required for
self-reflection, self-evaluation and self-control.
In this section, we review world models for Scientific Discovery through the lens of Cognitive
Architecture Theory (CAT), emphasizing Human–AI Collaboration within multi-agent frameworks.
As in previous sections, Sec. 6.1 covers contributions to world model representation (memory,
language, perception), while Sec. 6.2 examines generation and prediction. The reviewed works are
further subdivided according to the cognitive functions they emulate in their designs. Figure 9(a)
illustrates common multi-agent architectures, with (b) highlighting Global Workspace-like struc-
tures for shared domain knowledge. Table 5 summarizes all works within the CAT framework.
Sec. 6.3 summarizes key trends and limitations of epistemic world models.
6.1 World Model Representation
6.1.1Language.In human–AI collaboration systems, language is not only a medium for gen-
eration (e.g., code or hypotheses), but a substrate for shared world representation, coordination,
and self-evaluation, consistent with notions of a global workspace [ 11] as discussed in Sec. 3.1.
In co-science systems such as Gemini Co-scientist [69, 70], OpenAI Prism [155], SciSciGPT [180],
and OmniScientist [179], language encodes hypotheses, project state, and intermediate reasoning,
enabling iterative critique, revision, and verification across multi-agent interactions. Rather than
serving only as input/output, language acts as a persistent interface through which agents construct,
refine, and align their shared world model.
Reliable collaboration depends on maintaining explicit and evolving common ground rather than
relying on opaque internal state [114]. Language enables this by making agent intentions and rea-
soning processes interpretable and contestable [157]. This aligns with theories of human cognition
in which language emerges from the capacity to share intentions, attention, and goals [47, 100, 205].
Viewed through this lens,languagefunctions as an integrative interface linkingperception,
reasoning, andmetacognition, rather than as a standalone token prediction mechanism. It is
through language that internal representations become shared, inspected, and coordinated, enabling
collaborative intelligence over a common world model.
6.1.2Perception.Many software co-pilots extend perception beyond plain text, treating struc-
tured artifacts, speech, and embodied signals as first-class inputs [62, 110, 113, 155, 179, 180, 189, 251].
OpenAI Prism [155] exemplifies document-centric perception by operating directly over LaTeX
structure (equations, references, figures), grounding edits in the manuscript’s semantics. SciS-
ciGPT [180] reframes perception as evidence acquisition, retrieving and parsing literature and
structured datasets to support downstream reasoning. Similarly, OmniScientist [179] organizes
perception into structured representations of scientific knowledge. Across these systems, perception
shifts from passive input processing to active construction of task-relevant representations.
In embodied and assistive settings,perceptionbecomes inherently multimodal and user-centric [62,
189]. Mehri Shervedani et al. [189] integrate dialogue acts with multimodal signals to infer user
intent in collaborative tasks, while Fung et al. [ 62] emphasize continuous, first-person sensing
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 38

```text
38 Rupprecht et al.
Table 5. Epistemic world model works in this report mapped to Cognitive Architecture Theory (CAT) functions
and subtasks. In theSubtaskcolumn,T= Trust, Human-alignment, and Interpretability,C= Software Co-
pilots,M= Medical Research and Application, andS= Social Science. Composite labels indicate that a work
contributes to multiple Human–AI collaboration subtasks. A check ( ✓) indicates the work makes a clear
contribution to that CAT function in the context of collaboration.
Work Year Subtask
Mem.
Perc.
Lang.
Reas.
Imag.
Moti.
Meta.Description
Global Workspace: language, with human-in-the-loop
Gemini Co-
scientist [69, 70]
2025 T+C+M✓ ✓ ✓ ✓ ✓ ✓ multi-agent AI collaborator for hypothesis
generation and refinement
OpenAI Prism [155] 2026 T+C✓ ✓ ✓ ✓ ✓ ✓ LaTeX-native workspace for scientific writ-
ing and collaboration
SciSciGPT [180] 2025 T+C+S✓ ✓ ✓ ✓ ✓ ✓ agentic science-of-science analytics over lit-
erature and structured datasets
OmniScientist [179] 2025 T+C+S✓ ✓ ✓ ✓ ✓ ✓ human–AI scientist ecosystem with com-
munity evaluation (ScienceArena)
Mehri Shervedani et
al. [189]
2025 T+M+S✓ ✓ ✓ ✓ ✓ ✓ multimodal RL interaction manager for as-
sistive human–robot collaboration
CellAtria [153] 2026 M✓ ✓ ✓ ✓ ✓ ✓ Using AI for RNA sequencing and analysis
Gentile et al. [67] 2026 M✓ ✓ ✓ ✓ ✓ ✓ AI Transcriptomics with human-in-the-
loop for gene expression analysis
Global Workspace: language, without human-in-the-loop
Generative
Agents [157]
2023 T+S✓ ✓ ✓ ✓ ✓ LLM agents with memory, reflection, and
planning for social simulation
SpeechAgents [251] 2024 S✓ ✓ ✓ multi-agent spoken interaction controlled
by a speech-centric LLM
Kumar et al. [113] 2025 T+S✓ ✓ ✓ ✓ unified speech-to-speech model claims for
multilingual, emotional interaction
Kim et al. [110] 2025 S✓ ✓ ✓ ✓ multimodal conversational agent generat-
ing engaging speech from audio-visual cues
Reviews, Benchmarks, and Position Papers
Xie et al. [229] 2025 T+C+S✓ ✓ Roadmap on AI scientists emphasizing ver-
ification and falsification
Agentic Coding Man-
ifests [33]
2025 T+C✓ ✓ Empirical study of Claude Code’s repo man-
ifests that externalize project context and
rules for coding agents
Tsvetkova et al. [206] 2024 T+S✓ ✓ ✓ framework for sociology of mixed human–
machine communities
Strachan et al. [195] 2024 T+S✓ ✓ empirical theory-of-mind benchmark com-
paring LLMs and humans
Chen et al. [36] 2025 T+S✓ ✓ ✓ survey of consciousness/metacognition the-
ories, implementations, and risks in LLMs
Kwok et al. [114] 2026 T+S✓ ✓ ✓ ✓ explicit shared world models for reliable
human–robot collaboration
Fung et al. [62] 2025 M+S✓ ✓ ✓ ✓ ✓ position paper on embodied assistants with
memory, world models, and goal inference
in wearable or embodied assistants. These approaches enable proactive assistance but introduce
challenges in reliability, ambiguity resolution, and privacy, making perception a critical bottleneck
for safe deployment.
In social interaction,perceptionexpands to include communicative signals such as prosody,
emotion, and contextual cues [110, 113, 114, 251]. SpeechAgents [251] treat speech as a primary
interaction channel, preserving rhythm and affect rather than reducing communication to text.
Kim et al. [110] further condition interaction on audio-visual signals to improve engagement, while
Kwok et al. [114] highlight the importance of grounding ambiguous social cues in shared context for
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 39

```text
Human Cognition in Machines: A Unified Perspective of World Models 39
reliable collaboration. Other systems approximate perception through dialogue-history encodings
or structured observations (e.g., pose or environment state), trading richness for tractability.
Across domains, improvements in trust are less about increasing perceptual bandwidth and more
about structuring and grounding perceptual inputs. Systems that expose intermediate representa-
tions (e.g., retrieved evidence, structured documents, or shared context) makeperceptionmore
interpretable, whereas purely latent encodings of multimodal input remain difficult to audit. As a
result, effective co-pilots treat perception not as raw sensing, but as the construction of verifiable,
task-aligned state.
6.1.3Memory.Many co-pilots improve memory by externalizing long-horizon context into
persistent artifacts such as project state, corpora, or structured workspaces [33, 62, 110, 113, 155,
179, 180]. OpenAI Prism [155] treats the LaTeX project itself as working memory, enabling consistent
revision across documents, while OmniScientist [179] extends memory into a research ecosystem
via knowledge graphs and evolving “idea stacks. ” In contrast, Agentic Coding Manifests [33] provide
a lightweight approach, storing repository conventions and constraints as human-authored memory.
Across these systems, a central trade-off emerges between simple explicit memory (manifests),
structured external memory (graphs, databases), and conversational state.
In medical research settings, explicit long-termmemoryremains underdeveloped despite its
importance. Two works in particular however, provide novel world encoding strategies for their
RNA transcription setting [67, 153]. In both, using agentic reasoning for RNA sequence analysis
requires representing sequence annotations or researcher meta-data as written language. Also in
both works, they can utilize the sequence of RNA (itself semantically and symbolically salient)
as embeddings that LLMs can use to reason with the RNA-text-like representation itself. This
representation of RNA for a global workspace framework is observable in Figure 9.
Social and interactive systems place stronger demands onmemoryfor continuity and shared
understanding [62, 113, 114, 157, 189]. Generative Agents [157] exemplify this by storing episodic
experiences and synthesizing higher-level reflections that guide future behavior. Similarly, Kwok et
al. [114] and Mehri Shervedani et al. [189] model memory as shared state (common ground) that
must be continuously updated during interaction. In speech systems, longer-term personalization
is often approximated through dialogue history or user-specific embeddings [113], while embodied
assistants require episodic memory to sustain coherent assistance over time [62]. A key distinction
is between interpretable shared-memory representations (e.g., common ground) and implicit history
encodings that are harder to audit.
Across domains, improvements in trust are closely tied to makingmemoryexplicit, structured,
and inspectable [33, 69, 70, 114, 155, 157, 179, 189]. Generative Agents [157] provide a clear ex-
ample by exposing both raw episodic memories and derived reflections, enabling users to trace
behavior back to stored experience. Similarly, manifests [33] and shared-state representations [114]
externalize assumptions and context into artifacts that can be inspected and revised. Larger systems
such as Prism [155] and OmniScientist [179] extend this idea to document- and ecosystem-level
memory. Overall, the dominant pattern is a shift away from opaque latent state toward persistent
artifacts that users can inspect, version, and contest.
6.2 World Model Prediction and Generation
6.2.1Imagination.Co-pilots employ imagination to generate candidate hypotheses, plans, or
expressive outputs that a human or downstream process can select, refine, or test [69, 70, 110, 179,
189, 251]. In scientific collaboration, Gemini Co-scientist [69, 70] produces research hypotheses and
experimental proposals, while OmniScientist [179] treats ideation as a first-class module, evolving
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 40

```text
40 Rupprecht et al.
candidate ideas within a structured knowledge graph. In these settings, imagination functions as
controlled hypothesis expansion rather than unconstrained generation.
In medical and scientific domains,imaginationmost directly appears as hypothesis generation
under experimental constraints [69, 70]. Systems such as Gemini Co-scientist propose candidate
mechanisms, repurposing strategies subsequently filtered by feasibility and empirical validation,
reflecting a generate-then-triage workflow aligned with the scientific method.
In interactive and social systems,imaginationoften takes the form of one-to-many generation.
For example, Kim et al. [110] generate expressive paralinguistic speech, while Mehri Shervedani
et al. [ 189] employ simulated rollouts via user models to support policy learning. Generative
Agents [157] extend this paradigm to multi-agent settings, where imagined actions at the individual
level produce emergent group behaviors over time. Across these domains, imagination supports
diverse objectives, including expressive communication, social simulation, and action planning.
Imaginationis not used in isolation. Its utility depends on coupling downstream selection
mechanisms, such as ranking, constraint satisfaction, or evaluation. In practice, trust is not derived
from the generative step itself, but from the processes that filter, verify, and prioritize candidates.
6.2.2Reasoning.Reasoning in world models and co-pilots is typically framed as multi-step
problem solving under constraints, and mediated by tool use, workflows, or multi-agent protocols
[33, 62, 69, 70, 113, 155, 179, 180, 189, 229]. Systems span a spectrum from structured, tool-grounded
reasoning to deliberative, multi-agent reasoning. OpenAI Prism [155] constrains reasoning over
structured artifacts (e.g., LaTeX projects), while SciSciGPT [180] operationalizes reasoning as an
end-to-end empirical pipeline (decomposition, retrieval, computation, and visualization). In contrast,
Gemini Co-scientist [69, 70] and OmniScientist [179] deliberates through multi-agent protocols such
as debate, reflection, and workflow orchestration. At the policy level, Gemini Co-scientist [69, 70]
use agents to recognize novel research trajectories by debating hypotheses, ranking ideas with an
Elo-style system, filtering out redundant ideas, while Mehri Shervedani et al. [189] frame reasoning
as action selection under uncertainty, learning dialogue and intervention policies for assistive tasks.
In medical and assistive settings,reasoningbifurcates intoscientific reasoninganddecision-
making under uncertainty. Gemini Co-scientist [ 69, 70] focuses on evidence-backed hypothesis
generation and refinement via multi-agent deliberation, while Mehri Shervedani et al. [189] optimize
real-time interaction policies for successful task completion. This contrast highlights reasoning as
either hypothesis validation or policy optimization. In RNA transcription medical research, models
reason from representations of RNA to profile genetic sequences for personalized medicine [67, 153].
In social and collaborative contexts,reasoningextends beyond individual cognition to include
theory-of-mind inference, experimental methodology, and system-level dynamics [36, 62, 114, 157,
180, 189, 195, 206, 229]. SciSciGPT [180] exemplifies reasoning as transparent scientific workflows,
while Kwok et al. [114] emphasize explicit shared models for reasoning about human goals. Strachan
et al. [ 195] evaluates theory-of-mind capabilities, exposing systematic failure modes in social
reasoning tasks. At a broader scale, Tsvetkova et al. [206] model mixed human–machine systems
as dynamical processes, and Xie et al. [ 229] identifies verification and falsification as central
bottlenecks for scalable scientific reasoning. Together, these works position reasoning as both an
individual capability and an emergent property of socio-technical systems.
Across these domains,reasoningis tightly coupled to trust through auditability and verification
[36, 69, 70, 113, 114, 155, 179, 180, 189, 195, 206, 229]. Multi-agent deliberation surfaces alternatives
and justifications (e.g., Gemini Co-scientist), while procedural pipelines enable reproducibility and
inspection (e.g., SciSciGPT). Evaluation frameworks, such as those by Strachan et al. [ 195], test
whether reasoning capabilities generalize across conditions. More broadly, Xie et al. [229] argues
that trustworthiness requires explicit verification loops, and Tsvetkova et al. [206] situates trust
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 41

```text
Human Cognition in Machines: A Unified Perspective of World Models 41
within ecosystem-level dynamics. Reasoning in current systems spans deliberative (multi-agent
critique), procedural (tool-grounded workflows), and evaluative (verification and benchmarking)
paradigms, which together form the basis for reliable and interpretable decision-making.
6.2.3Motivation.Motivation remains underdeveloped in epistemic world models, with most
works relying on externally specified objectives rather than intrinsic drives. Existing work primarily
operationalizes motivation through rewards, goals, or intent inference [62, 179, 189, 206, 229].
A key distinction emerges betweenoptimization-drivenandinference-drivenmotivation. In RL
settings, motivation is encoded implicitly as an optimization signal via reward shaping and penalties,
as in assistive human–robot interaction systems that incentivize efficient and valid behavior [189].
In contrast, embodied assistants increasingly model motivation as the inference of user goals or
intent, enabling proactive assistance without explicit commands [62]. This reframes motivation as
alignment to latent human objectives rather than adherence to predefined reward functions.
As discussed in Sec. 3.3, in practice, motivation is predominantlyextrinsicand often safety-
or task-driven, particularly in medical and assistive domains [ 62, 189]. Systems are designed
to optimize externally defined criteria such as correctness, efficiency, or user satisfaction, with
little evidence of intrinsic or self-directed objective formation. At a broader scale, motivation is
shaped by the surrounding socio-technical system. Incentives, credit assignment, and selection
pressures govern agent behavior in collaborative and scientific settings [179, 206, 229]. Tsvetkova
et al. [206] demonstrate how incentive structures drive emergent phenomena such as cascades and
manipulation, while OmniScientist [179] embeds motivation in mechanisms such as attribution
and peer review to regulate collaboration quality. Xie et al. [229] further argues that automation
reshapes which problems are pursued, effectively altering the motivational landscape of the research
ecosystem. Motivation in current world models is not intrinsic but arises from externally imposed
objectives, highlighting a key gap between machine systems and human-like cognition.
6.2.4Metacognition.Metacognition is introduced as a reliability scaffold in epistemic world
models, through self-reflection, self-evaluation, uncertainty management, and error checking
[33, 36, 69, 70, 155, 157, 179, 180, 206, 229]. Many designs separate generation from judgment,
forming propose–evaluate loops. OpenAI Prism [ 155] introduces an always-on reviewer layer
for proofreading and consistency checking, while Gemini Co-scientist [ 69, 70] and OmniScien-
tist [179] operationalize critique through dedicated self-reflection roles and ranking mechanisms.
SciSciGPT [180] further emphasizes reproducibility and output validation within empirical pipelines.
Metacognitive mechanisms operate at two levels. At theindividual level, systems employ inter-
nal self-reflection to refine outputs or update beliefs, as seen in Generative Agents [157], where
reflection transforms experience into higher-level behavioral. At thesystem or community level,
metacognition is externalized through evaluation platforms, auditability, and feedback loops, en-
abling reproducibility and collective validation [179, 180]. This distinction highlights a key design
axis: internal self-reflection, self-evaluation, and self-control versus external governance.
These safeguards are particularly critical in high-stakes settings, where unchecked generation
can propagate errors or overconfident hypotheses. For instance, Gemini Co-scientist [69, 70] uses
critique and reflection loops to down-select hypotheses prior to wet-lab validation, reducing exper-
imental cost and risk. More broadly, Chen et al. [36] and Xie et al. [229] argue that without explicit
self-evaluation and external oversight, iterative self-improvement can amplify errors. Overall,
effective metacognition in world models emerges from coupling strong generative capabilities with
explicit, testable judgment layers, often combining internal self-reflection, self-evaluation, and
self-control with external evaluation and governance.
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 42

```text
42 Rupprecht et al.
6.3 Trends and Limitations
Epistemic world models are emerging as a shift from implicit latent-state modeling toward explicit,
externalized knowledge-state modeling. Rather than compressing observations into an opaque
latent state, these systems maintain the “world” as a shared epistemiclanguage-based global
workspace consisting of literature, code, documents, tool outputs, retrieved evidence, hypotheses,
experimental data, and human feedback. This makes scientific discovery more interpretable than in
many video or embodied world models. A recurring trend is therefore the use of global workspaces in
which agents coordinate tool use, propose hypotheses, revise artifacts, and expose partial reasoning
to humans [33, 69, 70, 155, 179, 180]. In this sense, epistemic world models provide one of the
clearest current pathways toward metacognitive scaffolding: generation is separated from judgment
through reviewer agents, critique loops, debate, ranking, execution traces, and human oversight.
However, these systems remain limited in ways that are easy to obscure behind fluent language
and multi-agent workflows. First, their epistemic state transitions are rarely formalized as clearly as
latent world models; the state is often distributed across prompts, documents, databases, retrieved
passages, logs, and human edits, making reproducibility and causal attribution difficult. Second,
motivation remains mostly extrinsic, inherited from user instructions, benchmarks, reward func-
tions, institutional incentives, or peer-review mechanisms rather than intrinsic objective formation.
Third, metacognition is still scaffolded rather than autonomous: self-evaluation usually depends on
additional agents, external tools, or human validators that may share the same blind spots as the
generator. As a result, the central challenge for epistemic world models is not merely adding more
agents, but developing reliable mechanisms for provenance tracking, uncertainty-aware verification,
and accountable human–AI governance over the evolving knowledge state [36, 206, 229].
7 Conclusion
We identify in video, embodied, and newly named epistemic world model literature trends for
overcoming common problems with common solutions. We are the first to propose a taxonomy
of recent world models rooted in cognitive architecture theory. Our taxonomy reveals a research
gap regarding the cognitive functions of motivation (especially intrinsic), and metacognition that
may not have been identified otherwise. Additionally, our taxonomy inspires us to rethink agent
frameworks for scientific discovery as epistemic world models with strong metacognitive capabili-
ties from language-based Global Workspaces. Adding a human in the loop to promptable video,
embodied and epistemic world models, for them to lend their own motivation and metacognitive
ability, remains one of the clearest observances of human cognition in machines.
In answer to what ahuman-like world model would look like, we propose a unified world
model framework that holistically incorporates all of the component parts of cognition: memory,
perception, language, reasoning, imagining, motivation, and metacognition. This framework acts as
a conceptual roadmap for researchers. Unified world models encourage researchers to 1) use multi-
modal inputs, 2) encode multi-scalar spatio-temporal representations, 3) include tokenized language
as an input, intermediate reasoning space, or output to enable human-in-the-loop cooperation, 4)
utilize sim-to-real training when data is scarce and hypothetical reasoning at inference, 5) reason
with domain-specific state-of-the-art architectures, 6) provide intrinsic reward signals to world
models and lastly 7) utilize a global workspace enabling self-reflection, self-evaluation, and self-
control. Our report provides researchers a vocabulary to debate the merits of equating human and
machine cognition. Our review shows that to begin to fully equate machine and human cognition
in function, let alone in any philosophical level, requires a world model that holistically emulates
all component parts of cognition, including the under-researched cognitive functions of motivation,
and metacognition.
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 43

```text
Human Cognition in Machines: A Unified Perspective of World Models 43
References
[1] 2026. Being-H0.7: A Latent World-Action Model from Egocentric Videos.preprint(2026). https://research.beingbeyond.
com/projects/being-h07/being-h07.pdf
[2] Niket Agarwal, Arslan Ali, Maciej Bala, Yogesh Balaji, Erik Barker, Tiffany Cai, Prithvijit Chattopadhyay, Yongxin
Chen, Yin Cui, Yifan Ding, et al . 2025. Cosmos world foundation model platform for physical ai.arXiv preprint
arXiv:2501.03575(2025).
[3] Arman Akbari, Ci Zhang, Arash Akbari, Lin Zhao, Yixiao Chen, Weiwei Chen, Xuan Zhang, Geng Yuan, and Yanzhi
Wang. 2026. Flash-WAM: Modality-Aware Distillation for World Action Models.arXiv preprint arXiv:2606.05254
(2026).
[4] Arslan Ali, Junjie Bai, Maciej Bala, Yogesh Balaji, Aaron Blakeman, Tiffany Cai, Jiaxin Cao, Tianshi Cao, Elizabeth
Cha, Yu-Wei Chao, et al. 2025. World simulation with video foundation models for physical ai.arXiv preprint
arXiv:2511.00062(2025).
[5] Eloi Alonso, Adam Jelley, Vincent Micheli, Anssi Kanervisto, Amos Storkey, Tim Pearce, and François Fleuret. 2024.
Diffusion for world modeling: Visual details matter in atari.Advances in Neural Information Processing Systems37
(2024), 58757–58791.
[6] Dario Amodei, Chris Olah, Jacob Steinhardt, Paul Christiano, John Schulman, and Dan Mané. 2016. Concrete problems
in AI safety.arXiv preprint arXiv:1606.06565(2016).
[7] John R Anderson, Michael Matessa, and Christian Lebiere. 1997. ACT-R: A theory of higher level cognition and its
relation to visual attention.Human–Computer Interaction12, 4 (1997), 439–462.
[8] Kaleem Arshid, Ali Krayani, Lucio Marcenaro, David Martin Gomez, and Carlo Regazzoni. 2025. Toward autonomous
UAV swarm navigation: a review of trajectory design paradigms.Sensors (Basel, Switzerland)25, 18 (2025), 5877.
[9] Mido Assran, Adrien Bardes, David Fan, Quentin Garrido, Russell Howes, Matthew Muckley, Ammar Rizvi, Claire
Roberts, Koustuv Sinha, Artem Zholus, et al. 2025. V-jepa 2: Self-supervised video models enable understanding,
prediction and planning.arXiv preprint arXiv:2506.09985(2025).
[10] Mahmoud Assran, Quentin Duval, Ishan Misra, Piotr Bojanowski, Pascal Vincent, Michael Rabbat, Yann LeCun,
and Nicolas Ballas. 2023. Self-supervised learning from images with a joint-embedding predictive architecture. In
Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 15619–15629.
[11] Bernard J Baars. 1993.A cognitive theory of consciousness. Cambridge University Press.
[12] Anurag Bagchi, Zhipeng Bao, Homanga Bharadhwaj, Yu-Xiong Wang, Pavel Tokmakov, and Martial Hebert. 2026.
Walk through Paintings: Egocentric World Models from Internet Priors.arXiv preprint arXiv:2601.15284(2026).
[13] Leonardo Barcellona, Andrii Zadaianchuk, Davide Allegro, Samuele Papa, Stefano Ghidoni, and Efstratios Gavves.
2025. Dream to manipulate: Compositional world models empowering robot imitation learning with imagination. In
International Conference on Learning Representations, Vol. 2025. 56729–56763.
[14] Adrien Bardes, Quentin Garrido, Jean Ponce, Xinlei Chen, Michael Rabbat, Yann LeCun, Mido Assran, and Nicolas
Ballas. 2023. V-jepa: Latent video prediction for visual representation learning. (2023).
[15] Adrien Bardes, Quentin Garrido, Jean Ponce, Xinlei Chen, Michael Rabbat, Yann LeCun, Mahmoud Assran, and
Nicolas Ballas. 2024. Revisiting feature prediction for learning visual representations from video.arXiv preprint
arXiv:2404.08471(2024).
[16] Glen Berseth, Daniel Geng, Coline Devin, Nicholas Rhinehart, Chelsea Finn, Dinesh Jayaraman, and Sergey Levine.
2019. Smirl: Surprise minimizing reinforcement learning in unstable environments.arXiv preprint arXiv:1912.05510
(2019).
[17] Ayush Bheemaiah and Seungyong Yang. 2025. Knowledge Graphs as World Models for Semantic Material-Aware
Obstacle Handling in Autonomous Vehicles.arXiv preprint arXiv:2503.21232(2025).
[18] Hongzhe Bi, Hengkai Tan, Shenghao Xie, Zeyuan Wang, Shuhe Huang, Haitian Liu, Ruowen Zhao, Yao Feng, Chendong
Xiang, Yinze Rong, et al. 2026. Motus: A unified latent action world model. InProceedings of the IEEE/CVF Conference
on Computer Vision and Pattern Recognition. 35101–35113.
[19] Ahsan Bilal, Muhammad Ahmed Mohsin, Muhammad Umer, Muhammad Awais Khan Bangash, and Muhammad Ali
Jamshed. 2025. Meta-thinking in llms via multi-agent reinforcement learning: A survey.arXiv preprint arXiv:2504.14520
(2025).
[20] Kevin Black, Mitsuhiko Nakamoto, Pranav Atreya, Homer Walke, Chelsea Finn, Aviral Kumar, and Sergey Levine.
2024. Zero-shot robotic manipulation with pre-trained image-editing diffusion models. InInternational Conference on
Learning Representations, Vol. 2024. 33431–33452.
[21] Rafal Bogacz. 2017. A tutorial on the free-energy framework for modelling perception and learning.Journal of
mathematical psychology76 (2017), 198–211.
[22] James Boggs. 2025. Towards visual-symbolic integration in the Soar cognitive architecture.Cognitive Systems Research
91 (2025), 101353.
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 44

```text
44 Rupprecht et al.
[23] Carlo Bosio, Greg Woelki, Noureldin Hendy, Nicholas Roy, and Byungsoo Kim. 2025. RDAR: Reward-Driven Agent
Relevance Estimation for Autonomous Driving.arXiv preprint arXiv:2509.19789(2025).
[24] Thomas Brandt, Marianne Dieterich, and Doreen Huppert. 2024. Human senses and sensors from Aristotle to the
present.Frontiers in Neurology15 (2024), 1404720.
[25] Jake Bruce, Michael D Dennis, Ashley Edwards, Jack Parker-Holder, Yuge Shi, Edward Hughes, Matthew Lai, Aditi
Mavalankar, Richie Steigerwald, Chris Apps, et al. 2024. Genie: Generative interactive environments. InForty-first
International Conference on Machine Learning.
[26] Arthur Earl Bryson. 2018.Applied optimal control: optimization, estimation and control. Routledge.
[27] Karl Bühler. 1934.Sprachtheorie. Vol. 2. Jena Fischer.
[28] Maxime Burchi and Radu Timofte. 2025. Accurate and efficient world modeling with masked latent transformers.
arXiv preprint arXiv:2507.04075(2025).
[29] Meng Cao, Haoran Tang, Haoze Zhao, Mingfei Han, Ruyang Liu, Qiang Sun, Xiaojun Chang, Ian Reid, and Xiaodan
Liang. 2026. Order from Chaos: Physical World Understanding from Glitchy Gameplay Videos.arXiv preprint
arXiv:2601.16471(2026).
[30] Jun Cen, Chaohui Yu, Hangjie Yuan, Yuming Jiang, Siteng Huang, Jiayan Guo, Xin Li, Yibing Song, Hao Luo, Fan
Wang, et al. 2025. Worldvla: Towards autoregressive action world model.arXiv preprint arXiv:2506.21539(2025).
[31] Huiwen Chang, Han Zhang, Lu Jiang, Ce Liu, and William T Freeman. 2022. Maskgit: Masked generative image
transformer. InProceedings of the IEEE/CVF conference on computer vision and pattern recognition. 11315–11325.
[32] Jonathan Chang, Masatoshi Uehara, Dhruv Sreenivas, Rahul Kidambi, and Wen Sun. 2021. Mitigating covariate shift
in imitation learning via offline data with partial coverage.Advances in Neural Information Processing Systems34
(2021), 965–979.
[33] Worawalan Chatlatanagulchai, Kundjanasith Thonglek, Brittany Reid, Yutaro Kashiwa, Pattara Leelaprute, Arnon
Rungsawang, Bundit Manaskasemsak, and Hajimu Iida. 2025. On the use of agentic coding manifests: An empirical
study of claude code. InInternational Conference on Product-Focused Software Process Improvement. Springer, 543–551.
[34] Chi-Lam Cheang, Guangzeng Chen, Ya Jing, Tao Kong, Hang Li, Yifeng Li, Yuxiao Liu, Hongtao Wu, Jiafeng Xu, Yichu
Yang, et al. 2024. Gr-2: A generative video-language-action model with web-scale knowledge for robot manipulation.
arXiv preprint arXiv:2410.06158(2024).
[35] Boyuan Chen, Tianyuan Zhang, Haoran Geng, Kiwhan Song, Caiyi Zhang, Peihao Li, William T Freeman, Jitendra
Malik, Pieter Abbeel, Russ Tedrake, et al. 2025. Large video planner enables generalizable robot control.arXiv preprint
arXiv:2512.15840(2025).
[36] Sirui Chen, Shuqin Ma, Shu Yu, Hanwang Zhang, Shengjie Zhao, and Chaochao Lu. 2025. Exploring Consciousness
in LLMs: A Systematic Survey of Theories, Implementations, and Frontier Risks. arXiv:2505.19806 [cs.CL] https:
//arxiv.org/abs/2505.19806
[37] Yuntao Chen, Yuqi Wang, and Zhaoxiang Zhang. 2025. Drivinggpt: Unifying driving world modeling and planning
with multi-modal autoregressive transformers. InProceedings of the IEEE/CVF International Conference on Computer
Vision. 26890–26900.
[38] Clara Colombatto and Stephen M Fleming. 2024. Folk psychological attributions of consciousness to large language
models.Neuroscience of Consciousness2024, 1 (2024), niae013.
[39] Ciem Cornelissen, Sam Leroux, and Pieter Simoens. 2026. Le MuMo JEPA: Multi-Modal Self-Supervised Representation
Learning with Learnable Fusion Tokens. InProceedings of the IEEE/CVF Conference on Computer Vision and Pattern
Recognition. 8238–8247.
[40] Fergus IM Craik and Robert S Lockhart. 1972. Levels of processing: A framework for memory research.Journal of
verbal learning and verbal behavior11, 6 (1972), 671–684.
[41] Kenneth JW Craik. 1947. Theory of the human operator in control systems 1: I. The operator as an engineering
system.British Journal of Psychology. General Section38, 2 (1947), 56–61.
[42] Kenneth JW Craik. 1948. Theory of the human operator in control systems. II. Man as an element in a control system.
British journal of psychology38, 3 (1948), 142.
[43] Kenneth James Williams Craik. 1967.The nature of explanation. Vol. 445. CUP Archive.
[44] Chenxu Dang, Haiyan Liu, Jason Bao, Pei An, Xinyue Tang, An Pan, Jie Ma, Bingchuan Sun, and Yan Wang. 2026.
Sparseworld: A flexible, adaptive, and efficient 4d occupancy world model powered by sparse and dynamic queries. In
Proceedings of the AAAI Conference on Artificial Intelligence, Vol. 40. 3497–3505.
[45] Charles Darwin. 1872.The descent of man, and selection in relation to sex. Vol. 2. D. Appleton.
[46] Kristopher De Asis, J Hernandez-Garcia, G Holland, and Richard Sutton. 2018. Multi-step reinforcement learning: A
unifying algorithm. InProceedings of the AAAI conference on artificial intelligence, Vol. 32.
[47] Terrence W Deacon. 1998.The symbolic species: The co-evolution of language and the brain. WW Norton & Company.
[48] Vittoria Dentella, Fritz Günther, Elliot Murphy, Gary Marcus, and Evelina Leivada. 2024. Testing AI on language
comprehension tasks reveals insensitivity to underlying meaning.Scientific Reports14, 1 (2024), 28083.
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 45

```text
Human Cognition in Machines: A Unified Perspective of World Models 45
[49] Matthieu Destrade, Oumayma Bounou, Quentin Le Lidec, Jean Ponce, and Yann LeCun. 2025. Value-guided action
planning with JEPA world models.arXiv preprint arXiv:2601.00844(2025).
[50] Karthik Dharmarajan, Wenlong Huang, Jiajun Wu, Li Fei-Fei, and Ruohan Zhang. 2025. Dream2Flow: Bridging Video
Generation and Open-World Manipulation with 3D Object Flow.arXiv preprint arXiv:2512.24766(2025).
[51] Jingtao Ding, Yunke Zhang, Yu Shang, Yuheng Zhang, Zefang Zong, Jie Feng, Yuan Yuan, Hongyuan Su, Nian Li,
Nicholas Sukiennik, et al. 2025. Understanding world or predicting future? a comprehensive survey of world models.
Comput. Surveys58, 3 (2025), 1–38.
[52] Adrien Doerig, Tim C Kietzmann, Emily Allen, Yihan Wu, Thomas Naselaris, Kendrick Kay, and Ian Charest. 2025.
High-level visual representations in the human brain are aligned with large language models.Nature Machine
Intelligence(2025), 1–15.
[53] Merlin Donald. 1993.Origins of the modern mind: Three stages in the evolution of culture and cognition. Harvard
university press.
[54] Jiahua Dong, Qi Lyu, Baichen Liu, Xudong Wang, Wenqi Liang, Duzhen Zhang, Jiahang Tu, Hongliu Li, Hanbin
Zhao, Henghui Ding, et al. 2026. Learning to Model the World: A Survey of World Models in Artificial Intelligence.
Authorea Preprints(2026).
[55] Yilun Du, Sherry Yang, Bo Dai, Hanjun Dai, Ofir Nachum, Josh Tenenbaum, Dale Schuurmans, and Pieter Abbeel.
2023. Learning universal policies via text-guided video generation.Advances in neural information processing systems
36 (2023), 9156–9172.
[56] Viet Dung Nguyen, Zhizhuo Yang, Christopher L Buckley, and Alexander Ororbia. 2024. R-AIF: Solving Sparse-Reward
Robotic Tasks from Pixels with Active Inference and World Models.arXiv e-prints(2024), arXiv–2409.
[57] Zane Durante, Silky Singh, Arpandeep Khatua, Shobhit Agarwal, Reuben Tan, Yong Jae Lee, Jianfeng Gao, Ehsan
Adeli, and Li Fei-Fei. 2026. VideoWeave: A Data-Centric Approach for Efficient Video Understanding.arXiv preprint
arXiv:2601.06309(2026).
[58] Mohammad K Ebrahimpour, Jiayun Li, Yen-Yun Yu, Jackson Reesee, Azadeh Moghtaderi, Ming-Hsuan Yang, and
David C Noelle. 2019. Ventral-dorsal neural networks: object detection via selective attention. In2019 IEEE Winter
Conference on Applications of Computer Vision (W ACV). IEEE, 986–994.
[59] Karl Friston. 2010. The free-energy principle: a unified brain theory?Nature reviews neuroscience11, 2 (2010), 127–138.
[60] Karl Friston, Lancelot Da Costa, Alexander Tschantz, Conor Heins, Christopher Buckley, Tim Verbelen, and Thomas
Parr. 2025. Active inference and artificial reasoning.arXiv preprint arXiv:2512.21129(2025).
[61] Karl Friston, Thomas FitzGerald, Francesco Rigoli, Philipp Schwartenbeck, Giovanni Pezzulo, et al . 2016. Active
inference and learning.Neuroscience & Biobehavioral Reviews68 (2016), 862–879.
[62] Pascale Fung, Yoram Bachrach, Asli Celikyilmaz, Kamalika Chaudhuri, Delong Chen, Willy Chung, Emmanuel
Dupoux, Hongyu Gong, et al. 2025. Embodied AI Agents: Modeling the World. arXiv:2506.22355
[63] Shenyuan Gao, Siyuan Zhou, Yilun Du, Jun Zhang, and Chuang Gan. 2025. Adaworld: Learning adaptable world
models with latent actions.arXiv preprint arXiv:2503.18938(2025).
[64] Yinfeng Gao, Qichao Zhang, Da-Wei Ding, and Dongbin Zhao. 2024. Dream to drive with predictive individual world
model.IEEE Transactions on Intelligent Vehicles(2024).
[65] Quentin Garrido, Tushar Nagarajan, Basile Terver, Nicolas Ballas, Yann LeCun, and Michael Rabbat. 2026. Learning
Latent Action World Models In The Wild.arXiv preprint arXiv:2601.05230(2026).
[66] Zhiqi Ge, Hongzhe Huang, Mingze Zhou, Juncheng Li, Guoming Wang, Siliang Tang, and Yueting Zhuang. 2024.
Worldgpt: Empowering llm as multimodal world model. InProceedings of the 32nd ACM International Conference on
Multimedia. 7346–7355.
[67] Giulia Gentile, Giovanna Morello, Valentina La Cognata, Maria Guarnaccia, and Sebastiano Cavallaro. 2026. Artificial
Intelligence in Transcriptomics: From Human-in-the-Loop to Agentic AI.Journal of Personalized Medicine16, 4 (2026),
181.
[68] Mitchell Goff, Greg Hogan, George Hotz, Armand du Parc Locmaria, Kacper Raczy, Harald Schäfer, Adeeb Shihadeh,
Weixing Zhang, and Yassine Yousfi. 2025. Learning to drive from a world model. InProceedings of the Computer Vision
and Pattern Recognition Conference. 1964–1973.
[69] Juraj Gottweis, Wei-Hung Weng, Alexander Daryin, Tao Tu, Anil Palepu, Petar Sirkovic, Artiom Myaskovsky, Felix
Weissenberger, Keran Rong, Ryutaro Tanno, et al. 2025. Towards an AI co-scientist.arXiv preprint arXiv:2502.18864
(2025).
[70] Juraj Gottweis, Wei-Hung Weng, Alexander Daryin, Tao Tu, Petar Sirkovic, Artiom Myaskovsky, Grzegorz Glowaty,
Felix Weissenberger, Alessio Orlandi, Dan Popovici, et al. 2026. Accelerating scientific discovery with Co-Scientist.
Nature(2026), 1–3.
[71] Rick Grush. 2004. The emulation theory of representation: Motor control, imagery, and perception.Behavioral and
brain sciences27, 3 (2004), 377–396.
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 46

```text
46 Rupprecht et al.
[72] Yu Gu, Kai Zhang, Yuting Ning, Boyuan Zheng, Boyu Gou, Tianci Xue, Cheng Chang, Sanjari Srivastava, Yanan Xie,
Peng Qi, et al. 2024. Is your llm secretly a world model of the internet? model-based planning for web agents.arXiv
preprint arXiv:2411.06559(2024).
[73] Christian Gumbsch, Noor Sajid, Georg Martius, and Martin V Butz. 2023. Learning hierarchical world models with
adaptive temporal abstractions from discrete latent dynamics. InThe Twelfth International Conference on Learning
Representations.
[74] Jun Guo, Xiaojian Ma, Yikai Wang, Min Yang, Huaping Liu, and Qing Li. 2026. Flowdreamer: A rgb-d world model
with flow-based motion representations for robot manipulation.IEEE Robotics and Automation Letters11, 3 (2026),
2466–2473.
[75] David Ha and Jürgen Schmidhuber. 2018. World models.arXiv preprint arXiv:1803.101222, 3 (2018).
[76] Yoav HaCohen, Nisan Chiprut, Benny Brazowski, Daniel Shalem, Dudu Moshe, Eitan Richardson, Eran Levin, Guy
Shiran, Nir Zabari, Ori Gordon, et al. 2024. Ltx-video: Realtime video latent diffusion.arXiv preprint arXiv:2501.00103
(2024).
[77] Dylan Hadfield-Menell, Anca D Dragan, Pieter Abbeel, and Stuart Russell. 2017. The off-switch game.. InAAAI
Workshops.
[78] Danijar Hafner, Timothy Lillicrap, Jimmy Ba, and Mohammad Norouzi. 2019. Dream to control: Learning behaviors
by latent imagination.arXiv preprint arXiv:1912.01603(2019).
[79] Nick Hansen, Hao Su, and Xiaolong Wang. 2024. Td-mpc2: Scalable, robust world models for continuous control. In
International Conference on Learning Representations, Vol. 2024. 47376–47405.
[80] Nick Hansen, Jyothir SV, Vlad Sobal, Yann LeCun, Xiaolong Wang, and Hao Su. 2025. Hierarchical world models as
visual whole-body humanoid controllers. InInternational Conference on Learning Representations, Vol. 2025. 62175–
62195.
[81] Chenjie Hao, Weyl Lu, Yifan Xu, and Yubei Chen. 2025. Neural motion simulator pushing the limit of world models
in reinforcement learning. InProceedings of the Computer Vision and Pattern Recognition Conference. 27608–27617.
[82] Jonathan Ho, Ajay Jain, and Pieter Abbeel. 2020. Denoising diffusion probabilistic models.Advances in neural
information processing systems33 (2020), 6840–6851.
[83] James Hollan, Edwin Hutchins, and David Kirsh. 2000. Distributed cognition: toward a new foundation for human-
computer interaction research.ACM Transactions on Computer-Human Interaction (TOCHI)7, 2 (2000), 174–196.
[84] Bohan Hou, Gen Li, Jindou Jia, Tuo An, Xinying Guo, Sicong Leng, Haoran Geng, Yanjie Ze, Tatsuya Harada, Philip
Torr, et al. 2026. World Model for Robot Learning: A Comprehensive Survey.arXiv preprint arXiv:2605.00080(2026).
[85] Anthony Hu, Lloyd Russell, Hudson Yeo, Zak Murez, George Fedoseev, Alex Kendall, Jamie Shotton, and Gianluca
Corrado. 2023. Gaia-1: A generative world model for autonomous driving.arXiv preprint arXiv:2309.17080(2023).
[86] Yutong Hu, Jan-Nico Zaech, Nikolay Nikolov, Yuanqi Yao, Sombit Dey, Giuliano Albanese, Renaud Detry, Luc Van Gool,
and Danda Paudel. 2026. AR-VLA: True Autoregressive Action Expert for Vision-Language-Action Models.arXiv
preprint arXiv:2603.10126(2026).
[87] Siqiao Huang. 2025. Awesome-World-Models. https://github.com/knightnemo/Awesome-World-Models. GitHub
repository, accessed 2026-05-26.
[88] Siyuan Huang, Liliang Chen, Pengfei Zhou, Shengcong Chen, Yue Liao, Zhengkai Jiang, Yue Hu, Peng Gao, Hongsheng
Li, Maoqing Yao, et al. 2026. Enerverse: Envisioning embodied future space for robotics manipulation.Advances in
Neural Information Processing Systems38 (2026), 37693–37720.
[89] Suning Huang, Qianzhong Chen, Xiaohan Zhang, Jiankai Sun, and Mac Schwager. 2025. Particleformer: A 3d point
cloud world model for multi-object, multi-material robotic manipulation.arXiv preprint arXiv:2506.23126(2025).
[90] Wenlong Huang, Yu-Wei Chao, Arsalan Mousavian, Ming-Yu Liu, Dieter Fox, Kaichun Mo, and Li Fei-Fei. 2026.
PointWorld: Scaling 3D World Models for In-The-Wild Robotic Manipulation.arXiv preprint arXiv:2601.03782(2026).
[91] Weidong Huang, Jiaming Ji, Chunhe Xia, Borong Zhang, and Yaodong Yang. 2024. Safedreamer: Safe reinforcement
learning with world models. InInternational Conference on Learning Representations, Vol. 2024. 53839–53869.
[92] Xun Huang, Zhengqi Li, Guande He, Mingyuan Zhou, and Eli Shechtman. 2025. Self Forcing: Bridging the Train-Test
Gap in Autoregressive Video Diffusion. arXiv:2506.08009 [cs.CV] https://arxiv.org/abs/2506.08009
[93] Yuhang Huang, Jiazhao Zhang, Shilong Zou, Xinwang Liu, Ruizhen Hu, and Kai Xu. 2025. LaDi-WM: A Latent
Diffusion-based World Model for Predictive Manipulation.arXiv preprint arXiv:2505.11528(2025).
[94] Minyoung Huh, Brian Cheung, Tongzhou Wang, and Phillip Isola. 2024. The platonic representation hypothesis.
arXiv preprint arXiv:2405.07987(2024).
[95] Lujain Ibrahim and Myra Cheng. 2025. Thinking beyond the anthropomorphic paradigm benefits LLM research.
arXiv preprint arXiv:2502.09192(2025).
[96] Physical Intelligence, Kevin Black, Noah Brown, James Darpinian, Karan Dhabalia, Danny Driess, Adnan Esmail,
Michael Equi, Chelsea Finn, Niccolo Fusai, Manuel Y. Galliker, et al. 2025. 𝜋0.5: a Vision-Language-Action Model with
Open-World Generalization. arXiv:2504.16054
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 47

```text
Human Cognition in Machines: A Unified Perspective of World Models 47
[97] Joel Jang, Seonghyeon Ye, Zongyu Lin, Jiannan Xiang, Johan Bjorck, Yu Fang, Fengyuan Hu, Spencer Huang, Kaushil
Kundalia, Yen-Chen Lin, et al. 2025. Dreamgen: Unlocking generalization in robot learning through video world
models.arXiv preprint arXiv:2505.12705(2025).
[98] Jinwoo Jang, Minjong Yoo, Sihyung Yoon, and Honguk Woo. 2026. Test-Time Mixture of World Models for Embodied
Agents in Dynamic Environments.arXiv preprint arXiv:2601.22647(2026).
[99] Sangwon Jang, Taekyung Ki, Jaehyeong Jo, Saining Xie, Jaehong Yoon, and Sung Ju Hwang. 2026. Self-Refining Video
Sampling.arXiv preprint arXiv:2601.18577(2026).
[100] Julian Jaynes. 2013. from The Origin of Consciousness in the Breakdown of the Bicameral Mind. InCreative Writing.
Routledge, 541–543.
[101] Anqing Jiang, Yu Gao, Yiru Wang, Zhigang Sun, Shuo Wang, Yuwen Heng, Hao Sun, Shichen Tang, Lijuan Zhu,
Jinhao Chai, et al. 2025. Irl-vla: Training an vision-language-action policy via reward world model.arXiv preprint
arXiv:2508.06571(2025).
[102] Samuel GB Johnson, Amir-Hossein Karimi, Yoshua Bengio, Nick Chater, Tobias Gerstenberg, Kate Larson, Sydney
Levine, Melanie Mitchell, Iyad Rahwan, Bernhard Schölkopf, et al. 2025. Imagining and building wise machines: The
centrality of AI metacognition.Trends in Cognitive Sciences(2025).
[103] Gregory Kahn, Pieter Abbeel, and Sergey Levine. 2021. Badgr: An autonomous self-supervised learning-based
navigation system.IEEE Robotics and Automation Letters6, 2 (2021), 1312–1319.
[104] Bongsu Kang, Jundong Kim, Taerim Yun, Hyojin Bae, and Chang-Eop Kim. 2025. Identifying Features that Shape
Perceived Consciousness in LLM-based AI: A Quantitative Study of Human Responses.Computers in Human Behavior
Reports(2025), 100901.
[105] Mark Kashirskiy and Ilya Makarov. 2026. SuS: Strategy-aware Surprise for Intrinsic Exploration.arXiv preprint
arXiv:2601.10349(2026).
[106] Bernhard Kerbl, Georgios Kopanas, Thomas Leimkühler, George Drettakis, et al . 2023. 3d gaussian splatting for
real-time radiance field rendering.ACM Trans. Graph.42, 4 (2023), 139–1.
[107] Feeza Khan Khanzada and Jaerock Kwon. 2025. InDRiVE: Intrinsic Disagreement based Reinforcement for Vehicle
Exploration through Curiosity Driven Generalized World Model.arXiv preprint arXiv:2503.05573(2025).
[108] Moo Jin Kim, Yihuai Gao, Tsung-Yi Lin, Yen-Chen Lin, Yunhao Ge, Grace Lam, Percy Liang, Shuran Song, Ming-Yu
Liu, Chelsea Finn, et al. 2026. Cosmos policy: Fine-tuning video models for visuomotor control and planning.arXiv
preprint arXiv:2601.16163(2026).
[109] Sang Hun Kim, Dongkyu Park, Jongmin Lee, So Young Lee, and Yosep Chong. 2025. Humanoid artificial consciousness
designed with Large Language Model based on psychoanalysis and personality theory.Cognitive Systems Research
(2025), 101392.
[110] Taesoo Kim, Yongsik Jo, Hyunmin Song, and Taehwan Kim. 2025. Towards Human-like Multimodal Conversational
Agent by Generating Engaging Speech. InInterspeech 2025 (interspeech_2025). ISCA, 4828–4832.
[111] Alexander S Klyubin, Daniel Polani, and Chrystopher L Nehaniv. 2005. Empowerment: A universal agent-centric
measure of control. In2005 ieee congress on evolutionary computation, Vol. 1. IEEE, 128–135.
[112] Asher Koriat et al. 2006.Metacognition and consciousness. Institute of Information Processing and Decision Making,
University of Haifa . . . .
[113] Vansh Kumar and M. Tanusri. 2025. Unified Speech-To-Speech Models for Real-Time, Multilingual, and Emotionally
Aware AI.Journal of Current Trends in Computer Science Research4, 6 (2025), 01–06. doi:10.33140/JCTCSR.04.06.02
[114] Kenneth Kwok, Basura Fernando, Qianli Xu, Vigneshwaran Subbaraju, Dongkyu Choi, and Boon Kiat Quek. 2026.
Explicit World Models for Reliable Human-Robot Collaboration. arXiv:2601.01705 [cs.RO] https://arxiv.org/abs/2601.
01705
[115] John Laird, Christian Lebiere, Paul Rosenbloom, and Andrea Stocco. 2025. A proposal to extend the common model
of cognition with metacognition.arXiv preprint arXiv:2506.07807(2025).
[116] John E Laird. 2019.The Soar cognitive architecture. MIT press.
[117] Pat Langley and Dongkyu Choi. 2006. A unified cognitive architecture for physical agents. InProceedings of the
National Conference on Artificial Intelligence, Vol. 21. Menlo Park, CA; Cambridge, MA; London; AAAI Press; MIT
Press; 1999, 1469.
[118] Pat Langley, Kathleen B McKusick, John A Allen, Wayne F Iba, and Kevin Thompson. 1991. A design for the icarus
architecture.ACM Sigart Bulletin2, 4 (1991), 104–109.
[119] Minh-Quan Le, Yuanzhi Zhu, Vicky Kalogeiton, and Dimitris Samaras. 2025. What about gravity in video generation?
Post-Training Newton’s Laws with Verifiable Rewards.arXiv preprint arXiv:2512.00425(2025).
[120] Trong Le, Phat Thai, Sang Nguyen, Minh Hua, Ngan Pham, Thang Bui, Tho Quan, and Tuan Bui. 2025. Text-
JEPA: A Joint Embedding Predictive Architecture for the Conversion of Natural Language into First-Order Logic. In
International Conference on Computational Collective Intelligence. Springer, 200–214.
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 48

```text
48 Rupprecht et al.
[121] Yann LeCun et al. 2022. A path towards autonomous machine intelligence version 0.9. 2, 2022-06-27.Open Review62,
1 (2022), 1–62.
[122] Yaniv Leviathan, Matan Kalman, and Yossi Matias. 2025. Prompt Repetition Improves Non-Reasoning LLMs.arXiv
preprint arXiv:2512.14982(2025).
[123] Fei-fei Li. 2025. From Words to Worlds: Spatial Intelligence is AI’s Next Frontier. https://drfeifei.substack.com/p/from-
words-to-worlds-spatial-intelligence Published on Dr. Li’s SubStack.
[124] Lin Li, Qihang Zhang, Yiming Luo, Shuai Yang, Ruilin Wang, Fei Han, Mingrui Yu, Zelin Gao, Nan Xue, Xing Zhu,
et al. 2026. Causal World Modeling for Robot Control.arXiv preprint arXiv:2601.21998(2026).
[125] Qifeng Li, Xiaosong Jia, Shaobo Wang, and Junchi Yan. 2024. Think2drive: Efficient reinforcement learning by
thinking with latent world model for autonomous driving (in carla-v2). InEuropean conference on computer vision.
Springer, 142–158.
[126] Xinqing Li, Xin He, Le Zhang, Min Wu, Xiaoli Li, and Yun Liu. 2025. A comprehensive survey on world models for
embodied ai.arXiv preprint arXiv:2510.16732(2025).
[127] Yingyan Li, Lue Fan, Jiawei He, Yuqi Wang, Yuntao Chen, Zhaoxiang Zhang, and Tieniu Tan. 2025. Enhancing
end-to-end autonomous driving with latent world model. InInternational Conference on Learning Representations,
Vol. 2025. 42942–42959.
[128] Zongyue Li, Xiao Han, Yusong Li, Niklas Strauss, and Matthias Schubert. 2025. DAWM: Diffusion Action World
Models for Offline Reinforcement Learning via Action-Inferred Transitions.arXiv preprint arXiv:2509.19538(2025).
[129] Ao Liang, Lingdong Kong, Tianyi Yan, Hongsi Liu, Yu Yang, Ziqi Huang, Wei Yin, Jialong Zuo, Yixuan Hu, Dekai
Zhu, et al. 2026. WorldLens: Full-spectrum evaluations of driving world models in real world. InProceedings of the
IEEE/CVF Conference on Computer Vision and Pattern Recognition. 36385–36399.
[130] Alan Liang, Youquan Liu, Yu Yang, Dongyue Lu, Linfeng Li, Lingdong Kong, Huaici Zhao, and Wei Tsang Ooi. 2026.
LiDARCrafter: Dynamic 4D world modeling from LiDAR sequences. InProceedings of the AAAI Conference on Artificial
Intelligence, Vol. 40. 18406–18414.
[131] Philip Lieberman. 2006.Toward an evolutionary biology of language. Harvard University Press.
[132] Juyi Lin, Arash Akbari, Yumei He, Lin Zhao, Haichao Zhang, Arman Akbari, Xingchen Xu, Zoe Y Lu, Enfu Nan,
Hokin Deng, et al. 2026. PhyGround: Benchmarking Physical Reasoning in Generative World Models.arXiv preprint
arXiv:2605.10806(2026).
[133] Juyi Lin, Arash Akbari, Yumei He, Lin Zhao, Haichao Zhang, Arman Akbari, Xingchen Xu, Zoe Y. Lu, Enfu Nan, Hokin
Deng, Edmund Yeh, Sarah Ostadabbas, Yun Fu, Jennifer Dy, Pu Zhao, and Yanzhi Wang. 2026. PhyGround: Bench-
marking Physical Reasoning in Generative World Models. https://phyground.github.io/. arXiv:2605.10806 [cs.CV]
Project website and benchmark resources, accessed 2026-05-26.
[134] Juyi Lin, Amir Taherin, Arash Akbari, Arman Akbari, Lei Lu, Guangyu Chen, Taskin Padir, Xiaomeng Yang, Weiwei
Chen, Yiqian Li, et al. 2025. Vote: vision-language-action optimization with trajectory ensemble voting.arXiv preprint
arXiv:2507.05116(2025).
[135] Minghui Lin, Xiang Wang, Yishan Wang, Shu Wang, Fengqi Dai, Pengxiang Ding, Cunxiang Wang, Zhengrong Zuo,
Nong Sang, Siteng Huang, et al. 2025. Exploring the evolution of physics cognition in video generation: A survey.
arXiv preprint arXiv:2503.21765(2025).
[136] Daochang Liu, Junyu Zhang, Anh-Dung Dinh, Eunbyung Park, Shichao Zhang, Ajmal Mian, Mubarak Shah, and
Chang Xu. 2025. Generative physical ai in vision: A survey.arXiv preprint arXiv:2501.10928(2025).
[137] Jun Liu, Zhenglun Kong, Pu Zhao, Changdi Yang, Xuan Shen, Hao Tang, Geng Yuan, Wei Niu, Wenbin Zhang, Xue
Lin, et al. 2025. Toward adaptive large language models structured pruning via hybrid-grained weight importance
assessment. InProceedings of the AAAI Conference on Artificial Intelligence, Vol. 39. 18879–18887.
[138] Yang Liu, Pengxiang Ding, Tengyue Jiang, Xudong Wang, Wenxuan Song, Minghui Lin, Han Zhao, Hongyin Zhang,
Zifeng Zhuang, Wei Zhao, et al. 2026. MMaDA-VLA: Large Diffusion Vision-Language-Action Model with Unified
Multi-Modal Instruction and Generation.arXiv preprint arXiv:2603.25406(2026).
[139] Xiaoxiao Long, Qingrui Zhao, Kaiwen Zhang, Zihao Zhang, Dingrui Wang, Yumeng Liu, Zhengjie Shu, Yi Lu,
Shouzheng Wang, Xinzhe Wei, et al. 2025. A Survey: Learning Embodied Intelligence from Physical Simulators and
World Models.arXiv preprint arXiv:2507.00917(2025).
[140] Guanxing Lu, Shiyi Zhang, Ziwei Wang, Changliu Liu, Jiwen Lu, and Yansong Tang. 2024. Manigaussian: Dynamic
gaussian splatting for multi-task robotic manipulation. InEuropean Conference on Computer Vision. Springer, 349–366.
[141] Yunhong Lu, Yanhong Zeng, Haobo Li, Hao Ouyang, Qiuyu Wang, Ka Leong Cheng, Jiapeng Zhu, Hengyuan Cao,
Zhipeng Zhang, Xing Zhu, Yujun Shen, and Min Zhang. 2025. Reward Forcing: Efficient Streaming Video Generation
with Rewarded Distribution Matching Distillation. arXiv:2512.04678 [cs.CV] https://arxiv.org/abs/2512.04678
[142] Hao Luo, Ye Wang, Wanpeng Zhang, Sipeng Zheng, Ziheng Xi, Chaoyi Xu, Haiweng Xu, Haoqi Yuan, Chi Zhang,
Yiqing Wang, et al. 2026. Being-H0. 5: Scaling Human-Centric Robot Learning for Cross-Embodiment Generalization.
arXiv preprint arXiv:2601.12993(2026).
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 49

```text
Human Cognition in Machines: A Unified Perspective of World Models 49
[143] Chak-Wing Mak, Guanyu Zhu, Boyi Zhang, Hongji Li, Xiaowei Chi, Kevin Zhang, Yichen Wu, Yangfan He, Chun-Kai
Fan, Wentao Lu, et al . 2026. PhysicsMind: Sim and Real Mechanics Benchmarking for Physical Reasoning and
Prediction in Foundational VLMs and World Models.arXiv preprint arXiv:2601.16007(2026).
[144] Léopold Maytié, Roland Bertin Johannet, and Rufin VanRullen. 2025. Multimodal Dreaming: A Global Workspace
Approach to World Model-Based Reinforcement Learning.arXiv preprint arXiv:2502.21142(2025).
[145] Pietro Mazzaglia, Tim Verbelen, Bart Dhoedt, Aaron Courville, and Sai Rajeswar. 2024. Genrl: Multimodal-foundation
world models for generalization in embodied agents.Advances in neural information processing systems37 (2024),
27529–27555.
[146] David E Meyer, Jennifer M Glass, Shane T Mueller, Travis L Seymour, and David E Kieras. 2001. Executive-process
interactive control: A unified computational theory for answering 20 questions (and more) about cognitive ageing.
European Journal of Cognitive Psychology13, 1-2 (2001), 123–164.
[147] Asen Nachkov, Danda Pani Paudel, Jan-Nico Zaech, Davide Scaramuzza, and Luc Van Gool. 2025. Dream to drive:
Model-based vehicle control using analytic world models.arXiv e-prints(2025), arXiv–2502.
[148] I Made Aswin Nahrendra, Byeongho Yu, and Hyun Myung. 2023. Dreamwaq: Learning robust quadrupedal locomotion
with implicit terrain imagination via deep reinforcement learning. In2023 IEEE International Conference on Robotics
and Automation (ICRA). IEEE, 5078–5084.
[149] Allen Newell. 1994.Unified theories of cognition. Harvard University Press.
[150] Allen Newell and Herbert A Simon. 1995. GPS, a program that simulates human thought. InComputation & Intelligence:
collected readings. 415–428.
[151] Derrick H Nguyen and Bernard Widrow. 1990. Neural networks for self-learning control systems.IEEE Control
systems magazine10, 3 (1990), 18–23.
[152] Quan Nguyen-Tri, Mukul Ranjan, and Zhiqiang Shen. 2025. Attention is all you need for kv cache in diffusion llms.
arXiv preprint arXiv:2510.14973(2025).
[153] Nima Nouri, Ronen Artzi, and Virginia Savova. 2026. An agentic AI framework for ingestion and standardization of
single-cell RNA-seq data analysis.npj Artificial Intelligence2, 1 (2026), 8.
[154] OpenAI. 2024. Video Generation Models as World Simulators. https://openai.com/research/video-generation-models-
as-world-simulators.
[155] OpenAI. 2026. Introducing Prism: A Free LaTeX-Native Workspace for Scientific Writing and Collaboration. https:
//openai.com/index/introducing-prism/. Accessed: 2026-02-16.
[156] Nicolò Pagan, Petter Törnberg, Christopher A Bail, Anikó Hannák, and Christopher Barrie. 2025. Computational
Turing Test Reveals Systematic Differences Between Human and AI Language.arXiv preprint arXiv:2511.04195(2025).
[157] Joon Sung Park, Joseph C. O’Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, and Michael S. Bernstein. 2023.
Generative Agents: Interactive Simulacra of Human Behavior. arXiv:2304.03442 [cs.HC] https://arxiv.org/abs/2304.
03442
[158] Neeley Pate, Adiba Mahbub Proma, Hangfeng He, James N Druckman, Daniel Molden, Gourab Ghoshal, and Ehsan
Hoque. 2026. Replicating Human Motivated Reasoning Studies with LLMs.arXiv preprint arXiv:2601.16130(2026).
[159] Deepak Pathak, Pulkit Agrawal, Alexei A Efros, and Trevor Darrell. 2017. Curiosity-driven exploration by self-
supervised prediction. InInternational conference on machine learning. PMLR, 2778–2787.
[160] Joséphine Pazem, Marius Krumm, Alexander Q Vining, Lukas J Fiderer, and Hans J Briegel. 2025. Free Energy
Projective Simulation (FEPS): Active inference with interpretability.PLoS One20, 9 (2025), e0331047.
[161] William Peebles and Saining Xie. 2023. Scalable diffusion models with transformers. InProceedings of the IEEE/CVF
international conference on computer vision. 4195–4205.
[162] Giovanni Pezzulo, Thomas Parr, and Karl Friston. 2024. Active inference as a theory of sentient behavior.Biological
Psychology186 (2024), 108741.
[163] Steven Pinker and Paul Bloom. 1990. Natural language and natural selection.Behavioral and brain sciences13, 4
(1990), 707–727.
[164] Andrzej Porębski and Jakub Figura. 2025. There is no such thing as conscious artificial intelligence.Humanities and
Social Sciences Communications12, 1 (2025), 1–12.
[165] Li Puyin, Tiange Xiang, Ella Mao, Shirley Wei, Xinye Chen, Adnan Masood, Li Fei-Fei, and Ehsan Adeli. 2026.
Quantiphy: A quantitative benchmark evaluating physical reasoning abilities of vision-language models. InProceedings
of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 33174–33184.
[166] Yansong Qu, Zilin Huang, Zihao Sheng, Jiancong Chen, Sikai Chen, and Samuel Labi. 2025. Vl-safe: Vision-
language guided safety-aware reinforcement learning with world models for autonomous driving.arXiv preprint
arXiv:2505.16377(2025).
[167] Xuanchi Ren et al. 2025. Cosmos-Drive-Dreams: Scalable Synthetic Driving Data Generation with World Foundation
Models.arXiv preprint arXiv:2506.09042(2025).
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 50

```text
50 Rupprecht et al.
[168] Frank E Ritter, Farnaz Tehranchi, and Jacob D Oury. 2019. ACT-R: A cognitive architecture for modeling cognition.
Wiley Interdisciplinary Reviews: Cognitive Science10, 3 (2019), e1488.
[169] Jack Rome, Stephen James, and Subramanian Ramamoorthy. 2026. Learning to unfold cloth: Scaling up world models
to deformable object manipulation.arXiv preprint arXiv:2602.16675(2026).
[170] David M Rosenthal. 2000. Consciousness, content, and metacognitive judgments.Consciousness and cognition9, 2
(2000), 203–214.
[171] Timothy Rupprecht and Yanzhi Wang. 2022. A survey for deep reinforcement learning in markovian cyber–physical
systems: Common problems and solutions.Neural Networks153 (2022), 13–36.
[172] Lloyd Russell et al. 2025. GAIA-2: A Controllable Multi-View Generative World Model for Autonomous Driving.
arXiv preprint arXiv:2503.20523(2025).
[173] Ruhi Sarikaya. 2025. Path to Artificial General Intelligence: Past, present, and future.Annual Reviews in Control60
(2025), 101021.
[174] Martin Schrimpf, Idan Asher Blank, Greta Tuckute, Carina Kauf, Eghbal A. Hosseini, Nancy Kanwisher, Joshua B.
Tenenbaum, and Evelina Fedorenko. 2021. The neural architecture of language: Integrative modeling con-
verges on predictive processing.Proceedings of the National Academy of Sciences118, 45 (2021), e2105646118.
arXiv:https://www.pnas.org/doi/pdf/10.1073/pnas.2105646118 doi:10.1073/pnas.2105646118
[175] Ramanan Sekar, Oleh Rybkin, Kostas Daniilidis, Pieter Abbeel, Danijar Hafner, and Deepak Pathak. 2020. Planning to
explore via self-supervised world models. InInternational conference on machine learning. PMLR, 8583–8592.
[176] Younggyo Seo, Danijar Hafner, Hao Liu, Fangchen Liu, Stephen James, Kimin Lee, and Pieter Abbeel. 2023. Masked
world models for visual control. InConference on Robot Learning. PMLR, 1332–1344.
[177] Dhruv Shah, Ajay Sridhar, Nitish Dashora, Kyle Stachowicz, Kevin Black, Noriaki Hirose, and Sergey Levine. 2023.
ViNT: A foundation model for visual navigation.arXiv preprint arXiv:2306.14846(2023).
[178] Yu Shang, Xin Zhang, Yinzhou Tang, Lei Jin, Chen Gao, Wei Wu, and Yong Li. 2026. Roboscape: Physics-informed
embodied world model.Advances in Neural Information Processing Systems38 (2026), 63674–63698.
[179] Chenyang Shao, Dehao Huang, Yu Li, Keyu Zhao, Weiquan Lin, Yining Zhang, Qingbin Zeng, et al. 2025. OmniScientist:
Toward a Co-evolving Ecosystem of Human and AI Scientists. arXiv:2511.16931 [cs.CY] https://arxiv.org/abs/2511.
16931
[180] Erzhuo Shao, Yifang Wang, Yifan Qian, Zhenyu Pan, Han Liu, and Dashun Wang. 2025. SciSciGPT: advancing
human–AI collaboration in the science of science.Nature Computational Science(2025), 1–15.
[181] Xuan Shen, Chenxia Han, Yufa Zhou, Yanyue Xie, Yifan Gong, Quanyi Wang, Yiwei Wang, Yanzhi Wang, Pu Zhao,
and Jiuxiang Gu. 2025. Draftattention: Fast video diffusion via low-resolution attention guidance.arXiv preprint
arXiv:2505.14708(2025).
[182] Xuan Shen, Weize Ma, Jing Liu, et al. 2025. QuartDepth: Post-Training Quantization for Real-Time Depth Estimation
on the Edge. InCVPR.
[183] Xuan Shen, Weize Ma, Yufa Zhou, Enhao Tang, Yanyue Xie, Zhengang Li, Yifan Gong, Quanyi Wang, Henghui Ding,
Yiwei Wang, et al. 2025. Fastcar: Cache attentive replay for fast auto-regressive video generation on the edge.arXiv
preprint arXiv:2505.14709(2025).
[184] Xuan Shen, Zhao Song, Yufa Zhou, et al. 2025. Lazydit: Lazy learning for the acceleration of diffusion transformers.
InAAAI.
[185] Xuan Shen, Zhao Song, Yufa Zhou, et al. 2025. Numerical pruning for efficient autoregressive models. InAAAI.
[186] Xuan Shen, Yizhou Wang, Xiangxi Shi, Yanzhi Wang, Pu Zhao, and Jiuxiang Gu. 2025. Efficient reasoning with hidden
thinking.arXiv preprint arXiv:2501.19201(2025).
[187] Xuan Shen, Pu Zhao, Yifan Gong, Zhenglun Kong, Zheng Zhan, Yushu Wu, Ming Lin, Chao Wu, Xue Lin, and Yanzhi
Wang. 2024. Search for Efficient Large Language Models. InNeurIPS.
[188] Xuan Shen, Hangyu Zheng, Yifan Gong, et al. 2025. Sparse Learning for State Space Models on Mobile. InICLR.
[189] Afagh Mehri Shervedani, Siyu Li, Natawut Monaikul, Bahareh Abbasi, Miloš Žefran, and Barbara Di Eugenio. 2025.
Multimodal Reinforcement Learning for Robots Collaborating with Humans.International Journal of Social Robotics
17, 12 (2025), 3003–3025. doi:10.1007/s12369-025-01287-6
[190] Haochen Shi, Huazhe Xu, Zhiao Huang, Yunzhu Li, and Jiajun Wu. 2024. Robocraft: Learning to see, simulate, and
shape elasto-plastic objects in 3d with graph networks.The International Journal of Robotics Research43, 4 (2024),
533–549.
[191] David Silver, Satinder Singh, Doina Precup, and Richard S Sutton. 2021. Reward is enough.Artificial intelligence299
(2021), 103535.
[192] Karen Simonyan and Andrew Zisserman. 2014. Two-stream convolutional networks for action recognition in videos.
Advances in neural information processing systems27 (2014).
[193] Zhangde Song, Jieyu Lu, Yuanqi Du, Botao Yu, Thomas M Pruyn, Yue Huang, Kehan Guo, Xiuzhe Luo, Yuanhao Qu,
Yi Qu, et al. 2025. Evaluating large language models in scientific discovery.arXiv preprint arXiv:2512.15567(2025).
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 51

```text
Human Cognition in Machines: A Unified Perspective of World Models 51
[194] Ajay Sridhar, Dhruv Shah, Catherine Glossop, and Sergey Levine. 2024. Nomad: Goal masked diffusion policies for
navigation and exploration. In2024 IEEE International Conference on Robotics and Automation (ICRA). IEEE, 63–70.
[195] James W. A. Strachan, Dalila Albergo, Giulia Borghini, Oriana Pansardi, Eugenio Scaliti, et al. 2024. Testing theory of
mind in large language models and humans.Nature Human Behaviour8, 7 (2024), 1285–1295. doi:10.1038/s41562-
024-01882-z
[196] Jingwen Sun, Wenyao Zhang, Zekun Qi, Shaojie Ren, Zezhi Liu, Hanxin Zhu, Guangzhong Sun, Xin Jin, and Zhibo Chen.
2026. VLA-JEPA: Enhancing Vision-Language-Action Model with Latent World Model.arXiv preprint arXiv:2602.10098
(2026).
[197] Yang-Tian Sun, Zehuan Huang, Yifan Niu, Lin Ma, Yan-Pei Cao, Yuewen Ma, and Xiaojuan Qi. 2026. Stereo World
Model: Camera-Guided Stereo Video Generation. arXiv:2603.17375 [cs.CV] https://arxiv.org/abs/2603.17375
[198] Cong Tang, Yuang Liu, Yueling Wu, Wence Han, Qian Yin, Xin Zheng, Wenyi Zeng, and Qiuli Zhang. 2025. MoE-World:
A Mixture-of-Experts Architecture for Multi-Task World Models.Electronics14, 24 (2025), 4884.
[199] GigaBrain Team, Angen Ye, Boyuan Wang, Chaojun Ni, Guan Huang, Guosheng Zhao, Haoyun Li, Jie Li, Jiagang
Zhu, Lv Feng, et al . 2025. Gigabrain-0: A world model-powered vision-language-action model.arXiv preprint
arXiv:2510.19430(2025).
[200] GigaWorld Team, Angen Ye, Boyuan Wang, Chaojun Ni, Guan Huang, Guosheng Zhao, Haoyun Li, Jiagang Zhu,
Kerui Li, Mengyuan Xu, et al . 2025. Gigaworld-0: World models as data engine to empower embodied ai.arXiv
preprint arXiv:2511.19861(2025).
[201] Kling Team, Jialu Chen, Yuanzheng Ci, Xiangyu Du, Zipeng Feng, Kun Gai, Sainan Guo, Feng Han, Jingbin He, Kang
He, et al. 2025. Kling-Omni Technical Report.arXiv preprint arXiv:2512.16776(2025).
[202] Marble World Team. 2025. Marble: A Multimodal World Model. https://www.worldlabs.ai/blog/marble-world-model
Published on Marble World’s Blog.
[203] Robbyant Team, Zelin Gao, Qiuyu Wang, Yanhong Zeng, Jiapeng Zhu, Ka Leong Cheng, Yixuan Li, Hanlin Wang,
Yinghao Xu, Shuailei Ma, et al. 2026. Advancing Open-source World Models.arXiv preprint arXiv:2601.20540(2026).
[204] Michael Tomasello. 2000.Two Hypotheses About Primate Cognition. MIT Press.
[205] Michael Tomasello, Malinda Carpenter, Josep Call, Tanya Behne, and Henrike Moll. 2005. Understanding and sharing
intentions: The origins of cultural cognition.Behavioral and brain sciences28, 5 (2005), 675–691.
[206] Milena Tsvetkova, Taha Yasseri, Niccolo Pescetelli, and Tobias Werner. 2024. A new sociology of humans and
machines.Nature Human Behaviour8, 10 (Oct. 2024), 1864–1876. doi:10.1038/s41562-024-02001-8
[207] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz Kaiser, and Illia
Polosukhin. 2017. Attention is all you need.Advances in neural information processing systems30 (2017).
[208] Khang HN Vo, Duc PT Nguyen, Thong T Nguyen, and Tho T Quan. 2024. TI-JEPA: An innovative energy-based joint
embedding strategy for text-image multimodal systems. InInternational Symposium on Information and Communication
Technology. Springer, 141–154.
[209] Team Wan, Ang Wang, Baole Ai, Bin Wen, Chaojie Mao, Chen-Wei Xie, Di Chen, Feiwu Yu, Haiming Zhao, Jianxiao
Yang, et al. 2025. Wan: Open and advanced large-scale video generative models.arXiv preprint arXiv:2503.20314
(2025).
[210] Hang Wang, Xin Ye, Feng Tao, Chenbin Pan, Abhirup Mallik, Burhan Yaman, Liu Ren, and Junshan Zhang. 2025.
Adawm: Adaptive world model based planning for autonomous driving. InInternational Conference on Learning
Representations, Vol. 2025. 85591–85615.
[211] Jiaming Wang, Diwen Liu, Jizhuo Chen, Jiaxuan Da, Nuowen Qian, Minh Man Tram, and Harold Soh. 2025. Genie: A
generalizable navigation system for in-the-wild environments.IEEE Robotics and Automation Letters(2025).
[212] Kangrui Wang, Pingyue Zhang, Zihan Wang, Yaning Gao, Linjie Li, Qineng Wang, Hanyang Chen, Yiping Lu,
Zhengyuan Yang, Lijuan Wang, et al. 2026. Vagen: Reinforcing world model reasoning for multi-turn vlm agents.
Advances in Neural Information Processing Systems38 (2026), 172871–172933.
[213] Lingyi Wang, Rashed Shelim, Walid Saad, and Naren Ramakrishna. 2026. MetaMind: General and Cognitive World
Models in Multi-Agent Systems by Meta-Theory of Mind.arXiv preprint arXiv:2603.00808(2026).
[214] Linhan Wang, Zichong Yang, Chen Bai, Guoxiang Zhang, Xiaotong Liu, Xiaoyin Zheng, Xiao-Xiao Long, Chang-Tien
Lu, and Cheng Lu. 2026. Drive-JEPA: Video JEPA Meets Multimodal Trajectory Distillation for End-to-End Driving.
arXiv preprint arXiv:2601.22032(2026).
[215] Linbo Wang, Yupeng Zheng, Qiang Chen, Shiwei Li, Yichen Zhang, Zebin Xing, Qichao Zhang, Xiang Li, Deheng
Qian, Pengxuan Yang, et al. 2026. Latent-WAM: Latent World Action Modeling for End-to-End Autonomous Driving.
arXiv preprint arXiv:2603.24581(2026).
[216] Qineng Wang, Wenlong Huang, Yu Zhou, Hang Yin, Tianwei Bao, Jianwen Lyu, Weiyu Liu, Ruohan Zhang, Jiajun
Wu, Li Fei-Fei, and Manling Li. 2025. ENACT: Evaluating Embodied Cognition with World Modeling of Egocentric
Interaction. arXiv:2511.20937 [cs.AI] https://arxiv.org/abs/2511.20937
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 52

```text
52 Rupprecht et al.
[217] Ruixiang Wang, Qingming Liu, Yueci Deng, Guiliang Liu, Zhen Liu, and Kui Jia. 2026. EVA: Aligning Video World
Models with Executable Robot Actions via Inverse Dynamics Rewards.arXiv preprint arXiv:2603.17808(2026).
[218] Yunheng Wang, Yuetong Fang, Taowen Wang, Yixiao Feng, Yawen Tan, Shuning Zhang, Peiran Liu, Yiding Ji, and
Renjing Xu. 2025. Dreamnav: A trajectory-based imaginative framework for zero-shot vision-and-language navigation.
arXiv preprint arXiv:2509.11197(2025).
[219] Hongtao Wu, Ya Jing, Chilam Cheang, Guangzeng Chen, Jiafeng Xu, Xinghang Li, Minghuan Liu, Hang Li, and Tao
Kong. 2024. Unleashing large-scale video generative pre-training for visual robot manipulation. InInternational
Conference on Learning Representations, Vol. 2024. 10641–10662.
[220] Jialong Wu, Shaofeng Yin, Ningya Feng, and Mingsheng Long. 2026. Rlvr-world: Training world models with
reinforcement learning.Advances in Neural Information Processing Systems38 (2026), 125312–125350.
[221] Jialong Wu, Xiaoying Zhang, Hongyi Yuan, Xiangcheng Zhang, Tianhao Huang, Changjing He, Chaoyi Deng,
Renrui Zhang, Youbin Wu, and Mingsheng Long. 2026. Visual Generation Unlocks Human-Like Reasoning through
Multimodal World Models.arXiv preprint arXiv:2601.19834(2026).
[222] Philipp Wu, Alejandro Escontrela, Danijar Hafner, Pieter Abbeel, and Ken Goldberg. 2023. Daydreamer: World models
for physical robot learning. InConference on robot learning. PMLR, 2226–2240.
[223] Wenhao Wu, Fuhong Liu, Haoru Li, Zican Hu, Daoyi Dong, Chunlin Chen, and Zhi Wang. 2026. Mixture-of-experts
meets in-context reinforcement learning.Advances in Neural Information Processing Systems38 (2026), 24751–24785.
[224] Wei Wu, Fan Lu, Yunnan Wang, Shuai Yang, Shi Liu, Fangjing Wang, Qian Zhu, He Sun, Yong Wang, Shuailei Ma,
et al. 2026. A Pragmatic VLA Foundation Model.arXiv preprint arXiv:2601.18692(2026).
[225] Chendong Xiang, Jiajun Liu, Jintao Zhang, Xiao Yang, Zhengwei Fang, Shizun Wang, Zijun Wang, Yingtian Zou,
Hang Su, and Jun Zhu. 2026. Geometry-Aware Rotary Position Embedding for Consistent Video World Model.arXiv
preprint arXiv:2602.07854(2026).
[226] Jiannan Xiang, Yi Gu, Zihan Liu, Zeyu Feng, Qiyue Gao, Yiyan Hu, Benhao Huang, Guangyi Liu, Yichi Yang, Kun
Zhou, et al. 2025. Pan: A world model for general, interactable, and long-horizon world simulation.arXiv preprint
arXiv:2511.09057(2025).
[227] Lingyu Xiao, Jiang-Jiang Liu, Sen Yang, Xiaofan Li, Xiaoqing Ye, Wankou Yang, and Jingdong Wang. 2025. Learning
multiple probabilistic decisions from latent world model in autonomous driving. In2025 IEEE International Conference
on Robotics and Automation (ICRA). IEEE, 1279–1285.
[228] Yunze Xiao, Lynnette Hui Xian Ng, Jiarui Liu, and Mona Diab. 2025. Humanizing machines: Rethinking llm anthropo-
morphism through a multi-level framework of design. InProceedings of the 2025 Conference on Empirical Methods in
Natural Language Processing. 3331–3350.
[229] Qiujie Xie, Yixuan Weng, Minjun Zhu, Fuchen Shen, Shulin Huang, Zhen Lin, Jiahui Zhou, Zilan Mao, Zijie Yang, Linyi
Yang, Jian Wu, and Yue Zhang. 2025. How Far Are AI Scientists from Changing the World? arXiv:2507.23276 [cs.AI]
https://arxiv.org/abs/2507.23276
[230] Eric Xing, Mingkai Deng, Jinyu Hou, and Zhiting Hu. 2025. Critiques of world models.arXiv preprint arXiv:2507.05169
(2025).
[231] Hu Xu, Gargi Ghosh, Po-Yao Huang, Prahal Arora, Masoumeh Aminzadeh, Christoph Feichtenhofer, Florian Metze,
and Luke Zettlemoyer. 2021. Vlm: Task-agnostic video-language model pre-training for video understanding. In
Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021. 4227–4239.
[232] Kai Xu, Hang Zhao, Ruizhen Hu, Yuhang Huang, Ziqiao Zhou, Wancheng Feng, Yi Li, Sida Peng, Xing Liu, Zihao Liu,
et al. 2026. From Specialist to Generalist: A Comprehensive Survey on World Models.Authorea Preprints(2026).
[233] Liu Yang, Kangwook Lee, Robert Nowak, and Dimitris Papailiopoulos. 2024. Looped transformers are better at
learning learning algorithms. InInternational conference on learning representations, Vol. 2024. 42195–42214.
[234] Shusheng Yang, Jihan Yang, Pinzhi Huang, Ellis L Brown II, Zihao Yang, Yue Yu, Shengbang Tong, Zihan Zheng, Yifan
Xu, Muhan Wang, et al. 2025. Cambrian-s: Towards spatial supersensing in video. InThe Fourteenth International
Conference on Learning Representations.
[235] Zhenjie Yang, Xiaosong Jia, Qifeng Li, Xue Yang, Maoqing Yao, and Junchi Yan. 2026. Raw2drive: Reinforcement
learning with aligned world models for end-to-end autonomous driving (in carla v2).Advances in Neural Information
Processing Systems38 (2026), 134122–134147.
[236] Angen Ye, Boyuan Wang, Chaojun Ni, Guan Huang, Guosheng Zhao, Hao Li, Hengtao Li, Jie Li, Jindi Lv, Jingyu Liu,
et al. 2026. GigaWorld-Policy: An Efficient Action-Centered World–Action Model.arXiv preprint arXiv:2603.17240
(2026).
[237] Seonghyeon Ye, Yunhao Ge, Kaiyuan Zheng, Shenyuan Gao, Sihyun Yu, George Kurian, Suneel Indupuru, You Liang
Tan, Chuning Zhu, Jiannan Xiang, et al . 2026. World action models are zero-shot policies.arXiv preprint
arXiv:2602.15922(2026).
[238] Yavar Taheri Yeganeh, Mohsen Jafari, and Andrea Matta. 2025. Deep Active Inference Agents for Delayed and
Long-Horizon Environments.arXiv preprint arXiv:2505.19867(2025).
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 53

```text
Human Cognition in Machines: A Unified Perspective of World Models 53
[239] Pinrui Yu, Dan Luo, Timothy Rupprecht, Lei Lu, et al. 2024. FasterVD: On Acceleration of Video Diffusion Models.. In
IJCAI. 8838–8842.
[240] Wei Yu, Runjia Qian, Yumeng Li, Liquan Wang, Songheng Yin, Sri Siddarth Chakaravarthy P, Dennis Anthony, Yang
Ye, Yidi Li, Weiwei Wan, and Animesh Garg. 2026. MosaicMem: Hybrid Spatial Memory for Controllable Video World
Models. arXiv:2603.17117 [cs.CV] https://arxiv.org/abs/2603.17117
[241] Fang Yuan, Junjie Zeng, Yue Hu, Zhengqiu Zhu, Quanjun Yin, and Yuxiang Xie. 2025. NL2GenSym: Natural Lan-
guage to Generative Symbolic Rules for SOAR Cognitive Architecture via Large Language Models.arXiv preprint
arXiv:2510.09355(2025).
[242] Jianhao Yuan, Xiaofeng Zhang, Felix Friedrich, Nicolas Beltran-Velez, Melissa Hall, Reyhane Askari-Hemmat, Xi-
aochuang Han, Nicolas Ballas, Michal Drozdzal, and Adriana Romero-Soriano. 2026. Inference-time Physics Alignment
of Video Generative Models with Latent World Models.arXiv preprint arXiv:2601.10553(2026).
[243] Shenghai Yuan, Yuanyang Yin, Zongjian Li, Xinwei Huang, Xiao Yang, and Li Yuan. 2026. Helios: Real Real-Time
Long Video Generation Model. arXiv:2603.04379 [cs.CV] https://arxiv.org/abs/2603.04379
[244] Tianyuan Yuan, Zibin Dong, Yicheng Liu, and Hang Zhao. 2026. Fast-WAM: Do World Action Models Need Test-time
Future Imagination? arXiv:2603.16666 [cs.CV] https://arxiv.org/abs/2603.16666
[245] Jingtong Yue, Ziqi Huang, Zhaoxi Chen, Xintao Wang, Pengfei Wan, and Ziwei Liu. 2025. Simulating the Visual
World with Artificial Intelligence: A Roadmap.arXiv preprint arXiv:2511.08585(2025).
[246] Valentinos Zachariou, Roberta Klatzky, and Marlene Behrmann. 2014. Ventral and dorsal visual stream contributions
to the perception of object shape and object location.Journal of Cognitive Neuroscience26, 1 (2014), 189–209.
[247] Kai Zeng, Zhanqian Wu, Kaixin Xiong, Xiaobao Wei, Xiangyu Guo, Zhenxin Zhu, Kalok Ho, Lijun Zhou, Bohan Zeng,
Ming Lu, et al. 2025. Rethinking Driving World Model as Synthetic Data Generator for Perception Tasks.arXiv
preprint arXiv:2510.19195(2025).
[248] Zheng Zhan, Zhenglun Kong, Yifan Gong, et al. 2024. Exploring Token Pruning in Vision State Space Models. In
NeurIPS.
[249] Zheng Zhan, Yushu Wu, Yifan Gong, et al . 2024. Fast and Memory-Efficient Video Diffusion Using Streamlined
Inference. InNeurIPS.
[250] Zheng Zhan, Yushu Wu, Zhenglun Kong, Changdi Yang, Yifan Gong, Xuan Shen, Xue Lin, Pu Zhao, and Yanzhi Wang.
2024. Rethinking token reduction for state space models. InProceedings of the 2024 Conference on Empirical Methods
in Natural Language Processing. 1686–1697.
[251] Dong Zhang, Zhaowei Li, Pengyu Wang, Xin Zhang, Yaqian Zhou, and Xipeng Qiu. 2024. SpeechAgents: Human-
Communication Simulation with Multi-Modal Multi-Agent Systems. arXiv:2401.03945 [cs.CL] https://arxiv.org/abs/
2401.03945
[252] Kaifeng Zhang, Baoyu Li, Kris Hauser, and Yunzhu Li. 2024. Adaptigraph: Material-adaptive graph-based neural
dynamics for robotic manipulation.arXiv preprint arXiv:2407.07889(2024).
[253] Kaidong Zhang, Pengzhen Ren, Bingqian Lin, Junfan Lin, Shikui Ma, Hang Xu, and Xiaodan Liang. 2024. Pivot-r:
Primitive-driven waypoint-aware world model for robotic manipulation.Advances in Neural Information Processing
Systems37 (2024), 54105–54136.
[254] Kaiwen Zhang, Zhenyu Tang, Xiaotao Hu, Xingang Pan, Xiaoyang Guo, Yuan Liu, Jingwei Huang, Li Yuan, Qian Zhang,
Xiao-Xiao Long, et al. 2025. Epona: Autoregressive diffusion world model for autonomous driving. InProceedings of
the IEEE/CVF International Conference on Computer Vision. 27220–27230.
[255] Lunjun Zhang, Yuwen Xiong, Ze Yang, Sergio Casas, Rui Hu, and Raquel Urtasun. 2024. Copilot4d: Learning
unsupervised world models for autonomous driving via discrete diffusion. InInternational Conference on Learning
Representations, Vol. 2024. 7269–7299.
[256] Xiangdong Zhang, Jiaqi Liao, Shaofeng Zhang, Fanqing Meng, Xiangpeng Wan, Junchi Yan, and Yu Cheng. 2026.
Videorepa: Learning physics for video generation through relational alignment with foundation models.Advances in
Neural Information Processing Systems38 (2026), 122647–122676.
[257] Yumeng Zhang, Shi Gong, Kaixin Xiong, Xiaoqing Ye, Xiao Tan, Fan Wang, Jizhou Huang, Hua Wu, and Haifeng
Wang. 2024. Bevworld: A multimodal world model for autonomous driving via unified bev latent space.arXiv preprint
arXiv:2407.05679(2024).
[258] Pu Zhao, Arash Akbari, Xuan Shen, Zhenglun Kong, Yixin Shen, Sung-En Chang, Timothy Rupprecht, Lei Lu, Enfu
Nan, Changdi Yang, et al. 2025. Open-Source Multimodal Moxin Models with Moxin-VLM and Moxin-VLA.arXiv
preprint arXiv:2512.22208(2025).
[259] Pu Zhao, Juyi Lin, Timothy Rupprecht, Arash Akbari, Chence Yang, Rahul Chowdhury, Elaheh Motamedi, Arman
Akbari, Yumei He, Chen Wang, et al. 2026. PhyWorld: Physics-Faithful World Model for Video Generation.arXiv
preprint arXiv:2605.19242(2026).
[260] Pu Zhao, Xuan Shen, Zhenglun Kong, Yixin Shen, Sung-En Chang, Timothy Rupprecht, Lei Lu, Enfu Nan, Changdi
Yang, Yumei He, et al. 2024. Fully Open Source Moxin-7B Technical Report.arXiv preprint arXiv:2412.06845(2024).
, Vol. 1, No. 1, Article . Publication date: June 2026.
```

## PDF page 54

```text
54 Rupprecht et al.
[261] Pu Zhao, Fei Sun, Xuan Shen, et al . 2024. Pruning Foundation Models for High Accuracy without Retraining. In
Findings of EMNLP 2024. ACL.
[262] Zhida Zhao, Talas Fu, Yifan Wang, Lijun Wang, and Huchuan Lu. 2026. From forecasting to planning: Policy
world model for collaborative state-action prediction.Advances in Neural Information Processing Systems38 (2026),
134585–134611.
[263] Haoyu Zhen, Qiao Sun, Hongxin Zhang, Junyan Li, Siyuan Zhou, Yilun Du, and Chuang Gan. 2025. Tesseract: learning
4d embodied world models.arXiv preprint arXiv:2504.20995(2025).
[264] Wenzhao Zheng, Weiliang Chen, Yuanhui Huang, Borui Zhang, Yueqi Duan, and Jiwen Lu. 2024. Occworld: Learning
a 3d occupancy world model for autonomous driving. InEuropean conference on computer vision. Springer, 55–72.
[265] Wenzhao Zheng, Zetian Xia, Yuanhui Huang, Sicheng Zuo, Jie Zhou, and Jiwen Lu. 2024. Doe-1: Closed-loop
autonomous driving with large world model.arXiv preprint arXiv:2412.09627(2024).
[266] Siyuan Zhou, Yilun Du, Jiaben Chen, Yandong Li, Dit-Yan Yeung, and Chuang Gan. 2024. Robodreamer: Learning
compositional world models for robot imagination.arXiv preprint arXiv:2404.12377(2024).
[267] Chuning Zhu, Raymond Yu, Siyuan Feng, Benjamin Burchfiel, Paarth Shah, and Abhishek Gupta. 2025. Unified world
models: Coupling video and action diffusion for pretraining on large robotic datasets.arXiv preprint arXiv:2504.02792
(2025).
[268] Fangqi Zhu, Hongtao Wu, Song Guo, Yuxiao Liu, Chilam Cheang, and Tao Kong. 2025. Irasim: A fine-grained world
model for robot manipulation. InProceedings of the IEEE/CVF International Conference on Computer Vision. 9834–9844.
[269] Hongzhou Zhu, Min Zhao, Guande He, Hang Su, Chongxuan Li, and Jun Zhu. 2026. Causal Forcing: Autoregressive
Diffusion Distillation Done Right for High-Quality Real-Time Interactive Video Generation. arXiv:2602.02214 [cs.CV]
https://arxiv.org/abs/2602.02214
[270] Yixuan Zhu, Jiaqi Feng, Wenzhao Zheng, Yuan Gao, Xin Tao, Pengfei Wan, Jie Zhou, and Jiwen Lu. 2025. Astra:
General Interactive World Model with Autoregressive Denoising.arXiv preprint arXiv:2512.08931(2025).
[271] Ziyue Zhu, Shangyang Wu, Shuai Zhao, Zhiqiu Zhao, Shengjie Li, Yi Wang, Fang Li, and Haoran Luo. [n. d.]. NS-VLA:
Towards Neuro-Symbolic Vision-Language-Action Models. ([n. d.]).
[272] Shaobin Zhuang, Zhipeng Huang, Ying Zhang, Fangyikang Wang, Canmiao Fu, Binxin Yang, Chong Sun, Chen Li,
and Yali Wang. 2025. Video-gpt via next clip diffusion.arXiv preprint arXiv:2505.12489(2025).
, Vol. 1, No. 1, Article . Publication date: June 2026.
```
