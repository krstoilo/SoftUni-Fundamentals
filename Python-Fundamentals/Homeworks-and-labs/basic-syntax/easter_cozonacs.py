budget = float(input())
flour_price = float(input())
egg_pack_price = 0.75 *flour_price
milk_price = flour_price + 0.25 * flour_price

cozonac_price = flour_price + egg_pack_price + (milk_price*0.25)

baked_cozonacs = 0
gathered_eggs = 0

while budget > cozonac_price:
    budget -= cozonac_price
    baked_cozonacs += 1
    gathered_eggs += 3
    if baked_cozonacs % 3 == 0:
        gathered_eggs -= (baked_cozonacs - 2)

print(f'You made {baked_cozonacs} cozonacs! Now you have {gathered_eggs} eggs and {budget:.2f}BGN left.')