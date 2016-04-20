import React from 'react';
import { browserHistory } from 'react-router';
import styles from './style.scss';

import Button from 'react-bootstrap/lib/Button';


export default class LoginPage extends React.Component {
    signUp() {
        browserHistory.push('/home');
    }

    render() {
        return (
            <div className={styles.content}>
                <h1 className={styles.heading}>Login Page</h1>
                <Button> This is a test </Button>
                <p className={styles.lead}>Create an account to get started!</p>
                <button className={styles.signUpButton} onClick={this.signUp}>Sign up</button>
            </div>
        );
    }
}