def decode_message(encoded_message):
    def decode_ways(index):
        if index == len(encoded_message):
            return [""]
        if encoded_message[index] == "0":
            return []
        ways = []
        for i in range(1, 3):
            if index + i <= len(encoded_message):
                num = int(encoded_message[index:index + i])
                if 1 <= num <= 26:
                    char = chr(num + 64)
                    for suffix in decode_ways(index + i):
                        ways.append(char + suffix)
        return ways

    return decode_ways(0)

encoded_message = "11106"
decoded_messages = decode_message(encoded_message)
print(decoded_messages)
