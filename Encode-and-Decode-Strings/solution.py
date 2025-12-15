#Given:
# a list of string,
# write two function encode and decode such that
# encode encodes the list of strings into single string
# decode decodes the string back into list of strings

#Since, we are told that each string is at most 2 character(0 <= strs.length < 100)
#we will use that idea that we can add prefix of length with padding of 2 so that 
#we read that much character next and then new prefix length start and we keep reading and so on

class Solution:
    def encode(self, strs: list) -> str:
        final = ""

        for string in strs:
            slen = len(string)
            len_prefix = str(slen).zfill(2) #padding with 0 in case of single digit len

            final += f"{len_prefix}{string}"
        
        return final
    
    def decode(self, strs: str) -> list:
        strs_cpy = str(strs)
        strings = []

        while strs_cpy:
            cur_str_len = int(strs_cpy[:2])
            cur_str = strs_cpy[2:2+cur_str_len]
            
            strings.append(cur_str)

            strs_cpy = strs_cpy[2+cur_str_len:]
        
        return strings

obj = Solution()
encoded = obj.encode(["azan","shahid","usama"])
decoded = obj.decode(encoded)

print(decoded)