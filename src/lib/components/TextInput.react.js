import React, {Component} from 'react';

class TextInput extends Component {
    constructor(props) {
        super(props);
        this.state = {
            value: 'dash',
        };
    }

    setProps(newProps) {
        this.setState(newProps);
    }

    handleInputChange = (e) => {
        // get the value from the DOM node
        const newValue = e.target.value;
        this.props.setProps({value: newValue});
    };

    render() {
        return (
            <TextInput
                label={'Dash'}
                value={this.state.value}
                setProps={this.setProps}
            />
        );
    }
}

export default TextInput;
