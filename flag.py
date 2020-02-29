# Nome: Adrian Cerbaro
# País Selecionado: Burundi

import arcade
import math


def draw(pos_x, pos_y, w):

    # Como os valores da posição podem não ser números inteiros e,
    # a tela é composta por pixels, padroniza a posição da bandeira para não
    # haver problemas na hora de calcular as posições dos elementos
    pos_x, pos_y = math.floor(pos_x), math.floor(pos_y)

    # Todos os valores relacionados ao tamanho da bandeira também são padronizados
    # para o maior valor inteiro menor ou igual ao valor dado
    proportion = 3 / 5                       # Proporção da bandeira
    width = math.floor(w)                    # Largura da bandeira
    height = math.floor(width * proportion)  # Altura da bandeira

    # Como a posição x e y passadas para a função correspondem ao
    # canto superior esquerdo, diminui a posição y pelo tamanho da bandeira
    # para encontrar a posição do ponto inferior esquerdo, padrão do arcade
    pos_y = pos_y - height

    # Calcula a posição x de um elemento relativo a posição informada nos parâmetros da função
    def x(pos=0):
        return pos_x + pos

    # Calcula a posição y de um elemento relativo a posição informada nos parâmetros da função
    def y(pos=0):
        return pos_y + pos

    # Retorna o valor proporcional a largura da bandeira
    def sw(var):
        return math.floor((var / 100) * width)

    # Retorna o valor proporcional a altura da bandeira
    def sh(var):
        return math.floor((var / 100) * height)

    # Variáveis úteis
    x_center = x(round(width / 2))   # Posição x referente ao centro da bandeira
    y_center = y(round(height / 2))  # Posição y referente ao centro da bandeira
    right = x(width)                 # Posição x referente ao lado direito da bandeira
    left = x()                       # Posição x referente ao lado esquerdo da bandeira
    top = y(height)                  # Posição y referente ao topo da bandeira
    bottom = y()                     # Posição y referente a parte inferior da bandeira

    # Cores da bandeira em hexadecimal
    # Tuple contendo os valores RGB
    red_color = (0xE0, 0x00, 0x1E)
    green_color = (0x00, 0xCA, 0x3C)
    white_color = (255, 255, 255)

    # Base retangular da bandeira
    arcade.draw_xywh_rectangle_filled(left, bottom, width, height, white_color)

    # Espessura das linhas que formam um X branco no centro da bandeira
    line_stroke = 15

    # Triângulos do fundo
    # Desenha um triângulo em cada extremidade da bandeira, sendo que,
    # cada triângulo tem seu tamanho reduzido, metade da espessura da linha em cada ponta,
    # para dar a impressão de que há duas linhas brancas se cruzando em forma de X
    # no centro da bandeira

    # Triângulo inferior
    arcade.draw_triangle_filled(x(sw(line_stroke / 2)), bottom, x_center, y_center - sh(line_stroke / 2),
                                right - sw(line_stroke / 2), bottom, red_color)

    # Triângulo superior
    arcade.draw_triangle_filled(x(sw(line_stroke / 2)), top, x_center, y_center + sh(line_stroke / 2),
                                right - sw(line_stroke / 2), top, red_color)

    # Triângulo lateral esquerdo
    arcade.draw_triangle_filled(left, y(sh(line_stroke/2)), x_center - sw(line_stroke/2), y_center,
                                left, top - sh(line_stroke/2), green_color)

    # Triângulo lateral direito
    arcade.draw_triangle_filled(right, y(sh(line_stroke / 2)), x_center + sw(line_stroke / 2), y_center,
                                right, top - sh(line_stroke / 2), green_color)

    # Circulo branco central da bandeira
    circle_radius = sw(17.12)  # Tamanho do círculo central proporcional à bandeira
    arcade.draw_circle_filled(x_center, y_center, circle_radius, white_color)

    # Desenha as 3 estrelas de davi no centro da bandeira
    stars_dist = sw(15.28)  # Distância entre as estrelas de Davi em pixels proporcional à bandeira
    star_size = sw(5.6)  # Tamanho da estrela em pixels proporcional à bandeira
    star_border = sw(1.3)  # Tamanho da borda verde da estrela em pixels proporcional à bandeira

    # Desenha uma estrela de Davi em cada vértice de um triângulo equilatero
    # com o tamanho de seu lado sendo a distância entre cada estrela
    for vert in get_eq_triangle_vertices(x_center, y_center, stars_dist):
        x, y = vert  # Coordenadas do vértice

        # Gera uma estrela maior de cor verde e uma menor de cor vermelha no centro do vértice
        # para dar a impressão de que a estrela possui uma borda
        render_star_of_david(x, y, star_size + star_border, green_color)
        render_star_of_david(x, y, star_size, red_color)


# Retorna as coordenadas dos vértices de um triângulo equilátero a partir da
# coordenada do centro de simetria (center_x, center_y)
# O parâmetro "size" refere-se ao tamanho dos lados do triângulo em pixels
# O parâmetro "direction" refere-se a direção do triângulo (virado para cima (0) ou para baixo (1))
def get_eq_triangle_vertices(center_x, center_y, size, direction=0):
    # Distância do centro de simetria do triângulo até seu topo (2/3 da altura)
    center_top = (math.sqrt(3) / 3) * size

    # Converte a distância do centro até o topo para número negativo caso
    # a direção do triângulo deva ser para baixo
    if direction == 1:
        center_top *= -1

    x1, y1 = center_x, center_y + center_top  # Coordenadas do vértice superior ou inferior
    x2, y2 = center_x - size / 2, center_y - center_top / 2  # Coordenadas do vértice esquerdo
    x3, y3 = center_x + size / 2, y2  # Coordenadas do vértice direito
    return [x1, y1], [x2, y2], [x3, y3]


# Renderiza um triângulo equilátero preenchido a partir do centro de simetria
def render_equilateral_triangle(center_x, center_y, size, color, direction=0):
    (x1, y1), (x2, y2), (x3, y3) = get_eq_triangle_vertices(center_x, center_y, size, direction)
    arcade.draw_triangle_filled(x1, y1, x2, y2, x3, y3, color)


# Renderiza dois triângulos equiláteros apontados para direções opostas, para
# formar uma estrela de Davi
def render_star_of_david(center_x, center_y, size, color):
    render_equilateral_triangle(center_x, center_y, size, color)
    render_equilateral_triangle(center_x, center_y, size, color, direction=1)
