class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self):
        # Crea un nuevo bloque y lo añade a la cadena
        pass

    def new_transaction(self, sender, recipient, amount):
        # Añade una nueva transacción a la lista de transacciones
        pass

    @staticmethod
    def hash(block):
        # Hace hash de un bloque
        pass

    @property
    def last_block(self):
        # Devuelve el último bloque de la cadena
        pass
