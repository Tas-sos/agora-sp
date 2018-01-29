
var formName = 'External Service Dependencies Form';


var opType;
var serviceId;
var serviceDependencyId;
var newServiceId;
var newServiceDependencyId;
var globalServiceData;
var globalExternalServiceData;

var optionsServiceData = [
  {id: 1, value: -1, text: "Select service"}
];

var optionsData = [
  {id: 1, value: -1, text: "Select external service dependency"}
];

var resourceObject = [
	{ tag: 'select', type: 'text', name: 'service_id', placeholder: 'Enter service name', label: 'Service', optionsData: optionsServiceData },
	{ tag: 'select', type: 'text', name: 'service_dependency_id', placeholder: 'Enter external service dependency name', label: 'Service dependency', optionsData: optionsData },
	{tag: 'button', type: 'button', name: 'add-external', label: 'Add external service', value: "Add external service"}
];

var OptionsComponent = React.createClass({
	render: function(){
		var htmlOptions = this.props.options.map(function(option) {
      return(
      	<option value={option.value} key={option.id}>{option.text}</option>
      );
		});		
		return (
			<select name={this.props.selectName} id={this.props.selectName} className="form-control">
				{htmlOptions}
		  </select>
		);
	}
});

var parameter = getParameterByName("serviceId", window.location);
if(parameter != null) {
	serviceId = parameter;
	newServiceId = parameter;
	jQuery.support.cors = true;
        $.ajax({
            url: $("#host")[0].value + "/api/v1/portfolio/services/" + serviceId,
			headers: {
				"X-CSRFToken": $("input[name=csrfmiddlewaretoken]")[0].value,
				"AUTH_TOKEN": localStorage.apiToken,
				"EMAIL": localStorage.apiEmail
			},
            dataType: "json",
            crossDomain: true,
            type: "GET",
            cache: false,
            success: function (response) {
				var name = response.data.name;

				var service = $("#service_id");
				var optionsCount = $("#service_id>option").length;
				if(optionsCount <= 1){
					var option = $('<option></option>').attr("value", name)
							.text(name);
						service.append(option);
				}
				service.val(name).change();
            },
            error: function (xhr, status, err) {
            }
        });
}

