import React from 'react'
import {useParams} from "react-router-dom";


const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>{project.id}</td>
            <td>{project.name}</td>
            <td>{project.users}</td>
            <td>{project.repo_url}</td>
        </tr>
    )
}


const SingleProject = ({projects}) => {
    let { id } = useParams();
    let filterProjects = projects.filter((project) => project.project.id === +id);
    return (
        <table>
            <tr>
                <th>Name</th>
                <th>Users</th>
                <th>Repository</th>
            </tr>
            <tbody>
            {filterProjects.map((project) => <ProjectItem key={project.id} project={project}/>)}
            </tbody>
        </table>
    )
}

export default SingleProject;


