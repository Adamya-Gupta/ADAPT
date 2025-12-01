import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"
import AddContent from "../AddContent"
import EditContent from "../EditContent"
import { SingleFile } from "../../../types"


export function Modal({children , title, Adding, Editing, filecontent}:{children:React.ReactNode,title:string,Adding?:boolean,Editing?:boolean, filecontent: SingleFile}) {
  return (
    <Dialog>
   
        <DialogTrigger asChild>
          {children}
        </DialogTrigger>
        
        <DialogContent className="sm:max-w-[425px]">
          
          <DialogHeader>
            <DialogTitle>{title}</DialogTitle>
          </DialogHeader>

         {Adding && <AddContent/>}
         {Editing && <EditContent filecontent={filecontent} />}     
        </DialogContent>
   
    </Dialog>
  )
}
