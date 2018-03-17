#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import urllib2
from pyfingerprint.pyfingerprint import PyFingerprint

## Se intenta inicializar el lector de huellas
try:
    f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

    if ( f.verifyPassword() == False ):
        raise ValueError('La clave del lector es incorrecta!')

except Exception as e:
    print('El lector de huellas no pudo ser inicializado!')
    print('Mensaje de error: ' + str(e))
    raw_input('Presione cualquier tecla para salir...')
    exit(1)

## Se trata de encontrar la huella en el sistema y calcular el hash
try:
    print('Por favor coloque el dedo...')

    ## Esperar a que se coloque el dedo
    while ( f.readImage() == False ):
        pass

    ## Convierte la imagen a characteristics y lo guarda en charbuffer 1
    f.convertImage(0x01)

    ## Se busca el template
    result = f.searchTemplate()

    positionNumber = result[0]
    accuracyScore = result[1]

    if ( positionNumber == -1 ):
        print('No se ha encontrado registrada esta huella.')
        raw_input('Presione cualquier tecla para salir...')
        exit(0)
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
            print("Identificacion: " + patientId)
            print("Nombre: " + patientInfo[0])
            print("Apellido: " + patientInfo[1])
            print("Sexo: " + patientInfo[2])
            print("Fecha de nacimiento: " + patientInfo[3])
            print("Tipo de Sangre: " + patientInfo[4])
            print("Aseguradora: " + patientInfo[5])
            print("NSS: " + patientInfo[6])
            print("Direccion: " + patientInfo[7])
            print("Alergias: " + patientInfo[8])
            print("Condiciones especiales: " + patientInfo[9])
            print("Contacto de emergencia #1: " + patientInfo[10])
            print("Contacto de emergencia #2: " + patientInfo[11])
            print("Hospital de preferencia: " + patientInfo[12])
            raw_input('Presione cualquier tecla para salir...')
            exit(0)
            pass
        except Exception as e:
            print("Ha ocurrido un error en la red. Verifique que esta conectado a internet")
            print('Mensaje de error: ' + str(e))
            raw_input('Presione cualquier tecla para salir...')
            exit(1)

except Exception as e:
    print('Operacion fallida!')
    print('Mensaje de error: ' + str(e))
    raw_input('Presione cualquier tecla para salir...')
    exit(1)
