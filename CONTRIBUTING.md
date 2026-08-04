# Contributing

Thank you for helping keep Awesome Agentic Robotics accurate and useful.

## Inclusion criteria

A paper should make an LLM, VLM, MLLM, or coding agent an explicit part of a robot control, learning, evaluation, or development loop. Eligible contributions include planning, tool use, executable program synthesis, reflection, memory, skill discovery, autonomous improvement, multi-agent coordination, robot-agent infrastructure, and focused empirical evaluation.

Please do not add a paper solely because it uses a foundation model. Pure end-to-end VLA models, conventional imitation or reinforcement learning, and perception-only methods are outside scope unless an explicit agent loop is a central contribution.

Physical-robot evidence is preferred, but an influential simulation-only precursor or benchmark is welcome when its setting is labeled accurately.

## Adding a paper

1. Read the primary paper and verify its title, first public release month, venue, and experimental setting.
2. Search the README for both the title and method name to avoid duplicates.
3. Choose the category matching the paper's primary agentic contribution.
4. Insert the row in reverse chronological order.
5. Link directly to the paper, preferably an arXiv abstract page, official proceedings page, or DOI.
6. Write one factual sentence explaining what the agent does, not a performance claim or promotional summary.
7. Run the validator:

       python3 scripts/validate_readme.py

Use this row shape:

    | YYYY-MM | **Method** — [Full paper title](https://paper-url) | Venue YEAR | Evidence | One factual sentence describing the agentic mechanism. |

## Metadata conventions

- **Date:** earliest verifiable public release month, normally arXiv v1 or an official online-publication date.
- **Venue:** accepted archival venue when verified; otherwise use arXiv.
- **Physical:** direct experiments on robot hardware.
- **Sim + physical:** both simulated and hardware experiments.
- **Sim-to-real:** a policy or artifact developed in simulation and transferred to hardware.
- **Simulation:** no physical-robot evidence reported in the paper.
- **Review:** survey, review, or perspective rather than a new robot method.

When a paper's status changes, update the venue but retain the original release date. If evidence or status is ambiguous, use the conservative label and explain the uncertainty in the pull request.

## Quality bar

- Prefer primary sources and author project pages over secondary summaries.
- Keep descriptions neutral, specific, and limited to one sentence.
- Do not copy paper abstracts.
- Do not add citation counts, unverified “first” claims, or transient leaderboard results.
- Keep each paper in one primary category and mention cross-category relationships in the pull request when useful.
