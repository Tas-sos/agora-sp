
var formName = 'Service Component Implementation Form';

var componentId = null;
var componentImplementationId = null;
var opType = "";
var globalData;

var optionsData = [
  {id: 1, value: -1, text: "Select component"}
];

var resourceObject = [
	{ tag: 'input', type: 'text', name: 'name', placeholder: 'Enter name', label: 'Name' },
	{ tag: 'textarea', type: 'textarea', name: 'description', label: 'Description', placeholder: "Enter description", onChange: 'textareaHTMLValidation' },
	{tag: 'button', type: 'button', name: 'edit-description', label: 'Edit', value: "Edit"},
	{ tag: 'select', type: 'text', name: 'component_id', label: 'Component', placeholder: "Enter component name", optionsData: optionsData }
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
//
var parameter = getParameterByName("componentId", window.location);
if(parameter != null) {
	componentId = parameter;
	jQuery.support.cors = true;
        $.ajax({
            url: $("#host")[0].value + "/api/v1/component/" + componentId,
			headers: {
				"X-CSRFToken": $("input[name=csrfmiddlewaretoken]")[0].value,
				"AUTHTOKEN": localStorage.apiToken,
				"EMAIL": localStorage.apiEmail
			},
            dataType: "json",
            crossDomain: true,
            type: "GET",
            cache: false,
            success: function (response) {

				var name = response.data.name;

				var component = $("#component_id");
				var optionsCount = $("#component_id>option").length;
				if(optionsCount <= 1){
					var option = $('<option></option>').attr("value", name)
							.text(name);
						component.append(option);
				}
				component.val(name).change();
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
					    <textarea className="form-control" id={field.name} name={field.name} placeholder={field.placeholder} rows="6" onChange={this[field.onChange]}></textarea>
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

	textareaHTMLValidation: function(e){
		var div = document.createElement('div');
		div.innerHTML = $(e.target).val();
		if($(div).find('script').length > 0 || $(div).find('link').length){
			div = null;
			this.markInvalid($(e.target).attr('name'), 'This HTML content must not have script or css tags');
		}
		else{
			$(e.target).parent().removeClass('has-error');
			$(e.target).parent().find('.validation-message').addClass('sr-only');
		}
		div = null
	},

	validateForm: function(e){
		this.clearValidations();
		var validationObjects = [];
		var validationMessage = '';

		// --- validation code goes here ---
		if($('#name').val() == ''){
			validationMessage = "The name is required";
			validationObjects.push( { field: 'name', message: validationMessage } );
		}
		if($('#name').val().length > 255){
			validationMessage = "Content exceeds max length of 255 characters.";
			validationObjects.push( { field: 'name', message: validationMessage } );			
		}

		var comp_id = $('#component_id').val();
		if(comp_id == null || comp_id == "" || comp_id == -1){
			validationMessage = "The component is required.";
			validationObjects.push( { field: 'component_id', message: validationMessage } );
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

			var component_id =  $("#component_id").val();

			if(component_id != "")
			{
				componentId = null;
				for(var i = 0; i < globalData.length; i++){
					if(component_id == globalData[i].name){
						componentId = globalData[i].uuid;
						break;
					}
				}
			}



			var params = {};
			params["name"] = $("#name").val();
			params["description"] = $("#description").val();
			params["component_uuid"] = componentId;


			var parts = window.location.href.split("/");
			var host = "https://" + parts[2];
			var url = "";

			if(this.props.source != null && this.props.source != ""){
				params["uuid"] = parts[parts.length - 1];
				url = host + "/api/v1/component/service_component_implementation/edit";
				opType = "edit";
			}
			else {
				url = host + "/api/v1/component/service_component_implementation/add";
				opType = "add";
			}

			this.serverRequest = $.ajax({
				url: url,
				headers: {
					"X-CSRFToken": $("input[name=csrfmiddlewaretoken]")[0].value,
					"AUTHTOKEN": localStorage.apiToken,
					"EMAIL": localStorage.apiEmail
				},
				dataType: "json",
				crossDomain: true,
				type: "POST",
				contentType:"application/json",
				cache: false,
				data: JSON.stringify(params),
				success: function (data) {
					if(opType == "add")
						$("#modal-success-body").text("You have successfully inserted a new component implementation");
					else
						$("#modal-success-body").text("You have successfully updated the component implementation");
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


	render: function(){		
		var formElements = this.generateFormElements(this.props.resourceObject);
		return(
			<div className="widget">

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

var ImplementationDetailsTable = React.createClass({


	getInitialState: function () {
		return {
			implementationsDetails: [],
			count: 0,
			selected: 0
		}
	},

	render: function() {

		var array = [];
		for(var i = 0; i < this.state.count; i++)
			array.push(i);

		return (
			<div className="row">
				<div className="col-xs-12">
					<div className="well with-header  with-footer">
						<div className="form-group">
			      	        <button value="Add component implementation details" id="add-imp-det" className="btn btn-purple">Add component implementation details</button>
			      	    </div>
						<table className="table table-hover">
							<thead className="bordered-darkorange">
								<tr>
									<th>
										Version
									</th>
									<th>
										Configuration Parameters
									</th>

									<th>

									</th>
								</tr>
							</thead>
							<tbody>

							{this.props.implementationsDetails.map(function (implementation) {
								return (
									<tr key={implementation.version}>
										<td>{implementation.version}</td>
										<td>{implementation.configuration_parameters}</td>
										<td><a href={"/ui/component/implementation_detail/" + implementation.uuid}>Edit</a></td>
									</tr>
								)
							})}

							</tbody>

						</table>

						<div className="col-xs-hidden col-sm-6"></div>
							<div className="col-xs-12 col-sm-6">
								<div className="dataTables_paginate paging_bootstrap" id="simpledatatable_paginate">

								</div>
							</div>

					</div>

				</div>

			</div>
		);
	}
});

var Tabs = React.createClass({

	getInitialState: function () {
		return {
			component_implementation: {
				name: "",
				description: ""
			},
			implementationsDetails: []
		}
	},

    componentDidMount: function () {


		jQuery.support.cors = true;
		var url = window.location.href;
        var contents = url.split("/");
        var host = contents[0] + "//" + contents[2];

		$.getJSON(
            host + "/api/v1/component/all",
            function (data) {
				var component_id = $("#component_id");
				var current = component_id.val();

				if(current != -1){
					$("#component_id option[value='" + current + "']").remove();
				}
				for(var i = 0; i < data.data.length; i++) {
					var option = $('<option></option>').attr("value", data.data[i].name).text(data.data[i].name);
					component_id.append(option);

				}
				if(current != -1)
					component_id.val(current).change();

				globalData = data.data;

            });


		if(this.props.source == null || this.props.source == "")
            return;

		this.serverRequest = $.ajax({
            url: this.props.source,
			headers: {
				"X-CSRFToken": $("input[name=csrfmiddlewaretoken]")[0].value,
				"AUTHTOKEN": localStorage.apiToken,
				"EMAIL": localStorage.apiEmail
			},
            dataType: "json",
            crossDomain: true,
            type: "GET",
            cache: false,
            success: function (data) {
				this.setState({component_implementation: data.data});
                $("#name").val(this.state.component_implementation.name);
                $("#description").val(this.state.component_implementation.description);
				componentId = this.state.component_implementation.component.uuid;
				componentImplementationId = this.state.component_implementation.uuid;

				this.setState({implementationsDetails: this.state.component_implementation.component_implementation_details_list.component_implementation_details});

				var component = $("#component_id");
				var optionsCount = $("#component_id>option").length;
				if(optionsCount <= 1){
					var option = $('<option></option>').attr("value", this.state.component_implementation.component.name)
							.text(this.state.component_implementation.component.name);
						component.append(option);
				}
				component.val(this.state.component_implementation.component.name).change();
            }.bind(this),
            error: function (xhr, status, err) {
            }.bind(this)
        });
    },

    componentWillUnmount: function () {
        this.serverRequest.abort();
    },

	render: function() {
		return (
			<div className="row">
				<div>
					<div className="widget flat radius-bordered">
						<div className="widget-header bg-themeprimary">
							<span className="widget-caption">Component Implementation</span>
						</div>

						<div className="widget-body">
							<div className="widget-main ">
								<div className="tabbable">
									<ul className="nav nav-tabs tabs-flat" id="myTab11">
										<li className="active">
											<a data-toggle="tab" href="#home11">
												Component Implementation
											</a>
										</li>
										<li>
											<a data-toggle="tab" href="#profile12">
												Implementations Details
											</a>
										</li>
									</ul>
									<div className="tab-content tabs-flat">
										<div id="home11" className="tab-pane in active">
											<FormWrapper resourceObject={resourceObject} formName={formName} source={this.props.source} />
										</div>

										<div id="profile12" className="tab-pane">
											<ImplementationDetailsTable implementationsDetails={this.state.implementationsDetails} />
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
				<div className="col-lg-6 col-sm-6 col-xs-12">
				</div>
			</div>
		);
	}
});


ReactDOM.render(
  <Tabs source={$("#source")[0].value} />,
  document.getElementById('write-content')
);

$(function(){

	$("#add-imp-det").click(function () {
		window.open("/ui/component/implementation_detail?componentId=" + componentId + "&componentImplementationId=" + componentImplementationId, "_blank");
	});

	$("#btn-edit-description").click(function(e){
		e.preventDefault();
		tinymce.init({
			selector:'#rich-edit',
			height: 250,
			plugins: "advlist"
		});
		tinymce.get('rich-edit').setContent($("#description").val());
		$("#modal-rich-html").modal('show');
	});

	$("#confirm-edit").click(function () {
		$("#description").val(tinymce.get('rich-edit').getContent());
	});

});