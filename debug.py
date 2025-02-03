import pdb

for i in range(10):
    print(i)
    if i == 5:
        five = 5
        
def add(x, y):
    pdb.set_trace()  # 여기서 코드 실행이 멈추고 디버거 모드로 전환됩니다.
    return x + y

result = add(3, 5)
print(result)