from django.http import JsonResponse
from service import models as service_models
from options import models as options_models
from models import  ServiceDetailsOption, ServiceDetails, Service
from rest_framework.decorators import *
from common import helper, strings
import re


# Returns the selected service details options information
@api_view(['GET'])
def get_service_sla(request, search_type, version, sla_uuid):
    """
    Retrieves the service sla

    """

    service, parsed_name, uuid = None, None, None

    response = {}
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")
    result = prog.match(search_type)
    result_comp = prog.match(sla_uuid)

    if result_comp is None:
        response = helper.get_error_response(strings.SLA_INVALID_UUID)
        return JsonResponse(response)


    if result is None:
        parsed_name = search_type.replace("_", " ").strip()
    else:
        uuid = search_type


    try:
        if result is None:
            service = service_models.Service.objects.get(name=parsed_name)
        else:
            service = service_models.Service.objects.get(id=uuid)


        service_details = service_models.ServiceDetails.objects.get(id_service=service.pk, version=version)

        sla = options_models.SLA.objects.get(id=sla_uuid)
        service_det_options = options_models.ServiceDetailsOption.objects.get(service_id=service.pk,
                                                                           service_details_id=service_details.pk,
                                                                           service_options_id=sla.service_option_id.pk)

        data = sla.as_json(service.name, version)
        response = helper.get_response_info(strings.SLA_INFORMATION, data)

    except service_models.Service.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_NOT_FOUND)

    except service_models.ServiceDetails.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_DETAILS_NOT_FOUND)

    except options_models.SLA.DoesNotExist:
        response = helper.get_error_response(strings.SLA_NOT_FOUND)

    except options_models.ServiceDetailsOption.DoesNotExist:
        response = helper.get_error_response(strings.SLA_SERVICE_DETAILS_MISMATCH)

    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response = helper.get_error_response(strings.INVALID_UUID)

    return JsonResponse(response)


# Returns the selected service details options information
@api_view(['GET'])
def get_service_sla_parameter(request, search_type, version, sla_uuid, sla_param_uuid):
    """
    Retrieves the service sla parameter

    """
    """
    Inserts a service option object

    """
    service, parsed_name, uuid = None, None, None

    response = {}
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")
    result = prog.match(search_type)
    result_comp = prog.match(sla_uuid)

    if result_comp is None:
        response = helper.get_error_response(strings.SLA_INVALID_UUID)
        return JsonResponse(response)

    result_comp = prog.match(sla_param_uuid)
    if result_comp is None:
        response = helper.get_error_response(strings.SLA_PARAMETER_INVALID_UUID)
        return JsonResponse(response)

    if result is None:
        parsed_name = search_type.replace("_", " ").strip()
    else:
        uuid = search_type

    try:
        if result is None:
            service = service_models.Service.objects.get(name=parsed_name)
        else:
            service = service_models.Service.objects.get(id=uuid)


        service_details = service_models.ServiceDetails.objects.get(id_service=service.pk, version=version)

        sla = options_models.SLA.objects.get(id=sla_uuid)

        service_det_options = options_models.ServiceDetailsOption.objects.get(service_id=service.pk,
                                                                           service_details_id=service_details.pk,
                                                                           service_options_id=sla.service_option_id.pk)

        sla_param = options_models.SLAParameter.objects.get(sla_id=sla.pk,
                                                            service_option_id=service_det_options.service_options_id,
                                                            parameter_id=sla_param_uuid)
        parameter = options_models.Parameter.objects.get(id=sla_param_uuid)

        data = parameter.as_json(service.name, version, sla_uuid)
        response = helper.get_response_info(strings.SLA_PARAMETER_INFORMATION, data)

    except service_models.Service.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_NOT_FOUND)

    except service_models.ServiceDetails.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_DETAILS_NOT_FOUND)

    except options_models.SLA.DoesNotExist:
        response = helper.get_error_response(strings.SLA_NOT_FOUND)

    except options_models.SLAParameter.DoesNotExist:
        response = helper.get_error_response(strings.SLA_PARAMETER_NOT_FOUND)

    except options_models.ServiceDetailsOption.DoesNotExist:
        response = helper.get_error_response(strings.SLA_SERVICE_DETAILS_MISMATCH)

    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response = helper.get_error_response(strings.INVALID_UUID)


    return JsonResponse(response)


