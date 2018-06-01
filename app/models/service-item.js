import DS from 'ember-data';
import Ember from 'ember';
import { shorten } from '../utils/common/common';

export default DS.Model.extend({
  name: DS.attr(),
  service_type: DS.attr(),
  funders_for_service: DS.attr(),
  description_external: DS.attr(),
  value_to_customer: DS.attr(),
  risks: DS.attr(),
  description_internal: DS.attr(),
  short_description: DS.attr(),
  competitors: DS.attr(),
  logo: DS.attr(),
  request_procedures: DS.attr(),
  customer_facing: DS.attr({
    type: 'boolean',
    label: 'service_item.fields.customer_facing',
    defaultValue: true,
  }),
  internal: DS.attr({
    type: 'boolean',
    label: 'service_item.fields.internal',
    defaultValue: false,
  }),
  service_version_url: Ember.computed('id', function() {
    return `/service-versions/create?service=${Ember.get(this, 'id')}`;
  }),
  service_area: DS.belongsTo('service-area', {
    formAttrs: {
      optionLabelAttr: 'name',
    },
  }),
  id_contact_information: DS.belongsTo('contact-information', {
    formAttrs: {
      optionLabelAttr: 'full_name',
    },
  }),
  id_contact_information_internal: DS.belongsTo('contact-information', {
    formAttrs: {
      optionLabelAttr: 'full_name',
    },
  }),
  service_trl: DS.belongsTo('service-trl', {
    formAttrs: {
      optionLabelAttr: 'value',
    },
  }),
  // computed
  short_desc: Ember.computed('short_description', function() {
    return shorten(Ember.get(this, 'short_description'));
  }),
  service_owners_ids: DS.attr(),
  __api__: {
    path: 'services',
  },
});
