palavras = ('aprender', 'progamar', 'linguagem', 'python', 
             'curso', 'gratis', 'estudar', 'praticar', 
             'trabalhar', 'mercado', 'progamador', 'futuro')

for p in palavras:
    print(f'\nNa palavra {p} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='  ')