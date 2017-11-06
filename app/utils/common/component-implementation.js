import { field } from 'ember-gen';

const SORT_FIELDS = [
  'name',
  'component_id'
];

/********************************************
                LIST VIEW
********************************************/

const TABLE_FIELDS = [
  field('name', {
    type: 'text',
    label: 'component_implementation.fields.name'
  }),
  field('description', {
    type: 'text',
    label: 'component_implementation.fields.description'
  }),
  field('component_id.name', {
    type: 'text',
    label: 'component.belongs.name'
  }),
];

/********************************************
                DETAILS VIEW
********************************************/

const DETAILS_FIELDSETS = [
  {
    label: 'component_implementation.cards.basic_information',
    fields: [
      field('name', {
        type: 'text',
        label: 'component_implementation.fields.name'
      }),
      field('description', {
        type: 'text',
        label: 'component_implementation.fields.description',
        htmlSafe: true
      }),
      field('component_id.name', {
        type: 'text',
        label: 'component.belongs.name'
      }),
    ]
  }
];

/********************************************
                 EDIT VIEW
                CREATE VIEW
********************************************/

const CREATE_FIELDSETS = [
  {
    label: 'Component Category',
    fields: [
      field('name', {
        type: 'text',
        label: 'component_implementation.fields.name'
      }),
      field('description', {
        type: 'text',
        label: 'component_implementation.fields.description'
      }),
      field('component_id', {
        label: 'component.belongs.name'
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
