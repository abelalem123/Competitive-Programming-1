class Solution {
    public String removeKdigits(String num, int k) {
        Stack<Character> stack = new Stack<Character>();
        int i=0;
        while(i<num.length()){
            while (k>0 && !stack.isEmpty() && num.charAt(i)<stack.peek()){
                stack.pop();
                k--;
            }
            if (!stack.isEmpty() || num.charAt(i)!='0'){
            stack.push(num.charAt(i));
            }
            i++;
        }
        while(k>0 && !stack.isEmpty()){
            stack.pop();
            k--;
        }
        StringBuilder result=new StringBuilder();
        while (!stack.isEmpty()){
            result.append(stack.pop());
        }
        result.reverse();
        String temp=result.toString();
        if (temp==""){
            return "0";
        }
        return temp;
    }
}