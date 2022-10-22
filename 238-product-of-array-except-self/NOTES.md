#  New solution o(1) space and o(n) time
first compute prefix for each element, and append the result list, **for first element
it will just be 1**, for others it will be the number before them times the result we compute before i.e            ****      pre=nums[i-1]*res[i-1] res.append(pre)****
​
then compute post fix for each element starting from -2 index and multiply it by the prefix you already stored at the result set.  i.e maintain **a post variable** for the last element you don't need to compute postfix (since there is none)
​
# old solution o(n) space and o(n) time
compute prefix and postfix for each element i ds
when computing prefix start from index 1, **since index 0 has no prefix, prefix[0]=num[0] to help the next computation.**
when  computing postfix start from index -2 (before last) **since nums[-1] has no postfix element postfix[-1]=nums[-1]**
then **res is prefix[i-1] * postfix[i+1]**
when printing make sure you are not using the above formula since 0 and -1 index has no prefix and postfix respectively so use one of them.