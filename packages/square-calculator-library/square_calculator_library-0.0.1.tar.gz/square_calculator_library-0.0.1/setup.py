import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = [
    "flake8==6.0.0",
    "flake8-isort==6.0.0",
    "isort==5.13.2",
    "mccabe==0.7.0",
    "pycodestyle==2.10.0",
    "pyflakes==3.0.1",
]

setuptools.setup(
    # Имя дистрибутива пакета. Оно должно быть уникальным, поэтому добавление вашего имени пользователя в конце является обычным делом.
    name="square_calculator_library",
    # Номер версии вашего пакета. Обычно используется семантическое управление версиями.
    version="0.0.1",
    # Имя автора.
    author="Aleksandr Buchelnikov",
    # Его почта.
    author_email="al.buchelnikov@gmail.com",
    # Краткое описание, которое будет показано на странице PyPi.
    description="The library allows you to calculate the area of geometric shapes.",
    # Длинное описание, которое будет отображаться на странице PyPi. Использует README.md репозитория для заполнения.
    long_description=long_description,
    # Определяет тип контента, используемый в long_description.
    long_description_content_type="text/markdown",
    # URL-адрес, представляющий домашнюю страницу проекта. Большинство проектов ссылаются на репозиторий.
    url="https://github.com/AVanslov/square_calculator_library",
    # Находит все пакеты внутри проекта и объединяет их в дистрибутив.
    packages=setuptools.find_packages(),
    # requirements или dependencies, которые будут установлены вместе с пакетом, когда пользователь установит его через pip.
    install_requires=requirements,
    # Предоставляет pip некоторые метаданные о пакете. Также отображается на странице PyPi.
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # Требуемая версия Python.
    python_requires='>=3.10',
)
