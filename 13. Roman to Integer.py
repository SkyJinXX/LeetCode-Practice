class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        ctn = False
        for i in range(len(s)):
            if ctn:
                ctn = False
                continue

            ch = s[i]
            if i != len(s)-1:
                next_ch = s[i+1]
            else:   
                next_ch = None

            if ch == 'I':
                if next_ch == 'V':
                    sum += 4
                    ctn = True
                    continue
                elif next_ch == 'X':
                    sum += 9
                    ctn = True
                    continue
                else:
                    sum += 1
                    #i += 1
                    continue
            elif ch == 'V':
                sum += 5
                continue
            elif ch == 'X':
                if next_ch == 'L':
                    sum += 40
                    ctn = True
                    continue
                elif next_ch == 'C':
                    sum += 90
                    ctn = True
                    continue
                else:
                    sum += 10
                    continue
            elif ch == 'L':
                sum += 50
                continue
            elif ch == 'C':
                if next_ch == 'D':
                    sum += 400
                    ctn = True
                    continue
                elif next_ch == 'M':
                    sum += 900
                    ctn = True
                    continue
                else:
                    sum += 100
                    continue
            elif ch == 'D':
                sum += 500
                continue
            elif ch == 'M':
                sum += 1000
                continue
        return sum

                
