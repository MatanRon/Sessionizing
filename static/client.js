// TODO: handle Code duplications

class Client {
    constructor() {

		$('#number_of_sessions_get').click(this.onNumberOfSessionsGetValue);
		$('#median_length_get').click(this.onMedianLengthGetValue);
		$('#number_of_visited_sites_get').click(this.onNumberOfVisitedSitesGetValue);
    }

    onNumberOfSessionsGetValue(event) { // $ represent an instance of jquery
        let session_site_url = $('#session_site_url').val()
        $.ajax({ // ajax func utils to send http request
            url: '/number_of_sessions_get/', // ajax func receives a jason as an argument with the key url.
            type: "POST",
	        data: JSON.stringify({'session_site_url': session_site_url}),
	        contentType: "application/json; charset=utf-8",
			success: function(data) {

                document.getElementById('lblNumberOfSessionsResult').innerHTML =  data;
				console.log("Data Start:");
				console.log(data);
				console.log("Data End");
				
				return data;
			},

        }).done(function() {
            alert('let\'s check out your popularity')
        })
    }

    onMedianLengthGetValue(event) { // $ represent an instance of jquery
        let site_url = $('#site_url').val()
        $.ajax({ // ajax is a func which utils to send http request (it operates on $)
            url: '/median_length_get/', // ajax func receive a jason as an argument with the key url. url is the path of the specific button in the server.
            type: "POST",
	        data: JSON.stringify({'site_url': site_url}),
	        contentType: "application/json; charset=utf-8",
			success: function(data) {
				document.getElementById('lblMedianSessionLength').innerHTML = data;

				console.log("Data Start:");
				console.log(data);
				console.log("Data End");

				return data;
			},

        }).done(function() {
            alert('The median session length result is on its way')
        })
    }

    onNumberOfVisitedSitesGetValue(event) {
        let visitor_id = $('#visitor_id').val()
        $.ajax({
            url: '/number_of_visited_sites_get/',
            type: "POST",
	        data: JSON.stringify({'visitor_id': visitor_id}),
	        contentType: "application/json; charset=utf-8",
			success: function(data) {

				document.getElementById('lblUniqueVisitedSites').innerHTML = data;

				console.log("Data Start:");
				console.log(data);
				console.log("Data End");

				return data;
			},

        }).done(function() {
            alert('The number of visitor\'s unique visited sites is on its way')
        })
    }
}


new Client()