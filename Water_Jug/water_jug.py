class WaterJugProblem:
    def __init__(self, cap1, cap2, target):
        self.cap1 = cap1
        self.cap2 = cap2
        self.target = target
        self.initial_state = (0, 0)
        
    def is_goal(self, state):
        return state[0] == self.target or state[1] == self.target
        
    def get_successors(self, state):
        j1, j2 = state
        successors = []
        c1 = self.cap1
        c2 = self.cap2
        
        # Fill jug 1
        if j1 < c1: successors.append(("Fill Jug 1", (c1, j2)))
        # Fill jug 2
        if j2 < c2: successors.append(("Fill Jug 2", (j1, c2)))
        # Empty jug 1
        if j1 > 0: successors.append(("Empty Jug 1", (0, j2)))
        # Empty jug 2
        if j2 > 0: successors.append(("Empty Jug 2", (j1, 0)))
        
        # Pour jug 1 to jug 2
        if j1 > 0 and j2 < c2:
            amount = min(j1, c2 - j2)
            successors.append(("Pour J1 -> J2", (j1 - amount, j2 + amount)))
            
        # Pour jug 2 to jug 1
        if j2 > 0 and j1 < c1:
            amount = min(j2, c1 - j1)
            successors.append(("Pour J2 -> J1", (j1 + amount, j2 - amount)))
            
        return successors