# Returns the selected service details options information
@api_view(['GET'])
def get_service_options(request, search_type, version):
    """
    Retrieves the service options

    """

    service, parsed_name, uuid = None, None, None

    response = {}
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")
    result = prog.match(search_type)

    if result is None:
        parsed_name = search_type.replace("_", " ").strip()
    else:
        uuid = search_type

    try:
        if result is None:
            service = service_models.Service.objects.get(name=parsed_name)
        else:
            service = service_models.Service.objects.get(id=uuid)

        detail = service.get_service_details_by_version(version=str(version))
        options = ServiceDetailsOption.objects.filter(service_details_id=detail.id, service_id=detail.id_service.pk)

        data = helper.build_list_object("service_options", [ option.as_json() for option in options ])
        response = helper.get_response_info(strings.SERVICE_OPTIONS, data)

    except ServiceDetails.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_DETAILS_NOT_FOUND)

    except ServiceDetailsOption.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_DETAILS_OPTIONS_NOT_FOUND)

    except Service.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_NOT_FOUND)

    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response = helper.get_error_response(strings.INVALID_UUID)

    return JsonResponse(response)


# Updates a Service Option object
@api_view(['POST'])
def edit_service_option(request):
    """

    :param request:
    :return:
    """

    insert_service_option(request)

# Inserts a Service Option object
@api_view(['POST'])
def insert_service_option(request):
    """
    Inserts a service option object

    """

    op_type = helper.get_last_url_part(request)
    uuid, name, service_option = None, None, None
    params = request.POST.copy()
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")

    if "name" not in params and op_type == "add":
        return JsonResponse(helper.get_error_response(strings.SERVICE_OPTION_NAME_NOT_PROVIDED,
                                                      status=strings.REJECTED_405))
    elif "name" in params:
        name = params.get('name')
        if name is None or len(name) == 0:
            return JsonResponse(helper.get_error_response(strings.SERVICE_OPTION_NAME_EMPTY,
                                                          status=strings.REJECTED_405))
    elif op_type == "edit":
        name = None

    if "uuid" in params:

        uuid = params.get("uuid")
        result = prog.match(uuid)

        if result is None:
            return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                          status=strings.REJECTED_405))

        try:
            service_option = options_models.ServiceOption.objects.get(id=uuid)
            if op_type == "add":
                return JsonResponse(helper.get_error_response(strings.SERVICE_OPTION_UUID_EXISTS,
                                                              status=strings.CONFLICT_409))
        except options_models.ServiceOption.DoesNotExist:
            service_option = options_models.ServiceOption()
            if op_type == "edit":
                return JsonResponse(helper.get_error_response(strings.SERVICE_OPTION_NOT_FOUND,
                                                              status=strings.NOT_FOUND_404))
    elif op_type == "edit":
        return JsonResponse(helper.get_error_response(strings.SERVICE_OPTION_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_405))
    elif op_type == "add":
        service_option = options_models.ServiceOption()

    if name is not None:
        service_option.name = name
    if "description" in params:
        service_option.description = params.get('description')
    if "pricing" in params:
        service_option.pricing = params.get('pricing')

    if uuid is not None:
        service_option.id = uuid

    service_option.save()
    data = service_option.as_json()
    msg = strings.SERVICE_OPTION_INSERTED if op_type == "add" else strings.SERVICE_OPTION_UPDATED
    status = strings.CREATED_201 if op_type == "add" else strings.UPDATED_202
    response = helper.get_response_info(msg, data, status=status)

    return JsonResponse(response)


# Updates a SLA object
@api_view(['POST'])
def edit_SLA(request):
    """

    :param request:
    :return:
    """

    insert_SLA(request)

