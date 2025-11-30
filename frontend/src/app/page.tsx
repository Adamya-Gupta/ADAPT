import Image from "next/image";
import { Button } from "@/components/ui/button"
import { Modal } from "@/components/ui/Modal";
import Filestable from "@/components/Filestable";

export default function Home() {
  return (
    <div className="">
      <main className="bg-blue-100 mt-8 mx-auto max-w-5xl">
        {/* Modal Section */}
        <section> 
          <Modal title="Add content" Adding={true}>
          <Button variant="default" className="w-full bg-blue-600 px-2 py-1 text-white uppercase text-lg">Add content</Button>
          </Modal>
        </section>
        {/* Content Section */}
        <section>
          <Filestable/>
        </section>
        
      </main>
    </div>
  );
}
