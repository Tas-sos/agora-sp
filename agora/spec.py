import copy
  # djoser_verifier: agora.utils.djoser_verifier
  # userid_extractor: agora.utils.userid_extractor

SERVICE_FIELDS_COMMON = {
    'id': {
        '.field.uuid': {},
        '.flag.nowrite': {}},
    'name': {
        '.field.string': {},
        '.flag.filterable': {},
        '.flag.searchable': {},
        '.flag.orderable': {}},
    'short_description': {
        '.field.string': {},
        '.flag.searchable': {},
        '.flag.nullable.default': {}},
    'description_external': {
        '.field.string': {},
        '.flag.nullable.default': {}},
    'description_internal': {
        '.field.string': {},
        '.flag.nullable.default': {}},
    'service_type': {
        '.field.string': {},
        '.flag.orderable': {},
        '.flag.nullable.default': {},
        '.flag.filterable': {}},
    'request_procedures': {
        '.field.string': {},
        '.flag.nullable.default': {}},
    'funders_for_service': {
        '.field.string': {},
        '.flag.nullable.default': {}},
    'value_to_customer': {
        '.field.string': {},
        '.flag.nullable.default': {}},
    'risks': {
        '.field.string': {},
        '.flag.nullable.default': {}},
    'competitors': {
        '.field.string': {},
        '.flag.nullable.default': {}},
    'customer_facing': {
        '.flag.filterable': {},
        '.field.boolean': {}},
    'internal': {
        '.flag.filterable': {},
        '.field.boolean': {}},
    'service_area_ext': {
        '.field.string': {},
        '.flag.nowrite': {},
        '.flag.orderable': {},
        'source': 'service_area.name'},
    'service_trl_ext': {
        '.field.string': {},
        '.flag.nowrite': {},
        '.flag.orderable': {},
        'source': 'service_trl.value'},
}


SERVICE_FIELDS_INT = {
    'service_area': {
        '.field.ref': {},
        'source': 'service_area_id',
        'to': '/api/v2/service-areas',
        '.flag.nullable.default': {},
        '.flag.orderable': {},
        '.flag.filterable': {}},
    'service_trl': {
        '.field.ref': {},
        'source': 'service_trl_id',
        'to': '/api/v2/service-trls',
        '.flag.orderable': {},
        '.flag.filterable': {},
        '.flag.nullable.default': {}},
    'id_service_owner': {
        '.field.ref': {},
        'source': 'id_service_owner_id',
        'to': '/api/v2/service-owners',
        '.flag.nullable.default': {}},
    'contact_information_external': {
        '.field.struct': {},
        'source': 'id_contact_information',
        '.flag.nullable.default': {},
        'fields': {
            'id': {
                '.field.uuid': {},
                '.flag.nowrite': {}},
            'first_name': {
                '.field.string': {},
                '.flag.nullable.default': {}},
            'last_name': {
                '.field.string': {},
                '.flag.nullable.default': {}},
            'email': {
                '.field.string': {},
                '.flag.nullable.default': {}},
            'phone': {
                '.field.string': {},
                '.flag.nullable.default': {}},
            'full_name': {
                '.field.string': {},
                '.flag.nowrite': {},
                '.flag.nullable.default': {}},
            'url': {
                '.field.string': {},
                '.flag.nullable.default': {}},
        }
    },
    'contact_information_internal': {
        '.field.struct': {},
        'source': 'id_contact_information_internal',
        '.flag.nullable.default': {},
        'fields': {
            'id': {
                '.field.uuid': {},
                '.flag.nowrite': {}},
            'first_name': {
                '.field.string': {},
                '.flag.nullable.default': {}},
            'last_name': {
                '.field.string': {},
                '.flag.nullable.default': {}},
            'email': {
                '.field.string': {},
                '.flag.nullable.default': {}},
            'phone': {
                '.field.string': {},
                '.flag.nullable.default': {}},
            'full_name': {
                '.field.string': {},
                '.flag.nowrite': {},
                '.flag.nullable.default': {}},
            'url': {
                '.field.string': {},
                '.flag.nullable.default': {}},
        }
    },
    'id_contact_information': {
        '.field.ref': {},
        '.flag.nowrite': {},
        'source': 'id_contact_information_id',
        'to': '/api/v2/contact-information',
        '.flag.nullable.default': {}},
    'id_contact_information_internal': {
        '.field.ref': {},
        '.flag.nowrite': {},
        'source': 'id_contact_information_internal_id',
        'to': '/api/v2/contact-information',
        '.flag.nullable.default': {}},
    'logo': {
        '.field.file': {},
        'default': ''},
    'service_admins_ids': {
        '.field.string': {},
        '.flag.nowrite': {}},
    'pending_service_admins_ids': {
        '.field.string': {},
        '.flag.nowrite': {}},
    'rejected_service_admins_ids': {
        '.field.string': {},
        '.flag.nowrite': {}},
}

