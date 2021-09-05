import './App.css';

import React from "react";
import UsersList from "./components/Users";
import axios from "axios";
import Header from "./components/Header";
import Footer from "./components/Footer";
import Users from "./components/Users";

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'users': []
        };
    }

    componentDidMount() {
        //this.setState(this.state = {
        //    'users': users
        //}
        //)

        axios
            .get('http://127.0.0.1:8000/api/users/')
            .then(response => {
                const users = response.data
                this.setState(
                    {'users': users}
                )
            })
            .catch(error => console.log(error))
    }

    render() {
        return (<div className='App'>
                <Header/>
                <UsersList users={this.state.users}/>
                <Footer/>
            </div>
        )
    }
}


export default App;
