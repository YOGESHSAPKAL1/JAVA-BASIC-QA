import java.io.*; // for handling input/output
import java.util.*; // contains Collections framework

// don't change the name of this class
// you can add inner classes if needed
class Main {
  public static void main(String args[])
 {
     Scanner sc= new Scanner(System.in);
    int n= sc.nextInt();
    int a[]=new int[n];
    double rms=0;
    double sum=0;
    for (int i=0;i<n;i++)
    {
        a[i]=sc.nextInt();
        sum=sum+a[i]*a[i];

    }
    double ans =sum/n;
    rms=rms+Math.sqrt(ans);
    System.out.format("%.6f", rms);
 }
}