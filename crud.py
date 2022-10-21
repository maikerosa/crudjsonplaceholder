from time import sleep
from users_wrapper import uw as users
class crud:
    def __init__(self,):
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
        9 - Listar usuário específico
        ''')
    
    def menu(self):
        op = -1
        while op != 0:
            sleep(2)
            self.options()
            op = int(input("Digite a opção desejada: "))
            if op == 1:
                users.list_all_users(self)
            elif op == 2:
                name = input('Digite o seu nome: ')
                username = input('Seu usuário: ')
                email = input('Seu email: ')
                print('Usuário criado! ', users.create_user(self, name, username, email))
            elif op == 3:
                user_id =  users.valid_user_id().user_id
                name = input('Digite o seu nome: ')
                username = input('Seu usuário: ')
                email = input('Seu email: ')
                print('Usuário atualizado! ' , users.update_user(self, user_id, name, username, email))
            elif op == 4:
                user_id = users.valid_user_id().user_id
                print('Usuário deletado! Status da ação: ', users.delete_user(self, user_id))
                
            elif op == 5:
                user_id =  users.valid_user_id(self)
                json =  users.list_todo(self, user_id)
                print('TODOs do usuário: ')
                for task in json:
                    print('Título: ', task['title'])
                    print('ID', task['id'])
                    print('Status: ', task['completed'])
                    print()
            elif op == 6:
                user_id = users.valid_user_id(self)
                print('Usuário selecionado: ', users.list_all_users(self, False)[int(user_id) - 1]['name'])
                title = input('Digite o título da tarefa: ')
                completed = input('Digite o status da tarefa (true/false): ')
                print('Tarefa criada! ', users.create_task(self, user_id, title, completed))
            elif op == 7:
                task_id = input('Digite o ID da tarefa que deseja atualizar: ')
                print('Tarefa selecionada: ', users.name_task(self, task_id))
                title = input('Digite o título da tarefa: ')
                completed = input('Digite o status da tarefa (true/false): ')
                print('Tarefa atualizada! ', users.update_task(self, task_id, title, completed))
            elif op == 8:
                task_id = input('Digite o ID da tarefa que deseja deletar: ')
                print('Tarefa deletada! Status da ação: ', users.delete_task(self, task_id))
            elif op == 9:
                user_id =  users.valid_user_id(self)
            
                print('Usuário selecionado: ', users.read_user(self, user_id))
            elif op == 0:
                print('Saindo...')
            else:
                print('Opção inválida!')
       
    
    

if __name__ == "__main__":
    new_crud = crud()