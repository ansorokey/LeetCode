# Completely misunderstood the question, but blow works well for counting groups
# class Solution:
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         # Initialize a count and a collection of visited cities
#         count = 0
#         visited = {}
        
#         # Top and bottom bounds of matrix
#         xT, xB = 0, len(isConnected[0])
        
#         # left and right bounds of matrix
#         yL, yR = 0, len(isConnected)
        
#         def addNeighbors(x, y):
#             city = str(x) + 'x' + str(y)
#             if city not in visited:
#                 visited[city] = True
                
#                 # up
#                 if x-1 >= xT and isConnected[x-1][y] == 1:
#                     addNeighbors(x-1, y)
#                 # down
#                 if x+1 < xB and isConnected[x+1][y] == 1:
#                     addNeighbors(x+1, y)
#                 # left
#                 if y-1 >= yL and isConnected[x][y-1] == 1:
#                     addNeighbors(x, y-1)
#                 # right    
#                 if y+1 < yR and isConnected[x][y+1] == 1:
#                     addNeighbors(x, y+1)
            
            
        
#         # Iterate through the matrix
#         for i in range(len(isConnected)):
#             subArr = isConnected[i]
#             for j in range(len(subArr)):
#                 city = str(i) + 'x' + str(j)
#                 if city not in visited and isConnected[i][j] == 1:
#                     addNeighbors(i, j)
#                     count += 1
        
#         # Return the count
#         # print(visited)
#         return count


# Submission:
# Time:
# Space:
# Runtime:

# This runs terribly BUT IT RuNS BABY IT RUNS
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.count = 0
        self.visited = set()
        self.checked = [False for i in range(len(isConnected))]
        
        def check(city):
            for i in range(len(isConnected[city])):
                connection = isConnected[city][i]
                if connection == 1:
                    c1 = str(city) + 'x' + str(i)
                    c2 = str(i) + 'x' + str(city)
                    if c1 not in self.visited or c2 not in self.visited:
                        self.visited.add(c1)
                        self.visited.add(c2)
                        check(i)
            self.checked[city] = True
        
        for city in range(len(isConnected)):
            if self.checked[city] == False:
                check(city)
                self.count += 1
        
        return self.count

# Submission:
# Time: 610ms - 5.05%
# Space: 20.2mb - 7.81%
# Runtime: toooo much        