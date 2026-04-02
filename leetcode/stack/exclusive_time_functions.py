class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        lastTimestamp = -1
        res = [0] * n
        callStack = []

        for log in logs:
            info = log.split(":")
            id = int(info[0]) 
            action = info[1]
            timeStamp = int(info[2])

            if (action != "start"):
                timeStamp += 1

            if (len(callStack) != 0):
                latestId = callStack[-1]
                res[latestId] += timeStamp - lastTimestamp
  
            if (action == "start"):
                callStack.append(id)
            else:
                callStack.pop()
            
            lastTimestamp = timeStamp
        return res

