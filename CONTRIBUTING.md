# Contributing

Thank you for helping keep Awesome Agentic Robotics accurate and useful. The list follows the taxonomy and coding rules of the survey *A Survey of Agentic Robotics: Toward Continual Self-Improvement*. The "Analyzed in the survey" tables mirror the paper. Please report errors in them as an issue instead of editing them. New papers go into the "More systems" tables or, for agent-directed improvement, into the I<sub>agent</sub> table.

## Scope

A paper is in scope when a foundation model (an LLM, VLM, MLLM, or FM-based coding agent) does at least one of the following:

- it makes or revises a decision that affects robot behavior in a goal-directed task;
- it takes part in a loop that persistently improves the system.

The system must be evaluated on a physical robot, or in an embodied simulator built on a physics engine or on 3D scans of real buildings.

Out of scope:

- perception-only use of FMs (detection, captioning, scene understanding, or 3D grounding with no decision that affects robot behavior);
- standalone vision-language-action models or end-to-end policies with no agent-level decision loop. A foundation policy is in scope when an FM planner or verifier steers it, or when its own experience drives its update;
- systems with no FM-mediated decision;
- purely digital agents (web, software, text-only worlds);
- dialogue or explanation where the FM does not decide robot actions.

Surveys go under **Related surveys**, and benchmarks for FM-based robot agents go under **Benchmarks**.

## Choosing the section

Code each paper by what the FM actually outputs or decides in the system as evaluated, not by how the paper describes it.

- **T (task orchestration):** the FM outputs a subgoal, plan, skill, tool or API call, or semantic target (an object or place, by name or ID) that other modules turn into geometry.
- **M (motion/action generation):** the FM outputs geometric or control information. Examples are actions or a chosen action candidate, poses, waypoints, keypoints, constraints, cost maps, rewards optimized at execution time, metric skill parameters, or code that computes them. The actions of an FM policy also count.
- **I (improvement):** the system's own simulated or real experience changes a persistent behavior-generating artifact, such as weights, a training reward, program code, an executed skill, a symbolic planning model, or the agent's own prompts and tools. It is **I<sub>agent</sub>** if the FM makes at least one of these process decisions:
  - D1: which kind of artifact to change;
  - D2: what evidence to collect;
  - D3: which tests or experiments to run;
  - D4: how the update procedure works.

  Otherwise it is **I<sub>fixed</sub>**.

Boundary rules:

1. Classify the FM by the decision its output determines. If the FM scores candidates and a fixed rule (an argmax or a threshold) picks one, the FM makes that decision. An FM that only estimates scene state, object properties, intent, or success for a separate planner adds no locus.
2. An FM-generated objective or constraint that a motion solver optimizes is M. An FM-generated symbolic or formal specification that a planner solves is T.
3. Stored trajectories, corrections, or lessons that are only retrieved into later FM context are memory, not improvement.
4. FM-generated tasks, data, rewards, or designs count as improvement only when the system's own experience drives the update.

Then place the paper:

- I<sub>agent</sub>: the table under **Agent-directed improvement**.
- I<sub>fixed</sub>: **More systems** under **Fixed-procedure improvement**.
- Otherwise: **More systems** under **Task orchestration**, **Motion/action generation**, or **Task and motion**.

## Adding a paper

1. Read the primary paper and verify its title, first public release year, venue, and experimental setting.
2. Search the README for both the title and the method name to avoid duplicates.
3. Choose the section using the rules above.
4. Insert the row so that the table stays newest first.
5. Link directly to the paper, preferably an arXiv abstract page, official proceedings page, or DOI.
6. Run the validator:

       python3 scripts/validate_readme.py

Row format for the **More systems** tables:

    | YYYY | **Method** — [Paper title after the method name](https://paper-url) | Venue YEAR | Evidence | One factual sentence describing what the FM decides. |

Row format for the **Agent-directed improvement** table. Use ● when the FM decides, ○ when the designer fixes the decision, and – when only one artifact can change (D1 only):

    | YYYY | **Method** — [Paper title](https://paper-url) | Venue YEAR | Evidence | D1 | D2 | D3 | D4 | FM / Fixed rule / Human / NR | Yes / No | No / After update / Before promotion |

## Metadata conventions

- **Year:** the year of the first public version, normally arXiv v1 or an official online-publication date.
- **Venue:** the accepted archival venue when verified, otherwise arXiv. When a paper's status changes, update the venue but keep the original year.
- **Evidence:**
  - **Physical:** direct experiments on robot hardware.
  - **Sim + physical:** both simulated and hardware experiments.
  - **Sim-to-real:** a policy or artifact developed in simulation and transferred to hardware.
  - **Simulation:** no physical-robot experiments reported.
- **Held-out test:** the improved artifact is evaluated on tasks, configurations, or environments not used during improvement.
- **Regression test:** earlier tasks or capabilities are re-tested, either before a change is promoted or only after the update.

If evidence or status is ambiguous, use the conservative label and explain the uncertainty in the pull request.

## Quality bar

- Prefer primary sources and author project pages over secondary summaries.
- Keep descriptions neutral, specific, and limited to one sentence.
- Do not copy paper abstracts.
- Do not add citation counts, unverified "first" claims, or transient leaderboard results.
- Keep each paper in one section.
