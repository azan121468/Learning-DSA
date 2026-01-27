from sample import *

def canFinish(numCourses: int, prerequisites: list) -> bool:
    UNVISITED, VISITING, VISITED = 0, 1, 2
    premap = {i: [] for i in range(numCourses)}

    # prerequisites = to_take, required 
    for to_take, required in prerequisites:
        premap[to_take].append(required)
    
    # initialize all course as unvisited at start
    state = [UNVISITED] * numCourses

    def dfs(course):
        if state[course] == VISITING:  #cycle detected as we are revisiting a node which is already in visiting state
            return False
        
        if state[course] == VISITED:   #this course is already completed so we can complete the courses requiring this course
            return True

        state[course] = VISITING

        for c in premap[course]:
            if not dfs(c):
                return False

        state[course] = VISITED

        return True
    
    for c in range(numCourses):  #loop through every course and check if it can be completed.
        if not dfs(c):
            return False
    
    return True

ans = canFinish(*input1)
print(ans)
ans = canFinish(*input2)
print(ans)