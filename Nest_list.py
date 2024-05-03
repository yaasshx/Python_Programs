if __name__ == '__main__':
    name_list=[]
    score_list=[]
    records=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
        name_list.append(name)
        score_list.append(score)
    score_list=list(set(score_list))
    score_list.sort()
    second_low=score_list[1]
    out=[i[0] for i in records if i[1]==second_low]
    out.sort()
    for i in out:
        print(i)
