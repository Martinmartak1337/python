def main():
	arr = ['A', 'B', 'C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','Q','S','T','U','V','W','X','Y','Z']
	xyz = ['O', 'P', 'R', 'A', 'V', 'A']
	lst = [None] * len(xyz)
	for i in range(0, len(xyz)):
		for j in range(0, len(arr)):
			if(xyz[i] == arr[j]):
				if(j + 4 > len(arr)):
					lst[i] = arr[j+4-len(arr)]
				else:
					lst[i] = arr[j+4]
	print(lst)


main()	