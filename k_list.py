def get_list(k):
	if k == 1:
		return [0, 0]
	else:
		return[get_list(k - 1), get_list(k - 1)]

 print(get_list(int(input())))