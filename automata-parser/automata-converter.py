import xml.etree.ElementTree as ET
import os

def print_cpp_matrix(matrix, num_states, comment_matrix):
    print("int transitions[{}][128] = {{".format(num_states))
    for i in range(num_states):
        print("    {", end="")
        for j in range(128):
            print(matrix[i][j], end="")
            if comment_matrix[i][j]:
                print(f" /* {comment_matrix[i][j]} */", end="")
            if j < 127:
                print(", ", end="")
        print("},")
    print("};")

def create_cpp_matrix(states, transitions):
    num_states = len(states)
    num_symbols = 128  # Número de caracteres no alfabeto ASCII

    matrix = [[-1 for _ in range(num_symbols)] for _ in range(num_states)]
    comment_matrix = [["" for _ in range(num_symbols)] for _ in range(num_states)]

    for transition in transitions:
        start_state, symbol, end_state = transition
        comment = f"Transição de {start_state} para {end_state} com '{symbol}'"

        if symbol.startswith('[') and symbol.endswith(']'):
            symbol = symbol[1:-1]
            for char in symbol:
                if char == '-':
                    start_char = ord(symbol[symbol.index('-') - 1])
                    end_char = ord(symbol[symbol.index('-') + 1])
                    for char_code in range(start_char, end_char + 1):
                        if char_code < num_symbols:
                            matrix[start_state][char_code] = end_state
                            comment_matrix[start_state][char_code] = comment
                else:
                    char_code = ord(char)
                    if char_code < num_symbols:
                        matrix[start_state][char_code] = end_state
                        comment_matrix[start_state][char_code] = comment
        else:
            if symbol == "\\n":
                char_code = 10
            else:
                char_code = ord(symbol)
            if char_code < num_symbols:
                matrix[start_state][char_code] = end_state
                comment_matrix[start_state][char_code] = comment

    return matrix, comment_matrix


# Caso seu arquivo JFF(Jflap) nao esteja no mesmo diretorio que seu script de python insira o caminho aqui
file_path = os.path.join("C:\\", "Users", "marco", "Downloads", "lista_5_exercicio_1.jff")

# Insiram aqui o nome do arquivo do automato caso o script esteja na mesma pasta que o seu arquivo JFLAP
tree = ET.parse("automato_5-2.jff")
root = tree.getroot()

transitions = []
for transition_element in root.findall(".//transition"):
    from_state = int(transition_element.find(".//from").text)
    to_state = int(transition_element.find(".//to").text)
    symbol = transition_element.find(".//read").text
    transitions.append((from_state, symbol, to_state))

# Encontrar o número de estados
states_element = root.findall(".//state")
num_states = len(states_element)

matrix, comment_matrix = create_cpp_matrix(list(range(num_states)), transitions)

# Imprimir a matriz em formato C++
print_cpp_matrix(matrix, num_states, comment_matrix)
