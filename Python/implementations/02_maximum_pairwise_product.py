def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for i in range(n):
        for j in range(i+1, n):
            max_product = max(max_product, numbers[i] * numbers[j])
    return max_product


if __name__ == '__main__':
    _ = input()
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
