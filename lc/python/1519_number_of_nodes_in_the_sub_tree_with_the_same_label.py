# dfs
# time O(n)
# space O(n)

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        ret = [0]*n

        def dfs(node, parent):
            nonlocal ret, labels, graph

            node_cnt = [0]*26
            node_cnt[ord(labels[node])-ord("a")] = 1

            for nei in graph[node]:
                if nei == parent:
                    continue
                nei_node_cnt = dfs(nei, node)

                for i in range(26):
                    node_cnt[i] += nei_node_cnt[i]

            ret[node] = node_cnt[ord(labels[node])-ord("a")]
            return node_cnt
        dfs(0, -1)

        return ret
      
      
# bfs
# time O(n)
# space O(n)

class Solution {
public:
    vector<int> countSubTrees(int n, vector<vector<int>>& edges, string labels) {
        unordered_map<int, unordered_set<int>> adj;
        for (auto& edge : edges) {
            adj[edge[0]].insert(edge[1]);
            adj[edge[1]].insert(edge[0]);
        }

        // Store count of all alphabets of subtree of each node.
        vector<vector<int>> counts(n, vector<int>(26));
        queue<int> q;

        for (int node = 0; node < n; ++node) {
            counts[node][labels[node] - 'a'] = 1;
            // Store all leaf nodes in the queue.
            if (node != 0 && adj[node].size() == 1) {
                q.push(node);
            }
        }

        while (q.size()) {
            int curr = q.front();
            q.pop();

            // Each node will have only one element which will be its parent.
            int parent = *adj[curr].begin();
            // Remove current node from adjency list of parent node
            // so current node is not traversed again by parent node.
            // (due to this step, we remove all child nodes from a parent, at end parent node will only have its parent in adjacency list)
            adj[parent].erase(curr);

            // Add counts of current node in parent's frequency array.
            for (int i = 0; i < 26; ++i) {
                counts[parent][i] += counts[curr][i];
            }

            // If parent adj size is 1, it has only it's parent in the adjacency list so,
            // it means current node is last child of parent so we insert it in queue now.
            if (parent != 0 && adj[parent].size() == 1) {
                q.push(parent);
            }
        }

        vector<int> ans(n);
        for (int node = 0; node < n; ++node) {
            ans[node] = counts[node][labels[node] - 'a'];
        }

        return ans;
    }
};
