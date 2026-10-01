# Homepage figures

The homepage follows the camera-ready manuscript titled **SCRIBE: Learning Reusable Skill Rubrics for Process Reward Models**.

- `scribe-overview.png`: original introduction figure from the camera-ready LaTeX source (`latex/scribe_intro.png`).
- `skill-prototype.svg`: editable rendering of the compact **Bound-Based Conclusion & Synthesis** prototype in the Method section. Wording is shortened for display; the boundary-leak example and its score are preserved.
- `reward-consistency.png` / `.pdf`: plot of exact-agreement values from the repeated-evaluation and cross-instance-consistency tables, respectively labeled `tab:repeat_consistency` and `tab:cross_instance_consistency` in the manuscript.
- `plot_consistency.py`: standalone Matplotlib script to reproduce the plot. Run `python assets/plot_consistency.py` with Matplotlib and NumPy installed.

The plots use reported aggregate values, not new experiments. No uncertainty bars are added because the corresponding tables do not provide them.
