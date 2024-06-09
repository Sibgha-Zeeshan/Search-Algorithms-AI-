from collections import deque
class MissionariesAndCannibalsProblem:
      
    """
    Defines the problem of missionaries and cannibals where the objective is to safely
    transport all missionaries and cannibals across a river without ever allowing the
    cannibals to outnumber the missionaries on either bank of the river.
    """

    def __init__(self):
        """
        Initializes the problem with an initial state where all missionaries and cannibals
        are on the left bank of the river and the boat is also on the left bank.
        """
        self.initial_state = (3, 3, 0, 0, 0)  # Initial state (M, C on left, boat, M, C on right)
        self.goal_state = (0, 0, 1, 3, 3)  # Goal state (all on right side)

  
    def is_valid_state(self, state):
        ml, cl, boat, mr, cr = state

    # Check for negative numbers of missionaries or cannibals
        if ml < 0 or cl < 0 or mr < 0 or cr < 0:
         return False

    # Check the balance of missionaries and cannibals on each side
        if (ml > 0 and ml < cl) or (mr > 0 and mr < cr):
           return False

    # Check the totals match the initial configuration
        if ml + mr != 3 or cl + cr != 3:
          return False

        return True


    def get_successors(self, state):
        """
        Generates a list of successor states from the current state along with the move that
        resulted in each successor state.

        Parameters:
            state (tuple): The current state from which successors are to be generated.

        Returns:
            list of tuples: A list of tuples where each tuple contains a successor state
                            and the move that resulted in it.
        """
        # (Implementation here)
        ml , cl , boat , mr , cr = state 
        successors = []
        moves = [(2,0),(0,2),(1,1),(1,0),(0,1)]
      

        for m,c in moves:
            # if boat is on left:
            if boat == 0:
                new_state =(ml-m , cl-c, 1, mr+m, cr+c)
            elif boat == 1:
                new_state =(ml+m , cl+c, 0, mr-m, cr-c)

            if self.is_valid_state(new_state) == True:
                successors.append(new_state)

        return successors

    def bfs(self):
        """
        Performs a breadth-first search to find a solution to the problem from the initial state.

        Returns:
            list of tuples: A list of tuples representing the path from the initial state to the
                            goal state, including each intermediate state and the move that
                            resulted in it.
        """
        # (Implementation here)
        """"
        initializes the queue with the initial state and sets up the visited set and 
        parent dictionary to keep track of the explored nodes and the path, respectively
        """
        queue1 = deque([self.initial_state])
        visited = set()
        parent = {self.initial_state:None}

        while queue1:
            current_state = queue1.popleft()
        # base case if we find goal state already in the start
            if current_state == self.goal_state:
                return self.reconstruct_path(current_state,parent)
        
            visited.add(current_state)

        # get successors of current state
            successors = self.get_successors(current_state)

            # For each valid successor of the current state, if the successor
            # is not in the visited set or parent dictionary, it is added to the queue
            # and the parent dictionary is updated to keep track of the path

            for successor in successors:
                if successor not in visited and successor not in parent:
                   queue1.append(successor)
                   parent[successor] = current_state


       
            
        # If the goal state is not found and the queue is exhausted, the function returns None
        return None


    def reconstruct_path(self, state, parent):
        """
        Reconstructs the path to the goal state from a given state by tracing back through the
        parent pointers.

        Parameters:
            state (tuple): The goal state from which to trace back the path.
            parent (tuple): The parent state and move leading to the goal state.
            move (tuple): The move that resulted in the goal state.

        Returns:
            list of tuples: A list of tuples representing the path from the initial state to the
                            goal state, including each intermediate state and the move that
                            resulted in it.
        """
        # (Implementation here)
        path = []
        current_state = state 

        while current_state is not None:
            path.append(current_state)
            current_state = parent[current_state]

        path.reverse()
        return path

object1 = MissionariesAndCannibalsProblem()
solution = object1.bfs()

if solution :
    print('solution found')
    for state in solution:
        print(f'state : {state}')
else:
    print('solution not found')