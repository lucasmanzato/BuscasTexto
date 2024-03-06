def naive(T, P):
    n = len(T)
    m = len(P)

    for s in range(n - m + 1):
        if T[s:s + m] == P:
            print(f"Padrão ocorre com deslocamento {s}")

def naiveElCoringa(T, P):
    n = len(T)
    m = len(P)

    for s in range(n - m + 1):
        match = True
        for i in range(m):
            if P[i] != "x" and T[s + i] != P[i]:
                match = False
                break
        if match:
            print(f"Padrão ocorre com deslocamento {s}")

def rabinKarpMatcher(T, P, d, q):
    n = len(T)
    m = len(P)
    h = pow(d, m - 1, q)
    p = 0
    t = 0

    for i in range(m):
        p = (d * p + ord(P[i])) % q
        t = (d * t + ord(T[i])) % q


    for s in range(n - m + 1):
        if p == t:
            if P == T[s:s + m]:
                print(f"Padrão ocorre com deslocamento {s}")

        if s < n - m:
            t = (d * (t - ord(T[s]) * h) + ord(T[s + m])) % q

def rabinKarpiText(T, P, d, q):
    n = len(T)
    m = max(len(P) for P in P)
    h = pow(d, m - 1, q)

    def hash_string(s):
        hash_value = 0
        for char in s:
            hash_value = (d * hash_value + ord(char)) % q
        return hash_value

    pattern_hashes = [hash_string(P) for P in P]
    
    t = hash_string(T[:m])

    for s in range(n - m + 1):
        if any(pattern_hashes[i] == t for i, P in enumerate(P)):
            print(f"Padrão ocorre com deslocamento {s}")

        if s < n - m:
            t = (d * (t - ord(T[s]) * h) + ord(T[s + m])) % q

def default():
    print("Opção inválida.")

def main():
    opc = int(input("OPCOES:\n1- Naive String Matcher\n2- Naive String Matcher com elemento coringa\n3- Rabin Karp Matcher \n4- Rabin karp Matcher (text)\nDigite a Opcao Desejada: "))

    if opc == 1:
        texto = "luclucascaslucaslu"
        padrao = "lucas"
        naive(texto, padrao)

    elif opc == 2:
        texto = "luclucasulcaslucaslu"
        padrao = "lucxs"
        naiveElCoringa(texto, padrao)

    elif opc == 3:
        texto = "luclucascaslucaslu"
        padrao = "lucas"
        d = 256 
        q = 101  
        rabinKarpMatcher(texto, padrao, d, q)

    elif opc == 4:
        texto = "Era uma vez, em uma terra distante, um pequeno vilarejo. Neste vilarejo, vivia um jovem chamado João, que sonhava em aventuras. Um dia, João decidiu partir em uma jornada para explorar o mundo."

        padrao = ["João", "vilarejo", "aventuras"]
        d = 256  
        q = 101  
        rabinKarpiText(texto, padrao, d, q)

    else:
        default()

main()
