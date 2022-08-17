# ведёт к кольцевому импорту
# from import4 import IM4

import import4

IM5 = 500

IM5 = 550
print(f"\n{IM5 = }")
# также ведёт к кольцевому импорту, потому что пытается обратиться к выполняемому главному модулю
print(f"\n{import4.import5.IM5 = }")
