import struct

# Função para ler uma imagem BMP (formato específico para simplicidade)
def read_bmp(filename):
    with open(filename, 'rb') as f:
        # Ler cabeçalho BMP (54 bytes)
        bmp_header = f.read(54)
        data_offset = struct.unpack('<I', bmp_header[10:14])[0]
        width = struct.unpack('<I', bmp_header[18:22])[0]
        height = struct.unpack('<I', bmp_header[22:26])[0]
        bits_per_pixel = struct.unpack('<H', bmp_header[28:30])[0]

        # Validar formato
        if bits_per_pixel != 24:
            raise ValueError('Apenas imagens 24 bits são suportadas.')

        # Ler dados de pixel
        f.seek(data_offset)
        row_padded = (width * 3 + 3) & ~3
        data = []
        for y in range(height):
            row = []
            for x in range(width):
                b, g, r = struct.unpack('BBB', f.read(3))
                row.append((r, g, b))
            f.seek(row_padded - width * 3, 1)
            data.insert(0, row)
        return width, height, data

# Função para converter para tons de cinza
def to_grayscale(image):
    width, height, data = image
    grayscale = []
    for row in data:
        gray_row = [(int(0.3 * r + 0.59 * g + 0.11 * b),) * 3 for r, g, b in row]
        grayscale.append(gray_row)
    return width, height, grayscale

# Função para converter para imagem binária (preto e branco)
def to_binary(image, threshold=128):
    width, height, data = image
    binary = []
    for row in data:
        binary_row = [(255, 255, 255) if (0.3 * r + 0.59 * g + 0.11 * b) > threshold else (0, 0, 0) for r, g, b in row]
        binary.append(binary_row)
    return width, height, binary

# Função para salvar imagem BMP
def save_bmp(filename, image):
    width, height, data = image
    row_padded = (width * 3 + 3) & ~3
    with open(filename, 'wb') as f:
        # Cabeçalho BMP
        f.write(b'BM')
        f.write(struct.pack('<I', 54 + row_padded * height))
        f.write(b'\x00\x00')
        f.write(b'\x00\x00')
        f.write(struct.pack('<I', 54))
        f.write(struct.pack('<I', 40))
        f.write(struct.pack('<I', width))
        f.write(struct.pack('<I', height))
        f.write(struct.pack('<H', 1))
        f.write(struct.pack('<H', 24))
        f.write(b'\x00\x00\x00\x00')
        f.write(struct.pack('<I', row_padded * height))
        f.write(b'\x00\x00\x00\x00')
        f.write(b'\x00\x00\x00\x00')
        f.write(b'\x00\x00\x00\x00')
        f.write(b'\x00\x00\x00\x00')

        # Dados de pixel
        for row in reversed(data):
            for r, g, b in row:
                f.write(struct.pack('BBB', b, g, r))
            f.write(b'\x00' * (row_padded - width * 3))

# Leitura e execução do algoritmo
input_file = 'input.bmp'
output_gray = 'output_gray.bmp'
output_binary = 'output_binary.bmp'

# Carregar imagem
image = read_bmp(input_file)

# Converter para cinza e salvar
gray_image = to_grayscale(image)
save_bmp(output_gray, gray_image)

# Converter para binário e salvar
binary_image = to_binary(image)
save_bmp(output_binary, binary_image)

print("Imagens processadas salvas com sucesso!")
