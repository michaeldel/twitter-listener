# Twitter Listener
Simple program listening some Twitter users' feed and storing statuses to a file (by default, other backends like Discord Webhooks are also availables).

## Usage
First set your twitter environment variables as follows:
```bash
export TWITTER_CONSUMER_KEY=...
export TWITTER_CONSUMER_SECRET=...
export TWITTER_TOKEN8KEY=...
export TWITTER_TOKEN_SECRET=...
```
Then run the program using
```
pip install -r requirements.txt
python twitter-listener.py <user_1> [user_2] [...] [-f db_file] [--file db_file]
```
`db_file` defaults to `db.json`. More options may be found using the `--help` flag.
## Example:
```
python twitter-listener.py metaphorminute -f metaphorminute_statuses.json
```
