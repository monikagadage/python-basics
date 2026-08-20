"""
Lesson 4: Linked Lists — building a data structure out of raw pointers.

A Python list lives as one contiguous block of memory: item 0, item 1, item 2,
sitting right next to each other, so `my_list[500]` jumps straight there.

A linked list is different: instead of one block, it's a chain of small
objects (Nodes), each one holding a VALUE and a POINTER to the next node.
There's no "jump straight there" — to reach node 500 you have to walk the
chain from the start, one `.next` at a time. That trade-off (slower random
access, but O(1) insertion at the front, and no need to know the size up
front) is *why* this data structure exists.

How to use this file: same as lessons 1-3 — fill in each TODO, run the file,
fix whatever [FAIL] tells you, repeat.
"""


# ============================================================
# SECTION 1 — the Node: one value, one pointer
# ============================================================
# This is the entire building block. Nothing fancy — just data, plus a
# pointer to the next Node in the chain (or None, if it's the last one).

# EXAMPLE (already correct — read it, then run this file to see it in action):
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None  # points to the next Node, or None if this is the last


# Wiring three nodes together BY HAND, no LinkedList class yet — this is
# what push_front/push_back will automate for you below.
a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c
# chain is now: a -> b -> c -> None

current = a
values = []
while current is not None:
    values.append(current.value)
    current = current.next
print(f"walked the chain by hand: {values}")  # [1, 2, 3]


# ============================================================
# SECTION 2 — the LinkedList: wrapping the chain in a class
# ============================================================
# A LinkedList just needs to remember where the chain STARTS (self.head).
# Everything else — adding, searching, removing — means walking from there.

class LinkedList:
    def __init__(self):
        self.head: Node | None = None

    def to_list(self) -> list:
        """TODO: walk the chain from self.head to the end, collecting every
        node's .value into a normal Python list, and return it.
        Hint (same walk as the SECTION 1 example above, but building a list):
          result = []
          current = self.head
          while current is not None:
              result.append(current.value)
              current = current.next
          return result
        """
        return []  # replace this

    def push_front(self, value) -> None:
        """TODO: add a new node holding `value` at the FRONT of the chain.
        This is O(1) — no walking required, unlike push_back below.
        Steps:
          1. Create new_node = Node(value)
          2. Point it at the current front: new_node.next = self.head
          3. Make it the new front: self.head = new_node
        """
        pass

    def push_back(self, value) -> None:
        """TODO: add a new node holding `value` at the END of the chain.
        Unlike push_front, this is O(n) for a plain singly linked list —
        you have to walk all the way to the last node first, because nothing
        remembers where the end is (a real-world linked list often keeps a
        self.tail pointer to make this O(1) too — we're skipping that here to
        keep the exercise focused on chain-walking).

        Steps:
          1. new_node = Node(value)
          2. If the list is empty (self.head is None): self.head = new_node; return.
          3. Otherwise, walk from self.head until you find the node whose
             .next is None (the last node):
               current = self.head
               while current.next is not None:
                   current = current.next
          4. Attach the new node there: current.next = new_node
        """
        pass

    def find(self, value) -> bool:
        """TODO: return True if any node's .value equals `value`, else False.
        Same walk as to_list(), but checking instead of collecting.
        """
        return False  # replace this

    def remove(self, value) -> bool:
        """TODO: remove the FIRST node whose value equals `value`.
        Return True if something was removed, False if `value` wasn't found.

        Removing a node means making the node BEFORE it point past it —
        `prev.next = current.next` "skips over" current, unlinking it from
        the chain (Python then garbage-collects it, since nothing points to
        it anymore).

        Two cases:
          - The match is the HEAD: no "previous" node exists, so just move
            self.head to self.head.next.
          - The match is anywhere else: walk the chain keeping track of both
            the current node AND the one before it, until current.value
            matches, then rewire prev.next = current.next.

        Steps:
          if self.head is None:
              return False
          if self.head.value == value:
              self.head = self.head.next
              return True
          prev = self.head
          current = self.head.next
          while current is not None:
              if current.value == value:
                  prev.next = current.next
                  return True
              prev = current
              current = current.next
          return False
        """
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
    ll = LinkedList()
    _check("new LinkedList.to_list() is empty", ll.to_list() == [], "an empty chain (self.head is None) should give back [].")

    ll.push_front(3)
    ll.push_front(2)
    ll.push_front(1)
    _check("push_front three times", ll.to_list() == [1, 2, 3], "each push_front should land at the FRONT, so the last one pushed ends up first.")

    ll.push_back(4)
    _check("push_back adds to the end", ll.to_list() == [1, 2, 3, 4], "push_back should walk to the last node (.next is None) and attach there.")

    _check("find an existing value", ll.find(3) is True, "walk the chain; return True as soon as current.value == value.")
    _check("find a missing value", ll.find(99) is False, "if you walk off the end (current becomes None) without a match, return False.")

    removed_middle = ll.remove(2)
    _check("remove returns True when found", removed_middle is True, "remove should return True after successfully unlinking a node.")
    _check("remove from the middle", ll.to_list() == [1, 3, 4], "prev.next = current.next should skip over the removed node.")

    removed_missing = ll.remove(99)
    _check("remove returns False when not found", removed_missing is False, "if you walk off the end without a match, return False.")

    ll.remove(1)
    _check("remove the head", ll.to_list() == [3, 4], "removing the head means self.head = self.head.next (no 'prev' node exists for the head).")

    ll.remove(4)
    _check("remove the tail", ll.to_list() == [3], "the last node's prev.next = current.next (which is None) should work the same as any other removal.")

    print("\nAll checks passed.")
