def ventana_consulta(self, ):
                self.root = Tk()
                self.root.title("Consulta")
                self.root.geometry("300x180")
                self.root.iconbitmap("d:\Desktop\PYTHON\CODO A CODO\Etapa Phython\TPFINAL\codoacodo.ico")
        
                self.var_id_cons = StringVar()        
                self.var_nom_cons = StringVar()
                self.var_cat_cons = StringVar()
                self.var_proc_cons = StringVar()


        
                self.busc_id=Label(self.root, text="Buscar por ID").grid(row=0, column=0, sticky="W", padx=5)
                self.busc_nom=Label(self.root, text="Buscar por Nombre").grid(row=1, column=0, sticky="W", padx=5)
                
                
                self.busc_id_entry = Entry(self.root, textvariable=self.var_id_cons, width=20).grid(row=0, column=1, padx=10, pady=5)
                self.busc_nom_entry = Entry(self.root, textvariable=self.var_nom_cons, width=20).grid(row=1, column=1, padx=10, pady=5)
                        
                self.cat= Label (self.root, text="Buscar por Categoría").grid(row=2, column=0, sticky="w", padx=5, pady=5)
                self.proce= Label (self.root, text="Buscar por Procedencia").grid(row=3, column=0, sticky="w", padx=5, pady=5)              
                
                self.categ = ["Herramientas", "Consumibles", "Otros" ]
                self.entry_categoria = ttk.Combobox(self.root, values= self.var_cat_cons ,  textvariable=self.var_categoria, width=17)
                self.entry_categoria.grid(row=2, column=1, pady=5)
                self.proc = ["Nacional", "Importado"]
                self.entry_procedencia = ttk.Combobox(self.root, values= self.var_proc_cons, textvariable=self.var_procedencia, width=17)
                self.entry_procedencia.grid(row=3, column=1, pady=5)

                self.boton_b = Button(self.root, text="Buscar", command=lambda:self.consular_reporte_vista2(self.var_categoria, self.var_a, self.tree), width=10)
                self.boton_b.grid(row=4, column=0, pady=15)
                self.boton_c = Button(self.root, text="Cancelar", command= lambda: self.quit() , width=10)
                self.boton_c.grid(row=4, column=1, pady=15)
                
                self.root.mainloop()
        
        def quit(self):
                self.root.destroy()

        def consular_reporte_vista2(self, a, b, c, d, tree):
                print(a, b, c, d, tree)
                #self.obj_de_modelo.consulta_reporte_mod(a, b, c, d, tree)
                self.quit()
                