class Wallet:
    def __init__(self, client, balance):
        self.client = client 
        self.balance = balance 
    def client_info(self):
        return "Клиент: \"" + self.client + "\", Баланс: " + str(self.balance) + " руб." 
    
        
client1 = Wallet("Иван Петров", 50)   
print(client1.client_info())

