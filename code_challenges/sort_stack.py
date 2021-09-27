def pop_until(fromstack, tostack, val):
    '''
    pops from fromstack onto tostack until val is greater than the last
    value popped. Returns the count of items popped.
    '''
    count = 0
    while fromstack:
        if fromstack[-1] < val:
            return count
        pop_val = fromstack.pop()
        tostack.append(pop_val)
        count += 1
    return count

def push_until(fromstack, tostack, n):
    '''
    pushes values from fromstack onto tostack n times
    '''
    for _ in range(n):
        tostack.append(fromstack.pop())
        
def sort_stack(astack:list) -> list:
    '''
    sorts elements from astack onto a tmpstack and returns the sorted tmpstack.
    astack is emptied of values.
    '''
    tmpstack = []
    while astack:
        val = astack.pop()
        # tmpstack is empty
        if not tmpstack:
            tmpstack.append(val)
        # tmpstack is ordered when appending val
        elif tmpstack[-1] < val:
            tmpstack.append(val)
        # tmpstack is unordered when appending val, so pop tmpstack until
        # the order is retained, then push popped (previously ordered) values back onto tmpstack
        else:
            depth = pop_until(tmpstack, astack, val)
            tmpstack.append(val)
            push_until(astack, tmpstack, depth)
    return tmpstack
    
astack = [1,-11,0,1,2]
print(sort_stack(astack))
