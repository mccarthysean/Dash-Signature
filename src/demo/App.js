/* eslint no-magic-numbers: 0 */
import React, {useState} from 'react';

import {Signature} from '../lib';
import {TextInput} from '../lib';

class App extends Component {
    constructor() {
        super(props);

        this.state = {
            value: 'dash',
        };
    }

    render() {
        return <TextInput label={'Dash'} value={this.state.value} />;
    }
}

export default App;
