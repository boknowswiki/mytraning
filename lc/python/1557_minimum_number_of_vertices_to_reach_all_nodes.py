# graph
# time O(n)
# space O(n)

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 0:
            return []

        ret = set([i for i in range(n)])

        for a, b in edges:
            if b in ret:
                ret.remove(b)

        return ret
      
      
class Solution {
  public List<Integer> findSmallestSetOfVertices(int n, List<List<Integer>> edges) {
    // List to signify if the vertex has an incoming edge or not.
    boolean[] isIncomingEdgeExists = new boolean[n];
    for (List<Integer> edge : edges) {
      isIncomingEdgeExists[edge.get(1)] = true;
    }

    List<Integer> requiredNodes = new ArrayList();
    for (int i = 0; i < n; i++) {
      // Store all the nodes that don't have an incoming edge.
      if (!isIncomingEdgeExists[i]) {
        requiredNodes.add(i);
      }
    }

    return requiredNodes;
  }
}
