def maxProfit(costPerCut, salePrice, lengths):
    # totalprofit = (TotalUniformRods x SaleLength x SalePrice) - (TotalCuts x CostperCut)
    new = []
    for i in lengths:
        if i%2 != 0:
            new.append(i-1)
        else:
            new.append(i)
    x = 26/2
    (10*x)
print(maxProfit(1,10,[26,103,59]))