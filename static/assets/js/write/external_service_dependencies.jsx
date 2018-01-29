
var formName = 'External Service Dependencies Form';


var opType;
var serviceId;
var serviceDependencyId;
var newServiceId;
var newServiceName;
var newServiceDependencyId;
var newServiceDependencyName;
var globalServiceData;
var globalExternalServiceData;

var optionsData = [
  {id: 1, value: 1, text: "option 1"},
  {id: 2, value: 2, text: "option 2"},
	{id: 3, value: 3, text: "option 3"}
];

var resourceObject = [
	{ tag: 'input', type: 'text', name: 'service_id', placeholder: 'Enter service name', label: 'Service' },
	{ tag: 'input', type: 'text', name: 'service_dependency_id', placeholder: 'Enter external service dependency name', label: 'Service dependency' },
	{ tag: 'button', name: 'btn-service_dependency_id', value: 'Add external service' }
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
		if(service == '' || service == null){
			validationMessage = "The service is required";
			validationObjects.push( { field: 'service_id', message: validationMessage } );
		}

		var externalDependency = $("#service_dependency_id").val();
		if(externalDependency == '' || externalDependency == null){
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

			if(newServiceName != service_id){
				if(newServiceName != null || service_id != "")
				{
					newServiceName = null;
					newServiceId = null;
					for(var i = 0; i < globalServiceData.length; i++){
						if(service_id == globalServiceData[i].name){
							newServiceId = globalServiceData[i].uuid;
							newServiceName = service_id;
							break;
						}
					}
				}
			}

			var service_dependency_id =  $("#service_dependency_id").val();

			if(newServiceDependencyName != service_dependency_id){
				if(newServiceDependencyName != null || service_dependency_id != "")
				{
					newServiceDependencyName = null;
					newServiceDependencyId = null;
					for(var i = 0; i < globalExternalServiceData.length; i++){
						if(service_dependency_id == globalExternalServiceData[i].name){
							newServiceDependencyId = globalExternalServiceData[i].id;
							newServiceDependencyName = service_dependency_id;
							break;
						}
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
				headers: {"X-CSRFToken": $("input[name=csrfmiddlewaretoken]")[0].value },
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

        if(this.props.source == null || this.props.source == "")
            return;

        jQuery.support.cors = true;
        this.serverRequest = $.ajax({
            url: this.props.source,
            dataType: "json",
            crossDomain: true,
            type: "GET",
            cache: false,
            success: function (data) {
                this.setState({external_dependency: data.data});
                $("#service_id").val(this.state.external_dependency.service.name);
                $("#service_dependency_id").val(this.state.external_dependency.external_service.name);
				serviceId = this.state.external_dependency.service.uuid;
				newServiceName = this.state.external_dependency.service.name;
				serviceDependencyId = this.state.external_dependency.external_service.uuid;
				newServiceDependencyName = this.state.external_dependency.external_service.name;
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




$( function() {

	$("#btn-service_dependency_id").click(function(e){
		e.preventDefault();
		var url = window.location.href;
        var contents = url.split("/");
        var host = contents[0] + "//" + contents[2];

		window.open(host + "/ui/service/external", "_blank");
	});


	var temp = null;
	$(document).bind('click', function (event) {
        // Check if we have not clicked on the search box
        if (!($(event.target).parents().andSelf().is('#service_id'))) {
			$(".ui-menu-item").remove();
		}

		if (!($(event.target).parents().andSelf().is('#service_dependency_id'))) {
			$(".ui-menu-item").remove();
		}
	});


	var getDataService = function(request, response){

        var url = window.location.href;
        var contents = url.split("/");
        var host = contents[0] + "//" + contents[2];

        $.getJSON(
            host + "/api/v1/services/all?search=" + request.term,
            function (data) {
				for(var i = 0; i < data.data.length; i++) {
					data.data[i].value = data.data[i].name;
					data.data[i].label = data.data[i].name;
                    data.data[i].index = i;
				}
				globalServiceData = data.data;
                response(data.data);
            });
	};

	var getDataExternalService = function(request, response){

        var url = window.location.href;
        var contents = url.split("/");
        var host = contents[0] + "//" + contents[2];

        $.getJSON(
            host + "/api/v1/services/external/all?search=" + request.term,
            function (data) {
				for(var i = 0; i < data.data.length; i++) {
					data.data[i].value = data.data[i].name;
					data.data[i].label = data.data[i].name;
                    data.data[i].index = i;
				}
				globalExternalServiceData = data.data;
                response(data.data);
            });
	};



    $( "#service_id" ).autocomplete({
      source: getDataService,
      minLength: 2,
      select: function( event, ui ) {
		this.value = ui.item.name;
		newServiceId = ui.item.uuid;
		newServiceName = ui.item.name;
		$(".ui-autocomplete").hide();
		$(".ui-menu-item").remove();
      },
	  focus: function(event, ui){
          var items = $(".ui-menu-item");
		  items.removeClass("ui-menu-item-hover");
		  $(items[ui.item.index]).addClass("ui-menu-item-hover");
	  }
    }).autocomplete( "instance" )._renderItem = function( ul, item ) {
		return $( "<li>" )
        .append( item.name )
        .appendTo( ul );
    };


	$( "#service_dependency_id" ).autocomplete({
      source: getDataExternalService,
      minLength: 2,
      select: function( event, ui ) {
		this.value = ui.item.name;
		newServiceDependencyId = ui.item.id;
		newServiceDependencyName = ui.item.name;
		$(".ui-autocomplete").hide();
		$(".ui-menu-item").remove();
      },
	  focus: function(event, ui){
          var items = $(".ui-menu-item");
		  items.removeClass("ui-menu-item-hover");
		  $(items[ui.item.index]).addClass("ui-menu-item-hover");
	  }
    }).autocomplete( "instance" )._renderItem = function( ul, item ) {
		return $( "<li>" )
        .append( item.name )
        .appendTo( ul );
    };




  } );