#프로그래머스 - 스킬트리
def solution(skill, skill_trees):
    tree_len = len(skill_trees)
    answer = 0
    for i in range(tree_len):
        skill_list = list(skill)
        for k in skill_trees[i]:
            if k in skill:
                if (k == skill_list[0]):
                    skill_list.pop(0)
                else:
                    answer -= 1
                    break
            else:
                continue
        answer += 1
    return answer