# Algoritmo simples para facilitar o uso do transcoder FFmpeg no Linux

## Requisítos __ter o FFmpeg instalado__
* Se ainda não tiver instalado, pode instalar pelo menu opção [1] depois inserir a senha e aguarda a instalação

## Como baixar e utilizar o script

```
git clone https://github.com/Hp2501/media_transcoder.git
cd media_transcoder
chmod +x main.py
./main.py
```

## Primeira vez que escolher uma das opções

#
  ### Se for converter vídeo:
  * Será criada uma pasta __videos_para_conversção__ *(aqui ficarão os vídeos para conversão)*
  * Será criada uma pasta __videos_convertidos__ *(aqui ficarão os vídeos após conversão)*
  ### Se for converter áudio:
  * Será criada uma pasta __audios_para_conversão__ *(aqui ficarão os áudios para conversão)*
  * Será criada uma pasta __audios_convertidos__ *(aqui ficarão os áudios convertidos)*
  ### Se for extrai áudio:
  * Será criada uma pasta __videos_para_extracao__ *(aqui ficarão os vídeos para extração do áudio)*
  * Será criada uma pasta __audios_extraidos__ *(aqui ficarão oa áudios extraídos dos vídeos)*

#
## Poderão ser definidos:
  * O formato do(s) vídeo(s)/áudio(s) de origem 
  * O formato do(s) vídeos(s)/áudio(s) de destino
  * Cortar o(s) áudio(s)/vídeo(s)
  * Sobreescrever arquivo(s) existentes(s)

```
Esses valores será usado na conversão de um e/ou quantos arquivos tiver na pasta de origem.
```
#
