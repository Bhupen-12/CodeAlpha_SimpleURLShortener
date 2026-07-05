# CodeAlpha_SimpleURLShortener
# Simple URL Shortener

A simple URL Shortener web application built using **Python (Flask)** and **SQLite**.

## Features

- Shorten long URLs into unique short links.
- Store URL mappings in an SQLite database.
- Redirect users from short URLs to the original URLs.
- Simple and user-friendly web interface.

## Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- HTML

## Project Structure

```
url-shortener/
│── app.py
│── requirements.txt
│── README.md
│── .gitignore
└── templates/
    └── index.html
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/simple-url-shortener.git
```

2. Move into the project folder:

```bash
cd simple-url-shortener
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python app.py
```

5. Open your browser and visit:

```
http://127.0.0.1:5000
```

## API

### Create a Short URL

**POST** `/shorten`

Example request:

```json
{
  "url": "https://www.google.com"
}
```

Example response:

```json
{
  "short_url": "http://127.0.0.1:5000/Ab12Cd"
}
```

## License

This project is open source and available under the Code_Alpha Licence.