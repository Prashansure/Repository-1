<h1 align="center">Python Open Source Challenge</h1>

<p align="center">Ninety small Python programs. Every one of them is broken on purpose.<br>
Fix one, open a pull request, and you have made your first open source contribution.</p>

<p align="center">
  <img src="https://img.shields.io/badge/issues-90-7057FF" alt="90 issues">
  <img src="https://img.shields.io/badge/python-3.8%2B-blue" alt="Python 3.8+">
  <img src="https://img.shields.io/badge/dependencies-none-1F883D" alt="No dependencies">
  <img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT">
</p>

---

## Start here

You need **Python 3** and nothing else. No `pip install`, no virtual environment,
no setup.

```bash
git clone https://github.com/Prashansure/Repository-1.git
cd Repository-1
python3 python-open-source-challenge/issue-01.py
```

You will see an `AssertionError`. **That is correct.** Every file in this
repository is deliberately incomplete — the error is the work waiting for you.

When you have repaired it, the same command prints:

```
All checks passed!
```

That is the whole game.

---

## Where to look, and what to ignore

A repository with ninety files in it looks like a lot the first time you open
one. Almost none of it is yours to worry about.

### 🎯 Your work goes here

| Folder | What is in it |
|---|---|
| **`python-open-source-challenge/`** | **All ninety programs, one per file.** `issue-01.py` through `issue-90.py`. The issue you claim tells you exactly which file is yours. You will only ever edit one of them. |

That is the entire list. There is no second folder you need.

### 📖 Worth reading, not editing

| File | Why |
|---|---|
| `CONTRIBUTING.md` | The workflow: claim an issue, branch, commit, open a pull request. |
| This README | You are here. |

### 🙈 Safe to ignore completely

You will never need to touch any of these, and nothing in your issue will
require it.

| Thing | What it actually is |
|---|---|
| `.github/` | Robots. The checks that run on your pull request, the issue templates, and the bot that assigns you an issue when you comment `/claim`. Maintainer territory. |
| `LICENSE`, `SECURITY.md`, `CODE_OF_CONDUCT.md` | Standard paperwork every open source project carries. |
| `__pycache__/`, `.pyc` files | Junk Python generates when it runs. Already ignored by Git. |

**The short version:** your issue names one file in
`python-open-source-challenge/`. Open it, fix it, and ignore everything else.

---

## How each file works

Every one of the ninety files has the same four parts:

```python
# ISSUE 42                     <- 1. which issue this file belongs to
#
# Problem:
# Write a program that ...     <- 2. what the program is supposed to do


def above_department_average(employees):
    ...
    # TODO: Check how each department's average is calculated.   <- 3. the clues
    ...


def check_solution():
    assert above_department_average(...) == ...                  <- 4. the marking scheme
    print("All checks passed!")
```

**The `# TODO:` comments are the point.** Each one sits next to something that is
wrong or missing. They do not tell you the answer — they tell you where to look
and what to think about. Work through them one at a time.

**`check_solution()` is the marking scheme.** It decides whether you are done.
Read it: the `assert` lines tell you exactly what the function is expected to
return for a given input, which is often clearer than the description at the top.

> **Do not rewrite the program from scratch, and do not edit `check_solution()`.**
> Reading code that somebody else wrote and making a careful, minimal change to
> it is the actual skill this repository is teaching. Deleting it and starting
> over skips the lesson, and changing the checks so they pass is not a fix.

---

## Pick an issue

1. Browse the [open issues](../../issues). Each one names its file and its difficulty.
2. Comment **`/claim`** on the one you want. A bot assigns it to you.
3. Only claimed, unassigned issues are fair game — if someone already has it, pick another.

| Label | What to expect |
|---|---|
| `difficulty: beginner` | One loop or one condition. If you know `if` and `for`, you can do these. |
| `difficulty: intermediate` | Several moving parts — grouping records, building dictionaries, returning more than one value. |
| `difficulty: advanced` | Recursion, or an algorithm you have to think about before you type. |

New to all of this? Sort by `difficulty: beginner` and pick anything that sounds
interesting. They are all self-contained, so there is no wrong choice.

---

## The workflow

1. Fork this repository.
2. Clone your fork.
3. Comment `/claim` on the issue you want.
4. Create a branch: `git checkout -b fix/issue-42`
5. Open the one file your issue names.
6. Read the existing code and find the `# TODO:` comments.
7. Repair it — minimally. Do not replace the program.
8. Run it and make the checks pass.
9. Commit, push, and open a pull request that says `Closes #42`.
10. A maintainer reviews it. Once approved, it is merged.

Full detail, including branch naming and commit messages, is in
[CONTRIBUTING.md](CONTRIBUTING.md).

---

## What the robot checks

When you open a pull request, an automatic check runs **only the files you
changed** and requires each one to print `All checks passed!`.

It does not run the other eighty-nine. Those are still broken, on purpose, and
that is not your problem.

If the check goes red, open it and read the log — it prints the same error you
would see on your own machine, so you can reproduce it locally with one command.

---

## A note on AI tools

You may use ChatGPT, GitHub Copilot, or any other AI tool.

You are responsible for understanding what it suggests, running it yourself, and
being able to explain it in review. A pull request whose author cannot explain
their own change will not be merged — not as a punishment, but because the entire
point of this repository is that you learned something.

---

## License

MIT — see [LICENSE](LICENSE).
