initial_stops = input()

command = input()
while command != "Travel":
    if "Add" in command:
        command = command.replace("Add ","")
        token = command.split(":")
        index = int(token[1])
        stop_string = token[2]
        if index < len(initial_stops):
            initial_stops = initial_stops[:index] + stop_string + initial_stops[index:]
        print(initial_stops)
    elif "Remove" in command:
        token = command.split(":")
        start_index = int(token[1])
        end_index = int(token[2])
        if start_index < len(initial_stops) and end_index < len(initial_stops):
            initial_stops = initial_stops[:start_index] + initial_stops[end_index+1:]
        print(initial_stops)
    elif "Switch" in command:
        token = command.split(":")
        old_str = token[1]
        new_str = token[2]
        if old_str in initial_stops:
            initial_stops = initial_stops.replace(old_str, new_str)
        print(initial_stops)
    command = input()


print(f"Ready for world tour! Planned stops: {initial_stops}")