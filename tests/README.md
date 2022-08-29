# Testing workflow

Github actions and Travis are used to automate the testing workflow.

## Use the appropriate python version

You can specify the python version in the `python-auto-test.yml` file. 

If unspecified, it will take the default version in the system `PATH` 

## Dependencies

```bash
steps:
    - uses: actions/checkout@v3
    - name: Set up Python 3.10
      uses: actions/setup-python@v3
      with:
        python-version: "3.10"
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
```

## Requirements file

We can download dependencies using `requirements.txt`. Ensure pip is upgraded before this.

```bash
steps:
    - uses: actions/checkout@v3
    - name: Set up Python 3.10
      uses: actions/setup-python@v3
      with:
        python-version: "3.10"
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
```

## Testing with pytest

You can use `pytest` to run the test cases.

```bash
steps:
    - uses: actions/checkout@v3
    - name: Set up Python 3.10
      uses: actions/setup-python@v3
      with:
        python-version: "3.10"
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install flake8 pytest
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
```