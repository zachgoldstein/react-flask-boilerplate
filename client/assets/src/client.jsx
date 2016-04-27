
/**
 * App entry point
 */

import 'babel-polyfill';

import React from 'react';
import ReactDOM from 'react-dom';
import App from './common/components/App.jsx';

// ID of the DOM element to mount app on
const DOM_APP_EL_ID = 'app';

console.log("Using endpoint,",__API_ENDPOINT__);

// Render the router
ReactDOM.render((<App/>), document.getElementById(DOM_APP_EL_ID));