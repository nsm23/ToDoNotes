import React from "react";


const NoteItem = ({ note }) => {
    return (
        <tr>
            <td>
                {note.project}
            </td>
            <td>
                {note.remark}
            </td>
            <td>
                {note.created_day}
            </td>
            <td>
                {note.updated_day}
            </td>

        </tr>

    )
}

const NotesList = ({ notes }) => {
    return (<div className='body'>
            <table>
                <thead>
                <tr>
                    <th>Project</th>
                    <th>Remark</th>
                    <th>Created</th>
                    <th>Updated</th>
                </tr>
                </thead>
                <tbody>
                {notes.map((note) => <NoteItem key={note.id} note={note}/>)}
                </tbody>
            </table>
        </div>
    );

}

export default NotesList;
