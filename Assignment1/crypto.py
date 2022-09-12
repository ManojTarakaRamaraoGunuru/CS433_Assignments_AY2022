def reverse(s):
    ans = ""
    l = 0
    r = 0
    while(r<len(s) and (s[r]=="\n" or s[r]=="\r" or s[r]==" ")):
        ans += s[r]
        r += 1
    temp = ""
    while(r<len(s)):
        if(s[r] == "\n" or s[r] == "\r" or s[r] == " "):
            # a = s[l:r]
            ans += temp[::-1]
            temp = ""
            while(r<len(s) and (s[r] == "\n" or s[r] == "\r" or s[r] == " ")):
                ans += s[r]
                r += 1
                l = r
        else:
            temp+=s[r]
            r += 1
    ans+=temp[::-1]
    return ans


def encrypt(string,opt,val=2):
    if opt == 1:
        return string
    elif opt == 2:
        # lt = string.split(" ")
        # ans = ""
        # for word in lt:
        #     for char in word:
        #         if char.isupper():
        #             ans += chr((ord(char)+val -65)%26 + 65)
        #         elif char.islower():
        #             ans += chr((ord(char)+val -97)%26 + 97)
        #     ans+=" "
        # return ans[:-1]
        ans = ""
        l = 0
        r = 0
        while(r<len(string) and (string[r]=="\n" or string[r]=="\r" or string[r]==" ")):
            ans += string[r]
            r += 1
        temp = ""
        while(r<len(string)):
            if(string[r] == "\n" or string[r] == "\r" or string[r] == " "):
                # a = string[l:r]
                ans += temp
                temp = ""
                while(r<len(string) and (string[r] == "\n" or string[r] == "\r" or string[r] == " ")):
                    ans += string[r]
                    r += 1
                    l = r
            else:
                if string[r].isupper():
                    temp += chr((ord(string[r])+val -65)%26 + 65)
                elif string[r].islower():
                    temp += chr((ord(string[r])+val -97)%26 + 97)
                # temp+=string[r]
                r += 1
        ans+=temp
        return ans
    else:
        return reverse(string)
    
    

def decrypt(string,opt,val = 24):
    return encrypt(string, opt, val)


# a = "   Server filestatus ok  \n\n p"
# print(a)
# a = encrypt(a,2)
# print(a)
# a = decrypt(a,2)
# print(a)
