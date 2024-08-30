
def flippingBits(n):
    flipped_binary = ""
    binary_number = bin(n)[2:].zfill(32)
    for bit in binary_number:
        if bit == "0":
            bit = "1"
        elif bit == "1":
            bit = "0"

        flipped_binary += bit
    
    interger_number = int(flipped_binary, 2)

    return interger_number


# return (2**32 - 1) - n

# def flippingBits(n):
#     result = []
#     for item in n:
#         binary_number = bin(item)[2:]  # Convert to binary and remove '0b' prefix
#         flipped_binary = "".join('1' if bit == '0' else '0' for bit in binary_number)
#         interger_number = int(flipped_binary, 2)  # Convert the flipped binary back to an integer
#         result.append(interger_number)
#     return result


items = [3, 2147483647, 1, 0]
for item in items:
    print(flippingBits(item))