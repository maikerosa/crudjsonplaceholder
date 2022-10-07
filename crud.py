from time import sleep
import requests

global api_url
api_url = "https://jsonplaceholder.typicode.com/users"

class crud:
    def __init__(self):
        self.menu()
    
    def options(self):
        print('''
        1 - Listar todos os usuários
        2 - Criar um usuário
        3 - Atualizar um usuário
        4 - Deletar um usuário
        5 - Listar TODOs de um usuário
        6 - Deletar uma tarefa
        ''')
    
    def menu(self):
        op = -1
        while op != 0:
            sleep(2)
            self.options()
            op = int(input("Digite a opção desejada: "))
            if op == 1:
                self.list_all_users()
            elif op == 2:
                name = input('Digite o seu nome: ')
                username = input('Seu usuário: ')
                email = input('Seu email: ')
                print('Usuário criado! ', self.create_user(name, username, email))
            elif op == 3:
                user_id = 11
                while user_id > 10 or user_id < 1:
                    user_id = input('Digite o ID do usuário que deseja atualizar (0>n<10): ')
                    try:
                        user_id = int(user_id)
                    except:
                        print('ID inválido!')
                        user_id = 11
                        continue
                name = input('Digite o seu nome: ')
                username = input('Seu usuário: ')
                email = input('Seu email: ')
                print('Usuário atualizado! ' , self.update_user(user_id, name, username, email))
            elif op == 4:
                user_id = input('Digite o ID do usuário que deseja deletar: ')
                print('Usuário deletado! Status da ação: ', self.delete_user(user_id))
            elif op == 5:
                user_id = input('Digite o ID do usuário que deseja ver os TODOs: ')
                print('TODOs do usuário: ', self.list_todo(user_id))
            elif op == 6:
                task_id = input('Digite o ID da tarefa que deseja deletar: ')
                print('Tarefa deletada! Status da ação: ', self.delete_task(task_id))
            elif op == 0:
                print('Saindo...')
            else:
                print('Opção inválida!')
       
    
    def list_todo(self, user_id):
        return requests.get(api_url + "/" + str(user_id) + "/todos").json()

    def create_user(self, name, username, email):
        return requests.post(api_url, data={"name": name, "username": username, "email": email}).json()

    def update_user(self, user_id, name, username, email):
        return requests.put(api_url + "/" + str(user_id), data={"name": name, "username": username, "email": email}).json()

    def delete_user(self, user_id):
        return requests.delete(api_url + "/" + str(user_id)).status_code

    def delete_task(self, task_id):
        return requests.delete(api_url + "/" + str(task_id)).status_code

    def list_all_users(self):
        list = requests.get(api_url).json()
        for user in list:
            print(user['name'])
        return list

if __name__ == "__main__":
    new_crud = crud()