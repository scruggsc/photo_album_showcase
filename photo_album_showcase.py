def get_album_data(album_input):
    import json
    from urllib.request import urlopen

    request_url = f"https://jsonplaceholder.typicode.com/photos?albumId={album_input}"

    response = urlopen(request_url)
    return json.loads(response.read())


if __name__ == "__main__":
    while True:
        print("Please type the ID of an album or type 'c' to exit: ")
        album_input = input()

        if album_input.lower() == "c":
            exit()

        album_data = get_album_data(album_input)

        if not album_data:
            print("Album not found.\n")
            continue

        print("Album ID\tAlbum Title")
        for album in album_data:
            print(
                f"[{album.get('id')}]\t\t{album.get('title')}"
            )
        print("\n")
