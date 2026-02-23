days = [1,2,3,4,5,6,7,8,9,10,30,31]
costs = [2, 7, 15]

def get_minimum_cost(days, costs):
    min_cost = [0]*(days[-1]+1)
    for i in range(1, days[-1]+1):
        if i not in days:
            min_cost[i] = min_cost[i-1]
        else:
            min_cost[i] = min(min_cost[i-1]+2, min_cost[max(0,i-7)]+7, min_cost[max(0,i-30)]+15)
    return min_cost[-1]
s = get_minimum_cost(days, costs)
