targets_sequence = [int(i) for i in input().split()]
shoot_index = input()
shot_count = 0
while shoot_index != 'End':
    if shoot_index.isdigit():
        shoot_index = int(shoot_index)
    if 0 <= shoot_index < len(targets_sequence) and targets_sequence[shoot_index] != -1:
        current = targets_sequence[shoot_index]
        for n in range(len(targets_sequence)):
            if targets_sequence[n] > current and targets_sequence[n] != -1:
                targets_sequence[n] -= current
            elif targets_sequence[n] <= current and targets_sequence[n] != -1:
                targets_sequence[n] += current
        targets_sequence[shoot_index] = -1
        shot_count += 1
    shoot_index = input()

targets_sequence = [str(i) for i in targets_sequence]
print(f"Shot targets: {shot_count} -> {' '.join(targets_sequence)}")