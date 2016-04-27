import Requests from "./Requests.js"

export default class Auth {
    static signUp(username, password) {
        var endpoint = __API_ENDPOINT__ + "/api/users/";
        return fetch(endpoint, {
            method: 'POST',
            body: JSON.stringify({
                username: username,
                password: password
            }),
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
        }).then(function(response) {
            if (response.status != 200 && response.status != 201) {
                console.log('Request to ' + endpoint + ' returned error status:' + response.status);
            }
            var location = response.headers.get("location");
            if (location != null) {
                sessionStorage.setItem('userLocation', location);
                return location;
            }
            return response.json();
        }).then(function(result) {
            if (result['message'] != null) {
                console.log("API Error: " + result['message'])
            }
        }).catch(function(error) {
            console.log('Could not sign up error: ' + error.message);
        });
    }

    static getAuthToken(username, password) {
        var endpoint = __API_ENDPOINT__ + "/api/users/auth";
        return fetch(endpoint, {
            method: 'POST',
            body: JSON.stringify({
                username: username,
                password: password
            }),
            headers: {
                'Content-Type': 'application/json; charset=utf-8',
                'Accept': 'application/json'
            }
        }).then(function(response) {
            if (response.status != 200 && response.status != 201) {
                console.log('Request to ' + endpoint + ' returned error status:' + response.status);
            }
            return response.json();
        }).then(function(result){
            if (result['access_token'] != null) {
                sessionStorage.setItem('accessToken', result['access_token']);
                return result['access_token'];
            } else if (result['message'] != null) {
                console.log("API Error: " + result['message'])
            }
        }).catch(function(error) {
            console.log('Could not sign up error: ' + error.message);
        });
    }

    static getCurrentAuthedUser() {
        var endpoint = "/api/users/me";
        return Requests.issueRequest(endpoint, 'GET');
    }

    static logout() {
        sessionStorage.removeItem('accessToken');
    }
}
