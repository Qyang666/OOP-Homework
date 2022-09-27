class Patient:

#__init__ 
    def __init__(self,Id, name, address, phone, vs):
        self.__Id= Id
        self.__name= name
        self.__address = address
        self.__phone_num = phone
        self.__veteran_status = vs

# Accessor methods of each attributes

    def get_Id(self):
        return self.__Id

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone_num(self):
        return self.__phone_num

    def get_va(self):
        return self.__veteran_status

