# UninformedSearch-Algorithms-AI-
This repository contains solutions to common problems using uninformed/blind search algorithms, created for an Artificial Intelligence course.

# Missionaries and Cannibals
There are 3 missionaries, 3 cannibals, and 1 boat that can carry up to two people on one side of a river.
• Goal: Move all the missionaries and cannibals across the river.
• Constraint: Missionaries can never be outnumbered by cannibals on either side of river, or else the missionaries are killed.
• State: configuration of missionaries and cannibals and boat on each side of river.
• Operators: Move boat containing some set of occupants across the river (in either direction) to the other side.

One possible solution: The filled circles represent missionaries. The non-filled circles - cannibals.

![235-missionaries-and-cannibals-solution](https://github.com/Sibgha-Zeeshan/Search-Algorithms-AI-/assets/132210204/89673f49-c7a0-4405-a716-9c55c8e0e75e)

**BFS** algorithm explores all possible states level by level until the goal state is reached or all states are exhausted.

**DFS** explores one branch of the state space tree as deeply as possible before backtracking. This can be more memory-efficient compared to breadth-first search (BFS), but it does not guarantee finding the shortest path to the goal. However, for the Missionaries and Cannibals problem, where there is no notion of edge costs, DFS is a suitable and efficient choice.

**Depth-Limited Search (DLS)** is a variation of Depth-First Search (DFS) that limits the depth of exploration to a specified limit. It recursively explores states up to this depth, backtracking if the limit is reached without finding the goal. DLS is useful when the depth of the solution is known or estimated, but may miss solutions beyond the specified depth.

**Iterative Deepening Search (IDS)** combines the benefits of both Depth-First Search (DFS) and Breadth-First Search (BFS). It repeatedly performs DLS with increasing depth limits, starting from zero and incrementing by one until the goal is found.

