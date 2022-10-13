from time import sleep
import requests

global api_url
global api_url_todos
api_url = "https://jsonplaceholder.typicode.com/users"
api_url_todos = "https://jsonplaceholder.typicode.com/todos"

class crud:
    def __init__(self):
        self.menu()
    
    def options(self):
        print('''
        0 - Sair
        1 - Listar todos os usuários
        2 - Criar um usuário
        3 - Atualizar um usuário
        4 - Deletar um usuário
        5 - Listar TODOs de um usuário
        6 - Criar uma tarefa
        7 - Atualizar uma tarefa
        8 - Deletar uma tarefa
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
                json =  self.list_todo(user_id)
                print('TODOs do usuário: ')
                for task in json:
                    print('Título: ', task['title'])
                    print('ID', task['id'])
                    print('Status: ', task['completed'])
                    print()
            elif op == 6:
                user_id = input('Digite o ID do usuário que deseja criar uma tarefa: ')
                print('Usuário seleionado: ', self.list_all_users(False)[int(user_id) - 1]['name'])
                title = input('Digite o título da tarefa: ')
                completed = input('Digite o status da tarefa (true/false): ')
                print('Tarefa criada! ', self.create_task(user_id, title, completed))
            elif op == 7:
                task_id = input('Digite o ID da tarefa que deseja atualizar: ')
                print('Tarefa selecionada: ', self.name_task(task_id))
                title = input('Digite o título da tarefa: ')
                completed = input('Digite o status da tarefa (true/false): ')
                print('Tarefa atualizada! ', self.update_task(task_id, title, completed))
            elif op == 8:
                task_id = input('Digite o ID da tarefa que deseja deletar: ')
                print('Tarefa deletada! Status da ação: ', self.delete_task(task_id))
            elif op == 0:
                print('Saindo...')
            else:
                print('Opção inválida!')
       
    
    def create_task(self, user_id, title, completed):
        return requests.post(api_url + "/" + str(user_id) + "/todos", data={"title": title, "completed": completed}).json()

    def update_task(self, task_id, title, completed):
        return requests.put(api_url_todos + "/" + str(task_id), data={"title": title, "completed": completed}).json()

    def list_user_tasks(self, user_id):
        return requests.get(api_url + "/" + str(user_id) + "/todos").json()

    def list_todo(self, user_id=None, task_id=None):
        return requests.get(api_url + "/" + str(user_id) + "/todos").json()

    def create_user(self, name, username, email):
        return requests.post(api_url, data={"name": name, "username": username, "email": email}).json()

    def update_user(self, user_id, name, username, email):
        return requests.put("api_url" + "/" + str(user_id), data={"name": name, "username": username, "email": email}).json()

    def delete_user(self, user_id):
        return requests.delete(api_url + "/" + str(user_id)).status_code

    def delete_task(self, task_id):
        return requests.delete(api_url_todos + "/" + str(task_id)).status_code

    def list_all_users(self, print_users = True):
        list = requests.get(api_url).json()
        if print_users:
            for user in list:
                print(user['name'])
        return list

    def name_task(self, task_id):
        return requests.get(api_url_todos + "/" + str(task_id)).json()['title']

if __name__ == "__main__":
    new_crud = crud()