# Inserts an SLA object
@api_view(['POST'])
def insert_SLA(request):
    """
    Inserts a SLA object

    """

    op_type = helper.get_last_url_part(request)
    uuid, name, SLA = None, None, None
    params = request.POST.copy()
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")

    if "name" not in params and op_type == "add":
        return JsonResponse(helper.get_error_response(strings.SLA_NAME_NOT_PROVIDED,
                                                      status=strings.REJECTED_405))
    elif "name" in params:
        name = params.get('name')
        if name is None or len(name) == 0:
            return JsonResponse(helper.get_error_response(strings.SLA_NAME_EMPTY, status=strings.REJECTED_405))
    elif op_type == "edit":
        name = None

    if "service_option_uuid" not in params:
        return JsonResponse(helper.get_error_response(strings.SERVICE_OPTION_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_405))
    service_option_uuid = params.get('service_option_uuid')

    if service_option_uuid is None or len(service_option_uuid) == 0:
        return JsonResponse(helper.get_error_response(strings.SERVICE_OPTION_UUID_EMPTY, status=strings.REJECTED_405))


    result = prog.match(service_option_uuid)

    if result is None:
        return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                      status=strings.REJECTED_405))

    try:
        service_option = options_models.ServiceOption.objects.get(id=service_option_uuid)
    except options_models.ServiceOption.DoesNotExist:
        return JsonResponse(helper.get_error_response(strings.SERVICE_OPTION_NOT_FOUND,
                                                      status=strings.NOT_FOUND_404))

    if "uuid" in params:

        uuid = params.get("uuid")
        result = prog.match(uuid)

        if result is None:
            return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                          status=strings.REJECTED_405))

        try:
            SLA = options_models.SLA.objects.get(id=uuid)
            if op_type == "add":
                return JsonResponse(helper.get_error_response(strings.SLA_UUID_EXISTS,
                                                              status=strings.CONFLICT_409))
        except options_models.SLA.DoesNotExist:
            SLA = options_models.SLA()
            if op_type == "edit":
                return JsonResponse(helper.get_error_response(strings.SLA_NOT_FOUND, status=strings.NOT_FOUND_404))
    elif op_type == "edit":
        return JsonResponse(helper.get_error_response(strings.SLA_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_405))
    elif op_type == "add":
        SLA = options_models.SLA()

    if name is not None:
        SLA.name = name
    SLA.service_option_id = service_option

    if uuid is not None:
        SLA.id = uuid

    SLA.save()
    data = SLA.as_json()
    msg = strings.SLA_INSERTED if op_type == "add" else strings.SLA_UPDATED
    status = strings.CREATED_201 if op_type == "add" else strings.UPDATED_202
    response = helper.get_response_info(msg, data, status=status)

    return JsonResponse(response)


# Updates a Parameter object
@api_view(['POST'])
def edit_parameter(request):
    """

    :param request:
    :return:
    """

    insert_parameter(request)

# Inserts a Parameter object
@api_view(['POST'])
def insert_parameter(request):
    """
    Inserts a paramater object

    """

    op_type = helper.get_last_url_part(request)
    uuid, name, type, parameter = None, None, None, None
    params = request.POST.copy()
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")

    if "name" not in params and op_type == "add":
        return JsonResponse(helper.get_error_response(strings.PARAMETER_NAME_NOT_PROVIDED,
                                                      status=strings.REJECTED_405))
    elif "name" in params:
        name = params.get('name')
        if name is None or len(name) == 0:
            return JsonResponse(helper.get_error_response(strings.PARAMETER_NAME_EMPTY, status=strings.REJECTED_405))
    elif op_type == "edit":
        name = None

    if "type" not in params and op_type == "add":
        return JsonResponse(helper.get_error_response(strings.PARAMETER_TYPE_NOT_PROVIDED,
                                                      status=strings.REJECTED_405))
    elif "type" in params:
        type = params.get('type')
        if type is None or len(type) == 0:
            return JsonResponse(helper.get_error_response(strings.PARAMETER_TYPE_EMPTY, status=strings.REJECTED_405))
    elif op_type == "edit":
        type = None

    if "uuid" in params:

        uuid = params.get("uuid")
        result = prog.match(uuid)

        if result is None:
            return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                          status=strings.REJECTED_405))

        try:
            parameter = options_models.Parameter.objects.get(id=uuid)
            if op_type == "add":
                return JsonResponse(helper.get_error_response(strings.PARAMETER_UUID_EXISTS,
                                                              status=strings.CONFLICT_409))
        except options_models.Parameter.DoesNotExist:
            parameter = options_models.Parameter()
            if op_type == "edit":
                return JsonResponse(helper.get_error_response(strings.PARAMETER_NOT_FOUND,
                                                              status=strings.NOT_FOUND_404))
    elif op_type == "edit":
        return JsonResponse(helper.get_error_response(strings.PARAMETER_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_405))
    elif op_type == "add":
        parameter = options_models.Parameter()

    if name is not None:
        parameter.name = name
    if type is not None:
        parameter.type = type
    if "expression" in params:
        parameter.expression = parameter.get('expression')

    if uuid is not None:
        parameter.id = uuid

    parameter.save()
    data = parameter.as_json()
    msg = strings.PARAMETER_INSERTED if op_type == "add" else strings.PARAMETER_UPDATED
    status = strings.CREATED_201 if op_type == "add" else strings.UPDATED_202
    response = helper.get_response_info(msg, data, status=status)

    return JsonResponse(response)


