//sort

import (
  "sort"
)
/**
 * @param hand: 
 * @param W: 
 * @return: return true or false
 */
type card struct {
	id    int
	count int
}

func isNStraightHand(hand []int, W int) bool {
	if len(hand)%W != 0 {
		return false
	}
	counts := make(map[int]int)

	for _, v := range hand {
		var count = 1
		if prev, ok := counts[v]; ok {
			count = prev + 1
		}
		counts[v] = count
	}
	cards := make([]*card, 0, len(hand))
	for k, v := range counts {
		cards = append(cards, &card{k, v})
	}
	sort.Slice(cards, func(i, j int) bool {
		return cards[i].id < cards[j].id
	})
	for len(cards) >= W {
		deduction := cards[0].count
		cards[0].count = 0
		for j := 1; j != W; j++ {
			cards[j].count -= deduction
			if cards[j].id-cards[j-1].id != 1 || cards[j].count < 0 {
				return false
			}
		}
		for len(cards) != 0 && cards[0].count == 0 {
			cards = cards[1:]
		}
	}
	return len(cards) == 0
}
