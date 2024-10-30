def cipher_text(plain_text):
    clean_text = plain_text.lower().translate(str.maketrans(".-@,%!", " " * 6)).replace(" ", "")
    text_len = len(clean_text)
    square = []
    cipher_chunks = []

    if text_len <= 1:
        return clean_text

    row = round(text_len ** 0.5)
    if text_len > row * row:
        col = row + 1
    else:
        col = row

    for i in range(0, text_len, col):
        row_text = clean_text[i:i + col].ljust(col)
        square.append(row_text)

    for c in range(col):
        chunk = ""
        for r in range(row):
            if c < len(square[r]):
                chunk += square[r][c]
        cipher_chunks.append(chunk.ljust(row))

    return " ".join(cipher_chunks)
