from Api import consulta

print("Seja bem vindo ao Busca Cep:)")

while True:
    print("Insira o cep:")
    cep = input()
    consulta(cep)

    #O usuario informa se deseja consultar outro cep ou não
    print("Deseja consultar outro cep ?")
    print("Y/N")
    resposta_usu = input().lower()

    #if para caso o usuario não queira consultar outro cep
    if resposta_usu != "y":
        print("Obrigado por usar nosso sistema:")
        break