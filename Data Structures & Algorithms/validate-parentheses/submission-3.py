class Solution:
    def isValid(self, s: str) -> bool:
        valids = []
        for br in s:
            if br=="(" or br=="{" or br=="[":
                valids.append(br)
            elif len(valids)==0:
                return False
            else:
                if br == ")":
                    if valids[-1]!="(":
                        return False
                    else:
                        valids.pop()
                elif br == "}":
                    if valids[-1]!="{":
                        return False
                    else:
                        valids.pop()
                elif br == "]":
                    if valids[-1]!="[":
                        return False
                    else:
                        valids.pop()
        if len(valids)>0:
            return False
        return True