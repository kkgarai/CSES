import java.util.Arrays;
import java.util.Scanner;

class CoinCombinations2 {
    public static void main(String[] args) {
        int mod = (int) (1e9 + 7);
        Scanner sc = new Scanner(System.in);
        int n, x;
        n = sc.nextInt();
        x = sc.nextInt();
        // sc.nextLine();
        // int[] coins = Arrays.stream(sc.nextLine().split("
        // ")).mapToInt(Integer::parseInt).toArray();
        // System.out.println(coins.toString());
        int[] coins = new int[n];
        for (int i = 0; i < n; i++)
            coins[i] = sc.nextInt();
        long dp[] = new long[x + 1];
        Arrays.fill(dp, 0);
        dp[0] = 1;
        for (int c : coins) {
            for (int i = c; i <= x; i++) {
                dp[i] = (dp[i] + dp[i - c]) % mod;

            }
        }

        System.out.println(dp[dp.length - 1]);
    }
}