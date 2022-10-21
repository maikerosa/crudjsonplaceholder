import requests
global api_url
global api_url_todos
api_url = "https://jsonplaceholder.typicode.com/users"
api_url_todos = "https://jsonplaceholder.typicode.com/todos"


class uw():
    def __init__(self):
        self.user_id = self.valid_user_id()

    def valid_user_id(self):
        user_id = 11
        while user_id > 10 or user_id < 1:
            user_id = input('Digite o ID do usuário que deseja atualizar (0>n<10): ')
            try:
                user_id_str  = str(user_id)
                user_id = int(user_id_str)
            except:
                print('ID inválido!')
                user_id = 11
                continue

        return user_id



    
    def create_task(self, user_id, title, completed):
        return requests.post(api_url + "/" + str(user_id) + "/todos", data={"title": title, "completed": completed}).json()

    def update_task(self, task_id, title, completed):
        return requests.put(api_url_todos + "/" + str(task_id), data={"title": title, "completed": completed}).json()

    def list_user_tasks(self, user_id):
        return requests.get(api_url + "/" + str(user_id) + "/todos").json()

    def list_todo(self, user_id):
        return requests.get(api_url + "/" + str(user_id) + "/todos").json()

    def create_user(self, name, username, email):
        return requests.post(api_url, data={"name": name, "username": username, "email": email}).json()

    def read_user(self, user_id):
        return requests.get(api_url + "/" + str(user_id)).json()

    def update_user(self, user_id, name, username, email):
        return requests.put(api_url + "/" + str(user_id), data={"name": name, "username": username, "email": email}).json()

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