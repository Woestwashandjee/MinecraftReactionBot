import time, os
import keyboard

def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line
if __name__ == "__main__":
    logfile = open(os.getenv("APPDATA")+"/.minecraft/logs/latest.log", "r")
    loglines = follow(logfile)
    for line in loglines:
        if "[Client thread/INFO]: [CHAT]" and "reaction" in line.lower()\
                and "won in" not in line.lower()\
                and "nobody got" not in line.lower():
            insert = ' '.join(line.split()[6:-2])
            keyboard.write(insert)
            time.sleep(1)
            keyboard.press_and_release('enter')
            time.sleep(0.1)
            keyboard.press_and_release('t')
            time.sleep(0.5)
            keyboard.write('fast as fck boiis')
            time.sleep(0.5)
            keyboard.press_and_release('enter')
            time.sleep(0.5)
            keyboard.press_and_release('t')
