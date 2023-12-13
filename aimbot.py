import os
import pyautogui
from PIL import Image

# Defina as coordenadas da região que você deseja capturar
left, top, width, height = 350, 350, 600, 600

# Captura a região da tela
screenshot = pyautogui.screenshot(region=(left, top, width, height))

# Verifica se a pasta de destino existe, se não, cria
output_folder = "C:\Users\Thiago\Desktop\projeto1"
os.makedirs(output_folder, exist_ok=True)

# Caminho completo para o arquivo de saída
output_file_path = os.path.join(output_folder, "screenshot.png")

# Salva a captura de tela como um arquivo na pasta específica
screenshot.save(output_file_path)

# Converte a captura de tela para um formato de imagem manipulável pelo Pillow
image = Image.open(output_file_path)

# Define a cor que você está procurando (exemplo: vermelho)
target_color = (255, 0, 0)

# Itera sobre os pixels na imagem procurando pela cor alvo
for x in range(width):
    for y in range(height):
        pixel_color = image.getpixel((x, y))

        # Verifica se o pixel é da cor alvo
        if pixel_color == target_color:
            print(f"Encontrou a cor alvo em ({left + x}, {top + y})")

# Você também pode executar ações com base nos resultados, por exemplo, mover o mouse para a posição encontrada
# pyautogui.moveTo(left + x, top + y)
