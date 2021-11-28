from typing import final
from django.db import models
from collections import Counter




def getEdadMinima(data,club):
    actualMinumAge=1000
    for partner in data:
        if partner["club"]==club:
         if int(partner["age"])<actualMinumAge:
            actualMinumAge=int(partner["age"])
    return actualMinumAge

def cantidadSocios(e):
            return e['cant_socios']


def getClubesName(data):
    listaDeClubes=[]
    for partner in data:
        if not partner["club"] in listaDeClubes :
            listaDeClubes.append(partner["club"])
    return listaDeClubes
def getCantidadDeSociosEnClub(data,club):
    cantidad=0
    for partner in data:
        if partner["club"] == club:
            cantidad+=1
                    
    return cantidad
def getEdadPromedioSocios(data,club):
    actualTotalAge=0
    actualQuantityOfPartners=0
    result=0
    for partner in data:
        if partner["club"]==club:
            actualTotalAge+=int(partner["age"])
            actualQuantityOfPartners+=1
        if(actualQuantityOfPartners!=0):
            result=actualTotalAge/actualQuantityOfPartners
    return result

def getEdadMaxima(data,club):
    actualMaxAge=-1
    for partner in data:
        if partner["club"]==club:
            if int(partner["age"])>actualMaxAge:
                actualMaxAge=int(partner["age"])
    return actualMaxAge

class Handler(models.Model):

    def getCantidadTotalDeSocios(data):
        return len(data)

    def getEdadPromedioSociosDeRacing(data):
        return getEdadPromedioSocios(data,"Racing")
       
    
    
    def getPrimerasCienPersonasCasadasConEstudiosUniversitariosOrdenadosPorEdad(data):
        def age(e):
            return e['age']
        
        listOfPartners=[]
        for partner in data:
            if partner["estudios"]=="Universitario\r" and partner["state"]=="Casado":
                listOfPartners.append(partner)
        listOfPartners=listOfPartners[0:100]
        
        listOfPartners.sort(key=age)
        return listOfPartners

    
    def getCincoNombresMasComunes(data):
        def getHinchasDeRiverName(data):
            namesList=[]
            for partner in data:
                if partner["club"]=="River":
                    namesList.append(partner["name"])
            return namesList
    
        namesList=getHinchasDeRiverName(data)
        moreCommons=Counter(namesList)
        fiveMoreCommons=moreCommons.most_common(5)
        
        return fiveMoreCommons
    
    def getListadoFinal(data):

        listOfClubs=getClubesName(data)
        finalListOfClubsData=[]
        for club in listOfClubs:
            club_dict = {}
            club_dict["nombre"] = club
            club_dict["cant_socios"] = getCantidadDeSociosEnClub(data,club)
            club_dict["edad_promedio"] = getEdadPromedioSocios(data,club)
            club_dict["maxima_edad"] = getEdadMaxima(data,club)
            club_dict["minima_edad"] = getEdadMinima(data,club)
            finalListOfClubsData.append(club_dict)
        finalListOfClubsData.sort(key=cantidadSocios)
        return finalListOfClubsData
    

 