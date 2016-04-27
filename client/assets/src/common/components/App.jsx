import React from 'react';

import Login from '../../pages/login/page.jsx';
import Home from '../../pages/home/page.jsx';
import Auth from '../api/Auth.js'
import User from '../api/User.js'

const CHECK_TOKEN_FREQ = 1000*3;

export default class App extends React.Component{
    constructor() {
        super();

        // Manage a bit of state here:

        this.gotAuth = this.gotAuth.bind(this);
        this.checkToken = this.checkToken.bind(this);
        this.loggedOut = this.loggedOut.bind(this);
        // TODO: Check if we have an auth token already in the session
        this.state = {isLoggedIn: false}
    }

    gotAuth() {
        this.timer = setInterval(this.checkToken, CHECK_TOKEN_FREQ);
        this.setState({isLoggedIn: true});
    }

    checkToken() {
        console.log("checking token...");
        var location = sessionStorage.getItem('userLocation');
        var userId = location.split("/")[location.split("/").length - 1];
        //return

        var self = this;
        Auth.getCurrentAuthedUser().then(function(user){
            if (user == null) {
                console.log("token invalid");
                self.setState({isLoggedIn: false});
                clearTimeout(self.timer);
            } else {
                console.log("token valid");
                self.setState({
                    isLoggedIn: true,
                    username: user['username']
                });
            }
        })
    }

    loggedOut() {
        Auth.logout();
        this.setState({isLoggedIn: false});
        console.log("logged out");
    }


    render() {

        var currentPage = <Login authHandler={this.gotAuth}/>;
        if (this.state.isLoggedIn) {
            currentPage = <Home username={this.state.username} logoutHandler={this.loggedOut} />;
        }

        //var currentPage = <Home authToken={this.state.authToken} logoutHandler={this.loggedOut} />;
        return currentPage;
    }
}