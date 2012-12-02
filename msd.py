a = ['she', 'sells', 'seashells', 'by', 'the', 'sea', 'shore', 'the', 'shells', 'she', 'sells',
        'are', 'surely', 'seashells']

R = 256
N = len(a)
aux = ['' for i in range(N)]

def charAt(s, d):
    if d < len(s):
       return ord(s[d])
    else:
        return -1
      
def msdsort(a, lo, hi, d):
    if hi <= lo:
        return
    count = [0 for i in range(R+2)]
    for i in xrange(lo, hi+1):
        charoct = charAt(a[i], d)
        count[charoct + 2] += 1

    for r in xrange(0, R+1):
        count[r+1] += count[r] 

    for i in xrange(lo, hi+1):
        charoct = charAt(a[i], d)
        aux[count[charoct + 1]] = a[i] 
        count[charoct + 1] += 1

    for i in xrange(lo, hi+1):
        a[i] = aux[i-lo]

    print a

    for r in xrange(0, R):
        msdsort(a, lo + count[r], lo + count[r+1] - 1, d + 1)

msdsort(a, 0, N-1, 0)


