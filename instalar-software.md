# Curso de "sistemas de gestión de datos" / bases de datos - si2003/st0246 semestre 2025-1
# profesor: Edwin Montoya - emontoya@eafit.edu.co
#
# Instalación de software en una máquina con Ubuntu 22.04:

## 1. clonar el repositorio de la materia:

    git clone https://github.com/st0246eafit/st0246-251.git
  
## 2. Instalar MySQL versión 8.0.30 o sup:

ref: https://linuxhint.com/install-mysql-on-ubuntu-22-04/

    sudo apt update -y
    sudo apt install mysql-server -y
    sudo systemctl enable mysql
    sudo systemctl start mysql

    sudo mysql

    ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Eafit2023.';
    FLUSH PRIVILEGES;
    QUIT;

    mysql -u root -p
    Password: Eafit2023.
    > Sentencias SQL
    > quit

### conexión de mysql workbench al servidor en aws via un Tunnel SSH

adicione esta instrucción al comando ssh: -L puertoLocal:ip:puertoAWSMysql

$ ssh -i "vockey.pem" -L 3307:127.0.0.1:3306 ubuntu@ec2-54-89-21-204.compute-1.amazonaws.com

consideraciones: 
1. normalmente el puerto 3306 es para el servidor local, por ello, vamos a utilizar el puerto 3307 para crear el Tunel hacia amazon.

2. cambie la dirección IP pública a su propio servidor, cambie:ec2-54-89-21-204.compute-1.amazonaws.com

## 3. instalar nodejs

ver pagina: https://nodejs.org/
Versión 22.15.0

### instalar version nodejs 22.x

    sudo apt update

# Download and install fnm:
curl -o- https://fnm.vercel.app/install | bash

# Download and install Node.js:
fnm install 22

# Verify the Node.js version:
node -v # Should print "v22.15.0".

# Verify npm version:
npm -v # Should print "10.9.2".


### probar versiones:

    node -v
    
    npm -v

# instalar mongodb en ubuntu 22.04

## ir a la página: https://www.mongodb.com/try/download/community
## opcion de descarga en diferentes sistemas operativos

## probar mongodb:

    mongosh