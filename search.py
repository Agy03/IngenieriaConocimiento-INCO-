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
    "*** YOUR CODE HERE ***"
    """Busca el camino al nodo objetivo usando búsqueda en profundidad (DFS)."""
   
    # Pila para la frontera de búsqueda
    fringe = Stack()
    # Conjunto de nodos visitados
    visited = set()
    
    # Cada elemento en la pila es una tupla (estado, camino hasta ese estado)
    fringe.push((problem.getStartState(), []))

    while not fringe.isEmpty():
        state, path = fringe.pop()  # Sacamos el nodo más reciente

        if problem.isGoalState(state):
            return path  # Si es la meta, retornamos el camino

        if state not in visited:
            visited.add(state)  # Marcamos el estado como visitado

            # Expandimos el nodo obteniendo sus sucesores
            for successor, action, stepCost in problem.getSuccessors(state):
                if successor not in visited:
                    new_path = path + [action]  # Guardamos el nuevo camino
                    fringe.push((successor, new_path))  # Lo añadimos a la pila

    return []  # Si no hay solución, devolvemos una lista vacía
    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    # Cola para la frontera de búsqueda
    fringe = Queue()
    # Conjunto de nodos visitados
    visited = set()
    
    # Cada elemento en la cola es una tupla (estado, camino hasta ese estado)
    fringe.push((problem.getStartState(), []))

    while not fringe.isEmpty():
        state, path = fringe.pop()  # Sacamos el nodo más antiguo

        if problem.isGoalState(state):
            return path  # Si es la meta, retornamos el camino

        if state not in visited:
            visited.add(state)  # Marcamos el estado como visitado

            # Expandimos el nodo obteniendo sus sucesores
            for successor, action, stepCost in problem.getSuccessors(state):
                if successor not in visited:
                    new_path = path + [action]  # Guardamos el nuevo camino
                    fringe.push((successor, new_path))  # Lo añadimos a la cola

    return []  # Si no hay solución, devolvemos una lista vacía
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    # Cola de prioridad para la frontera de búsqueda
    fringe = PriorityQueue()
    # Conjunto de nodos visitados con su menor costo acumulado
    visited = {}

    # Inicializar con el estado inicial, costo 0 y camino vacío
    fringe.push((problem.getStartState(), [], 0), 0)

    while not fringe.isEmpty():
        state, path, cost = fringe.pop()  # Sacamos el nodo con menor costo

        # Si encontramos la meta, devolvemos el camino
        if problem.isGoalState(state):
            return path

        # Si el estado no ha sido visitado o se encontró un menor costo, expandimos
        if state not in visited or cost < visited[state]:
            visited[state] = cost  # Guardamos el menor costo para este estado

            # Expandimos el nodo obteniendo sus sucesores
            for successor, action, stepCost in problem.getSuccessors(state):
                newCost = cost + stepCost  # Sumar el costo acumulado
                newPath = path + [action]  # Construir el nuevo camino
                fringe.push((successor, newPath, newCost), newCost)  # Agregar a la cola de prioridad

    return []  # Si no hay solución, devolvemos una lista vacía
    util.raiseNotDefined()

def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
