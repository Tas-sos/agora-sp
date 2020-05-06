import DS from 'ember-data';
import { shorten } from '../utils/common/common';
import { countries } from '../resources';
import ENV from '../config/environment';

const {
  get,
  computed,
} = Ember;


export default DS.Model.extend({
  name: DS.attr({
    label: 'provider.fields.name',
    hint: 'provider.hints.name'
  }),
  description: DS.attr({
    label: 'provider.fields.description',
    hint: 'provider.hints.description'
  }),
  logo: DS.attr({
    label: 'provider.fields.logo',
    hint: 'provider.hints.logo'
  }),
  contact: DS.attr({
    label: 'provider.fields.contact',
    hint: 'provider.hints.contact',
  }),
  pd_bai_3_legal_entity: DS.attr({
    type: 'boolean',
    defaultValue: false,
    label: 'provider.fields.pd_bai_3_legal_entity',
    hint: 'provider.hints.pd_bai_3_legal_entity',
  }),
  pd_bai_0_id: DS.attr({
    label: 'provider.fields.pd_bai_0_id',
    hint: 'provider.hints.pd_bai_0_id',
  }),
  pd_bai_1_name: DS.attr({
    label: 'provider.fields.pd_bai_1_name',
    hint: 'provider.hints.pd_bai_1_name',
  }),
  pd_bai_2_abbreviation: DS.attr({
    label: 'provider.fields.pd_bai_2_abbreviation',
    hint: 'provider.hints.pd_bai_2_abbreviation',
  }),
  pd_bai_3_legal_status: DS.attr({
    type: 'select',
    choices: ENV.APP.resources.LEGAL_STATUSES,
    label: 'provider.fields.pd_bai_3_legal_status',
    hint: 'provider.hints.pd_bai_3_legal_status',
  }),
  pd_bai_4_website: DS.attr({
    label: 'provider.fields.pd_bai_4_website',
    hint: 'provider.hints.pd_bai_4_website',
  }),
  // location information
  pd_loi_1_street_name_and_number: DS.attr({
    label: 'provider.fields.pd_loi_1_street_name_and_number',
    hint: 'provider.hints.pd_loi_1_street_name_and_number',
  }),
  pd_loi_2_postal_code: DS.attr({
    label: 'provider.fields.pd_loi_2_postal_code',
    hint: 'provider.hints.pd_loi_2_postal_code',
  }),
  pd_loi_3_city: DS.attr({
    label: 'provider.fields.pd_loi_3_city',
    hint: 'provider.hints.pd_loi_3_city',
  }),
  pd_loi_4_region: DS.attr({
    label: 'provider.fields.pd_loi_4_region',
    hint: 'provider.hints.pd_loi_4_region',
  }),
  pd_loi_5_country_or_territory: DS.attr({
  type: 'select',
  // Quickly bake an appropriate select-friendly array from original countries resource
  choices: function () {
    let countrySel = []
    for (let country of countries) {
      countrySel.push([country.toLowerCase(), country]);
    }
    return countrySel;
  }(),
  label: 'provider.fields.pd_loi_5_country_or_territory',
  hint: 'provider.hints.pd_loi_5_country_or_territory',
  }),
  // marketing information
  pd_mri_1_description: DS.attr({
    label: 'provider.fields.pd_mri_1_description',
    hint: 'provider.hints.pd_mri_1_description',
  }),
  pd_mri_2_logo: DS.attr({
    label: 'provider.fields.pd_mri_2_logo',
    hint: 'provider.hints.pd_mri_2_logo',
  }),
  pd_mri_3_multimedia: DS.attr({
    label: 'provider.fields.pd_mri_3_multimedia',
    hint: 'provider.hints.pd_mri_3_multimedia',
  }),
  // computed
  short_desc: computed('description', function() {
    return shorten(get(this, 'description'));
  }),
  pd_mti_1_life_cycle_status: DS.attr({
    type: 'select',
    choices: ENV.APP.resources.PROVIDER_LIFE_CYCLE_STATUSES,
    label: 'provider.fields.pd_mti_1_life_cycle_status',
    hint: 'provider.hints.pd_mti_1_life_cycle_status',
  }),
  // maturity information
  pd_mti_2_certifications: DS.attr({
    label: 'provider.fields.pd_mti_2_certifications',
    hint: 'provider.hints.pd_mti_2_certifications',
  }),
  // contact information
  main_contact: DS.belongsTo('contact-information', {
    label: 'provider.fields.main_contact',
    hint: 'provider.hints.main_contact',
    inverse: null
  }),
  public_contact: DS.belongsTo('contact-information', {
    label: 'provider.fields.public_contact',
    hint: 'provider.hints.public_contact',
    inverse: null
  }),
  // other information
  pd_oth_3_affiliations: DS.hasMany('affiliation', {
    label: 'provider.fields.pd_oth_3_affiliations',
    hint: 'provider.hints.pd_oth_3_affiliations',
  }),
  affiliation_names: DS.attr({
    label: 'provider.fields.affiliation_names',
  }),
  pd_oth_4_networks: DS.hasMany('network', {
    label: 'provider.fields.pd_oth_4_networks',
    hint: 'provider.hints.pd_oth_4_networks',
  }),
  network_names: DS.attr({
    label: 'provider.fields.network_names',
  }),
  pd_oth_5_structure_type: DS.hasMany('structure', {
    label: 'provider.fields.pd_oth_5_structure_type',
    hint: 'provider.hints.pd_oth_5_structure_type',
  }),
  structure_names: DS.attr({
    label: 'provider.fields.structure_names',
  }),

  __api__: {
    serialize: function(hash, _) {
      // do not send readonly keys to backend
      delete hash['affiliation_names'];
      delete hash['network_names'];
      delete hash['structure_names'];
      return hash;
    },
  },




});
