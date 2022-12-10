from solutions.loader.input_loader import load_input_data


def packet_value(packet):
    value = 0
    for i in range(0, len(packet)):
        for j in range(i + 1, len(packet)):
            if packet[i] == packet[j]:
                value += 1

    return value


class TuningTrouble:
    _lines: [str] = []

    def __init__(self, is_example: bool):
        self._lines = load_input_data(6, is_example)

    def start_of_packet(self, packet_size):
        for buffer in self._lines:
            for i in range(packet_size, len(buffer)):
                packet = []
                for x in range(i - packet_size, i):
                    packet.append(buffer[x])

                value = packet_value(packet)

                if value == 0:
                    print(f"{buffer.strip()}: first marker after character {i}")
                    break
