class Bank:
    name='Bank Etika'
    users=[]
    
    def add_users(self, user):
        self.users.append(user)

    def authentication(self, name, account_number):
        for i in range(len(self.users)):
            if name in self.users[i].account.values() and account_number in self.users[i].account.values():
                print()
                print("Authentication successful!")
                return self.clients[i]