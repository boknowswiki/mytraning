
//康拓展开的应用, 模板题.
//
//康拓展开, 计算排列与字典序排名的映射关系.
//https://zh.wikipedia.org/wiki/%E5%BA%B7%E6%89%98%E5%B1%95%E5%BC%80

var flag []bool // flag[i] 表示 i+1 是否被使用

func getPermutation(n int, k int) string {
    if n == 0 {
		return ""
	}
	flag = make([]bool, n)
	return dfs(n, k-1) // k 表示组内索引，从 0 开始，0~(n-1)!-1 共 (n-1)! 个元素
}

func dfs(n, k int) string {
	if n == 0 {
		return ""
	}
	f := factorial(n - 1)
	c := k / f // c 表示组间索引，从 0 开始，0~n-1 共 n 个组

	index := 0                      // 找到第 c 组的第一个字符的下标
	for i, j := 0, c; j >= 0; i++ { // 第 c 组的第一个字符是剩余数字里从小到大第 c 个数
		if flag[i] == false {
			j--
			index = i
		}
	}

	flag[index] = true
	res := string(byte(index+1) + '0') // 当前选择的字符
	res += dfs(n-1, k-c*f)             // 下一组的组内偏移是 k-c*f，还是从 0 开始
	return res
}

// 求阶乘
func factorial(i int) int {
	res := 1
	for i > 1 {
		res *= i
		i--
	}
	return res
}
