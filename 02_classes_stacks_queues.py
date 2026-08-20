"""
Lesson 2: classes — taught by building your first two data structures.

A class is a blueprint for making objects that bundle DATA (attributes) with
BEHAVIOR (methods) that acts on that data. This is exactly the pattern behind
QuadTree in geo.py and Driver/Trip in models.py from the uber-geo-system
project — you're about to learn the mechanics those were built from.

How to use this file: same as lesson 1 — fill in each TODO, run the file,
fix whatever [FAIL] tells you, repeat.
"""


# ============================================================
# SECTION 1 — class basics: __init__, self, methods
# ============================================================
# `class Name:` defines a blueprint. `__init__` runs once, when you create a
# new object (`Counter()`), and sets up its starting data. `self` is just
# "the specific object this method was called on" — every method takes it
# as its first parameter, and you never pass it yourself; Python does.

# EXAMPLE (already correct — read it, then run this file to see it in action):
class Counter:
    def __init__(self):
        self.count = 0  # every Counter starts at 0

    def increment(self):
        self.count = self.count + 1

    def value(self):
        return self.count


c = Counter()
c.increment()
c.increment()
print(f"Counter is at {c.value()}")  # Counter is at 2


class Point:
    def __init__(self, x: float, y: float):
        # TODO: store x and y on self, same way Counter stores self.count above.
        self.x = x
        self.y = y
        pass

    def distance_to(self, other: "Point") -> float:
        """TODO: return the straight-line distance between self and other.
        Formula: sqrt((x2-x1)^2 + (y2-y1)^2). In Python, `** 0.5` is square root,
        e.g. `9 ** 0.5` is 3.0. No import needed.
        """
        
        return ((self.x-other.x)**2 + (self.y-other.y)**2) **0.5 # replace this


# ============================================================
# SECTION 2 — Stack (LIFO: Last In, First Out)
# ============================================================
# Think: a stack of plates. You can only add ("push") or remove ("pop") from
# the TOP. The last plate you put on is the first one you take off.
#
# We build it on top of a plain Python list, using:
#   .append(x)  -> adds x to the END of the list   (this is our "top")
#   .pop()      -> removes and returns the LAST item of the list
#   list[-1]    -> "peek" at the last item without removing it

class Stack:
    def __init__(self):
        self.items: list = []

    def push(self, item) -> None:
        """TODO: add item to the top of the stack."""
        
        self.items.append(item)
        

    def pop(self):
        """TODO: remove and return the top item."""
        return self.items.pop()
        

    def peek(self):
        """TODO: return the top item WITHOUT removing it."""
       	return self.items[-1]

    def is_empty(self) -> bool:
        """TODO: return True if the stack has no items, else False.
        Hint: an empty list is "falsy" — `len(self.items) == 0` works fine.
        """
        
        return len(self.items) == 0

    def size(self) -> int:
        """TODO: return how many items are in the stack."""
        return len(self.items)


# ============================================================
# SECTION 3 — Queue (FIFO: First In, First Out)
# ============================================================
# Think: a line at a coffee shop. Whoever got in line FIRST gets served
# first. New people join at the BACK; people leave from the FRONT.
#
#   .append(x)     -> adds x to the end (back of the line)
#   .pop(0)        -> removes and returns the FIRST item (front of the line)
#
# Aside, for later: `.pop(0)` has to shift every remaining item down by one,
# so it's O(n) — slow for a big queue. Python's `collections.deque` avoids
# this and does it in O(1). You don't need that yet; just know it's coming
# up when we cover Big-O.

class Queue:
    def __init__(self):
        self.items: list = []

    def enqueue(self, item) -> None:
        self.items.append(item)

    def dequeue(self):
        first = self.items.pop(0)
        return first

    def is_empty(self) -> bool:
        """TODO: same idea as Stack.is_empty() above."""
        return len(self.items) ==0

    def size(self) -> int:
        """TODO: same idea as Stack.size() above."""
        return len(self.items)


# ============================================================
# Self-check — do not edit below this line.
# ============================================================

def _check(label: str, condition: bool, hint: str) -> None:
    status = "PASS" if condition else "FAIL"
    print(f"[{status}] {label}" + ("" if condition else f"  <-- {hint}"))
    if not condition:
        raise AssertionError(f"{label} is not correct yet. {hint}")


if __name__ == "__main__":
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    _check(
        "Point stores x and y",
        p1.x == 0 and p1.y == 0 and p2.x == 3 and p2.y == 4,
        "In __init__, set self.x = x and self.y = y.",
    )
    _check(
        "Point.distance_to",
        p1.distance_to(p2) == 5.0,
        "sqrt((x2-x1)**2 + (y2-y1)**2) -> ((other.x - self.x)**2 + (other.y - self.y)**2) ** 0.5",
    )

    s = Stack()
    _check("new Stack is empty", s.is_empty() is True, "is_empty should return True when self.items is empty.")
    s.push(1)
    s.push(2)
    s.push(3)
    _check("Stack.size after 3 pushes", s.size() == 3, "size should return len(self.items).")
    _check("Stack.peek sees the top", s.peek() == 3, "peek should return self.items[-1] without removing it.")
    _check("Stack.peek doesn't remove", s.size() == 3, "peek must not modify self.items — only look at it.")
    popped = s.pop()
    _check("Stack.pop returns the top", popped == 3, "pop should remove and return self.items[-1] (or use .pop()).")
    _check("Stack.pop removes it", s.size() == 2, "after pop(), size should have gone down by 1.")
    _check("Stack LIFO order", s.pop() == 2 and s.pop() == 1, "the last item pushed should be the first one popped.")
    _check("Stack empty again", s.is_empty() is True, "after popping everything, is_empty() should be True again.")

    q = Queue()
    _check("new Queue is empty", q.is_empty() is True, "is_empty should return True when self.items is empty.")
    q.enqueue("a")
    q.enqueue("b")
    q.enqueue("c")
    _check("Queue.size after 3 enqueues", q.size() == 3, "size should return len(self.items).")
    dequeued = q.dequeue()
    _check("Queue.dequeue returns the FRONT item", dequeued == "a", "dequeue should remove and return self.items[0], the first one in.")
    _check("Queue FIFO order", q.dequeue() == "b" and q.dequeue() == "c", "items should come out in the same order they went in.")
    _check("Queue empty again", q.is_empty() is True, "after dequeuing everything, is_empty() should be True again.")

    print("\nAll checks passed.")
