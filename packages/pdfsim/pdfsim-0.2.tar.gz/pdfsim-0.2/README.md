# PDF Similarity Matcher

The **PDF Similarity Matcher** is a command-line tool for finding and displaying PDF documents similar to a given input PDF based on extracted text features. It leverages text extraction and similarity comparison to help you identify relevant matches from a directory of PDFs.

## Features

- Extracts text from PDF files.
- Processes and compares features from multiple PDFs.
- Calculates similarity scores between an input PDF and PDFs in the directory.
- Optionally displays detailed key-value feature information for similar PDFs.

## Installation

Follow these steps to install and set up the PDF Similarity Matcher:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/pdfsim.git
    cd pdfsim
    ```

2. **Create a virtual environment:**

    ```bash
    python3 -m venv venv
    ```

3. **Activate the virtual environment:**

    - **On Windows:**

      ```bash
      venv\Scripts\activate
      ```

    - **On macOS/Linux:**

      ```bash
      source venv/bin/activate
      ```

4. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

    Ensure `requirements.txt` includes the necessary libraries:

    ```
    PyPDF2
    scikit-learn
    nltk
    ```

## Usage

To find similar PDFs, use the following command:

```bash
python3 main.py -d <directory_containing_pdf> -i <input_pdf> -t <top_n> [-kv]
```

## Arguments
- -d, --database (required): Path to the directory containing PDF files to compare against.
- -i, --input (required): Path to the input PDF file you want to compare.
- -t, --top (optional, default: 1): Number of top similar PDFs to display.
- -kv (optional): Enable detailed key-value feature output for similar PDFs.
