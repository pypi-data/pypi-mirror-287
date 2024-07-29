import subprocess
import sys
import time

def install_ollama(stdscr):
    if sys.platform == "linux":
        stdscr.clear()
        command = "curl -fsSL https://ollama.com/install.sh | sh"
        process = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
        )
        output = ""
        max_y, max_x = stdscr.getmaxyx()
        current_y = 0

        for line in process.stdout:
            output += line
            if current_y < max_y - 1:
                stdscr.addstr(current_y, 0, line)
                current_y += 1
            else:
                stdscr.move(0, 0)
                stdscr.deleteln()
            stdscr.refresh()
            stdscr.move(max_y - 2, 0)
            stdscr.insertln()
            stdscr.addstr(max_y - 2, 0, line.strip())

        process.wait()


        if process.returncode != 0:
            raise subprocess.CalledProcessError(process.returncode, command, output)
        if process.returncode == 0:
            stdscr.clear()
            stdscr.addstr(1, 0, ">>> Ollama installed ✅")
            stdscr.refresh()
            time.sleep(2)
            return True

    else:
        stdscr.addstr(1, 0, "Your pc does not support this application.")
        stdscr.refresh()
        stdscr.getch()


def check_ollama_installation(stdscr):
    if (
        subprocess.run(["ollama", "--version"], stdout=subprocess.DEVNULL).returncode
        == 1
    ):
        stdscr.addstr(3, 0, ">>> Ollama is installed ✅")
        stdscr.refresh()
        time.sleep(2)
        return True
    else:
        stdscr.clear()
        stdscr.addstr(1, 0, ">>> Ollama is not installed")
        stdscr.addstr(2, 0, ">>> Do you want to install it (y/n)?")
        stdscr.refresh()
        key = stdscr.getch()
        if key == ord("y"):
            installed = install_ollama(stdscr)
            if installed:
                return True
            else:
                return False
        else:
            stdscr.addstr(3, 0, "Press any key to leave...")
            stdscr.refresh()
            stdscr.getch()
            return False
