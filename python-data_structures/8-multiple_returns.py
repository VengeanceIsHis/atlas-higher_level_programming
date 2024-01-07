#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        for i, char in enumerate(sentence):
            if i == 0:
                firstchar = char    
                length = i + 1
        return length, firstchar
    else:
    return 0, None
if __name__ == "__main__":
    main()
