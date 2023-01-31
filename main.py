class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        ml = 0  # number of element with minimal length
        for i in range(1, len(strs)):  # find the shortest string in list
            if len(strs[ml]) > len(strs[i]):
                ml = i

        ls1 = list(strs[ml])

        count1 = 0  # counter of words with this symbol
        count2 = 0  # counter of repeated symbols

        for i in range(len(strs[ml])):
            for j in range(len(strs)):
                ls2 = list(strs[j])

                if ls1[i] == ls2[i]:
                    count1 += 1

            if count1 == len(strs):
                count2 += 1
            else:
                break

            count1 = 0

        if count2 == 0:
            return ''

        s = ''
        for i in range(count2):
            s += ls1[i]

        return s

def main():

    print("Enter count of strings in list of strings:")
    l = int(input())

    strs = []

    print("Enter strings below:")
    for i in range(l):
        strs.append(input())

    ml = 0 # number of element with minimal length
    for i in range(1, l): # find the shortest string in list
        if len(strs[ml]) > len(strs[i]):
            ml = i

    ls1 = list(strs[ml])

    count1 = 0 # counter of words with this symbol
    count2 = 0 # counter of repeated symbols

    for i in range (len(strs[ml])):
        for j in range(len(strs)):
            ls2 = list(strs[j])

            print("i =", i, "; j =", j)
            if ls1[i] == ls2[i]:
                count1 += 1

        if count1 == len(strs):
               count2 += 1
        else:
            break

        count1 = 0

    if count2 == 0:
        print("Result: ''")
        return ''

    s = ''
    for i in range(count2):
        s += ls1[i]

    print("Result:", s)
    return s


main()