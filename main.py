from solutions.day_04.dwarf_mess_cleaner import DwarfMessCleaner

if __name__ == '__main__':
    mess_cleaner = DwarfMessCleaner(is_example=False)

    print(mess_cleaner.fully_contains())
    print(mess_cleaner.overlaps())
