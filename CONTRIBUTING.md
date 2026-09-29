# Contributing

Welcome. This repository exists so that people can make their first ever open
source contribution, so this guide assumes you have never done it before. If you
have, skip to [The workflow](#the-workflow).

---

## The one-paragraph version

Claim an issue by commenting `/claim`. It names one file in
`python-open-source-challenge/`. That file is a small Python program that is
broken on purpose. Fix it — minimally, following the `# TODO:` comments — until
running it prints `All checks passed!`. Open a pull request that says
`Closes #<number>`. Done.

---

## What you need

Python 3. That is the entire list.

```bash
python3 --version
```

No `pip install`, no virtual environment, no editor requirements. If that command
prints a version number, you are ready.

---

## The workflow

### 1. Claim an issue

Browse the [open issues](../../issues) and comment **`/claim`** on one that looks
interesting. A bot assigns it to you within seconds and adds `status: claimed`.

**Only claim what you will actually work on.** You can hold two issues at a time.
If you go quiet for five days the bot releases your claim so somebody else can
take it — no hard feelings, just come back and claim another.

If an issue is already assigned, pick a different one. There are ninety.

### 2. Fork and clone

Click **Fork** at the top of this page, then:

```bash
git clone https://github.com/<your-username>/Repository-1.git
cd Repository-1
```

### 3. Make a branch

Never work on `main`. Name the branch after your issue:

```bash
git checkout -b fix/issue-42
```

| Prefix | Use it for |
|---|---|
| `fix/` | Repairing one of the ninety programs — almost always this one |
| `docs/` | README, CONTRIBUTING, comments |
| `ci/` | Workflows |

### 4. Fix the file

Open the one file your issue names. Run it first, so you can see what failing
looks like:

```bash
python3 python-open-source-challenge/issue-42.py
```

You will get an `AssertionError`. Read it — it tells you the input that was
given, what the code returned, and what it should have returned.

Now work through the `# TODO:` comments. Each one sits next to something that is
wrong or missing. They are clues, not answers.

Three rules, and they matter:

- **Do not rewrite the program from scratch.** Reading somebody else's code and
  making a small careful change is the skill being taught here. Starting over
  skips the lesson.
- **Do not edit `check_solution()`.** That is the marking scheme. Changing the
  test so it agrees with your code is not a fix, and it will be spotted in review.
- **Do not delete the `# TODO:` comments** unless the thing they describe is
  genuinely done. If you fixed it, removing the comment is correct and welcome.

### 5. Check it

```bash
python3 python-open-source-challenge/issue-42.py
```

You are finished when it prints:

```
All checks passed!
```

Nothing else counts as done.

### 6. Commit

```bash
git add python-open-source-challenge/issue-42.py
git commit -m "fix: correct the department average calculation in issue 42"
```

Write commit messages as `<type>: <what changed>`. Use `fix`, `docs`, `test`,
`ci`, `refactor` or `chore`.

### 7. Push and open a pull request

```bash
git push -u origin fix/issue-42
```

GitHub will offer you a **Compare & pull request** button. Fill in the template
and make sure the description contains:

```
Closes #42
```

That line is what links your work to the issue and closes it automatically when
you are merged. Without it a maintainer has to close the issue by hand, which is
how issues get forgotten.

### 8. Review

A maintainer will read it. They may ask for changes — that is normal and is not a
criticism. Push more commits to the same branch and the pull request updates
itself.

---

## What the automatic check does

When you open a pull request, a robot runs **only the file or files you changed**
and requires each to print `All checks passed!`.

It deliberately does not run the other eighty-nine. Those are still broken, by
design, and they are not your problem.

If the check goes red, open the log. It prints the same error you would see on
your own machine, and the failing `assert` names the exact input and expected
result. You can always reproduce it in one line:

```bash
python3 python-open-source-challenge/issue-42.py
```

---

## Using AI tools

You may use ChatGPT, GitHub Copilot, or anything else.

What you may not do is open a pull request you cannot explain. You are
responsible for understanding the change, running it yourself, and answering
questions about it in review. That is not a rule against AI — it is the whole
reason this repository exists.

---

## What gets rejected

So that nobody wastes an afternoon:

| Rejected | Why |
|---|---|
| The program rewritten from scratch | Skips the actual exercise |
| `check_solution()` edited so the test agrees with the code | Changing the marking scheme is not a fix |
| Whitespace-only or comment-only changes to game files | No substance |
| Several unrelated issues in one pull request | Unreviewable. One issue, one pull request |
| A pull request with no `Closes #<number>` | Cannot be traced to an issue |
| Work on an issue claimed by somebody else | Somebody else got there first |

If your pull request is closed for one of these, it is not personal. Claim
another issue and have another go.

---

## Getting unstuck

- **Read `check_solution()` first.** The `assert` lines describe the expected
  behaviour more precisely than the sentence at the top of the file.
- **Run the file constantly.** After every small change. It takes half a second.
- **Add `print()` statements.** Put one inside the loop to see what the code
  actually does versus what you assumed.
- **Still stuck?** Comment on your issue and say what you have tried. Asking is
  not failing — a good question is itself a contribution.

---

## Code of conduct

By taking part you agree to the [Code of Conduct](CODE_OF_CONDUCT.md). Be kind to
people who are learning. Everybody here is new at something.
