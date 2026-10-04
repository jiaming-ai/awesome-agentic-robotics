# Awesome Agentic Robotics

A curated literature map of AI agents that plan, program, orchestrate, diagnose, coordinate, or improve robots and robot policies.


## Taxonomy

| Category | Where the agent has agency |
|---|---|
| [Planning, reasoning, and closed-loop execution](#planning-reasoning-and-closed-loop-execution) | Decomposes goals, chooses skills, verifies outcomes, asks for help, and replans. |
| [Code-as-policy and tool orchestration](#code-as-policy-and-tool-orchestration) | Writes executable robot programs and composes perception, planning, and control APIs. |
| [Spatial grounding and constraint programs](#spatial-grounding-and-constraint-programs) | Converts language and images into explicit spatial objectives, constraints, or scene queries. |
| [Memory, failure repair, and skill discovery](#memory-failure-repair-and-skill-discovery) | Diagnoses failures, stores experience, repairs behavior, and grows reusable skill libraries. |
| [Autonomous task, data, reward, and policy improvement](#autonomous-task-data-reward-and-policy-improvement) | Changes data collection, rewards, policies, or training code using environment feedback. |
| [Multi-agent and multi-robot coordination](#multi-agent-and-multi-robot-coordination) | Assigns specialist roles, negotiates plans, allocates tasks, and coordinates multiple robots. |
| [Frameworks, benchmarks, and empirical evaluations](#frameworks-benchmarks-and-empirical-evaluations) | Supplies robot-agent interfaces, benchmarks capabilities, or measures reliability and safety. |
| [Surveys and perspectives](#surveys-and-perspectives) | Organizes the field, its architectures, and open research problems. |

## Planning, reasoning, and closed-loop execution

| Date | Method and paper | Venue | Evidence | One-sentence contribution |
|---|---|---|---|---|
| 2026-07 | **ACE** — [Agentic Control for Embodied Manipulation via Zero-shot Workflow Reasoning](https://arxiv.org/abs/2607.04162) | arXiv | Physical | ACE grounds a reasoned workflow through mask-based vision-action skills and uses multi-timescale memory to verify, retry, repair, or replan after physical outcomes. |
| 2025-05 | **Agentic Robot** — [A Brain-Inspired Framework for Vision-Language-Action Models in Embodied Agents](https://arxiv.org/abs/2505.23450) | arXiv | Simulation | A standardized action procedure coordinates a reasoning model, a VLA executor, and a temporal verifier for self-verified long-horizon manipulation. |
| 2025-02 | **Reflective Planning** — [Vision-Language Models for Multi-Stage Long-Horizon Robotic Manipulation](https://arxiv.org/abs/2502.16707) | CoRL 2025 | Simulation | A VLM uses a learned dynamics model to imagine future states and reflect on suboptimal actions before executing multi-stage manipulation plans. |
| 2024-10 | **BUMBLE** — [Unifying Reasoning and Acting with Vision-Language Models for Building-wide Mobile Manipulation](https://arxiv.org/abs/2410.06237) | ICRA 2025 | Physical | BUMBLE combines open-world visual reasoning, a broad motor-skill library, and dual memory to perform building-scale mobile manipulation. |
| 2024-09 | **SELP** — [Generating Safe and Efficient Task Plans for Robot Agents with Large Language Models](https://arxiv.org/abs/2409.19471) | arXiv | Simulation | SELP maps language to temporal logic using equivalence voting and constrains decoding so generated drone and manipulation plans satisfy user rules. |
| 2023-07 | **SayPlan** — [Grounding Large Language Models using 3D Scene Graphs for Scalable Robot Task Planning](https://arxiv.org/abs/2307.06135) | CoRL 2023 | Sim + physical | SayPlan searches a hierarchical 3D scene graph, invokes a classical planner, and uses simulator feedback to revise long-horizon plans. |
| 2023-07 | **KnowNo** — [Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners](https://arxiv.org/abs/2307.01928) | CoRL 2023 | Sim + physical | KnowNo applies conformal prediction to an LLM planner so the robot requests human help when uncertainty threatens statistically calibrated task success. |
| 2023-06 | **Statler** — [State-Maintaining Language Models for Embodied Reasoning](https://arxiv.org/abs/2306.17840) | ICRA 2024 | Simulation | Statler separates world-state estimation from action generation and updates the latent textual state after every embodied action. |
| 2023-03 | **Grounded Decoding** — [Guiding Text Generation with Grounded Models for Robot Control](https://arxiv.org/abs/2303.00855) | NeurIPS 2023 | Sim + physical | Grounded Decoding combines token probabilities with affordance, safety, and preference model scores while an LLM generates a robot plan. |
| 2022-09 | **ProgPrompt** — [Generating Situated Robot Task Plans using Large Language Models](https://arxiv.org/abs/2209.11302) | ICRA 2023 | Sim + physical | ProgPrompt expresses available objects, actions, assertions, and recovery steps as a programmatic prompt that constrains situated task plans. |
| 2022-07 | **Inner Monologue** — [Embodied Reasoning through Planning with Language Models](https://arxiv.org/abs/2207.05608) | CoRL 2022 | Sim + physical | Inner Monologue feeds success signals, scene descriptions, and human feedback back into an LLM planner to close the execution loop. |
| 2022-04 | **SayCan** — [Do As I Can, Not As I Say: Grounding Language in Robotic Affordances](https://arxiv.org/abs/2204.01691) | CoRL 2022 | Physical | SayCan ranks language-model skill proposals with learned affordance value functions so high-level plans remain feasible for the robot. |

## Code-as-policy and tool orchestration

| Date | Method and paper | Venue | Evidence | One-sentence contribution |
|---|---|---|---|---|
| 2026-07 | **ARCHITECT** — [A Few Words Go a Long Way: Language Guided Robot Policy Synthesis](https://arxiv.org/abs/2607.23784) | arXiv | Physical | ARCHITECT treats policy acquisition as interactive program synthesis and distills trace-grounded language corrections into a persistent skill library. |
| 2026-01 | **ALRM** — [Agentic LLM for Robotic Manipulation](https://arxiv.org/abs/2601.19510) | arXiv | Simulation | ALRM supports ReAct-style execution through complementary Code-as-Policy and Tool-as-Policy modes and introduces a 56-task reasoning benchmark. |
| 2025-11 | **Maestro** — [Orchestrating Robotics Modules with Coding Agents for Zero-Shot Generalist Robots](https://maestro-robot.github.io/static/Maestro.pdf) | NeurIPS SpaVLE Workshop 2025 | Physical | Maestro wraps diverse perception, planning, control, and learned-policy modules in a coding-agent harness that renders tool outputs for verification and recovery. |
| 2025-10 | **Towards Reliable Code-as-Policies** — [A Neuro-Symbolic Framework for Embodied Task Planning](https://arxiv.org/abs/2510.21302) | NeurIPS 2025 | Sim + physical | The framework combines symbolic verification with exploratory code that actively acquires missing observations before synthesizing a grounded policy. |
| 2025-10 | **ModuLoop** — [Low-Level Code Generation using Modular Synthesizer and Closed-Loop Debugger for Robotic Control](https://doi.org/10.1109/LRA.2025.3623437) | IEEE RA-L 2025 | Physical | ModuLoop generates low-level control code module by module, inserts diagnostic probes, and iteratively debugs executions for calibration and manipulation. |
| 2024-06 | **IFVF Code Generation** — [Enabling Robots to Follow Abstract Instructions and Complete Complex Dynamic Tasks](https://arxiv.org/abs/2406.11231) | arXiv | Physical | GPT-4 retrieves domain knowledge and writes robot code whose execution is adapted through integrated force and visual feedback. |
| 2024-02 | **RoboCodeX** — [Multimodal Code Generation for Robotic Behavior Synthesis](https://arxiv.org/abs/2402.16117) | arXiv | Sim + physical | RoboCodeX uses tree-structured multimodal code generation to decompose instructions into object-centric, affordance-aware, and safety-aware programs. |
| 2023-05 | **Demo2Code** — [From Summarizing Demonstrations to Synthesizing Code via Extended Chain-of-Thought](https://arxiv.org/abs/2305.16744) | NeurIPS 2023 | Simulation | Demo2Code recursively summarizes demonstrations into reusable behavior specifications and expands them into executable robot programs. |
| 2023-05 | **Instruct2Act** — [Mapping Multi-modality Instructions to Robotic Actions with Large Language Model](https://arxiv.org/abs/2305.11176) | arXiv | Physical | Instruct2Act generates Python programs that call foundation-model perception APIs and robot primitives directly from multimodal instructions. |
| 2023-02 | **ChatGPT for Robotics** — [Design Principles and Model Abilities](https://arxiv.org/abs/2306.17582) | IEEE Access 2024 | Sim + physical | The framework exposes a high-level robot function library and uses dialogue, code generation, and closed-loop feedback to refine behavior across embodiments. |
| 2022-09 | **Code as Policies** — [Language Model Programs for Embodied Control](https://arxiv.org/abs/2209.07753) | ICRA 2023 | Physical | Code as Policies recursively generates executable policy functions that compose perception and control APIs with ordinary Python libraries. |

Maestro's current author-hosted paper and project page use “Coding Agents”; its earlier [arXiv record](https://arxiv.org/abs/2511.00917) used “Vision-Language Models” and is withdrawn while the revised work is under review.

## Spatial grounding and constraint programs

| Date | Method and paper | Venue | Evidence | One-sentence contribution |
|---|---|---|---|---|
| 2025-09 | **ASP** — [Agentic Scene Policies: Unifying Space, Semantics, and Affordances for Robot Action](https://arxiv.org/abs/2509.19571) | arXiv | Physical | ASP lets an LLM agent query an object-centric scene representation for semantic, spatial, and affordance facts that guide downstream motion planning. |
| 2024-09 | **ReKep** — [Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation](https://arxiv.org/abs/2409.01652) | CoRL 2024 | Physical | ReKep converts a language task and image into executable relational keypoint constraints that a perception-action optimization loop satisfies online. |
| 2024-03 | **MOKA** — [Open-World Robotic Manipulation through Mark-Based Visual Prompting](https://arxiv.org/abs/2403.03174) | RSS 2024 | Physical | MOKA prompts a VLM with marked images to infer object affordance points and motion paths for open-world manipulation. |
| 2023-09 | **LLM-Grounder** — [Open-Vocabulary 3D Visual Grounding with Large Language Model as an Agent](https://arxiv.org/abs/2309.12311) | ICRA 2024 | Simulation | LLM-Grounder decomposes complex referring expressions and invokes 3D grounding tools as an agent to locate open-vocabulary objects. |
| 2023-07 | **VoxPoser** — [Composable 3D Value Maps for Robotic Manipulation with Language Models](https://arxiv.org/abs/2307.05973) | CoRL 2023 | Sim + physical | VoxPoser uses LLM-generated code to compose VLM-grounded 3D value maps that serve as objectives for model-based trajectory optimization. |

## Memory, failure repair, and skill discovery

| Date | Method and paper | Venue | Evidence | One-sentence contribution |
|---|---|---|---|---|
| 2026-09 | **APPL** — [Agent Priors-guided Policy Learning](https://arxiv.org/abs/2609.35690) | arXiv | Simulation | A language-model construction agent segments demonstrations into skills and trains and verifies one policy per proposed structural prior, and a runtime agent selects and composes these policies through interfaces stating each prior's applicability. |
| 2026-06 | **ASPIRE** — [Agentic /Skills Discovery for Robotics](https://arxiv.org/abs/2607.00272) | arXiv | Sim-to-real | ASPIRE uses multimodal execution traces, autonomous code repair, evolutionary exploration, and a growing library to discover reusable cross-task robot skills. |
| 2026-03 | **Uni-Skill** — [Building Self-Evolving Skill Repository for Generalizable Robotic Manipulation](https://arxiv.org/abs/2603.02623) | arXiv | Sim + physical | Uni-Skill detects missing capabilities during planning and retrieves automatically annotated video demonstrations to implement and retain new skills. |
| 2026-03 | **Act-Observe-Rewrite** — [Multimodal Coding Agents as In-Context Policy Learners for Robot Manipulation](https://arxiv.org/abs/2603.04466) | arXiv | Simulation | A multimodal coding agent observes trial outcomes and rewrites the complete executable controller between episodes without gradients or demonstrations. |
| 2025-09 | **Growing with Your Embodied Agent** — [A Human-in-the-Loop Lifelong Code Generation Framework for Long-Horizon Manipulation Skills](https://arxiv.org/abs/2509.18597) | arXiv | Sim + physical | The framework converts human corrections into reusable code skills stored in external memory and retrieves them with task-specific hints. |
| 2025-08 | **L3M+P** — [Lifelong Planning with Large Language Models](https://arxiv.org/abs/2508.01917) | arXiv | Sim + physical | L3M+P maintains a verified knowledge graph from sensor and language updates and retrieves it to construct classical planning problems. |
| 2025-04 | **Memory-Augmented Household Agent** — [LLM-Empowered Embodied Agent for Memory-Augmented Task Planning in Household Robotics](https://arxiv.org/abs/2504.21716) | Austrian Robotics Workshop 2025 | Physical | Routing, planning, and knowledge agents use retrieval-augmented long-term object memory to plan household service-robot tasks. |
| 2024-11 | **RONAR** — [I Can Tell What I am Doing: Toward Real-World Natural Language Grounding of Robot Experiences](https://arxiv.org/abs/2411.12960) | CoRL 2024 | Physical | RONAR turns multimodal robot traces into grounded narratives that support behavior explanation, failure analysis, and human-guided recovery. |
| 2024-06 | **AIC MLLM** — [Autonomous Interactive Correction MLLM for Robust Robotic Manipulation](https://arxiv.org/abs/2406.11548) | CoRL 2024 | Sim + physical | AIC MLLM extracts feedback from failed interactions and revises low-level contact poses using visual masks and language prompts. |
| 2023-06 | **REFLECT** — [Summarizing Robot Experiences for Failure Explanation and Correction](https://arxiv.org/abs/2306.15724) | CoRL 2023 | Sim + physical | REFLECT compresses multisensory histories into hierarchical summaries that an LLM uses to explain failures and generate corrective plans. |

## Autonomous task, data, reward, and policy improvement

| Date | Method and paper | Venue | Evidence | One-sentence contribution |
|---|---|---|---|---|
| 2026-06 | **ENPIRE** — [Agentic Robot Policy Self-Improvement in the Real World](https://arxiv.org/abs/2606.19980) | arXiv | Physical | ENPIRE closes the physical research loop with automatic reset and verification, fleet rollouts, coding-agent policy improvement, and evolutionary branching. |
| 2026-06 | **RHO** — [Your Coding Agent is Secretly a Roboticist](https://arxiv.org/abs/2606.16458) | arXiv | Simulation | Robotics Harness Optimization lets coding agents search interpretable multi-file policy repositories from execution and reward feedback before deployment. |
| 2024-06 | **DrEureka** — [Language Model Guided Sim-To-Real Transfer](https://arxiv.org/abs/2406.01967) | RSS 2024 | Sim-to-real | DrEureka uses an LLM to design rewards and convert reward diagnostics into domain-randomization ranges for zero-shot hardware transfer. |
| 2024-01 | **AutoRT** — [Embodied Foundation Models for Large Scale Orchestration of Robotic Agents](https://arxiv.org/abs/2401.12963) | arXiv | Physical | AutoRT combines VLM scene understanding, LLM task proposals, and safety filters to orchestrate a robot fleet that collected 77,000 real episodes. |
| 2023-11 | **RoboGen** — [Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation](https://arxiv.org/abs/2311.01455) | ICML 2024 | Simulation | RoboGen autonomously proposes tasks, generates scenes and supervision, and trains policies in a self-guided generative simulation loop. |
| 2023-10 | **Eureka** — [Human-Level Reward Design via Coding Large Language Models](https://arxiv.org/abs/2310.12931) | ICLR 2024 | Simulation | Eureka evolves executable reward code and reflects on training statistics to outperform human-engineered rewards across many simulated robots. |
| 2023-10 | **GenSim** — [Generating Robotic Simulation Tasks via Large Language Models](https://arxiv.org/abs/2310.01361) | ICLR 2024 | Sim-to-real | GenSim uses goal-directed and exploratory LLM agents to generate task assets, environment code, and demonstrations that train transferable policies. |
| 2023-06 | **RoboCat** — [A Self-Improving Foundation Agent for Robotic Manipulation](https://arxiv.org/abs/2306.11706) | TMLR 2023 | Sim + physical | RoboCat repeatedly fine-tunes a goal-conditioned multi-embodiment policy on self-generated trajectories to improve adaptation to new tasks and robots. |

## Multi-agent and multi-robot coordination

| Date | Method and paper | Venue | Evidence | One-sentence contribution |
|---|---|---|---|---|
| 2026-07 | **Closed-Loop Multi-Agent Manipulation** — [A Closed-Loop Multi-Agent Framework for Robust Multi-Robot Manipulation](https://arxiv.org/abs/2607.06990) | RSS 2026 | Physical | A planning agent, per-robot manipulation agents, and a verification agent coordinate tool use and feed semantic corrections back after physical execution. |
| 2025-07 | **UROSA** — [Distributed AI Agents for Cognitive Underwater Robot Autonomy](https://arxiv.org/abs/2507.23735) | arXiv | Sim + physical | UROSA distributes perception, reasoning, planning, adaptation, and on-the-fly ROS 2 node generation across specialized underwater-robot agents. |
| 2025-05 | **RAI** — [Flexible Agent Framework for Embodied AI](https://arxiv.org/abs/2505.07532) | arXiv | Sim + physical | RAI supplies embodiment mechanisms, ROS 2 and digital-twin integrations, and composable agents for physical and simulated robot systems. |
| 2024-11 | **MALMM** — [Multi-Agent Large Language Models for Zero-Shot Robotics Manipulation](https://arxiv.org/abs/2411.17636) | arXiv | Simulation | MALMM separates high-level planning, low-level code generation, and supervision among specialist LLM agents that replan from each observation. |
| 2024-09 | **MHRC** — [Closed-loop Decentralized Multi-Heterogeneous Robot Collaboration with Large Language Models](https://arxiv.org/abs/2409.16030) | arXiv | Simulation | MHRC lets heterogeneous mobile and manipulation agents exchange textual feedback, request help, and revise decentralized collaborative plans. |
| 2024-04 | **LABOR** — [Large Language Models for Orchestrating Bimanual Robots](https://arxiv.org/abs/2404.02018) | arXiv | Simulation | LABOR uses an LLM to analyze task dependencies and synthesize coordination policies for two robot arms without bimanual demonstrations. |
| 2023-09 | **SMART-LLM** — [Smart Multi-Agent Robot Task Planning using Large Language Models](https://arxiv.org/abs/2309.10062) | arXiv | Sim + physical | SMART-LLM stages task decomposition, coalition formation, and capability-aware allocation for heterogeneous robot teams. |
| 2023-07 | **RoCo** — [Dialectic Multi-Robot Collaboration with Large Language Models](https://arxiv.org/abs/2307.04738) | ICRA 2024 | Sim + physical | RoCo represents each robot with an LLM agent that discusses strategy and waypoints, then revises plans from collision and feasibility feedback. |

## Frameworks, benchmarks, and empirical evaluations

| Date | Method and paper | Venue | Evidence | One-sentence contribution |
|---|---|---|---|---|
| 2026-04 | **dWorldEval** — [Scalable Robotic Policy Evaluation via Discrete Diffusion World Model](https://arxiv.org/abs/2604.22152) | arXiv | Sim + physical | dWorldEval predicts action-conditioned futures and progress tokens in a unified discrete space to evaluate policies across simulated and real tasks. |
| 2026-03 | **CaP-X** — [A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation](https://arxiv.org/abs/2603.22435) | arXiv | Sim + physical | CaP-X combines CaP-Gym, CaP-Bench, a training-free multi-turn agent, and reinforcement learning to measure and improve coding-agent robustness. |
| 2026-03 | **Language-to-Action Evaluation** — [From Language to Action: Can LLM-Based Agents Be Used for Embodied Robot Cognition?](https://arxiv.org/abs/2603.03148) | arXiv | Simulation | The study evaluates an LLM cognitive core with working and episodic memory and exposes persistent grounding and reliability limitations. |
| 2026-02 | **Agentic AI for Robot Control** — [Flexible but still Fragile](https://arxiv.org/abs/2602.13081) | arXiv | Physical | A physical-robot study stress-tests iterative tool-based planners and documents how operator intervention, timing, and execution events still cause failures. |
| 2025-06 | **ARNA** — [General-Purpose Robotic Navigation via LVLM-Orchestrated Perception, Reasoning, and Acting](https://arxiv.org/abs/2506.17462) | arXiv | Simulation | ARNA provides an LVLM agent that dynamically assembles perception, reasoning, and navigation tools and evaluates the resulting workflows on navigation tasks. |
| 2025-05 | **WorldEval** — [World Model as Real-World Robot Policies Evaluator](https://arxiv.org/abs/2505.19017) | arXiv | Physical | WorldEval uses a policy-conditioned video world model to rank checkpoints and screen unsafe candidate actions before costly hardware evaluation. |
| 2025-02 | **EmbodiedBench** — [Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents](https://arxiv.org/abs/2502.09560) | arXiv | Simulation | EmbodiedBench evaluates MLLM agents on 1,128 tasks across four environments and isolates perception, reasoning, planning, and action bottlenecks. |
| 2024-10 | **ROSA** — [Robot Operating System Agent](https://arxiv.org/abs/2410.06472) | IEEE Aerospace 2025 | Sim + physical | ROSA exposes validated ROS 1 and ROS 2 operations as agent tools and adds constraint checks for natural-language robot inspection and control. |
| 2024-02 | **RobotScript** — [An LLM and Simulator-Assisted Robot Programming System for Human-Robot Interaction](https://arxiv.org/abs/2402.14623) | arXiv | Sim + physical | RobotScript maps free-form instructions to a deployable robot API, validates generated programs in simulation, and transfers them to physical arms. |

## Surveys and perspectives

| Date | Paper | Venue | Evidence | One-sentence contribution |
|---|---|---|---|---|
| 2026-06 | [When Multi-Robot Systems Meet Agentic AI: Towards Embodied Collective Intelligence](https://arxiv.org/abs/2606.27929) | arXiv | Review | This perspective frames collective robot intelligence around shared world, task, and skill memories and illustrates the architecture on navigation. |
| 2025-08 | [Towards Embodied Agentic AI: Review and Classification of LLM- and VLM-Driven Systems for Manufacturing](https://arxiv.org/abs/2508.05294) | arXiv | Review | The review classifies embodied agents by protocol, interface, orchestration, embedded intelligence, and the roles assigned to foundation models. |
| 2025-02 | [Large Language Models for Multi-Robot Systems: A Survey](https://arxiv.org/abs/2502.03814) | arXiv | Review | This survey organizes LLM-enabled multi-robot work across communication, task allocation, planning, control, human interaction, and safety. |
| 2024-02 | [Real-World Robot Applications of Foundation Models: A Review](https://arxiv.org/abs/2402.05741) | arXiv | Review | The review maps foundation models to perception, planning, control, interaction, and learning in deployed robot systems. |
| 2024-01 | [Agent AI: Surveying the Horizons of Multimodal Interaction](https://arxiv.org/abs/2401.03568) | arXiv | Review | Agent AI develops a broad multimodal-agent taxonomy that connects foundation-model reasoning, tool use, embodiment, and multi-agent behavior. |

## Reading the field

The literature shows a progression from **grounded skill selection** (SayCan), through **executable program synthesis** (Code as Policies), to **closed-loop orchestration** (Maestro and CaP-X), and finally to **agents that modify the robotics development process itself** (RHO, ENPIRE, and ASPIRE). Three distinctions are especially useful when comparing methods:

1. **Deployment-time agency vs. development-time agency:** Maestro and ACE reason while executing, whereas RHO and ENPIRE use agents to improve policies before the final policy is deployed.
2. **Fixed skills vs. evolving skills:** SayCan selects from a fixed library, while Uni-Skill and ASPIRE acquire and retain new skills.
3. **Digital feedback vs. physical feedback:** many systems learn from simulators, while ENPIRE turns reset, rollout, verification, and code revision into a repeatable real-world loop.

The central open problem is no longer merely whether a model can propose a plausible action; it is whether the entire agent harness can ground decisions, recover safely, accumulate reliable knowledge, and improve under the latency and irreversibility of the physical world.

## Contributing

Contributions are welcome; see [CONTRIBUTING.md](CONTRIBUTING.md) for the inclusion criteria and row format.

## License

This repository is available under the [MIT License](LICENSE).
