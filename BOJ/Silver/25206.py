rank_dict = {"A+" : 4.5, "A0" : 4.0, "B+" : 3.5, "B0" : 3.0, "C+" : 2.5, "C0" : 2.0, "D+" : 1.5, "D0" : 1.0, "F": 0.0}
total_score = 0.0   # 학점의 총합
score_subject = 0   # 학점 * 과목평점

for _ in range(20) :
    subject_name, score, rank = input().split()
    if rank == "P" :
        continue
    score_subject += float(score) * rank_dict[rank]
    total_score += float(score)
print(score_subject / total_score)