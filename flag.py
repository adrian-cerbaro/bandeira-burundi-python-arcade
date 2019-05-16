import arcade
import math


def draw(pos_x, pos_y, w):
    # Propriedades da bandeira
    proportion = 3 / 5  # Proporção da bandeira
    width = w  # Largura da bandeira
    height = w * proportion  # Comprimento da bandeira

    # Correção de altura
    ######################################
    pos_y = pos_y - height
    ######################################

    # Calcula a posição x relativo a bandeira
    def x(pos):
        return pos_x + pos

    # Calcula a posição y relativo a bandeira
    def y(pos):
        return pos_y + pos

    # Retorna o valor proporcional a largura da bandeira
    def sw(var):
        return (var / 100) * width

    # Retorna o valor proporcional a altura da bandeira
    def sh(var):
        return (var / 100) * height

    # Utils
    #########################################
    x_center = x(width / 2)
    y_center = y(height / 2)
    right = x(width)
    left = x(0)
    top = y(height)
    bottom = y(0)
    ###########################################

    # Cores da bandeira
    red_color = (0xE0, 0x00, 0x1E)
    green_color = (0x00, 0xCA, 0x3C)
    white_color = (255, 255, 255)

    # Cria base da bandeira
    arcade.draw_rectangle_filled(x_center, y_center, width, height, white_color)

    # Line stroke
    line_stroke = 15.3
    correction = 0.75

    # Triangulos do fundo
    #############################################

    # Verticais
    arcade.draw_triangle_filled(x(sw(line_stroke / 2)), y(-correction), x_center, y_center - sh(line_stroke / 2),
                                right - sw(line_stroke / 2), y(-correction), red_color)

    arcade.draw_triangle_filled(x(sw(line_stroke / 2)), y(height + correction), x_center, y_center + sh(line_stroke / 2),
                                right - sw(line_stroke / 2), y(height + correction), red_color)

    # Laterais
    arcade.draw_triangle_filled(left, y(sh(line_stroke/2)), x_center - sw(line_stroke/2), y_center,
                                left, top - sh(line_stroke/2), green_color)

    arcade.draw_triangle_filled(right, y(sh(line_stroke / 2)), x_center + sw(line_stroke / 2), y_center,
                                right, top - sh(line_stroke / 2), green_color)

    # Circulo central
    ############################################
    circle_radius = sw(17.12)
    arcade.draw_circle_filled(x_center, y_center, circle_radius, white_color)

    # Estrelas
    ############################################
    stars_radius = circle_radius/1.12
    star_size = sw(5.5)
    star_border = sw(1.3)
    for vert in get_eq_triangle_vertices(x_center, y_center, stars_radius):
        x, y = vert
        render_star_of_david(x, y, star_size + star_border, green_color)
        render_star_of_david(x, y, star_size, red_color)


def get_eq_triangle_vertices(center_x, center_y, size, direction=0):
    center_top = (math.sqrt(3) / 3) * size

    if direction == 1:
        center_top *= -1

    x1, y1 = center_x, center_y + center_top
    x2, y2 = center_x - size / 2, center_y - center_top / 2
    x3, y3 = center_x + size / 2, y2
    return [x1, y1], [x2, y2], [x3, y3]


def render_equilateral_triangle(center_x, center_y, size, color, direction=0):
    (x1, y1), (x2, y2), (x3, y3) = get_eq_triangle_vertices(center_x, center_y, size, direction)
    arcade.draw_triangle_filled(x1, y1, x2, y2, x3, y3, color)


def render_star_of_david(center_x, center_y, size, color):
    render_equilateral_triangle(center_x, center_y, size, color)
    render_equilateral_triangle(center_x, center_y, size, color, direction=1)

