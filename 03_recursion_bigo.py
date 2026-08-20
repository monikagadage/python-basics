"""
Lesson 3: recursion, and Big-O intuition you can actually SEE, not just read about.

How to use this file: same as lessons 1-2 — fill in each TODO, run the file,
fix whatever [FAIL] tells you, repeat.
"""

import time


# ============================================================
# SECTION 1 — recursion basics
# ============================================================
# A recursive function calls ITSELF, on a smaller version of the problem,
# until it hits a BASE CASE simple enough to answer directly without
# recursing further. Every recursive function needs both parts, or it
# never stops (Python will eventually crash with RecursionError).
#
#   base case:      the smallest input, answered directly, no recursion.
#   recursive case:  "solve a smaller piece, then combine it with this one."

# EXAMPLE (already correct — read it):
def factorial(n: int) -> int:
    if n <= 1:          # base case: factorial(0) and factorial(1) are both 1
        return 1
    return n * factorial(n - 1)   # recursive case: n * (factorial of everything smaller)


print(f"factorial(5) = {factorial(5)}")  # 5*4*3*2*1 = 120


def sum_list(items: list[int]) -> int:
    """TODO: return the sum of all numbers in items, recursively (no sum() or loops!).
    Base case: an empty list sums to 0.
    Recursive case: items[0] + (the sum of everything after it, i.e. items[1:]).
    """
    if len(items) == 0:
        return 0
    
    return items[0] + sum_list(items[1:])  # replace this


def power(base: int, exp: int) -> int:
    """TODO: return base ** exp, recursively (no ** or loops!).
    Base case: anything to the power 0 is 1.
    Recursive case: base * (base raised to one smaller exponent).
    
    """
    if exp == 0:
    	return 1
    
    return base * power(base , exp-1) # replace this


# ============================================================
# SECTION 2 — when recursion gets slow: naive Fibonacci
# ============================================================
# The Fibonacci sequence: each number is the sum of the two before it.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
#
# The obviously-correct recursive version:
#
#   def fib(n):
#       if n <= 1: return n
#       return fib(n - 1) + fib(n - 2)
#
# ...is CORRECT but wastefully slow, because it recomputes the same values
# over and over. fib(5) calls fib(3) — but so does fib(4), separately, from
# scratch. The tree of calls doubles in size for every step you go up, so
# this is O(2^n): fib(30) alone makes over a million redundant calls.
#
# The fix — MEMOIZATION — is simple: remember (cache) every answer you've
# already computed, in a dict, and check the cache before recomputing.

def fib_memo(n: int, cache: dict[int, int] | None = None) -> int:
    """TODO: like the naive fib() above, but check `cache` first and store
    every result you compute, so no value is ever calculated twice.

    Steps:
      1. If cache is None, create an empty dict: cache = {}
         (can't use {} as a default argument directly — that's a classic
         Python gotcha, which is why the parameter defaults to None instead)
      2. If n is already a key in cache, return cache[n] immediately.
      3. Base case: if n <= 1, return n.
      4. Otherwise: compute result = fib_memo(n - 1, cache) + fib_memo(n - 2, cache),
         store it in cache[n], and return it.
    """
    if n <=1:
    	return n
    if cache is None:
        	cache ={}
    if n in cache:
        return cache[n]
    
    result = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)
    cache[n] = result
    return result


# ============================================================
# SECTION 3 — Big-O, made visible
# ============================================================
# Big-O describes how an algorithm's work grows as input size (n) grows.
#   O(1)      constant    — same work no matter how big n is (dict lookup)
#   O(log n)  logarithmic — work barely grows as n grows (binary search)
#   O(n)      linear      — work grows exactly with n (one loop over a list)
#   O(n^2)    quadratic   — work grows with n*n (a loop nested inside a loop)
#
# Below: two ways to check "does this list contain any duplicate?" — same
# correct answer, very different Big-O. You'll write both, then run a race
# between them further down to see the difference for yourself.

def has_duplicate_slow(items: list[int]) -> bool:
    """TODO: O(n^2) approach — for every item, compare it against every OTHER
    item, looking for a match. Two nested loops.
    Hint:
      for i in range(len(items)):
          for j in range(len(items)):
              if i != j and items[i] == items[j]:
                  return True
      return False
    """
    for i in range(len(items)):
        for j in range(len(items)):
            if i!= j and items[i] == items[j]:
                return True
    return False  # replace this


def has_duplicate_fast(items: list[int]) -> bool:
    """TODO: O(n) approach — walk the list ONCE, remembering what you've seen
    in a set (sets have O(1) "have I seen this?" lookups, unlike scanning a list).
    Hint:
      seen = set()
      for item in items:
          if item in seen:
              return True
          seen.add(item)
      return False
    """
    seen = set()
    for item in items:
        if item in seen:
            return True
        seen.add(item)
    return False  # replace this


# ============================================================
# Self-check — do not edit below this line.
# ============================================================

def _check(label: str, condition: bool, hint: str) -> None:
    status = "PASS" if condition else "FAIL"
    print(f"[{status}] {label}" + ("" if condition else f"  <-- {hint}"))
    if not condition:
        raise AssertionError(f"{label} is not correct yet. {hint}")


if __name__ == "__main__":
    _check("sum_list([1,2,3,4])", sum_list([1, 2, 3, 4]) == 10, "items[0] + sum_list(items[1:]); empty list -> 0.")
    _check("sum_list([])", sum_list([]) == 0, "base case: an empty list sums to 0.")
    _check("power(2, 10)", power(2, 10) == 1024, "base * power(base, exp - 1); exponent 0 -> 1.")
    _check("power(5, 0)", power(5, 0) == 1, "base case: anything to the power 0 is 1.")

    _check("fib_memo(10)", fib_memo(10) == 55, "fib_memo(n-1, cache) + fib_memo(n-2, cache), base case n<=1 returns n.")
    _check("fib_memo(20)", fib_memo(20) == 6765, "same formula, just a bigger n — should still be instant if memoized.")

    _check(
        "has_duplicate_slow finds a duplicate",
        has_duplicate_slow([1, 2, 3, 2]) is True,
        "two nested loops, comparing every pair of positions.",
    )
    _check(
        "has_duplicate_slow on no duplicates",
        has_duplicate_slow([1, 2, 3]) is False,
        "make sure you return False after the loops if nothing matched.",
    )
    _check(
        "has_duplicate_fast finds a duplicate",
        has_duplicate_fast([1, 2, 3, 2]) is True,
        "walk the list once, tracking seen items in a set.",
    )
    _check(
        "has_duplicate_fast on no duplicates",
        has_duplicate_fast([1, 2, 3]) is False,
        "make sure you return False after the loop if nothing matched.",
    )

    print("\nAll checks passed.")
    print("\n--- Now watch the Big-O difference for yourself ---")
    big_list = list(range(2500))  # no duplicates -> both functions do their FULL worst-case work

    start = time.perf_counter()
    has_duplicate_slow(big_list)
    slow_seconds = time.perf_counter() - start

    start = time.perf_counter()
    has_duplicate_fast(big_list)
    fast_seconds = time.perf_counter() - start

    print(f"O(n^2) version on 2500 items: {slow_seconds:.4f}s")
    print(f"O(n)   version on 2500 items: {fast_seconds:.4f}s")
    print(f"...the O(n) version was about {slow_seconds / max(fast_seconds, 1e-9):.0f}x faster.")
    print("Same correct answer, same input size — the only difference is Big-O.")
