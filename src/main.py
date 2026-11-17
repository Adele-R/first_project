import os
from dotenv import load_dotenv


def print_author():
    load_dotenv()                      # подхватывает переменные из .env в окружение
    author = os.getenv("AUTHOR")
    print(f"Автор проекта: {author}")


if __name__ == "__main__":
    print_author()