SERVICE_FIELDS_EXT = {
    # extended keys
    'service_owner_ext': {
        '.field.string': {},
        '.flag.nowrite': {},
        'source': 'id_service_owner.full_name'},
    'contact_information_ext': {
        '.field.string': {},
        '.flag.nowrite': {},
        'source': 'id_contact_information.full_name'},
    'contact_information_internal_ext': {
        '.field.string': {},
        '.flag.nowrite': {},
        'source': 'id_contact_information_internal.full_name'},
    'user_customers_ext': {
        '.field.string': {},
        '.flag.nowrite': {},
        'source': 'user_customers_names'},
    'logo': {
        '.field.string': {},
        '.flag.nowrite': {},
        'source': 'logo_absolute_path'},
}

SERVICE_FIELDS_INTERNAL = dict(SERVICE_FIELDS_COMMON, **SERVICE_FIELDS_INT)
SERVICE_FIELDS_EXTERNAL = dict(SERVICE_FIELDS_COMMON, **SERVICE_FIELDS_EXT)

USERS = {
    '.collection.django': {},
    'model': 'accounts.models.User',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'username': {
            '.flag.orderable': {},
            '.field.string': {}},
        'email': {
            '.flag.orderable': {},
            '.field.string': {}},
        'first_name': {
            '.field.string': {}},
        'last_name': {
            '.field.string': {}},
        'is_staff': {
            '.field.boolean': {}},
        'is_active': {
            '.flag.orderable': {},
            '.field.boolean': {}},
        'date_joined': {
            '.field.string': {}},
        'avatar': {
            '.field.file': {},
            'default': ''},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
    }
}

USER_CUSTOMERS = {
    '.collection.django': {},
    'model': 'service.models.UserCustomer',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.ref': {},
            'source': 'name_id',
            'to': 'api/v2/user-roles'},
        'role': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'service_id': {
            '.field.ref': {},
            'source': 'service_id_id',
            '.flag.filterable': {},
            'to': 'api/v2/services'},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
    }
}

SERVICE_DEPENDSON_SERVICES = {
    '.collection.django': {},
    'model': 'service.models.Service_DependsOn_Service',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'id_service_one': {
            '.field.ref': {},
            'source': 'id_service_one_id',
            'to': '/api/v2/service'},
        'id_service_two': {
            '.field.ref': {},
            'source': 'id_service_two_id',
            'to': '/api/v2/service'},
    }
}

SERVICE_EXTERNAL_SERVICES = {
    '.collection.django': {},
    'model': 'service.models.Service_ExternalService',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'id_service': {
            '.field.ref': {},
            'source': 'id_service_id',
            'to': '/api/v2/service'},
        'id_external_service': {
            '.field.ref': {},
            'source': 'id_external_service_id',
            'to': '/api/v2/external_service'},
    }
}

SERVICE_STATUS = {
    '.collection.django': {},
    'model': 'service.models.ServiceStatus',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'value': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.filterable': {}},
        'order': {
            '.field.integer': {}},
        },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        },
}

SERVICE_TRLS = {
    '.collection.django': {},
    'model': 'service.models.ServiceTrl',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'value': {
            '.field.string': {},
            '.flag.filterable': {},
            '.flag.orderable': {}},
        'order': {
            '.field.integer': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
    },
}

EXTERNAL_SERVICES = {
    '.collection.django': {},
    'model': 'service.models.ExternalService',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {}},
        'description': {
            '.field.string': {}},
        'service': {
            '.field.string': {}},
        'details': {
            '.field.string': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
    },
}

USER_ROLES = {
    '.collection.django': {},
    'model': 'service.models.UserRole',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.flag.orderable': {},
            '.field.string': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
    },
}

SERVICE_AREAS = {
    '.collection.django': {},
    'model': 'service.models.ServiceArea',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.filterable': {},
            '.flag.orderable': {}},
        'icon': {
            '.field.file': {},
            'default': ''},
        'icon_absolute_path': {
            '.field.string': {},
            '.flag.nowrite': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

SERVICE_OWNERS = {
    '.collection.django': {},
    'model': 'owner.models.ServiceOwner',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'first_name': {
            '.field.string': {}},
        'last_name': {
            '.field.string': {}},
        'email': {
            '.field.email': {}},
        'phone': {
            '.field.string': {}},
        'id_service_owner': {
            '.field.ref': {},
            'source': 'id_service_owner_id',
            'to': '/api/v2/institutions'},
        'id_account': {
            '.field.ref': {},
            'source': 'id_account_id',
            'to': '/api/v2/custom-users'},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
    },
}

