sales=[1200, 1500, 900, 1800, 2200, 1700, 1300]
total_sales=sum(sales)
highest_sale=max(sales)
lowest_sale=min(sales)
average_sales=total_sales/len(sales)
No_of=0
for i in sales:
    if i>1500:
        No_of += 1
print("total sales : ", total_sales)
print("average sales : ", average_sales)
print("highest sale : ", highest_sale)
print("lowest sale : ", lowest_sale)
print("number of sales above 1500 : ", No_of)
