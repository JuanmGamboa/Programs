using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Convercion_C_F_K
{
    class Program
    {
        static void Main(string[] args)
        {
            double C, F, K;
            string texto;
            int entrada;
            Console.WriteLine("Converciones");
            Console.WriteLine("Seleciona una opcion\n");
            Console.WriteLine("1.- Convertir de  Centigrados a Fahrenheit\n");
            Console.WriteLine("2.- Convertir de Fahrenheit a Centigrados\n");
            Console.WriteLine("3.- Convertir de Centigrados a Kelvin\n");
            Console.WriteLine("4.- Convertir de Kelvin a Centigrados\n");
            Console.WriteLine("5.- Convertir de Kelvin a Fahrenheit\n");
            Console.WriteLine("6.- Convertir de Fahrenheit a Kelvin\n");
            texto = Console.ReadLine();
            entrada = Convert.ToInt32(texto);
            if (entrada == 1)
            {
                Console.WriteLine("\nDame el valor en Centigrados:\n");
                texto = Console.ReadLine();
                C = Convert.ToDouble(texto);
                F = 1.8*C+32;
                Console.WriteLine("\nLa temperatura en Fahrenheit es: {0}", F);
              
            }
            else if (entrada == 2)
            {
                Console.WriteLine("\nDame el valor en Fahrenheit:\n");
                texto = Console.ReadLine();
                F = Convert.ToDouble(texto);
                C = (F - 32) / 1.8;
                Console.WriteLine("\nLa temperatura en Centigrados es: {0}", C);
               
            }
             else if (entrada == 3)
            {
                Console.WriteLine("\nDame el Valor en Centigrados:\n");
                texto = Console.ReadLine();
                C = Convert.ToDouble(texto);
                K = C + 273.15;
                Console.WriteLine("\nLa temperatura en grados Kelvin es: {0} ", K);
             
            }
             else if (entrada == 4)
            {
               Console.WriteLine("\nDame el Valor en Kelvin:\n");
               texto = Console.ReadLine();
               K = Convert.ToDouble(texto);
               C = K - 273.15;
               Console.WriteLine("\nLa temperatura en grados Centigrados es: {0} ", C);

            }
            else if (entrada == 5)
            {
                Console.WriteLine("\nDame el Valor en Kelvin:\n");
                texto = Console.ReadLine();
                K = Convert.ToDouble(texto);
                F = 1.8 * (K - 273.15) + 32;
                Console.WriteLine("\nLa temperatura en grados Fahrenheit es: {0} ", F);
            }
            else if (entrada == 6)
            {
                Console.WriteLine("\nDame el Valor en Fahrenheit:\n");
                texto = Console.ReadLine();
                F = Convert.ToDouble(texto);
                K = (F - 32) / 1.8 + 273.15;
                Console.WriteLine("\nLa temperatura en grados Kelvin es: {0} ", K);
            }
            else
            {
                Console.WriteLine("Opción no valida");
            }

        }
    }
}
