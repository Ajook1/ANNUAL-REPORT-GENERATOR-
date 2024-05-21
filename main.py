# from flask import Flask, request, render_template_string, send_file, jsonify
# from werkzeug.utils import secure_filename
# import os
# import PyPDF2
# from transformers import pipeline

# app = Flask(__name__)

# # Ensure the upload folder exists
# UPLOAD_FOLDER = 'uploads'
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# HTML_TEMPLATE = '''
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Academic Report Generator</title>
#     <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
#     <style>
#         body {
#             font-family: 'Roboto', sans-serif;
#             background-color: #f8f9fa;
#         }

#         header {
#             background: linear-gradient(45deg, #d2b48c, #f5f5dc);
#             box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
#         }

#         .navbar {
#             padding: 15px 20px;
#         }

#         .navbar-brand {
#             display: flex;
#             align-items: center;
#         }

#         .navbar-brand img {
#             height: 50px;
#             margin-right: 15px;
#         }

#         .navbar-brand h1 {
#             font-size: 1.8em;
#             color: #333;
#             margin: 0;
#         }

#         main {
#             max-width: 900px;
#             margin: 30px auto;
#             padding: 20px;
#         }

#         .card {
#             margin-bottom: 20px;
#             background-color: #fff;
#             border: none;
#             box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
#             border-radius: 10px;
#         }

#         .card-body {
#             padding: 30px;
#         }

#         .card-title {
#             color: #8b4513;
#         }

#         .card-text {
#             color: #8b4513;
#         }

#         .download-report {
#             text-align: center;
#             margin-top: 30px;
#         }

#         .download-report button {
#             padding: 15px 30px;
#             font-size: 1.2em;
#             color: white;
#             background-color: #8b4513;
#             border: none;
#             border-radius: 5px;
#             cursor: pointer;
#             transition: background-color 0.2s;
#         }

#         .download-report button:hover {
#             background-color: #6b3a0a;
#         }
#     </style>
# </head>
# <body>
#     <header>
#         <nav class="navbar navbar-expand-lg navbar-light">
#             <div class="container">
#                 <a class="navbar-brand" href="#">
#                     <img src="logo.png" alt="Logo">
#                     <h1>Academic Report Generator</h1>
#                 </a>
#             </div>
#         </nav>
#     </header>
#     <main class="container">
#         <section class="upload-options">
#             <div class="card">
#                 <div class="card-body text-center">
#                     <h2 class="card-title">Upload Single PDF</h2>
#                     <p class="card-text">Upload a single PDF file to generate a summarized report.</p>
#                     <input type="file" id="singlePdf" accept=".pdf" class="form-control">
#                 </div>
#             </div>
#             <div class="card">
#                 <div class="card-body text-center">
#                     <h2 class="card-title">Upload Multiple PDFs</h2>
#                     <p class="card-text">Upload multiple PDF files to generate a comprehensive summarized report.</p>
#                     <input type="file" id="multiplePdfs" accept=".pdf" multiple class="form-control">
#                 </div>
#             </div>
#             <div class="card">
#                 <div class="card-body text-center">
#                     <h2 class="card-title">Upload PDF from URL</h2>
#                     <p class="card-text">Provide a URL to a PDF file for report summarization.</p>
#                     <input type="url" id="pdfUrl" placeholder="Enter PDF URL" class="form-control">
#                 </div>
#             </div>
#         </section>
#         <div class="download-report">
#             <button id="downloadBtn" class="btn btn-primary btn-lg">Download Summarized Report</button>
#         </div>
#     </main>
#     <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
#     <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"></script>
#     <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
#     <script>
#         document.getElementById('downloadBtn').addEventListener('click', function() {
#             const singlePdf = document.getElementById('singlePdf').files[0];
#             const multiplePdfs = document.getElementById('multiplePdfs').files;
#             const pdfUrl = document.getElementById('pdfUrl').value;

