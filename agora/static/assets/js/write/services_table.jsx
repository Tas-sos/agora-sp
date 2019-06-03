

var ServiceTable = React.createClass({

	getInitialState: function(){
		return {
			services: [],
			count: 0,
			selected: 0
		}
	},

	componentDidMount: function () {
        this.serverRequest = $.ajax({
            url: this.props.source,
            dataType: "json",
            crossDomain: true,
            type: "GET",
            cache: false,
            success: function (data) {
				this.setState({
                    services: data.data.services,
					count: data.data.count
                });

            }.bind(this),
            error: function (xhr, status, err) {
                console.log(this.props.source, status, err.toString());
            }.bind(this)
        });


    },

    componentWillUnmount: function () {
        this.serverRequest.abort();
    },

	render: function() {

		var array = [];
		for(var i = 0; i < this.state.count; i++)
			array.push(i);

		return (
			<div className="row">
				<div className="col-xs-12">
					<div className="well with-header  with-footer">
						<div className="header bg-blue">
							Services
						</div>
						<table className="table table-hover">
							<thead className="bordered-darkorange">
								<tr>
									<th>
										Name
									</th>
									<th>
										Description internal
									</th>
									<th>
										Service category
									</th>
									<th>
										Service type
									</th>
									<th>

									</th>
								</tr>
							</thead>
							<tbody>

							{this.state.services.map(function (service) {
								return (
									<tr key={service.name}>
										<td>{service.name}</td>
										<td>{service.description_internal}</td>
										<td>{service.service_category}</td>
										<td>{service.service_type}</td>
										<td><a href={"/ui/service/" + service.uuid}>Edit</a></td>
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

ReactDOM.render(
  <ServiceTable  source={$("#source")[0].value}/>,
  document.getElementById('write-content')
);
