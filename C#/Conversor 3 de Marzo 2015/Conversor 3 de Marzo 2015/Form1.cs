using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Conversor_3_de_Marzo_2015
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Convertir_Click(object sender, EventArgs e)
        {
            float pulgada, pie, metro, centimetro;
            if (Pies.Text == "" && Metros.Text == "" && Centimetros.Text == "")
            {
                pulgada = Convert.ToSingle(Pulgadas.Text);
                pie = pulgada / 12f;
                centimetro = 2.54f * pulgada;
                metro = centimetro / 100f;
                Pies.Text = Convert.ToString(pie);
                Metros.Text = Convert.ToString(metro);
                Centimetros.Text = Convert.ToString(centimetro);
            }
            if (Pulgadas.Text == "" && Metros.Text == "" && Centimetros.Text == "")
            {
                pie = Convert.ToSingle(Pies.Text);
                pulgada = pie * 12f;
                centimetro = 2.54f * pulgada;
                metro = centimetro / 100f;
                Pulgadas.Text = Convert.ToString(pulgada);
                Metros.Text = Convert.ToString(metro);
                Centimetros.Text = Convert.ToString(centimetro);
            }
            if (Pies.Text == "" && Pulgadas.Text == "" && Centimetros.Text == "")
            {
                metro = Convert.ToSingle(Metros.Text);
                centimetro = 100f * metro;
                pulgada = centimetro * 2.54f;
                pie = 12f * pulgada;
                Pies.Text = Convert.ToString(pie);
                Pulgadas.Text = Convert.ToString(pulgada);
                Centimetros.Text = Convert.ToString(centimetro);
            }
            if (Pies.Text == "" && Metros.Text == "" && Pulgadas.Text == "")
            {
                centimetro = Convert.ToSingle(Centimetros.Text);
                pulgada = centimetro / 2.54f ;
                pie = pulgada / 12f;
                metro = centimetro / 100f;
                Pies.Text = Convert.ToString(pie);
                Metros.Text = Convert.ToString(metro);
                Pulgadas.Text = Convert.ToString(pulgada);
            }
        }

        private void Borrar_Click(object sender, EventArgs e)
        {
            Pulgadas.Text = "";
            Metros.Text = "";
            Pies.Text = "";
            Centimetros.Text = "";

        }
    }
}