#             const formData = new FormData();
#             if (singlePdf) {
#                 formData.append('file', singlePdf);
#             } else if (multiplePdfs.length > 0) {
#                 for (const file of multiplePdfs) {
#                     formData.append('file', file);
#                 }
#             } else if (pdfUrl) {
#                 formData.append('url', pdfUrl);
#             } else {
#                 alert('Please upload a PDF file or provide a URL.');
#                 return;
#             }

#             fetch('/upload', {
#                 method: 'POST',
#                 body: formData,
#             })
#             .then(response => response.blob())
#             .then(blob => {
#                 const url = window.URL.createObjectURL(blob);
#                 const a = document.createElement('a');
#                 a.style.display = 'none';
#                 a.href = url;
#                 a.download = 'summary.txt';
#                 document.body.appendChild(a);
#                 a.click();
#                 window.URL.revokeObjectURL(url);
#                 alert('Summarized report is ready for download.');
#             })
#             .catch(error => {
#                 console.error('Error:', error);
#                 alert('Failed to generate summary. Please try again.');
#             });
#         });
#     </script>
# </body>
# </html>
# '''

# @app.route('/')
# def index():
#     return render_template_string(HTML_TEMPLATE)

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if 'file' not in request.files and 'url' not in request.form:
#         return jsonify({'error': 'No file or URL provided'}), 400

#     if 'file' in request.files:
#         files = request.files.getlist('file')
#         text = ""
#         for file in files:
#             filename = secure_filename(file.filename)
#             filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#             file.save(filepath)
#             text += extract_text_from_pdf(filepath) + "\n"
#     elif 'url' in request.form:
#         url = request.form['url']
#         # Code to handle URL fetching and text extraction
#         # For simplicity, this example does not implement URL fetching
#         text = "URL fetching not implemented in this example."

#     if not text:
#         return jsonify({'error': 'Failed to extract text from PDF'}), 500

#     summary = summarize_text(text)
#     summary_filename = 'summary.txt'
#     summary_filepath = os.path.join(app.config['UPLOAD_FOLDER'], summary_filename)
#     with open(summary_filepath, 'w') as f:
#         f.write(summary)

#     return send_file(summary_filepath, as_attachment=True)

# def extract_text_from_pdf(pdf_path):
#     try:
#         with open(pdf_path, 'rb') as file:
#             reader = PyPDF2.PdfFileReader(file)
#             text = ''
#             for page_num in range(reader.numPages):
#                 text += reader.getPage(page_num).extract_text()
#         return text
#     except Exception as e:

#         print(f"Error reading PDF: {e}")
#         return None

# def summarize_text(text):
#     try:
#         summarizer = pipeline("summarization")
#         summary = summarizer(text, max_length=200, min_length=50, do_sample=False)
#         return summary[0]['summary_text']
#     except Exception as e:
#         print(f"Error summarizing text: {e}")
#         return "Error in summarizing text."

# if __name__ == '_main_':
#     app.run(debug=True)


