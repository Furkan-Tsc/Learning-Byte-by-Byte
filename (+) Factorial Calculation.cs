// Factorial
// Faktöriyel 1den n. sayıya kadar olan tüm sayıların çarpımıdır yani n! = 1.2.3.4.....n

using System;
using System.Numerics; // BigInteger için gerekli referans

internal class Program
{
    public static void Main(string[] args)
    {
        BigInteger sonuc = 1; // int in 32 bitlik alanı olduğu için 12! hesaplanabilirken 13! hesaplanamıyor bu yüzden int yerine sınırsız sayı tutabilen bigint kullandık
        int sayi;

        Console.Write("Sayı Giriniz: ");

        try
        {
            sayi = int.Parse(Console.ReadLine());
        }
        catch (FormatException) //input olarak sayı yerine harf vs. girilirse programın çökmesini engelle
        {
            Console.WriteLine("Sayı girmediniz");
            return;
        }

        for (int i = sayi; i > 0 ; i--) // hesaplama için sayıyı 1e kadar tek tek azalt
        {
            sonuc *= i; // sayi dan 1 kadar olan sayıların çarpımı
        }
        Console.WriteLine($"{sayi}!: " + sonuc);
    }
}
