# SCRIBE — Speaker Script

English · 18 slides · approximately 12–14 minutes at a measured pace.

The slide numbers below match scribe-emnlp-revised.pptx. Staged result reveals have separate short transitions.

## Slide 1 — Opening: Reusable Rubrics

Hello everyone. I’m Yuxuan Jiang from the University of Maryland, Baltimore County. This is joint work with my advisor, Francis Ferraro. Today I’ll present SCRIBE. Our core contribution is reusable rubrics: shared scoring criteria for reasoning skills that can be applied across different problems. Instead of creating a new rubric around each problem’s reference answer, we organize evaluation around what an intermediate reasoning step is trying to accomplish. I’ll show how we build these rubrics, how they guide reinforcement learning, and why reuse helps make rewards more consistent. The QR code links to our project and slides.

## Slide 2 — Unreliable LLM-as-a-Judge Reward

Let’s start with the problem. These two trajectories illustrate two ways an LLM judge can give a misleading reward. On the left, the model reaches the correct final answer through flawed reasoning, but receives a high reward. On the right, the strategy is sound, but a minor syntax error leads to a low reward. These are illustrative examples. The issue is that a correct final answer and a well-executed reasoning process are different things. Without explicit criteria for the behavior being evaluated, the judge can reward the wrong thing or penalize useful progress.

## Slide 3 — Why Reward Reliability Matters

That distinction matters during reinforcement learning. The reward is the signal that tells the policy which behaviors to repeat. If it overlooks reasoning flaws or over-penalizes small execution errors, training can reinforce the wrong behavior. The curve on the right illustrates the instability that motivates this work. Our response is to make the evaluation standard explicit and reusable, so that a step is judged against a clear intermediate objective.

## Slide 4 — From Final Answers to Intermediate Accomplishments

SCRIBE starts by identifying what each part of a trajectory is trying to accomplish. Consider a solution that factorizes a number, filters the factors, and then sums the remaining values. Each stage has a different objective and calls for a different skill. Rather than judging the entire trace with one vague standard, we evaluate whether each subgoal has been completed appropriately. This gives us a useful middle level between the final answer and individual tokens or lines of code.

## Slide 5 — Building Reusable Skill Rubrics

We build a library from reasoning trajectories. First, we extract subgoals, the skills they require, and the corresponding spans of reasoning. Then we group similar skills and distill each group into a skill prototype. A prototype describes when the skill applies, what successful execution looks like, and common mistakes with their scores. Crucially, it abstracts away the particular numbers and final answer. That is what makes the rubric reusable across instances.

## Slide 6 — Using the Rubrics During Training

During training, the policy generates a trajectory. A router identifies its subgoals and matches them to the appropriate prototypes. The judge then scores each subgoal using the retrieved rubric. We aggregate these scores into a process reward and use that reward for policy optimization with GRPO. The judge still interprets the reasoning, but it now has a shared checklist to follow. The prototype library provides a consistent reference for evaluating the same skill across different rollouts.

## Slide 7 — What a Prototype Looks Like

Here is a concrete prototype: drawing a conclusion from bounds. Suppose a solution establishes an upper bound and then claims that it is the maximum. The rubric asks whether the bound is attainable, whether the domain constraints are satisfied, and whether the relevant cases are covered. A rigorous conclusion receives the highest score. A correct-looking answer with an unproved tightness claim receives a lower score. These checks apply to many different optimization problems. We reuse the reasoning standard, without requiring a separate reference solution for each one.

## Slide 8 — The Instance-Level Rubric Comparison

A natural comparison is instance-level rubric generation. RaR uses a reference answer to construct criteria for an individual problem. This makes evaluation explicit, but the criteria depend on the reference and must be constructed for that instance. Our question is whether a shared skill-level standard can provide useful supervision without that dependency. The next results compare the two approaches on mathematical reasoning and tool use.

## Slide 9 — Reusable Rubrics Without Reference Answers

