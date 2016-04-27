import React from "react";
import styles from "./style.scss";

import {Button, Form, FormGroup, Grid, Col, Row, ControlLabel, FormControl} from 'react-bootstrap';
import Header from "../../common/components/Header.jsx"
import User from "../../common/api/User.js"

export default class HomePage extends React.Component {
    constructor() {
        super();
    }

    clickTESTADMIN() {
        User.testADMIN();

    }

    render() {
        return (
            <Grid fluid={true}>
                <Row>
                    <Header logoutHandler={this.props.logoutHandler} username={this.props.username} />
                </Row>
                <Row>
                    <Col smOffset={3} sm={6}>
                        <Row>
                            <Button type="button" onClick={this.clickTESTADMIN}
                                    bsStyle="primary" bsSize="large">
                                Test ADMIN auth
                            </Button>
                        </Row>
                        <Row>
                            Test
                        </Row>
                        <Row>
                            Test
                        </Row>
                        <Row>
                            Test
                        </Row>
                        <Row>
                            Test
                        </Row>
                        <Row>
                            Test
                        </Row>
                        <Row>
                            Test
                        </Row>
                    </Col>
                </Row>
            </Grid>
        );
    }
}

HomePage.propTypes = {
    logoutHandler: React.PropTypes.func,
    username: React.PropTypes.string
};