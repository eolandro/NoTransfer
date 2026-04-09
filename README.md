# NoTransfer
No Transfer File. Este repositorio es solo una prueba de concepto, no se tome con seriedad.

## Descripción
NoTransfer es un programa para compartir archivos sin compartirlos. Al menos la idea es no compartir directamente el archivo, si no que se adivine el archivo que se desea compartir.

Imaginemos que **Alicia** quiere enviar una Foto.jpg a **Beatriz**, en lugar de mandar directamente el archivo, alicia genera un nuevo archivo llamemosle Foto.jpg.nt, este archivo se crea con las siguientes condiciones:

1. Se lee 1 byte de **Foto.jpg.nt**.
2. Se obtiene la suma de verificación MD5 pura de ese byte.
3. Se guarda la suma de verificación MD5 pura en **Foto.jpg.nt**.
4. Se repite desde el punto 1 hasta que no hay más bytes en **Foto.jpg**.

El archivo que realmente se transfire es **Foto.jpg.nt**.

Ahora **Beatriz** para obtener el archivo original debe realizar lo siguiente:

1. Se crean un objeto para generar sumas de verificacion md5 **M** con cadena vacia.
2. Se leen 16 bytes de **Foto.jpg.nt** que corresponde a una suma de verificación md5 **HS**.
3. Se crean 256 copias del objeto **M**.
4. Se actualizan cada una de las copias **M** con un entero de 8 bits de 0 a 255 sin repetir. Asi hay una copia actualizada con 0x00, otra con 0x01, otra 0x02 y asi sucesivamente.
5. Se compara la suma de verificación de cada copia de **M** contra **HS**
6. Si son iguales se guarda la copia de **M** y el entero de 8 bits con el que fue actualizado.
7. La copia de **M** Tomara el lugar de **M**
8. El entero de 8 bits se almacena en una **Pila** (Stack)
9. Se repite desde el paso 2. hasta que no haya más bytes en **Foto.jpg.nt**
10. Se guarda la **Pila** en un archivo **Foto.jpg** este será el archivo original

## Uso

Para generar el archivo nt
```
notransfer.py <archivo_a_no_transferir> <archivo_nt>
```

Para adivinar el archivo original
```
unnotransfer.py <archivo_nt> <archivo_adivinado>
```

## Notas y Limitaciones

* Este es probablemente uno de los software más ineficientes que he escrito. Lo hice en una tarde noche de semana santa, no espere calidad
* Al estar escrito en python por naturaleza es lento, aunque se use la implementacion de md5 de openssl.
* Es CPU intensivo y tambien no aprovecha los nucleos de la CPU, probablemente seria mucho más rapido si se usara la GPU.
* Los archivos **nt** deberian ser al menos 16 veces mas grandes que el original, por lo que es un desastre de almacenamiento
* No es muy util para archivos de mas 10 Mib, a menos que tengas una muy buena CPU, en mi laptop *AMD A6-4400M APU with Radeon(tm) HD Graphics* se tarda horas  para adivinar un archivo de 7 Mib.
* Hay un notebook de google colab, pero aparentemente no hay una diferencia significativa con un *Intel Xeon* que da google gratuito, igual ahi esta.
* No deberias usarlo para piratear...

## Ejemplos de Rendimiento 
Todo esto fue hecho en una laptop  con *AMD A6-4400M APU with Radeon(tm) HD Graphics*
y con juegos gratuitos de itch.io

Creando archivo **nt** de *Halo Combat Devolved v2.31.gbc* este pesa 2097152 bytes

```
$time python notransfer.py Halo\ Combat\ Devolved\ v2.31.gbc Halo\ Combat\ Devolved\ v2.31.gbc.nt

real	0m3.425s
user	0m3.298s
sys	0m0.090s

```
Adivinando el archivo original apartir del archivo **nt**

```
time python unnotransfer.py Halo\ Combat\ Devolved\ v2.31.gbc.nt halo.gbc
 
real	5m36.477s
user	5m21.789s
sys	0m1.740s
```

## Y esto.. ¿Por que?...

1. Diversión.
2. Esta inspirado ligeramente un malware llamado GlassWorm.
3. Esta inspirado ligeramente en la teoría de información de Claude Shannon.
4. La principal inspiración es una empresa que da el *servicio* de *liberar* el software de codigo abiero para su uso en empresas privadas, escencialmente ponen una IA a recrear las APIs, funciones, métodos y objetos de los proyectos de codigo abierto, pero sin la licencia abierta. Y lo toman como válido porque estos ultimos son publicos y a partir de ahi hacen ingenieria inversa.  Es una porqueria si me preguntan, pero si a esas vamos. Creo que podemos estirar la liga, una suma de verificación a menudo es de pública y por definicion no deberia ser reversible. Asi que y si en lugar de mandar un archivo, mando todas las sumas de verificación de cada byte del archivo y luego pongo a un programa a por fuerza bruta a adivinar de que byte vienen. ¿Se considera transferir el archivo?

## PD
* No se uso ningun LLM para la codificación de este programa
* Tampoco VScode...

