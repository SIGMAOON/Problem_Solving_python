def solution(L, x):
    lo = 0
    hi = len(L) - 1
    
    while lo <= hi:
        
        mid = (lo + hi)//2
        
        if x == L[mid]:
            return mid
        
        if x > L[mid] :
              lo = mid + 1
            
        elif x < L[mid] :
              hi = mid - 1
             
    return -1
