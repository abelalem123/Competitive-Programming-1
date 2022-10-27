use a dp which is of length of string +1 intialize them with false
dp[0]=True
you calculate dp for each index in range(len(s)
at each index check if it matches with one of words in the worddict
then if it matches the dp[current index] will be what ever the (dp was if you minused the length of the matched word from the current index.)
answer will be stored at the last index