import re
def count_substring(string, sub_string):
    import re
    return len(re.findall(sub_string, string))

    # main = len(string) -1
    # count = 0
    # for i, s in enumerate(string):
    #     if i+2 > main:
    #         continue
    #     match = string[i] + string[i+1] + string[i+2]
    #     if sub_string in match:
    #         count += 1
    #return count

if __name__ == '__main__':
    count = count_substring("TestCaseTestCase", "CaseT")
    print(count)