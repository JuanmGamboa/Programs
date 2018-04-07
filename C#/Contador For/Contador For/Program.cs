using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;

namespace Contador_For
{
    class Program
    {
        static void Main(string[] args)
        {
            int i, n;
            string entrada;
            Console.WriteLine("Contador");
            Console.WriteLine("¿Hasta que número desea contar?");
            entrada = Console.ReadLine();
            n = Convert.ToInt32(entrada);
            for (i= 1; i<=n; i++)
            {
                Console.WriteLine("{0}", i); // Cuenta de 1 hasta n
                Thread.Sleep(100);
                
            }
            for (i = n; i >= 1; i--) // Cuenta regresiva de n hasta 1
            {
                Console.WriteLine("{0}", i);
                Thread.Sleep(100);
            }

        }
    }
}