With SCRIBE, the rubric construction does not require reference answers. In this comparison, SCRIBE reaches 95.8 on MATH500, 63.3 on AIME25, and 51.3 on BFCL overall. It outperforms the reference-based RaR configuration shown here on all three measures. The important point is that removing the reference-answer dependency does not force us to abandon explicit criteria. We obtain those criteria from reusable reasoning skills instead.

## Slide 10 — Repeated Scoring: The Same Input

Now let’s examine reward consistency directly. In this illustrative example, the solution establishes that x times one minus x is at most one quarter, but does not demonstrate attainment. We hold the problem, trajectory, judge, and available rubric fixed and score the same input ten times. We then measure score agreement and variation. The table reports aggregate experimental results, not ten scores for this illustration. SCRIBE has the highest agreement and lowest standard deviation among these methods. A shared rubric makes repeated evaluation more stable.

## Slide 11 — Cross-Instance Scoring: The Same Behavior

The second test asks a different question: do similar behaviors receive similar scores across different problems? The two illustrative solutions here both jump from an upper bound to a maximum without showing attainment. Their numbers differ, but the reasoning gap is the same. In the experiment, we group matching subgoal behaviors across instances and compare their scores. SCRIBE reaches 86.8 percent agreement with a reward gap of 0.24. This is where reuse matters most: the same underlying behavior is assessed using the same standard.

## Slide 12 — Two Forms of Consistency

These results address two complementary concerns. Repeated scoring tests whether the reward changes when the input does not. Cross-instance scoring tests whether it changes unnecessarily when the problem changes but the behavior stays the same. SCRIBE improves both measures in these experiments. Together, they support the role of reusable skill rubrics as a more consistent source of process supervision.

## Slide 13 — Mathematical Reasoning Evaluation

We next ask whether these rewards translate into better task performance. We evaluate mathematical reasoning on MATH500 and AIME25, using both Qwen and LLaMA backbones. The base and standard PRM rows provide reference points. This lets us check whether the benefit extends beyond scoring consistency to the behavior of the trained policy.

## Slide 14 — Mathematical Reasoning Results

Adding SCRIBE improves both models on both benchmarks shown here. For Qwen, AIME25 improves from 43.3 for the base model to 63.3 with SCRIBE, compared with 51.7 using the standard PRM. For LLaMA, MATH500 improves from 40.8 to 63.4. The main message is that better-structured process supervision is accompanied by stronger final task performance across the two backbones.

## Slide 15 — Tool-Use Evaluation

We also evaluate tool use with BFCL V4. Here, success requires selecting an appropriate tool, supplying suitable arguments, and coordinating calls when the task involves multiple steps. The benchmark includes search, memory, single-turn, and multi-turn settings. These tasks provide a different test of our approach: reusable skills must support tool-using behavior as well as mathematical reasoning.

## Slide 16 — Tool-Use Baselines

This table places the tool-use results beside the math results. Looking first at the base model and standard PRM rows, process supervision already provides a useful improvement in several settings. The remaining question is whether conditioning the reward on reusable skill rubrics provides additional gains. I’ll reveal those rows next.

## Slide 17 — Tool-Use Results

SCRIBE improves BFCL overall performance for both backbones shown here. Qwen rises from 33.0 at the base model to 51.3 with SCRIBE, while LLaMA rises from 21.5 to 30.8. The gains also appear in the single-turn and multi-turn results. Together with the math evaluation, these results suggest that reusable skill-level criteria can provide effective supervision across different task types.

## Slide 18 — Takeaway: Reusable Rubrics

The takeaway is simple: reuse the evaluation standard, rather than building it around each reference answer. SCRIBE turns recurring reasoning skills into reusable rubrics, uses those rubrics to score intermediate behavior, and trains the policy with the resulting rewards. Our experiments show more consistent scoring and stronger performance on mathematical reasoning and tool use. The core contribution is reusable rubrics for process rewards. Thank you. The QR code links to the project and slides, and I’d be happy to take questions.
