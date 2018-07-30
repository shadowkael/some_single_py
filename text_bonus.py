from bonus_plan import get_month_tax, get_only_bonus_tax


def test():
    total = input("total:\n")
    month_salary = input("month_salary:\n")
    bonus = input("bonus:\n")
    month_1 = input("month 1:\n")
    month_2 = input("month 2:\n")
    bonus_tax = get_only_bonus_tax(bonus, month_salary)
    month_1_tax = get_month_tax(month_1)
    month_2_tax = get_month_tax(month_2)

    print("bonus_tax:", bonus_tax)
    print("month_1_tax:", month_1_tax)
    print("month_2_tax:", month_2_tax)

    bonus_remain = total - bonus_tax - (get_month_tax(month_salary + month_1) - get_month_tax(month_salary)) - (
    get_month_tax(month_salary + month_2) - get_month_tax(month_salary))
    print("bonus_remain:", bonus_remain)

    test()


test()