var FormWrapper = React.createClass({

	generateFormElements: function(resourceObject){
		var formElements = resourceObject.map(function(field, i){
			if(field.tag == 'input'){
				if(field.type == 'text'){					
					return (
						<div className="form-group" key={i}>
			      	        <label htmlFor={field.name}>{field.label}</label>
			      	        <input className="form-control" id={field.name} type={field.type} name={field.name} placeholder={field.placeholder} aria-describedby={field.name + '-error'} />
							<span id={field.name + '-error'} className="validation-message sr-only"></span>
			      	    </div>
					);
				}
			}
			else if(field.tag == 'textarea'){
				return(
					<div className="form-group" key={i}>
					    <label htmlFor={field.name}>{field.label}</label>
					    <textarea className="form-control" id={field.name} name={field.name} rows="6"></textarea>
					    <span id={field.name + '-error'} className="validation-message sr-only"></span>
					</div>
				);				
			}
			else if(field.tag == 'select'){
				return(
					<div className="form-group">
					    <label htmlFor={field.name}>{field.label}</label>
					    <OptionsComponent options={field.optionsData} selectName={field.name}></OptionsComponent>
					    <span id={field.name + '-error'} className="validation-message sr-only"></span>
					</div>
				);				
			}
			else if(field.tag == 'button'){
				return (
					<div className="form-group" key={i}>
			      	        <button value={field.value} className="btn btn-purple" id={"btn-" + field.name}>{field.value}</button>

			      	    </div>
				)
			}
		}, this);
		return formElements;
	},

	markInvalid: function(elRef, message){
		$('#' + elRef).next().removeClass('sr-only');
		$('#' + elRef).next().html(message);
		$('#' + elRef).parent().addClass('has-error');
		$('html, body').animate({
        scrollTop: $('#' + elRef).offset().top
    	}, 800);
	},

	clearValidations: function(){
		$('body').find('.has-error').removeClass('has-error');
		$('body').find('.validation-message').addClass('sr-only');
	},

	validateForm: function(e){
		this.clearValidations();
		var validationObjects = [];
		var validationMessage = ''

		var service = $("#service_id").val();
		if(service == '' || service == null || service == -1){
			validationMessage = "The service is required";
			validationObjects.push( { field: 'service_id', message: validationMessage } );
		}

		var externalDependency = $("#service_dependency_id").val();
		if(externalDependency == '' || externalDependency == null || externalDependency == -1){
			validationMessage = "The external dependency is required";
			validationObjects.push( { field: 'service_dependency_id', message: validationMessage } );
		}

		if(validationObjects.length > 0){
			var i = 0;
			for (i = 0; i < validationObjects.length; i++) {
			    this.markInvalid(validationObjects[i].field, validationObjects[i].message);
			}
			return false;
		}

		return true;
	},

	handleSubmit: function(e) {
		// some validation
		// ajax url call + redirect
		e.preventDefault();

		if(this.validateForm()){			
			//var formValues = JSON.stringify($("#service-form").serializeJSON());
			//console.log("The form values are ->", formValues);

			var service_id =  $("#service_id").val();

			if(service_id != "")
			{
				newServiceId = null;
				for(var i = 0; i < globalServiceData.length; i++){
					if(service_id == globalServiceData[i].name){
						newServiceId = globalServiceData[i].uuid;
						break;
					}
				}
			}


			var service_dependency_id =  $("#service_dependency_id").val();

			if(service_dependency_id != "")
			{
				newServiceDependencyId = null;
				for(var i = 0; i < globalExternalServiceData.length; i++){
					if(service_dependency_id == globalExternalServiceData[i].name){
						newServiceDependencyId = globalExternalServiceData[i].id;
						break;
					}
				}
			}



			var params = {};

			var parts = window.location.href.split("/");
			var host = "https://" + parts[2];
			var url = "";

			if (this.props.source != null && this.props.source != "") {

				params["external_service_dependency"] = serviceDependencyId;
				params["new_external_service_dependency"] = newServiceDependencyId;
				params["service_id"] = serviceId;

				url = host + "/api/v1/services/" + newServiceId + "/service_external_dependencies/edit";
				opType = "edit";
			}
			else {

				params["external_service_dependency"] = newServiceDependencyId;

				url = host + "/api/v1/services/" + newServiceId + "/service_external_dependencies/add";
				opType = "add";
			}

			this.serverRequest = $.ajax({
				url: url,
				headers: {
					"X-CSRFToken": $("input[name=csrfmiddlewaretoken]")[0].value,
					"AUTH_TOKEN": localStorage.apiToken,
					"EMAIL": localStorage.apiEmail
				},
				dataType: "json",
				crossDomain: true,
				type: "POST",
				contentType: "application/json",
				cache: false,
				data: JSON.stringify(params),
				success: function (data) {
					if (opType == "add")
						$("#modal-success-body").text("You have successfully inserted a new external service dependency");
					else {
						serviceId = newServiceId;
						serviceDependencyId = newServiceDependencyId;
						$("#modal-success-body").text("You have successfully updated the external service dependency");
					}
					$("#modal-success").modal('show');
				}.bind(this),
				error: function (xhr, status, err) {
					var response = JSON.parse(xhr.responseText);
					$("#modal-body").text(response.errors.detail);
					$("#modal-danger").modal('show');
				}.bind(this)
			});
		}
		else{
		}	
	},

	getInitialState: function () {
		return {
			external_dependency: {
				service: {},
				external_service: {}
			}
		}
	},

    componentDidMount: function () {


		jQuery.support.cors = true;
		var url = window.location.href;
        var contents = url.split("/");
        var host = contents[0] + "//" + contents[2];

		$.getJSON(
            host + "/api/v1/services/all",
            function (data) {
				var service = $("#service_id");
				var current = service.val();

				if(current != -1){
					$("#service_id option[value='" + current + "']").remove();
				}
				for(var i = 0; i < data.data.length; i++) {
					var option = $('<option></option>').attr("value", data.data[i].name).text(data.data[i].name);
					service.append(option);

				}
				if(current != -1)
					service.val(current).change();

				globalServiceData = data.data;

            });

		$.getJSON(
            host + "/api/v1/services/external/all",
            function (data) {
				var service_dependency = $("#service_dependency_id");
				var current = service_dependency.val();

				if(current != -1){
					$("#service_dependency_id option[value='" + current + "']").remove();
				}
				for(var i = 0; i < data.data.length; i++) {
					var option = $('<option></option>').attr("value", data.data[i].name).text(data.data[i].name);
					service_dependency.append(option);

				}
				if(current != -1)
					service_dependency.val(current).change();

				globalExternalServiceData = data.data;

            });


        if(this.props.source == null || this.props.source == "")
            return;

        this.serverRequest = $.ajax({
            url: this.props.source,
			headers: {
				"X-CSRFToken": $("input[name=csrfmiddlewaretoken]")[0].value,
				"AUTH_TOKEN": localStorage.apiToken,
				"EMAIL": localStorage.apiEmail
			},
            dataType: "json",
            crossDomain: true,
            type: "GET",
            cache: false,
            success: function (data) {
                this.setState({external_dependency: data.data});

				var service = $("#service_id");
				var optionsCount = $("#service_id>option").length;
				if(optionsCount <= 1){
					var option = $('<option></option>').attr("value", this.state.external_dependency.service.name)
							.text(this.state.external_dependency.service.name);
						service.append(option);
				}
				service.val(this.state.external_dependency.service.name).change();


				var service_dependency = $("#service_dependency_id");
				optionsCount = $("#service_dependency_id>option").length;
				if(optionsCount <= 1){
					var option = $('<option></option>').attr("value", this.state.external_dependency.external_service.name)
							.text(this.state.external_dependency.external_service.name);
						service_dependency.append(option);
				}
				service_dependency.val(this.state.external_dependency.external_service.name).change();

				serviceId = this.state.external_dependency.service.uuid;
				serviceDependencyId = this.state.external_dependency.external_service.uuid;
				newServiceId = serviceId;
				newServiceDependencyId = serviceDependencyId;
            }.bind(this),
            error: function (xhr, status, err) {
                console.log(this.props.source, status, err.toString());
            }.bind(this)
        });
    },

    componentWillUnmount: function () {
        this.serverRequest.abort();
    },

	render: function(){		
		var formElements = this.generateFormElements(this.props.resourceObject);
		return(
			<div className="widget">
					<div className="widget-header bordered-bottom bordered-blue">
			     	<span className="widget-caption">{this.props.formName}</span>
			    </div>
			    <div className="widget-body">
			    	<form role="form" onSubmit={this.handleSubmit} id="service-form">
			    		{formElements}
			    		<button type="submit" className="btn btn-blue">Submit</button>
			    	</form>
			   	</div>
			</div>
		);
	}
});

ReactDOM.render(
  <FormWrapper resourceObject={resourceObject} formName={formName} source={$("#source")[0].value}/>,
  document.getElementById('write-content')
);

$(function(){
	$("#btn-add-external").click(function(){
		window.open("/ui/service/external", "_blank");
	});
});