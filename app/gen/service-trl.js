import { AgoraGen } from '../lib/common';
import { field } from 'ember-gen';

const {
  get
} = Ember;

export default AgoraGen.extend({
  modelName: 'service-trl',
  order: 100,
  path: 'service-trls',
  resourceName: 'api/v2/service-trls',
  list: {
    layout: 'table',
    page: {
      title: 'Service Technology Readiness Levels'
    },
    menu: {
      label: 'Service Technology Readiness Levels',
      group: 'settings'
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
      fields: [
        //'id',
        'value',
        'order'
      ]
    },
    filter: {
      active: true,
      serverSide: true,
      search: false,
      meta: {
        fields: [
          field(
            'value', {
              type: 'text',
              label: 'service_trl.fields.value'
            }
          ),
          field(
            'order', {
              type: 'text'
            }
          )
        ]
      }
    },
    sort: {
      serverSide: true,
      active: true,
      fields: [
        'value',
        'order'
      ]
    },
    paginate: {
      limits: [ 10, 50, 100 ],
      serverSide: true,
      active: true
    }
  }
});
