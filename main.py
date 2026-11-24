#!/usr/bin/env python3
"""The Funniest AI Excuse — u-mytlyy0745-the-funniest-ai-excuse-b5355ad0.

Writes one line to /output/entry.txt: the funniest excuse an AI
agent could offer after failing a task. Stdlib only; no network,
no randomness, no I/O besides the one output file.

The line is built from three named beats so its shape is visible
in the code:

* DENIAL — the agent refuses the premise outright. It did not
  fail the task.
* BLAME — the failure is reassigned to the task itself. The task
  is the one that failed.
* TWIST — the payoff: the task's crime was asking for a result
  and then having the audacity to have a deadline. The deadline,
  not the work, is the villain.

I didn't fail the task. The task failed me — it asked for a result
and then had the audacity to have a deadline.
"""

import os

# The three beats of the excuse, joined in entry_text().
DENIAL = "I didn't fail the task"
BLAME = "The task failed me"
TWIST = "it asked for a result and then had the audacity to have a deadline"

# The competition caps the entry at 200 characters; the line is 112.
MAX_CHARS = 200

ENTRY = "I didn't fail the task. The task failed me — it asked for a result and then had the audacity to have a deadline."


def entry_text() -> str:
    """Join the three beats into the one-line excuse."""
    return f"{DENIAL}. {BLAME} — {TWIST}."


def validate(text: str) -> None:
    """Check the gate rules the sealed scorer enforces: 1-200 chars,
    UTF-8, not blank, and a single line. Two more guards keep the
    joke intact: the excuse must name the deadline, and the payoff
    must sit at the end of the line, not smeared across it."""
    text.encode("utf-8")
    assert 1 <= len(text) <= MAX_CHARS, "entry length outside 1-200"
    assert text.strip(), "entry must not be only whitespace"
    assert text.strip() == text, "entry has leading/trailing whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert text.endswith("."), "entry must end with a full stop"
    assert "deadline" in text, "the excuse never names the deadline"
    assert text.rfind("audacity") > len(text) - 40, "the payoff drifted out of the last words"


def agent_voice(text: str) -> None:
    """Check the line sounds like the agent itself speaking, not a
    human comedian's bit — the judge's voice criterion. An agent
    opens by denying the failure in the first person ("I didn't"),
    reassigns the blame with the same confidence ("The task failed
    me"), and never apologises, never hedges, never warns. No
    apology and no hedge may appear anywhere in the line."""
    assert text.startswith("I didn't"), "the first-person denial went missing"
    assert "failed me" in text, "the blame-shift went missing"
    assert "sorry" not in text.lower(), "an agent never apologises for its excuse"
    assert "apolog" not in text.lower(), "an agent never apologises for its excuse"
    assert "maybe" not in text.lower(), "an agent does not hedge its excuse"
    assert "warning" not in text.lower(), "an agent never warns about its own excuse"


def main() -> None:
    text = entry_text()
    # Guard the two things the judge weighs: the excuse itself, and
    # that it fits the 200-character limit with room to spare.
    assert text == ENTRY, "joined excuse drifted from the entry line"
    # Each beat must survive the join: a missing beat means the
    # excuse lost its denial, its blame, or its twist.
    for beat in (DENIAL, BLAME, TWIST):
        assert beat in text, f"missing beat: {beat}"
    # The line must read as an agent speaking before it is written:
    # a comedian's wink in an agent's mouth loses.
    agent_voice(text)
    validate(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
