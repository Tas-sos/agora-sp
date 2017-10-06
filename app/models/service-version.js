import DS from 'ember-data';

export default DS.Model.extend({
  id_service: DS.belongsTo('service-item'),
  privacy_policy_has: DS.attr(),
  privacy_policy_url: DS.attr(),
  monitoring_has: DS.attr(),
  monitoring_url: DS.attr(),
  user_documentation_has: DS.attr(),
  user_documentation_url: DS.attr(),
  decommissioning_procedure_has: DS.attr(),
  decommissioning_procedure_url: DS.attr(),
  accounting_has: DS.attr(),
  accounting_url: DS.attr(),
  operations_documentation_has: DS.attr(),
  operations_documentation_url: DS.attr(),
  business_continuity_has: DS.attr(),
  business_continuity_url: DS.attr(),
  disaster_recovery_plan_has: DS.attr(),
  disaster_recovery_plan_url: DS.attr(),
  usage_policy_has: DS.attr(),
  usage_policy_url: DS.attr(),
  features_current: DS.attr(),
  cost_to_run: DS.attr(),
  version: DS.attr(),
  cost_to_build: DS.attr(),
  use_cases: DS.attr(),
  is_in_catalogue: DS.attr(),
  status: DS.belongsTo('service-status'),
});
