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


def encrypt(string,opt,val=2,flag=0):
    if opt == 1:
        return string
    elif opt == 2:
        ans = ""
        l = 0
        r = 0
        while(r<len(string) and (string[r]=="\n" or string[r]=="\r" or string[r]==" ")):
            ans += string[r]
            r += 1
        temp = ""
        while(r<len(string)):
            if(string[r] == "\n" or string[r] == "\r" or string[r] == " "):
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
                elif string[r].isdigit() and flag==0:
                    temp += chr((ord(string[r])+val -ord('0'))%10 + ord('0'))
                elif string[r].isdigit() and flag==1:
                    val = -2
                    temp += chr((ord(string[r])+val -ord('0'))%10 + ord('0'))
                else:
                    temp+=string[r]
                r += 1
        ans+=temp
        return ans
    else:
        return reverse(string)
    
    

def decrypt(string,opt,val = 24):
    return encrypt(string, opt, val, 1)

# Check the helper functions by uncommenting this
# a = "   Server filestatus ok  \n\n p"
# print(a)
# a = encrypt(a,2)
# print(a)
# a = decrypt(a,2)
# print(a)
