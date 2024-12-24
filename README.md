# Projeto de Redução de Dimensionalidade em Imagens para Redes Neurais

Este projeto realiza a conversão de imagens BMP coloridas para níveis de cinza e binarizadas (preto e branco) sem o uso de bibliotecas externas para manipulação de imagens, utilizando apenas bibliotecas nativas do Python.

Funcionalidades:
1. Leitura de imagens no formato BMP 24 bits.
2. Conversão para escala de cinza baseada na luminância (fórmula ponderada).
3. Conversão para imagens binárias (preto e branco) com um limiar ajustável.
4. Salvamento das imagens processadas no formato BMP.

Estrutura do Código:
- 'read_bmp': Lê uma imagem BMP e extrai os pixels RGB.
- 'to_grayscale: Converte a imagem para níveis de cinza.
- 'to_binary'`: Converte a imagem para preto e branco com base em um limiar definido.
- 'save_bmp': Salva a imagem processada em formato BMP.

Requisitos:
- A imagem de entrada deve estar no formato BMP 24 bits.

Como Executar:
1. Substitua o nome do arquivo de entrada no código pela imagem desejada.
2. Execute o script em um ambiente Python 3.
3. As imagens processadas serão salvas no mesmo diretório do script como 'output_gray.bmp' e 'output_binary.bmp'.

Observações:
- O código utiliza manipulação de bytes para trabalhar diretamente com os dados brutos da imagem.
- Não é necessário instalar bibliotecas externas.
