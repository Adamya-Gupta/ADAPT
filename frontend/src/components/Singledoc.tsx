import { SquareCheckBig, SquarePen, Trash2 } from "lucide-react";
import { SingleFile } from "../../types";
import ToolTip from "./ToolTip";
import { Modal } from "./ui/Modal";

export default function Singledoc({filecontent}:{filecontent:SingleFile}) {
  return (
    <>
    <tr className="flex justify-between items-center border-b border-gray-500 px-2 py-2">
        <td>
            {filecontent.content}
        </td>
        <td className="flex gap-x-2">
            <ToolTip tool_tip_content="Edited">
            <SquareCheckBig />
            </ToolTip>
            <Modal title="Edit content" Editing={true}>
            <SquarePen className="text-blue-500"/>
            </Modal>
            <Trash2 className="text-red-500" />
        </td>
    </tr>
    </>
  )
}
