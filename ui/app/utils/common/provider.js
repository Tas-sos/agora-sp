import { field } from 'ember-gen';
import { fileField } from '../../lib/common';


const CONTACT_FIELDSET = {
  label: 'provider.cards.contact',
  fields: [
    field(
      'main_contact', {
        displayAttr: 'displayInfo'
      }
    ),
    field(
      'public_contact', {
        displayAttr: 'displayInfo'
      }
    ),
  ],
  layout: {
    flex: [100, 100],
  },
};

const DETAILS_CONTACT_MAIN_FIELDSET = {
  label: 'provider.cards.main_contact',
  fields: [
    field('main_contact.first_name', {label: 'provider.fields.mc_first_name'}),
    field('main_contact.last_name', {label: 'provider.fields.mc_last_name'}),
    field('main_contact.email', {label: 'provider.fields.mc_email'}),
    field('main_contact.phone', {label: 'provider.fields.mc_phone'}),
    field('main_contact.position', {label: 'provider.fields.mc_position'}),
  ],
  layout: {
    flex: [50, 50, 50, 50, 50],
  },
};


const DETAILS_CONTACT_PUBLIC_FIELDSET = {
  label: 'provider.cards.public_contact',
  fields: [
    field('public_contact.first_name', {label: 'provider.fields.pc_first_name'}),
    field('public_contact.last_name', {label: 'provider.fields.pc_last_name'}),
    field('public_contact.email', {label: 'provider.fields.pc_email'}),
    field('public_contact.phone', {label: 'provider.fields.pc_phone'}),
    field('public_contact.position', {label: 'provider.fields.pc_position'}),
  ],
  layout: {
    flex: [50, 50, 50, 50, 50],
  },
};

/********************************************
                DETAILS VIEW
********************************************/

const DETAILS_FIELDSETS = [{
  label: 'provider.cards.basic_information',
  text: 'provider.cards.basic_hint',
  layout: {
    flex: [100, 100, 100, 100, 100, 100, 100, 100, 100, 50]
  },
  fields: [
    'name',
    'contact',
    'pd_bai_0_id',
    'pd_bai_1_name',
    'pd_bai_2_abbreviation',
    'pd_bai_3_legal_status',
    'pd_bai_4_website',
    field(
      'description', {
        type: 'text',
        htmlSafe: true,
        formComponent: 'text-editor',
      }
    ),
    fileField(
      'logo', 'provider', 'logo', {
        readonly: true,
      }, {
        img: true
      }
    ),
    'pd_bai_3_legal_entity',
  ]
},
{
  label: 'provider.cards.location',
  text: 'provider.cards.location_hint',
  layout: {
    flex: [100, 100, 100, 100, 100]
  },
  fields: [
    'pd_loi_1_street_name_and_number',
    'pd_loi_2_postal_code',
    'pd_loi_3_city',
    'pd_loi_4_region',
    'pd_loi_5_country_or_territory',
  ]
},
{
  label: 'provider.cards.marketing',
  text: 'provider.cards.marketing_hint',
  layout: {
    flex: [100, 100, 100]
  },
  fields: [
  'pd_mri_1_description',
  'pd_mri_2_logo',
  'pd_mri_3_multimedia',
]
},
DETAILS_CONTACT_MAIN_FIELDSET,
DETAILS_CONTACT_PUBLIC_FIELDSET,
]


/********************************************
                EDIT VIEW
********************************************/

const EDIT_FIELDSETS = [{
  label: 'provider.cards.basic_information',
  text: 'provider.cards.basic_hint',
  layout: {
    flex: [100, 100, 100, 100, 100, 100, 100, 100, 100, 50]
  },
  fields: [
    'name',
    'contact',
    'pd_bai_0_id',
    'pd_bai_1_name',
    'pd_bai_2_abbreviation',
    'pd_bai_3_legal_status',
    'pd_bai_4_website',
    field(
      'description', {
        type: 'text',
        htmlSafe: true,
        formComponent: 'text-editor',
      }
    ),
    fileField(
      'logo', 'provider', 'logo', {
      }, {
        img: true
      }
    ),
    'pd_bai_3_legal_entity',
  ]
},
{
  label: 'provider.cards.location',
  text: 'provider.cards.location_hint',
  layout: {
    flex: [100, 100, 100, 100, 100]
  },
  fields: [
    'pd_loi_1_street_name_and_number',
    'pd_loi_2_postal_code',
    'pd_loi_3_city',
    'pd_loi_4_region',
    'pd_loi_5_country_or_territory',
  ]
},
{
  label: 'provider.cards.marketing',
  text: 'provider.cards.marketing_hint',
  layout: {
    flex: [100, 100, 100]
  },
  fields: [
  'pd_mri_1_description',
  'pd_mri_2_logo',
  'pd_mri_3_multimedia',
]
},
CONTACT_FIELDSET
]



/********************************************
                CREATE  VIEW
********************************************/

const CREATE_FIELDSETS = [{
  label: 'provider.cards.basic_information',
  text: 'provider.cards.basic_hint',
  layout: {
    flex: [100, 100, 100, 100, 100, 100, 100, 100, 100, 50]
  },
  fields: [
    'name',
    'contact',
    'pd_bai_0_id',
    'pd_bai_1_name',
    'pd_bai_2_abbreviation',
    'pd_bai_3_legal_status',
    'pd_bai_4_website',
    field(
      'description', {
        type: 'text',
        htmlSafe: true,
        formComponent: 'text-editor',
      }
    ),
    'pd_bai_3_legal_entity',
  ]
},
{
  label: 'provider.cards.location',
  text: 'provider.cards.location_hint',
  layout: {
    flex: [100, 100, 100, 100, 100]
  },
  fields: [
    'pd_loi_1_street_name_and_number',
    'pd_loi_2_postal_code',
    'pd_loi_3_city',
    'pd_loi_4_region',
    'pd_loi_5_country_or_territory',
  ]
},
{
  label: 'provider.cards.marketing',
  text: 'provider.cards.marketing_hint',
  layout: {
    flex: [100, 100, 100]
  },
  fields: [
  'pd_mri_1_description',
  'pd_mri_2_logo',
  'pd_mri_3_multimedia',
]
},
CONTACT_FIELDSET,
]

export {
  DETAILS_FIELDSETS,
  EDIT_FIELDSETS,
  CREATE_FIELDSETS
};
