class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        fa = celsius * 1.80 + 32
        kel = celsius + 273.15
        return [kel, fa]