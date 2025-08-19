class Fila:

    def __init__(self):
        self.fila = []

    def add(self, senha, prioridade, identidade):
        self.fila.append({
            "senha": senha,
            "prioridade": prioridade,
            "identidade": identidade
        })
        return self.posicaoFila(senha)

    def chamar_normal(self):
        if not self._vazia():
            return self.fila.pop(0)
        else:
            raise IndexError("Fila vazia")
            
    def chamar_prioridade(self):
        if self._vazia():
            raise IndexError("Fila vazia")
        for p in [1, 2, 3]:
            for i, item in enumerate(self.fila):
                if item["prioridade"] == p:
                    return self.fila.pop(i)  # remove e retorna
        return self.fila.pop(0)            


    def _vazia(self):
        return len(self.fila) == 0
        

    def verFila(self):
        return [
            {
                "senha": item["senha"],
                "prioridade": item["prioridade"],
                "identidade": item["identidade"],
                "posicao": self.posicaoFila(item["senha"])
            }
            for item in self.fila
        ]

    def tamanhoFila(self):
        return len(self.fila)

    def posicaoFila(self, senha):
        senha = senha.replace("'\\'", "").replace('"', "")
        print("   " + senha)
        for i, item in enumerate(self.fila):
            if item["senha"] == senha:
                return i + 1
        return None

