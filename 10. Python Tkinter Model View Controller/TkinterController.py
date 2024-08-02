class Controller:
    def __init__(self, model, view):
        self.model= model
        self.view= view

    def save(self,email):
        try:
            self.model.email= email
            self.model.save()
            self.view.show_sucess(f'O email {email} foi salvo!')

        except ValueError as error:
            self.view.show_error(error)