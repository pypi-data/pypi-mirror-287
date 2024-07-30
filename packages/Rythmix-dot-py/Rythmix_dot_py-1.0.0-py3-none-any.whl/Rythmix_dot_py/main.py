from youtubesearchpython import VideosSearch
from yt_dlp import YoutubeDL
import curses
import vlc
import sys


def init_colors():
    curses.start_color()
    curses.init_pair(1, 231, 196)  # Red background, white text
    curses.init_pair(2, curses.COLOR_BLACK, 231)  # Black text, white background
    curses.init_pair(3, 231, 88)  # Blue background, white text


def searchSong(query):
    try:
        results = VideosSearch(query, limit=1)
        return results.result()['result'][0]
    except Exception as e:
        print(f"An error occurred in searchSong: {e}")
        return None


def playback_menu(stdscr, player, is_playing, song_title):
    h, w = stdscr.getmaxyx()
    menu = ["Play/Pause", "Stop", "Quit"]
    current_row = 0

    while player.get_state() != vlc.State.Ended:
        stdscr.clear()
        stdscr.addstr(0, 0, f"Playing: {song_title}", curses.color_pair(3))  # Show song title

        for idx, item in enumerate(menu):
            x = w // 2 - len(item) // 2
            y = h // 2 - len(menu) // 2 + idx
            if y < h and x < w:
                if idx == current_row:
                    stdscr.attron(curses.color_pair(1))
                    stdscr.addstr(y, x, item)
                    stdscr.attroff(curses.color_pair(1))
                else:
                    stdscr.attron(curses.color_pair(2))
                    stdscr.addstr(y, x, item)
                    stdscr.attroff(curses.color_pair(2))
            else:
                print(f"Warning: Attempting to write outside screen bounds at (y={y}, x={x})")

        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP:
            current_row = (current_row - 1) % len(menu)
        elif key == curses.KEY_DOWN:
            current_row = (current_row + 1) % len(menu)
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if menu[current_row] == "Play/Pause":
                if is_playing:
                    player.pause()
                else:
                    player.play()
                is_playing = not is_playing
            elif menu[current_row] == "Stop":
                player.stop()
                break
            elif menu[current_row] == "Quit":
                player.stop()
                sys.exit()

    return is_playing


def playSong(url, stdscr):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'quiet': True,
            'no_warnings': True
        }

        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            audio_url = info_dict['url']
            song_title = info_dict['title']

            Instance = vlc.Instance('--no-xlib -q > /dev/null 2>&1')
            Instance.log_unset()
            player = Instance.media_player_new()

            media = Instance.media_new(audio_url)
            player.set_media(media)
            player.play()

            is_playing = True

            playback_menu(stdscr, player, is_playing, song_title)

    except Exception as e:
        print(f"An error occurred in playSong: {e}")


def main_menu(stdscr):
    init_colors()
    curses.curs_set(0)
    stdscr.bkgd(' ', curses.color_pair(3))
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    menu = ["Play Song", "Exit"]
    current_row = 0

    ascii_art = r"""
    ____        __  __              _                   
   / __ \__  __/ /_/ /_  ____ ___  (_)  __  ____  __  __
  / /_/ / / / / __/ __ \/ __ `__ \/ / |/_/ / __ \/ / / /
 / _, _/ /_/ / /_/ / / / / / / / / />  <_ / /_/ / /_/ / 
/_/ |_|\__, /\__/_/ /_/_/ /_/ /_/_/_/|_(_) .___/\__, /  
      /____/                            /_/    /____/   
      by Arslaan Pathan (@RealArslaanYT)
    """

    while True:
        stdscr.clear()
        art_y = h // 4 - len(ascii_art.splitlines()) // 2
        art_x = w // 2 - max(len(line) for line in ascii_art.splitlines()) // 2
        for i, line in enumerate(ascii_art.splitlines()):
            stdscr.addstr(art_y + i, art_x, line, curses.color_pair(3))

        for idx, item in enumerate(menu):
            x = w // 2 - len(item) // 2
            y = h // 2 - len(menu) // 2 + len(ascii_art.splitlines()) + idx
            if y < h and x < w:
                if idx == current_row:
                    stdscr.attron(curses.color_pair(1))
                    stdscr.addstr(y, x, item)
                    stdscr.attroff(curses.color_pair(1))
                else:
                    stdscr.attron(curses.color_pair(2))
                    stdscr.addstr(y, x, item)
                    stdscr.attroff(curses.color_pair(2))
            else:
                print(f"Warning: Attempting to write outside screen bounds at (y={y}, x={x})")
        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP:
            current_row = (current_row - 1) % len(menu)
        elif key == curses.KEY_DOWN:
            current_row = (current_row + 1) % len(menu)
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if menu[current_row] == "Play Song":
                stdscr.clear()
                stdscr.addstr(h // 2 - 1, w // 2 - 10, "Enter search query: ")
                stdscr.refresh()

                curses.echo()
                query = ""
                while True:
                    stdscr.clear()
                    stdscr.addstr(h // 2 - 1, w // 2 - 10, "Enter search query: ")

                    input_x = w // 2 - len(query) // 2
                    if input_x >= 0 and h // 2 >= 0:
                        stdscr.addstr(h // 2, input_x, query, curses.color_pair(2))

                    stdscr.refresh()
                    key = stdscr.getch()

                    if key in [10, 13]:
                        break
                    elif key == 27:
                        return
                    elif key == curses.KEY_BACKSPACE or key == 127:
                        query = query[:-1]
                    else:
                        query += chr(key) if key < 256 else ''

                curses.noecho()

                song_info = searchSong(query)
                if song_info:
                    message = f"Playing: {song_info['title']}"
                    x = w // 2 - len(message) // 2
                    y = h // 2
                    if x >= 0 and y >= 0:
                        stdscr.clear()
                        stdscr.addstr(y, x, message, curses.color_pair(2))
                        stdscr.refresh()
                        playSong(song_info['link'], stdscr)
                        stdscr.clear()
                    else:
                        stdscr.addstr(0, 0, "Terminal window is too small to display message.")
                        stdscr.refresh()
                        stdscr.getch()
                stdscr.getch()
            elif menu[current_row] == "Exit":
                break


def main():
    curses.wrapper(main_menu)


if __name__ == "__main__":
    main()
