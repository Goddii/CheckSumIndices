class Solution:

    def twosums(self, nums,target):
        n = len(nums)

        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return 'No pair available to compute target'

sol = Solution()
results = []

while True:
    arr = input('Enter array (q to quit): ')
    if arr == 'q': break

    # convert arr to a list
    lst_arr = list(map(int, arr.split()))

    target = int(input('Enter target value: '))

    ans = sol.twosums(lst_arr, target)
    results.append((lst_arr, ans))

# to print out individual arrays and their values
for index, (lst_arr,ans) in enumerate(results, start=1):
    print(f'Results: {index}')
    print('Array: ', lst_arr)
    print('Indices: ', ans)
