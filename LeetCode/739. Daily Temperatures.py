def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
    answer = [0] * len(temperatures)
    stack = []
    for curr_day, curr_temp in enumerate(temperatures) :
        while stack and curr_temp > stack[-1][1] :
            prev_day, _ = stack.pop()
            answer[prev_day] = curr_day - prev_day
        stack.append((curr_day, curr_temp))
    return answer
            