import pcs_lexer as pcs


def main():
    while True:
        try:
            s = input('>> ')
        except EOFError:  # ctr + D
            pass
        pcs.parser.parse(s)


if __name__ == '__main__': main()