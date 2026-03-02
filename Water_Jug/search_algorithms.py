import time
from collections import deque

class Node:
    def __init__(self, state, parent=None, action=None, depth=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = depth

    def path(self):
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

def bfs(problem):
    start_time = time.time()
    node = Node(problem.initial_state)
    if problem.is_goal(node.state):
        return node, time.time() - start_time, 0
    
    frontier = deque([node])
    explored = set()
    explored.add(node.state)
    
    nodes_explored = 0
    
    while frontier:
        node = frontier.popleft()
        nodes_explored += 1
        
        for action, child_state in problem.get_successors(node.state):
            if child_state not in explored:
                child_node = Node(child_state, node, action, node.depth + 1)
                if problem.is_goal(child_state):
                    return child_node, time.time() - start_time, nodes_explored
                frontier.append(child_node)
                explored.add(child_state)
                
    return None, time.time() - start_time, nodes_explored

def dfs(problem):
    start_time = time.time()
    frontier = [Node(problem.initial_state)]
    explored = set()
    nodes_explored = 0
    
    while frontier:
        node = frontier.pop()
        nodes_explored += 1
        
        if problem.is_goal(node.state):
            return node, time.time() - start_time, nodes_explored
            
        explored.add(node.state)
        
        for action, child_state in problem.get_successors(node.state):
            if child_state not in explored and all(n.state != child_state for n in frontier):
                child_node = Node(child_state, node, action, node.depth + 1)
                frontier.append(child_node)
                
    return None, time.time() - start_time, nodes_explored

def dls(problem, limit):
    start_time = time.time()
    nodes_explored = [0]
    
    def recursive_dls(node, limit, current_path_states):
        nodes_explored[0] += 1
        if problem.is_goal(node.state):
            return node
        elif limit == 0:
            return 'cutoff'
        else:
            cutoff_occurred = False
            for action, child_state in problem.get_successors(node.state):
                if child_state in current_path_states:
                    continue
                    
                child_node = Node(child_state, node, action, node.depth + 1)
                current_path_states.add(child_state)
                result = recursive_dls(child_node, limit - 1, current_path_states)
                current_path_states.remove(child_state)
                
                if result == 'cutoff':
                    cutoff_occurred = True
                elif result is not None:
                    return result
            return 'cutoff' if cutoff_occurred else None

    path_states = set([problem.initial_state])
    result = recursive_dls(Node(problem.initial_state), limit, path_states)
    return result, time.time() - start_time, nodes_explored[0]

def ids(problem, max_depth=50):
    start_time = time.time()
    total_nodes_explored = 0
    
    for depth in range(max_depth):
        result, _, nodes = dls(problem, depth)
        total_nodes_explored += nodes
        if result != 'cutoff' and result is not None:
            return result, time.time() - start_time, total_nodes_explored
            
    return None, time.time() - start_time, total_nodes_explored
