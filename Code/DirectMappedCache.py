# Given word addresses
from math import log2

word_addresses = [43, 171, 45, 178, 179, 5, 174, 46, 4, 181, 65, 180]
word_address_length = 32
number_of_blocks = 4
words_per_block = 1
offset_bits = 2
word_addressing = True

def DirectMappedCache(word_addresses, number_of_blocks, words_per_block, word_address_length=32, offset_bits=2, word_addressing=True):
    from math import log2

    if not word_addressing:
        addresses_converted = [word_address * 4 for word_address in word_addresses]
    else:
        addresses_converted = word_addresses
    addresses_binary = [format(byte_address, '030b') for byte_address in addresses_converted]

    num_word_bits = int(log2(words_per_block))
    num_index_bits = int(log2(number_of_blocks))
    num_tag_bits = int(word_address_length - num_index_bits - num_word_bits - offset_bits)

    cache = {format(i, '0' + str(num_index_bits) + 'b'): {None: [None for _ in range(words_per_block)]} for i in range(2**num_index_bits)}
    index_width = max(len(str(index)) for index in cache.keys())
    tag_width = 4
    word_width = max(len(str(word_address)) for word_address in word_addresses + [3 * "…"])
    hit_count = 0
    for address_binary in addresses_binary:
        address_word = int(address_binary, 2)
        binary_word = address_binary[-num_word_bits:]
        binary_index = format(int(address_binary[-(num_word_bits + num_index_bits):-num_word_bits], 2) if num_word_bits != 0 else int(address_binary[-(num_word_bits + num_index_bits):-1], 2), '0' + str(num_index_bits) + 'b')
        binary_tag = address_binary[:num_tag_bits][-4:]
        int_word = int(binary_word, 2)
        int_index = int(binary_index, 2) if binary_index != "" else "0"
        int_tag = int(binary_tag, 2)
        new_index = {binary_tag:[None for i in range(words_per_block)]}
        new_index[binary_tag]=[address_word-i for i in range(words_per_block)]  # Changed the formula here
        current_index = cache[binary_index]
        if current_index == new_index:
            print(f"Word Address {address_word}: (Hit)")
            hit_count += 1
        else:
            print(f"Word Address {address_word}: (Miss)")
            current_index = new_index
        cache[binary_index] = current_index

    header_str = f"| {'Index':<{index_width}} | {'Tag':<{tag_width}} |"
    for i in reversed(range(words_per_block)):
        header_str += f" {'Word ' + str(i):<{word_width}} |"
    print(header_str)
    print("|" + '-'*(len(header_str)-1) + "|")
    for index, tag in cache.items():
        tag = list(tag.keys())[0]
        block = cache[index][tag]
        block_str = " | ".join(f"{word:<{word_width+3}}" if word is not None else "…" * (word_width+3) for word in block)
        print(f"| {index:<{index_width+2}} | {tag if tag is not None else f'None':<{tag_width}} | {block_str} |")
        
    print(f"Hit Rate: {hit_count / len(word_addresses) * 100:.2f}%")

# Run the function
DirectMappedCache(word_addresses, number_of_blocks, words_per_block, word_address_length, offset_bits, word_addressing)
"""


    words = [address_binary[-num_word_bits:] for address_binary in addresses_binary]
    indices = [address_binary[-(num_word_bits + num_index_bits):-num_word_bits] for address_binary in addresses_binary]
    tags = [address_binary[:num_tag_bits][-4:] for address_binary in addresses_binary]

    

    # Determine the maximum width for each column
    index_width = max(len(str(index)) for index in cache.keys())
    tag_width = 4
    word_width = max(len(str(word_address)) for word_address in word_addresses + [3 * "…"])
    hit_count = 0
    for word_address, address_binary, word, index, tag in zip(word_addresses, addresses_binary, words, indices, tags):
        current_index = cache[index]
    
        if tag in current_index.keys():
            print(f"Word Address {word_address}: (Hit)")
            hit_count += 1
        else:
            print(f"Word Address {word_address}: (Miss)")
            binary_Tag = tag
            new_index = {binary_Tag:[None for i in range(4)]}
            int_word = int(word, 2)
            new_index[binary_Tag]=[word_address+(words_per_block-int(word, 2)-1)-i for i in range(words_per_block)]
            cache[index] = new_index

    # Printing cache state
        print(f"| {'Index':<{index_width}} | {'Tag':<{tag_width}} | {'Word 3':<{word_width}} | {'Word 2':<{word_width}} | {'Word 1':<{word_width}} | {'Word 0':<{word_width}} |")
        print(f"|{'-'*(index_width+4)}|{'-'*(tag_width+2)}|{'-'*(word_width+5)}|{'-'*(word_width+5)}|{'-'*(word_width+5)}|{'-'*(word_width+5)}|")
        for index, tag in cache.items():
            tag = list(tag.keys())[0]
            block = cache[index][tag]
            block_str = " | ".join(f"{word:<{word_width+3}}" if word is not None else "…" * (word_width+3) for word in block)
            print(f"| {index:<{index_width+2}} | {tag if tag is not None else f'None':<{tag_width}} | {block_str} |")
        #input("Press Enter to continue...")

    print(f"Hit Rate: {hit_count / len(word_addresses) * 100}% ({hit_count}/{len(word_addresses)})")
"""