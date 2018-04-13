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

By default, results will be printed to the stdout.

If you want to write to a file, just uncomment one line in the `main.py` file (you should know where to uncomment).
Output file will be named like this `fvl-contribution-rocky-{current_week}-{current_date}.md`.
For example, `fvl-contribution-rocky-21-20170406.md`.

#### Content of the output

This is a sample of the output in plain markdown.

```markdown
### Team target

|  No.  |  Item   |  Target  |  Actual  |  Actual remain  |  Target to date  |  Target to date remain  |  Behind schedule  |
|:-----:|:-------:|:--------:|:--------:|:---------------:|:----------------:|:-----------------------:|:-----------------:|
|   1   | Commits |   129    |    28    |       101       |        29        |           100           |         1         |
|   2   | Reviews |   616    |    71    |       545       |       142        |           474           |        71         |

### Member target (commit/review)

|  No.  |  Member  |  Target  |  Actual  |  Actual remain  |  Target to date  |  Target to date remain  |  Behind schedule  |
|:-----:|:--------:|:--------:|:--------:|:---------------:|:----------------:|:-----------------------:|:-----------------:|
|   1   |   Kien   |   0/0    |  18/48   |     -18/-48     |       0/0        |           0/0           |      -18/-48      |
|   2   |   Dai    |   0/0    |   1/0    |      -1/0       |       0/0        |           0/0           |       -1/0        |
|   3   |   Nam    |  43/205  |   4/11   |     39/194      |       9/47       |         34/158          |       5/36        |
|   4   |  Duong   |  43/205  |   4/7    |     39/198      |       9/47       |         34/158          |       5/40        |
|   5   |   Vinh   |  43/206  |   1/5    |     42/201      |       9/47       |         34/159          |       8/42        |
```

This is a sample of the output in html table.

### Team target

|  No.  |  Item   |  Target  |  Actual  |  Actual remain  |  Target to date  |  Target to date remain  |  Behind schedule  |
|:-----:|:-------:|:--------:|:--------:|:---------------:|:----------------:|:-----------------------:|:-----------------:|
|   1   | Commits |   129    |    28    |       101       |        29        |           100           |         1         |
|   2   | Reviews |   616    |    71    |       545       |       142        |           474           |        71         |

### Member target (commit/review)

|  No.  |  Member  |  Target  |  Actual  |  Actual remain  |  Target to date  |  Target to date remain  |  Behind schedule  |
|:-----:|:--------:|:--------:|:--------:|:---------------:|:----------------:|:-----------------------:|:-----------------:|
|   1   |   Kien   |   0/0    |  18/48   |     -18/-48     |       0/0        |           0/0           |      -18/-48      |
|   2   |   Dai    |   0/0    |   1/0    |      -1/0       |       0/0        |           0/0           |       -1/0        |
|   3   |   Nam    |  43/205  |   4/11   |     39/194      |       9/47       |         34/158          |       5/36        |
|   4   |  Duong   |  43/205  |   4/7    |     39/198      |       9/47       |         34/158          |       5/40        |
|   5   |   Vinh   |  43/206  |   1/5    |     42/201      |       9/47       |         34/159          |       8/42        |
