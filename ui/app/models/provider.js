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
    autocomplete: true,
    choices: ENV.APP.resources.LEGAL_STATUSES,
    label: 'provider.fields.pd_bai_3_legal_status',
    hint: 'provider.hints.pd_bai_3_legal_status',
  }),
  pd_bai_4_website: DS.attr({
    label: 'provider.fields.pd_bai_4_website',
    hint: 'provider.hints.pd_bai_4_website',
  }),
  // classification information
  pd_cli_1_scientific_domain: DS.hasMany('domain', {
    label: 'provider.fields.pd_cli_1_scientific_domain',
    hint: 'provider.hints.pd_cli_1_scientific_domain',
  }),
  domain_names: DS.attr({
    label: 'provider.fields.domain_names',
  }),
  // TODO: Filter subdomain's ManyArray results according to domain selections
  pd_cli_2_scientific_subdomain: DS.hasMany('subdomain', {
    label: 'provider.fields.pd_cli_2_scientific_subdomain',
    hint: 'provider.hints.pd_cli_2_scientific_subdomain',
  }),
  subdomain_names: DS.attr({
    label: 'provider.fields.subdomain_names',
  }),
  pd_cli_3_tags: DS.attr({
    label: 'provider.fields.pd_cli_3_tags',
    hint: 'provider.hints.pd_cli_3_tags',
    //formComponent: 'agora-chips',
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
    autocomplete: true,
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
    autocomplete: true,
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
  pd_oth_1_hosting_legal_entity: DS.attr({
    label: 'provider.fields.pd_oth_1_hosting_legal_entity',
    hint: 'provider.hints.pd_oth_1_hosting_legal_entity',
  }),
  pd_oth_2_participating_countries: DS.attr({
    defaultValue: 'Europe',
    label: 'provider.fields.pd_oth_2_participating_countries',
    hint: 'provider.hints.pd_oth_2_participating_countries',
    formComponent: 'agora-chips',
    formAttrs: {
      options: countries,
      exactMatch: true,
    }
  }),
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
  pd_oth_6_esfri_domain: DS.hasMany('esfridomain', {
    autocomplete: true,
    label: 'provider.fields.pd_oth_6_esfri_domain',
    hint: 'provider.hints.pd_oth_6_esfri_domain',
  }),
  esfridomain_names: DS.attr({
    label: 'provider.fields.esfridomain_names',
  }),
  pd_oth_7_esfri_type: DS.belongsTo('esfritype', {
    autocomplete: true,
    label: 'provider.fields.pd_oth_7_esfri_type',
    hint: 'provider.hints.pd_oth_7_esfri_type',
    //inverse: null,
    formAttrs: {
      optionLabelAttr: 'name',
    },
  }),
  pd_oth_8_areas_of_activity: DS.hasMany('activity', {
    label: 'provider.fields.pd_oth_8_areas_of_activity:',
    hint: 'provider.hints.pd_oth_8_areas_of_activity:',
  }),
  activity_names: DS.attr({
    label: 'provider.fields.activity_names',
  }),
  pd_oth_9_societal_grand_challenges: DS.hasMany('challenge', {
    label: 'provider.fields.pd_oth_9_societal_grand_challenges',
    hint: 'provider.hints.pd_oth_9_societal_grand_challenges',
  }),
  challenge_names: DS.attr({
    label: 'provider.fields.challenge_names',
  }),
  pd_oth_10_national_roadmaps: DS.attr({
    label: 'provider.fields.pd_oth_10_national_roadmaps',
    hint: 'provider.hints.pd_oth_10_national_roadmaps',
  }),

  __api__: {
    serialize: function(hash, _) {
      // do not send readonly keys to backend
      delete hash['affiliation_names'];
      delete hash['network_names'];
      delete hash['structure_names'];
      delete hash['esfridomain_names'];
      delete hash['activity_names'];
      delete hash['challenge_names'];
      delete hash['domain_names'];
      delete hash['subdomain_names'];
      return hash;
    },
  },




});
