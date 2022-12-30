class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # stores the domain and times it was visited
        subDomainDict = defaultdict(int)
        arr = []
        
        for cpdomain in cpdomains:
            freq, dom = cpdomain.split()
            # records the times the whole domain was visited
            subDomainDict[dom] += int(freq)
            # splits the subdomains
            domList = list(dom.split('.'))
            
            # checks if the domain has 3 subdomains or 2 
            # and records each subdomain and the number of times they are visited
            if len(domList) == 2:
                subDomainDict[domList[1]] += int(freq)
            
            else:
                subDomainDict[domList[1] + '.' + domList[2]] += int(freq)
                subDomainDict[domList[2]] += int(freq)
        
        for domain in subDomainDict:
            arr.append(str(subDomainDict[domain]) + ' ' + domain)
        
        return arr