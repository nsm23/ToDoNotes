import React from "react";


const User = ({user}) => {
    return (
        <tr>
            <td>
                {user.username}
            </td>
            <td>
                {user.first_name}
            </td>
            <td>
                {user.last_name}
            </td>
            <td>
                {user.email}
            </td>

        </tr>

        )
}

const UsersList = ({users}) => {
    return <div className='body'>
        <table>
            <tr>
                <th>Username</th>
                <th>First name</th>
                <th>Last name</th>
                <th>Email</th>
            </tr>
            {users.map((user)=> <User user={user}/>)}

        </table>
        </div>

}

export default UsersList;