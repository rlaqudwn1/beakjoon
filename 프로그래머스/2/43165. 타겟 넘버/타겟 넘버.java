class Solution {
      static int answer =0;
    public int solution(int[] numbers, int target) {

        dfs(numbers, 0, target, 0);

        return answer;

    }
    private void dfs(int[] numbers, int result, int target, int i) {
        if (i == numbers.length) {
            if (result == target) {
                answer++;
            }
            return;
        }
        dfs(numbers, result - numbers[i], target, i + 1);
        dfs(numbers, result + numbers[i], target, i +1);
    }
}