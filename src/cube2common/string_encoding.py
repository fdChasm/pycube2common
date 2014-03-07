def encodeutf8(cube_string):
    src = bytearray(cube_string)
    dst = bytearray()

    for c in src:
        dst.extend(cube2uni(c))

    return dst

def decodeutf8(utf8_string):
    src = bytearray(utf8_string)
    dst = bytearray()

    srclen = len(src)
    i = 0
    while i < srclen:
        c = src[i]
        i += 1
        if c < 0x80:
            dst.append(c)
        elif c >= 0xC0:
            if c >= 0xE0:
                if c >= 0xF0:
                    if c >= 0xF8:
                        if c >= 0xFC:
                            if c >= 0xFE:
                                continue
                            uni = c & 1
                            if srclen - i < 5: break
                            c = src[i]
                            if (c & 0xC0) != 0x80: continue
                            i += 1
                            uni = (uni << 6) | (c & 0x3F)
                        else:
                            uni = c & 3
                            if srclen - i < 4: break
                        c = src[i]
                        if (c & 0xC0) != 0x80: continue
                        i += 1
                        uni = (uni << 6) | (c & 0x3F)
                    else:
                        uni = c & 7
                        if srclen - i < 3: break
                    c = src[i]
                    if (c & 0xC0) != 0x80: continue
                    i += 1
                    uni = (uni << 6) | (c & 0x3F)
                else:
                    uni = c & 0xF
                    if srclen - i < 2: break
                c = src[i]
                if (c & 0xC0) != 0x80: continue
                i += 1
                uni = (uni << 6) | (c & 0x3F)
            else:
                uni = c & 0x1F
                if srclen - i < 1: break
            c = src[i]
            if (c & 0xC0) != 0x80: continue
            i += 1
            uni = (uni << 6) | (c & 0x3F)

            c = uni2cube(uni)

            if not c: continue

            dst.append(c)

    return dst

def cube2uni(c):
    if c >= 0 and c <= 255:
        return cube2unichars[c]
    return 0

def uni2cube(c):
    return uni2cubechars[uni2cubeoffsets[c >> 8] + (c & 0xFF)] if c <= 0x7FF else 0

uni2cubeoffsets = [
    0, 256, 658, 658, 512, 658, 658, 658
]

uni2cubechars = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 10, 11, 12, 13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63,
    64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95,
    96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    1, 2, 3, 4, 5, 6, 7, 8, 14, 15, 16, 17, 18, 19, 20, 21, 0, 22, 23, 24, 25, 26, 27, 0, 28, 29, 30, 31, 127, 128, 0, 129,
    130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 0, 146, 147, 148, 149, 150, 151, 0, 152, 153, 154, 155, 156, 157, 0, 158,
    0, 0, 0, 0, 159, 160, 161, 162, 0, 0, 0, 0, 163, 164, 165, 166, 0, 0, 0, 0, 0, 0, 0, 0, 167, 168, 169, 170, 0, 0, 171, 172,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 173, 174, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 175, 176, 177, 178, 0, 0, 179, 180, 0, 0, 0, 0, 0, 0, 0, 181, 182, 183, 184, 0, 0, 0, 0, 185, 186, 187, 188, 0, 0, 189, 190,
    191, 192, 0, 0, 193, 194, 0, 0, 0, 0, 0, 0, 0, 0, 195, 196, 197, 198, 0, 0, 0, 0, 0, 0, 199, 200, 201, 202, 203, 204, 205, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 17, 0, 0, 206, 83, 73, 21, 74, 0, 0, 0, 0, 0, 0, 0, 65, 207, 66, 208, 209, 69, 210, 211, 212, 213, 75, 214, 77, 72, 79, 215,
    80, 67, 84, 216, 217, 88, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 97, 228, 229, 230, 231, 101, 232, 233, 234, 235, 236, 237, 238, 239, 111, 240,
    112, 99, 241, 121, 242, 120, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 0, 141, 0, 0, 253, 115, 105, 145, 106, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 254, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
]

