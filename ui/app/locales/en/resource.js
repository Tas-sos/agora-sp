const resource = {
  cards: {
    basic: 'Basic information',
    basic_hint: '',
    marketing: 'Marketing Information',
    geo: 'Geographical and Language Availability Information',
    contact: 'Contact Information',
    main_contact: 'Main Contact/Resource Owner',
    public_contact: 'Public Contact',
    other_contact: 'Other Contacts',
    management_information: 'Management Information',
    classification: 'Classification Information',
    classification_hint: '',
    financial: 'Financial Information',
    dependencies: 'Dependencies Information',
    access_order: 'Access and Order Information',
    attribution: 'Attribution Information',
  },
  fields: {
    erp_bai_0_id: 'ERP.BAI.0 - ID',
    erp_bai_1_name: 'ERP.BAI.1 - Name',
    erp_bai_2_service_organisation: 'ERP.BAI.2 - Resource Organisation',
    erp_bai_3_service_providers: 'ERP.BAI.3 - Resource Providers',
    erp_bai_4_webpage: 'ERP.BAI.4 - Webpage',
    providers_names: 'ERP.BAI.3 - Service Providers',
    erp_mri_1_description: 'ERP.MRI.1 - Description',
    erp_mri_2_tagline: 'ERP.MRI.2 - Tagline',
    erp_mri_3_logo: 'ERP.MRI.3 - Logo',
    erp_mri_4_mulitimedia: 'ERP.MRI.4 - Mulitimedia',
    erp_cli_5_target_users: 'ERP.CLI.5 - Target Users',
    erp_mri_6_target_customer_tags: 'ERP.MRI.6 - Customer Tags',
    erp_mri_5_use_cases: 'ERP.MRI.5 - Use Cases',
    erp_cli_1_scientific_domain: 'ERP.CLI.1 - Scientific Domain',
    erp_cli_2_scientific_subdomain: 'ERP.CLI.2 - Scientific Subdomain',
    erp_cli_3_category: 'ERP.CLI.3 - Category',
    erp_cli_4_subcategory: 'ERP.CLI.4 - Subcategory',
    erp_cli_5_tags: 'ERP.CLI.5 - Tags',
    erp_mgi_1_helpdesk_webpage: 'ERP.MGI.1 - Heldesk Page',
    erp_mgi_2_user_manual: 'ERP.MGI.2 - User Manual',
    erp_mgi_3_terms_of_use: 'ERP.MGI.3 - Terms of Use',
    erp_mgi_4_privacy_policy: 'ERP.MGI.4 - Privacy Policy',
    erp_mgi_5_access_policy: 'ERP.MGI.5 - Access Policy',
    erp_mgi_6_sla_specification: 'ERP.MGI.6 - Service Level',
    erp_mgi_7_training_information: 'ERP.MGI.7 - Training Information',
    erp_mgi_8_status_monitoring: 'ERP.MGI.8 - Status Monitoring',
    erp_mgi_9_maintenance: 'ERP.MGI.9 - Maintenance',
    erp_gla_1_geographical_availability: 'ERP.GLA.1 - Geographical Availability',
    erp_gla_2_language: 'ERP.GLA.2 - Language Availability',
    erp_aoi_1_order_type: 'ERP.AOI.1 - Order Type',
    erp_aoi_2_order: 'ERP.AOI.2 - Order',
    erp_fni_1_payment_model: 'ERP.FNI.1 - Payment Model',
    erp_fni_2_pricing: 'ERP.FNI.2 - Pricing',
    main_contact: 'Main Contact/Resource Owner',
    public_contact: 'Public Contact',
    erp_dei_1_required_resources: 'ERP.DEI.1 - Required Resources',
    erp_dei_2_related_resources: 'ERP.DEI.2 - Related Resources',
    erp_dei_3_related_platforms: 'ERP.DEI.3 - Related Platforms',
    erp_coi_13_helpdesk_email: 'EPR.COI.13 - Helpdesk Email',
    erp_coi_14_security_contact_email: 'ERP.COI.14 - Security Contact Email',
    erp_ati_1_funding_body: 'ERP.ATI.1 - Funding Body',
    erp_ati_2_funding_program: 'ERP.ATI.2 - Funding Program',
    erp_ati_3_grant_project_name: 'ERP.ATI.3 - Grant/Project Name',
    mc_first_name: 'ERP.COI.1 - First Name',
    mc_last_name: 'ERP.COI.2 - Last Name',
    mc_email: 'ERP.COI.3 - Email',
    mc_phone: 'ERP.COI.4 - Phone',
    mc_position: 'ERP.COI.5 - Position',
    mc_organisation: 'ERP.COI.6 - Organisation',
    pc_first_name: 'ERP.COI.7 - First Name',
    pc_last_name: 'ERP.COI.8 - Last Name',
    pc_email: 'ERP.COI.9 - Email',
    pc_phone: 'ERP.COI.10 - Phone',
    pc_position: 'ERP.COI.11 - Position',
    pc_organisation: 'ERP.COI.12 - Organisation',

  },
  hints: {
    erp_bai_0_id: 'Global <strong>unique and persistent</strong> reference to the Resource . The first part denotes the Resource Provider and the second part the unique identifier of the resource.<br />Example: openaire.foo',
    erp_bai_1_name: '<strong>Unique</strong>, brief and descriptive name of Resource as assigned by the Provider.',
    erp_bai_2_service_organisation: 'The name (or abbreviation) of the organisation that manages or delivers the Resource, or that coordinates resource delivery in a federated scenario.',
    erp_bai_3_service_providers: 'The name(s) (or abbreviation(s)) of Provider(s) that manage or deliver the Resource in federated scenarios.',
    erp_bai_4_webpage: 'Webpage with information about the Resource usually hosted and maintained by the Provider.',
    erp_mri_1_description: '',
    erp_mri_2_tagline: 'Short catch-phrase for marketing and advertising purposes.',
    erp_mri_3_logo: 'Link to the logo/visual identity of the Resource. The logo will be visible at the Portal.',
    erp_mri_4_mulitimedia: 'Link to video, screenshots or slides showing details of the Resource.',
    erp_mri_5_use_cases: 'Link to use cases supported by this Resource.',
    erp_cli_1_scientific_domain: 'The branch of science, scientific discipline that is related to the service/resource.',
    erp_cli_2_scientific_subdomain: 'The subbranch of science, scientific subdicipline that is related to the service/resource.',
    erp_cli_3_category: 'A named group of services/resources that offer access to the same type of resource or capabilities.',
    erp_cli_4_subcategory: 'A named group of services/resources that offer access to the same type of resource or capabilities, within the defined service category',
    erp_cli_5_tags: 'Keywords associated to the service/resource to simplify search by relevant keywords. <br/>Hit <strong>ENTER</strong> to register your tag.',
    erp_cli_5_target_users: '',
    erp_mgi_1_helpdesk_webpage: 'The URL to a webpage to ask more information from the Provider about this Resource.',
    erp_mgi_2_user_manual: 'Link to the Resource user manual and documentation.',
    erp_mgi_3_terms_of_use: 'Webpage describing the rules, Resource conditions and usage policy which one must agree to abide by in order to use the Resource.',
    erp_mgi_4_privacy_policy: 'Link to the privacy policy applicable to the Resource.',
    erp_mgi_5_access_policy: 'Information about the access policies that apply.',
    erp_mgi_6_sla_specification: 'Webpage with the information about the levels of performance that a Provider is expected to deliver.',
    erp_mgi_7_training_information: 'Webpage to training information on the Resource.',
    erp_mgi_8_status_monitoring: 'Webpage with monitoring information about this Resource.',
    erp_mgi_9_maintenance: 'Webpage with information about planned maintenance windows for this Resource.',
    erp_gla_1_geographical_availability: 'The countries in which your service is available to the users.<br>If the service is European-wide, please list "Europe".If the service is universal, please list "World".',
    erp_gla_2_language: 'Add the language codes using the <a href="https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes" target="_blank">2-letter codes from the ISO</a>',
    main_contact: 'This info will not be publicly exposed',
    public_contact: 'This info will be exposed to public API ',
    erp_dei_1_required_resources: 'List of other Resources required to use this Resource.',
    erp_dei_2_related_resources: 'List of other Resources that are commonly used with this Resource.',
    erp_dei_3_related_platforms: 'List of suites or thematic platforms in which the Resource is engaged or Providers (Provider groups) contributing to this Resource.',
    erp_ati_1_funding_body: 'Name of the funding body that supported the development and/or operation of the Resource.',
    erp_ati_2_funding_program: 'Name of the funding program that supported the development and/or operation of the Resource.',
    erp_ati_3_grant_project_name: 'Name of the project that supported the development and/or operation of the Resource.',
    erp_coi_13_helpdesk_email: '',
    erp_coi_14_security_contact_email: '',
    erp_aoi_1_order_type: 'Information on the order type (requires an ordering procedure, or no ordering and if fully open or requires authentication)',
    erp_aoi_2_order: 'Webpage through which an order for the Resource can be placed',
    erp_fni_1_payment_model: 'Webpage with the supported payment models and restrictions that apply to each of them.',
    erp_fni_2_pricing: 'Webpage with the information on the price scheme for this Resource in case the customer is charged for.',
  },
  table: {
    erp_bai_0_id: 'ID',
    erp_bai_1_name: 'Name',
    erp_bai_2_service_organisation: 'Organisation',
  },
  placeholders: {
    search: 'Search by ID or Name',
  },
  menu: 'Resources',
  my_menu: 'My Resources',
};

export { resource }
