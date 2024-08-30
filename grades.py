
def compute_hw_average(grades):
    if len(grades) == 0:
        return 0
    return sum(grades) / len(grades)]

def compute_hw_max(grades):
    if len(grades) == 0:
        return 0
    return max(grades)
