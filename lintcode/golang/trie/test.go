package main

// trie

/**
 * @param board: A list of lists of character
 * @param words: A list of string
 * @return: A list of string
 */
import "sort"

var directions = [][]int{
	[]int{1, 0},
	[]int{0, 1},
	[]int{0, -1},
	[]int{-1, 0},
}

func wordSearchII(board [][]byte, words []string) []string {
	m, n := len(board), 0
	if m == 0 {
		return []string{}
	}
	n = len(board[0])

	trie := NewTrie()
	for _, word := range words {
		trie.Add(word)
	}

	visited := make([][]bool, m, m)
	for i := range visited {
		visited[i] = make([]bool, n, n)
	}

	result := make([]string, 0)
	for i := range board {
		for j := range board[i] {
			dfs(board, i, j, visited, trie.Root, &result)
		}
	}
	sort.Strings(result)
	return result
}

func dfs(board [][]byte, x, y int, visited [][]bool, node *TrieNode, res *[]string) {
	child := node.Children[board[x][y]-'a']
	if child == nil {
		return
	}

	if child.Word != nil {
		*res = append(*res, *child.Word)
		child.Word = nil
	}

	visited[x][y] = true
	for _, direction := range directions {
		newX, newY := x+direction[0], y+direction[1]
		if newX < 0 || newY < 0 || newX >= len(board) || newY >= len(board[0]) {
			continue
		}
		if visited[newX][newY] {
			continue
		}
		dfs(board, newX, newY, visited, child, res)
	}
	visited[x][y] = false
}

type TrieNode struct {
	Children []*TrieNode
	Word     *string
}

func NewTrieNode() *TrieNode {
	return &TrieNode{Children: make([]*TrieNode, 26, 26)}
}

type Trie struct {
	Root *TrieNode
}

func NewTrie() *Trie {
	return &Trie{Root: NewTrieNode()}
}

func (t *Trie) Add(word string) {
	node := t.Root
	for _, c := range word {
		idx := c - 'a'
		if node.Children[idx] == nil {
			node.Children[idx] = NewTrieNode()
		}
		node = node.Children[idx]
	}
	node.Word = &word
}
