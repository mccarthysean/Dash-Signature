/* eslint no-magic-numbers: 0 */
import React, {useState} from 'react';

import Signature from '../lib/components/Signature.react';
import { divide } from 'ramda';

const App = () => {
  return (<div>
    <Signature id={'test'} setProps={()=>undefined}/>
  </div>)
}

export default App;
