class TimeMap:

    def __init__(self):
        self.dictt={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dictt:
            self.dictt[key]=[]
            self.dictt[key].append((timestamp,value))
        else:
            self.dictt[key].append((timestamp,value))
                

    def get(self, key: str, timestamp: int) -> str:
        if key in self.dictt:
            search = self.dictt[key]

            i=0
            j=len(search)-1

            while i<=j:
                mid = (i+j)//2
                if search[mid][0]==timestamp:
                    return search[mid][1]
                elif search[mid][0]<timestamp:
                    i=mid+1
                else:
                    j=mid-1
            if search[i-1][0]<timestamp:
                return search[i-1][1]
        return ""