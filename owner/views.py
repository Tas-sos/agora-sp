from django.http import JsonResponse
from owner import models
from service import models as service_models
from rest_framework.decorators import *
from common import helper, strings
import re


# Returns a list of the service owners
@api_view(['GET'])

def get_service_owner(request, service_name_or_uuid):
    """
    Retrieves a the service owner

    """

    response = {}
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")
    result = prog.match(service_name_or_uuid)
    service, parsed_name, uuid = None, None, None

    if result is None:
        parsed_name = service_name_or_uuid.replace("_", " ").strip()
    else:
        uuid = service_name_or_uuid

    try:
        if result is None:
            service = service_models.Service.objects.get(name=parsed_name)
        else:
            service = service_models.Service.objects.get(id=uuid)

    except service_models.Service.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_NOT_FOUND)

    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response = helper.get_error_response(strings.INVALID_UUID)

    if service is not None:
        response = helper.get_response_info(strings.SERVICE_OWNER_INFORMATION, service.get_service_owners())

    return JsonResponse(response)


# Returns the institution of the service owner by both name and uuid
@api_view(['GET'])
def get_service_owner_institution(request, service_name_or_uuid, service_owner):
    """
    Retrieves the institution of the owner

    """

    response = {}
    service, owner, parsed_name, uuid, owner_name, owner_uuid, owner_email = None, None, None, None, None, None, None

    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")
    result = prog.match(service_name_or_uuid)
    owner_match = prog.match(service_owner)

    if result is None:
        parsed_name = service_name_or_uuid.replace("_", " ").strip()
    else:
        uuid = service_name_or_uuid

    if owner_match is None:
        if '@' not in service_owner:
            owner_name = service_owner.split("_")
        else:
            owner_email = service_owner

    else:
        owner_uuid = service_owner

    try:
        if result is None:
            service = service_models.Service.objects.get(name=parsed_name)
        else:
            service = service_models.Service.objects.get(id=uuid)

        if owner_match is None:
            if '@' not in service_owner:
                owner = service_models.ServiceOwner.objects.get(first_name=owner_name[0], last_name=owner_name[1])
            else:
                owner = service_models.ServiceOwner.objects.get(email=owner_email)

        else:
            owner = service_models.ServiceOwner.objects.get(id=owner_uuid)

    except models.ServiceOwner.DoesNotExist:
        owner = None
        response = helper.get_error_response(strings.OWNER_NOT_FOUND)

    except service_models.Service.DoesNotExist:
        service = None
        response = helper.get_error_response(strings.SERVICE_NOT_FOUND)

    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response = helper.get_error_response(strings.INVALID_UUID)

    if service is not None and owner is not None:
        response = helper.get_response_info(strings.SERVICE_OWNER_INSTITUTION, owner.get_institution())

    return JsonResponse(response)


# Inserts an Institution object
@api_view(['POST'])
def insert_institution(request):
    """
    Inserts an institution object

    """
    params = request.POST.copy()
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")

    if "name" not in params:
        return JsonResponse(helper.get_error_response(strings.INSTITUTION_NAME_NOT_PROVIDED,
                                                      status=strings.REJECTED_405))

    uuid = None

    name = params.get('name')

    if name is None or len(name) == 0:
        return JsonResponse(helper.get_error_response(strings.INSTITUTION_NAME_EMPTY, status=strings.REJECTED_405))

    address = params.get('address') if "address" in params else None
    country = params.get('country') if "country" in params else None
    department = params.get('department') if 'department' in params else None


    if "uuid" in params:

        uuid = params.get("uuid")
        result = prog.match(uuid)

        if result is None:
            return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                          status=strings.REJECTED_405))

        try:
            models.Institution.objects.get(id=uuid)
            return JsonResponse(helper.get_error_response(strings.INSTITUTION_UUID_EXISTS,
                                                          status=strings.CONFLICT_409))
        except models.Institution.DoesNotExist:
            pass


    institution = models.Institution()
    institution.name = name
    institution.address = address
    institution.country = country
    institution.department = department
    institution.save()

    if uuid is not None:
        institution.id = uuid

    institution.save()

    data = institution.as_json()

    response = helper.get_response_info(strings.INSTITUTION_INSERTED, data, status=strings.CREATED_201)

    return JsonResponse(response)