CUSTOM_USERS = {
    '.collection.django': {},
    'model': 'accounts.models.User',
    ':permissions_namespace': 'agora.checks.User',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'username': {
            '.flag.orderable': {},
            '.flag.searchable': {},
            '.field.string': {}},
        'email': {
            '.flag.orderable': {},
            '.flag.searchable': {},
            '.field.string': {}},
        'first_name': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
        'last_name': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
        'is_staff': {
            '.field.boolean': {},
            '.flag.nullable.default': {}},
        'is_active': {
            '.flag.orderable': {},
            '.field.boolean': {}},
        'date_joined': {
            '.flag.nowrite': {},
            '.field.datetime': {}},
        'avatar': {
            '.field.file': {},
            'default': ''},
        'shibboleth_id': {
            '.field.string': {},
            '.flag.nowrite': {},
            '.flag.nullable.default': {}},
        'role': {
            '.flag.orderable': {},
            '.flag.filterable': {},
            '.field.string': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
    },
}

CONTACT_INFORMATION = {
    '.collection.django': {},
    'model': 'owner.models.ContactInformation',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'first_name': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'last_name': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'email': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.nullable.default': {}},
        'phone': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'full_name': {
            '.field.string': {},
            '.flag.nowrite': {},
            '.flag.nullable.default': {}},
        'url': {
            '.field.string': {},
            '.flag.nullable.default': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
    },
}

INSTITUTIONS = {
    '.collection.django': {},
    'model': 'owner.models.Institution',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.nullable.default': {}},
        'address': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'country': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.nullable.default': {}},
        'department': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.nullable.default': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
    },
}

SERVICE_OWNERS = {
    '.collection.django': {},
    'model': 'owner.models.ServiceOwner',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'first_name': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'last_name': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'email': {
            '.field.email': {},
            '.flag.nullable.default': {}},
        'phone': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'id_service_owner': {
            '.field.ref': {},
            'source': 'id_service_owner_id',
            'to': '/api/v2/institutions'},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
    }
}

COMPONENTS = {
    '.collection.django': {},
    'model': 'component.models.ServiceComponent',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.nullable.default': {}},
        'description': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'logo': {
            '.field.file': {},
            'default': ''},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
    },
}

COMPONENT_IMPLEMENTATIONS = {
    '.collection.django': {},
    'model': 'component.models.ServiceComponentImplementation',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'component_id': {
            '.field.ref': {},
            'source': 'component_id_id',
            'to': '/api/v2/components',
            '.flag.filterable': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
        'description': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
    },
}

COMPONENT_IMPLEMENTATION_DETAILS = {
    '.collection.django': {},
    'model': 'component.models.ServiceComponentImplementationDetail',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'component_id': {
            '.flag.filterable': {},
            '.field.ref': {},
            'source': 'component_id_id',
            'to': '/api/v2/components'},
        'component_implementation_id': {
            '.flag.filterable': {},
            '.field.ref': {},
            'source': 'component_implementation_id_id',
            'to': '/api/v2/component-implementations'},
        'version': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.nullable.default': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
    },
}

COMPONENT_IMPLEMENTATION_DETAIL_LINKS = {
    '.collection.django': {},
    'model': 'component.models.ServiceDetailsComponent',
    ':permissions_namespace': 'agora.checks.CIDL',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'service_id': {
            '.flag.filterable': {},
            '.field.ref': {},
            'source': 'service_id_id',
            'to': '/api/v2/services'},
        'service_details_id': {
            '.flag.filterable': {},
            '.field.ref': {},
            'source': 'service_details_id_id',
            'to': '/api/v2/service-versions'},
        'service_component_implementation_detail_id': {
            '.flag.filterable': {},
            '.field.ref': {},
            'source': 'service_component_implementation_detail_id_id',
            'to': '/api/v2/component-implementation-details'},
        'service_type': {
            '.flag.searchable': {},
            '.field.string': {},
            '.flag.nullable.default': {}},
        'configuration_parameters': {
            '.field.string': {},
            '.flag.nullable.default': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
    },
}

