wage = float(input("How much do you make an hour?:   "))
hours = float(input("How many hours have you worked?:   "))

pre_tax = wage * hours
print(f"Pre-tax earnings were ${wage}*{hours} = ${pre_tax} for the week.")
post_tax = 0
def earnings(pre_tax, post_tax):
     if pre_tax >= 2000:
        post_tax = pre_tax * .7
        print(f"Post-tax earnings were ${pre_tax}*.7( since we fall in the higher tax bracket) = ${post_tax} for the week")
     else:
        post_tax = pre_tax * .85
        print(f"Post-tax earnings were ${pre_tax}*.85( since we fall in the lower tax bracket) = ${post_tax} for the week")
earnings(pre_tax, post_tax)
