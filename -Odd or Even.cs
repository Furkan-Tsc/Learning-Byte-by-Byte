using System;

namespace Odd_or_Even
{
    internal class Program
    {
        static void Main(string[] args)
        {
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

            if (sayi % 2 == 0) // sayinin 2ye bölümünden kalan 0 ise çift
            {
                Console.WriteLine("Sayı Çift");
            }
            else // değilse tek
            {
                Console.WriteLine("Sayı Tek");
            }

            Console.ReadKey();
        }
    }
}
