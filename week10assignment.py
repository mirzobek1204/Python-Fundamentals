def organize_books(reading_log):
    library = {}
    for genre_list in reading_log:
        genre, title, pages = genre_list.split(",")
        pages = int(pages)
        if genre not in library:
            library[genre] = []
        library[genre].append((title, pages))
    return library
def print_genre_stats(library_dict):
    for genre, books in library_dict.items():
        total_pages = 0
        for title, pages in books:
            total_pages += pages

        print(f"{genre}: {total_pages} pages total")

reading_log = [
    "Fantasy,The Hobbit,310",
    "SciFi,Dune,412",
    "Fantasy,Harry Potter,223",
    "Mystery,Sherlock Holmes,300",
    "SciFi,Ender's Game,324",
    "Fantasy,The Alchemist,160"
]
library = organize_books(reading_log)
print_genre_stats(library)


