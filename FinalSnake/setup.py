import cx_Freeze
executables = [cx_Freeze.Executable("snake.py")]

cx_Freeze.setup (
    name = "SnakeGame",
    version = "1.0",
    options = {"build_exe":{"packages":["pygame"],"include_files":["apple.jpg","banana.jpg",
                                                                   "button.wav","credit.mp3",
                                                                   "food2.wav","front.jpg",
                                                                   "grapes.jpg",
                                                                   "introsnake.png",
                                                                   "mango.png","snake.png",
                                                                   "snakehead1.png"]}},
    description = "Snake Game project",
    executables = executables
    )
