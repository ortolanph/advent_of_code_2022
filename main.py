from solutions.day_06.tuning_trouble import TuningTrouble

if __name__ == '__main__':
    tuning_trouble = TuningTrouble(is_example=False)

    tuning_trouble.start_of_packet(packet_size=4)
    print("-----------------------------------------------------------")
    tuning_trouble.start_of_packet(packet_size=14)
