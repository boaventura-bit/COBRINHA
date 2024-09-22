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

## Requisitos 🛠️

- Python 3.6 ou superior
- Biblioteca Pygame

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

## Licença 📄

Este projeto é de código aberto e está licenciado sob a [MIT License](LICENSE).

## Contribuições 🤝

Contribuições são bem-vindas! Se você encontrar bugs ou tiver sugestões, sinta-se à vontade para abrir uma issue ou enviar um pull request.

---

Feito com ❤️ e Python!
```

Você pode personalizar o arquivo conforme desejar e incluir mais informações, como imagens, exemplos de gameplay ou até instruções mais detalhadas.
