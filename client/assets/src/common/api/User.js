import Requests from "./Requests.js"

export default class AuthUser {
    static getUser(id){
        var endpoint = "/api/users/" + id;
        return Requests.issueRequest(endpoint, 'GET');
    }


    static testADMIN(){
        var endpoint = "/api/users/test_admin";
        console.log("issuing request to ", endpoint);
        return Requests.issueRequest(endpoint, 'GET');
    }

    static editUser(id, data){
        var endpoint = "/api/users/" + id;
        return Requests.issueRequest(endpoint, 'POST', data);
    }
}