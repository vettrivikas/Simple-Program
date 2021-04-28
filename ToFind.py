class Ideone
{
	public static int totalWays(int n)
    {
       
        if (n < 0) {
        	return 0;
        }

        if (n == 0) {
        	return 1;
        }
        return totalWays(n - 1) + totalWays(n - 2) + totalWays(n - 3);
    }
 
	public static void main (String[] args) throws java.lang.Exception
	{
		int n = 4;
        		System.out.printf("Total ways to reach the %d'th stair are %d",n, totalWays(n));
	}
	
}