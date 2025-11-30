'use client'
import { add_file } from "@/actions/actions"
import { useActionState, useEffect, useRef } from "react"
import toast from "react-hot-toast";
import SubmitButton from "./SubmitButton";


export default function AddContent(){

  const ref = useRef<HTMLFormElement>(null);
  const [state,formAction] = useActionState(add_file,{status:" ",message:""})
  const {status,message} = state;

  useEffect(()=>{
    if(status === "success"){
      alert(message)
      ref.current?.reset();
      toast.success(message)
    }
    else if(status === "error"){
      toast.error(message) 
    }
  },[state])

  return (
    <form ref={ref} action={formAction} className='flex flex-col justify-between items-center gap-x-4 w-full'>
        <input 
        type='text' 
        placeholder='Add content here' 
        name="add_content"
        required 
        className='w-full px-2 py-1 border border-gray-300 rounded-md'/>
        <SubmitButton/>
    </form>
  )
}

