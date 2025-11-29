import {SingleFile} from "../../types"
import Singledoc from "./Singledoc"

function Filestable() {
    const file_list : SingleFile[] = [
        {id:1,content:"fist task",is_edited: false},
        {id:2,content:"secnd task",is_edited: false},
        {id:3,content:"thd task",is_edited: false},
        
    ]
  return (

    <table className='w-full'>
        <thead>
            <tr className='flex justify-between items-center px-2 py-1 bg-gray-100 shadow-md'>
                <th>Files</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
           
            {
                file_list.map((filecontent:SingleFile)=>(
                    <Singledoc key = {filecontent.id} filecontent={filecontent}/> 
                ))
            }
        </tbody>
    </table>
  

  )
}

export default Filestable