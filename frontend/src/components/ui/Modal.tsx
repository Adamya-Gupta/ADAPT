import { Button } from "@/components/ui/button"
import {
  Dialog,
  DialogClose,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"
import AddContent from "../AddContent"
import EditContent from "../EditContent"


export function Modal({children , title, Adding, Editing}:{children:React.ReactNode,title:string,Adding?:boolean,Editing?:boolean}) {
  return (
    <Dialog>
      <form>
        <DialogTrigger asChild>
          {children}

        </DialogTrigger>
        <DialogContent className="sm:max-w-[425px]">
          <DialogHeader>
            <DialogTitle>{title}</DialogTitle>
           
          </DialogHeader>
         {Adding && <AddContent/>}
         {Editing && <EditContent/>}

        
        </DialogContent>
      </form>
    </Dialog>
  )
}
