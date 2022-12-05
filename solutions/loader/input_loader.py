def load_input_data(day:int, is_example: bool) -> []:
    formatted_day = f"{day:02d}"

    if is_example:
        source_data_file = f"data/day{formatted_day}_example.txt"
    else:
        source_data_file = f"data/day{formatted_day}_input.txt"

    with open(source_data_file, "r", encoding="utf8") as day_input:
        return day_input.readlines()
