# python ../transcrypt --nomin -b ./sort_test.py
# npx rollup ./__target__/sort_test.js --o ./__target__/sort_test.bundle.js --f cjs
# node ./__target__/sort_test.bundle.js

import copy

def main():
    print("Hello!")

    # x = [4, 7, 23, 11]
    # print(max(x))
    # print("x:", x)

    # print("sorted(x):", sorted(x))
    # print("x:", x)
    # print("sorted(x str):", sorted(x, str))
    # print("sorted(x kstr):", sorted(x, key=str))

    # print("sorted(x rev):", sorted(x, reverse=True))
    # x.sort()
    # print("x.sort:", x)
    # x.sort(reverse=True)
    # print("x.reverse:", x)

    # a = [1, 5, 33, 2, -1]
    # print("sorted(a):", sorted(a))
    # print("sorted(a str):", sorted(a, key=str))
    # print("sorted(a int):", sorted(a, key=int))

    # items = [{'name': 'Defg', 'qty': 99}, {'name': 'Abcd', 'qty': 42}, {'name': 'Hijk', 'qty': 11}]
    # print("items:", items)
    #
    # items.sort(key=lambda k: k['name'])
    # print("items srt1:", items)
    #
    # items.sort(key=lambda k: k['qty'])
    # print("items srt2:", items)

    # items = sorted(items, key=lambda k: k['name'])
    # print("items srt:", items)
    # items = sorted(items, key=lambda k: k['name'], reverse=True)
    # print("items rev:", items)

    # a = {'a': 1, 'b': 2, 'c': 3}
    # b = copy.copy(a)
    # print("a:", a)
    # print("b:", b)
    # a['b'] = 9
    # print("a:", a)
    # print("b:", b)

    # m = ['1', 2, '3']
    # m2 = sorted(m)
    # print(m2)

    # print(dict(**{1: 2}))

    x = ['a','b','c']
    print("x:", x[-1])  # __:opov

    # n='13'
    # a = n[0]
    # b = n[-1]  # __:opov
    # c = n[-1::]
    # print("a:", a, "b:", b, "c:", c)
    # # print(x[::-1])
    # print("result0:", max(a, b))
    # print("result2:", max('1', '3'))
    #
    # print("rev:", x[::-1])
    # print("neg slice:", x[-3:-1])
    # x[-3:-1] = ['x', 'y']
    # print("x updated:", x)

    # x = 'abcd'
    # y = list(x)
    # print(x[::-1])
    # print(y[4::-1])
    # print(y[4:1:-2])
    # try:
    #     a = x[::0]
    #     print(a)
    # except object as e:
    #     print("Error:", str(e))

    sample_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    # aList = copy.copy(sample_list)
    # aList[1:5] = ['x', 'y', 'z']
    # print(aList)
    #
    # aList = copy.copy(sample_list)
    # aList[1:5] = 'xyz'
    # print(aList)

    # aList = copy.copy(sample_list)
    # aList[5:2:-1] = ['x', 'y', 'z']
    # print(aList)
    #
    # aList = copy.copy(sample_list)
    # aList[5:0:-2] = ['x', 'y', 'z']
    # print(aList)
    #
    # aList = copy.copy(sample_list)
    # aList[1:5:2] = ['x', 'y', 'z']
    # print(aList)

    # aList = copy.copy(sample_list)
    # aList[1:5:2] = ['x', 'y', 'z']
    # print(aList)

    # aList = copy.copy(sample_list)
    # aList[5:1:-1] = ['x', 'y', 'z']
    # print(aList)

    obj = {"a": "hello"}
    print(obj["a"])

if __name__ == '__main__':
    main()
