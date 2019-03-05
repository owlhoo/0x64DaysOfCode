from os import remove

def main():
	with open("new_kek.txt", "w") as new_info:
		with open("new_kek.txt", "r") as info:
			for line in info:
				if line.find("keep"):
					insert_string = str(input("Enter the security key \
you want to input:"))
					new_info.write(insert_string + '\n' + line)
				else:
					new_info.write(line)
			remove("kek.txt")

if __name__ == "__main__":
	main()

