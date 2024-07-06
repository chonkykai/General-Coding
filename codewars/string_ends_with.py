def solution(text, ending):
    if (ending in text[-len(ending):]):
        return True
    return False

print(solution("samurai", "ra"))
print(solution('abc', 'd'))
print(solution("samurai", "ai"))