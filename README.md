# Renard

A webform to send long-term care applications to German health insurers.
This is a work-in-progress to eventually replace <https://github.com/khaldoun-xyz/renard>.

## set up

- in root, run `docker build -t renard .`
- in root, run `docker run -p 8000:8000 --env-file=.env renard`
