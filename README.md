# Twitter Listener
Simple program listening some Twitter users' feed and storing statuses to a file.

## Usage
```
pip install -r requirements.txt
python twitter-listener.py <user_1> [user_2] [...] [-f db_file] [--file db_file]
```
`db_file` defaults to `db.json`
## Example:
```
python twitter-listener.py metaphorminute -f metaphorminute_statuses.json
```