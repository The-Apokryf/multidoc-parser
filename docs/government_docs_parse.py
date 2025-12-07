import marimo

__generated_with = "0.18.3"
app = marimo.App()


@app.cell
def _():
    # import pdfkit
    # import gitpython
    # import markdownify
    # import mistletoe
    # import plutoprint

    import pypandoc
    import requests
    import tempfile
    import pdf2docx 
    import os

    testpdf_url = "https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU19970780483/U/D19970483Lj.pdf"

    def parse_online_pdf(fileurl):
        data = None
        with tempfile.NamedTemporaryFile(delete_on_close=False) as pdf_tmp:
            constitution_load = requests.get(fileurl)
            for datapack in constitution_load.iter_content(chunk_size=128):
                pdf_tmp.write(datapack)
            pdf_tmp.close()
            with tempfile.NamedTemporaryFile(delete_on_close=False) as docx_tmp:
                docx_tmp.close()
            
                docx_tmp_reuse = pdf2docx.Converter(pdf_tmp.name)
                docx_tmp_reuse.convert(docx_tmp.name)    
                docx_tmp_reuse.close()
            
                data = pypandoc.convert_file(docx_tmp.name, "md", format='docx')
                os.unlink(docx_tmp.name)
        
            os.unlink(pdf_tmp.name)
        return data

    with open("constitution.md", "w") as test_doc:
        test_doc.write(parse_online_pdf(testpdf_url))
    return


if __name__ == "__main__":
    app.run()
