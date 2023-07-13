dic_sum = {'국어': 0, '수학': 0, '영어': 0, '도덕': 0, '물리': 0} #과목 데이터 사전
key_list = dic_sum.keys()
total = 0

for key in key_list:
    dic_sum[key] = int(input(f'{key}의 점수를 입력하시오: '))
    total += dic_sum[key]

avg = total/5
print(f"전체 평균 점수: {avg}")