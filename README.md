# Jogo da Cobrinha 🐍

Este é um projeto simples do **Jogo da Cobrinha** implementado em Python usando a biblioteca Pygame. O objetivo do jogo é controlar a cobrinha para comer a comida, crescer o máximo possível, e evitar colidir com as bordas ou com o próprio corpo.

## Como Jogar 🎮

- Use as **setas do teclado** para mover a cobrinha:
  - **←**: Esquerda
  - **→**: Direita
  - **↑**: Cima
  - **↓**: Baixo
- A cada comida que a cobra come, ela cresce e a pontuação aumenta.
- O jogo termina se a cobra colidir com as bordas ou com ela mesma.
- O recorde de pontuação é salvo localmente e será carregado na próxima vez que você jogar.

## Funcionalidades ⚙️

- **Cenário em 8-bits**: O jogo possui um fundo com tema de floresta em estilo 8-bits.
- **Sistema de Pontuação**: Mostra a pontuação atual e o recorde.
- **Registro de Recorde**: O recorde é salvo mesmo após o jogo ser fechado e exibido na próxima vez que o jogo for iniciado.

## 🛠️ Requisitos Mínimos de Hardware

Para rodar o jogo da cobrinha simples em Python com Pygame, os seguintes requisitos são recomendados:

1. **🖥️ Processador**:
   - Intel Core i3 (ou equivalente AMD) com frequência mínima de 1 GHz.

2. **💾 Memória RAM**:
   - 2 GB de RAM.

3. **🎮 Placa Gráfica**:
   - Placa gráfica integrada (como Intel HD Graphics) ou qualquer placa gráfica dedicada com suporte para OpenGL 2.0.

4. **💽 Armazenamento**:
   - 50 MB de espaço livre em disco (para o jogo e bibliotecas).

5. **💻 Sistema Operacional**:
   - Windows 7 ou superior

6. **🐍 Python**:
   - Python 3.6 ou superior instalado.

7. **🛠️ Pygame**:
   - Pygame 2.0 ou superior instalado.

### ⚠️ Considerações Adicionais

- **🖥️ Resolução**: Tela de pelo menos 800x600 pixels.
- **🌐 Conexão com a Internet**: Necessária apenas para baixar as dependências.

### Instalação de Dependências

Para instalar as dependências necessárias, use o seguinte comando:

```bash
pip install pygame
```

## Como Executar 🚀

1. Clone este repositório ou faça o download do código.
2. Certifique-se de que a imagem de fundo `floresta_8bits.png` esteja no mesmo diretório que o arquivo do jogo.
3. Execute o arquivo `snake.py`:

```bash
python snake.py
```

## Empacotando o Jogo para .exe

Caso queira transformar o jogo em um arquivo executável `.exe`, siga os passos:

1. Instale o **PyInstaller**:
   ```bash
   pip install pyinstaller
   ```

2. Gere o executável:
   ```bash
   pyinstaller --onefile --windowed snake.py
   ```

O executável será gerado na pasta `dist/`.

## Instalação do Jogo 💻

Baixe o instalador do jogo através do seguinte link:
[Link para o instalador](https://www.mediafire.com/file/x7eavrae3ihmot0/snake_v1.0.1_installer.exe/file)

## Licença 📄

Este projeto é de código aberto e está licenciado sob a [MIT License](https://github.com/boaventura-bit/COBRINHA/blob/main/LICENSE).

## Contribuições 🤝

Contribuições são bem-vindas! Se você encontrar bugs ou tiver sugestões, sinta-se à vontade para abrir uma issue ou enviar um pull request.

---

Feito com ❤️ e Python!
