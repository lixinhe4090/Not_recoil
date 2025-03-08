# Mouse Recoil Controller 🎯

# If you like this project, please consider giving it a star on GitHub! 🌟 Thank you for your support!🙏

## Hey there, gamers! Welcome to my little project! 🎉

This is a super-handy tool that'll help you dominate your games by automatically compensating for recoil. Just hold down the left mouse button, and it'll smoothly “push down” your aim for you. Trust me, it’s a game-changer! 😎

---

## What does it do?

- **One-Key Toggle**: Press `G` to turn the recoil compensation on or off. Easy peasy! ✨  
- **Auto-Recoil**: Hold down the left mouse button, and it’ll smoothly move your cursor down to simulate pressing the gun down. It’s like having a steady hand! 🤖  
- **Customizable Settings**: You can tweak the speed and interval of the mouse movement to fit your playstyle. Make it just right for you! 🛠️  

---

## How to Use It? 👇

### Getting Started:

1. Download and unzip the files to your computer. (Make sure you’ve got a Windows system, as this tool is made for Windows.) 💻  
2. Find the `./dist` folder. Inside, you’ll see `Moudow.exe`. 📁  

### Running the Program:

1. Double-click `Moudow.exe` to run it. (You might need to run it as an administrator. Right-click and select “Run as administrator.”) 💥  
2. Once it’s running, press `G` to toggle the recoil compensation on or off. Then, hold down the left mouse button and see the magic happen! 🎯  

### Want to Customize? (Optional)

If the default settings aren’t your vibe, you can tweak the parameters in the source code (`MouDow.py`):

- `MOUSE_MOVE_PIXELS`: This controls how many pixels the mouse moves each time. (Default is 3.)  
- `MOVE_INTERVAL_MS`: This sets the delay between each movement in milliseconds. (Default is 5 ms.)  

After making changes, you’ll need to recompile the executable. (Don’t worry, it’s easy!)

### How to Recompile? (Optional)

1. Make sure you have Python installed. (Version 3.8 or higher is recommended.) 🐍  
2. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```
3. Compile the script:
    ```bash
    pyinstaller --onefile MouDow.py
    ```
4. The new Moudow.exe will be in the ./dist folder. Ready to go! 🚀
5. Oh,you need to install some pip packages:
```bash
   pip install keyboard
   pip install pynput
   pip install win32api
   pip install win32con
   pip install threading
```

---

### Important Tips:

1. Game Compatibility: Be cautious! Some games might flag this as cheating. Use it responsibly and check your game’s rules. 🙏
2. Admin Rights: Running the program as an administrator is a good idea to avoid any hiccups. 💪
3. Exiting the Program: Press Ctrl+C or close the program window to exit. Easy! 👋

---

### Project Structure:
```
MouDow/
├── build/
    └── (There are too many files,I don't want to talk about it😁)
├── MouDow.py
├── MouDow.spec
└── dist/
    └── MouDow.exe
```

---

### Want to Contribute? 🤝

Got ideas or suggestions? Feel free to open an issue or submit a pull request! Let’s make this tool even better together! 🤝

---

### Contact Me:

Got questions or just want to chat? Hit me up via email! 📧
My email is: [lixinhe3465@163.com]
I am still a (junior high school) student, and there may be no way to reply in time, but I will check my email regularly and remember to indicate the purpose in the title~
---

## Hope you enjoy this tool! Happy gaming, and may the recoil be ever in your favor! 😎