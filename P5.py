# coding=utf-8

from tkinter import *
import hashlib
import urllib2
from pyfingerprint.pyfingerprint import PyFingerprint
#root = Tk()

class prueba:

    fields = 'Cédula', 'Nombre', 'Apellido', 'Sexo', 'Fecha de Nacimiento', 'Tipo de Sangre', 'Compañía de Seguros', 'Número del Seguro', 'Dirección', 'Alergias', 'Condiciones Médicas', 'Contacto de Emergencia #1', 'Contacto de Emergencia #2', 'Centro de Salud Preferido'
    
    def fetch(self,master,entries):
        for entry in entries:
            field = entry[0]
            text = entry[1].get()
            print('%s: "%s"' % (field, text))

        self.del_inf(master)

    def del_inf(self, master):

        self.cedu.delete(0,END)
        self.nomb.delete(0,END)
        self.apel.delete(0,END)
        self.sex.delete(0,END)
        self.naci.delete(0,END)
        self.sang.delete(0,END)
        self.segu.delete(0,END)
        self.nume.delete(0,END)
        self.dire.delete(0,END)
        self.aler.delete(0,END)
        self.cond.delete(0,END)
        self.cont1.delete(0,END)
        self.cont2.delete(0,END)
        self.cent.delete(0,END)
        #for row in rows:
        #    row.destroy()

        #reg()

    def makeform(self,master, fields):
        rows = []
        #for row in rows:
        #    row.destroy()
        entries = []
        self.row0 = Frame (master)
        self.lab0 = Label (self.row0, width = 25, text = fields[0], anchor = 'w')
        self.cedu = Entry(self.row0)
        self.row0.pack(side = TOP, fill = X, padx = 5, pady = 5)
        self.lab0.pack(side = LEFT)
        self.cedu.pack(side = RIGHT, expand = YES, fill = X)

        self.row1 = Frame (master)
        self.lab1 = Label (self.row1, width = 25, text = fields[1], anchor = 'w')
        self.nomb = Entry(self.row1)
        self.row1.pack(side = TOP, fill = X, padx = 5, pady = 5)
        self.lab1.pack(side = LEFT)
        self.nomb.pack(side = RIGHT, expand = YES, fill = X)

        self.row2 = Frame (master)
        self.lab2 = Label (self.row2, width = 25, text = fields[2], anchor = 'w')
        self.apel = Entry(self.row2)
        self.row2.pack(side = TOP, fill = X, padx = 5, pady = 5)
        self.lab2.pack(side = LEFT)
        self.apel.pack(side = RIGHT, expand = YES, fill = X)

        self.row3 = Frame (master)
        self.lab3 = Label (self.row3, width = 25, text = fields[3], anchor = 'w')
        self.sex = Entry(self.row3)
        self.row3.pack(side = TOP, fill = X, padx = 5, pady = 5)
        self.lab3.pack(side = LEFT)
        self.sex.pack(side = RIGHT, expand = YES, fill = X)
        
        self.row4 = Frame (master)
        self.lab4 = Label (self.row4, width = 25, text = fields[4], anchor = 'w')
        self.naci = Entry(self.row4)
        self.row4.pack(side = TOP, fill = X, padx = 5, pady = 5)
        self.lab4.pack(side = LEFT)
        self.naci.pack(side = RIGHT, expand = YES, fill = X)

        self.row5 = Frame (master)
        self.lab5 = Label (self.row5, width = 25, text = fields[5], anchor = 'w')
        self.sang = Entry(self.row5)
        self.row5.pack(side = TOP, fill = X, padx = 5, pady = 5)
        self.lab5.pack(side = LEFT)
        self.sang.pack(side = RIGHT, expand = YES, fill = X)

        self.row6 = Frame (master)
        self.lab6 = Label (self.row6, width = 25, text = fields[6], anchor = 'w')
        self.segu = Entry(self.row6)
        self.row6.pack(side = TOP, fill = X, padx = 5, pady = 5)
        self.lab6.pack(side = LEFT)
        self.segu.pack(side = RIGHT, expand = YES, fill = X)
        
        self.row7 = Frame (master)
        self.lab7 = Label (self.row7, width = 25, text = fields[7], anchor = 'w')
        self.nume = Entry(self.row7)
        self.row7.pack(side = TOP, fill = X, padx = 5, pady = 5)
        self.lab7.pack(side = LEFT)
        self.nume.pack(side = RIGHT, expand = YES, fill = X)

        self.row8 = Frame (master)
        self.lab8 = Label (self.row8, width = 25, text = fields[8], anchor = 'w')
        self.dire = Entry(self.row8)
        self.row8.pack(side = TOP, fill = X, padx = 5, pady = 5)
        self.lab8.pack(side = LEFT)
        self.dire.pack(side = RIGHT, expand = YES, fill = X)

        self.row9 = Frame (master)
        self.lab9 = Label (self.row9, width = 25, text = fields[9], anchor = 'w')
        self.aler = Entry(self.row9)
        self.row9.pack(side = TOP, fill = X, padx = 5, pady = 5)
        self.lab9.pack(side = LEFT)
        self.aler.pack(side = RIGHT, expand = YES, fill = X)

        self.row10 = Frame (master)
        self.lab10 = Label (self.row10, width = 25, text = fields[10], anchor = 'w')
        self.cond = Entry(self.row10)
        self.row10.pack(side = TOP, fill = X, padx = 5, pady = 5)
        self.lab10.pack(side = LEFT)
        self.cond.pack(side = RIGHT, expand = YES, fill = X)

        self.row11 = Frame (master)
        self.lab11 = Label (self.row11, width = 25, text = fields[11], anchor = 'w')
        self.cont1 = Entry(self.row11)
        self.row11.pack(side = TOP, fill = X, padx = 5, pady = 5)
        self.lab11.pack(side = LEFT)
        self.cont1.pack(side = RIGHT, expand = YES, fill = X)

        self.row12 = Frame (master)
        self.lab12 = Label (self.row12, width = 25, text = fields[12], anchor = 'w')
        self.cont2 = Entry(self.row12)
        self.row12.pack(side = TOP, fill = X, padx = 5, pady = 5)
        self.lab12.pack(side = LEFT)
        self.cont2.pack(side = RIGHT, expand = YES, fill = X)

        self.row13 = Frame (master)
        self.lab13 = Label (self.row13, width = 25, text = fields[13], anchor = 'w')
        self.cent = Entry(self.row13)
        self.row13.pack(side = TOP, fill = X, padx = 5, pady = 5)
        self.lab13.pack(side = LEFT)
        self.cent.pack(side = RIGHT, expand = YES, fill = X)
        
        '''
        nume = Entry(row)
        nume.pack(side = RIGHT, fill = X, padx = 5, pady = 5 )
        dire = Entry(row)
        dire.pack(side = RIGHT, fill = X, padx = 5, pady = 5 )
        aler = Entry(row)
        aler.pack(side = RIGHT, fill = X, padx = 5, pady = 5 )
        cond = Entry(row)
        cond.pack(side = RIGHT, fill = X, padx = 5, pady = 5 )
        info = []
        info.extend((cedu,nomb,apel,sex,naci,sang,segu,nume,dire,aler,cond,cont1,cont2,cent))
        print(info)
'''
        rows.extend((self.row0,self.row1,self.row2,self.row3,self.row4,self.row5,self.row6,self.row7,self.row8,self.row9,self.row10, self.row11, self.row12, self.row13))
        info = []
        info.extend((self.cedu,self.nomb,self.apel,self.sex,self.naci,self.sang,self.segu,self.nume,self.dire,self.aler,self.cond,self.cont1,self.cont2,self.cent))
        #print(info)
        n = 0
        for field in fields:
            entries.append((field,info[n]))
            n = n + 1
        
        return entries

    def mostrarVentanaRegistrar(self,master):
        print(self.control)
        if self.control == 2:
            self.del_ventanaBuscar(master)
        if self.control == 3:
            self.del_found(master)
            self.del_ventanaBuscar(master)
        elif self.control == 1:
            return
        self.control = 1
        ents = self.makeform(master,self.fields)
        master.bind('<Return>', (lambda event, e = ents: self.fetch(master,e)))
        self.b1 = Button(master, text = 'Guardar', command = (lambda e = ents: self.fetch(master,e)))
        self.b1.pack(side = LEFT, padx = 5, pady = 5)
        self.b2 = Button(master, text = 'Cancelar', command = lambda: self.del_inf(master))#master.quit)
        self.b2.pack(side = LEFT, padx = 5, pady = 5)

    def del_ventanaRegistrar(self, master):
        self.lab0.destroy()
        self.cedu.destroy()
        self.row0.destroy()

        self.nomb.destroy()
        self.lab1.destroy()
        self.row1.destroy()

        self.apel.destroy()
        self.lab2.destroy()
        self.row2.destroy()

        self.sex.destroy()
        self.lab3.destroy()
        self.row3.destroy()

        self.naci.destroy()
        self.lab4.destroy()
        self.row4.destroy()

        self.sang.destroy()
        self.lab5.destroy()
        self.row5.destroy()

        self.segu.destroy()
        self.lab6.destroy()
        self.row6.destroy()

        self.nume.destroy()
        self.lab7.destroy()
        self.row7.destroy()

        self.dire.destroy()
        self.lab8.destroy()
        self.row8.destroy()

        self.aler.destroy()
        self.lab9.destroy()
        self.row9.destroy()

        self.cond.destroy()
        self.lab10.destroy()
        self.row10.destroy()

        self.cont1.destroy()
        self.lab11.destroy()
        self.row11.destroy()

        self.cont2.destroy()
        self.lab12.destroy()
        self.row12.destroy()

        self.cent.destroy()
        self.lab13.destroy()
        self.row13.destroy()

        self.b1.destroy()
        self.b2.destroy()

    def mostrarVentanaBuscar(self,master):
        if self.control == 1:
            self.del_ventanaRegistrar(master)
        if self.control == 3:
            return
        elif self.control == 2:
            return
        self.control = 2
        self.ventanaBuscar = Entry(master)
        self.ventanaBuscar.pack(padx = 5, pady = 5)
        self.b3 = Button(master,text = 'Buscar', command = lambda: self.buscarPaciente(master))
        self.b3.pack()
        

    def buscarPaciente(self, master):
        try:
            f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

            if ( f.verifyPassword() == False ):
                raise ValueError('La clave del lector es incorrecta!')

        except Exception as e:
            self.mostrarMensaje('El lector de huellas no pudo ser inicializado!')
            print('Mensaje de error: ' + str(e))

        try:
            self.mostrarMensaje('Por favor coloque el dedo en el lector de huellas.')

            ## Esperar a que se coloque el dedo
            while ( f.readImage() == False ):
                pass

            ## Convierte la imagen a characteristics y lo guarda en charbuffer 1
            f.convertImage(0x01)

            ## Se busca el template
            result = f.searchTemplate()

            positionNumber = result[0]
            #accuracyScore = result[1]

            if ( positionNumber == -1 ):
                self.mostrarMensaje('No se ha encontrado registrada esta huella.')
            else:
                ## Carga el template al charbuffer 1
                f.loadTemplate(positionNumber, 0x01)
                ## Descarga los characteristics del template cargado en el charbuffer 1
                characterics = str(f.downloadCharacteristics(0x01)).encode('utf-8')
                ## Crea un hash SHA-2 con las characteristics del template
                fingerHash = hashlib.sha256(characterics).hexdigest()
                ## Busca en la base de datos el id del paciente al que pertenece la huella
                try:
                    patientId = urllib2.urlopen("http://sgra911.com/get-patient-id.php?fingerprint=" + fingerHash).read()
                    patientInfo = urllib2.urlopen("http://sgra911.com/get-patient-info.php?patient_id=" + patientId).read().split(",")
                    self.found(master,patientInfo)
                    self.mostrarMensaje("Identificación: " + patientId + "\n"
                    "Nombre: " + patientInfo[0] + "\n"
                    "Apellido: " + patientInfo[1] + "\n"
                    "Sexo: " + patientInfo[2] + "\n"
                    "Fecha de nacimiento: " + patientInfo[3] + "\n"
                    "Tipo de Sangre: " + patientInfo[4] + "\n"
                    "Aseguradora: " + patientInfo[5] + "\n"
                    "NSS: " + patientInfo[6] + "\n"
                    "Dirección: " + patientInfo[7] + "\n"
                    "Alergias: " + patientInfo[8] + "\n"
                    "Condiciones especiales: " + patientInfo[9] + "\n"
                    "Contacto de emergencia #1: " + patientInfo[10] + "\n"
                    "Contacto de emergencia #2: " + patientInfo[11] + "\n"
                    "Hospital de preferencia: " + patientInfo[12])
                    pass

                except Exception as e:
                    self.mostrarMensaje("Ha ocurrido un error en la red. Verifique que esta conectado a internet.")
                    print('Mensaje de error: ' + str(e))

        except Exception as e:
            self.mostrarMensaje('Operacion fallida!')
            print('Mensaje de error: ' + str(e))

    def mostrarMensaje(self, texto):

        r = Tk()
        r.title('Mensaje')
        r.geometry('230x50')
        r.resizable(width=False, height=False)
        mensaje = Label(r, text = texto)
        mensaje.pack()
        ok = Button(r, text = "Aceptar",command = r.quit)
        ok.pack()
        r.mainloop()
    
    def found(self,master,values):
        self.control = 3
        
        self.r0 = Frame (master)
        self.l0 = Label (self.r0, width = 25, text = self.fields[0], anchor = 'w')
        self.e0 = Entry(self.r0, text = values[0], state = DISABLED)
        self.r0.pack(side = TOP, fill = X, padx = 5, pady = 5)
        self.l0.pack(side = LEFT)
        self.e0.pack(side = RIGHT, expand = YES, fill = X)

        self.r1 = Frame (master)
        self.l1 = Label (self.r1, width = 25, text = self.fields[1], anchor = 'w')
        self.e1 = Entry(self.r1, text = values[1], state = DISABLED)
        self.r1.pack(side = TOP, fill = X, padx = 5, pady = 5)
        self.l1.pack(side = LEFT)
        self.e1.pack(side = RIGHT, expand = YES, fill = X)

        self.r2 = Frame (master)
        self.l2 = Label (self.r2, width = 25, text = self.fields[2], anchor = 'w')
        self.e2 = Entry(self.r2, text = values[2], state = DISABLED)
        self.r2.pack(side = TOP, fill = X, padx = 5, pady = 5)
        self.l2.pack(side = LEFT)
        self.e2.pack(side = RIGHT, expand = YES, fill = X)

        self.r3 = Frame (master)
        self.l3 = Label (self.r3, width = 25, text = self.fields[3], anchor = 'w')
        self.e3 = Entry(self.r3, text = values[3], state = DISABLED)
        self.r3.pack(side = TOP, fill = X, padx = 5, pady = 5)
        self.l3.pack(side = LEFT)
        self.e3.pack(side = RIGHT, expand = YES, fill = X)

        self.r4 = Frame (master)
        self.l4 = Label (self.r4, width = 25, text = self.fields[4], anchor = 'w')
        self.e4 = Entry(self.r4, text = values[4], state = DISABLED)
        self.r4.pack(side = TOP, fill = X, padx = 5, pady = 5)
        self.l4.pack(side = LEFT)
        self.e4.pack(side = RIGHT, expand = YES, fill = X)

        self.r5 = Frame (master)
        self.l5 = Label (self.r5, width = 25, text = self.fields[5], anchor = 'w')
        self.e5 = Entry(self.r5, text = values[5], state = DISABLED)
        self.r5.pack(side = TOP, fill = X, padx = 5, pady = 5)
        self.l5.pack(side = LEFT)
        self.e5.pack(side = RIGHT, expand = YES, fill = X)

        self.r6 = Frame (master)
        self.l6 = Label (self.r6, width = 25, text = self.fields[6], anchor = 'w')
        self.e6 = Entry(self.r6, text = values[6], state = DISABLED)
        self.r6.pack(side = TOP, fill = X, padx = 5, pady = 5)
        self.l6.pack(side = LEFT)
        self.e6.pack(side = RIGHT, expand = YES, fill = X)

        self.r7 = Frame (master)
        self.l7 = Label (self.r7, width = 25, text = self.fields[7], anchor = 'w')
        self.e7 = Entry(self.r7, text = values[7], state = DISABLED)
        self.r7.pack(side = TOP, fill = X, padx = 5, pady = 5)
        self.l7.pack(side = LEFT)
        self.e7.pack(side = RIGHT, expand = YES, fill = X)

        self.r8 = Frame (master)
        self.l8 = Label (self.r8, width = 25, text = self.fields[8], anchor = 'w')
        self.e8 = Entry(self.r8, text = values[8], state = DISABLED)
        self.r8.pack(side = TOP, fill = X, padx = 5, pady = 5)
        self.l8.pack(side = LEFT)
        self.e8.pack(side = RIGHT, expand = YES, fill = X)

        self.r9 = Frame (master)
        self.l9 = Label (self.r9, width = 25, text = self.fields[9], anchor = 'w')
        self.e9 = Entry(self.r9, text = values[9], state = DISABLED)
        self.r9.pack(side = TOP, fill = X, padx = 5, pady = 5)
        self.l9.pack(side = LEFT)
        self.e9.pack(side = RIGHT, expand = YES, fill = X)

        self.r10 = Frame (master)
        self.l10 = Label (self.r10, width = 25, text = self.fields[10], anchor = 'w')
        self.e10 = Entry(self.r10, text = values[10], state = DISABLED)
        self.r10.pack(side = TOP, fill = X, padx = 5, pady = 5)
        self.l10.pack(side = LEFT)
        self.e10.pack(side = RIGHT, expand = YES, fill = X)

        self.r11 = Frame (master)
        self.l11 = Label (self.r11, width = 25, text = self.fields[11], anchor = 'w')
        self.e11 = Entry(self.r11, text = values[11], state = DISABLED)
        self.r11.pack(side = TOP, fill = X, padx = 5, pady = 5)
        self.l11.pack(side = LEFT)
        self.e11.pack(side = RIGHT, expand = YES, fill = X)

        self.r12 = Frame (master)
        self.l12 = Label (self.r12, width = 25, text = self.fields[12], anchor = 'w')
        self.e12 = Entry(self.r12, text = values[12], state = DISABLED)
        self.r12.pack(side = TOP, fill = X, padx = 5, pady = 5)
        self.l12.pack(side = LEFT)
        self.e12.pack(side = RIGHT, expand = YES, fill = X)

        self.r13 = Frame (master)
        self.l13 = Label (self.r13, width = 25, text = self.fields[13], anchor = 'w')
        self.e13 = Entry(self.r13, text = values[13], state = DISABLED)
        self.r13.pack(side = TOP, fill = X, padx = 5, pady = 5)
        self.l13.pack(side = LEFT)
        self.e13.pack(side = RIGHT, expand = YES, fill = X)
    
    def del_ventanaBuscar(self, master):
        self.b3.destroy()
        self.ventanaBuscar.destroy()

    def del_found(self, master):
        self.l0.destroy()
        self.e0.destroy()
        self.r0.destroy()

        self.l0.destroy()
        self.e0.destroy()
        self.r0.destroy()

        self.l1.destroy()
        self.e1.destroy()
        self.r1.destroy()

        self.l2.destroy()
        self.e2.destroy()
        self.r2.destroy()

        self.l3.destroy()
        self.e3.destroy()
        self.r3.destroy()

        self.l0.destroy()
        self.e0.destroy()
        self.r0.destroy()

        self.l4.destroy()
        self.e4.destroy()
        self.r4.destroy()

        self.l5.destroy()
        self.e5.destroy()
        self.r5.destroy()

        self.l6.destroy()
        self.e6.destroy()
        self.r6.destroy()

        self.l7.destroy()
        self.e7.destroy()
        self.r7.destroy()
        
        self.l8.destroy()
        self.e8.destroy()
        self.r8.destroy()
        
        self.l9.destroy()
        self.e9.destroy()
        self.r9.destroy()

        self.l10.destroy()
        self.e10.destroy()
        self.r10.destroy()

        self.l11.destroy()
        self.e11.destroy()
        self.r11.destroy()

        self.l12.destroy()
        self.e12.destroy()
        self.r12.destroy()
        
        self.l13.destroy()
        self.e13.destroy()
        self.r13.destroy()



    def __init__(self, master):
        
        #frame = Frame(master)
        #frame.pack()
        self.control = int
        menubar = Menu(master)
        menubar.add_command(label = 'Registrar Paciente', command = lambda: self.mostrarVentanaRegistrar(master))
        menubar.add_command(label = 'Buscar Paciente', command = lambda: self.mostrarVentanaBuscar(master))
        master.config(menu = menubar)

        #self.holaButton = Button(master, text = "Hola", command = self.hola)
        #self.holaButton.pack()
   

#tkinter.messagebox.showinfo('Whindow Title', "Completar todos los campos.")
root = Tk()
root.title("SGRA 911")
root.geometry('{}x{}'.format(420, 490))
root.resizable(width=False, height=False)
p = prueba(root)


root.mainloop()
