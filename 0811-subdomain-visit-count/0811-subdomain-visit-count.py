class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        subDomainDict = defaultdict(int)
        arr = []
        
        for cpdomain in cpdomains:
            freq, dom = cpdomain.split()
            subDomainDict[dom] += int(freq)
            domList = list(dom.split('.'))
            
            if len(domList) == 2:
                subDomainDict[domList[1]] += int(freq)
            
            else:
                subDomainDict[domList[1] + '.' + domList[2]] += int(freq)
                subDomainDict[domList[2]] += int(freq)
        
        for domain in subDomainDict:
            arr.append(str(subDomainDict[domain]) + ' ' + domain)
        
        return arr