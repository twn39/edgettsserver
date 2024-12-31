## Usage


## Run
``` 
uvicorn app:app --host 0.0.0.0 --port 5000 --loop uvloop --workers 2
```

## Export package

``` 
uv pip compile pyproject.toml -o requirements.txt
```