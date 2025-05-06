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
hay 2 versiones: 16.16.0 LTS y 18.7.0 Actual (esta será la de trabajo de este demo)

### instalar version nodejs 18.x, ver página: https://techviewleo.com/how-to-install-node-js-18-lts-on-ubuntu/

    sudo apt update

    curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -

    sudo apt install nodejs

### probar versiones:

    node -v
    
    npm -v

# instalar mongodb en ubuntu 22.04

## ref: https://www.mongodb.com/docs/v6.0/tutorial/install-mongodb-on-ubuntu/

    sudo apt-get install gnupg

    curl -fsSL https://pgp.mongodb.com/server-6.0.asc | \
    sudo gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg \
    --dearmor

    echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list

    sudo apt-get update

    sudo apt-get install -y mongodb-org

    sudo systemctl enable mongod

    sudo systemctl daemon-reload

    sudo systemctl start mongod

    mongosh