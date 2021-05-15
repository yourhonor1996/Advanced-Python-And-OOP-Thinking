input_str = input()

def bolandgoo(word:str):
    # print(word)
    for i in range(1, len(word)+1):
        word = word[i-1]*i + word[i:]
        print(word)
        
bolandgoo(input_str)