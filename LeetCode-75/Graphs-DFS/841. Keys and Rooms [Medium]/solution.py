class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        #         AFTER THOUGHT: Could have used a bolean array to save space and used the same amount of lookup time
#       Create a hashmap of all the keys we have for all rooms expect for 0
        self.haveKey = {0: True}
        for i in range(1, len(rooms)):
            self.haveKey[i] = False
            
        def getKeys(room):
            for key in room:
                if self.haveKey[key] == False:
                    self.haveKey[key] = True
                    getKeys(rooms[key])
        
        # Original brute force idea
# #       Iterate through every room
#         for i in range(len(rooms)):
#             room = rooms[i]

# #           Check if we have the key to enter this room
#             if self.haveKey[i] == True:

# #               Collect every key in the room
#                 for j in room:
#                     self.haveKey[j] = True
            
        getKeys(rooms[0])
        # for v in values(self.haveKey):
        for k in self.haveKey:
            if self.haveKey[k] == False:
                return False
        # print(self.haveKey)
        return True


# Submission:
# Time: 63ms - 72.51%
# Space: 17mb - 62.24%
# Runtime: