from typing import List
import heapq

## Uso de lista encadeada para otimizar deleção
## Uso de minHeap para manter a minSum atualizada, sendo recuperada em O(1)
## Uso de lógica de violations para verificar ordenação em O(1)

class Node:
    def __init__(self, val, index):
        self.val = val
        self.index = index
        self.prev = None
        self.next = None

class SumPair:
    def __init__(self, node1, node2):
        self.sumVal = node1.val + node2.val
        self.node1 = node1
        self.node2 = node2
    
    def __lt__(self, other):
        if (self.sumVal != other.sumVal):
            return self.sumVal < other.sumVal
        return self.node1.index < other.node1.index

class Solution:
    
    def minimumPairRemovalII(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return 0

        nodes = [Node(v, i) for i, v in enumerate(nums)]
        for i in range(n):
            if i > 0: nodes[i].prev = nodes[i-1]
            if i < n - 1: nodes[i].next = nodes[i+1]

        heap = []
        violations = 0 # Contador para otimização
        
        for i in range(n - 1):
            heapq.heappush(heap, SumPair(nodes[i], nodes[i+1]))
            if nodes[i].val > nodes[i+1].val:
                violations += 1

        countOp = 0
        removedIds = set()

        # O segredo: trocar 'not self.isSorted' por 'violations > 0'
        while violations > 0 and heap:
            pair = heapq.heappop(heap)
            node1, node2 = pair.node1, pair.node2
            
            if (node1.index in removedIds or node2.index in removedIds or node1.next != node2 or pair.sumVal != node1.val + node2.val):
                continue
            
            # --- Atualizar contador de violações ANTES da mudança ---
            if node1.prev and node1.prev.val > node1.val: violations -= 1
            if node1.val > node2.val: violations -= 1
            if node2.next and node2.val > node2.next.val: violations -= 1

            # Lógica de merge original
            node1.val = node1.val + node2.val
            removedIds.add(node2.index)
            
            nextOfDeleted = node2.next
            node1.next = nextOfDeleted

            if nextOfDeleted:
                nextOfDeleted.prev = node1
                heapq.heappush(heap, SumPair(node1, nextOfDeleted))
            
            if node1.prev:
                heapq.heappush(heap, SumPair(node1.prev, node1))

            # --- Atualizar contador de violações DEPOIS da mudança ---
            if node1.prev and node1.prev.val > node1.val: violations += 1
            if node1.next and node1.val > node1.next.val: violations += 1

            countOp += 1

        return countOp

if __name__ == "__main__":
    arr = [-2,1,2,-1,-1,-2,-2,-1,-1,1,1]
    sol = Solution()
    print(sol.minimumPairRemovalII(arr))