// Fibonacci Methodu
// Fibonacci dizisi kendinden önceki 2 sayının toplamıdır. Bu dizi matematikte formülü f(n) = f(n-1) + f(n-2) ile ifade edilebilir.

using System;

internal class Fibonacci
{
    public static void fibonacciTablo(int n)
    {
        if (n == 0) // eğer n 0 ise direkt döndür
        {
            return;
        }

        int[] f = new int[n + 1]; // fibonacci değerlerinin saklandığıı dizi

        // fibonacci dizisi 0 1 1 2 3 5 8 13... olarak gider başlangıçta bize ilk 2 eleman lazım
        f[0] = 0;
        f[1] = 1;

        for (int i = 2; i <= n; i++) // döngü 2den başlar i değeri n kadar gider her adımda i bir artar
        {
            f[i] = f[i - 1] + f[i - 2]; // matematiksel formülü koda uyarladık
        }

        Console.WriteLine(f[n]);
    }
    static void Main(string[] args)
    {
        Console.Write("Fibonacci Sayısı: ");
        int sayi;

        try
        {
            sayi = int.Parse(Console.ReadLine());
        }
        catch (FormatException) //input olarak sayı yerine harf vs. girilirse programın çökmesini engelle
        {
            Console.WriteLine("Sayı girmediniz");
            return;
        }

        fibonacciTablo(sayi);
        Console.ReadKey();
    }

}

