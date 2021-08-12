package main


// bfs

import (
	"fmt"
	"strings"
)

/**
 * @param grid:
 * @return: The lowest number of moves to acquire all keys
 */

var Keys string = "abcdef"

type node struct {
	r     int
	c     int
	steps int
	keys  string
	cnt   int
}

type mapKey struct {
	r    int
	c    int
	keys string
}

func shortestPathAllKeys(grid []string) int {
	// write your code here
	m := len(grid)
	n := len(grid[0])

	var startI int
	var startJ int
	var numKeys int

	v := make(map[mapKey]bool)
	q := []node{}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if string(grid[i][j]) == "@" {
				startI = i
				startJ = j
			} else if strings.Contains(Keys, string(grid[i][j])) {
				numKeys++
			}
		}
	}

	fmt.Println("num key: ", numKeys)
	fmt.Println(startI, startJ)
	q = append(q, node{startI, startJ, 0, ".@abcdef", 0})
	//v[startI*n+startJ] = true
	fmt.Println(q)

	direcs := []struct {
		dx int
		dy int
	}{{-1, 0}, {0, -1}, {0, 1}, {1, 0}}

	for len(q) != 0 {
		i, j, steps, keys, cnt := q[0].r, q[0].c, q[0].steps, q[0].keys, q[0].cnt
		q = q[1:]

		if strings.Contains(Keys, string(grid[i][j])) && !strings.Contains(keys, strings.ToUpper(string(grid[i][j]))) {
			fmt.Println(strings.ToUpper(string(grid[i][j])))
			keys += strings.ToUpper(string(grid[i][j]))
			cnt++
		}
		if cnt == numKeys {
			return steps
		}

		for k := 0; k < 4; k++ {
			ci := i + direcs[k].dx
			cj := j + direcs[k].dy

			if ci >= 0 && ci < m && cj >= 0 && cj < n && (v[mapKey{r: ci, c: cj, keys: keys}] == false) && strings.Contains(keys, string(grid[i][j])) {
				fmt.Println(ci, cj)
				v[mapKey{r: ci, c: cj, keys: keys}] = true
				q = append(q, node{ci, cj, steps + 1, keys, cnt})
			}

		}

	}

	return -1
}

func main() {
	a := []string{"@.a.#", "###.#", "b.A.B"}
	shortestPathAllKeys(a)
}
