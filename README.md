# Readme if you want

## Disclaimer

This tool is heavily non-D.R.Y, glhf :))

## Install requirements

```bash
pip install -r requirements.txt
```

## Configure some information in configuration.py file

Just open it and you will understand how to change the numbers, names.

For fashion purpose, I will change configuration file to YAML format (j/k).

## Run, run, run

```bash
python main.py
```

### Output

#### Output destinations

By default, results will be printed to the stdout and write to a file with name
like this `fvl-contribution-rocky-{current_week}-{current_date}.md`.
For example, `fvl-contribution-rocky-21-20170406.md`.

#### Content of the output

I provided a sample output files in samples directory.

This is a sample of the output in plain markdown.

```markdown
### Team target

|  No.  |  Item   |  Target  |  Actual  |  Actual remain  |  Target to date  |  Target to date remain  |  Actual to date remain  |
|:-----:|:-------:|:--------:|:--------:|:---------------:|:----------------:|:-----------------------:|:-----------------------:|
|   1   | Commits |   129    |    25    |       104       |        24        |           105           |           -1            |
|   2   | Reviews |   616    |    66    |       550       |       118        |           498           |           52            |

### Member target (commit/review)

|  No.  |  Member  |  Target  |  Actual  |  Actual remain  |  Target to date  |  Target to date remain  |  Actual to date remain  |
|:-----:|:--------:|:--------:|:--------:|:---------------:|:----------------:|:-----------------------:|:-----------------------:|
|   1   |   Kien   |   0/0    |  16/45   |     -16/-45     |       0/0        |           0/0           |         -16/-45         |
|   2   |   Dai    |   0/0    |   1/0    |      -1/0       |       0/0        |           0/0           |          -1/0           |
|   3   |   Nam    |  43/205  |   4/10   |     39/195      |       8/39       |         35/166          |          4/29           |
|   4   |  Duong   |  43/205  |   3/6    |     40/199      |       8/39       |         35/166          |          5/33           |
|   5   |   Vinh   |  43/206  |   1/5    |     42/201      |       8/39       |         35/167          |          7/34           |
```

This is a sample of the output in html table.

### Team target

|  No.  |  Item   |  Target  |  Actual  |  Actual remain  |  Target to date  |  Target to date remain  |  Actual to date remain  |
|:-----:|:-------:|:--------:|:--------:|:---------------:|:----------------:|:-----------------------:|:-----------------------:|
|   1   | Commits |   129    |    25    |       104       |        24        |           105           |           -1            |
|   2   | Reviews |   616    |    66    |       550       |       118        |           498           |           52            |

### Member target (commit/review)

|  No.  |  Member  |  Target  |  Actual  |  Actual remain  |  Target to date  |  Target to date remain  |  Actual to date remain  |
|:-----:|:--------:|:--------:|:--------:|:---------------:|:----------------:|:-----------------------:|:-----------------------:|
|   1   |   Kien   |   0/0    |  16/45   |     -16/-45     |       0/0        |           0/0           |         -16/-45         |
|   2   |   Dai    |   0/0    |   1/0    |      -1/0       |       0/0        |           0/0           |          -1/0           |
|   3   |   Nam    |  43/205  |   4/10   |     39/195      |       8/39       |         35/166          |          4/29           |
|   4   |  Duong   |  43/205  |   3/6    |     40/199      |       8/39       |         35/166          |          5/33           |
|   5   |   Vinh   |  43/206  |   1/5    |     42/201      |       8/39       |         35/167          |          7/34           |
