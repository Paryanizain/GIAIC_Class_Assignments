class hospital():
    def __init__(self , Specialty):
        self.Doc_name = []
        self.Specialty = ['Specialist' ,Specialty]
        

    def add_doc(self, New_doc_add):
        return self.Doc_name.append(New_doc_add)
    
    def remove_doc(self , remove_doc):
        return self.Doc_name.remove(remove_doc)
    
    def get_doc(self):
        return self.Doc_name

doc1 = hospital('Heart and blood vessels')
print(doc1.Specialty)

class new_docs():
    def __init__(self , name):
        self.D_name = name

new_doc1 = new_docs('salman')
new_doc2 = new_docs('zain')
new_doc3 = new_docs('noor')

print(doc1.add_doc(new_doc1.D_name))
print(doc1.add_doc(new_doc2.D_name))
print(doc1.add_doc(new_doc3.D_name))
print(doc1.get_doc())
print(doc1.remove_doc('noor'))
print(doc1.Specialty)
print(doc1.get_doc())



class hospital_patient():
    def __init__(self , disease):
        self.patient_name = []
        self.disease = ['disease' ,disease]
        

    def add_patient(self, New_patient_add):
        return self.patient_name.append(New_patient_add)
    
    def remove_patient(self , remove_patient):
        return self.patient_name.remove(remove_patient)
    
    def get_patient(self):
        return self.patient_name

patient1 = hospital_patient('Heart problem')
print(patient1.disease)

class new_patients():
    def __init__(self , name):
        self.P_name = name

new_patient1 = new_patients('nafay')
new_patient2 = new_patients('ali')
new_patient3 = new_patients('talha')

print(patient1.add_patient(new_patient1.P_name))
print(patient1.add_patient(new_patient2.P_name))
print(patient1.add_patient(new_patient3.P_name))
print(patient1.get_patient())
print(patient1.remove_patient('talha'))
print(patient1.disease)
print(patient1.get_patient())


patient2 = hospital_patient('eye weakness')
patient2_new1 = new_patients('hamza')
print(patient2.add_patient(patient2_new1.P_name))
print(patient2.disease)
print(patient2.get_patient())