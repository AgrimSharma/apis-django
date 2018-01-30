from doctorbox_web.api.models import Patient


class PatientDeviceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        device_identifier = request.META.get('HTTP_DEVICE_IDENTIFIER', None)
        is_mobile_client = request.META.get('HTTP_CLIENT_VERSION', None)
        if device_identifier is not None and is_mobile_client is not None:
            try:
                patient = Patient.objects.get(device_identifier=device_identifier)
            except Patient.DoesNotExist:
                patient = Patient.objects.create(device_identifier=device_identifier)
            request.patient = patient

        response = self.get_response(request)

        return response
