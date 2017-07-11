# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
total_cost=float(input("Enter the total cost:"))
annual_salary=float(input("Enter annual salary:"))

portion_down_payment=0.25
current_saving=float(0)
r=0.04
monthly_salary=annual_salary/12.0
months=0
semi_annual_raise=float(input("Enter the percent of your salary to save, as a decimal:"))
i=0
j=10000
bise=1
jump=False
while i<=j:
    current_saving=0
    months=0
    q=int((i+j)/2)
    portion_saved=float(q/10000)
    need_months=0
    monthly_salary=annual_salary/12.0
    while need_months<48:
        current_saving=monthly_salary*portion_saved+current_saving*r/12+current_saving
        months=months+1
        need_months=need_months+1
        if months%6==0:
            monthly_salary=monthly_salary+monthly_salary*semi_annual_raise
    print(current_saving)
    print(portion_saved)
    if (current_saving>total_cost*portion_down_payment-10000)and(current_saving<total_cost*portion_down_payment+10000):
        jump=True
        break
    else:
        bise=bise+1
        if current_saving<total_cost*portion_down_payment:
            i=q+1
        else:
            j=q-1

if not jump:
    print("impossible")
else:
    print("Number of months",months)
    print(bise)
    print(q/10000)
