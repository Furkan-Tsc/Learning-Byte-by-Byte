// Basit bir taş kağıt makas oyunu / büyük küçük harfe duyarlıdır
using System;
using System.Collections.Generic;

internal class Program
{
    public static void Main(string[] args)
    {
        List<string> ogeler = new List<string> { "Taş", "Kağıt", "Makas" }; // indexler -> taş = 0, kağıt = 1, makas = 2
        var random = new Random();
        int index = random.Next(ogeler.Count); // rastgele seçim

        Console.WriteLine("Taş/Kağıt/Makas (T/K/M): ");
        string secim = Console.ReadLine();
        Console.WriteLine("vs");
        Console.WriteLine(ogeler[index]);

        if (secim == ogeler[index]) // beraberlik
        { Console.WriteLine("Berabere"); }

        // kaybetmeler
        else if ((secim == "Makas" || secim == "M" && index == 0) || // Makas vs Taş - Taş alır
                 (secim == "Taş" || secim == "T" && index == 1) ||   // Taş vs Kağıt - Kağıt alır
                 (secim == "Kağıt" || secim == "K" && index == 2))   // Kağıt vs Makas - Makas alır
        { Console.WriteLine("Kaybettin"); }

        // kazanmalar
        else if ((secim == "Makas" || secim == "M" && index == 1) || // Makas vs Kağıt - Makas alır
                 (secim == "Taş" || secim == "T" && index == 2) ||   // Taş vs Makas - Taş alır
                 (secim == "Kağıt" || secim == "K" && index == 0))   // Kağıt vs Taş - Kağıt alır
        { Console.WriteLine("Kazandın"); }

        else { Console.Clear();  Console.WriteLine("Hatalı girdi"); } // hatalı girdiler
    }
}

