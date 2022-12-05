from solutions.loader.input_loader import load_input_data


class Interval:
    lower_bound: int
    upper_bound: int

    def __init__(self, interval_notation):
        limits = interval_notation.split("-")
        self.lower_bound = int(limits[0])
        self.upper_bound = int(limits[1])

    def __eq__(self, other):
        return self.lower_bound == other.lower_bound and self.upper_bound == other.upper_bound

    def intersects(self, other):
        my_array = self.as_array()
        other_array = other.as_array()

        result = [x for x in my_array if x in other_array]
        return len(result) > 0

    def as_array(self):
        interval_array = []

        for n in range(self.lower_bound, self.upper_bound + 1):
            interval_array.append(n)

        return interval_array


class DwarfMessCleaner:
    _lines: [str] = []

    def __init__(self, is_example: bool):
        self._lines = load_input_data(4, is_example)

    def fully_contains(self):
        pairs = 0

        for line in self._lines:
            line = line.strip()

            intervals = line.split(",")
            interval1 = Interval(intervals[0])
            interval2 = Interval(intervals[1])

            if interval1.lower_bound >= interval2.lower_bound and interval1.upper_bound <= interval2.upper_bound:
                pairs += 1

            if interval2.lower_bound >= interval1.lower_bound and interval2.upper_bound <= interval1.upper_bound:
                pairs += 1

            if interval1 == interval2:
                pairs -= 1

        return pairs

    def overlaps(self):
        all_overlaps = 0

        for line in self._lines:
            line = line.strip()

            intervals = line.split(",")
            interval1 = Interval(intervals[0])
            interval2 = Interval(intervals[1])

            if interval1.intersects(interval2):
                all_overlaps += 1

        return all_overlaps
