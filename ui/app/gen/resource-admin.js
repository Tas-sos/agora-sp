import Ember from 'ember';
import validate from 'ember-gen/validate';
import { field } from 'ember-gen';
import ENV from '../config/environment';
import { AgoraGen } from '../lib/common';
import {
  approveResourceAdminship,
  rejectResourceAdminship,
  undoResourceAdminship,
} from '../utils/common/actions';

const CHOICES = ENV.APP.resources;

const {
  get,
} = Ember;

export default AgoraGen.extend({
  modelName: 'resource-admin',
  order: 100,
  path: 'resource-admins',
  resourceName: 'api/v2/resource-admins',
  abilityStates: {
    check_create_other: true,
 },
  common: {
    validators: {
      resource: [validate.presence(true)],
      admin: [validate.presence(true)],
    },
  },
  list: {
    getModel(params) {
      params = params || {};

      return this.store.query('resource-admin', params).then((sa) => {
        let user_id = get(this, 'session.session.authenticated.id');
        let res = sa.filter(el => get(el, 'admin_id').toString() !== user_id.toString());

        return res;
      });
    },
    page: {
      title: 'resource_admin.menu',
    },
    menu: {
      label: 'resource_admin.menu',
      order: 400,
      icon: 'people',
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
      fields: ['resource_name', 'admin_email', 'state']
    },
    sort: {
      serverSide: true,
      active: true,
      fields: ['resource_name', 'admin_email', 'state'],
    },
  },
  create: {
    getModel(params) {
      let store = get(this, 'store');

      return store.createRecord('resource-admin', {
        state: 'approved',
      });
    },
    fields : [
      field('admin', {
        query: (table, store, field, params) => {
          return store.query('custom-user', { role: 'serviceadmin' });
        },
      }),
      'resource',
    ],
  },
  details: {
    fieldsets: [{
      label: 'resource_admin.cards.basic_information',
      fields: [
        'state',
        'created_at',
        'updated_at',
      ],
    }, {
      label: 'resource_admin.cards.admin_info',
      fields: [
        'admin_full_name',
        'admin_email',
        'admin_id',
      ],
    }, {
      label: 'resource_admin.cards.resource_info',
      fields: [
        'resource_name',
        'resource.id',
      ],
    }],
  },
});