cube2unichars = [
    '\x00',
    '\xc3\x80',
    '\xc3\x81',
    '\xc3\x82',
    '\xc3\x83',
    '\xc3\x84',
    '\xc3\x85',
    '\xc3\x86',
    '\xc3\x87',
    '\t',
    '\n',
    '\x0b',
    '\x0c',
    '\r',
    '\xc3\x88',
    '\xc3\x89',
    '\xc3\x8a',
    '\xc3\x8b',
    '\xc3\x8c',
    '\xc3\x8d',
    '\xc3\x8e',
    '\xc3\x8f',
    '\xc3\x91',
    '\xc3\x92',
    '\xc3\x93',
    '\xc3\x94',
    '\xc3\x95',
    '\xc3\x96',
    '\xc3\x98',
    '\xc3\x99',
    '\xc3\x9a',
    '\xc3\x9b',
    ' ',
    '!',
    '"',
    '#',
    '$',
    '%',
    '&',
    "'",
    '(',
    ')',
    '*',
    '+',
    ',',
    '-',
    '.',
    '/',
    '0',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    ':',
    ';',
    '<',
    '=',
    '>',
    '?',
    '@',
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H',
    'I',
    'J',
    'K',
    'L',
    'M',
    'N',
    'O',
    'P',
    'Q',
    'R',
    'S',
    'T',
    'U',
    'V',
    'W',
    'X',
    'Y',
    'Z',
    '[',
    '\\',
    ']',
    '^',
    '_',
    '`',
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z',
    '{',
    '|',
    '}',
    '~',
    '\xc3\x9c',
    '\xc3\x9d',
    '\xc3\x9f',
    '\xc3\xa0',
    '\xc3\xa1',
    '\xc3\xa2',
    '\xc3\xa3',
    '\xc3\xa4',
    '\xc3\xa5',
    '\xc3\xa6',
    '\xc3\xa7',
    '\xc3\xa8',
    '\xc3\xa9',
    '\xc3\xaa',
    '\xc3\xab',
    '\xc3\xac',
    '\xc3\xad',
    '\xc3\xae',
    '\xc3\xaf',
    '\xc3\xb1',
    '\xc3\xb2',
    '\xc3\xb3',
    '\xc3\xb4',
    '\xc3\xb5',
    '\xc3\xb6',
    '\xc3\xb8',
    '\xc3\xb9',
    '\xc3\xba',
    '\xc3\xbb',
    '\xc3\xbc',
    '\xc3\xbd',
    '\xc3\xbf',
    '\xc4\x84',
    '\xc4\x85',
    '\xc4\x86',
    '\xc4\x87',
    '\xc4\x8c',
    '\xc4\x8d',
    '\xc4\x8e',
    '\xc4\x8f',
    '\xc4\x98',
    '\xc4\x99',
    '\xc4\x9a',
    '\xc4\x9b',
    '\xc4\x9e',
    '\xc4\x9f',
    '\xc4\xb0',
    '\xc4\xb1',
    '\xc5\x81',
    '\xc5\x82',
    '\xc5\x83',
    '\xc5\x84',
    '\xc5\x87',
    '\xc5\x88',
    '\xc5\x90',
    '\xc5\x91',
    '\xc5\x92',
    '\xc5\x93',
    '\xc5\x98',
    '\xc5\x99',
    '\xc5\x9a',
    '\xc5\x9b',
    '\xc5\x9e',
    '\xc5\x9f',
    '\xc5\xa0',
    '\xc5\xa1',
    '\xc5\xa4',
    '\xc5\xa5',
    '\xc5\xae',
    '\xc5\xaf',
    '\xc5\xb0',
    '\xc5\xb1',
    '\xc5\xb8',
    '\xc5\xb9',
    '\xc5\xba',
    '\xc5\xbb',
    '\xc5\xbc',
    '\xc5\xbd',
    '\xc5\xbe',
    '\xd0\x84',
    '\xd0\x91',
    '\xd0\x93',
    '\xd0\x94',
    '\xd0\x96',
    '\xd0\x97',
    '\xd0\x98',
    '\xd0\x99',
    '\xd0\x9b',
    '\xd0\x9f',
    '\xd0\xa3',
    '\xd0\xa4',
    '\xd0\xa6',
    '\xd0\xa7',
    '\xd0\xa8',
    '\xd0\xa9',
    '\xd0\xaa',
    '\xd0\xab',
    '\xd0\xac',
    '\xd0\xad',
    '\xd0\xae',
    '\xd0\xaf',
    '\xd0\xb1',
    '\xd0\xb2',
    '\xd0\xb3',
    '\xd0\xb4',
    '\xd0\xb6',
    '\xd0\xb7',
    '\xd0\xb8',
    '\xd0\xb9',
    '\xd0\xba',
    '\xd0\xbb',
    '\xd0\xbc',
    '\xd0\xbd',
    '\xd0\xbf',
    '\xd1\x82',
    '\xd1\x84',
    '\xd1\x86',
    '\xd1\x87',
    '\xd1\x88',
    '\xd1\x89',
    '\xd1\x8a',
    '\xd1\x8b',
    '\xd1\x8c',
    '\xd1\x8d',
    '\xd1\x8e',
    '\xd1\x8f',
    '\xd1\x94',
    '\xd2\x90',
    '\xd2\x91',
]