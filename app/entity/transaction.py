from app.entity.entity import Entity


class Transaction(Entity):
    def __init__(self):
        self.transaction_id = None
        self.user_id = None
        self.user_type = None
        self.transaction_date = None
        self.transaction_type = None
        self.amount = None
        self.converted_amount = None
        self.converted_comission = None
        self.comission = None
        self.currency = None
        self.is_previous_free = None
        self.is_discounted = None

    def to_array(self):
        return {
            'transaction_id': self.get_transaction_id(),
            'user_id': self.get_user_id(),
            'user_type': self.get_user_type(),
            'transaction_date': self.get_transaction_date(),
            'transaction_type': self.get_transaction_type(),
            'amount': self.get_amount(),
            'converted_amount': self.get_converted_amount(),
            'comission': self.get_converted_comission(),
            'currency': self.get_currency(),
            'is_previous_free': self.get_is_previous_free(),
            'is_discounted': self.get_is_discounted()
        }

    def get_is_discounted(self):
        return self.is_discounted

    def set_is_discounted(self, is_discounted):
        self.is_discounted = is_discounted

    def get_is_previous_free(self):
        return self.is_previous_free

    def set_is_previous_free(self, is_previous_free):
        self.is_previous_free = is_previous_free

    def get_transaction_id(self):
        return self.transaction_id

    def set_transaction_id(self, transaction_id):
        self.transaction_id = transaction_id

    def get_user_id(self):
        return self.user_id

    def set_user_id(self, user_id):
        self.user_id = user_id

    def get_user_type(self):
        return self.user_type

    def set_user_type(self, user_type):
        self.user_type = user_type

    def get_transaction_date(self):
        return self.transaction_date

    def set_transaction_date(self, transaction_date):
        self.transaction_date = transaction_date

    def get_transaction_type(self):
        return self.transaction_type

    def set_transaction_type(self, transaction_type):
        self.transaction_type = transaction_type

    def get_amount(self):
        return self.amount

    def set_amount(self, amount):
        self.amount = amount

    def get_converted_amount(self):
        return self.converted_amount

    def set_converted_amount(self, converted_amount):
        self.converted_amount = converted_amount

    def get_converted_comission(self):
        return self.converted_comission

    def set_converted_comission(self, converted_comission):
        self.converted_comission = converted_comission

    def get_comission(self):
        return self.comission

    def set_comission(self, comission):
        self.comission = comission

    def get_currency(self):
        return self.currency

    def set_currency(self, currency):
        self.currency = currency