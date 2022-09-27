import PatientClass as pc
import ProcedureClass as proc_c


def main():

    #patients instance
    patient1=  pc.Patient(1,'Matt Jones', '123 Main st, Waco TX 76706', '254-555-7415','TRUE')
    #creating 3 procedure instances
    procedure1 = proc_c.Procedure('Physical Exam','2/15/2022', 'Dr. Irvine' ,250, 1)
    procedure2 = proc_c.Procedure('MRI','2/15/2022', 'Dr. Hamilton' ,1500, 1)
    procedure3 = proc_c.Procedure('CT Scan','2/17/2022', 'Dr. Drey' ,1200, 2)

    #initializing variables
    charge1 = 0
    charge2 = 0
    charge3 = 0
    disc_amnt = 0
    print()
    #print statement for the Bill

    print("****Patient Bill***")
    print("Name: ",patient1.get_name())
    print("Address: ",patient1.get_address())
    print("Phone: ",patient1.get_phone_num())
    print()

    #checking the IDs from both the classes to pull only the corresponding records of that patient
    if patient1.get_Id() == procedure1.get_patient_ID():
        print("Procedure: ",procedure1.get_name_of_proc())
        print("Date: ",procedure1.get_date_of_proc())
        print("Practioner: ",procedure1.get_name_of_practitioner())
        print("Charge: ",procedure1.get_charges_of_proc())
        charge1 = procedure1.get_charges_of_proc()
    print()
    if patient1.get_Id() == procedure2.get_patient_ID():
        print("Procedure: ",procedure2.get_name_of_proc())
        print("Date: ",procedure2.get_date_of_proc())
        print("Practioner: ",procedure2.get_name_of_practitioner())
        print("Charge: ",procedure2.get_charges_of_proc())
        charge2 = procedure2.get_charges_of_proc()

    print()
    if patient1.get_Id() == procedure3.get_patient_ID():
        print("Procedure: ",procedure3.get_name_of_proc())
        print("Date: ",procedure3.get_date_of_proc())
        print("Practioner: ",procedure3.get_name_of_practitioner())
        print("Charge: ",procedure3.get_charges_of_proc())
        charge3 = procedure2.get_charges_of_proc()

    #Sum of the individual procedure charges of the patient 1
    total_charge = charge1 + charge2 + charge3
    print("Total Amount before discount :", total_charge)
    #checking if the patient is Veteran or not
    if patient1.get_va() == 'TRUE':
        #providing 40% off for Veteran patient
        disc_amnt = 0.40* total_charge
    print("40 % Discount Amount if Veteran:",disc_amnt)

    #Reducing the discount amount from  the initial total charge
    total_charge = total_charge - disc_amnt
    print("Total charges : ",total_charge)



main()