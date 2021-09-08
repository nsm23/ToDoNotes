import React from "react";
import {Link} from "react-router-dom";


const ProjectItem = ({project}) => {
    return (

        <tr>
                <td>
                    <Link to={`/projects/${project.id}/`}>{project.id}</Link>
                </td>
            <td>
                {project.name}
            </td>
            <td>
                {project.users}
            </td>
            <td>
                {project.repo_url}
            </td>
        </tr>

    )
}

const ProjectList = ({projects}) => {
    return (<div className='body'>
            <table>
                <thead>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Author</th>
                    <th>Repo</th>
                </tr>
                </thead>
                <tbody>
                {projects.map((project) => <ProjectItem key={project.id} project={project}/>)}
                </tbody>
            </table>
        </div>
    );

}

export default ProjectList;
