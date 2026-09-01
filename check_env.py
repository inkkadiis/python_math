# 환경이 제대로 설치되었는지 확인하는 스크립트
# 실행: python check_env.py

import numpy as np
import scipy
import sympy as sp
import matplotlib
import pandas as pd

print(f"numpy      {np.__version__}")
print(f"scipy      {scipy.__version__}")
print(f"sympy      {sp.__version__}")
print(f"matplotlib {matplotlib.__version__}")
print(f"pandas     {pd.__version__}")

# 간단한 수학 예제
# 1) numpy: 행렬 연산
A = np.array([[1, 2], [3, 4]])
print("\n행렬 A의 역행렬:\n", np.linalg.inv(A))

# 2) sympy: 기호 수학 (미분/적분)
x = sp.symbols("x")
f = x**2 * sp.sin(x)
print("\nf(x) = x²·sin(x)")
print("f'(x) =", sp.diff(f, x))
print("∫f dx =", sp.integrate(f, x))
