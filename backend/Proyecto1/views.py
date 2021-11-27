from django.http import HttpResponse
from django.http.response import JsonResponse
#from django.template import Template, Context
#from django.template import loader
from bdapp.models import Handler as myHandler




def reciver(request):
    
    if(request.method=="POST"):

        try:
            file=request.FILES['file']
        except:
            return badRequestHandler()
        
        if file.name.endswith('.csv'):
            if not file.multiple_chunks():
                
                try:
                    file_data = file.read().decode("utf-8", errors='ignore')	
                    lines = file_data.split("\n")
                except:
                    return badRequestHandler()

                list_dict = []
                for line in lines:
                    fields = line.split(";")
                    if len(fields)>1:
                        data_dict = {}
                        data_dict["name"] = fields[0]
                        data_dict["age"] = fields[1]
                        data_dict["club"] = fields[2]
                        data_dict["state"] = fields[3]
                        data_dict["estudios"] = fields[4]
                        list_dict.append(data_dict)

                cantTotalSocios=myHandler.getCantidadTotalDeSocios(list_dict)
                edadPromedioSociosDeRaciog=myHandler.getEdadPromedioSociosDeRacing(list_dict)
                PrimerasCienPersonasCasadasConEstudiosUniversitariosOrdenadosPorEdad=myHandler.getPrimerasCienPersonasCasadasConEstudiosUniversitariosOrdenadosPorEdad(list_dict)
                #for socio in PrimerasCienPersonasCasadasConEstudiosUniversitariosOrdenadosPorEdad:
                    #print("Nombre: ",socio["name"],"Edad: ",socio["age"],"Club: ",socio["club"],"\n")

                cincoNombresMasComunes=myHandler.getCincoNombresMasComunes(list_dict)
                #print("los nombres mas comunes son: \n")
                #for nombre in cincoNombresMasComunes:
                    #print(nombre[0])

                listadoFinal=myHandler.getListadoFinal(list_dict)
                #print("\n \n El listado es: \n")
                #for informationOfClub in listadoFinal:
                    #print("Club: ",informationOfClub["nombre"],
                        #"Edad primedio: ",informationOfClub["edad_promedio"],
                        #"Maxima edad: ",informationOfClub["maxima_edad"],
                        #"minima edad: ",informationOfClub["minima_edad"], "\n")

                aJson={"result1":cantTotalSocios,
                "result2":edadPromedioSociosDeRaciog,
                "result3":PrimerasCienPersonasCasadasConEstudiosUniversitariosOrdenadosPorEdad,
                "result4":cincoNombresMasComunes,
                "result5":listadoFinal}

                return JsonResponse(aJson)
            return badRequestHandler()
        return badRequestHandler()
    return badRequestHandler()

def badRequestHandler():
    return JsonResponse({})