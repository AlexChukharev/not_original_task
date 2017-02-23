from collections import deque

q = deque()

ans = ''

while True:
	s = input()
	if s.startswith('pu'):
		n = s.split()[1]
		q.append(n)
		ans += 'ok\n'
		continue
	if s[0] == 'f':
		if (len(q) == 0):
			ans += 'error\n'
			continue
		n = q.popleft()
		ans += n + '\n'
		q.appendleft(n)
		continue
	if s[0] == 's':
		ans += str(len(q)) + '\n'
		continue
	if s[0] == 'p':
		if (len(q) == 0):
			ans += 'error\n'
			continue
		ans += q.popleft() + '\n'
		continue
	if s[0] == 'c':
		q.clear()
		ans += 'ok\n'
		continue
	if s[0] == 'e':
		print(ans + 'bye')
		break
