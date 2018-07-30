# coding=utf-8
import time
base_quota = 3500
tax_quota = [1500, 4500, 9000, 35000, 55000, 80000]
tax_rat = [0.03, 0.10, 0.20, 0.25, 0.30, 0.35, 0.45]
tax_quick = [0, 105, 555, 1005, 2755, 5505, 13505]

one_month = 0
two_month = 0


# 主线程执行函数
def run():
    year_bonus = input('Please input bonus\n')
    month_salary = input('Please input salary\n')

    # 获取三种方案的税额（不拆分、拆入一个月、拆入两个月）
    start_time = time.clock()
    year_bonus_tax = get_only_bonus_tax(year_bonus, month_salary)
    one_month_tax = get_one_month_bonus(year_bonus, month_salary)
    two_month_tax = get_two_month_bonus(year_bonus, month_salary)

    # 取最小税额并计算税后奖金
    min_tax = min(year_bonus_tax, one_month_tax, two_month_tax)
    bonus_remain = year_bonus - min_tax

    if min_tax == year_bonus_tax:
        print year_bonus, "0", "0", bonus_remain
    elif min_tax == one_month_tax:
        print year_bonus - one_month, one_month, "0", bonus_remain
    elif min_tax == two_month_tax:
        print year_bonus - (two_month * 2), two_month, two_month, bonus_remain
    else:
        return
    end_time = time.clock()
    print(u"耗时："),
    print (end_time - start_time)
    run()
    return


# 获取税率等级
def get_tax_num(money):
    for i in range(len(tax_quota)):
        if money > tax_quota[-1]:
            return len(tax_quota)
        elif money <= tax_quota[i]:
            return i
        else:
            continue


# 获取税率
def get_tax_rat(money):
    return rat(get_tax_num(money))


# 获取速算扣除数
def get_tax_quick(money):
    return quick(get_tax_num(money))


def rat(num):
    if num < len(tax_rat):
        return tax_rat[num]
    else:
        print "function rat error"


def quick(num):
    if num < len(tax_quick):
        return tax_quick[num]
    else:
        print "function quick error"


# 获取平常月交税金额
def get_month_tax(money):
    if money <= base_quota:
        return 0
    else:
        money -= base_quota
        return money * get_tax_rat(money) - get_tax_quick(money)


# 获取年奖平均月交税金额
def get_per_month_tax(money):
    return money * get_tax_rat(money) - get_tax_quick(money)


# 获取不拆分年奖交税总额
def get_only_bonus_tax(year_bonus, month_salary):
    if month_salary <= base_quota:
        if year_bonus < base_quota - month_salary:
            return 0
        else:
            per_month = (year_bonus - (base_quota - month_salary)) / 12.0
            tax = (year_bonus - (base_quota - month_salary)) * get_tax_rat(per_month) - get_tax_quick(
                per_month)
    else:
        per_month = year_bonus / 12.0
        tax = year_bonus * get_tax_rat(per_month) - get_tax_quick(per_month)

    return tax


# 获取拆分为一个月交税总额
def get_one_month_bonus(year_bonus, month_salary):
    now_bonus_tax = get_only_bonus_tax(year_bonus, month_salary)
    for i in range(1, int(year_bonus)):
        bonus_remain = year_bonus - i
        month_add_salary = month_salary + i
        month_tax_add = get_month_tax(month_add_salary) - get_month_tax(month_salary)
        bonus_tax = round(get_only_bonus_tax(bonus_remain, month_salary) + month_tax_add, 2)

        if bonus_tax < now_bonus_tax:
            now_bonus_tax = bonus_tax
            global one_month
            one_month = i
    return now_bonus_tax


# 获取拆分为两个月交税总额
def get_two_month_bonus(year_bonus, month_salary):
    now_bonus_tax = get_only_bonus_tax(year_bonus, month_salary)
    for i in range(1, int(year_bonus)):
        bonus_remain = year_bonus - i
        month_add_salary = month_salary + (i / 2.0)
        month_tax_add = (get_month_tax(month_add_salary) - get_month_tax(month_salary)) * 2.0
        bonus_tax = round(get_only_bonus_tax(bonus_remain, month_salary) + month_tax_add, 2)

        if bonus_tax < now_bonus_tax:
            now_bonus_tax = bonus_tax
            global two_month
            two_month = i / 2.0
    return now_bonus_tax


# 运行主函数
run()


# 注意此算法仅能实现功能，没有做多线程，没有进行优化。
