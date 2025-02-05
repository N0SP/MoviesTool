from setuptools import setup


from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text('utf-8')




setup(
    name = 'MovieTool',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    packages = ['MovieTool'],
    version = '3.8.3',
    license = 'MIT',
    description = "Descarga tus peliculas y series, automatiza todo y crea tu propio Netflix (hecho con fines de aprendizaje) completamente funcional (y con más contenido que el de Netflix) haciendo uso de Plex, Ombi y otras tecnologías más. ⭐",
    author = 'N0SP',
    author_email = 'habanferd@gmail.com',
    url = 'https://github.com/N0SP/MoviesTool',
    keywords = ['python', 'torrent', 'torrent-management', 'movies', 'plex', 'hbo', 'series', 'netflix', 'ombi', 'peliculas'],
    classifiers = [
        'Programming Language :: Python :: 3.10'
    ],
    install_requires=["pandas==1.4.4", "python-qbittorrent==0.4.2", "feedparser==6.0.10"]
)