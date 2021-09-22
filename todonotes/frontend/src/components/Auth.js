import React from "react";


class LoginForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            username: '',
            password: ''
        }
    }
    render(){
        return(
            <form>
                <input type='text' name='username'/>
                <input type='text' name='password'/>
                <input type='submit' value='login'/>
            </form>
        )
    }
}


export default LoginForm