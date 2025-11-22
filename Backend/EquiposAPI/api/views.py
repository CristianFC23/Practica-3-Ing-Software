from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Patient, Laboratorist, LabResults
import json

# ---------------- Patients ----------------
@method_decorator(csrf_exempt, name='dispatch')
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

