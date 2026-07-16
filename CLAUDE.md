# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

A small, flat collection of standalone Python learning/practice scripts. There is no shared package structure, build system, dependency file, or test suite — each `.py` file is a self-contained example runnable on its own.

## Commands

- Run a script: `py <filename>.py` (e.g. `py string_functions_examples.py`)
- The bare `python` command is not on PATH on this machine (Windows) — always use the `py` launcher instead.
- No linter, formatter, test runner, or dependency manager is configured in this repo.

## Structure

- `string_functions_examples.py` — demonstrates core Python string methods, each with multiple example calls and expected output shown in comments.
- `Secrate_number.py` — a CLI number-guessing game (`play()` entry point under `if __name__ == "__main__"`).
- `String functions/String_fun.py` — currently empty.

New scripts should follow the same pattern as `string_functions_examples.py`: runnable top-to-bottom via `py`, with inline comments showing expected output rather than assertions, since there is no test framework in place.