# Updates a SLA parameter object
@api_view(['POST'])
def edit_SLA_parameter(request):
    """

    :param request:
    :return:
    """

    insert_SLA_parameter(request)

# Inserts an SLA parameter object
@api_view(['POST'])
def insert_SLA_parameter(request):
    """
    Inserts a SLA parameter object

    """

    op_type = helper.get_last_url_part(request)
    params = request.POST.copy()
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")
    uuid, sla_parameter = None, None

    if "parameter_uuid" not in params:
        return JsonResponse(helper.get_error_response(strings.PARAMETER_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_405))

    if "sla_uuid" not in params:
        return JsonResponse(helper.get_error_response(strings.SLA_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_405))

    if "service_option_uuid" not in params:
        return JsonResponse(helper.get_error_response(strings.SERVICE_OPTION_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_405))

    parameter_uuid = params.get('parameter_uuid')
    sla_uuid = params.get('sla_uuid')
    service_option_uuid = params.get('service_option_uuid')

    if parameter_uuid is None or len(parameter_uuid) == 0:
        return JsonResponse(helper.get_error_response(strings.PARAMETER_UUID_EMPTY, status=strings.REJECTED_405))


    if service_option_uuid is None or len(service_option_uuid) == 0:
        return JsonResponse(helper.get_error_response(strings.SERVICE_OPTION_UUID_EMPTY, status=strings.REJECTED_405))


    if sla_uuid is None or len(parameter_uuid) == 0:
        return JsonResponse(helper.get_error_response(strings.SLA_UUID_EMPTY, status=strings.REJECTED_405))


    result = prog.match(parameter_uuid)

    if result is None:
        return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                      status=strings.REJECTED_405))

    result = prog.match(service_option_uuid)

    if result is None:
        return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                      status=strings.REJECTED_405))

    result = prog.match(sla_uuid)

    if result is None:
        return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                      status=strings.REJECTED_405))

    try:
        service_option = options_models.ServiceOption.objects.get(id=service_option_uuid)
        sla = options_models.SLA.objects.get(id=sla_uuid)
        parameter = options_models.Parameter.objects.get(id=parameter_uuid)
    except options_models.ServiceOption.DoesNotExist:
        return JsonResponse(helper.get_error_response(strings.SERVICE_OPTION_NOT_FOUND,
                                                      status=strings.NOT_FOUND_404))
    except options_models.SLA.DoesNotExist:
        return JsonResponse(helper.get_error_response(strings.SLA_NOT_FOUND,
                                                      status=strings.NOT_FOUND_404))
    except options_models.Parameter.DoesNotExist:
        return JsonResponse(helper.get_error_response(strings.PARAMETER_NOT_FOUND,
                                                      status=strings.NOT_FOUND_404))

    obj, created = options_models.SLAParameter.objects.get_or_create(parameter_id=parameter,
                                                                          sla_id=sla,
                                                                     service_option_id=service_option)

    if not created and op_type == "add":
        return JsonResponse(helper.get_error_response(strings.SLA_PARAMETER_EXISTS, status=strings.CONFLICT_409))
    elif created and op_type == "edit":
        return JsonResponse(helper.get_error_response(strings.SLA_PARAMETER_NOT_FOUND, status=strings.NOT_FOUND_404))

    if "uuid" in params:

        uuid = params.get("uuid")
        result = prog.match(uuid)

        if result is None:
            return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                          status=strings.REJECTED_405))

        try:
            sla_parameter = options_models.SLAParameter.objects.get(id=uuid)
            if op_type == "add":
                return JsonResponse(helper.get_error_response(strings.SLA_PARAMETER_UUID_EXISTS,
                                                              status=strings.CONFLICT_409))
        except options_models.SLAParameter.DoesNotExist:
            sla_parameter = options_models.SLAParameter()
            if op_type == "edit":
                return JsonResponse(helper.get_error_response(strings.SLA_PARAMETER_NOT_FOUND,
                                                              status=strings.NOT_FOUND_404))
    elif op_type == "edit":
        return JsonResponse(helper.get_error_response(strings.SLA_PARAMETER_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_405))
    elif op_type == "add":
        sla_parameter = options_models.SLAParameter()

    sla_parameter.parameter_id = parameter
    sla_parameter.service_option_id = service_option
    sla_parameter.sla_id = sla

    if uuid is not None:
        sla_parameter.id = uuid

    sla_parameter.save()
    data = sla_parameter.as_json()
    msg = strings.SLA_PARAMETER_INSERTED if op_type == "add" else strings.SLA_PARAMETER_UPDATED
    status = strings.CREATED_201 if op_type == "add" else strings.UPDATED_202
    response = helper.get_response_info(msg, data, status=status)

    return JsonResponse(response)

