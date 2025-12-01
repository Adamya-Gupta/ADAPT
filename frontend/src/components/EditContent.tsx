'use client'
import { edit_file } from "@/actions/actions";
import { SingleFile } from "../../types";
import { useState, useActionState,  useEffect } from "react";
import SubmitButton from "./SubmitButton";
import { toast } from "react-hot-toast";


export default function EditContent({filecontent}:{filecontent:SingleFile}) {
  const [value, setValue] = useState(filecontent.content);
  const [state,formAction] = useActionState(edit_file,{status:" ",message:" "})
  const {status,message} = state;
  
  const handleSubmit = async (formData:FormData) => {
    const id:number = filecontent.id;
    const content = formData.get('edit_content') as string;

    const doc_type:string = filecontent.doc_type;
    const is_edited:boolean = true;
    formAction({id, content, doc_type, is_edited});
  }

  const handleChange = (e:React.ChangeEvent<HTMLInputElement>) => {
    setValue(e.target.value);
  } 

  useEffect(()=>{
    if(status === "success"){
      // alert(message)
     
      toast.success(message)
    }
    else if(status === "error"){
      toast.error(message) 
    }
  },[state,message,status])

  return (
    <form action={handleSubmit} className='flex flex-col justify-between items-center gap-x-4 w-full'>
        <input type='text' 
        onChange={handleChange}
        name="edit_content"
        value={value}
        className='w-full px-2 py-1 border border-gray-300 rounded-md mb-2'/>
        <SubmitButton/>
    </form>
  )
}

