import java.util.LinkedList;
import java.util.Queue;

class Solution {
    int[] dx = {1, -1, 0, 0};
    int[] dy = {0, 0, 1, -1};

    public int solution(int[][] maps) {
        int answer = 0;
        int y = maps.length;
        int x = maps[0].length;
        answer = bfs(maps);
        return answer;
    }

    private int bfs(int[][] maps) {
        boolean[][] visited = new boolean[maps.length][maps[0].length];
        Queue<int[]> queue = new LinkedList<>();
        visited[0][0]=true;
        int[] que = {0, 0, 1};
        queue.add(que);
        while (!queue.isEmpty()) {
            int[] q = queue.poll();
            if (q[0] == maps[0].length - 1 && q[1] == maps.length - 1) {
                return q[2];
            }

            for (int i = 0; i < 4; i++) {
                int x = q[0] + dx[i];
                int y = q[1] + dy[i];
                if (x >= 0&&x<maps[0].length&&y>=0&&y< maps.length&&!visited[y][x]) {
                    if (maps[y][x] == 1) {
                        visited[y][x] = true;
                        queue.add(new int[]{x, y, q[2] + 1});
                    }
                }
            }
        }
        return -1;
    }
}