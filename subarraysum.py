def subArraySum(arr, n, sum_):
    # string starting point
    for i in range(n):
        currentSum = arr[i]

        # try all subarrays starting with i
        j = i + 1
        while j <= n:
            if currentSum == sum_:
                print("Sum found between")
                print("indexes % d and % d" % (i, j - 1))
                return 1

            if currentSum > sum_ or j == n:
                break

            currentSum = currentSum + arr[j]
            j += 1

    print("No subarray found")
    return 0


# Driver program
if __name__ == '__main__':
    arr = [15, 9, 5, 10, 23, 4, 2, 1]
n = len(arr)
sum_ = 30

subArraySum(arr, n, sum_)