#META: criar um progama que de 10 termos de uma progressao aritmetica;

primeirotermo = int(input('primeiro termo: '))
razao = int(input('razao: '))
decimo = primeirotermo + (10 - 1) * razao
for ordem in range(primeirotermo, decimo + razao , razao):
    print('{} -> '.format(ordem), end= ' ')
    
print('ACABOU')