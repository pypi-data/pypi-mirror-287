def align_text(text, width, align='left'):
    text_len = len(text)
    if align == 'left':
        padding = 0
    elif align == 'right':
        padding = width - text_len
    elif align == 'center':
        padding = (width - text_len) // 2
        if (width - text_len) % 2 != 0 and text_len % 2 == 0:
            padding += 1
    else:
        raise ValueError("Invalid alignment. Use 'left', 'right', or 'center'.")
    return ' ' * padding + text
