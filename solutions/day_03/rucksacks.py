from solutions.loader.input_loader import load_input_data


def _split_string(text):
    first_part = text[:len(text)//2]
    last_part = text[len(text)//2:]
    return first_part, last_part


def _extract_common_elements(part1, part2):
    part1_array = list(part1)
    part2_array = list(part2)

    return [x for x in part1_array if x in part2_array]


def _calculate_score(my_char):
    my_score = ord(my_char) - 96

    if my_score < 0:
        my_score = ord(my_char) - 38

    return my_score


class Rucksack:
    _lines: [str] = []

    def __init__(self, is_example: bool):
        self._lines = load_input_data(3, is_example)

    def sum_of_priorities(self):
        priorities = 0
        for line in self._lines:
            my_tuple = _split_string(line.strip())
            my_char = _extract_common_elements(my_tuple[0], my_tuple[1])[0]

            priorities += _calculate_score(my_char)

        return priorities

    def sum_of_groups(self):
        my_sum_of_groups = 0
        group_count = 0
        elves_group = []

        for line in self._lines:
            line = line.strip()

            elves_group.append(line)
            group_count += 1

            if group_count == 3:
                first_common_elements = _extract_common_elements(elves_group[0], elves_group[1])
                final_common_elements = _extract_common_elements(first_common_elements, elves_group[2])
                my_sum_of_groups += _calculate_score(final_common_elements[0])
                group_count = 0
                elves_group = []

        return my_sum_of_groups
