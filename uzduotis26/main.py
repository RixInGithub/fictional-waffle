# Klaviatūra įvedami n skaičių. Jei įvestas skaičius lyginis - pridedamas prie sumos, jei nelyginis - kaupiama sandauga. Rezultatas parodomas ekrane.
res = [0,0] # 0 => sum, 1 => product
n = 5
count = 0
while count < n:
	num = int(input())
	match num % 2:
		case 0:
			res[0] += num
		case _: # allat for no else statements? worth it
			res[1] *= num
	count += 1
print(" ".join(res))