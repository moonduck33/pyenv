# pyenv
# .env Finder

A lightweight, multithreaded Python script that scans domains for exposed `.env` files — often containing sensitive configuration data such as `APP_KEY`, database credentials, or API tokens.

## Features
- Fast concurrent scanning (100 threads by default)  
- Detects exposed `.env` files via HTTPS  
- Saves valid results automatically to `env.txt`  
- Ignores SSL certificate errors silently  
- Clean output — no noisy error logs  

## Requirements
- Python **3.x**
- `requests` library

Install dependencies:

pip install requests

Usage: 
	1.	Put your target domains in a file, one per line:
