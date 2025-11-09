# DISCLAIMER: in even tiny serious scenarios, never store user data in a file.
# this is meant for educational and hypothetical purposes only.
# very scuffed.
import json
from hashlib import sha256

def main():
	print("1 - prisijungti\n2 - registruotis")
	try: opt = int(input("pasirinkite pasirinkimą: "))
	except: opt = 2
	print("")
	u = input("email (must have @ symbol): ") # in even tiny serious cases, emails must be validated using regexes.
	print("")
	if not "@" in u:
		print("email check failed.")
		return
	p = input("password (must have 8 characters minimum): ")
	print("")
	if len(p)<8:
		print("password must have 8 chars.")
		return
	pHash = sha256(p.encode()).hexdigest()
	with open("users.json","w",encoding="utf8") as chkIO: pass
	with open("users.json","r+",encoding="utf8") as usersIO: # REMINDER to ALWAYS store user data in DATABASES in even tiny serious scenarios.
		dt = json.load(usersIO)
		match opt:
			case 1:
				if not u in dt.keys():
					print("nonexistent account.")
					return
				if dt[u]!=pHash:
					print("incorrect password.")
					return
			case _:
				if u in dt.keys():
					print("email taken.")
					return
				dt[u]=pHash
		usersIO.seek(0)
		json.dump(dt, usersIO)
		print("successfully logged in!")

main()