SERVICES = {
    '.collection.django': {},
    'model': 'service.models.Service',
    'fields': SERVICE_FIELDS_INTERNAL,
    ':permissions_namespace': 'agora.checks.Service',
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
        'create': {
            'processors': {
                'custom_post_create': {
                    '.processor': {},
                    'module_path': 'service.models.PostCreateService',
                    'read_keys': {'=': (
                        'backend/raw_response',
                        'auth/user',
                    )},
                    'write_keys': {'=': (
                        'backend/raw_response',
                    )},
                },
            },
        },
    },
}

EXT_SERVICES = {
    '.collection.django': {},
    'model': 'service.models.Service',
    'fields': SERVICE_FIELDS_EXTERNAL,
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.partial_update': {},
    },
}

SERVICE_TYPES_FIELDS = {
    'id': {
        '.field.uuid': {},
        '.flag.nowrite': {}},
    'service_name': {
        '.field.string': {},
        '.flag.nowrite': {},
        'source': 'service_id.name'},
    'service_type': {
        '.field.string': {},
        '.flag.nowrite': {}},
    'in_catalogue': {
        '.field.boolean': {},
        '.flag.nowrite': {},
        '.flag.filterable': {},
        'source': 'service_details_id.is_in_catalogue'},
    'visible_to_marketplace': {
        '.field.boolean': {},
        '.flag.nowrite': {},
        '.flag.filterable': {},
        'source': 'service_details_id.visible_to_marketplace'},
    'external_service': {
        '.field.boolean': {},
        '.flag.nowrite': {},
        '.flag.filterable': {},
        'source': 'service_id.customer_facing'},
    'internal_service': {
        '.field.boolean': {},
        '.flag.nowrite': {},
        '.flag.filterable': {},
        'source': 'service_id.internal'},
    'service_area': {
        '.field.string': {},
        '.flag.nowrite': {},
        '.flag.filterable': {},
        'source': 'service_id.service_area.name'},
    'service_version': {
        '.field.string': {},
        '.flag.nowrite': {},
        '.flag.filterable': {},
        'source': 'service_details_id.version'},
    'component_name': {
        '.field.string': {},
        '.flag.nowrite': {},
        '.flag.filterable': {},
        'source': 'service_component_implementation_detail_id.component_id.name'},
    'component_version': {
        '.field.string': {},
        '.flag.nowrite': {},
        '.flag.filterable': {},
        'source': 'service_component_implementation_detail_id.version'},
    'service_id': {
        '.field.uuid': {},
        '.flag.nowrite': {},
        '.flag.filterable': {},
        'source': 'service_id.id'},


}

SERVICE_TYPES = {
    '.collection.django': {},
    'model': 'component.models.ServiceDetailsComponent',
    'fields': SERVICE_TYPES_FIELDS,
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
    },
}

SERVICE_VERSIONS = {
    '.collection.django': {},
    'model': 'service.models.ServiceDetails',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'id_service': {
            '.field.ref': {},
            'source': 'id_service_id',
            'to': '/api/v2/services',
            '.flag.filterable': {}},
        'status': {
            '.field.ref': {},
            'source': 'status_id',
            'to': '/api/v2/service-status',
            '.flag.filterable': {},
            '.flag.nullable.default': {}},
        'version': {
            '.flag.orderable': {},
            '.field.string': {}},
        'features_current': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'features_future': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'usage_policy_has': {
            '.field.boolean': {}},
        'usage_policy_url': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'privacy_policy_has': {
            '.field.boolean': {}},
        'privacy_policy_url': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'user_documentation_has': {
            '.field.boolean': {}},
        'user_documentation_url': {
            '.field.string': {},
            #'.flag.blankable': {},
            '.flag.nullable.default': {}},
        'operations_documentation_has': {
            '.field.boolean': {}},
        'operations_documentation_url': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'monitoring_has': {
            '.field.boolean': {}},
        'monitoring_url': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'accounting_has': {
            '.field.boolean': {}},
        'accounting_url': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'business_continuity_plan_has': {
            '.field.boolean': {}},
        'business_continuity_plan_url': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'disaster_recovery_plan_has': {
            '.field.boolean': {}},
        'disaster_recovery_plan_url': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'decommissioning_procedure_has': {
            '.field.boolean': {}},
        'decommissioning_procedure_url': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'cost_to_run': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'cost_to_build': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'use_cases': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'is_in_catalogue': {
            '.flag.filterable': {},
            '.flag.orderable': {},
            '.field.boolean': {}},
        'visible_to_marketplace': {
            '.flag.filterable': {},
            '.flag.orderable': {},
            '.field.boolean': {}},
        # extended fields
        'id_service_ext': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nowrite': {},
            'source': 'id_service.name'},
        'status_ext': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.nowrite': {},
            'source': 'status.value'},
        },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
    },
}

