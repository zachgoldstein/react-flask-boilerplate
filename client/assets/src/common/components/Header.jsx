import React from "react";

import {Navbar, Nav, NavItem, Button, Image} from 'react-bootstrap';

export default class Header extends React.Component {

    constructor() {
        super();
        this.onClickLogout = this.onClickLogout.bind(this);
    }

    onClickLogout() {
        this.props.logoutHandler();
    }

    render() {
        return (
            <Navbar inverse fluid={true}>
                <Navbar.Header>
                    <Image src="http://placekitten.com/g/150/50" rounded/>
                    <Navbar.Text>
                        TimeTrackr
                    </Navbar.Text>

                    <Navbar.Toggle />
                </Navbar.Header>
                <Navbar.Collapse>
                    <Nav pullRight>
                        <Navbar.Text>
                            {this.props.username}
                        </Navbar.Text>
                        <Image src="http://placekitten.com/g/50/50" circle/>
                        <NavItem onClick={this.onClickLogout}>Logout</NavItem>
                    </Nav>
                </Navbar.Collapse>

            </Navbar>
        );
    }
}

Header.propTypes = {
    logoutHandler: React.PropTypes.func,
    username: React.PropTypes.string
};