import math



def init():
    total = input('please input the number of total card:\n')
    every_card = input('please input the number of everyone should take:\n')
    # last_status = input('please define take the last one win or lose:\n')
    last_status = True


def output_style(first_take, held_num):
    print('First take:', first_take, 'cards')
    print('and you need held', held_num)


def get_answer():
    total = input('please input the number of total card:\n')
    every_card = input('please input the number of everyone should take:\n')
    last_status = input("please define take the last one win or lose:\n,win input '1', lose input '0'\n")
    # last_status = True

    loop_num = int(math.ceil(total / every_card))
    for j in range(1, every_card + 1):
        for i in range(loop_num):
            if last_status:
                if total == j + (i * (every_card + 1)):
                    plan_dic = dict()
                    plan_dic['first_take'] = j
                    plan_dic['held_num'] = every_card + 1
                    plan_dic['times'] = i
                    print plan_dic
            else:
                if total == j + ((i - 1) * (every_card + 1)) + every_card:
                    plan_dic = dict()
                    plan_dic['first_take'] = j
                    plan_dic['held_num'] = every_card + 1
                    plan_dic['times'] = i
                    print plan_dic
    get_answer()

# output_style(get_answer()[0], get_answer()[1])
