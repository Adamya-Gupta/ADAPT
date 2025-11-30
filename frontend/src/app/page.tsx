import Filestable from "@/components/Filestable";
import { Modal } from "@/components/ui/Modal";
import { Button } from "@/components/ui/button"

export default function Home() {
  return (
      <main className=" mt-8 mx-auto max-w-5xl">
        {/* Modal Section */}
        <section> 
          <Modal title="Add content" Adding={true}>
          <Button variant="default" className="w-full bg-blue-600 px-2 py-1 text-white uppercase text-lg">Add content</Button>
          </Modal>
        </section>
        
        {/* Content Section */}
        <section className="mt-4">
          <Filestable/>
        </section>
        
      </main>
  );
}
