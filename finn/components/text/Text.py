import pygame


def draw_text(screen, font, text, color, position, width=None, shadow=False, shadow_color=None):
    if shadow:
        if shadow_color is None:
            shadow_color = (0, 0, 0)
        shadow_position = (position[0]+2, position[1]+2)
        draw_text_raw(screen, font, text, shadow_color, shadow_position, width)
    draw_text_raw(screen, font, text, color, position, width)


# stolen a little bit from http://pygame.org/wiki/TextWrap
def draw_text_raw(screen, font, text, color, position, width=None):
    text = str(text)
    if not width:
        width = font.size(text)[0]
    line_spacing = 0
    y = position[1]
    font_height = font.size('Tg')[1]
    while text:
        i = 1
        while font.size(text[:i])[0] < width and i < len(text):
            i += 1

        if i < len(text):
            i = text.rfind(' ', 0, i) + 1

        image = font.render(text[:i], True, color)

        screen.blit(image, pygame.Rect(position[0], y, 0, 0))
        y += font_height + line_spacing

        # remove text just blitted
        text = text[i:]
