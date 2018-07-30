__author__ = 'lenovo'
# import sys
while True:
    input_data = raw_input().strip()
    if not input_data:
        break
    else:
        people = int(input_data)
        heights = raw_input().strip().split()
        if len(heights) == 1:
            print 1
        else:
            left_find = right_find = True
            sub_left = []
            for index, height in enumerate(heights):
                if index == 0:
                    continue
                if heights[index - 1] < height:
                    sub_left.append(height)
