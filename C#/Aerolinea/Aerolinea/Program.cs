using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Aerolinea
{
    class Program
    {
        static void Main(string[] args)
        {
            int  manuel, juan;
            string entrada, entrada2, entrada3;
            Console.WriteLine("Escriba el nombre de la aerlonia.");
            entrada = Console.ReadLine();
            Convert.ToString(entrada);
            Console.WriteLine("Escriba la Clave del vuelo");
            entrada2 = Console.ReadLine();
            Convert.ToString(entrada2);
            Console.WriteLine("Ciudad a la que viaja");
            entrada3 = Console.ReadLine();
            Convert.ToString(entrada3);
            Console.WriteLine("Nombre de la arelonia: {0}", entrada);
            Console.WriteLine("Clave de vuelo: {0}", entrada2);
            Console.WriteLine("Ciudad a la que viaja: {0}", entrada3);
        }
    }
}
