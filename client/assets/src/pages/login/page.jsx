import React from 'react';
import styles from './style.scss';

import {Button, Form, FormGroup, Grid, Col, Row, ControlLabel, FormControl} from 'react-bootstrap';
import Auth from '../../common/api/Auth.js'


export default class LoginPage extends React.Component {

    constructor() {
        super();
        this.clickSignUp = this.clickSignUp.bind(this);
        this.clickLogin = this.clickLogin.bind(this);
        this.onPasswordChange = this.onPasswordChange.bind(this);
        this.onUsernameChange = this.onUsernameChange.bind(this);
    }

    clickLogin() {
        var self = this;
        Auth.getAuthToken(self.state.username, self.state.password).then(function(token){
            if (token != null && token != '') {
                self.props.authHandler();
            }
        });
    }

    clickSignUp() {
        var num = Math.floor(Math.random() * 100);
        var TEMP_USERNAME = "test" + num + "@gmail.com";
        var TEMP_PASSWORD = "pass" + num;

        var self = this;

        Auth.signUp(TEMP_USERNAME, TEMP_PASSWORD).then(function(){
            return Auth.getAuthToken(TEMP_USERNAME, TEMP_PASSWORD);
        }).then(function(){
            console.log("new access token!: " + sessionStorage.getItem('accessToken') );
            self.props.authHandler();
        });
    }

    onUsernameChange(event){
        this.setState({username:event.target.value})
    }

    onPasswordChange(event){
        this.setState({password:event.target.value})
    }

    render() {
        var centerStyle = {
            textAlign:"center"
        };
        return (
            <Grid>
                <Row>
                    <Col smOffset={4} sm={4}>
                        <Form horizontal>
                            <h2 style={centerStyle} className="form-signin-heading">TimeTrackr</h2>
                            <FormGroup controlId="formHorizontalEmail">
                                <Col componentClass={ControlLabel} sm={3}>
                                    Username
                                </Col>
                                <Col sm={9}>
                                    <FormControl type="email" placeholder="Username"
                                                 onChange={this.onUsernameChange}/>
                                </Col>
                            </FormGroup>

                            <FormGroup controlId="formHorizontalPassword">
                                <Col componentClass={ControlLabel} sm={3}>
                                    Password
                                </Col>
                                <Col sm={9}>
                                    <FormControl type="password" placeholder="Password"
                                                 onChange={this.onPasswordChange}/>
                                </Col>
                            </FormGroup>

                            <FormGroup style={centerStyle}>
                                <Col sm={6}>
                                    <Button type="button" onClick={this.clickLogin}
                                            bsStyle="primary" bsSize="large">
                                        Log in
                                    </Button>
                                </Col>
                                <Col sm={6}>
                                    <Button type="button" onClick={this.clickSignUp}
                                            bsStyle="primary" bsSize="large">
                                        Register
                                    </Button>
                                </Col>
                            </FormGroup>
                        </Form>
                    </Col>
                </Row>
            </Grid>
        );
    }
}

LoginPage.propTypes = {
    authHandler: React.PropTypes.func
};