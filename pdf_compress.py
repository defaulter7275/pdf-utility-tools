import fitz  # PyMuPDF
import os

def hard_compress_pdf(input_path, output_path):
    # Open the document
    doc = fitz.open(input_path)
    
    # Save with garbage collection and image compression
    # 'deflate' compresses streams, 'garbage=4' removes all unused objects
    doc.save(output_path, 
             garbage=4, 
             deflate=True, 
             clean=True)
    
    doc.close()

    initial_size = os.path.getsize(input_path) / 1024
    final_size = os.path.getsize(output_path) / 1024
    
    print(f"Initial: {initial_size:.2f} KB")
    print(f"Final: {final_size:.2f} KB")
    print(f"Reduction: {100 * (initial_size - final_size) / initial_size:.1f}%")

if __name__ == "__main__":
    hard_compress_pdf("input.pdf", "output.pdf")

