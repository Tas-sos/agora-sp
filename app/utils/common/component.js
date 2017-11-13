import { field } from 'ember-gen';

const SORT_FIELDS = [
  'name'
];

/********************************************
                LIST VIEW
********************************************/

const TABLE_FIELDS = [
  field('name', {
    type: 'text',
    label: 'component.fields.name'
  }),
  field('description', {
    type: 'text',
    label: 'component.fields.description'
  }),
  field('logo', {
    type: 'text',
    label: 'component.fields.logo'
  }),
];

/********************************************
                DETAILS VIEW
********************************************/

const DETAILS_FIELDSETS = [
  {
    label: 'component.cards.basic_information',
    fields: [
      field('name', {
        type: 'text',
        label: 'component.fields.name'
      }),
      field('description', {
        type: 'text',
        label: 'component.fields.description',
        htmlSafe: true
      }),
      field('logo', {
        type: 'text',
        label: 'component.fields.logo'
      }),
    ]
  }
];

/********************************************
            EDIT VIEW/CREATE VIEW
********************************************/

const CREATE_FIELDSETS = [
  {
    label: 'Component Category',
    fields: [
      field('name', {
        type: 'text',
        label: 'component.fields.name'
      }),
      field('description', {
        type: 'text',
        label: 'component.fields.description'
      }),
      field('logo', {
        type: 'text',
        label: 'component.fields.logo'
      }),
    ]
  }
];

export {
  TABLE_FIELDS,
  SORT_FIELDS,
  DETAILS_FIELDSETS,
  CREATE_FIELDSETS
};
