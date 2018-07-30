# coding=utf-8
import sys

if __name__ == "__main__":
    while True:
        input_data = sys.stdin.readline().strip()
        if not input_data:
            break
        n, m, ceo = input_data.split()
        n = int(n)
        m = int(m)
        # 存入房间布局，单独记录总裁位置
        table_map = []
        ceo_location = []
        for i in range(n):
            cow = []
            for bean in sys.stdin.readline().strip():
                cow.append(bean)
            table_map.append(cow)

        for row in table_map:
            for cow in row:
                if cow == ceo:
                    ceo_location.append([row, cow])
        ass_location = []
        # 把总裁的位置向四周扩一圈，找有几个颜色
        for bean in ceo_location:
            if bean[0] == 0:
                pass
            if bean[1] == 0:
                pass


