def parse_input(user_input):
    #Парсить введену команду та її аргументи
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args