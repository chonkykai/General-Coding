def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return []
    else:
        negative = [i for i in arr if i < 0]
        positive = [x for x in arr if x > 0]
        return [len(positive), sum(negative)]



print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
print(count_positives_sum_negatives([0,0,0]))