from solutions.loader.input_loader import load_input_data


def determine_position(stack_number):
    if stack_number == 1:
        return 2
    else:
        return determine_position(stack_number - 1) + 4


class CraneCommand:
    _amount: int = 0
    _source: int = 0
    _target: int = 0

    def __init__(self, command):
        command = command.replace("move", "")
        command = command.replace("from", "")
        command = command.replace("to", "")
        commands = command.strip().split("  ")
        crane_commands = list(map(lambda x: int(x), commands))

        self._amount = crane_commands[0]
        self._source = crane_commands[1]
        self._target = crane_commands[2]

    def amount(self):
        return self._amount

    def source(self):
        return self._source

    def target(self):
        return self._target

    def __str__(self):
        return f"move {self._amount} from {self._source} to {self._target} [{self._amount}, {self._source}, {self._target}]"


class CrazyCrane:
    _lines: [str] = []
    _r_stacks: [str] = []
    _r_commands: [str] = []
    _stacks = {}
    _commands = []

    def __init__(self, is_example: bool):
        self._lines = load_input_data(5, is_example)

        load_stacks = True

        for line in self._lines:
            if line != "\n" and load_stacks:
                self._r_stacks.append(line)

            if line == "\n":
                load_stacks = False

            if line != "\n" and not load_stacks:
                self._r_commands.append(line.strip())

        self._load_stacks()
        self._load_commands()

    def _load_stacks(self):
        last_line_number = len(self._r_stacks) - 1

        stack_numbers = self._r_stacks[last_line_number].strip().split("  ")
        stack_numbers = list(map(lambda x: int(x), stack_numbers))

        for stack_number in stack_numbers:
            self._stacks.update({stack_number: []})

        stack_elements = self._r_stacks[0:last_line_number]
        stack_elements.reverse()

        for stack_element in stack_elements:
            for stack_number in stack_numbers:
                position = determine_position(stack_number)
                stack_len = len(stack_element)

                if not (stack_len < position):
                    position_element = stack_element[position]

                    if position_element != " ":
                        self._stacks[stack_number].append(stack_element[position - 1])

    def _load_commands(self):
        self._commands = list(map(lambda x: CraneCommand(x), self._r_commands))

    def crate_mover_9000(self):
        for command in self._commands:
            source_stack = self._stacks[command.source()]
            target_stack = self._stacks[command.target()]

            for x in range(1, command.amount() + 1):
                element = source_stack.pop()
                target_stack.append(element)

        message = ""

        for key in self._stacks.keys():
            my_stack = self._stacks[key]
            message += my_stack[len(my_stack) - 1]

        return message

    def crate_mover_9001(self):
        for command in self._commands:
            source_stack = self._stacks[command.source()]
            target_stack = self._stacks[command.target()]

            intermediate_stack = []

            for x in range(1, command.amount() + 1):
                element = source_stack.pop()
                intermediate_stack.append(element)

            intermediate_stack.reverse()

            for intermediate_item in intermediate_stack:
                target_stack.append(intermediate_item)

        message = ""

        for key in self._stacks.keys():
            my_stack = self._stacks[key]
            message += my_stack[len(my_stack) - 1]

        return message
