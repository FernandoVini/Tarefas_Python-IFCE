"""
    Módulo cliente -
    Classe Cliente -
    Atributos:
        _id       - chave primária    - informado
        _nome     - nome do cliente   - informado
        _codigo   - codigo do cliente - informado
        _cnpjcpf  - cnpj ou cpf       - informado
        _tipo     - tipo do cliente   - informado
                    (Pessoa Fisica ou Juridica)

"""



class Cliente():
    def __init__(self, id, nome, codigo, cnpjcpf):
        self._id = id
        self._nome = nome
        self._codigo = codigo
        self._cnpjcpf = cnpjcpf

    def str(self):
        string = "\nId={3} Codigo={2} Nome={1} CNPJ/CPF={0} ".format(self._cnpjcpf, self._codigo,
                                                                             self._nome, self._id)
        return string


if __name__ == '__main__':
    cliente = Cliente(1, "Jose Maria", 100, '200.100.345-34' )
    print(cliente.str())