# Inserts an Contact Information object
@api_view(['POST'])
def insert_contact_information(request):
    """
    Inserts a contact information object

    """
    params = request.POST.copy()
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")

    if "name" not in params:
        return JsonResponse(helper.get_error_response(strings.INSTITUTION_NAME_NOT_PROVIDED,
                                                      status=strings.REJECTED_405))

    first_name = params.get('first_name')
    last_name = params.get('last_name')
    email = params.get('department')
    phone = params.get('phone')
    url = params.get('url')

    if first_name is None or len(first_name) == 0:
        return JsonResponse(helper.get_error_response(strings.OWNER_FIRST_NAME_EMPTY, status=strings.REJECTED_405))

    if last_name is None or len(last_name) == 0:
        return JsonResponse(helper.get_error_response(strings.OWNER_LAST_NAME_EMPTY, status=strings.REJECTED_405))

    if email is None or len(email) == 0:
        return JsonResponse(helper.get_error_response(strings.OWNER_EMAIL_EMPTY, status=strings.REJECTED_405))

    if phone is None or len(phone) == 0:
        return JsonResponse(helper.get_error_response(strings.OWNER_PHONE_EMPTY, status=strings.REJECTED_405))

    if url is None or len(url) == 0:
        return JsonResponse(helper.get_error_response(strings.OWNER_URL_EMPTY, status=strings.REJECTED_405))


    if "uuid" in params:

        uuid = params.get("uuid")
        result = prog.match(uuid)

        if result is None:
            return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                          status=strings.REJECTED_405))

        try:
            models.ContactInformation.objects.get(id=uuid)
            return JsonResponse(helper.get_error_response(strings.CONTACT_INFORMATION_UUID_EXISTS,
                                                          status=strings.CONFLICT_409))
        except models.Institution.DoesNotExist:
            pass


    contact_information = models.ContactInformation()
    contact_information.first_name = first_name
    contact_information.last_name = last_name
    contact_information.email = email
    contact_information.phone = phone
    contact_information.url = url

    if uuid is not None:
        contact_information.id = uuid

    contact_information.save()

    data = contact_information.as_json()

    response = helper.get_response_info(strings.CONTACT_INFORMATION_INSERTED, data, status=strings.CREATED_201)

    return JsonResponse(response)


# Inserts an Service Owner object
@api_view(['POST'])
def insert_service_owner(request):
    """
    Inserts an service owner object

    """
    params = request.POST.copy()
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")

    if "institution_uuid" not in params:
        return JsonResponse(helper.get_error_response(strings.INSTITUTION_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_405))

    institution_uuid = None
    uuid = None

    first_name = params.get('first_name')
    last_name = params.get('last_name')
    email = params.get('email')
    phone = params.get('phone')
    institution_uuid = params.get('institution_uuid')


    if first_name is None or len(first_name) == 0:
        return JsonResponse(helper.get_error_response(strings.OWNER_FIRST_NAME_EMPTY, status=strings.REJECTED_405))

    if last_name is None or len(last_name) == 0:
        return JsonResponse(helper.get_error_response(strings.OWNER_LAST_NAME_EMPTY, status=strings.REJECTED_405))

    if email is None or len(email) == 0:
        return JsonResponse(helper.get_error_response(strings.OWNER_EMAIL_EMPTY, status=strings.REJECTED_405))

    if phone is None or len(phone) == 0:
        return JsonResponse(helper.get_error_response(strings.OWNER_PHONE_EMPTY, status=strings.REJECTED_405))


    result = prog.match(institution_uuid)

    if result is None:
        return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                      status=strings.REJECTED_405))

    try:
        institution = models.Institution.objects.get(id=institution_uuid)

    except models.Institution.DoesNotExist:
        return JsonResponse(helper.get_error_response(strings.INSTITUTION_NOT_FOUND, status=strings.NOT_FOUND_404))


    if "uuid" in params:

        uuid = params.get("uuid")
        result = prog.match(uuid)

        if result is None:
            return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                          status=strings.REJECTED_405))

        try:
            models.ServiceOwner.objects.get(id=uuid)
            return JsonResponse(helper.get_error_response(strings.SERVICE_OWNER_UUID_EXISTS,
                                                          status=strings.CONFLICT_409))
        except models.Institution.DoesNotExist:
            pass


    service_owner = models.ServiceOwner()
    service_owner.first_name = first_name
    service_owner.last_name = last_name
    service_owner.email = email
    service_owner.phone = phone
    service_owner.id_service_owner = institution

    if uuid is not None:
        service_owner.id = uuid

    service_owner.save()

    data = service_owner.as_json()

    response = helper.get_response_info(strings.SERVICE_OWNER_INSERTED, data, status=strings.CREATED_201)

    return JsonResponse(response)