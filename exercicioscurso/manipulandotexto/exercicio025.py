#META: criar um progama para verificar se seu nome tem 'silva';


name = str(input('type your name ')).strip()
print('your name he has silva?\n')
print('Seu nome tem silva? {}'.format('silva' in name.lower()))