import React from 'react';
import { Route, IndexRoute } from 'react-router';

import App from './App.jsx';
import LoginPage from '../../pages/login/page.jsx';
import HomePage from '../../pages/home/page.jsx';


export default (
    <Route path="/" component={App}>
        <IndexRoute component={LoginPage} />
        <Route path="home" component={HomePage} />
    </Route>
);