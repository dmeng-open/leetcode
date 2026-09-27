from typing import List


class SummaryRanges:
    def __int__(self):
        self.values = set()

    def add_num(self, value: int):
        self.values.add(value)

    def get_intervals(self) -> List[int]:
        if not self.values:
            return []

        result = []
        ordered = sorted(self.values)
        start = end = ordered[0]
        for value in ordered[1:]:
            if value == end + 1:
                end = value
            else:
                result.append([start, end])
                start = end = value
        result.append([start, end])
        return result