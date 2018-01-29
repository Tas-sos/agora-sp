.meta:
  get_rules: agora.utils.get_rules
api/v2:
  .endpoint: {}
  users:
    .collection:
      model: accounts.models.User
    '*':
      id:
        .uuid: {}
        .readonly: {}
      username:
        .string: {}
      email:
        .string: {}
    .actions=:
      .list: {}
  service:
    .collection:
      model: service.models.Service
    '*':
      id:
        .uuid: {}
        .readonly: {}
      name:
        .string: {}
      service-trls:
        .ref: {'to': '/api/v2/service-trls'}
      id_service_owner:
        .ref: {'to': '/api/v2/service_owner'}
      id_contact_information:
        .ref: {'to': '/api/v2/contact_information'}
      id_contact_information_internal:
        .ref: {'to': '/api/v2/contact_information_internal'}
  service_details:
    .collection:
      model: service.models.ServiceDetails
    '*':
      id:
        .uuid: {}
        .readonly: {}
      id_service:
        .ref: {'to': '/api/v2/service'}
      status:
        .ref: {'to': '/api/v2/service_status'}
      version:
        .string: {}
  service_dependsOn_service:
    .collection:
      model: service.models.Service_DependsOn_Service
    '*':
      id:
        .uuid: {}
        .readonly: {}
      id_service_one:
        .ref: {'to': '/api/v2/service'}
      id_service_two:
        .ref: {'to': '/api/v2/service'}
  service_externalService:
    .collection:
      model: service.models.Service_ExternalService
    '*':
      id:
        .uuid: {}
        .readonly: {}
      id_service:
        .ref: {'to': '/api/v2/service'}
      id_external_service:
        .ref: {'to': '/api/v2/external_service'}
  service_status:
    .collection:
      model: service.models.ServiceStatus
    '*':
      id:
        .uuid: {}
        .readonly: {}
      value:
        .string: {}
      order:
        .integer: {}
      .actions=:
        .retrieve: {}
        .update: {}
        .delete: {}
    .actions=:
      .list: {}
      .create: {}
  service-trls:
    .collection:
      model: service.models.ServiceTrl
    '*':
      id:
        .uuid: {}
        .readonly: {}
      value:
        .string: {}
        .filterable: {}
        .searchable: {}
        .sortable: {}
      order:
        .integer: {}
      .actions=:
        .retrieve: {}
        .update: {}
        .delete: {}
    .actions=:
      .list: {}
      .create: {}
  external_service:
    .collection:
      model: service.models.ExternalService
    '*':
      id:
        .uuid: {}
        .readonly: {}
      name:
        .string: {}
      description:
        .string: {}
      service:
        .string: {}
      details:
        .string: {}
      .actions=:
        .retrieve: {}
        .update: {}
        .delete: {}
    .actions=:
      .list: {}
      .create: {}
  external_service:
    .collection:
      model: service.models.ExternalService
    '*':
      id:
        .uuid: {}
        .readonly: {}
      name:
        .string: {}
  user_role:
    .collection:
      model: service.models.UserRole
    '*':
      id:
        .uuid: {}
        .readonly: {}
      name:
        .string: {}
      .actions=:
        .retrieve: {}
        .update: {}
        .delete: {}
    .actions=:
      .list: {}
      .create: {}
  user_customer:
    .collection:
      model: service.models.UserCustomer
    '*':
      id:
        .uuid: {}
        .readonly: {}
      name:
        .ref: {'to': '/api/v2/user_role'}
      service_id:
        .ref: {'to': '/api/v2/service'}
      role:
        .string: {}
  service_area:
    .collection:
      model: service.models.ServiceArea
    '*':
      id:
        .uuid: {}
        .readonly: {}
      name:
        .string: {}
      icon:
        .file: {}
      .actions=:
        .update: {}
        .delete: {}
    .actions=:
      .list: {}
      .create: {}
  service_owner:
    .collection:
      model: owner.models.ServiceOwner
    '*':
      id:
        .uuid: {}
        .readonly: {}
      id_service_owner:
        .ref: {'to': '/api/v2/institution'}
      id_account:
        .ref: {'to': '/api/v2/custom_user'}
  institution:
    .collection:
      model: owner.models.Institution
    '*':
      id:
        .uuid: {}
        .readonly: {}
      name:
        .string: {}
  contact_information:
    .collection:
      model: owner.models.ContactInformation
    '*':
      id:
        .uuid: {}
        .readonly: {}
      first_name:
        .string: {}
      last_name:
        .string: {}
