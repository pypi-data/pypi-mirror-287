def generate_code(blocks):
    # Generate TensorFlow code from a list of blocks
    code = ""
    for block in blocks:
        code += block.to_code() + "\n"
    return code
