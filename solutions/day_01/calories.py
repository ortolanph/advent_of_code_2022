from solutions.loader.input_loader import load_input_data


class Calories:

    _lines: [str] = []

    def __init__(self, is_example: bool):
        self._lines = load_input_data(1, is_example)

    def _process(self):
        calories = 0
        all_calories = []

        for line in self._lines:
            line = line.strip()

            if line:
                calories += int(line)
            else:
                all_calories.append(calories)
                calories = 0

        all_calories.append(calories)
        all_calories.sort(reverse=True)
        return all_calories

    def gourmand(self):
        return self._process()[0]

    def gourmand_three(self):
        return self._process()[0] + self._process()[1] + self._process()[2]
