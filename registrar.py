#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import urllib2
import hashlib
from pyfingerprint.pyfingerprint import PyFingerprint


## Registra un dedo nuevo
##

## Trata de inicializar el sensor
try:
    f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

    if ( f.verifyPassword() == False ):
        raise ValueError('La clave del lector de huellas es incorrecta!')

except Exception as e:
    print('El lector de huellas no se ha podido iniciaizar!')
    print('Mensaje de error: ' + str(e))
    raw_input('Presione cualquier tecla para salir...')
    exit(1)

## Trata de registrar una huella nueva
try:
    print('Por favor, coloque el dedo...')

    ## Esperar a que se lea ese dedo
    while ( f.readImage() == False ):
        pass

    print('Remueva el dedo...')
    time.sleep(2)
    
    ## Convertir la imagen leida a characteristics y guardarlo en el charbuffer 1
    f.convertImage(0x01)

    ## Revisa si el dedo ya estaba registrado
    result = f.searchTemplate()
    positionNumber = result[0]

    if ( positionNumber >= 0 ):
        answer = raw_input('Esta huella ya esta registrada. Desea cambiar el paciente asignado? (S/N)')
        if answer != 'S' and answer != 's' and answer != 'si' and answer != 'Si' and answer != 'SI' and answer != 'sI':
            exit(0)
        else:
            f.loadTemplate(positionNumber, 0x01)
            characterics = str(f.downloadCharacteristics(0x01)).encode('utf-8')
            fingerHash = hashlib.sha256(characterics).hexdigest()
            urllib2.urlopen("http://sgra911.com/remove-fingerprint.php?fingerprint=" + fingerHash)
            if ( f.deleteTemplate(positionNumber) == True ):  
                print('Esta huella ha sido desvinculada del paciente anterior.')
            

    print('Vuelva a colocar el mismo dedo de nuevo...')

    ## Esperar a que el dedo se vuelva a leer
    while ( f.readImage() == False ):
        pass

    ## Convertir la imagen leida a characteristics y guardarlo en el charbuffer 2
    f.convertImage(0x02)

    ## Compara los charbuffers
    if ( f.compareCharacteristics() == 0 ):
        raise Exception('Las huellas no coinciden.')
        raw_input('Presione cualquier tecla para salir...')

    ## Se crea un template
    f.createTemplate()

    ## Se guarda el template en una posicion nueva
    positionNumber = f.storeTemplate()
    print('La huella ha sido muestreada exitosamente.')
    print('Por favor, digite la identificacion del paciente al cual sera asociada esta huella.')
    patientId = raw_input('ID: ')
    try:
        patientInfo = urllib2.urlopen("http://sgra911.com/get-patient-info.php?patient_id=" + patientId).read()
        while patientInfo == '-1':
            print('No se ha encontrado ningun paciente registrado con ese ID. Por favor, vuelva a intentarlo.')
            patientId = raw_input('ID: ')
            patientInfo = urllib2.urlopen("http://sgra911.com/get-patient-info.php?patient_id=" + patientId).read()
        ## Carga el template al charbuffer 1
        f.loadTemplate(positionNumber, 0x01)
        ## Descarga los characteristics del template cargado en el charbuffer 1
        characterics = str(f.downloadCharacteristics(0x01)).encode('utf-8')
        ## Crea un hash SHA-2 con las characteristics del template
        fingerHash = hashlib.sha256(characterics).hexdigest()
        result = urllib2.urlopen("http://sgra911.com/update-patient-fingerprint.php?patient_id=" + patientId + "&fingerprint=" + fingerHash).read()
        print('La huella se ha registrado exitosamente!')
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