def edit_service_details_option(request):
    """

    :param request:
    :return:
    """

    params = request.POST.copy()
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")

    if "service_uuid" not in params:
        return JsonResponse(helper.get_error_response(strings.SERVICE_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_405))

    if "service_details_uuid" not in params:
        return JsonResponse(helper.get_error_response(strings.SERVICE_DETAILS_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_405))

    if "service_options_uuid" not in params:
        return JsonResponse(helper.get_error_response(strings.SERVICE_OPTION_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_405))

    if "new_service_uuid" not in params:
        return JsonResponse(helper.get_error_response(strings.NEW_SERVICE_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_405))

    if "new_service_details_uuid" not in params:
        return JsonResponse(helper.get_error_response(strings.NEW_SERVICE_DETAILS_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_405))

    if "new_service_options_uuid" not in params:
        return JsonResponse(helper.get_error_response(strings.NEW_SERVICE_OPTION_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_405))

    service_id = params.get('service_uuid')
    service_details_id = params.get('service_details_uuid')
    service_options_id = params.get('service_options_uuid')

    new_service_id = params.get('new_service_uuid')
    new_service_details_id = params.get('new_service_details_uuid')
    new_service_options_id = params.get('new_service_options_uuid')


    result = prog.match(service_id)

    if result is None:
        return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                      status=strings.REJECTED_405))

    result = prog.match(service_details_id)

    if result is None:
        return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                      status=strings.REJECTED_405))

    result = prog.match(service_options_id)

    if result is None:
        return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                      status=strings.REJECTED_405))

    result = prog.match(new_service_id)

    if result is None:
        return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                      status=strings.REJECTED_405))

    result = prog.match(new_service_details_id)

    if result is None:
        return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                      status=strings.REJECTED_405))

    result = prog.match(new_service_options_id)

    if result is None:
        return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                      status=strings.REJECTED_405))

    try:
        service = service_models.Service.objects.get(id=service_id)
        service_details = service_models.ServiceDetails.objects.get(id=service_details_id)
        service_option = options_models.ServiceOption.objects.get(id=service_options_id)

        new_service = service_models.Service.objects.get(id=new_service_id)
        new_service_details = service_models.ServiceDetails.objects.get(id=new_service_details_id)
        new_service_option = options_models.ServiceOption.objects.get(id=new_service_options_id)

    except options_models.ServiceOption.DoesNotExist:
        return JsonResponse(helper.get_error_response(strings.SERVICE_OPTION_NOT_FOUND,
                                                      status=strings.NOT_FOUND_404))
    except service_models.Service.DoesNotExist:
        return JsonResponse(helper.get_error_response(strings.SERVICE_NOT_FOUND,
                                                      status=strings.NOT_FOUND_404))
    except service_models.ServiceDetails.DoesNotExist:
        return JsonResponse(helper.get_error_response(strings.SERVICE_DETAILS_NOT_FOUND,
                                                      status=strings.NOT_FOUND_404))

    try:
        service_details_option = options_models.ServiceDetailsOption.objects.get(service_id=service,
                                                                                 service_details_id=service_details,
                                                                                 service_options_id=service_option)

        service_details_option.service_id = new_service
        service_details_option.service_details_id = new_service_details
        service_details_option.service_options_id = new_service_option
        service_details_option.save()
    except options_models.ServiceDetailsOption.DoesNotExist:
            return JsonResponse(helper.get_error_response(strings.SERVICE_OPTION_NOT_FOUND,
                                                          status=strings.NOT_FOUND_404))

    data = service_details_option.as_json()
    msg = strings.SERVICE_DETAILS_OPTION_UPDATED
    status = strings.UPDATED_202
    response = helper.get_response_info(msg, data, status=status)

    return JsonResponse(response)

