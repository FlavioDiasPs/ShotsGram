# ShotsGram
#### pt-BR
Envios de capturas do seu monitor para um chat do telegram. Essa é a função principal e única (até o momento) deste projeto, onde você pode de qualquer local do mundo se conectar ao programa e solicitar imagens da tela do seu computador ou notebook desde que o mesmo esteja rodando na máquina.

#### en-US
Uploads screenshots from your monitor to a telegram chat. This is the main and unique function (so far) of this project, where you can connect to the program from anywhere in the world and request images of your computer or notebook screen as long as it is running on the machine.

# Pré Requisitos / Pre Requirements
#### pt-BR
O requisito mais importante de todos: instalar Python 3.7.0;<br>
Segundo requisito: antes de utilizar o código, é necessário instalar as bibliotecas não nativas do Python que ele utiliza e você pode fazer isso da seguinte forma pelo Prompt de Comando (executando como administrador):<br>
...
pip install -r requirements.txt
...

#### en-US
The most important requirement of all: install Python 3.7.0;<br>
Second requirement: before using the code, it is necessary to install the non-native Python libraries it uses and you can do this as follows from the Command Prompt (running as administrator):<br>
...
pip install -r requirements.txt
...

# Como Usar / How to Use
#### pt-BR
Para usar é simples, entre no telegram e pesquisa por @BotFather para iniciar a criação do seu bot de telegram;<br>
Clique em /start para começar e em seguida digite /newbot.<br>
Digite um nome para seu bot e após isso tecle enter;<br>
Digite um nome de usuário para seu bot (importante que neste nome tenha "Bot" nele) por exemplo: MeuPrimeiroRobo_bot ou MeuPrimeiroRoboBot;<br>
Agora pegue o link que o BotFather te forneceu como algo parecido de "t.me/NomeDoSeuBot" e também o Token que deve ser algo semelhante com "52930512641:ABRS25VND2LPWSzVw525c-LmNw29Oz_dXU6" e salve-os.<br>
Abra o código "bot.py" e procure por "TOKEN", dentro das aspas coloque o Token que você salvou e logo abaixo dele defina uma senha para você acessar seu bot.<br>
Agora abra o link que você também salvou do seu bot e digite "/start" para começar.<br>
Após logar no seu bot (com /password SUA_SENHA) você deve utilizar o comando "/screenshot" para tirar capturas de tela do seu monitor.

#### en-US
It's simple to use, enter the telegram and search for @BotFather to start creating your telegram bot;<br>
Click /start to get started and then type /newbot.<br>
Type a name for your bot and after that hit enter;<br>
Enter a username for your bot (important that this name has "Bot" in it) for example: MyFirstRobo_bot or MyFirstRoboBot;<br>
Now take the link that BotFather provided you with something like "t.me/NameDoYourBot" and also the Token that should look something like "52930512641:ABRS25VND2LPWSzVw525c-LmNw29Oz_dXU6" and save them.<br>
Open the code "bot.py" and look for "TOKEN", inside the quotes put the Token you saved and right below it define a password for you to access your bot.<br>
Now open the link you also saved from your bot and type "/start" to start.<br>
After logging into your bot (with /password YOUR_PASSWORD) you must use the "/screenshot" command to take screenshots of your monitor.

# Atenção / Attention
#### pt-br
Caso o programa seja encerrado será necessário logar novamente no telegram. Evite usar a opção de "parar bot" pelo telegram para evitar erros.

#### en-US
If the program is terminated, it will be necessary to log back into the telegram. Avoid using "stop bot" option by telegram to avoid errors.