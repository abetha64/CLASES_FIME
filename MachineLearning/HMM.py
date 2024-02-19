from tabulate import tabulate
from colorama import Fore, init, Style
init()

# Solicitar al usuario los estados y las probabilidades iniciales
estados = ['Casa', 'Oficina', 'Cafe']
val_pi = {'Casa': 0.4, 'Oficina': 0.4, 'Cafe': 0.2}

# Solicitar al usuario las probabilidades de transición (Tabla A)
tb_A = {'Casa': {'Casa': 0.2, 'Oficina': 0.6, 'Cafe': 0.2},
        'Oficina': {'Casa': 0.5, 'Oficina': 0.2, 'Cafe': 0.3},
        'Cafe': {'Casa': 0.2, 'Oficina': 0.8, 'Cafe': 0.0}}

# Solicitar al usuario las probabilidades de emisión (Tabla B)
tb_B = {'Casa': {'wb': 0.3, 'fb': 0.5, 'email': 0.2},
        'Oficina': {'wb': 0.1, 'fb': 0.1, 'email': 0.8},
        'Cafe': {'wb': 0.8, 'fb': 0.1, 'email': 0.1}}

observacion_1 = ['wb', 'email', 'wb', 'fb']

def forward_backward(obs, states, start_p, trans_p, emit_p):
    # Forward algorithm
    forward = [{}]
    for st in states:
        forward[0][st] = start_p[st] * emit_p[st][obs[0]]

    for t in range(1, len(obs)):
        forward.append({})
        for st in states:
            forward[t][st] = sum(forward[t - 1][prev_st] * trans_p[prev_st][st] * emit_p[st][obs[t]] for prev_st in states)

    # Backward algorithm
    backward = [{} for _ in range(len(obs))]
    for st in states:
        backward[len(obs) - 1][st] = 1

    for t in range(len(obs) - 2, -1, -1):
        for st in states:
            backward[t][st] = sum(trans_p[st][next_st] * emit_p[next_st][obs[t + 1]] * backward[t + 1][next_st] for next_st in states)

    # Calculate the probability of the sequence
    prob = sum(forward[len(obs) - 1][final_st] for final_st in states)

    # Print Forward and Backward tables
    print('\n ###################### Forward Table ###################### \n')
    forward_table = [[forward[i][st] for st in states] for i in range(len(obs))]
    print(tabulate(forward_table, headers=states, tablefmt="grid"))

    print('\n ###################### Backward Table ###################### \n')
    backward_table = [[backward[i][st] for st in states] for i in range(len(obs))]
    print(tabulate(backward_table, headers=states, tablefmt="grid"))

    # Obtain the most likely sequence of states
    optimal_sequence = []
    for t in range(len(obs)):
        max_state = max(states, key=lambda state: forward[t][state] * backward[t][state])
        optimal_sequence.append(max_state)

    return prob, optimal_sequence

# Main
if __name__ == "__main__":
    # Observations
    print(Fore.RED +'\n Forward-Backward Algorithm \n'+ Style.RESET_ALL)
    probability, sequence = forward_backward(observacion_1, estados, val_pi, tb_A, tb_B)
    print(Fore.MAGENTA +"\n\n La probabilidad de la secuencia observada es:"+ Style.RESET_ALL, probability)
    print(Fore.YELLOW +"La secuencia de estados más probable es:"+ Style.RESET_ALL, sequence)
