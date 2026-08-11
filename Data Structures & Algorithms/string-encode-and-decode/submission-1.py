class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string=""
        for string in strs:
            length = len(string)
            encoded_string += str(length)
            encoded_string+="#"
            encoded_string+=string
        
        # print(encoded_string)
        return encoded_string


    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i=0
        n = len(s)
        while(i<n):
            length = ""
            start=s[i]
            i=i+1
            while(s[i]!="#"):
                start=start+s[i]
                i=i+1
            i=i+1
            length = int(start)
            string = s[i:i+length]
            i=i+length
            decoded_strs.append(string)
        return decoded_strs
