class number:

	def __init__(self, string_num, base):
		cur_val = 0;
		string_num = string_num.lower()
		for c in string_num:
			cur_val *= base
			if c <= '9' and c >= '0':
				cur_val += int(c)
			else:
				cur_val += ord(c) - ord('a') + 10
		self.val = cur_val

	def to_string(self, base):
		cur_val = self.val
		if cur_val == 0:
			return '0'
		res = ''
		alf = '0123456789abcdefghijklmnopqrstuvwxyz'
		while cur_val != 0:
			res += alf[cur_val % base]
			cur_val //= base
		return res[::-1]


tr1, num = input().split()
tr2 = input()
frm = int(tr1)
t = int(tr2)
print(number(num, frm).to_string(t))
