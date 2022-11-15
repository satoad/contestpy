str1 = input()
str2 = input()

flag = True

if (str1.find(str2[0]) != -1):
    ind1 = list([j for j, char in enumerate(str1) if char == str2[0]])
    if (len(str2) > 2):
        if (str2.find(str2[1]) != -1):
            ind2 = list([j for j, char in enumerate(str1) if char == str2[1]])  
            for i in ind1:
                for j in ind2:
                    if (i < j):
                        dist = j - i
                            let = 1
                            for g in str2[2:]:
                                if j + let * dist > len(str1) or str1[j + let * dist] != g:
                                    break

                                let += 1
                            else:
                                print("YES")
                                flag = False
                                break
                if not flag:
                    break
            else:
                print("NO")
    elif (len(str2) == 2):
        if (str2[1] in str(str1)):
            print("YES")
        else:
            print("NO")
    elif (str2 in str(str1)):
        print("YES")
    else:
        print("NO")
else:                  
    print("NO")