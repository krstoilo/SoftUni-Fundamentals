days = int(input())
plunder_a_day = int(input())
target_plunder = float(input())

gathered_plunder = 0

for n in range(1, days+1):
    gathered_plunder += plunder_a_day
    if n % 3 == 0:
        gathered_plunder += 0.5 * plunder_a_day
    if n % 5 == 0:
        gathered_plunder -= 0.3 * gathered_plunder

if gathered_plunder >= target_plunder:
    print(f"Ahoy! {gathered_plunder:.2f} plunder gained.")
else:
    print(f"Collected only {gathered_plunder/target_plunder*100:.2f}% of the plunder.")
