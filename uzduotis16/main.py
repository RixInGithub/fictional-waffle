import json

def main():
	with open("booksOrMovies.json","r+",encoding="utf8") as bM_IO:
		bM_Data = json.load(bM_IO)
		bM_IO.seek(0)
		print("1 - pridėti knygą/filmą į katalogą\n2 - peržiūrėti katalogą")
		try: opt = int(input("pasirinkite pasirinkimą: "))
		except: opt = 1
		print("")
		match opt:
			case 1:
				bM_Name = input("knygos/filmo pavadinimas: ")
				print("")
				if bM_Name in bM_Data.keys():
					print(f"\"{bM_Name}\" jau egzistuoja.")
					return
				try: bM_Rating = int(input("įvertinimas (x/10): "))
				except:
					print("")
					print("įvertinimas nėra numeris.")
					return
				print("")
				bM_Data[bM_Name]=bM_Rating
				json.dump(bM_Data,bM_IO)
				bM_Data = json.load(bM_IO)
				print(f"\"{bM_Name}\" pridėta sėkmingai! (įvertinimas: {bM_Rating}/10)")
			case _:
				bM_Data = json.load(bM_IO)
				print("katalogas")
				print("")
				for name,rating in bM_Data.items():
					print(name, f"- {rating}/10")

main()