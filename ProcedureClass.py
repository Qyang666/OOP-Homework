class Procedure:

#__init__ method 
    def __init__(self,name_of_proc, date_of_proc, name_of_practitioner , charges_of_proc, patient_ID):
        self.__name_of_proc= name_of_proc
        self.__date_of_proc= date_of_proc
        self.__name_of_practitioner = name_of_practitioner
        self.__charges_of_proc = charges_of_proc
        self.__patient_ID = patient_ID

#methods 

    def get_name_of_proc(self):
        return self.__name_of_proc

    def get_date_of_proc(self):
        return self.__date_of_proc

    def get_name_of_practitioner(self):
        return self.__name_of_practitioner

    def get_charges_of_proc(self):
        return self.__charges_of_proc

    def get_patient_ID(self):
        return self.__patient_ID