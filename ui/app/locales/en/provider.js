const provider = {
  'cards': {
    'basic_information': 'Basic information',
    'basic_hint': '',
    'location': 'Location information',
    'location_hint': '',
    'marketing': 'Marketing Information',
    'marketing_hint': 'Marketing Information for the Provider',
    'maturity': 'Maturity Information',
    'maturity_hint': 'Maturity Information for the Provider',
    'contact': 'Contact Information',
    'main_contact': 'Main Contact/Service Owner',
    'public_contact': 'Public Contact',
    'other': 'Other Information',
    'other_hint': '',
    'classification': 'Classification Information',
    'classification_hint': '',

  },
  'fields': {
    'epp_bai_3_legal_entity': 'EPP.BAI.3 - Legal Entity',
    'epp_bai_3_legal_status': 'EPP.BAI.3 - Legal Status',
    'epp_bai_0_id': 'EPP.BAI.0 - ID',
    'epp_bai_1_name': 'EPP.BAI.1 - Name',
    'epp_bai_2_abbreviation': 'EPP.BAI.2 - Abbreviation',
    'epp_bai_4_website': 'EPP.BAI.4 - Website',
    'epp_cli_1_scientific_domain': 'EPP.CLI.1 - Scientific Domain',
    'epp_cli_2_scientific_subdomain': 'EPP.CLI.2 - Scientific Subdomain',
    'epp_cli_3_tags': 'EPP.CLI.3 - Tags',
    'epp_loi_1_street_name_and_number': 'EPP.LOI.1 - Street Name and Number',
    'epp_loi_2_postal_code': 'EPP.LOI.2 - Postal Code',
    'epp_loi_3_city': 'EPP.LOI.3 - City',
    'epp_loi_4_region': 'EPP.LOI.4 - Region',
    'epp_loi_5_country_or_territory': 'EPP.LOI.5 - Country or Territory',
    'epp_mri_1_description': 'EPP.MRI.1 - Description',
    'epp_mri_2_logo': 'EPP.MRI.2 - Logo',
    'epp_mri_3_multimedia': 'EPP.MRI.3 - Multimedia',
    'epp_mti_1_life_cycle_status': 'EPP.MTI.1 - Life Cycle Status',
    'epp_mti_2_certifications': 'EPP.MTI.2 - Certifications',
    'main_contact': 'Main Contact/Service Owner',
    'public_contact': 'Public Contact',
    'mc_first_name': 'EPP.COI.1 - First Name',
    'mc_last_name': 'EPP.COI.2 - Last Name',
    'mc_email': 'EPP.COI.3 - Email',
    'mc_phone': 'EPP.COI.4 - Phone',
    'mc_position': 'EPP.COI.5 - Position',
    'pc_first_name': 'EPP.COI.6 - First Name',
    'pc_last_name': 'EPP.COI.7 - Last Name',
    'pc_email': 'EPP.COI.8 - Email',
    'pc_phone': 'EPP.COI.9 - Phone',
    'pc_position': 'EPP.COI.10 - Position',
    'epp_oth_1_hosting_legal_entity': 'EPP.OTH.1 - Hosting Legal Entity',
    'epp_oth_2_participating_countries': 'EPP.OTH.2 - Participating Countries',
    'epp_oth_3_affiliations': 'EPP.OTH.3 - Affiliations',
    'epp_oth_4_networks': 'EPP.OTH.4 - Networks',
    'epp_oth_5_structure_type': 'EPP.OTH.5 - Structure Type',
    'epp_oth_6_esfri_domain': 'EPP.OTH.6 - ESFRI Domain',
    'epp_oth_7_esfri_type': 'EPP.OTH.7 - ESFRI Type',
    'epp_oth_8_areas_of_activity': 'EPP.OTH.8 - Areas of activity',
    'epp_oth_9_societal_grand_challenges': 'EPP.OTH.9 - Societal Grand challenges',
    'affiliation_names': 'EPP.OTH.3 - Affiliations',
    'network_names': 'EPP.OTH.4 - Networks',
    'structure_names': 'EPP.OTH.5 - Structure Type',
    'esfridomain_names': 'EPP.OTH.6 - ESFRI Domain',
    'activity_names': 'EPP.OTH.8 - Areas of activity',
    'challenge_names': 'EPP.OTH.9 - Societal Grand challenges',
    'epp_oth_10_national_roadmaps': 'EPP.OTH.10 - National Roadmaps',


  },
  'hints': {
    'epp_bai_3_legal_entity': 'Is the provider a legal entity?',
    'epp_bai_3_legal_status': 'Legal Status of the Service Provider',
    'epp_bai_0_id': '<strong>Unique</strong> identifier of the provider',
    'epp_bai_1_name': '<strong>Unique</strong> Full Name of the Provider offering the resource and acting as main contact point.',
    'epp_bai_2_abbreviation': 'Abbreviation or Short name of the Provider',
    'epp_bai_4_website': 'Website with information about the Provider.',
    'epp_cli_1_scientific_domain': 'The branch of science, scientific discipline that is related to the service/resource.',
    'epp_cli_2_scientific_subdomain': 'The subbranch of science, scientific subdicipline that is related to the service/resource.',
    'epp_cli_3_tags': 'Keywords associated to the service/resource to simplify search by relevant keywords. <br/>Hit <strong>ENTER</strong> to register your tag.',
    'epp_loi_1_street_name_and_number': 'Street and number of the Provider\'s physical location.<br />example: Christou Lada Str.',
    'epp_loi_2_postal_code': 'Postal code of the Provider\'s physical location.<br />example: 10561',
    'epp_loi_3_city': 'City that the Provider is located in.<br />example: Athens',
    'epp_loi_4_region': 'Region that the Provider is located in.<br />example: Attika',
    'epp_loi_5_country_or_territory': 'Select a Country or Territory that the Provider is located in.<br />example: Greece',
    'epp_mri_1_description': 'The description of the Provider',
    'epp_mri_2_logo': 'Link to the logo/visual identity of the Provider',
    'epp_mri_3_multimedia': 'Link toCurrent status of the Provider/Research infrastucture lifecycle',
    'epp_mti_2_certifications': 'List of certifications obtained for the Provider (including the certification body and any certificate number).',
    'main_contact': 'This info will not be publicly exposed',
    'public_contact': 'This info will be exposed to public API ',
    'epp_oth_1_hosting_legal_entity': 'Name of the organisation/institution legally hosting (housing) the provider/research infrastructure or its coordinating centre.',
    'epp_oth_2_participating_countries': 'Providers/Research Infrastructures that are funded by several countries should list here all supporting countries (including the Coordinating country).',
    'epp_oth_3_affiliations': '<br />Select the provider\'s affiliations',
    'epp_oth_4_networks': '<br />Select the networks the Provider is participating in.',
    'epp_oth_5_structure_type': '<br />Define the providers structure types',
    'epp_oth_6_esfri_domain': '<br />ESFRI domain classification.',
    'epp_oth_7_esfri_type': '<br />If the research infrastructure is (part of) an ESFRI project indicate how the RI participates',
    'epp_oth_8_areas_of_activity': '<br />Basic research, Applied research or Technological development',
    'epp_oth_9_societal_grand_challenges': '<br />Provider’s participation in the grand societal challenges as defined by the European Commission',
    'epp_oth_10_national_roadmaps': 'Provider being part of a national roadmap for research infrastructures',
  },
  table: {
    epp_bai_0_id: 'ID',
    epp_bai_1_name: 'Name',
    epp_bai_2_abbreviation: 'Abbreviation',
  },
  'belongs': {
    'name': 'Provider',
    'hint': ''
  },
  'menu': 'Providers'
};

export { provider };
