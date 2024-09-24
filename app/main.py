import requests
from bs4 import BeautifulSoup as bf






class PageParser:
    def __init__(self, url):
        self.target_url = url
        self.response = requests.get(self.target_url)
        self.soup = bf(self.response.text, "html.parser")

    def show_raw(self):
        print(self.response.content)
        print(self.response.status_code)
        print(self.response.headers)

    def find_all_p(self):
        paragraphs = self.soup.find_all('p')
        # Extract and print the text within the <p> tags
        for p in paragraphs:
            print(p.text)

    def find_audios(self):
        # Find all <source> or <audio> tags that may contain .m4a files
        m4a_files = []

        # Searching for <audio> tags
        for audio in self.soup.find_all('audio'):
            if audio.get('src') and audio['src'].endswith('.m4a'):
                m4a_files.append(audio['src'])

        # Searching for <source> tags
        for source in self.soup.find_all('source'):
            if source.get('src') and source['src'].endswith('.m4a'):
                m4a_files.append(source['src'])

        # Searching for direct <a> tags linking to .m4a files
        for link in self.soup.find_all('a', href=True):
            if link['href'].endswith('.m4a'):
                m4a_files.append(link['href'])

        # Print all the .m4a links found
        for m4a in m4a_files:
            print(m4a)






def main():
    pp = PageParser('http://www.ychy.org/play/16516-0-1.html')
    pp.find_all_p()

if __name__ == '__main__':
    main()