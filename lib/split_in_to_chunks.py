

def split_into_chunks(text, max_size):
    lines = text.splitlines(True)
    chunks, current_chunk = [], []
    current_size = 0

    for line in lines:
        line_length = len(line)
        if current_size + line_length > max_size:
            chunks.append(''.join(current_chunk))
            current_chunk = [line]
            current_size = line_length
        else:
            current_chunk.append(line)
            current_size += line_length

    if current_chunk:
        chunks.append(''.join(current_chunk))

    return chunks