from flask import Flask, request, render_template_string, send_file, jsonify
from werkzeug.utils import secure_filename
import os
import PyPDF2
from transformers import pipeline

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Academic Report Generator</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            background-color: #f8f9fa;
        }

        header {
            background: linear-gradient(45deg, #d2b48c, #f5f5dc);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        .navbar {
            padding: 15px 20px;
        }

        .navbar-brand {
            display: flex;
            align-items: center;
        }

        .navbar-brand img {
            height: 50px;
            margin-right: 15px;
        }

        .navbar-brand h1 {
            font-size: 1.8em;
            color: #333;
            margin: 0;
        }

        main {
            max-width: 900px;
            margin: 30px auto;
            padding: 20px;
        }

        .card {
            margin-bottom: 20px;
            background-color: #fff;
            border: none;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            border-radius: 10px;
        }

        .card-body {
            padding: 30px;
        }

        .card-title {
            color: #8b4513;
        }

        .card-text {
            color: #8b4513;
        }

        .download-report {
            text-align: center;
            margin-top: 30px;
        }

        .download-report button {
            padding: 15px 30px;
            font-size: 1.2em;
            color: white;
            background-color: #8b4513;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.2s;
        }

        .download-report button:hover {
            background-color: #6b3a0a;
        }
    </style>
</head>
<body>
    <header>
        <nav class="navbar navbar-expand-lg navbar-light">
            <div class="container">
                <a class="navbar-brand" href="#">
                    <img src="logo.png" alt="Logo">
                    <h1>Academic Report Generator</h1>
                </a>
            </div>
        </nav>
    </header>
    <main class="container">
        <section class="upload-options">
            <div class="card">
                <div class="card-body text-center">
                    <h2 class="card-title">Upload Single PDF</h2>
                    <p class="card-text">Upload a single PDF file to generate a summarized report.</p>
                    <input type="file" id="singlePdf" accept=".pdf" class="form-control">
                </div>
            </div>
            <div class="card">
                <div class="card-body text-center">
                    <h2 class="card-title">Upload Multiple PDFs</h2>
                    <p class="card-text">Upload multiple PDF files to generate a comprehensive summarized report.</p>
                    <input type="file" id="multiplePdfs" accept=".pdf" multiple class="form-control">
                </div>
            </div>
            <div class="card">
                <div class="card-body text-center">
                    <h2 class="card-title">Upload PDF from URL</h2>
                    <p class="card-text">Provide a URL to a PDF file for report summarization.</p>
                    <input type="url" id="pdfUrl" placeholder="Enter PDF URL" class="form-control">
                </div>
            </div>
        </section>
        <div class="download-report">
            <button id="downloadBtn" class="btn btn-primary btn-lg">Download Summarized Report</button>
        </div>
    </main>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    <script>
        document.getElementById('downloadBtn').addEventListener('click', function() {
            const singlePdf = document.getElementById('singlePdf').files[0];
            const multiplePdfs = document.getElementById('multiplePdfs').files;
            const pdfUrl = document.getElementById('pdfUrl').value;

            const formData = new FormData();
            if (singlePdf) {
                formData.append('file', singlePdf);
            } else if (multiplePdfs.length > 0) {
                for (const file of multiplePdfs) {
                    formData.append('file', file);
                }
            } else if (pdfUrl) {
                formData.append('url', pdfUrl);
            } else {
                alert('Please upload a PDF file or provide a URL.');
                return;
            }

            fetch('/upload', {
                method: 'POST',
                body: formData,
            })
            .then(response => response.blob())
            .then(blob => {
                const url = window.URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.style.display = 'none';
                a.href = url;
                a.download = 'summary.txt';
                document.body.appendChild(a);
                a.click();
                window.URL.revokeObjectURL(url);
                alert('Summarized report is ready for download.');
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Failed to generate summary. Please try again.');
            });
        });
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files and 'url' not in request.form:
        return jsonify({'error': 'No file or URL provided'}), 400

    text = ""
    if 'file' in request.files:
        files = request.files.getlist('file')
        for file in files:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            extracted_text = extract_text_from_pdf(filepath)
            if extracted_text:
                text += extracted_text + "\n"
            else:
                return jsonify({'error': 'Failed to extract text from PDF'}), 500
    elif 'url' in request.form:
        url = request.form['url']
        text = "URL fetching not implemented in this example."

    if text:
        summary = summarize_text(text)
    else:
        return jsonify({'error': 'No text extracted from files'}), 500

    summary_filename = 'summary.txt'
    summary_filepath = os.path.join(app.config['UPLOAD_FOLDER'], summary_filename)
    with open(summary_filepath, 'w') as f:
        f.write(summary)

    return send_file(summary_filepath, as_attachment=True)

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ''
        for page_num in range(reader.numPages):
            page_text = reader.getPage(page_num).extract_text()
            if page_text:
                text += page_text
        return text

def summarize_text(text):
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=200, min_length=50, do_sample=False)
    return summary[0]['summary_text']

if __name__ == '_main_':
    app.run(debug=True)

