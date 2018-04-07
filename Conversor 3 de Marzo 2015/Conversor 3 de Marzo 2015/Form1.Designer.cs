namespace Conversor_3_de_Marzo_2015
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.Pulgadas = new System.Windows.Forms.TextBox();
            this.Pies = new System.Windows.Forms.TextBox();
            this.Metros = new System.Windows.Forms.TextBox();
            this.Centimetros = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.Convertir = new System.Windows.Forms.Button();
            this.Borrar = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // Pulgadas
            // 
            this.Pulgadas.Location = new System.Drawing.Point(54, 43);
            this.Pulgadas.Name = "Pulgadas";
            this.Pulgadas.Size = new System.Drawing.Size(100, 20);
            this.Pulgadas.TabIndex = 0;
            // 
            // Pies
            // 
            this.Pies.Location = new System.Drawing.Point(54, 85);
            this.Pies.Name = "Pies";
            this.Pies.Size = new System.Drawing.Size(100, 20);
            this.Pies.TabIndex = 1;
            // 
            // Metros
            // 
            this.Metros.Location = new System.Drawing.Point(54, 134);
            this.Metros.Name = "Metros";
            this.Metros.Size = new System.Drawing.Size(100, 20);
            this.Metros.TabIndex = 2;
            // 
            // Centimetros
            // 
            this.Centimetros.Location = new System.Drawing.Point(54, 188);
            this.Centimetros.Name = "Centimetros";
            this.Centimetros.Size = new System.Drawing.Size(100, 20);
            this.Centimetros.TabIndex = 3;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(77, 25);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(51, 13);
            this.label1.TabIndex = 4;
            this.label1.Text = "Pulgadas";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(88, 69);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(27, 13);
            this.label2.TabIndex = 5;
            this.label2.Text = "Pies";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(88, 118);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(39, 13);
            this.label3.TabIndex = 6;
            this.label3.Text = "Metros";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(77, 172);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(62, 13);
            this.label4.TabIndex = 7;
            this.label4.Text = "Centimetros";
            // 
            // Convertir
            // 
            this.Convertir.Location = new System.Drawing.Point(223, 82);
            this.Convertir.Name = "Convertir";
            this.Convertir.Size = new System.Drawing.Size(75, 23);
            this.Convertir.TabIndex = 8;
            this.Convertir.Text = "Convertir";
            this.Convertir.UseVisualStyleBackColor = true;
            this.Convertir.Click += new System.EventHandler(this.Convertir_Click);
            // 
            // Borrar
            // 
            this.Borrar.Location = new System.Drawing.Point(223, 146);
            this.Borrar.Name = "Borrar";
            this.Borrar.Size = new System.Drawing.Size(75, 23);
            this.Borrar.TabIndex = 9;
            this.Borrar.Text = "Borrar";
            this.Borrar.UseVisualStyleBackColor = true;
            this.Borrar.Click += new System.EventHandler(this.Borrar_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(433, 224);
            this.Controls.Add(this.Borrar);
            this.Controls.Add(this.Convertir);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.Centimetros);
            this.Controls.Add(this.Metros);
            this.Controls.Add(this.Pies);
            this.Controls.Add(this.Pulgadas);
            this.Name = "Form1";
            this.Text = "Conversion Metrica 6.6";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox Pulgadas;
        private System.Windows.Forms.TextBox Pies;
        private System.Windows.Forms.TextBox Metros;
        private System.Windows.Forms.TextBox Centimetros;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Button Convertir;
        private System.Windows.Forms.Button Borrar;
    }
}

