a = ['asdfdd3', '2322432', 'sdf1sdf', '2345000', '2345600', '2345601', '2345599', 'asd123f']

N = len(a)
aux = ['' for i in range(N)]
w = 7
R = 256

for d in xrange(w-1, 0-1, -1):
    count = [0 for i in range(R+1)]
    for i in xrange(0, N):
        # a[i].charAt(d)
        charoct = ord(a[i][d])
        # count frequency
        count[charoct + 1] += 1

    for r in xrange(0, R):
        count[r+1] += count[r] 

    for i in xrange(0, N):
        insert_position = ord(a[i][d])
        aux[count[insert_position]] = a[i]
        count[insert_position] += 1

    for i in xrange(0, N):
        a[i] = aux[i]

print a

