# Rotate Problem

Problem belonging to the post-classroom Mock Interview Question Repository.

## Problem Statement

Our goal is to write a function that will rotate a linked list by `k` places to the right.

For example,if we have the following input list:

a → b → c → d → e

After rotating by a `k` value of 2, we should get the following output list:

d → e → a → b → c

Notice that everything has been moved 2 spaces to the right. Anything that reaches the end of the list is wrapped back around to the beginning.

The value 'a' was originally in the 0th position (the head of the list), so when it is shifted by two, it ends up in the 2nd position.

The value 'e' was originally in the 4th position (the end of the list). When it is shifted two places, it wraps to the beginning of the list (position 0) and then moves one additional space, ending at the 1st position.

`k` is guaranteed to be positive.

Adapted from https://leetcode.com/problems/rotate-list/

## Examples

### Example 1

Rotating the following list

a → b → c → d → e

by 1 produces

e → a → b → c → d

### Example 2

Rotating the following list

a → b → c → d → e

by 2 produces

d → e → a → b → c

### Example 3

Rotating the following list

a → b → c → d → e

by 10 produces

a → b → c → d → e

### Example 4

Rotating the following list

55 → 8 → 2 → 99

by 6 produces

2 → 99 → 55 → 8

### Example 5

Rotating the following list

1 → 2

by 5 produces

2 → 1

## Notes for the Interviewer

### Clarifying Questions

#### Q: What should I do if there's only one node in the list or an empty list?

A: You can assume the list will have at least two nodes

#### Q: What should I do if invalid input is passed in?

A: You can assume that the input will be valid.

#### Q: What should I do if k is negative or zero?

A: You can assume that k will be a positive integer.

#### Q: What should I do if there's a cycle in the input list?

A: You can assume there will be no cycle.

### Hints

- If your candidate struggles with an initial algorithm, encourage them to walk through an example and describe how they would do it using only pen and paper.

- If your candidate struggles to determine how to handle cases where `k` is greater than the length of the list, encourage them to first solve the simpler case where `k` is less than the length of the list. This will make the first 2 test cases pass.

- If your candidate's result has a cycle in it, the assertions will fail. If your candidate runs into this, encourage them to print the list nodes one by one to determine where the cycle happens in their list. This is a tricky problem where it's very easy to accidentally make a cycle!

## Optional Bonus At-Home Challenges

To be attempted after completing the interview.

- What's the complexity of the first sample solution? What's the complexity of the second sample solution? Which has the better complexity? What would it look like to achieve the same optimal complexity with a normal Python list instead of a linked list? (VERY difficult)

- What would be the impact on complexity of the first solution if we didn't modulo `k` by the length of the list?

- Expand your solution so it can handle negative numbers. Negative numbers should cause the list to rotate in the opposite direction.

- What if the input were guaranteed to be one large cycle? How would your solution change? What impact would this have on complexity?
