/* eslint no-magic-numbers: 0 */
import React, { useState } from 'react';

import { Signature } from '../lib';

const App = () => {

  const [state, setState] = useState({ value: '' });
  const setProps = (newProps) => {
    setState(newProps);
  };

  return (
    <Signature
      setProps={setProps}
      {...state}
    />
  )
};


export default App;
