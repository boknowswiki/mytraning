package main

// trie

import (
	"fmt"
	"sort"
)

type trie struct {
	children map[byte]*trie
	isWord   bool
	word     string
}

var root *trie

func newTrie() *trie {
	return &trie{
		children: make(map[byte]*trie),
		isWord:   false,
	}
}

func (t *trie) insert(word string) {
	cur := root
	for idx := range word {
		if nextCur, ok := cur.children[word[idx]]; !ok {
			nextCur = newTrie()
			cur.children[word[idx]] = nextCur
		}
		cur = cur.children[word[idx]]
	}
	cur.isWord = true
	cur.word = word
	return
}

/**
 * @param board: A list of lists of character
 * @param words: A list of string
 * @return: A list of string
 */
func wordSearchII(board [][]byte, words []string) []string {
	// write your code here
	m := len(board)
	if m == 0 {
		return []string{}
	}
	n := len(board[0])
	if n == 0 {
		return []string{}
	}

	root = newTrie()

	for idx := range words {
		root.insert(words[idx])
	}

	ret := []string{}
	visited := make([][]bool, m, m)
	for i := range visited {
		visited[i] = make([]bool, n, n)
	}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			//visited[i][j] = true
			search(board, i, j, root, visited, &ret)
			//visited[i][j] = false
		}
	}
	sort.Strings(ret)
	return ret
}

func search(board [][]byte, x, y int, node *trie, visited [][]bool, ret *[]string) {
	fmt.Printf("searching %v, %v, %v, %v, %v\n", x, y, string(board[x][y]), visited, node.children)
	if _, ok := node.children[board[x][y]]; !ok {
		return
	}

	next := node.children[board[x][y]]
	if next.isWord {
		*ret = append(*ret, next.word)
		next.isWord = false
		//return
	}

	visited[x][y] = true
	direcs := []struct {
		dx int
		dy int
	}{{-1, 0}, {0, -1}, {0, 1}, {1, 0}}
	for i := 0; i < 4; i++ {
		nx := x + direcs[i].dx
		ny := y + direcs[i].dy

		if valid(board, nx, ny, visited) {
			//visited[nx][ny] = true
			search(board, nx, ny, next, visited, ret)
			//visited[nx][ny] = false
		}
	}
	visited[x][y] = false

	return
}

func valid(board [][]byte, x int, y int, visited [][]bool) bool {
	m := len(board)
	n := len(board[0])
	if x < 0 || x >= m || y < 0 || y >= n || visited[x][y] {
		return false
	}
	return true
}

func main() {
	/*
		b := make([][]byte, 3)
		b[0] = []byte("doaf")
		b[1] = []byte("agai")
		b[2] = []byte("dcan")

		w := []string{"dog", "dad", "dgdg", "can", "again"}
	*/
	/*
		b := make([][]byte, 3)
		b[0] = []byte("abce")
		b[1] = []byte("sfcs")
		b[2] = []byte("adee")

		w := []string{"see", "se"}
	*/
	b := make([][]byte, 3)
	b[0] = []byte("abce")
	b[1] = []byte("sfcs")
	b[2] = []byte("adee")

	w := []string{"as", "ab", "cf", "da", "ee", "e", "adee", "eeda"}

	fmt.Println(wordSearchII(b, w))
}



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
