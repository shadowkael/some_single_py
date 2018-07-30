__author__ = 'lenovo'


class Solution:
    # @param str: a string
    # @return an integer
    def atoi(self, str):
        # write your code here
        str = str.strip()
        new_str = ''
        num_flag = True
        legal_flag = 2
        for i in str:
            try:
                num_i = int(i)
                str_i = '%s' % num_i
                new_str += str_i
                legal_flag = 2
            except ValueError:
                legal_flag -= 1
                if not new_str and legal_flag == 0:
                    return 0
                if '.' == i:
                    index = str.index('.')
                    for inner in str[index + 1:]:
                        if inner != '0':
                            break
                    else:
                        return int(str[:index])
                elif '-' == i:
                    num_flag = False
                    continue
                elif '+' == i and not new_str:
                    continue
                elif not new_str:
                    return 0
                else:
                    if num_flag:
                        return_num = int(new_str)
                    else:
                        return_num = -int(new_str)
                    return return_num

        if not len(new_str):
            return 0

        if num_flag:
            return_num = int(new_str)
        else:
            return_num = -int(new_str)

        if return_num >= 2147483647:
            return 2147483647
        elif return_num <= -2147483648:
            return -2147483648
        else:
            return return_num


test = Solution()
print test.atoi(' -00000012d121212121212121')
