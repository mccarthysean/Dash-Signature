import '../css/output.css'
import PropTypes from 'prop-types';

function Test({ id, setProps }) {
  return (
    <span className='bg-red-500' id={id}>Test Component</span>
  )
}

Test.defaultProps = {};

Test.propTypes = {
  /**
   * The ID used to identify this component in Dash callbacks.
   */
  id: PropTypes.string,

  /**
   * Dash-assigned callback that should be called to report property changes
   * to Dash, to make them available for callbacks.
   */
  setProps: PropTypes.func
};

export default Test;
