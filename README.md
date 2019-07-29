# lobsters-bisque

Simple script to generate a RSS feed for [Lobsters](https://lobste.rs) that
does the following:

- Filter articles by a minimum score
- Utilizes the comments link rather than original article link

Inspired by [Hacker News RSS](https://edavis.github.io/hnrss/).

# CRONTAB

Here is an example of how to use `cron` to execute the script every `10`
minutes:

```
*/10 * * * *    /path/to/lobsters-bisque/lobsters-bisque.py > /path/to/lobsters-bisque.rss
```
