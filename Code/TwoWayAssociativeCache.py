from math import log2

word_addresses = [43, 171, 45, 178, 179, 5, 174, 46, 4, 181, 65, 180]
word_address_length = 32
number_of_sets = 4
words_per_block = 2
offset_bits = 2
word_addressing = True

def TwoWaySetAssociativeCache(word_addresses, number_of_sets, words_per_block, word_address_length=32, offset_bits=2, word_addressing=True):
    if not word_addressing:
        addresses_converted = [word_address * 4 for word_address in word_addresses]
    else:
        addresses_converted = [address for address in word_addresses]

    addresses_binary = [format(byte_address, '030b') for byte_address in addresses_converted]
    
    word_bits = int(log2(words_per_block))
    index_bits = int(log2(number_of_sets))
    tag_bits = int(word_address_length - index_bits - word_bits - offset_bits)

    words = [address_binary[-word_bits:] for address_binary in addresses_binary]
    indices = [address_binary[-(word_bits + index_bits):-word_bits] for address_binary in addresses_binary]
    tags = [address_binary[:tag_bits][-4:] for address_binary in addresses_binary]
    line = {None: [None for _ in range(words_per_block)] for _ in range(2)} 

    cache = {format(i, '0' + str(index_bits) + 'b'): [line, line]for i in range(2**index_bits)}
    
    # Determine the maximum width for each column
    index_width = max(len(str(index)) for index in cache.keys())
    tag_width = 4
    word_width = max(len(str(word_address)) for word_address in word_addresses + [3 * "…"])
    hit_count = 0
    for word_address, address_binary, word, index, tag in zip(word_addresses, addresses_binary, words, indices, tags):
        current_set = cache[index]
        
        hit = False
        for line in current_set:
            if tag in list(line.keys()):
                print(f"Word Address {word_address}: (Hit)")
                hit_count += 1
                hit = True
                break
                
        if not hit:
            print(f"Word Address {word_address}: (Miss)")
            binary_Tag = tag
            int_word = int(word, 2)
            new_words = [word_address + (words_per_block - int_word - 1) - i for i in range(words_per_block)]
            if current_set[0] == current_set[1] == None:
                current_set[0] = {binary_Tag: new_words}
            elif current_set[0] != None and current_set[1] == None:
                current_set[1] = {binary_Tag: new_words}
            else:
                current_set[0] = current_set[1]
                current_set[1] = {binary_Tag: new_words}
            cache[index] = current_set

        # Printing cache state
        print(f"| {'Index':<{index_width}} | {'Tag':<{tag_width}} | {'Word 3':<{word_width}} | {'Word 2':<{word_width}} | {'Word 1':<{word_width}} | {'Word 0':<{word_width}} |")
        divider = f"|{'-'*(index_width+5)}|{'-'*(tag_width+2)}|{'-'*(word_width+5)}|{'-'*(word_width+5)}|{'-'*(word_width+5)}|{'-'*(word_width+5)}|"
        print(divider)
        for index, lines in cache.items():
            for line in lines:
                for tag, block in line.items():
                    block_str = " | ".join(f"{word:<{word_width+3}}" if word is not None else "…" * (word_width+3) for word in block)
                    print(f"| {index:<{index_width+3}} | {tag if tag is not None else f'None':<{tag_width}} | {block_str} |")
            print("|"+("-"*(len(divider)-2))+"|")
        input("Press Enter to continue...")

    print(f"Hit Rate: {hit_count / len(word_addresses) * 100}% ({hit_count}/{len(word_addresses)})")

TwoWaySetAssociativeCache(word_addresses, number_of_sets, words_per_block, word_address_length, offset_bits, word_addressing)
