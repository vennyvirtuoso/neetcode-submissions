class Solution {
public:
    bool chck(string &s){
        int n = s.size();
        int i = 0; int j = n-1;
        while(i <= j){
            if(s[i] != s[j]) return false;
            i++;
            j--;
        }
        return true;
    }
    bool validPalindrome(string s) {
        if(chck(s)) return true;
        int i = 0; int j = s.size()-1;
        while(i <= j){
            if(s[i] != s[j]){
                string a = s;
                string b = s;
                a.erase(a.begin() + i);
                b.erase(b.begin() + j);
                if(chck(a) || chck(b)) return true;
                return false;        
            }
            i++;
            j--;
        }
        return true;
    }
};