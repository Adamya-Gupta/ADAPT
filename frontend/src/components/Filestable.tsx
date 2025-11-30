import {SingleFile} from "../../types"
import Singledoc from "./Singledoc"


export default async function FilesTable() {
    const response  = await fetch('http://localhost:8000/contents/')
    const file_list : SingleFile[] = await response.json()

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
