# plpred

By Maria Clara Martins

A protein subcellular location prediction program

## Setup

```
$ make setup
```

## Project Structure

- `environment.yml`: Environment configuration file.
- `requirements.txt`: Libs needed for the project.
- `Makefile`: Create "rules" to centralize and execute main commands.
- `plpred`: Main package directory, with application functions.
- `data/`: Data directory. Raw data are saved in `data/raw`, preprocessed data in `data/processed` and trained models are saved in `data/models` (models are serialized using pickle).

