export default class Requests {
    static issueRequest(endpoint, method, data) {
        endpoint = __API_ENDPOINT__ + endpoint;
        return fetch(endpoint, {
            method: method,
            headers: {
                'Content-Type': 'application/json; charset=utf-8',
                'Accept': 'application/json',
                'Authorization': "JWT " + sessionStorage.getItem('accessToken')
            },
            body: JSON.stringify(data)
        }).then(function(response) {
            if (response.status != 200 && response.status != 201) {
                console.log('Request to ' + endpoint + ' returned error status:' + response.status);
            }
            return response.json();
        }).then(function(result){
            if (result['message'] != null) {
                console.log("API Error: " + result['message'])
                return null;
            }
            return result;
        }).catch(function(error) {
            console.log('Could not issue request to ' + endpoint + ' error: ' + error.message);
            return null;
        });
    }
}