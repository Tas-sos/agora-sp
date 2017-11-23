import { field } from 'ember-gen';

/********************************************
                LIST VIEW
********************************************/

const SORT_FIELDS = [];
const TABLE_FIELDS = [
    field('service_component_implementation_detail_id.component_id.name', {
      type: 'text',
      label: 'component.belongs.name'
    }),
    field('service_component_implementation_detail_id.component_implementation_id.name', {
      type: 'text',
      label: 'component_implementation.belongs.name'
    }),
    field('service_component_implementation_detail_id.version', {
      type: 'text',
      label: 'component_implementation_detail.belongs.name'
    }),
    field('configuration_parameters', {
      type: 'text',
      label: 'cidl.fields.configuration_parameters'
    }),
    field('service_id.name', {
      type: 'text',
      label: 'service_item.belongs.name'
    }),
    field('service_details_id.version', {
      type: 'text',
      label: 'service_version.belongs.version'
    }),
];

/********************************************
                DETAILS VIEW
********************************************/

const DETAILS_FIELDSETS = [
  {
    label: 'cidl.cards.components',
    layout: {
      flex: [100, 100, 100 ,100]
    },
    fields: [
      field('service_component_implementation_detail_id.component_id.name', {
        type: 'text',
        label: 'component.belongs.name'
      }),
      field('service_component_implementation_detail_id.component_implementation_id.name', {
        type: 'text',
        label: 'component_implementation.belongs.name'
      }),
      field('service_component_implementation_detail_id.version', {
        type: 'text',
        label: 'component_implementation_detail.belongs.name'
      }),
      field('configuration_parameters', {
        type: 'text',
        label: 'cidl.fields.configuration_parameters'
      }),
    ]
  },
  {
    label: 'cidl.cards.service_version',
    fields: [
      field(
        'service_id.name', {
          type: 'text',
          label: 'service_item.belongs.name'
        }
      ),
      field(
        'service_details_id.version', {
          label: 'service_version.belongs.version'
        }
      ),
    ],
    layout: {
      flex: [100, 100]
    }
  }
];

/********************************************
                  EDIT VIEW
********************************************/

const CREATE_FIELDSETS = [
  {
    label: 'cidl.cards.components',
    fields: [
      field('service_component', {
        label: 'component.belongs.name'
      }),
      field('service_component_implementation', {
        label: 'component_implementation.belongs.name'
      }),
      field('service_component_implementation_detail_id', {
        label: 'component_implementation_detail.belongs.name'
      }),
      field('configuration_parameters', {
        label: 'cidl.fields.configuration_parameters'
      })
    ],
    layout: {
      flex: [100, 100, 100, 100]
    }
  },
  {
    label: 'cidl.cards.service_version',
    fields: [
      field('service_id', {
        label: 'service_item.belongs.name'
      }),
      field('service_details_id', {
        label: 'service_version.belongs.version'
      }),
    ],
    layout: {
      flex: [100, 100]
    }
  }
];

/********************************************
                  EDIT VIEW
********************************************/

const EDIT_FIELDSETS = [
  {
    label: 'components',
    fields: [
      field('service_component', {
        label: 'component.belongs.name'
      }),
      field('service_component_implementation', {
        label: 'component_implementation.belongs.name'
      }),
      field('service_component_implementation_detail_id', {
        label: 'component_implementation_detail.belongs.name'
      }),
      field('configuration_parameters', {
        type: 'text'
      }),
    ],
    layout: {
      flex: [100, 100, 100, 100]
    }
  },
  {
    label: 'service version',
    fields: [
      field('service_id', {
        label: 'service_item.belongs.name'
      }),
      field('service_details_id', {
        label: 'service_version.belongs.version'
      }),
    ],
    layout: {
      flex: [100, 100]
    }
  }
];

export {
  TABLE_FIELDS,
  SORT_FIELDS,
  DETAILS_FIELDSETS,
  CREATE_FIELDSETS,
  EDIT_FIELDSETS
};
