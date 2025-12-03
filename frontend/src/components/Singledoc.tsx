'use client';
import { SquareCheckBig, SquarePen, Trash2 } from "lucide-react";
import { SingleFile } from "../../types";
import ToolTip from "./ToolTip";
import { Modal } from "./ui/Modal";
import { Button } from "./ui/button";
import { delete_file } from "@/actions/actions";
import { toast } from "react-hot-toast/headless";

// task -> filecontent
// Todo -> SingleFile
export default function Singledoc({filecontent}:{filecontent:SingleFile}) {

  const handleDelete = async () => {
    const response = await delete_file(filecontent.id);
    if (response.status === "success") {
      toast.success(response.message);
      console.log('File deleted successfully');

    } else {
      toast.error(response.message);
      console.error('Failed to delete the file');
    }
  }

  return (
  
    <tr className="flex justify-between items-center border-b border-gray-500 px-2 py-2">
        <td>
            {filecontent.content}
        </td>
        <td className="flex gap-x-2">
            <ToolTip tool_tip_content="Edited">
            <SquareCheckBig />
            </ToolTip>
            <Modal title="Edit content" Editing={true} filecontent={filecontent}>
            <SquarePen className="text-blue-500" />
            </Modal>
            <Button onClick={handleDelete} variant="ghost">
            <Trash2 className="text-red-500 " />
            </Button>
        </td>
    </tr>

  )
}
