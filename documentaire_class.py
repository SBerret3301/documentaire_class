class Documentaire() :
    
    _count = 0
    def __init__(self, titre, date):
        self.__titre = titre
        self.__date = date
        Documentaire._count +=1

    
    def gettitre(self) :
        return self.__titre
    
    def getdate(self) :
        return self.__date
    
    def getcode(self) :
        return Documentaire._count

    def settitre(self, titre) :
        self.__titre = titre

    def setdate(self, date) :
        self.__date = date

    def getcount(self) :
        return Documentaire._count
    
    def ToString(self) :
        return "Code : ", Documentaire._count, "titre : ", self.gettitre(), "date : ", self.getdate()
    
    def Equals(self, doc) :
        if self.getcode == doc.getcode :
            return True
        else :
            return False



class Exemplaire(Documentaire) :
    def __init__(self, titre, date, numero, date_dachat) :
        super().__init__(titre, date)
        self.__numero = numero
        self.__date_dachat = date_dachat
    def getnumero(self) :
        return self.__numero
    def getdatedachat(self) :
        return self.__date_dachat
    def setnumero(self, numero) :
        self.__numero = numero
    def setdatedachat(self, datedachat) :
        self.__date_dachat = datedachat
    def ToString(self) :
        return super().ToString(), "numero : ", self.getnumero(), "date d'achat : ", self.getdatedachat()
    
    
doc1 = Documentaire("computer", 11122003)

print(doc1.ToString())

exemple1 = Exemplaire("python", 1232004, 70, 12122020)

print(exemple1.ToString())

print(doc1.Equals(exemple1))