SERVICE_ADMINS = {
    '.collection.django': {},
    'model': 'service.models.ServiceAdminship',
    ':permissions_namespace': 'agora.checks.ServiceAdminship',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'state': {
            '.field.string': {},
            'default': 'pending',
            '.flag.filterable': {},
            '.flag.orderable': {}},
        'service': {
            '.field.ref': {},
            'source': 'service_id',
            'to': '/api/v2/services',
            '.flag.nullable.default': {},
            '.flag.filterable': {}},
        'service_name': {
            '.field.string': {},
            '.flag.nowrite': {},
            '.flag.orderable': {},
            'source': 'service.name'},
        'admin_email': {
            '.field.string': {},
            '.flag.nowrite': {},
            '.flag.orderable': {},
            'source': 'admin.email'},
        'admin_first_name': {
            '.field.string': {},
            '.flag.nowrite': {},
            'source': 'admin.first_name'},
        'admin_last_name': {
            '.field.string': {},
            '.flag.nowrite': {},
            'source': 'admin.last_name'},
        'admin_id': {
            '.field.uuid': {},
            '.flag.nowrite': {},
            'source': 'admin.id'},
        'created_at': {
            '.field.datetime': {},
            '.flag.nullable': {},
            '.flag.nowrite': {}},
        'updated_at': {
            '.field.datetime': {},
            '.flag.nullable': {},
            '.flag.nowrite': {}},
        'admin': {
            '.field.ref': {},
            'source': 'admin_id',
            '.flag.filterable': {},
            '.flag.nullable.default': {},
            'to': '/api/v2/custom-users'},

    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
        'create': {
            'processors': {
                'custom_post_create': {
                    '.processor': {},
                    'module_path': 'service.models.PostCreateServiceadminship',
                    'read_keys': {'=': (
                        'backend/raw_response',
                        'auth/user',
                        'request/meta/headers',
                    )},
                    'write_keys': {'=': (
                        'backend/raw_response',  # declared to ensure chaining
                    )},
                },
            },
        },
       'partial_update': {
           'processors': {
               'custom_post_partial_update': {
                   '.processor': {},
                   'module_path': 'service.models.PostPartialUpdateServiceadminship',
                   'read_keys': {'=': (
                       'backend/raw_response',
                       'auth/user',
                       'request/meta/headers',
                   )},
                   'write_keys': {'=': (
                       'backend/raw_response',  # declared to ensure chaining
                   )},
               },
           },
       },

    },
}


APP_CONFIG = {
    '.apimas_app': {},
    ':permission_rules': 'agora.utils.get_rules',
    ':authenticator': 'apimas.auth.DjoserAuthentication',
    ':verifier': 'agora.utils.djoser_verifier',
    ':user_resolver': 'agora.utils.userid_extractor',
    ':permissions_namespace': 'agora.checks',
    ':filter_compat': True,
    ':ordering_compat': True,

    'endpoints': {
        'api': {
            'prefix': 'api/v2',
            'collections': {
                'users': USERS,
                'services': SERVICES,
                'ext-services': EXT_SERVICES,
                'service-types': SERVICE_TYPES,
                'service-versions': SERVICE_VERSIONS,
                'user-customers': USER_CUSTOMERS,
                'service_dependsOn_services': SERVICE_DEPENDSON_SERVICES,
                'service_externalServices': SERVICE_EXTERNAL_SERVICES,
                'service-status': SERVICE_STATUS,
                'service-trls': SERVICE_TRLS,
                'external_services': EXTERNAL_SERVICES,
                'user-roles': USER_ROLES,
                'user_customers': USER_CUSTOMERS,
                'service-areas': SERVICE_AREAS,
                'service-owners': SERVICE_OWNERS,
                'service-admins': SERVICE_ADMINS,
                'custom-users': CUSTOM_USERS,
                'contact-information': CONTACT_INFORMATION,
                'institutions': INSTITUTIONS,
                'service-owners': SERVICE_OWNERS,
                'components': COMPONENTS,
                'component-implementations': COMPONENT_IMPLEMENTATIONS,
                'component-implementation-details': COMPONENT_IMPLEMENTATION_DETAILS,
                'component-implementation-detail-links': COMPONENT_IMPLEMENTATION_DETAIL_LINKS,
            },
        },
    },
}