# Inserts an service details option object
@api_view(['POST'])
def insert_service_details_option(request):
    """
    Inserts a service details object

    """

    params = request.POST.copy()
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")


    uuid, service_details_option = None, None


    if "service_uuid" not in params:
        return JsonResponse(helper.get_error_response(strings.SERVICE_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_405))

    if "service_details_uuid" not in params:
        return JsonResponse(helper.get_error_response(strings.SERVICE_DETAILS_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_405))

    if "service_options_uuid" not in params:
        return JsonResponse(helper.get_error_response(strings.SERVICE_OPTION_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_405))

    service_id = params.get('service_uuid')
    service_details_id = params.get('service_details_uuid')
    service_options_id = params.get('service_options_uuid')

    if service_id is None or len(service_id) == 0:
        return JsonResponse(helper.get_error_response(strings.SERVICE_UUID_EMPTY, status=strings.REJECTED_405))


    if service_details_id is None or len(service_details_id) == 0:
        return JsonResponse(helper.get_error_response(strings.SERVICE_DETAILS_UUID_EMPTY, status=strings.REJECTED_405))


    if service_options_id is None or len(service_options_id) == 0:
        return JsonResponse(helper.get_error_response(strings.SERVICE_OPTION_UUID_EMPTY, status=strings.REJECTED_405))


    result = prog.match(service_id)

    if result is None:
        return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                      status=strings.REJECTED_405))

    result = prog.match(service_details_id)

    if result is None:
        return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                      status=strings.REJECTED_405))

    result = prog.match(service_options_id)

    if result is None:
        return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                      status=strings.REJECTED_405))

    try:
        service = service_models.Service.objects.get(id=service_id)
        service_details = service_models.ServiceDetails.objects.get(id=service_details_id)
        service_option = options_models.ServiceOption.objects.get(id=service_options_id)

    except options_models.ServiceOption.DoesNotExist:
        return JsonResponse(helper.get_error_response(strings.SERVICE_OPTION_NOT_FOUND,
                                                      status=strings.NOT_FOUND_404))
    except service_models.Service.DoesNotExist:
        return JsonResponse(helper.get_error_response(strings.SERVICE_NOT_FOUND,
                                                      status=strings.NOT_FOUND_404))
    except service_models.ServiceDetails.DoesNotExist:
        return JsonResponse(helper.get_error_response(strings.SERVICE_DETAILS_NOT_FOUND,
                                                      status=strings.NOT_FOUND_404))

    service_details_option, created = options_models.ServiceDetailsOption.objects.get_or_create(service_id=service,
                                                                          service_details_id=service_details,
                                                                     service_options_id=service_option)
    if not created:
        return JsonResponse(helper.get_error_response(strings.SERVICE_OPTION_EXISTS, status=strings.CONFLICT_409))

    data = service_details_option.as_json()
    msg = strings.SERVICE_DETAILS_OPTION_INSERTED
    status = strings.CREATED_201
    response = helper.get_response_info(msg, data, status=status)

    return JsonResponse(response)

