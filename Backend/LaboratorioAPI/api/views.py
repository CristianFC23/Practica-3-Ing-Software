from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Patient, Laboratorist, LabResults
import json

# ---------------- Patients ----------------
class PatientView(View):

    def get(self, request, id=None):
        if id:
            try:
                patient = Patient.objects.get(id=id)
                data = {
                    "id": patient.id,
                    "name": patient.name,
                    "lastname": patient.lastname,
                    "documento": patient.documento,
                    "cod_ing": patient.cod_ing,
                    "direccion": patient.direccion,
                    "telefono": patient.telefono
                }
                return JsonResponse(data, status=200)
            except Patient.DoesNotExist:
                return JsonResponse({"error": "Patient not found"}, status=404)
        else:
            patients = list(Patient.objects.values())
            return JsonResponse(patients, safe=False, status=200)

    def post(self, request):
        try:
            data = json.loads(request.body)
            patient = Patient.objects.create(**data)
            return JsonResponse({"message": "Patient created", "id": patient.id}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    def put(self, request, id):
        try:
            data = json.loads(request.body)
            patient = Patient.objects.get(id=id)
            for field, value in data.items():
                setattr(patient, field, value)
            patient.save()
            return JsonResponse({"message": "Patient updated"}, status=200)
        except Patient.DoesNotExist:
            return JsonResponse({"error": "Patient not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    def delete(self, request, id):
        try:
            patient = Patient.objects.get(id=id)
            patient.delete()
            return JsonResponse({"message": "Patient deleted"}, status=200)
        except Patient.DoesNotExist:
            return JsonResponse({"error": "Patient not found"}, status=404)


# ========================== LABORATORISTAS ==========================
@method_decorator(csrf_exempt, name='dispatch')
class LaboratoristView(View):

    def get(self, request, id=0):
        if id > 0:
            labs = list(Laboratorist.objects.filter(id=id).values())
            if len(labs) > 0:
                datos = {"message": "Success", "laboratorist": labs[0]}
            else:
                datos = {"message": "Laboratorist not found"}
        else:
            labs = list(Laboratorist.objects.values())
            datos = {"message": "Success", "laboratorists": labs}
        return JsonResponse(datos, safe=False)

    def post(self, request):
        try:
            JsonData = json.loads(request.body)
            Laboratorist.objects.create(
                name=JsonData["name"],
                lastname=JsonData["lastname"],
                cod_int=JsonData["cod_int"],
                titulo=JsonData["titulo"],
                telefono=JsonData["telefono"]
            )
            return JsonResponse({"message": "Laboratorist created successfully"})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    def put(self, request, id):
        try:
            JsonData = json.loads(request.body)
            lab = Laboratorist.objects.filter(id=id).first()
            if lab:
                lab.name = JsonData["name"]
                lab.lastname = JsonData["lastname"]
                lab.cod_int = JsonData["cod_int"]
                lab.titulo = JsonData["titulo"]
                lab.telefono = JsonData["telefono"]
                lab.save()
                return JsonResponse({"message": "Laboratorist updated successfully"})
            else:
                return JsonResponse({"message": "Laboratorist not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    def delete(self, request, id):
        lab = Laboratorist.objects.filter(id=id).first()
        if lab:
            lab.delete()
            return JsonResponse({"message": "Laboratorist deleted successfully"})
        else:
            return JsonResponse({"message": "Laboratorist not found"}, status=404)

# ---------------- Lab Results ----------------
class LabResultsView(View):

    def get(self, request, id=None):
        if id:
            try:
                result = LabResults.objects.get(id=id)
                data = {
                    "id": result.id,
                    "cedula": result.cedula,
                    "cod_ing_r": result.cod_ing_r,
                    "col_tot": result.col_tot,
                    "col_hdl": result.col_hdl,
                    "col_ldl": result.col_ldl,
                    "trig": result.trig
                }
                return JsonResponse(data, status=200)
            except LabResults.DoesNotExist:
                return JsonResponse({"error": "Lab result not found"}, status=404)
        else:
            results = list(LabResults.objects.values())
            return JsonResponse(results, safe=False, status=200)

    def post(self, request):
        try:
            data = json.loads(request.body)
            result = LabResults.objects.create(**data)
            return JsonResponse({"message": "Lab result created", "id": result.id}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)