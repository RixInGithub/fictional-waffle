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
			if res[1]==0: res[1]=1
			res[1] *= num
	count += 1
print(" ".join([str(a) for a in res]))