# Conversor de Áudio by Pev

Este é um conversor de áudio simples desenvolvido em Python com Tkinter e Pydub. Atualmente, ele suporta conversão entre os formatos **MP3, WAV, FLAC, OGG e AAC**.

![image](https://github.com/user-attachments/assets/973cd706-d73c-4516-91b4-9fa386521dd3)

## Funcionalidades
- Interface gráfica intuitiva
- Seleção de arquivo de áudio
- Escolha do formato de saída
- Definição da pasta de destino
- Conversão rápida usando FFmpeg
- Barra de progresso durante a conversão

## Requisitos
Este programa já inclui o **FFmpeg**, então não é necessário baixá-lo separadamente. Porém, caso tenha problemas na conversão, você pode baixar manualmente de [ffmpeg.org](https://ffmpeg.org/) e configurar o caminho corretamente.

## Melhorias Futuras
Esta é uma versão inicial e melhorias serão implementadas, incluindo:
- Suporte para mais formatos de áudio
- Opção de ajustar bitrate e qualidade
- Suporte para arrastar e soltar arquivos
- Suporte com API's onlines

## Como Usar
1. **Baixe o executável (tá na pasta 'dist')** ou **rode o código em Python**.
2. **Selecione o arquivo de áudio**.
3. **Escolha a pasta de destino**.
4. **Escolha o formato desejado**.
5. **Clique em "Converter"** e aguarde.

## Instalação via Código
Se preferir rodar via código fonte, certifique-se de ter Python e instale as dependências com:
```
pip install -r requirements.txt
```
Depois, execute:
```
python conversor2.py
```

