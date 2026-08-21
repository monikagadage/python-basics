# Python Basics — hands-on lessons

A separate, standalone place to practice Python fundamentals, independent of
the `uber-geo-system` project. Each lesson is a single runnable script: you
fill in small `TODO` pieces, run it, and it tells you exactly what's still
wrong.

## How to run a lesson

```bash
cd python-basics
python3 01_variables_functions_data.py
```

If something's wrong, you'll get a clear `AssertionError` pointing at which
exercise failed. Fix it, rerun, repeat. When it prints `All checks passed.`,
you're done with that lesson.

## Lessons

1. [`01_variables_functions_data.py`](01_variables_functions_data.py) —
   variables & f-strings, functions with type hints, lists, dicts, tuple
   unpacking. This is exactly the Python used in `geo.py`'s math functions.
2. [`02_classes_stacks_queues.py`](02_classes_stacks_queues.py) — classes,
   `__init__`/`self`, methods — taught by building your first two real data
   structures: a **Stack** (LIFO) and a **Queue** (FIFO).
3. [`03_recursion_bigo.py`](03_recursion_bigo.py) — recursion (base case +
   recursive case), memoization, and Big-O made visible: you write an O(n²)
   and an O(n) version of the same check and the file races them for you.
4. [`04_linked_lists.py`](04_linked_lists.py) — build a linked list from raw
   `Node` objects: `push_front`/`push_back`, `find`, and pointer-surgery
   `remove` (including the head and tail edge cases).

## Data structures & algorithms track

Track pivoted from "general Python" to DSA specifically, taught the same
hands-on way — each data structure/algorithm gets built as a class or
function you complete and self-check, not just read about. Planned order,
each depending on the last:

- ~~Classes basics~~ → **Stack & Queue** (lesson 2 — done)
- ~~Recursion + Big-O intuition~~ (lesson 3 — done)
- ~~Linked Lists~~ (lesson 4 — done)
- Binary Trees / BST (traversal, search)
- Sorting algorithms (bubble → merge/quick, and *why* the faster ones are faster)
- Binary search + searching in sorted structures
- Graphs (BFS/DFS) — ties back to the Uber project's spatial-index idea

Hash Maps was originally planned here but moved to the
[system-design-daily](../system-design-daily) repo (day 1) instead, alongside
the system-design context for *why* hash tables matter (caches, sharding,
indexes) — no point building it twice.

This is the DSA/coding-round leg of a
[15-day interview-prep sprint](../system-design-daily/README.md) that also
covers low-level design and system design in `system-design-daily`. Lessons
get built one at a time as you finish the previous one, not all upfront — so
this list is a map, not a promise of what exists yet.
