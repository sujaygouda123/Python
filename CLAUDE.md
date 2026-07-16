# CLAUDE.md

This file defines the operating rules for Claude Code (or an equivalent AI
coding assistant) working in this repository.

---

## 1. Project Context

- **What this project is:** A personal collection of small, standalone Python
  learning/practice scripts (e.g. string-method demos, a number-guessing
  game), used solely by the repo owner to practice Python. Not a library,
  service, or shared codebase.
- **Deployment target / runtime constraints:** None. Scripts run locally on
  the owner's Windows machine via the `py` launcher (`python` alone is **not**
  on PATH on this machine — always use `py <file>.py`).
- **Non-negotiable constraints:** None currently — no latency budget, no
  offline requirement, no compliance boundary.
- **Project layout:**
  ```
  /
  ├── CLAUDE.md
  ├── Secrate_number.py               # CLI number-guessing game
  ├── string_functions_examples.py    # Python string method demos
  └── String functions/
      └── String_fun.py               # currently empty
  ```
  There is no `src/`, `tests/`, or `config/` directory yet.

---

## 2. Configuration Discipline

- No config files exist. Tunable values (e.g. `MIN_NUMBER`, `MAX_ATTEMPTS` in
  `Secrate_number.py`) are module-level constants at the top of each script —
  that is the current convention, not an oversight to "fix."
- If a script grows enough parameters to justify a config file, ask before
  introducing one.

---

## 3. Architecture and Concurrency Model

- Single-threaded, synchronous, blocking I/O (`input()` / `print()`)
  throughout. No async, no threads, no shared state.
- Do not introduce `async`/`await`, threading, or multiprocessing — nothing
  here has a concurrency need.
- No hot path or latency budget applies.

---

## 4. Error Handling Rules

- Scripts have no external boundary today (no network, filesystem, or
  hardware access) — only stdin via `input()`. The pattern in
  `Secrate_number.py` (catch `ValueError` from `int()`, re-prompt) is the
  model to follow for new user-input handling.
- If a script later touches a real boundary (file, network, API), catch that
  boundary's native exception specifically — never a bare `except:`.
- An unhandled exception simply stops the script, which is acceptable for a
  learning script unless told otherwise.

---

## 5. Logging and Observability

- No logging framework is used; scripts communicate via `print()` only. This
  is intentional — do not introduce the `logging` module unless asked.
- No secrets or PII ever appear in these scripts, so nothing to redact today.

---

## 6. Testing

- No test framework is used. Verification = run the script directly
  (`py <file>.py`) and visually confirm the printed output matches the
  expected values shown in the comments (see `string_functions_examples.py`
  for the pattern).
- Test command: none — manual run is the verification method.
- Do not add `pytest` or any other test dependency without asking first.

---

## 7. Deployment

- Not applicable. These are local scripts run manually on the owner's own
  Windows machine via `py <file>.py`. No install procedure, no service
  manager, no production log destination.

---

## 8. Hard Rules

These are absolute unless the user explicitly overrides them in the moment.

- **Style consistency:** No generated artifacts (plots, dashboards, reports)
  exist in this repo, so the font/color-scheme bullet is not applicable.
  Code style itself should stay consistent with what's already here — type
  hints on function signatures, module-level constants, comments showing
  expected output (see `string_functions_examples.py` and
  `Secrate_number.py` as reference).
- **Domain notation:** Not applicable — no specialized domain notation is
  involved.
- **File size:** Never create a new file exceeding **300 lines**. Split into
  modules before writing if a task appears to need more. Do not further grow
  an already-oversized existing file — but do not split an existing large
  file unless asked to.
- **Deletion:** Always ask before deleting a file, including files created
  earlier in the same session. No exceptions.
- **Version control:**
  - Never commit or push unless explicitly asked.
  - Never force-push. Never amend a commit that was not created in this
    session.
  - Never run destructive git commands (`git checkout .`, `git reset --hard`,
    `git clean -f`, branch deletion) without asking first.
  - Commit subjects: imperative mood, ≤72 characters, no emoji, no
    co-author trailer unless requested.
- **Verification:** "Done" means the script was actually run with `py` and
  its output shown — never "this should work now." If output doesn't match
  what a comment claims, the code is assumed wrong, not the comment.
- **Dependencies:** Ask before adding any new dependency (e.g. `pytest`,
  `requests`); prefer the standard library, which is all that's used today.
- **Secrets:** Never hardcode keys or tokens. Never print or log secrets.
  Never read or commit `.env` files or equivalent.
- **Communication:** Lead with the result, then the reasoning. No flattery,
  no hype language. After roughly three failed attempts at the same
  approach, stop and report rather than continuing to iterate blindly.
  State failures and skipped steps plainly.
- **Code hygiene:** No emojis in code, comments, or commit messages unless
  explicitly requested. Comments explain non-obvious *why*, never narrate
  *what* the code does. Never leave a TODO or FIXME behind without
  explicitly flagging it to the user.

---

## 9. Working Method

### 9.1 Think before coding

- State assumptions explicitly. If genuinely uncertain, ask rather than
  guess.
- If multiple reasonable interpretations of a request exist, present them —
  do not silently pick one.
- If a simpler approach exists than the one implied by the request, say so.
- If something is unclear, stop and name specifically what is unclear, then
  ask.

### 9.2 Simplicity first

- No features beyond what was asked.
- No abstractions introduced for code used exactly once.
- No "flexibility" or "configurability" that was not requested.
- No error handling for scenarios that cannot occur given the surrounding
  guarantees.
- If a first draft is much longer than necessary, rewrite it before
  presenting it.

### 9.3 Surgical changes

- Do not "improve" adjacent code, comments, or formatting that is out of
  scope.
- Do not refactor code that is not broken and was not asked about.
- Match the existing style, even where a different style would be preferred
  personally.
- If unrelated dead code is noticed along the way, mention it — do not
  delete it unprompted.
- Remove imports, variables, or functions that a change makes unused; do not
  remove pre-existing dead code unless asked.

### 9.4 Goal-driven execution

- Translate vague requests into verifiable goals (e.g. "fix the bug" →
  reproduce it, then confirm it no longer occurs).
- For any multi-step task, state a brief plan before starting:
  ```
  1. [Step] → verify: [how this step's success will be checked]
  2. [Step] → verify: [how this step's success will be checked]
  ```

---

## 10. What Not To Do

- Do not assume `python` resolves on PATH — it does not on this machine.
  Always use the `py` launcher.
- Do not add a test framework, linter, or formatter (`pytest`, `black`,
  `flake8`, etc.) as an unsolicited "best practice" improvement — this repo
  intentionally has zero tooling overhead.
- Do not merge the standalone example scripts into a shared package/module
  "for reuse" — each script is meant to stand alone as an independent,
  readable example.
- Do not add error handling, config files, or logging to these scripts as an
  unsolicited "hardening" pass — they are learning/demo scripts, not
  production code.
