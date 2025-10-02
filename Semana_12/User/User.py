from abc import ABC, abstractmethod


class User(ABC):

    def __init__(self,name):
        super().__init__()
        self.name = name

    @abstractmethod
    def get_role():
        pass

    @abstractmethod
    def has_permission(permission):
        pass

class AdminUser(User):

    def __init__(self, name):
        super().__init__(name)
    

    def get_role(self):
        return 'SuperUser'

    def has_permission(self,permission):
        if permission == 'delete' or permission == 'create' or permission == 'write' or permission == 'update' :
            return True
        else:
            return False

class RegularUser(User):
    def __init__(self, name):
        super().__init__(name)
    
    def get_role(self):
        return 'db_reader'
    
    def has_permission(self,permission):
        if permission == 'delete' or permission == 'create' or permission == 'write' or permission == 'update' :
            return False
        else:
            return True
    

def main():
    user1 = AdminUser('Mar')
    user2 = RegularUser('sha')
    print(f'User 1: {user1.name} - Rol: {user1.get_role()} - Permission Delete = {user1.has_permission('delete')} - Create = {user1.has_permission('create')} - Write = {user1.has_permission('update')} - Update = {user1.has_permission('update')} - Read Only = {user1.has_permission('read')}')
    print(f'User 2: {user2.name} - Rol: {user2.get_role()} - Permission Delete = {user2.has_permission('delete')} - Create = {user2.has_permission('create')} - Write = {user2.has_permission('update')} - Update = {user2.has_permission('update')} - Read Only = {user2.has_permission('read')}')



if __name__ == '__main__':
    main()