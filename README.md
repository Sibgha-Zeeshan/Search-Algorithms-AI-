# Search-Algorithms-AI-
This repository contains solutions to common problems using search algorithms, created for an Artificial Intelligence course.

# Missionaries and Cannibals
There are 3 missionaries, 3 cannibals, and 1 boat that can carry up to two people on one side of a river.
• Goal: Move all the missionaries and cannibals across the river.
• Constraint: Missionaries can never be outnumbered by cannibals on either side of river, or else the missionaries are killed.
• State: configuration of missionaries and cannibals and boat on each side of river.
• Operators: Move boat containing some set of occupants across the river (in either direction) to the other side.

One possible solution: The filled circles represent missionaries. The non-filled circles - cannibals.
![235-missionaries-and-cannibals-solution](https://github.com/Sibgha-Zeeshan/Search-Algorithms-AI-/assets/132210204/89673f49-c7a0-4405-a716-9c55c8e0e75e)

# Goal State by Breadth First Search Approach:
 BFS algorithm explores all possible states level by level until the goal state is reached or all states are exhausted.

