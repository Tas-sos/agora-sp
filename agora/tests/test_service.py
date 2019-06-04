from agora.testing import *
import json
from service.models import Service


def test_name_trim(superadmin):
    """
    Test that Service 'name' field is trimmed before the model is saved.
    """
    url = RESOURCES_CRUD['services']['url']
    data = {
        "internal": False,
        "customer_facing": True,
    }

    data.update(name='ice hockey')
    superadmin.post(url, data)
    assert superadmin.get(url).json()[0]['name'] == 'ice hockey'

    data.update(name='table tennis ')
    superadmin.post(url, data)
    assert superadmin.get(url).json()[1]['name'] == 'table tennis'

    data.update({'name': ' ski'})
    superadmin.post(url, data)
    assert superadmin.get(url).json()[2]['name'] == 'ski'


def test_related_services_fieldset(superadmin):
    """
    Test that Service related_services fields work as intended.
    """
    url = RESOURCES_CRUD['services']['url']
    data = {
        'internal': False,
        'customer_facing': True,
        'name': 'hockey',
        'other_required_services': 'what',
        'other_related_services': 'what2',
        'related_platform': '?!',
    }
    superadmin.post(url, data)
    assert superadmin.get(url).json()[0]['name'] == 'hockey'
    hockey_service = superadmin.get(url).json()[0]
    hockey_service_obj = Service.objects.get(name=hockey_service['name'])
    assert hockey_service['other_required_services'] == 'what'
    assert hockey_service['other_related_services'] == 'what2'
    assert hockey_service['related_platform'] == '?!'

    data.update(name='tennis', required_services=[hockey_service['id']])
    superadmin.post(url, json.dumps(data), content_type='application/json')
    assert superadmin.get(url).json()[1]['name'] == 'tennis'
    tennis_service = superadmin.get(url).json()[1]
    tennis_service_obj = Service.objects.get(name=tennis_service['name'])
    assert len(tennis_service['required_services']) == 1
    assert tennis_service_obj.required_services.first() == hockey_service_obj

    data.update({
        'name': 'ski',
        'related_services': [hockey_service['id'], tennis_service['id']],
        'required_services': [hockey_service['id']],
        })
    superadmin.post(url, json.dumps(data), content_type='application/json')
    assert superadmin.get(url).json()[2]['name'] == 'ski'
    ski_service = superadmin.get(url).json()[2]
    ski_service_obj = Service.objects.get(name=ski_service['name'])
    assert len(ski_service['related_services']) == 2
    assert len(ski_service['required_services']) == 1
    assert ski_service_obj.related_services.get(name='tennis') \
                           == tennis_service_obj

    data.clear()
    data.update(required_services=[hockey_service['id'], ski_service['id']])
    resp = superadmin.patch(url + ski_service['id'] + '/', json.dumps(data),
                            content_type='application/json')
    assert resp.status_code == 200
    ski_service = superadmin.get(url).json()[2]
    ski_service_obj = Service.objects.get(name=ski_service['name'])
    assert len(ski_service['required_services']) == 2
    assert ski_service_obj.required_services.get(name='ski') \
                           == ski_service_obj
