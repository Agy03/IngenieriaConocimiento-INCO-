# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from game import Directions
from typing import List
from util import Stack 
from util import Queue
from util import PriorityQueue

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()

def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
   
    fringe = Stack() # Stack for the search frontier
    visited = set() # Set of visitied nodes
    
    # Each element in the stack is a tuple (state, path to that state)
    fringe.push((problem.getStartState(), []))

    while not fringe.isEmpty():
        state, path = fringe.pop()  # Remove the most recent node

        if problem.isGoalState(state):
            return path  # If it is the goal, return the path

        if state not in visited:
            visited.add(state)  # Mark the state as visited

            # Expand the node by getting its successors
            for successor, action, stepCost in problem.getSuccessors(state):
                if successor not in visited:
                    new_path = path + [action]  # Store the new path
                    fringe.push((successor, new_path)) # Add it to the stack

    return []  # If no solution is found, return an empty list

def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""

    fringe = Queue()  # Queue to store states
    visited = set()  # Keep track of visited nodes
    fringe.push((problem.getStartState(), []))  # Start state

    while not fringe.isEmpty():
        state, path = fringe.pop()  # Take first added state (FIFO)

        if problem.isGoalState(state):
            return path  # Goal reached, return path

        if state not in visited:
            visited.add(state)  # Mark as visited

            for nextState, action, cost in problem.getSuccessors(state):
                if nextState not in visited:
                    fringe.push((nextState, path + [action]))  # Add new state

    return []  # No solution found

def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""

    fringe = PriorityQueue()  # Priority queue to store states
    visited = {}  # Dictionary to track the lowest cost to each state
    fringe.push((problem.getStartState(), [], 0), 0)  # Start state (position, path, cost)

    while not fringe.isEmpty():
        state, path, cost = fringe.pop()  # Take the state with the lowest cost

        if problem.isGoalState(state):
            return path  # Goal reached, return the path

        if state not in visited or cost < visited[state]:  # Expand if a cheaper path is found
            visited[state] = cost  # Store the lowest cost for this state

            for nextState, action, stepCost in problem.getSuccessors(state):
                newCost = cost + stepCost  # Update total cost
                newPath = path + [action]  # Update path
                fringe.push((nextState, newPath, newCost), newCost)  # Add new state with priority

    return []  # No solution found

def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """
    A* Search: Encuentra un camino desde el estado inicial hasta un estado meta usando:
      f(n) = g(n) + h(n), donde:
        - g(n) es el costo acumulado hasta n.
        - h(n) es una estimación admisible del costo restante.
    
    Esta función es genérica y se utiliza tanto para Q4 (problemas generales) como para Q6 
    (CornersProblem), dependiendo de la heurística que se le pase.
    """

    fringe = PriorityQueue()
    visited_states = {}  # Almacena el menor costo (g(n)) alcanzado para cada estado.
    start = problem.getStartState()
    start_cost = 0
    fringe.push((start, [], start_cost), start_cost + heuristic(start, problem))
    
    while not fringe.isEmpty():
        state, path, cost = fringe.pop()
        if problem.isGoalState(state):
            return path
        if state not in visited_states or cost < visited_states[state]:
            visited_states[state] = cost
            for nextState, action, stepCost in problem.getSuccessors(state):
                newCost = cost + stepCost
                newPath = path + [action]
                priority = newCost + heuristic(nextState, problem)
                fringe.push((nextState, newPath, newCost), priority)
    return []

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
