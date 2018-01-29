var formName = 'Service Form';

var opType;
var serviceOwnerId;
var serviceOwnerName;
var internalContactInformationId;
var internalContactInformationName;
var externalContactInformationId;
var externalContactInformationName;

var globalOwnerData;
var globalInternalContactData;
var globalExternalContactData;

var optionsData = [
  {id: 1, value: 1, text: "option 1"},
  {id: 2, value: 2, text: "option 2"},
	{id: 3, value: 3, text: "option 3"}
];

var resourceObject = [
	{ tag: 'input', type: 'text', name: 'name', placeholder: 'Enter name', label: 'Name', required: true },
	{ tag: 'textarea', type: 'textarea', name: 'description_external', placeholder: "Enter external description", label: 'External Description', required: true, onChange: 'textareaHTMLValidation' },
	{ tag: 'textarea', type: 'textarea', name: 'description_internal', placeholder: "Enter internal description", label: 'Internal Description', required: true, onChange: 'textareaHTMLValidation' },
	{ tag: 'input', type: 'text', name: 'service_area', placeholder: 'Enter service area', label: 'Service Area', required: true },
	{ tag: 'input', type: 'text', name: 'service_type', placeholder: 'Enter service type', label: 'Service Type', required: true },
	{ tag: 'textarea', type: 'textarea', name: 'request_procedures', placeholder: "Enter request procedures", label: 'Request Procedures', required: true, onChange: 'textareaHTMLValidation' },
	{ tag: 'textarea', type: 'textarea', name: 'funders_for_service', placeholder: "Enter funders for service", label: 'Funders for Service', required: true, onChange: 'textareaHTMLValidation' },
	{ tag: 'textarea', type: 'textarea', name: 'value_to_customer', placeholder: "Enter value to customer", label: 'Value to customer', required: true, onChange: 'textareaHTMLValidation' },
	{ tag: 'textarea', type: 'textarea', name: 'risks', placeholder: "Enter risks", label: 'Risks', required: true, onChange: 'textareaHTMLValidation' },
	{ tag: 'textarea', type: 'textarea', name: 'competitors', placeholder: "Enter competitors", label: 'Competitors', required: true, onChange: 'textareaHTMLValidation' },
	// todo: how to fill the data for the options (should be done before rendering)
	{ tag: 'input', type: 'text', name: 'service_owner', label: 'Service Owner', placeholder: "Enter service owner name" },
	{ tag: 'input', type: 'text', name: 'contact_information_external', label: 'Contact Information External', placeholder: "Enter external contact info" },
	{ tag: 'input', type: 'text', name: 'contact_information_internal', label: 'Contact Information Internal', placeholder: "Enter internal contact info" }
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
					    <textarea className="form-control" id={field.name} placeholder={field.placeholder} name={field.name} rows="6" onChange={this[field.onChange]}></textarea>
					    <span id={field.name + '-error'} className="validation-message sr-only"></span>
					</div>
				);				
			}
			else if(field.tag == 'select'){
				return(
					<div className="form-group" key={i}>
					    <label htmlFor={field.name}>{field.label}</label>
					    <OptionsComponent options={field.optionsData} selectName={field.name}></OptionsComponent>
					    <span id={field.name + '-error'} className="validation-message sr-only"></span>
					</div>
				);				
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
			validationMessage = "The name is required"
			validationObjects.push( { field: 'name', message: validationMessage } );
		}

		if($('#name').val().length > 255){
			validationMessage = "Content exceeds max length of 255 characters."
			validationObjects.push( { field: 'name', message: validationMessage } );			
		}

		if($('#service_area').val().length > 255){
			validationMessage = "Content exceeds max length of 255 characters."
			validationObjects.push( { field: 'service_area', message: validationMessage } );			
		}

		if($('#service_type').val().length > 255){
			validationMessage = "Content exceeds max length of 255 characters."
			validationObjects.push( { field: 'service_type', message: validationMessage } );
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
			this.clearValidations();
			//var formValues = JSON.stringify($("#service-form").serializeJSON());
			//console.log("The form values are ->", formValues);


			var service_owner_id =  $("#service_owner").val();

			if(serviceOwnerName != service_owner_id){
				if(serviceOwnerName != null || service_owner_id != "")
				{
					serviceOwnerName = null;
					serviceOwnerId = null;
					for(var i = 0; i < globalOwnerData.length; i++){
						if(service_owner_id == globalOwnerData[i].first_name + " " + globalOwnerData[i].last_name){
							serviceOwnerId = globalOwnerData[i].uuid;
							serviceOwnerName = service_owner_id;
							break;
						}
					}
				}
			}

			var external_contact_information =  $("#contact_information_external").val();

			if(externalContactInformationName != external_contact_information){
				if(externalContactInformationName != null || external_contact_information != "")
				{
					externalContactInformationName = null;
					externalContactInformationId = null;
					for(var i = 0; i < globalExternalContactData.length; i++){
						if(external_contact_information == globalExternalContactData[i].first_name + " " + globalExternalContactData[i].last_name){
							externalContactInformationId = globalExternalContactData[i].uuid;
							externalContactInformationName = external_contact_information;
							break;
						}
					}
				}
			}

			var internal_contact_information =  $("#contact_information_internal").val();

			if(internalContactInformationName != internal_contact_information){
				if(internalContactInformationName != null || internal_contact_information != "")
				{
					internalContactInformationName = null;
					internalContactInformationId = null;
					for(var i = 0; i < globalInternalContactData.length; i++){
						if(internal_contact_information == globalInternalContactData[i].first_name + " " + globalInternalContactData[i].last_name){
							internalContactInformationId = globalInternalContactData[i].uuid;
							internalContactInformationName = internal_contact_information;
							break;
						}
					}
				}
			}

			var params = {};
			params["name"] = $("#name").val();
			params["description_external"] = $("#description_external").val();
			params["description_internal"] = $("#description_internal").val();
			params["service_area"] = $("#service_area").val();
			params["service_type"] = $("#service_type").val();
			params["request_procedures"] = $("#request_procedures").val();
			params["funders_for_service"] = $("#funders_for_service").val();
			params["value_to_customer"] = $("#value_to_customer").val();
			params["risks"] = $("#risks").val();
			params["competitors"] = $("#competitors").val();
			params["service_owner_uuid"] = serviceOwnerId;
			params["service_contact_information_uuid"] = externalContactInformationId;
			params["service_internal_contact_information_uuid"] = internalContactInformationId;


			var parts = window.location.href.split("/");
			var host = "http://" + parts[2];
			var url = "";

			if(this.props.source != null && this.props.source != ""){
				params["uuid"] = parts[parts.length - 1];
				url = host + "/api/v1/services/edit";
				opType = "edit";
			}
			else {
				url = host + "/api/v1/services/add";
				opType = "add";
			}

			this.serverRequest = $.ajax({
				url: url,
				dataType: "json",
				crossDomain: true,
				type: "POST",
				contentType:"application/json",
				cache: false,
				data: JSON.stringify(params),
				success: function (data) {
					if(opType == "add")
						$("#modal-success-body").text("You have successfully inserted a new service version");
					else
						$("#modal-success-body").text("You have successfully updated the service version");
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
			service: {
				name: "",
				description_internal: ""
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
                this.setState({service: data.data});
                $("#name").val(this.state.service.name);
                $("#description_internal").val(this.state.service.description_internal);
                $("#description_external").val(this.state.service.description_external);
                $("#service_area").val(this.state.service.service_area);
                $("#service_type").val(this.state.service.service_type);
                $("#request_procedures").val(this.state.service.request_procedures);
                $("#funders_for_service").val(this.state.service.funders_for_service);
                $("#value_to_customer").val(this.state.service.value_to_customer);
                $("#risks").val(this.state.service.risks);
                $("#competitors").val(this.state.service.competitors);
				$("#service_owner").val(this.state.service.service_owner.email);
				$("#contact_information_internal").val(this.state.service.contact_information.internal_contact_information
					.internal_contact_information.internal_contact_information.first_name + " " +
				this.state.service.contact_information.internal_contact_information
					.internal_contact_information.internal_contact_information.last_name);

				$("#contact_information_external").val(this.state.service.contact_information.external_contact_information
					.internal_contact_information.internal_contact_information.first_name + " " +
				this.state.service.contact_information.external_contact_information
					.internal_contact_information.internal_contact_information.last_name);
				serviceOwnerId = this.state.service.service_owner.uuid;

				internalContactInformationId = this.state.service.contact_information.internal_contact_information.
					internal_contact_information.internal_contact_information.uuid;
				internalContactInformationName = $("#contact_information_internal").val();
				externalContactInformationId = this.state.service.contact_information.external_contact_information.
					internal_contact_information.internal_contact_information.uuid;
				externalContactInformationName = $("#contact_information_external").val();

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

	var temp = null;
	$(document).bind('click', function (event) {
        // Check if we have not clicked on the search box
        if (!($(event.target).parents().andSelf().is('#service_owner'))) {
			$(".ui-menu-item").remove();
		}

        if (!($(event.target).parents().andSelf().is('#contact_information_external'))) {
			$(".ui-menu-item").remove();
		}

        if (!($(event.target).parents().andSelf().is('#contact_information_internal'))) {
			$(".ui-menu-item").remove();
		}

        if (!($(event.target).parents().andSelf().is('#service_area'))) {
			$(".ui-menu-item").remove();
		}

        if (!($(event.target).parents().andSelf().is('#service_type'))) {
			$(".ui-menu-item").remove();
		}


    });

	var getDataServiceOwner = function(request, response){

        var url = window.location.href;
        var contents = url.split("/");
        var host = contents[0] + "//" + contents[2];

		$.getJSON(
            host + "/api/v1/owner/all?search=" + request.term,
            function (data) {
				for(var i = 0; i < data.data.length; i++) {
					data.data[i].value = data.data[i].first_name + " " + data.data[i].last_name;
					data.data[i].label = data.data[i].first_name + " " + data.data[i].last_name;
                    data.data[i].index = i;
				}
				globalOwnerData = data.data;
                response(data.data);
            });
	};

    var getDataContactInformationExternal = function(request, response){

        var url = window.location.href;
        var contents = url.split("/");
        var host = contents[0] + "//" + contents[2];

        $.getJSON(
            host + "/api/v1/owner/contact_information/all?search=" + request.term,
            function (data) {
				for(var i = 0; i < data.data.length; i++) {
                    data.data[i] = data.data[i].internal_contact_information.internal_contact_information;
					data.data[i].value = data.data[i].first_name + " " + data.data[i].last_name;
					data.data[i].label = data.data[i].first_name + " " + data.data[i].last_name;
                    data.data[i].index = i;
				}
				globalExternalContactData = data.data;
                response(data.data);
            });
	};

	var getDataContactInformationInternal = function(request, response){

        var url = window.location.href;
        var contents = url.split("/");
        var host = contents[0] + "//" + contents[2];

        $.getJSON(
            host + "/api/v1/owner/contact_information/all?search=" + request.term,
            function (data) {
				for(var i = 0; i < data.data.length; i++) {
                    data.data[i] = data.data[i].internal_contact_information.internal_contact_information;
					data.data[i].value = data.data[i].first_name + " " + data.data[i].last_name;
					data.data[i].label = data.data[i].first_name + " " + data.data[i].last_name;
                    data.data[i].index = i;
				}
				globalInternalContactData = data.data;
                response(data.data);
            });
	};

    var getDataServiceArea = function(request, response){

        var url = window.location.href;
        var contents = url.split("/");
        var host = contents[0] + "//" + contents[2];

        $.getJSON(
            host + "/api/v1/services/area/all?search=" + request.term,
            function (data) {
				for(var i = 0; i < data.data.length; i++) {
                    data.data[i].value = data.data[i].area;
					data.data[i].label = data.data[i].area;
                    data.data[i].index = i;
				}
                response(data.data);
            });
	};

    var getDataServiceType = function(request, response){

        var url = window.location.href;
        var contents = url.split("/");
        var host = contents[0] + "//" + contents[2];

        $.getJSON(
            host + "/api/v1/services/type/all?search=" + request.term,
            function (data) {
				for(var i = 0; i < data.data.length; i++) {
                    data.data[i].value = data.data[i].type;
					data.data[i].label = data.data[i].type;
                    data.data[i].index = i;
				}
                response(data.data);
            });
	};

    $( "#service_owner" ).autocomplete({
      source: getDataServiceOwner,
      minLength: 2,
      select: function( event, ui ) {
		this.value = ui.item.first_name + " " + ui.item.last_name;
		serviceOwnerId = ui.item.uuid;
		serviceOwnerName = ui.item.first_name + " " + ui.item.last_name;
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
        .append( item.first_name + " " + item.last_name )
        .appendTo( ul );
    };

    $( "#contact_information_internal" ).autocomplete({
      source: getDataContactInformationInternal,
      minLength: 2,
      select: function( event, ui ) {
		this.value = ui.item.first_name + " " + ui.item.last_name;
		internalContactInformationId = ui.item.uuid;
		internalContactInformationName = ui.item.first_name + " " + ui.item.last_name;
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
        .append( item.first_name + " " + item.last_name )
        .appendTo( ul );
    };


	$( "#contact_information_external" ).autocomplete({
      source: getDataContactInformationExternal,
      minLength: 2,
      select: function( event, ui ) {
		this.value = ui.item.first_name + " " + ui.item.last_name;
		externalContactInformationId = ui.item.uuid;
		externalContactInformationName = ui.item.first_name + " " + ui.item.last_name;
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
        .append( item.first_name + " " + item.last_name )
        .appendTo( ul );
    };

    $( "#service_area" ).autocomplete({
      source: getDataServiceArea,
      minLength: 2,
      select: function( event, ui ) {
		this.value = ui.item.area;
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
        .append( item.area )
        .appendTo( ul );
    };

    $( "#service_type" ).autocomplete({
      source: getDataServiceType,
      minLength: 2,
      select: function( event, ui ) {
		this.value = ui.item.type;
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
        .append( item.type )
        .appendTo( ul );
    };


  } );