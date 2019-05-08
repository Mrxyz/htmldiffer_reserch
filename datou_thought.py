from itertools import zip_longest
import difflib
alist = ["ass", "bsd", "cccf", "asdf"]
blist = ["add", "sdf", "cdf"]
for index, (a,b) in enumerate(zip_longest(alist, blist)):
    print("index: %d" % index)
    if a and b:
        for i,s in enumerate(difflib.ndiff(a, b)):
            if s[0]==' ': continue
            elif s[0]=='-':
                print(u'Delete "{}" from position {}'.format(s[-1],i))
            elif s[0]=='+':
                print(u'Add "{}" to position {}'.format(s[-1],i))
    else:
        print("Index %d: Empty line" % index)



'''
zip_longest(*iterables, fillvalue=None)
依次从每个iterables中取出一个元素进行组合，当短的iterable取完了时用fillvalue进行填充

difflib.ndiff
比较a与b(字符串列表)，返回一个Differ-style 的差异结果
'''