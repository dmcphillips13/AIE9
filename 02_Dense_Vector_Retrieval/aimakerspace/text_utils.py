import os
from typing import List


class BaseFileLoader:
    def __init__(self, path: str, encoding: str = "utf-8", fileType: str = ".txt"):
        self.documents = []
        self.path = path
        self.encoding = encoding
        self.fileType = fileType

    def load(self):
        if os.path.isdir(self.path):
            self.load_directory()
        elif os.path.isfile(self.path) and self.path.endswith(self.fileType):
            self.load_file()
        else:
            raise ValueError(
                f"Provided path is neither a valid directory nor a {self.fileType} file."
            )

    def load_directory(self):
        for root, _, files in os.walk(self.path):
            for file in files:
                if file.endswith(self.fileType):
                    file_path = os.path.join(root, file)
                    # Temporarily set path to current file for load_file to work
                    original_path = self.path
                    self.path = file_path
                    self.load_file()
                    self.path = original_path

    def load_file(self):
        raise NotImplementedError("Subclasses must implement load_file()")

    def load_documents(self):
        self.load()
        return self.documents


class TextFileLoader(BaseFileLoader):
    def __init__(self, path: str, encoding: str = "utf-8"):
        super().__init__(path, encoding, fileType=".txt")

    def load_file(self):
        with open(self.path, "r", encoding=self.encoding) as f:
            self.documents.append(f.read())


class PdfFileLoader(BaseFileLoader):
    def __init__(self, path: str, encoding: str = "utf-8"):
        super().__init__(path, encoding, fileType=".pdf")
        try:
            from pypdf import PdfReader
            self.PdfReader = PdfReader
        except ImportError:
            raise ImportError(
                "pypdf is required for PDF support. Install it with: uv sync"
            )

    def load_file(self):
        try:
            reader = self.PdfReader(self.path)
            text_content = []
            for page in reader.pages:
                text_content.append(page.extract_text())
            combined_text = "\n".join(text_content)
            self.documents.append(combined_text)
        except Exception as e:
            raise ValueError(
                f"Error reading PDF file {self.path}: {str(e)}"
            )


class CharacterTextSplitter:
    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
    ):
        assert (
            chunk_size > chunk_overlap
        ), "Chunk size must be greater than chunk overlap"

        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split(self, text: str) -> List[str]:
        chunks = []
        for i in range(0, len(text), self.chunk_size - self.chunk_overlap):
            chunks.append(text[i : i + self.chunk_size])
        return chunks

    def split_texts(self, texts: List[str]) -> List[str]:
        chunks = []
        for text in texts:
            chunks.extend(self.split(text))
        return chunks


if __name__ == "__main__":
    loader = TextFileLoader("data/KingLear.txt")
    loader.load()
    splitter = CharacterTextSplitter()
    chunks = splitter.split_texts(loader.documents)
    print(len(chunks))
    print(chunks[0])
    print("--------")
    print(chunks[1])
    print("--------")
    print(chunks[-2])
    print("--------")
    print(chunks[-1])
