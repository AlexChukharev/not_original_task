class list_element:

	def __init__(self, val, prv, nxt):
		self.val = val
		self.prv = prv
		self.nxt = nxt

	def get_prev(self):
		return self.prv

	def get_next(self):
		return self.nxt

	def set_next(self, nxt):
		self.nxt = nxt

	def set_prev(self, prv):
		self.prv = prv

	def get_val(self):
		return self.val


class linked_list:

	def __init__(self):
		self.begin = None
		self.end = None
		self.size = 0

	def empty(self):
		return self.size == 0

	def push_front(self, val):
		if self.empty():
			new_e = list_element(val, None, None)
			self.begin = new_e
			self.end = new_e
		else:
			new_begin = list_element(val, None, self.begin)
			self.begin.set_prev(new_begin)
			self.begin = new_begin
		self.size += 1

	def push_back(self, val):
		if self.empty():
			new_e = list_element(val, None, None)
			self.begin = new_e
			self.end = new_e
		else:
			new_end = list_element(val, self.end, None)
			self.end.set_next(new_end)
			self.end = new_end
		self.size += 1

	def get_front(self):
		return self.begin.get_val()

	def get_back(self):
		return self.end.get_val()

	def pop_back(self):
		if self.size != 1:
			self.end = self.end.get_prev()
		else:
			self.end = None
			self.begin = None
		self.size -= 1

	def pop_front(self):
		if self.size != 1:
			self.begin = self.begin.get_next()
		else:
			self.end = None
			self.begin = None
		self.size -= 1

	def get_size(self):
		return self.size

q = linked_list()

ans = ''

while True:
	s = input()
	if s.startswith('pu'):
		n = s.split()[1]
		q.push_back(n)
		ans += 'ok\n'
		continue
	if s[0] == 'p':
		if (q.empty()):
			ans += 'error\n'
			continue
		ans += q.get_front() + '\n'
		q.pop_front()
		continue
	if s[0] == 'f':
		if (q.empty()):
			ans += 'error\n'
			continue
		ans += q.get_front() + '\n'
		continue
	if s[0] == 's':
		ans += str(q.get_size()) + '\n'
		continue
	if s[0] == 'c':
		q = linked_list()
		ans += 'ok\n'
		continue
	if s[0] == 'e':
		print(ans + 'bye')
		break