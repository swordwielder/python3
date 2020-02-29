class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices % 2 != 0 or tomatoSlices < cheeseSlices * 2:
            return []
        smallBurgers = int(tomatoSlices / 2)
        if smallBurgers == cheeseSlices:
            return [0, smallBurgers]
        jumboBurgers = smallBurgers - cheeseSlices
        smallBurgers = smallBurgers - jumboBurgers * 2
        if smallBurgers < 0:
            return []
        return [jumboBurgers, smallBurgers]
