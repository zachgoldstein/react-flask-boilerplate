import React from "react";
import styles from "./style.scss";

import Button from 'react-bootstrap/lib/Button';


export default class HomePage extends React.Component {
    render() {
        return (
            <div className={styles.content}>
                <h1>Home Page</h1>
                <Button> This is a test </Button>
                <p className={styles.welcomeText}>Thanks for joining!</p>
            </div>
        );
    }
}