# ghc2024-vectorization-workshop

## Set-Up

### Option 1: From your local Python3 shell:

0. Clone this repo (optionally: fork it to your github first)

```
git clone <>
```

1. Enter the directory and make your virtual environment (any Python3 version should be fine. Here I use 3.9)

```
cd ghc2024-vectorization-workshop
python3.9 -m venv venv
```

2. Activate your new virtual environment
```
source venv/bin/activate
```

3. Install required packages from the requirements.txt
```
python -m pip install -r requirements.txt
```

### Option 2: In a Google Colab Notebook

1. Open a new Google Colab Notebook (https://colab.research.google.com). You will need to be signed into your own Google account

2. copy-paste the code from `utils.py` into the first cell and run

## Writing and testing the functions

### Option 1: From your local Python3 shell:

1. Open the `q#.py` in your text editor, according to the question (q1 through q7). For the given question, put your optimized code in the `vec_*` function where it says `pass # insert your code here`.

2. To test that your function works and compare the speed (for relevent questions) by running the `test_run.py` script:

```
python test_run.py
```

Note: if you're having trouble with one function and want to skip to the next one, just use `#` to comment out that line in the `test_run.py`

If your function matches the desired output, then you should see either a "Success" message, or a printout of the timing differences.

### Option 2: In a Google Colab Notebook

1. Copy the code from the `q#.py` for your corresponding question (q1 through q7). Be sure to include the imports too, EXCEPT **do not include the line `from util import print_time_results, time_funcs`. You have already pasted these functions into your notebook during the Setup.

2. Update the `vec_*` function where it says `pass # insert your code here`.

3. Run the `test_*` function to determine if your output is satisfactory, and what the speedup is (for relevent questions). You won't use the `test_run.py` script if you're working in a Notebook; just copy-paste the `test_` functions directly and run them.

## Brag about your gains!

1. Go to the Google Form https://forms.gle/9xrjTUSEDozPm4kJ6 and report the speed-up factor you acheived for each function! We'll shout-out the biggest speed-ups live in the workshop.

