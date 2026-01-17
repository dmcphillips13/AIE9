import os
import re
from typing import List, Union


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


class BaseContentLoader:
    def __init__(self, urls: Union[str, List[str]]):
        self.urls = urls if isinstance(urls, list) else [urls]
        self.documents = []

    def load_documents(self) -> List[str]:
        for url in self.urls:
            try:
                self.extract_content(url)
            except Exception as e:
                print(f"Warning: Failed to extract content from {url}: {str(e)}")
        return self.documents

    def extract_content(self, url: str):
        raise NotImplementedError("Subclasses must implement extract_content()")


class YouTubeLoader(BaseContentLoader):
    def extract_content(self, url: str):
        from youtube_transcript_api import YouTubeTranscriptApi

        video_id = self._extract_video_id(url)
        if not video_id:
            raise ValueError(f"Invalid YouTube URL: {url}")

        try:
            api = YouTubeTranscriptApi()
            fetched_transcript = api.fetch(video_id, languages=['en'])
            transcript_data = fetched_transcript.to_raw_data()

            transcript_text = " ".join([entry["text"] for entry in transcript_data])
            self.documents.append(transcript_text)
        except Exception as e:
            raise ValueError(
                f"Error fetching transcript for video {video_id}: {str(e)}. "
                "The video may not have transcripts available."
            )

    def _extract_video_id(self, url: str) -> str:
        pattern = r"(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/)([^&\n?#]+)"
        match = re.search(pattern, url)
        return match.group(1) if match else ""


class PodcastLoader(BaseContentLoader):
    def __init__(self, urls: Union[str, List[str]], api_key: str):
        super().__init__(urls)
        import requests
        from groq import Groq
        self.requests = requests
        self.groq_client = Groq(api_key=api_key)

    def extract_content(self, url: str):
        import tempfile

        print(f"Downloading audio from {url}...")
        response = self.requests.get(url, stream=True, timeout=300)
        response.raise_for_status()

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
            for chunk in response.iter_content(chunk_size=8192):
                temp_file.write(chunk)
            temp_path = temp_file.name

        print("Transcribing audio...")
        try:
            with open(temp_path, 'rb') as audio_file:
                transcription = self.groq_client.audio.transcriptions.create(
                    file=audio_file,
                    model="whisper-large-v3",
                )
            self.documents.append(transcription.text)
        finally:
            os.remove(temp_path)


class BlogLoader(BaseContentLoader):
    def extract_content(self, url: str):
        import requests
        from bs4 import BeautifulSoup

        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")

        for element in soup(["script", "style", "nav", "header", "footer", "aside"]):
            element.decompose()

        article = (soup.find("article") or
                   soup.find("main") or
                   soup.find("div", class_=re.compile("article|content|post", re.I)))

        if article:
            text = article.get_text(separator="\n", strip=True)
        else:
            text = "\n".join([p.get_text(strip=True) for p in soup.find_all("p") if p.get_text(strip=True)])

        if not text:
            raise ValueError(f"No content found on page: {url}")

        self.documents.append(text)


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
