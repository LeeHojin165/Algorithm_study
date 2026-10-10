from collections import defaultdict, deque

class Tree:
    def __init__(self, n, graph,root=1):
        self.nodes = {j: Node(j) for j in range(1, n + 1)}
        
        self.root = self.nodes[root]
        visited = {root}
        q = deque([root])
        
        while q:
            cur = q.popleft()
            
            #인접한 노드를 다시 넣는다.
            for nxt in graph[cur]:
                if nxt not in visited:
                    visited.add(nxt)
                    self.nodes[cur].add_children(self.nodes[nxt])
                    q.append(nxt)
                    
    def subtree_size(self, node):
        return 1 + sum(self.subtree_size(c) for c in node.children)
    
    
    
    
class Node:
    def __init__(self, val):
        self.val = val
        self.children = []
        self.parent = None
        
    def add_children(self, child):
        child.parent = self
        self.children.append(child)
    
    def children_size(self):
        return len(self.children)
    
    
        
def solution(n, wires):
    answer = 9999
    #인접리스트 만들기
    graph = defaultdict(list)
    
    for wire in wires:
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])
        
        
    #모든 송전탑을 돌아가면서 서브트리를 하나 떼어냈을 때 본 트리와 서브트리의 차가 가장 적은 경우를 구한다? 일리가 있다 왜나하면 n이 2이상 100이하이기 때문에 모든 송전탑을 다돌아도 O(100)이니까
    
    #만약 1을 루트로 정하면
    tree = Tree(n,graph,1)
    answer = min(
        abs(n - 2 * tree.subtree_size(node))
        for node in tree.nodes.values()
        if node is not tree.root
    )
    
        
    return answer